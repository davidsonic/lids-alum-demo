# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 07:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('wagtailimages', '0018_remove_rendition_filter'),
    ]

    operations = [
        migrations.CreateModel(
            name='BreadIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Bread ingredients',
            },
        ),
        migrations.CreateModel(
            name='BreadPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('introduction', models.TextField(blank=True, help_text='Text to describe the page')),
                ('body', wagtail.core.fields.StreamField((('heading_block', wagtail.core.blocks.StructBlock((('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))))), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))))), ('block_quote', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.TextBlock()), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Guy Picciotto', required=False))))), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', template='blocks/embed_block.html'))), blank=True, verbose_name='Page body')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='BreadsIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('introduction', models.TextField(blank=True, help_text='Text to describe the page')),
                ('body', wagtail.core.fields.StreamField((('heading_block', wagtail.core.blocks.StructBlock((('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))))), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))))), ('block_quote', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.TextBlock()), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Guy Picciotto', required=False))))), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', template='blocks/embed_block.html'))), blank=True, verbose_name='Page body')),
                ('image', models.ForeignKey(blank=True, help_text='Landscape mode only; horizontal width between 1000px and 3000px.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='BreadType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Bread types',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Countries of Origin',
            },
        ),
        migrations.AddField(
            model_name='breadpage',
            name='bread_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='breads.BreadType'),
        ),
        migrations.AddField(
            model_name='breadpage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Landscape mode only; horizontal width between 1000px and 3000px.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='breadpage',
            name='ingredients',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='breads.BreadIngredient'),
        ),
        migrations.AddField(
            model_name='breadpage',
            name='origin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='breads.Country'),
        ),
    ]
