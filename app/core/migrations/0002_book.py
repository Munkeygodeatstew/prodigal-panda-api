# Generated by Django 2.2.1 on 2019-06-09 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('athors', models.CharField(max_length=200)),
                ('published_date', models.CharField(max_length=50)),
                ('pages', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
    ]
