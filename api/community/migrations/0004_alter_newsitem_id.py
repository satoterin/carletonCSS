# Generated by Django 3.2 on 2021-07-25 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("community", "0003_alter_newsitem_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newsitem",
            name="id",
            field=models.CharField(
                default="P7KeaD5935q5HGyvh65Gvp",
                editable=False,
                max_length=40,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
