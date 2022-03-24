# Generated by Django 3.1.7 on 2022-03-24 09:20

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='Anon', max_length=50)),
                ('isbn', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('abstract', models.TextField()),
                ('editorial', models.CharField(max_length=50)),
                ('publication_date', models.DateField(default=None, null=True)),
                ('language', models.CharField(max_length=50)),
                ('number_of_pages', models.IntegerField()),
                ('category', models.CharField(choices=[('ED', 'Education'), ('ENT', 'Entertainment'), ('FN', 'Finance'), ('FT', 'Fiction'), ('SC', 'Science'), ('TN', 'Technology')], default='No provided', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('ED', 'Education'), ('ENT', 'Entertainment'), ('FN', 'Finance'), ('FT', 'Fiction'), ('SC', 'Science'), ('TN', 'Technology')], default='No provided', max_length=20)),
                ('description', models.TextField(default='No desc. provided')),
            ],
        ),
        migrations.CreateModel(
            name='BookItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('borrowed_date', models.DateTimeField(null=True)),
                ('due_date', models.DateTimeField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('book_format', models.CharField(choices=[('AB', 'Audiobook'), ('EB', 'Ebook'), ('HC', 'Hardcover'), ('JN', 'Journal'), ('MG', 'Magazine'), ('NW', 'Newspaper'), ('PB', 'Paperback')], default='Format not provided yet', max_length=2)),
                ('status', models.CharField(choices=[('A', 'Available'), ('B', 'Borrowed'), ('L', 'Lost'), ('R', 'Reserved')], default='A', max_length=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookItem', to='books.book')),
                ('rack', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='book', to='books.rack')),
            ],
        ),
    ]
