# Generated by Django 5.0.6 on 2024-07-14 04:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pioneros', '0003_remove_features_content_large_image_feature_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='News_Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/newsandevent/')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('updated_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
