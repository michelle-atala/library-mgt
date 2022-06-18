

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('The_Library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),

                ('email', models.CharField(max_length=50)),
                ('student_number', models.CharField(max_length=12)),

            ],
        ),
        migrations.RenameModel(
            old_name='books',
            new_name='book',
        ),
    ]
