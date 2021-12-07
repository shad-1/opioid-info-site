# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models.fields import TextField
from django_quill.fields import QuillField

class Author(models.Model):
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    organization = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        elif self.first_name:
            return self.first_name
        else: 
            return self.organization


PUBLICATION_TYPE = (('Article' , 'Article'), ('Blog','Blog'), ('Local Resource', 'Local Resource'))

class Article(models.Model):

    def preview_img_path(instance, filename):
        return './prescribeless/prescribeless/static/img/preview_img/{0}.jpeg'.format(instance.id)

    title = models.CharField(max_length=255, unique=True)
    body = QuillField()
    pub_date = models.DateTimeField(auto_now_add=True, serialize=True)
    author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.CASCADE)
    publication_type = models.CharField(max_length=20, choices=PUBLICATION_TYPE)
    preview_text = models.CharField(max_length=255, blank=True, null=True)
    preview_img = models.ImageField(upload_to=preview_img_path, blank=True, null=True)

    def __str__(self):
        return self.title

class Fact(models.Model):
    title = models.CharField(max_length=255, unique=True)
    body = QuillField()
    date_modified = models.DateTimeField(auto_now=True, serialize=True)
    internal_resources = models.ManyToManyField(Article, blank=True)
    external_resource_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Quote(models.Model):
    author = models.CharField(max_length=255)
    quote = TextField()
    date_modified = models.DateTimeField(auto_now=True, serialize=True)
    internal_resources = models.ManyToManyField(Article, blank=True)
    external_resource_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.author