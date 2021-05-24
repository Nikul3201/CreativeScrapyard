# Generated by Django 3.1.4 on 2021-03-03 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0010_auto_20210303_1451'),
        ('Payments', '0002_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='order_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='Order.tbl_orders_mst'),
            preserve_default=False,
        ),
    ]