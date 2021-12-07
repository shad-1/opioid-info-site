from django.db.models.base import Model
from django.db.models.expressions import Value
from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from django.contrib.postgres import search
from .recommendations import Recommendations


from . import forms
from . import models

# Create your views here.
ctx = {'view': 'Elevated'}

def indexPageView(request):
    return render(request, 'prescriber_portal/index.html', ctx)

def searchPageView(request, entity=None):
    ctx['entity'] = entity
    ctx['queryset'] = None
    entity_queryset = None
    form = None
    result_set_limit = 25
    ENTITY_OPTIONS = ("drug", "prescriber")

    if entity not in ENTITY_OPTIONS and entity is not None:
        return redirect('search')
    #todo: throw errors on invalid form submission
    #todo: route appropriately on submission
    
    if entity == 'drug':
        form = forms.DrugForm(request.GET or None)
        entity_model = models.PdDrug
    elif entity == 'prescriber':
        form = forms.PrescriberForm(request.GET or None)
        entity_model = models.PdPrescriber
    
    #* Form Processing *#
    if form is not None and form.is_valid():
        result_size = form.cleaned_data['result_size']
        if result_size != '':
            if result_size == 'ALL':
                result_size = 10000
            result_size = int(result_size)

        if entity == 'drug':
            dname = form.cleaned_data['drugname']
            isopioid = form.cleaned_data['isopioid']
            order_by = form.cleaned_data['order_by']

            entity_queryset = models.PdDrug.objects.all()
            if dname != '':
                entity_queryset = entity_queryset.filter(drugname__icontains=dname)
            if isopioid != None:
                entity_queryset = entity_queryset.filter(isopioid=isopioid)
            
            #* Order by *#
            drug_order_by_options = {
                'DRUG_NAME': 'drugname',
                '~DRUG_NAME': '-drugname',
                '': 'drugname',
            }
            
            entity_queryset = entity_queryset.order_by(drug_order_by_options[order_by])[:result_size or result_set_limit]
            # Exclusive search
            """ vector = search.SearchVector('drugname')
            query = search.SearchQuery(f'{dname}')
            entity_queryset = entity_model.objects.annotate(rank=search.SearchRank(vector, query)).order_by('-rank').filter(isopioid=isopioid)[:10] # add filter for isOpioid match, also limit to 10 results """
      
        elif entity == 'prescriber': #maybe enable cover_density for proximity of matching phrases
            pname = form.cleaned_data['prescriber_name']
            pgender = form.cleaned_data['gender']
            pstate = form.cleaned_data['state']
            popioid = form.cleaned_data['isopioidprescriber']
            ptotal = form.cleaned_data['total_prescriptions']
            order_by = form.cleaned_data['order_by']
            
            entity_queryset = models.PdPrescriber.objects.all()

            if pname != '':
                entity_queryset = entity_queryset.exclude(~Q(fname__icontains=pname) & ~Q(lname__icontains=pname))
               
            if pgender != 'U':
                entity_queryset = entity_queryset.exclude(~Q(gender=pgender))
            if pstate != '':
                entity_queryset = entity_queryset.exclude(~Q(state=pstate))
            if popioid is not None:
                entity_queryset = entity_queryset.exclude(~Q(isopioidprescriber=popioid))
            if ptotal is not None:
                entity_queryset = entity_queryset.exclude(~Q(totalprescriptions=ptotal))

            #* order by processing *#
            prescriber_order_by_options = {
                'F_NAME' : 'fname', 
                '~F_NAME' : '-fname',
                'L_NAME' : 'lname',
                '~L_NAME' : '-lname',
                'TOTAL_PRESCRIPTIONS' : 'totalprescriptions',
                '~TOTAL_PRESCRIPTIONS' : '-totalprescriptions',
                '' : 'lname'
            }

            entity_queryset = entity_queryset.order_by(prescriber_order_by_options[order_by])[:result_size or result_set_limit]
    
        ctx['queryset'] = entity_queryset   #todo: conditions and error handling?
    
    ctx['form'] = form
    return render(request, 'prescriber_portal/search.html', ctx)
    

def detailsPageView(request, npi):
    prescriber = models.PdPrescriber.objects.get(npi=npi)

    ctx['record'] = prescriber

    ctx['recommended_drugs'] = Recommendations.recommend_drug(prescriber)

    return render(request, 'prescriber_portal/details.html', ctx)

def recommendPageView(request, entity=None):
    if entity == 'drug':

        return render(request, 'prescriber_portal/recommend_drug.html', ctx)

    elif entity == 'prescriber':
        
        return render(request, 'prescriber_portal/recommend_prescriber.html', ctx)

    else: #todo: add 404 page
        return render(request, 'prescriber_portal/index.html', ctx)
    
