# Generated by Django 5.1.4 on 2024-12-05 17:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('avatar_url', models.URLField(blank=True, null=True)),
                ('change_percentage', models.FloatField()),
                ('nfts_sold', models.PositiveIntegerField()),
                ('volume', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArtistImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='artist_images/')),
                ('artist', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='account.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('minted_date', models.DateField()),
                ('blockchain', models.CharField(default='Ethereum', max_length=255)),
                ('etherscan_link', models.URLField(blank=True, null=True)),
                ('original_link', models.URLField(blank=True, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='collections', to='account.artist')),
                ('tags', models.ManyToManyField(related_name='collections', to='account.tag')),
            ],
        ),
        migrations.CreateModel(
            name='NFT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('highest_bid', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nfts', to='account.collection')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nfts', to='account.artist')),
            ],
        ),
        migrations.CreateModel(
            name='NFTCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('preview_image', models.ImageField(upload_to='categories/')),
                ('price_range', models.CharField(max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='account.artist')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_address', models.CharField(max_length=255)),
                ('volume', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nfts_sold', models.PositiveIntegerField()),
                ('followers', models.PositiveIntegerField()),
                ('bio', models.TextField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('discord', models.URLField(blank=True, null=True)),
                ('artist', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to='account.artist')),
            ],
        ),
    ]
