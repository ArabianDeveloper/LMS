# Generated by Django 3.2.5 on 2021-07-13 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0005_book_pdf_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='Books'),
        ),
    ]