# Generated by Django 4.1 on 2022-09-03 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('method', models.TextField()),
                ('ingredients', models.TextField()),
                ('source_url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('category', models.CharField(choices=[('pork', 'pork'), ('chiken', 'chiken'), ('beef', 'beef'), ('fish', 'fish'), ('vegetarian', 'vegetarian')], max_length=100)),
                ('difficulty', models.CharField(choices=[('easy', 'easy'), ('moderate', 'moderate'), ('hard', 'hard')], max_length=100)),
                ('cuisine', models.CharField(choices=[('american', 'american'), ('australian', 'australian'), ('chinese', 'chinese'), ('european', 'european')], max_length=100)),
            ],
        ),
    ]
