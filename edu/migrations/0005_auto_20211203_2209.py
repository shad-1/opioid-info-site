# Generated by Django 3.2.9 on 2021-12-03 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0004_auto_20211203_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fact',
            name='internal_resource_link',
        ),
        migrations.AddField(
            model_name='fact',
            name='internal_resource',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='edu.article', verbose_name='Internal Resource ID'),
        ),
    ]
