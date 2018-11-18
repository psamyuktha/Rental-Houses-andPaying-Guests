from django.http import HttpResponse
from .models import Album
from django.shortcuts import render
from django.http import Http404
# from django.template import loader
from django.shortcuts import render
from .models import Album, Song


def index(request):
    all_albums = Album.objects.all()
    return render(request, 'myApp/index.html', {'all_albums': all_albums})


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'myApp/detail.html', {'album': album})


def favorite(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'myApp/detail.html', {
            'album' : album,
            'error_message' : "You did not select a valid song",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'myApp/detail.html', {'album': album})

