# Generated by Django 4.1.7 on 2023-02-26 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0008_alter_subject_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='code',
            field=models.CharField(max_length=255),
        ),
    ]