# Generated by Django 3.1.3 on 2020-11-15 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallary', '0007_auto_20201115_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='category',
        ),
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gallary.category'),
        ),
    ]
