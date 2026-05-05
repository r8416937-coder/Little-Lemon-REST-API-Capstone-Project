# Generated for Little Lemon Capstone Project
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('reservation_date', models.DateField()),
                ('reservation_slot', models.SmallIntegerField()),
            ],
            options={
                'ordering': ['reservation_date', 'reservation_slot'],
                'unique_together': {('reservation_date', 'reservation_slot')},
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('inventory', models.SmallIntegerField(default=0)),
            ],
        ),
    ]
