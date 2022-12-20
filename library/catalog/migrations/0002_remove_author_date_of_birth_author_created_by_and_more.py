# Generated by Django 4.1.4 on 2022-12-09 03:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='author',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On Loan'), ('a', 'Available'), ('r', 'Reserved')], default='a', max_length=1),
        ),
    ]
