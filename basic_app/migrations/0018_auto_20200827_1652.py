# Generated by Django 3.0.3 on 2020-08-27 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0017_auto_20200827_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='influencer',
            name='race',
            field=models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, related_name='influencers', to='basic_app.Race'),
        ),
    ]