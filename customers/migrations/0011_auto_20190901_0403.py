# Generated by Django 2.2.3 on 2019-09-01 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0010_auto_20190831_1516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='qty',
            new_name='total_qty',
        ),
        migrations.RemoveField(
            model_name='order',
            name='item',
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=0)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Item')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Order')),
            ],
        ),
    ]