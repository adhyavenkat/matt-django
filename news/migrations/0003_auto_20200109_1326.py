# Generated by Django 2.2.5 on 2020-01-09 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200109_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='id',
            field=models.IntegerField(editable=False, max_length=50, primary_key=True, serialize=False),
        ),
    ]
