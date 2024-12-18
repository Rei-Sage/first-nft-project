from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator
from .forms import NFTForm, InformationForm

from account.models import *
# Create your views here.

def workspace(request):
    artist=NFT.objects.all()
    paginator = Paginator(artist, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  
    context={
        'page_obj':page_obj,
    }
    return render(request,'workspace/index.html',context)


# def create(request):
#     if request.method == 'POST':
#         nft_form = NFTForm(request.POST)
#         info_form = InformationForm(request.POST)       
#         if nft_form.is_valid() and info_form.is_valid():
#             nft_data = nft_form.cleaned_data
#             info_data = info_form.cleaned_data
#             tags = info_data.pop('tags') 

#             nft = NFT.objects.create(
#                 name=nft_data['name'],
#                 creator=nft_data['creator'],
#                 price=nft_data['price'],
#                 highest_bid=nft_data['highest_bid'],
#                 image_url=nft_data['image_url'],
#                 minted_date=nft_data['minted_date']
#             )

#             information = Information.objects.create(
#                 nft=nft, 
#                 description=info_data['description'],
#                 blockchain=info_data['blockchain'],
#                 etherscan_link=info_data['etherscan_link'],
#                 original_link=info_data['original_link']
#             )

#             information.tags.add(*tags) 
#             information.save()  

#             return redirect('workspace')  
#     else:
#         nft_form = NFTForm()
#         info_form = InformationForm()
    
#     return render(
#         request, 
#         'workspace/create.html', 
#         {'nft_form': nft_form, 'info_form': info_form})

def create(request):
    if request.method == 'POST':
        nft_form = NFTForm(request.POST)
        info_form = InformationForm(request.POST)       
        if nft_form.is_valid() and info_form.is_valid():
            nft = nft_form.save()
            info = info_form.save(commit=False)
            info.nft = nft  
            info.save()
            return redirect('workspace')  
    else:
        nft_form = NFTForm()
        info_form = InformationForm()
    
    return render(
        request, 
        'workspace/create.html', 
        {'nft_form': nft_form, 'info_form': info_form})

# def create(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         change_percentage = request.POST['change_percentage']
#         nfts_sold = request.POST['nfts_sold']
#         volume = request.POST['volume']
#         image = request.FILES.get('image')

#         artist = NFT.objects.create(
#             name=name,
#             change_percentage=change_percentage,
#             nfts_sold=nfts_sold,
#             volume=volume
#         )



#         if image:
#             ArtistImage.objects.create(artist=artist, image=image)
#         return redirect('workspace') 
#     return render(request,'workspace/create.html')


# def update(request, id):
#     artist = get_object_or_404(Artist, id=id)
#     artist_image = ArtistImage.objects.filter(artist=artist).first()  

#     if request.method == 'POST':
#         artist.name = request.POST.get('name', artist.name)
#         artist.change_percentage = request.POST.get('change_percentage', artist.change_percentage)
#         artist.nfts_sold = request.POST.get('nfts_sold', artist.nfts_sold)
#         artist.volume = request.POST.get('volume', artist.volume)
#         artist.save()
#         image = request.FILES.get('image')
#         if image:
#             if artist_image:
#                 artist_image.image = image
#                 artist_image.save()
#             else:
#                 ArtistImage.objects.create(artist=artist, image=image)

#         return redirect('workspace') 

#     return render(request, 'workspace/update.html', {
#         'artist': artist,
#         'artist_image': artist_image,
#     })


def update(request, nft_id):
    nft = get_object_or_404(NFT, id=nft_id)
    information = get_object_or_404(Information, nft=nft)

    if request.method == 'POST':
        nft_form = NFTForm(request.POST)
        info_form = InformationForm(request.POST)
        
        if nft_form.is_valid() and info_form.is_valid():
            nft.name = nft_form.cleaned_data['name']
            nft.creator = nft_form.cleaned_data['creator']
            nft.price = nft_form.cleaned_data['price']
            nft.highest_bid = nft_form.cleaned_data['highest_bid']
            nft.image_url = nft_form.cleaned_data['image_url']
            nft.minted_date = nft_form.cleaned_data['minted_date']
            nft.save()

            information.description = info_form.cleaned_data['description']
            information.blockchain = info_form.cleaned_data['blockchain']
            information.etherscan_link = info_form.cleaned_data['etherscan_link']
            information.original_link = info_form.cleaned_data['original_link']
            tags = info_form.cleaned_data['tags']
            information.save()

            information.tags.set(tags)

            return redirect('workspace')  
    else:
        nft_form = NFTForm(initial={
            'name': nft.name,
            'creator': nft.creator,
            'price': nft.price,
            'highest_bid': nft.highest_bid,
            'image_url': nft.image_url,
            'minted_date': nft.minted_date,
        })
        info_form = InformationForm(initial={
            'description': information.description,
            'blockchain': information.blockchain,
            'etherscan_link': information.etherscan_link,
            'original_link': information.original_link,
            'tags': information.tags.all(),
        })

    return render(
        request, 
        'workspace/update.html', 
        {'nft_form': nft_form, 'info_form': info_form, 'nft': nft}
    )

def delete(request, nft_id):
    nft = get_object_or_404(NFT, id=nft_id)
    information = get_object_or_404(Information, nft=nft)

    information.delete()
    nft.delete()

    return redirect('/')

    return render(request, 'workspace/index.html', {'message': 'NFT успешно удалено!'})