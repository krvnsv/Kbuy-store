# Generated by Django 5.1.5 on 2025-02-14 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_customer_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['user__first_name', 'user__last_name'], 'permissions': [('view_history', 'Can view history')]},
        ),
    ]
