# Generated by Django 2.2.9 on 2020-02-19 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200219_0136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table_cells',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cell', models.CharField(max_length=1)),
            ],
        ),
    ]