# Generated by Django 3.0.7 on 2020-06-15 09:07

import Test.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Test.Class')),
            ],
        ),
        migrations.CreateModel(
            name='HomeWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('student_id', models.ForeignKey(on_delete=Test.models.Student, to='Test.Student')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='school_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Test.School'),
        ),
    ]
