# Generated by Django 3.1.12 on 2021-06-14 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('make', models.CharField(max_length=512)),
                ('model', models.CharField(max_length=512)),
            ],
            options={
                'unique_together': {('make', 'model')},
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rating_value', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='cars.car')),
            ],
        ),
    ]
