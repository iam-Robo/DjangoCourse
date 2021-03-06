# Generated by Django 3.2.3 on 2021-06-21 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='مبلغ')),
                ('transaction_time', models.DateTimeField(auto_now_add=True, verbose_name='زمان تراکنش')),
                ('transaction_code', models.CharField(max_length=30, verbose_name='رسید تراکنش')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile', verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'پرداخت',
                'verbose_name_plural': 'پرداخت',
            },
        ),
    ]
