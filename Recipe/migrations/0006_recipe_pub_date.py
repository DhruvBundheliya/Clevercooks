# Generated by Django 3.2.6 on 2021-11-21 08:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0005_auto_20211121_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
