# Generated by Django 3.2.8 on 2021-10-09 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinefood', '0002_auto_20211010_0026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('features', models.IntegerField(choices=[(1, 'breakfast'), (2, 'launch'), (3, 'dinner'), (4, 'delivery'), (5, 'cafe'), (6, 'luxury dining'), (7, 'night life')])),
                ('timings', models.IntegerField(choices=[(1, 'monday'), (2, 'tuesday'), (3, 'wednesday'), (4, 'thursday'), (5, 'friday'), (6, 'saturday'), (7, 'sunday')])),
                ('order_quantity', models.PositiveIntegerField(default=1)),
                ('delivery_date', models.DateTimeField(auto_now_add=True)),
                ('delivery_agent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinefood.deliveryagent')),
            ],
        ),
    ]
