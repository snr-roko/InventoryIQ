# Generated by Django 5.1.1 on 2024-10-12 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('storages', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='storestock',
            unique_together={('stock_code', 'store')},
        ),
        migrations.AlterUniqueTogether(
            name='warehousestock',
            unique_together={('stock_code', 'warehouse')},
        ),
        migrations.RemoveField(
            model_name='storestock',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='warehousestock',
            name='supplier',
        ),
        migrations.AddField(
            model_name='storestock',
            name='supplier',
            field=models.ManyToManyField(blank=True, related_name='store_stocks', to='storages.supplier'),
        ),
        migrations.AddField(
            model_name='warehousestock',
            name='supplier',
            field=models.ManyToManyField(blank=True, related_name='warehouse_stocks', to='storages.supplier'),
        ),
    ]
