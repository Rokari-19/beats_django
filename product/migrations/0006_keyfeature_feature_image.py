# Generated by Django 5.0.3 on 2024-03-29 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_key_features_delete_productkeyfeature'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyfeature',
            name='feature_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
