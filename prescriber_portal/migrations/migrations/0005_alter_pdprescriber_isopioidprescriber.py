# Generated by Django 3.2.9 on 2021-12-05 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescriber_portal', '0004_alter_pddrug_isopioid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdprescriber',
            name='isopioidprescriber',
            field=models.IntegerField(),
        ),
    ]