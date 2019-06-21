# Generated by Django 2.2.2 on 2019-06-21 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wrestlers', '0003_auto_20190620_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='loosers',
        ),
        migrations.AddField(
            model_name='match',
            name='losers',
            field=models.ManyToManyField(blank=True, related_name='losers', to='wrestlers.Wrestler'),
        ),
        migrations.AlterField(
            model_name='match',
            name='summary',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.RemoveField(
            model_name='match',
            name='winners',
        ),
        migrations.AddField(
            model_name='match',
            name='winners',
            field=models.ManyToManyField(blank=True, related_name='winners', to='wrestlers.Wrestler'),
        ),
        migrations.AlterField(
            model_name='wrestler',
            name='affiliation',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='wrestler',
            name='birthdate',
            field=models.DateField(blank=True, null=True, verbose_name='birthday'),
        ),
        migrations.AlterField(
            model_name='wrestler',
            name='losses',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wrestler',
            name='nickname',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='wrestler',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wrestler',
            name='wins',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
