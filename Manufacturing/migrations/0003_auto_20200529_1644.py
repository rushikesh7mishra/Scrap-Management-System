# Generated by Django 3.0.6 on 2020-05-29 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manufacturing', '0002_auto_20200529_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scarp_material',
            name='doc_no',
            field=models.IntegerField(),
        ),
    ]