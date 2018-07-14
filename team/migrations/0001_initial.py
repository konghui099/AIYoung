# Generated by Django 2.0.6 on 2018-07-14 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('experience_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('experience_name', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('main_task', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('staff_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name_en', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('title', models.CharField(choices=[('Mr', 'Mr.'), ('Mrs', 'Mrs.'), ('Miss', 'Miss'), ('Dr', 'Dr.'), ('Prof', 'Prof.'), ('A_Prof', 'A/Prof.')], default='Mr', max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(blank=True, max_length=20)),
                ('biograph', models.TextField(blank=True)),
                ('research_interests', models.TextField()),
                ('photo', models.ImageField(upload_to='member/img/')),
                ('abstract', models.TextField(blank=True)),
                ('position', models.CharField(blank=True, max_length=250)),
                ('experience_list', models.ManyToManyField(blank=True, help_text='Select the experience for this member', to='team.Experience')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('publication_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('abstract', models.TextField(blank=True)),
                ('year', models.IntegerField()),
                ('venue_name', models.CharField(max_length=500)),
                ('publication_type', models.CharField(choices=[('conf', 'conference'), ('jour', 'journal'), ('patn', 'patent')], max_length=4)),
                ('authors', models.TextField()),
                ('volume', models.CharField(blank=True, max_length=20)),
                ('number_v', models.CharField(blank=True, max_length=20)),
                ('page_v', models.CharField(blank=True, max_length=20)),
                ('source_code', models.FileField(blank=True, upload_to='codes/')),
                ('manuscript', models.FileField(blank=True, upload_to='manuscript/')),
                ('demo_link', models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='publication_list',
            field=models.ManyToManyField(blank=True, help_text='Select the publication for this member', to='team.Publication'),
        ),
    ]
