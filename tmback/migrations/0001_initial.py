# Generated by Django 4.0.3 on 2022-04-21 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=50)),
                ('company_address', models.CharField(max_length=100)),
                ('company_number', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('category_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tmback.category')),
                ('company_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tmback.company')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('order_detail', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tmback.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=30)),
                ('customer_number', models.IntegerField()),
                ('customer_address', models.CharField(max_length=100)),
                ('date_ordered', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[['P', 'Pending'], ['O', 'Ongoing'], ['D', 'Done']], max_length=1)),
                ('company_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tmback.company')),
                ('order_detail_id', models.ManyToManyField(to='tmback.orderdetail')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_delivered', models.DateTimeField(auto_now=True)),
                ('company_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tmback.company')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tmback.order')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='company_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tmback.company'),
        ),
    ]
