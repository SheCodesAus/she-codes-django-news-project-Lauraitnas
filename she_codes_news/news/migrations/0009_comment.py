# Generated by Django 4.0.1 on 2022-02-19 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_delete_snippet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('newsstory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='news.newsstory')),
            ],
        ),
    ]
