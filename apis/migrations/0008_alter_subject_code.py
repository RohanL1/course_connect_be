# Generated by Django 4.1.7 on 2023-02-26 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0007_alter_term_end_date_alter_term_start_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='code',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]