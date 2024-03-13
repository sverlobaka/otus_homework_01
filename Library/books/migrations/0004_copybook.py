# Generated by Django 5.0.2 on 2024-02-29 10:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='CopyBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
            options={
                'verbose_name_plural': 'Экземпляры книг',
            },
        ),
    ]
