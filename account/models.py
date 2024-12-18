from django.db import models






class Artist(models.Model):
    class Meta:
        verbose_name = 'Художник'
        verbose_name_plural = 'Художники'

    name = models.CharField(max_length=255, verbose_name='Название')
    change_percentage = models.FloatField(verbose_name='Изменение') 
    nfts_sold = models.PositiveIntegerField(verbose_name='Количество проданных NFT')  
    volume = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Объем продаж в ETH')  

    def __str__(self):
        return self.name


class ArtistImage(models.Model):
    class Meta:
        verbose_name = 'Аватвар'
        verbose_name_plural = 'Аватар'
 
    artist = models.OneToOneField(Artist, on_delete=models.CASCADE, related_name='image', verbose_name='фото худ')  
    image = models.ImageField(upload_to="artist_images/", verbose_name='изображ') 

    def __str__(self):
        return f"Image of {self.artist.name}"

class NFT(models.Model):
    class Meta:
        verbose_name = 'NFT'
        verbose_name_plural = 'NFT'

    name = models.CharField(max_length=255, verbose_name='Название') 
    # collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='nfts', verbose_name='Связь с коллекцией') 
    creator = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True, related_name='nfts', verbose_name='Создатель')  
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')  
    highest_bid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Высшая ставка')  
    image_url = models.URLField(null=True, blank=True , verbose_name='Изображения NFT') 
    minted_date = models.DateField(null=True, blank=True,verbose_name='Время')
    def __str__(self):
        return self.name


class Information(models.Model):
    class Meta:
        verbose_name = 'Детальная информация'
        verbose_name_plural = 'Детальная информация'
    nft = models.OneToOneField(NFT, on_delete=models.CASCADE, related_name='token',null=True, verbose_name='Для какой nft') 
    description = models.TextField(verbose_name='описание') 
    # created_by = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True, related_name='collections', verbose_name='Автор') 
    blockchain = models.CharField(max_length=255, default='Ethereum', verbose_name='Блокчейн')
    tags = models.ManyToManyField('Tag', related_name='collections', verbose_name='тэг')  
    etherscan_link = models.URLField(blank=True, null=True, verbose_name='Etherscan') 
    original_link = models.URLField(blank=True, null=True, verbose_name='оригинальная ссылка')  

    def __str__(self):
        return self.description


class Tag(models.Model):
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    name = models.CharField(max_length=100, unique=True, verbose_name='Название') 

    def __str__(self):
        return self.name


class NFTCategory(models.Model):
    class Meta:
        verbose_name = 'NFT категории'
        verbose_name_plural = 'NFT категории'
    name = models.CharField(max_length=255, verbose_name='Нахвание Категории') 
    author = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='categories', verbose_name='Автор')  

    def __str__(self):
        return self.name




class UserProfile(models.Model):

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'

    artist = models.OneToOneField(Artist, on_delete=models.CASCADE, related_name='user_profile', verbose_name='профиль') 
    wallet_address = models.CharField(max_length=255, verbose_name='Кошельек') 
    volume = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Объем продаж')  
    nfts_sold = models.PositiveIntegerField(verbose_name='Количество проданных NFT') 
    followers = models.PositiveIntegerField(verbose_name='Количество подписчиков') 
    bio = models.TextField(blank=True, null=True, verbose_name='Биография ')  
    website = models.URLField(blank=True, null=True, verbose_name='Сайт')  
    twitter = models.URLField(blank=True, null=True, verbose_name='Twitter') 
    instagram = models.URLField(blank=True, null=True, verbose_name='Instagram')  
    discord = models.URLField(blank=True, null=True, verbose_name='Discord')  

    def __str__(self):
        return self.artist.name



class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)

    def __str__(self):
        return self.username