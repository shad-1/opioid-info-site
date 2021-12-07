# Generated by Django 3.2.9 on 2021-12-02 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0002_auto_20211202_0533'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='organization',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='preview_text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='publication_type',
            field=models.CharField(choices=[('Article', 'Article'), ('Blog', 'Blog')], max_length=20),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]