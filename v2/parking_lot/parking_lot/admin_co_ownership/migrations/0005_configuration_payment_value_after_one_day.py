# Generated by Django 4.2.11 on 2024-05-03 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_co_ownership', '0004_alter_parkingplace_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='payment_value_after_one_day',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=10, verbose_name='Valor extra a cobrar después de un dia de uso'),
            preserve_default=False,
        ),
    ]