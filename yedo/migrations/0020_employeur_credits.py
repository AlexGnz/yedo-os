# Generated by Django 2.2 on 2019-09-18 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yedo', '0019_achat'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeur',
            name='credits',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
