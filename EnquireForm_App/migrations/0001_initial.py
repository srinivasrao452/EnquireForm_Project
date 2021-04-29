# Generated by Django 2.0.5 on 2020-11-24 05:50

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnquireData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('course', multiselectfield.db.fields.MultiSelectField(choices=[('Python', 'Python'), ('Django', 'Django'), ('Flask', 'Flask'), ('REST_API', 'REST_API')], max_length=28)),
                ('location', multiselectfield.db.fields.MultiSelectField(choices=[('Hyderabad', 'Hyd'), ('Bangalore', 'Bang'), ('Chennai', 'Che')], max_length=27)),
                ('start_date', models.DateField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]