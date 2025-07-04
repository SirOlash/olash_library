# Generated by Django 5.2.1 on 2025-06-17 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_book_author_alter_genre_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(choices=[('R', 'ROMANCE'), ('C', 'COMEDY'), ('P', 'POLITICS'), ('F', 'FINANCE')], default='F', max_length=1, unique=True),
        ),
    ]
