# Generated by Django 5.0.4 on 2024-05-09 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exames', '0005_acessomedico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acessomedico',
            name='token',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
