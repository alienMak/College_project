# Generated by Django 4.1.3 on 2022-11-30 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='color1',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='accounts',
            name='color2',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='accounts',
            name='color3',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='accounts',
            name='color4',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
