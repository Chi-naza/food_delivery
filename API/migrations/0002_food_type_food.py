# Generated by Django 4.0.4 on 2022-06-01 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('P', 'Popular'), ('R', 'Recommended')], max_length=20)),
                ('description', models.CharField(max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.CharField(max_length=220)),
                ('stars', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('people', models.IntegerField()),
                ('selected', models.IntegerField()),
                ('img', models.ImageField(upload_to='food_image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('food_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.food_type')),
            ],
        ),
    ]