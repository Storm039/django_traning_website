# Generated by Django 4.0.3 on 2022-03-21 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_cmsslider_cms_css_alter_cmsslider_cms_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmsslider',
            name='cms_css',
            field=models.CharField(default='-', max_length=200, null=True, verbose_name='CSS класс'),
        ),
    ]