# Generated by Django 4.2.8 on 2024-01-04 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_rename_movie_movies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=200)),
                ('resim', models.FileField(null=True, upload_to='filmler/', verbose_name='film resmi')),
                ('film', models.FileField(null=True, upload_to='film/', verbose_name='film video')),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.kategori')),
            ],
        ),
        migrations.DeleteModel(
            name='Movies',
        ),
    ]
