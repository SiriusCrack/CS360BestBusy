# Generated by Django 4.0.3 on 2022-04-18 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_brands_brand_rename_displaytypes_displaytype_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='displaySize',
            field=models.IntegerField(default=27),
            preserve_default=False,
        ),
    ]
