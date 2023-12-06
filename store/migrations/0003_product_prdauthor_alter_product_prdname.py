# Generated by Django 5.0 on 2023-12-06 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_alter_product_options_alter_product_prddesc_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="PRDAuthor",
            field=models.CharField(default="", max_length=50, verbose_name="Author"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="product",
            name="PRDName",
            field=models.CharField(max_length=50, verbose_name="Book Title"),
        ),
    ]
