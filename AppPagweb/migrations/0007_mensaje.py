# Generated by Django 4.1.7 on 2023-03-28 02:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppPagweb', '0006_postear_creado_el_alter_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.TextField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('creado_el', models.DateTimeField(auto_now_add=True)),
                ('destinatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
