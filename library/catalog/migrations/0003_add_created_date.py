# Generated by Django 4.1.4 on 2022-12-09 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_remove_author_date_of_birth_author_created_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='created_by',
        ),
        migrations.AddField(
            model_name='author',
            name='created_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
