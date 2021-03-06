# Generated by Django 2.0.1 on 2018-05-29 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='materias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('ab1', models.DecimalField(decimal_places=2, max_digits=6)),
                ('ab2', models.DecimalField(decimal_places=2, max_digits=6)),
                ('reav', models.DecimalField(decimal_places=2, max_digits=6)),
                ('final', models.DecimalField(decimal_places=2, max_digits=6)),
                ('media', models.DecimalField(decimal_places=2, max_digits=6)),
                ('faltas', models.IntegerField()),
                ('carga_horaria', models.IntegerField()),
                ('max_faltas', models.IntegerField()),
                ('conceito', models.CharField(max_length=200)),
            ],
        ),
    ]
