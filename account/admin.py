from django.contrib import admin

# Register your models here.
from account.models import *

admin.site.register(User)

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'change_percentage', 'nfts_sold', 'volume')
    search_fields = ('name',)
    list_filter = ('change_percentage',)


@admin.register(ArtistImage)
class ArtistImageAdmin(admin.ModelAdmin):
    list_display = ('id','artist', 'image')


@admin.register(Information)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id','blockchain')
    search_fields = ('description',)
    list_filter = ('blockchain',)
    autocomplete_fields = ('tags',)  


@admin.register(NFT)
class NFTAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'creator', 'price', 'highest_bid')
    search_fields = ('name',)
    list_filter = ('creator',)
    autocomplete_fields = ('creator',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    search_fields = ('name',)


@admin.register(NFTCategory)
class NFTCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'author', )
    search_fields = ('name', 'author__name')
    autocomplete_fields = ('author',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id','artist', 'wallet_address', 'volume', 'nfts_sold', 'followers')
    search_fields = ('artist__name', 'wallet_address')
    list_filter = ('nfts_sold', 'followers')
    autocomplete_fields = ('artist',)
