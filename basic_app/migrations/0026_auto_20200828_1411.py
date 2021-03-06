# Generated by Django 3.0.3 on 2020-08-28 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0025_auto_20200828_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='influencer',
            name='gender',
            field=models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='influencers', to='basic_app.Gender'),
        ),
        migrations.AlterField(
            model_name='influencer',
            name='location',
            field=models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='influencers', to='basic_app.Location'),
        ),
        migrations.AlterField(
            model_name='influencer',
            name='race',
            field=models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='influencers', to='basic_app.Race'),
        ),
    ]
