# Generated by Django 4.1.7 on 2023-03-06 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0006_tek'),
    ]

    operations = [
        migrations.AddField(
            model_name='urun',
            name='seriNo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='urunler.tek'),
        ),
    ]
