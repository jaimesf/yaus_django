import re
from django.http import HttpResponseRedirect
from django.shortcuts import render
from web.forms import NewShortURL
from web.models import Url
from yaus import settings


def index(request):
    if request.method == 'POST':
        form = NewShortURL(request.POST)
        if form.is_valid():
            url = form.cleaned_data["url"]

            #Regex URL validation from John Gruber https://gist.github.com/uogbuji/705383
            p = re.compile(
                r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))')
            m = p.match(url)
            if m:
                url_to_insert = Url()
                url_to_insert.url = url
                url_to_insert.save()

                shorted_url = settings.PROTOCOL+'//'+settings.HOSTNAME+settings.PORT+'/'+str(url_to_insert.id_url)

                data = {
                    'shorted_url': shorted_url,
                    'original_url' : url
                }

                return render(request, 'web/result.html', data)
            else:
                data = {
                    'form': form,
                    'error': 'Field URL is not valid URL'
                }
                return render(request, 'web/form.html', data)
        else:
            data = {
                'form': form,
                'error': 'Please introduce url to short'
            }
            return render(request, 'web/form.html', data)

    else:
        form = NewShortURL()
        data = {
            'form': form,
        }
        return render(request, 'web/form.html', data)


def redirectioner(request, id):

    if id and is_number(id):

        url_to_redirect = Url.objects(id_url=id).first()
        if url_to_redirect:

            return HttpResponseRedirect(url_to_redirect.url)
        else:
            return render(request, 'web/error.html')
    else:
        return render(request, 'web/error.html')

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False