# Generated by Django 5.0.4 on 2024-05-20 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_variation_variation_category_reviewrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('color', 'color'), ('talla', 'talla')], max_length=100),
        ),
    ]
