# Generated by Django 2.0.6 on 2018-07-11 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('staff_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('en_name', models.CharField(max_length=250)),
                ('cn_name', models.CharField(max_length=250)),
                ('abstract', models.TextField()),
                ('position', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='member/')),
                ('department', models.CharField(max_length=250)),
            ],
        ),
    ]