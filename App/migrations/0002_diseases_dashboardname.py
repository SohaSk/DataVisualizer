# Generated by Django 4.2.7 on 2023-12-07 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diseases',
            name='dashboardName',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
