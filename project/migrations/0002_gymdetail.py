# Generated by Django 4.2.6 on 2023-11-27 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GymDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64)),
                ('descricao', models.CharField(max_length=640)),
                ('endereco', models.CharField(max_length=1000)),
                ('imagem', models.CharField(max_length=640)),
                ('imagem2', models.CharField(max_length=640)),
                ('linkacademia', models.CharField(max_length=640)),
                ('horario', models.CharField(max_length=640)),
                ('fitdance', models.BooleanField(blank=True, default=True, null=True)),
                ('nutricionista', models.BooleanField(blank=True, default=True, null=True)),
                ('arcondicionado', models.BooleanField(blank=True, default=True, null=True)),
                ('personal', models.BooleanField(blank=True, default=True, null=True)),
                ('natação', models.BooleanField(blank=True, default=True, null=True)),
                ('pilates', models.BooleanField(blank=True, default=True, null=True)),
                ('spinning', models.BooleanField(blank=True, default=True, null=True)),
                ('vestiario', models.BooleanField(blank=True, default=True, null=True)),
                ('estacionamento', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
    ]