# Generated by Django 2.2.4 on 2019-08-06 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='id')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('-created',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='id')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('short_name', models.TextField(max_length=10)),
            ],
            options={
                'ordering': ('-created',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='id')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('category', models.TextField(choices=[('GOOGLE', 'google-api'), ('CUSTOM', 'custom-api'), ('JUDGE', 'judge'), ('NORMAL', 'normal')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='id')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('URL', models.URLField()),
                ('cache_path', models.URLField()),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='websites', to='translator.UserProfile')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='websites', to='translator.Food')),
            ],
            options={
                'ordering': ('-created',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='id')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('cloud_URL', models.URLField()),
                ('filesize', models.IntegerField()),
                ('longitude', models.IntegerField()),
                ('latitude', models.IntegerField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='translator.UserProfile')),
                ('original_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='translator.Image')),
            ],
            options={
                'ordering': ('-created',),
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='food',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='translator.UserProfile'),
        ),
        migrations.AddField(
            model_name='food',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='translator.Language'),
        ),
        migrations.AddField(
            model_name='food',
            name='thumbnails',
            field=models.ManyToManyField(to='translator.Image'),
        ),
        migrations.CreateModel(
            name='Clip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='id')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('bounding_box', models.TextField(max_length=100)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clips', to='translator.UserProfile')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clips', to='translator.Image')),
            ],
            options={
                'ordering': ('-created',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='id')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('annotates_source_language', models.BooleanField()),
                ('clip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='annotations', to='translator.Clip')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='annotations', to='translator.UserProfile')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='annotations', to='translator.Language')),
            ],
            options={
                'ordering': ('-created',),
                'abstract': False,
            },
        ),
    ]