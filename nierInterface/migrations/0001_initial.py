# Generated by Django 3.1.1 on 2020-09-03 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_upload', models.ImageField(blank=True, null=True, upload_to='nier_logos', verbose_name='logo')),
                ('favicon', models.FileField(blank=True, null=True, upload_to='nier_favicons', verbose_name='favicon')),
                ('slogan', models.CharField(blank=True, max_length=100, verbose_name='slogan')),
                ('short_description', models.CharField(blank=True, max_length=500, verbose_name='short descripion')),
                ('keywords', models.CharField(blank=True, help_text='separate words with comma', max_length=100, verbose_name='keywords')),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='config', to='sites.site', verbose_name='site')),
            ],
            options={
                'verbose_name': 'site configuration',
                'verbose_name_plural': 'sites configurations',
                'ordering': ('site',),
            },
        ),
    ]
