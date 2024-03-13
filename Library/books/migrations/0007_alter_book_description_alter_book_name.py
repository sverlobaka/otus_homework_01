# Generated by Django 5.0.2 on 2024-03-01 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_bookissuanceaccounting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
