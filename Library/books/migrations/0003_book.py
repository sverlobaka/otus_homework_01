# Generated by Django 5.0.2 on 2024-02-29 10:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='books.author')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='books.genre')),
            ],
            options={
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
