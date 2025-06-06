# Generated by Django 5.1.6 on 2025-05-29 06:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeApp', '0003_kompilasi_slug_alter_peraturan_kategori_peraturan'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='peraturan',
            name='nama_peraturan',
            field=models.CharField(help_text='Tentang apa peraturan ini?', max_length=255),
        ),
        migrations.CreateModel(
            name='KategoriAccessUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codeApp.kategoriperaturan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Akses Kategori Peraturan',
                'verbose_name_plural': 'Akses Kategori Peraturan',
                'unique_together': {('user', 'kategori')},
            },
        ),
    ]
