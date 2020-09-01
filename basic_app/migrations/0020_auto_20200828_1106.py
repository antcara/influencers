# Generated by Django 3.0.3 on 2020-08-28 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0019_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='influencer',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='influencers', to='basic_app.Race'),
        ),
    ]
