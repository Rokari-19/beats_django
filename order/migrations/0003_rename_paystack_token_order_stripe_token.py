# Generated by Django 5.0.3 on 2024-04-12 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_rename_stripe_token_order_paystack_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='paystack_token',
            new_name='stripe_token',
        ),
    ]
