# Generated by Django 3.2.8 on 2021-10-09 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinefood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryAgent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=510)),
                ('adress', models.TextField()),
                ('mobile1', models.CharField(max_length=20)),
                ('mobile2', models.CharField(max_length=20)),
                ('manager_name', models.CharField(max_length=50)),
                ('deliver_Charge', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ordermenu',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]