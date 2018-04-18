# Generated by Django 2.0.3 on 2018-04-12 22:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_user_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ethnicity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ethnicity', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Ethnicity',
                'verbose_name_plural': 'Ethnicities',
            },
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Race',
                'verbose_name_plural': 'Races',
            },
        ),
        migrations.CreateModel(
            name='UserRaceEthnicity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other', models.CharField(blank=True, max_length=255, null=True)),
                ('ethnicity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Ethnicity')),
                ('race', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Race')),
            ],
            options={
                'verbose_name': 'UserRaceEthnicity',
                'verbose_name_plural': 'UserRaceEthnicities',
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.AddField(
            model_name='user',
            name='locations',
            field=models.ManyToManyField(blank=True, limit_choices_to=models.Q(('type', 'H'), ('type', 'W'), _connector='OR'), to='location.Location'),
        ),
        migrations.AddField(
            model_name='userraceethnicity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ethnicity',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Race'),
        ),
    ]
