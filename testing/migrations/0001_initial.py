# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 08:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classattended', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('group_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('sem', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='faces',
            fields=[
                ('face_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('student_usn', models.CharField(max_length=100)),
                ('sem', models.IntegerField()),
                ('person_id', models.CharField(max_length=100)),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.Department')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.Classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=100)),
                ('sem', models.IntegerField()),
                ('classdone', models.IntegerField()),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.Department')),
            ],
        ),
        migrations.AddField(
            model_name='faces',
            name='person_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.Student'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='dept_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.Department'),
        ),
        migrations.AddField(
            model_name='attendence',
            name='student_usn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.Student'),
        ),
        migrations.AddField(
            model_name='attendence',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.Subject'),
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together=set([('student_usn', 'person_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='attendence',
            unique_together=set([('student_usn', 'subject_id')]),
        ),
    ]