# Generated by Django 3.2.5 on 2021-07-15 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0006_alter_book_pdf_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]