# Generated by Django 2.0.5 on 2018-05-30 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('forum', '0002_auto_20180530_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
        ),
    ]
