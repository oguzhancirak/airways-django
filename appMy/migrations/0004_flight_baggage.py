# Generated by Django 4.1.7 on 2023-05-22 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0003_flight_variş_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='baggage',
            field=models.IntegerField(max_length=50, null=True, verbose_name='Bagaj Ağırlığı'),
        ),
    ]