# Generated by Django 5.0.2 on 2024-03-05 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_book_description_alter_book_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookissuanceaccounting',
            name='return_book',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
