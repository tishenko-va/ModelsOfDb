# Generated by Django 5.1.4 on 2025-01-03 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0002_buyer_password_alter_buyer_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
