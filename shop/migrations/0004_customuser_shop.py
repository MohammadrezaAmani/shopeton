# Generated by Django 3.2.9 on 2021-11-19 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_customuser_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='shop',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.myshop'),
        ),
    ]
