# Generated by Django 4.0.6 on 2022-08-14 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('noticia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(null=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('approved_comment', models.BooleanField(default=False)),
                ('noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noticia.noticia')),
            ],
        ),
    ]
