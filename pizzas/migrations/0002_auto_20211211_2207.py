# Generated by Django 3.0.5 on 2021-12-11 22:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzas.Pizza')),
            ],
        ),
    ]
