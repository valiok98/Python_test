# Generated by Django 2.0.3 on 2018-03-22 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_auto_20180322_1505'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_image',
            new_name='item_link',
        ),
        migrations.AlterField(
            model_name='item',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prof', to='Profile.PersonalProfile'),
        ),
    ]