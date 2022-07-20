# Generated by Django 4.0.6 on 2022-07-20 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='제목')),
                ('photo', models.ImageField(blank=True, upload_to='posts/%Y%M%d', verbose_name='사진')),
                ('content', models.TextField(verbose_name='내용')),
                ('interest', models.IntegerField(default=0, verbose_name='가격')),
                ('devTools', models.CharField(choices=[('CPP', 'C++'), ('NODEJS', 'Node.js'), ('REACT', 'react'), ('SPRING', 'Spring'), ('JAVA', 'Java'), ('DJANGO', 'django')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
