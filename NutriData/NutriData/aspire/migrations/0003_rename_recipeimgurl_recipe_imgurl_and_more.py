# Generated by Django 4.1.2 on 2022-12-05 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aspire', '0002_recipe_user_user_remove_folder_recipe_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='recipeImgUrl',
            new_name='imgUrl',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipeTitle',
            new_name='title',
        ),
        migrations.AddField(
            model_name='recipe',
            name='calories',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='carbs',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='fat',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='protein',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
    ]