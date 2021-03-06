# Generated by Django 4.0.5 on 2022-06-27 07:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planName', models.CharField(max_length=255)),
                ('amountOptions', models.JSONField(default='[5000, 10000, 20000]')),
                ('tenureOption', models.JSONField(default='[1, 2, 3]')),
                ('benefitPercentage', models.IntegerField()),
                ('benefitType', models.CharField(default='Cashback', max_length=255)),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('updatedOn', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Promotions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiresAt', models.DateTimeField(default=datetime.date(2023, 5, 4), null=True)),
                ('countLeft', models.IntegerField(null=True)),
                ('promotionType', models.CharField(max_length=255)),
                ('promotionBenefitPercentage', models.IntegerField()),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('updatedOn', models.DateTimeField(auto_now_add=True)),
                ('planId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.plan')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerGoals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=255)),
                ('selectedAmount', models.IntegerField()),
                ('selectedTenure', models.IntegerField()),
                ('startedDate', models.DateTimeField(auto_now_add=True)),
                ('depositedAmount', models.IntegerField()),
                ('benefitPercentage', models.IntegerField()),
                ('benefitType', models.CharField(max_length=255)),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('updatedOn', models.DateTimeField(auto_now_add=True)),
                ('planId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.plan')),
            ],
        ),
    ]
