# Generated by Django 4.2.6 on 2023-10-31 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='web_responders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('R_name', models.CharField(max_length=100)),
                ('R_age', models.IntegerField()),
                ('R_city', models.CharField(max_length=100)),
                ('R_gender', models.CharField(max_length=50)),
                ('R_academy', models.CharField(max_length=100)),
                ('R_phone', models.CharField(max_length=100)),
                ('R_email', models.CharField(max_length=100)),
                ('R_program', models.CharField(max_length=150)),
            ],
        ),
    ]
