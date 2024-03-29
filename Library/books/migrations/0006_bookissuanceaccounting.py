# Generated by Django 5.0.2 on 2024-02-29 10:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_reader'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookIssuanceAccounting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_issue', models.DateField(auto_now_add=True)),
                ('return_date', models.DateField()),
                ('return_book', models.BooleanField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('copy_book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='books.copybook')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='readers', to='books.reader')),
            ],
            options={
                'verbose_name_plural': 'Учет выдачи книг',
            },
        ),
    ]
