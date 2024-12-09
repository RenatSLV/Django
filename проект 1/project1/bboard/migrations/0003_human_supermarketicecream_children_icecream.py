# Generated by Django 5.1.3 on 2024-11-20 16:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_rubric_alter_bb_options_bb_rubric'),
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('has_children', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SupermarketIceCream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('place', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Children',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bboard.human')),
            ],
        ),
        migrations.CreateModel(
            name='Icecream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('datetimeCreate', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bboard.supermarketicecream')),
            ],
        ),
    ]
