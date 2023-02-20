# Generated by Django 4.1.7 on 2023-02-20 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sneaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('style', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
