# Generated by Django 4.0.4 on 2022-05-02 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_mprice_product_m_price_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default=False, max_length=800),
        ),
    ]