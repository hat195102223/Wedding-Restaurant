# Generated by Django 4.0.4 on 2022-05-09 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NhaHangTiecCuoi', '0006_alter_sanh_loai'),
    ]

    operations = [
        migrations.CreateModel(
            name='DichVu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('ten', models.CharField(max_length=100)),
                ('gia', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='menu',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='menus/%Y/%m'),
        ),
    ]
