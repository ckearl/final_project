# Generated by Django 4.1.2 on 2022-12-05 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aspire', '0005_alter_recipe_user_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe_user',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='aspire.user'),
        ),
    ]