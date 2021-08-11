# Generated by Django 3.2.3 on 2021-08-11 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210809_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentdata',
            name='eca',
        ),
        migrations.RemoveField(
            model_name='studentdata',
            name='quality1',
        ),
        migrations.RemoveField(
            model_name='studentdata',
            name='quality2',
        ),
        migrations.RemoveField(
            model_name='studentdata',
            name='quality3',
        ),
        migrations.RemoveField(
            model_name='studentdata',
            name='quality4',
        ),
        migrations.AddField(
            model_name='studentdata',
            name='academics',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='deployed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='extracirricular',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='friendly',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='hardworking',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='intern',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='leadership',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='quality',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='social',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='teamwork',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='studentlogininfo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
