# Generated by Django 2.0.7 on 2018-07-28 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=64)),
                ('street', models.CharField(max_length=64)),
                ('blockNumber', models.IntegerField()),
                ('apartmentNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=64)),
                ('type', models.IntegerField(choices=[(0, 'Niezdefiniowany'), (1, 'Domowy'), (2, 'Służbowy'), (3, 'Prywatny')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('surname', models.CharField(max_length=64)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('type', models.IntegerField(choices=[(0, 'Niezdefiniowany'), (1, 'Domowy'), (2, 'Służbowy'), (3, 'Prywatny')], default=0)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Person')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='persons',
            field=models.ManyToManyField(to='contact.Person'),
        ),
        migrations.AddField(
            model_name='email',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Person'),
        ),
        migrations.AddField(
            model_name='address',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Person'),
        ),
    ]
