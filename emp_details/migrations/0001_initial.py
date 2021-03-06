# Generated by Django 2.0.5 on 2019-01-29 15:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(default=uuid.UUID('f66f7180-bfd4-46b2-9ff2-d4055815521b'), max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp_details.Employee'),
        ),
    ]
