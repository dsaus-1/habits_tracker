# Generated by Django 4.1.7 on 2023-03-14 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='chat_id',
            field=models.CharField(default=132, max_length=10, verbose_name='Чат ID телеграма'),
            preserve_default=False,
        ),
    ]