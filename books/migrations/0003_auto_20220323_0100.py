# Generated by Django 3.1.7 on 2022-03-23 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20220322_0346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='rack',
        ),
        migrations.RemoveField(
            model_name='book',
            name='status',
        ),
        migrations.AddField(
            model_name='bookitem',
            name='rack',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='book', to='books.rack'),
        ),
        migrations.AddField(
            model_name='bookitem',
            name='status',
            field=models.CharField(choices=[('A', 'Available'), ('B', 'Borrowed'), ('L', 'Lost'), ('R', 'Reserved')], default='A', max_length=1),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bookitem',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='rack',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
