# Generated by Django 4.0.4 on 2022-07-15 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0019_alter_boleta_boldatec_alter_boleta_boldatee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleta',
            name='bolCant',
            field=models.IntegerField(verbose_name='Cantidad de los productos'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]