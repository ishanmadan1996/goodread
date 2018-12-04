# Generated by Django 2.1.2 on 2018-10-25 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.TextField()),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articless',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=256, unique=True)),
                ('visited', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Link',
                'verbose_name_plural': 'Links',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Topic',
                'verbose_name_plural': 'Topics',
            },
        ),
        migrations.AddIndex(
            model_name='link',
            index=models.Index(fields=['url', 'visited'], name='crawler_lin_url_29a44c_idx'),
        ),
        migrations.AddIndex(
            model_name='link',
            index=models.Index(fields=['visited'], name='visited_idx'),
        ),
        migrations.AddField(
            model_name='article',
            name='topics',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crawler.Topic'),
        ),
    ]
