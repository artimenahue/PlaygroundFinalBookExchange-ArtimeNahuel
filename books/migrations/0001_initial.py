# Generated by Django 4.2.4 on 2023-08-29 02:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='books/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField(default=False)),
                ('book_desired', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trade_desired', to='books.book')),
                ('book_offered', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trade_offered', to='books.book')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trades_offered', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trades_received', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
