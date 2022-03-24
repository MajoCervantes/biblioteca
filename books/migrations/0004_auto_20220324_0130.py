# Generated by Django 3.1.7 on 2022-03-24 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20220323_2332'),
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
            model_name='bookitem',
            name='book_format',
            field=models.CharField(choices=[('AB', 'Audiobook'), ('EB', 'Ebook'), ('HC', 'Hardcover'), ('JN', 'Journal'), ('MG', 'Magazine'), ('NW', 'Newspaper'), ('PB', 'Paperback')], default='Provide a format', max_length=2),
        ),
        migrations.AlterField(
            model_name='bookitem',
            name='borrowed_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='bookitem',
            name='due_date',
            field=models.DateTimeField(null=True),
        ),
    ]