# Generated by Django 4.2.8 on 2024-01-04 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=200)),
                ('resim', models.FileField(upload_to='filmler/', verbose_name='film resmi')),
            ],
        ),
    ]
