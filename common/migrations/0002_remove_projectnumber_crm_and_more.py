# Generated by Django 4.2 on 2023-06-24 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectnumber',
            name='crm',
        ),
        migrations.RemoveField(
            model_name='projectnumber',
            name='mobile_app',
        ),
        migrations.RemoveField(
            model_name='projectnumber',
            name='telegram_bot',
        ),
        migrations.RemoveField(
            model_name='projectnumber',
            name='web_site',
        ),
        migrations.RemoveField(
            model_name='statistic',
            name='client',
        ),
        migrations.RemoveField(
            model_name='statistic',
            name='freelance',
        ),
        migrations.RemoveField(
            model_name='statistic',
            name='project',
        ),
        migrations.RemoveField(
            model_name='statistic',
            name='support',
        ),
        migrations.AddField(
            model_name='projectnumber',
            name='number',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Number'),
        ),
        migrations.AddField(
            model_name='projectnumber',
            name='project_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Project name'),
        ),
        migrations.AddField(
            model_name='statistic',
            name='number',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Number'),
        ),
        migrations.AddField(
            model_name='statistic',
            name='statistic_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='statistic'),
        ),
    ]
