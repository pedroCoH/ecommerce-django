# Generated by Django 5.0.4 on 2024-05-22 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_variation_variation_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('talla', 'talla'), ('color', 'color')], max_length=100),
        ),
    ]
