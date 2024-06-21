# Generated by Django 3.2.21 on 2023-11-05 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('pay_id', models.AutoField(primary_key=True, serialize=False)),
                ('card_holder_name', models.CharField(max_length=45)),
                ('cvv', models.CharField(max_length=45)),
                ('date', models.DateField()),
                ('amount', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'payment',
                'managed': False,
            },
        ),
    ]
