# Generated by Django 4.1 on 2022-09-04 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0006_remove_student_uni_num_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificaterequest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
