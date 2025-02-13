# Generated by Django 5.1.5 on 2025-02-13 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_contact_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('quantity', models.IntegerField()),
                ('slug', models.SlugField(blank=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='product/files')),
            ],
            options={
                'db_table': 'product_table',
            },
        ),
    ]
