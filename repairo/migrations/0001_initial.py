# Generated by Django 2.0.5 on 2018-08-02 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=100)),
                ('vin_num', models.CharField(max_length=30)),
                ('license_plate', models.CharField(max_length=12)),
                ('serv_hist', models.TextField()),
                ('make', models.CharField(max_length=500)),
                ('model', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='repairo.Car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=13)),
                ('area_serviced', models.TextField()),
                ('invoice_num', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=500)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repairs', to='repairo.Car')),
            ],
        ),
    ]