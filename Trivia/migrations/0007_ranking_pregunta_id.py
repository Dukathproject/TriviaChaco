# Generated by Django 3.2.6 on 2021-09-04 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Trivia', '0006_userlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='ranking',
            name='pregunta_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Trivia.pregunta'),
            preserve_default=False,
        ),
    ]
