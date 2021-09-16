# Generated by Django 2.1.2 on 2018-10-20 16:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0065_auto_20181017_1346"),
        ("checkout", "0015_auto_20181017_1346"),
        ("payment", "0002_transfer_payment_to_payment_method"),
    ]

    operations = [
        migrations.RenameModel(old_name="PaymentMethod", new_name="Payment"),
        migrations.RenameField(
            model_name="transaction", old_name="payment_method", new_name="payment"
        ),
        migrations.AlterField(
            model_name="payment",
            name="checkout",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="payments",
                to="checkout.Cart",
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="order",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="payments",
                to="order.Order",
            ),
        ),
    ]
