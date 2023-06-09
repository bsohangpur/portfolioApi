# Generated by Django 3.2.18 on 2023-04-01 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Routes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('email', models.EmailField(default='', max_length=254)),
                ('subject', models.CharField(default='', max_length=255)),
                ('message', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.ImageField(default='', upload_to='projects/')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Routes.image')),
                ('title', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Routes.language')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('detail', models.TextField(default='')),
                ('images', models.ManyToManyField(default='', related_name='service_images', to='Routes.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('describtion', models.TextField(default='')),
                ('workflow_link', models.CharField(default='', max_length=255)),
                ('project_link', models.CharField(default='', max_length=255)),
                ('images', models.ManyToManyField(default='', related_name='images', to='Routes.Image')),
                ('languageAndTool', models.ManyToManyField(default='', related_name='tools', to='Routes.Language')),
            ],
        ),
    ]
