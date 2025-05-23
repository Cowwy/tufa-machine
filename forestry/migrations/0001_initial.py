# Generated by Django 5.2 on 2025-04-19 08:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ForestryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_hu', models.CharField(max_length=100, verbose_name='Kategória neve (HU)')),
                ('name_sk', models.CharField(max_length=100, verbose_name='Kategória neve (SK)')),
                ('order', models.IntegerField(default=0, verbose_name='Sorrend')),
            ],
            options={
                'verbose_name': 'Erdészeti Gépkategória',
                'verbose_name_plural': 'Erdészeti Gépkategóriák',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ForestryProduct',
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
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='forestry/pdfs/', verbose_name='PDF Fájl')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='forestry.forestrycategory', verbose_name='Kategória')),
            ],
            options={
                'verbose_name': 'Erdészeti Gép',
                'verbose_name_plural': 'Erdészeti Gépek',
                'ordering': ['category__order', 'name_hu'],
            },
        ),
        migrations.CreateModel(
            name='ForestryProductFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_hu', models.CharField(max_length=255, verbose_name='Jellemző (HU)')),
                ('feature_sk', models.CharField(max_length=255, verbose_name='Jellemző (SK)')),
                ('order', models.IntegerField(default=0, verbose_name='Sorrend')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='forestry.forestryproduct', verbose_name='Termék')),
            ],
            options={
                'verbose_name': 'Erdészeti Gép Jellemző',
                'verbose_name_plural': 'Erdészeti Gép Jellemzők',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ForestryProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='forestry/pics/', verbose_name='Kép')),
                ('order', models.IntegerField(default=0, verbose_name='Sorrend')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='forestry.forestryproduct', verbose_name='Termék')),
            ],
            options={
                'verbose_name': 'Erdészeti Gép Kép',
                'verbose_name_plural': 'Erdészeti Gép Képek',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ForestryProductSpec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spec_hu', models.CharField(max_length=255, verbose_name='Műszaki adat (HU)')),
                ('spec_sk', models.CharField(max_length=255, verbose_name='Műszaki adat (SK)')),
                ('order', models.IntegerField(default=0, verbose_name='Sorrend')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tech_specs', to='forestry.forestryproduct', verbose_name='Termék')),
            ],
            options={
                'verbose_name': 'Erdészeti Gép Műszaki Adat',
                'verbose_name_plural': 'Erdészeti Gép Műszaki Adatok',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ForestryProductWhyChoose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason_hu', models.CharField(max_length=255, verbose_name='Ok (HU)')),
                ('reason_sk', models.CharField(max_length=255, verbose_name='Ok (SK)')),
                ('order', models.IntegerField(default=0, verbose_name='Sorrend')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='why_choose', to='forestry.forestryproduct', verbose_name='Termék')),
            ],
            options={
                'verbose_name': 'Erdészeti Gép Miért Válassza',
                'verbose_name_plural': 'Erdészeti Gép Miért Válassza Okok',
                'ordering': ['order'],
            },
        ),
    ]
