# Generated by Django 5.0.7 on 2024-07-16 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='application',
            name='student_number',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
