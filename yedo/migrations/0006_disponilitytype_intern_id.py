# Generated by Django 2.2 on 2019-09-16 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yedo', '0005_auto_20190916_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='disponilitytype',
            name='intern_id',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
