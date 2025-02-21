# Generated by Django 4.2 on 2025-01-11 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('ACTION', 'Acción'), ('COMEDY', 'Comedia'), ('DRAMA', 'Drama'), ('HORROR', 'Terror'), ('SCI-FI', 'Ciencia Ficción'), ('ROMANCE', 'Romance')], max_length=50)),
                ('director', models.CharField(max_length=100)),
                ('release_year', models.IntegerField()),
                ('synopsis', models.TextField()),
            ],
        ),
    ]
