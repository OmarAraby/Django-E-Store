# Generated by Django 5.0 on 2023-12-06 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "Book", "verbose_name_plural": "Books"},
        ),
        migrations.AlterField(
            model_name="product",
            name="PRDDesc",
            field=models.TextField(verbose_name="Book Description"),
        ),
        migrations.AlterField(
            model_name="product",
            name="PRDISNew",
            field=models.BooleanField(default=True, verbose_name="New Book"),
        ),
        migrations.AlterField(
            model_name="product",
            name="PRDImage",
            field=models.ImageField(
                blank=True, null=True, upload_to="book_image/", verbose_name="Image"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="PRDName",
            field=models.CharField(max_length=50, verbose_name="Book Name"),
        ),
        migrations.AlterField(
            model_name="product",
            name="PRDSlug",
            field=models.SlugField(blank=True, null=True, verbose_name="Book URL"),
        ),
    ]