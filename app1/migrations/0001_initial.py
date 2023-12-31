# Generated by Django 4.2.1 on 2023-06-20 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('c_id', models.IntegerField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=100)),
                ('s_paid', models.IntegerField()),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.courses')),
            ],
        ),
    ]
