# Generated by Django 3.2.5 on 2021-07-13 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0002_book_total_rental'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(blank=True, choices=[('متاح', 'availbel'), ('rental', 'rental'), ('solid', 'solid')], max_length=50, null=True),
        ),
    ]