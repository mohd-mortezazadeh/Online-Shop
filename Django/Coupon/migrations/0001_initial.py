# Generated by Django 3.2 on 2021-04-19 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=250, verbose_name='کد')),
                ('percent', models.IntegerField(verbose_name='درصد تخفیف')),
                ('uses_number', models.IntegerField(default=1, verbose_name='تعداد قابل استفاده')),
                ('expiration', models.CharField(max_length=50, verbose_name='تاریخ انقضا')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
            ],
            options={
                'verbose_name': 'کد تخفیف',
                'verbose_name_plural': 'کد تخفیف ها',
            },
        ),
    ]