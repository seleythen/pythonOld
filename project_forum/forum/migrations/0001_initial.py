# Generated by Django 2.0.5 on 2018-05-29 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainForum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Tytuł')),
                ('slug', models.SlugField(max_length=100, verbose_name='Odnośnik')),
            ],
            options={
                'verbose_name': 'Forum',
                'verbose_name_plural': 'Fora',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Data dodania')),
                ('text', models.TextField(verbose_name='Treść')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posty',
            },
        ),
        migrations.CreateModel(
            name='SubForum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Tytuł')),
                ('slug', models.SlugField(max_length=100, verbose_name='Odnośnik')),
                ('object_id', models.PositiveIntegerField()),
                ('forum_slug', models.SlugField(max_length=100, verbose_name='Slug rodzica')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Tytuł')),
                ('slug', models.SlugField(max_length=100, verbose_name='Odnośnik')),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.SubForum')),
            ],
            options={
                'verbose_name': 'Wątek',
                'verbose_name_plural': 'Wątki',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Thread'),
        ),
        migrations.AlterUniqueTogether(
            name='thread',
            unique_together={('slug', 'forum')},
        ),
        migrations.AlterUniqueTogether(
            name='subforum',
            unique_together={('slug', 'forum_slug')},
        ),
    ]
