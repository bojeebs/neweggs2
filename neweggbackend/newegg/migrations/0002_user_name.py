# Generated by Django 4.2 on 2023-04-14 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newegg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='no name', max_length=255, null=True),
        ),
    ]
