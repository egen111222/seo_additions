# Generated by Django 3.1.14 on 2023-05-20 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seo', '0002_seoaddition_tags'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SeoTag',
            new_name='SeoKeyWord',
        ),
        migrations.RenameField(
            model_name='seokeyword',
            old_name='tag',
            new_name='keyword',
        ),
    ]
