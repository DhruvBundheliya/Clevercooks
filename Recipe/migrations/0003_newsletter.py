# Generated by Django 3.2.6 on 2021-11-25 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0002_alter_recipe_coverimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailaddress', models.EmailField(max_length=254)),
            ],
        ),
    ]
