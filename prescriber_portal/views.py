from django.conf.urls import url
from django.core.exceptions import ValidationError
from django.db.models.base import Model
from django.db.models.expressions import Value
from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from django.contrib.postgres import search
from .recommendations import Recommendations
from django.db import connection
from random import random
# from fall2021.prescriptions.prescribeless.prescriber_portal import recommendations

from .predictions import Predictions
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
            pspecialty = form.cleaned_data['specialty']
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
            if pspecialty != '':
                entity_queryset = entity_queryset.exclude(~Q(specialty__icontains=pspecialty))
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
    

def detailsPageView(request, entity, id):
    if entity == 'prescriber':
        prescriber = models.PdPrescriber.objects.get(npi=id)
        ctx['record'] = prescriber
        ctx['recommended_drugs'] = Recommendations.recommend_drug(prescriber)
        #list average stores the average for every drug
        listaverage = []
        #list drugid stores the drug id for every durg
        listdrugid = []
        #listdispalydrugid stores the drug id for a given npi
        listdisplaydrugid = []
        #listdisplayquantity stores the quantity for a given npi in order of drug id
        listdisplayquantity = []
        #listdrugname stores the name of all drugs, listlistplace is used to know which names to use
        listdrugname = []
        #listdisplayname stores the name for a drug given a drug id
        listdisplayname = []
        #listlistplace stores the list place of the drug id for to determine which averages to use
        listlistplace = []
        #listdisplayaverage stores the averages to be displayed
        listdisplayaverage = []
        with connection.cursor() as cursor:
            cursor.execute("select avg(quantity) as aq from pd_prescriptionquantity group by drugid order by drugid", [id])
            row = cursor.fetchall()
            listdisplayaverage = list(row)
        with connection.cursor() as cursor:
            cursor.execute("select drugid from pd_prescriptionquantity where npi = %s order by drugid", [id])
            row = cursor.fetchall()
            listdisplaydrugid = list(row)
        with connection.cursor() as cursor:
            cursor.execute("select quantity from pd_prescriptionquantity where npi = %s order by drugid", [id])
            row = cursor.fetchall()
            listdisplayquantity = list(row)
        with connection.cursor() as cursor:
            cursor.execute("select drugname from pd_drug order by drugid")
            row = cursor.fetchall()
            listdrugname = list(row)

        # for getdrugname in range(0,len(listdisplaydrugid)):
        #     for getname in range(0,len(listdisplayaverage)):
        #         if listdisplaydrugid[getdrugname] == listdrugid[getname]:
        #             listdisplaydrugname.append(listdrugname[getname])
        #             listprintaverage.append(listdisplayaverage[getname])
        listdisplaydrugname = []
        listprintaverage = []

        #create a numerical version of the drug id
        listnumericdrugid = []
        for numberloop in range(0,len(listdisplaydrugid)):
            sstring = "".join(str(listdisplaydrugid[numberloop]))
            sstring = sstring[1:]
            for ttwo in range(0,2):
                sstring = sstring[:-1]
            listnumericdrugid.append(int(sstring))

        for createdrugname in range(0,len(listnumericdrugid)):
            listdisplaydrugname.append(listdrugname[listnumericdrugid[createdrugname]-2])
            listprintaverage.append(listdisplayaverage[listnumericdrugid[createdrugname]-2])

        #NOW TO FORMAT THE LISTS PROPERLY
        printlistdrugname = []
        printlistquantity = []
        printlistaverage = []
        splaceholder = ""
        for lastloop in range(0,len(listdisplaydrugname)):
            #edit the name
            splaceholder = "".join(str(listdisplaydrugname[lastloop]))
            for cutnamefront in range(0, 1):
                splaceholder = splaceholder[1:]
            for cutnameback in range(0,2):
                splaceholder = splaceholder[:-1]
            printlistdrugname.append(splaceholder)
            #edit the quantity
            splaceholder = ""
            splaceholder = "" .join(str(listdisplayquantity[lastloop]))
            for cutnumberfront in range(0,1):
                splaceholder = splaceholder[1:]
            for cutnumberback in range(0,2):
                splaceholder = splaceholder[:-1]
            printlistquantity.append(splaceholder)
            #edit the average
            splaceholder = ""
            splaceholder = "".join(str(listprintaverage[lastloop]))
            for cutaveragefront in range(0,9):
                splaceholder = splaceholder[1:]
            for cutaverageback in range(0,3):
                splaceholder = splaceholder[:-1]
            #convert to double and round
            printlistaverage.append(splaceholder)


        ctx['drugname'] = printlistdrugname
        ctx['quantity'] = printlistquantity
        ctx['average'] = printlistaverage

    elif entity == 'drug':
        drug = models.PdDrug.objects.get(drugid=id)
        ctx['record'] = drug
        ctx['recommended_prescribers'] = []#Recommendations.recommend_prescriber(drug)
        pqdrug = models.PdPrescriptionquantity.objects.filter(drugid=id)
        total = 0
        for item in pqdrug:
            total += item.quantity

        top_ten = models.PdPrescriptionquantity.objects.raw("SELECT npi, drugid, quantity FROM pd_prescriptionquantity WHERE drugid = %s ORDER BY quantity DESC LIMIT 10" , [drug.drugid])
        ctx['querito'] = []
        for obj in top_ten:
            id = obj.npi
            ctx['querito'].append(models.PdPrescriber.objects.get(npi=id))
    
        ctx['total_prescriptions'] = total
    return render(request, 'prescriber_portal/details.html', ctx)

def recommendPageView(request, entity=None):
    if entity == 'drug':

        return render(request, 'prescriber_portal/recommend_drug.html', ctx)

    elif entity == 'prescriber':
        
        return render(request, 'prescriber_portal/recommend_prescriber.html', ctx)

    else: #todo: add 404 page
        return render(request, 'prescriber_portal/index.html', ctx)

def PredTotPrescPageView(request):
    if request.method == 'POST':
        form = forms.TotPrescPredForm(request.POST)
        if form.is_valid():
            state = form.cleaned_data['state']
            gender = form.cleaned_data['gender']
            isopioidprescriber = form.cleaned_data['isopioidprescriber']
            credential = form.cleaned_data['credential']
            specialty = form.cleaned_data['specialty']
            ctx['predicted_totalprescriptions'] = Predictions.totalprescriptions(state, gender, isopioidprescriber, credential, specialty)
    else:
        form = forms.TotPrescPredForm()

    ctx['form'] = form
    
    return render(request, 'prescriber_portal/predict_tot_presc.html', ctx)

def PredPrescOp(request):
    if request.method == 'POST':
        form = forms.PredPrescOp(request.POST)
        if form.is_valid():
            state = form.cleaned_data['state']
            gender = form.cleaned_data['gender']
            totalprescriptions = form.cleaned_data['totalprescriptions']
            specialty = form.cleaned_data['specialty']
            if specialty == '': form.add_error('specialty')
            ctx['predicted_opioidprescription'] = Predictions.predict_opioid(state, gender, totalprescriptions, specialty)
    else:
        form = forms.PredPrescOp()

    ctx['form'] = form
    
    return render(request, 'prescriber_portal/predprescop.html', ctx)

def showPrescribersPageView(request):
    ctx['record'] = models.PdPrescriber.objects.all()
    ctx['record'] = ctx['record'][:100]

    return render(request, 'prescriber_portal/showprescribers.html', ctx)

def updatePrescriberPageView(request, npi):
    prescriber = models.PdPrescriber.objects.get(npi=npi)
    form = forms.PrescriberCrud()
    if request.method == 'POST':
        
        form = forms.PrescriberCrud(request.POST)
        if form.is_valid():
            prescriber.fname = form.cleaned_data['fname']
            prescriber.lname = form.cleaned_data['lname']
            prescriber.gender = form.cleaned_data['gender']
            prescriber.state = form.cleaned_data['state']
            prescriber.specialty = form.cleaned_data['specialty']
            prescriber.isopioidprescriber = form.cleaned_data['isopioidprescriber']
            prescriber.totalprescriptions = form.cleaned_data['totalprescriptions']
            prescriber.save()

        return showPrescribersPageView(request)
    else:
    
        ctx['form'] = form = forms.PrescriberCrud({'npi':prescriber.npi, 'fname':prescriber.fname, 'lname':prescriber.lname, 'gender':prescriber.gender, 'state':prescriber.state.stateabbrev, 'specialty':prescriber.specialty, 'isopioidprescriber':prescriber.isopioidprescriber, 'totalprescriptions':prescriber.totalprescriptions})
        return render(request, 'prescriber_portal/editprescriber.html', ctx)
    

def deletePrescriberPageView(request, npi):
    prescriber = models.PdPrescriber.objects.get(npi=npi)

    prescriber.delete()

    return redirect(showPrescribersPageView)

def addPrescriberPageView(request):
    if request.method == 'POST':
        prescriber = models.PdPrescriber()
        form = forms.PrescriberCrud(request.POST)
        if form.is_valid():
            prescriber.npi =  random()*1000000000
            prescriber.fname = form.cleaned_data['fname']
            prescriber.lname = form.cleaned_data['lname']
            prescriber.gender = form.cleaned_data['gender']
            if(prescriber.gender == 'U'): 
                raise ValidationError('Please choose a gender')
            prescriber.state = models.PdStatedata.objects.get(stateabbrev=form.cleaned_data['state'])
            prescriber.specialty = form.cleaned_data['specialty']
            if(prescriber.specialty == ''): 
                raise ValidationError('Please choose a specialty')
            prescriber.isopioidprescriber = form.cleaned_data['isopioidprescriber']
            if(prescriber.isopioidprescriber == None): 
                raise ValidationError('Please choose an opioid prescription status')
            prescriber.totalprescriptions = form.cleaned_data['totalprescriptions']

            prescriber.save()

        return redirect(showPrescribersPageView)
    else:
        form = forms.PrescriberCrud(request.GET or None)

        ctx['form'] = form
        return render(request, 'prescriber_portal/addprescriber.html', ctx)