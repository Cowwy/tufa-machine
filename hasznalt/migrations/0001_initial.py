# Generated by Django 5.2 on 2025-04-21 05:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HasznaltCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_hu', models.CharField(max_length=100, verbose_name='Kategória neve (HU)')),
                ('name_sk', models.CharField(max_length=100, verbose_name='Kategória neve (SK)')),
                ('order', models.IntegerField(default=0, verbose_name='Sorrend')),
            ],
            options={
                'verbose_name': 'Használt Gép Kategória',
                'verbose_name_plural': 'Használt Gép Kategóriák',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='HasznaltProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_hu', models.CharField(max_length=200, verbose_name='Termék neve (HU)')),
                ('name_sk', models.CharField(max_length=200, verbose_name='Termék neve (SK)')),
                ('intro_hu', models.TextField(blank=True, verbose_name='Bevezető szöveg (HU)')),
                ('intro_sk', models.TextField(blank=True, verbose_name='Bevezető szöveg (SK)')),
                ('closing_text_hu', models.TextField(blank=True, verbose_name='Záró szöveg (HU)')),
                ('closing_text_sk', models.TextField(blank=True, verbose_name='Záró szöveg (SK)')),
                ('pdf_link_text_hu', models.CharField(default='Leírás itt!', max_length=100, verbose_name='PDF link szövege (HU)')),
                ('pdf_link_text_sk', models.CharField(default='[SK] Popis tu!', max_length=100, verbose_name='PDF link szövege (SK)')),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='hasznalt/pdfs/', verbose_name='PDF Fájl')),
                ('video_url', models.URLField(blank=True, null=True, verbose_name='YouTube videó URL')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='hasznalt.hasznaltcategory', verbose_name='Kategória')),
            ],
            options={
                'verbose_name': 'Használt Gép',
                'verbose_name_plural': 'Használt Gépek',
                'ordering': ['category__order', 'name_hu'],
            },
        ),
        migrations.CreateModel(
            name='HasznaltProductFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_hu', models.CharField(max_length=255, verbose_name='Jellemző (HU)')),
                ('feature_sk', models.CharField(max_length=255, verbose_name='Jellemző (SK)')),
                ('order', models.IntegerField(default=0, verbose_name='Sorrend')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='hasznalt.hasznaltproduct', verbose_name='Termék')),
            ],
            options={
                'verbose_name': 'Használt Gép Jellemző',
                'verbose_name_plural': 'Használt Gép Jellemzők',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='HasznaltProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='hasznalt/pics/', verbose_name='Kép')),
                ('order', models.IntegerField(default=0, verbose_name='Sorrend')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='hasznalt.hasznaltproduct', verbose_name='Termék')),
            ],
            options={
                'verbose_name': 'Használt Gép Kép',
                'verbose_name_plural': 'Használt Gép Képek',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='HasznaltProductSpec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spec_hu', models.CharField(max_length=255, verbose_name='Műszaki adat (HU)')),
                ('spec_sk', models.CharField(max_length=255, verbose_name='Műszaki adat (SK)')),
                ('order', models.IntegerField(default=0, verbose_name='Sorrend')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tech_specs', to='hasznalt.hasznaltproduct', verbose_name='Termék')),
            ],
            options={
                'verbose_name': 'Használt Gép Műszaki Adat',
                'verbose_name_plural': 'Használt Gép Műszaki Adatok',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='HasznaltProductWhyChoose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason_hu', models.CharField(max_length=255, verbose_name='Ok (HU)')),
                ('reason_sk', models.CharField(max_length=255, verbose_name='Ok (SK)')),
                ('order', models.IntegerField(default=0, verbose_name='Sorrend')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='why_choose', to='hasznalt.hasznaltproduct', verbose_name='Termék')),
            ],
            options={
                'verbose_name': 'Használt Gép Miért Válassza',
                'verbose_name_plural': 'Használt Gép Miért Válassza Okok',
                'ordering': ['order'],
            },
        ),
    ]
