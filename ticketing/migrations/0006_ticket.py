# Generated by Django 3.2.3 on 2021-06-12 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_balance'),
        ('ticketing', '0005_alter_cinema_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_count', models.IntegerField(verbose_name='تعداد صندلی')),
                ('order_time', models.DateTimeField(auto_now_add=True, verbose_name='زمان خرید')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.profile', verbose_name='خریدار')),
                ('showtime', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketing.showtime', verbose_name='سانس')),
            ],
            options={
                'verbose_name': 'بلیط',
                'verbose_name_plural': 'بلیط',
            },
        ),
    ]
