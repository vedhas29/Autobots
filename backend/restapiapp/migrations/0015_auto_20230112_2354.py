# Generated by Django 3.2.4 on 2023-01-12 18:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restapiapp', '0014_remove_myteam_team_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=15)),
                ('cpassword', models.CharField(max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='myproject',
            name='id',
        ),
        migrations.RemoveField(
            model_name='myteam',
            name='id',
        ),
        migrations.RemoveField(
            model_name='myteammember',
            name='id',
        ),
        migrations.AddField(
            model_name='myproject',
            name='proj_id',
            field=models.AutoField(default=django.utils.timezone.now, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myteam',
            name='team_id',
            field=models.AutoField(default=django.utils.timezone.now, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myteammember',
            name='team_member_id',
            field=models.AutoField(default=django.utils.timezone.now, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
