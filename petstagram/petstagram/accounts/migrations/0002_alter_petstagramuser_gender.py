# Generated by Django 5.0.3 on 2024-04-09 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petstagramuser',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('X', 'Do not show')], max_length=1),
        ),
    ]
