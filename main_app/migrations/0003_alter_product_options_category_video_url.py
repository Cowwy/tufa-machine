# Generated by Django 5.2 on 2025-04-19 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_product_pdf_url_product_pdf_file'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'XCMG_Termék', 'verbose_name_plural': 'XCMG_Termékek'},
        ),
        migrations.AddField(
            model_name='category',
            name='video_url',
            field=models.URLField(blank=True, null=True, verbose_name='YouTube videó URL'),
        ),
    ]
