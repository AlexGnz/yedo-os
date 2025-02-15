# Generated by Django 2.2 on 2019-09-30 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yedo', '0031_auto_20190926_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='jobs_wanted',
            field=models.ManyToManyField(blank=True, null=True, to='yedo.JobType'),
        ),
        migrations.AlterField(
            model_name='student',
            name='jours_dispo',
            field=models.ManyToManyField(blank=True, null=True, to='yedo.JourDispo'),
        ),
        migrations.AlterField(
            model_name='student',
            name='notes',
            field=models.ManyToManyField(blank=True, null=True, to='yedo.Rating'),
        ),
    ]
