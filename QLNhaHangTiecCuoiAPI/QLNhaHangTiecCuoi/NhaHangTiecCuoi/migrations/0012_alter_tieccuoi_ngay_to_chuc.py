# Generated by Django 4.0.4 on 2022-05-15 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NhaHangTiecCuoi', '0011_alter_tieccuoi_menu_alter_tieccuoi_sanh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tieccuoi',
            name='ngay_to_chuc',
            field=models.DateTimeField(),
        ),
    ]
