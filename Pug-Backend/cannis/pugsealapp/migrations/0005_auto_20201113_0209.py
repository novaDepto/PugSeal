# Generated by Django 3.1.1 on 2020-11-13 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pugsealapp', '0004_auto_20201112_1838'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requisicion',
            options={'verbose_name_plural': 'Requisiciones'},
        ),
        migrations.AlterField(
            model_name='requisicion',
            name='enlace_concepto',
            field=models.CharField(max_length=255, null=True),
        ),
    ]