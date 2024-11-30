# Generated by Django 3.0.5 on 2024-11-24 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20241124_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobposting',
            name='job_type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part-Time', 'Part-Time'), ('Contract', 'Contract')], default='Full Time', max_length=20, verbose_name='Type of job posted'),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='salary',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
