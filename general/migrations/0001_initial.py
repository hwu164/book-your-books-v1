# Generated by Django 4.2.1 on 2023-05-24 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bin',
            fields=[
                ('bin_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('bin_name', models.CharField(max_length=5)),
                ('def_loc', models.CharField(max_length=10)),
                ('num_books', models.SmallIntegerField()),
            ],
        ),
    ]
