# Generated by Django 3.2.9 on 2021-12-11 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_wishlist_post_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='post_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.postinfo', verbose_name='اطلاعات ارسال'),
        ),
    ]
