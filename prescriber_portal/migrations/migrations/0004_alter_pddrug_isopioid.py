# Generated by Django 3.2.9 on 2021-12-05 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescriber_portal', '0003_alter_pddrug_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pddrug',
            name='isopioid',
            field=models.BooleanField(),
        ),
    ]