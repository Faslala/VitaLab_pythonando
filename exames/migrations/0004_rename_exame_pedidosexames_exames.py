# Generated by Django 5.0.4 on 2024-05-08 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exames', '0003_pedidosexames'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedidosexames',
            old_name='exame',
            new_name='exames',
        ),
    ]
