# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Escolha',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('texto_escolha', models.CharField(max_length=200)),
                ('votos', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('texto_pergunta', models.CharField(max_length=200)),
                ('data_pub', models.DateTimeField(verbose_name='data de publicação')),
            ],
        ),
        migrations.AddField(
            model_name='escolha',
            name='pergunta',
            field=models.ForeignKey(to='enquetes.Pergunta'),
        ),
    ]
