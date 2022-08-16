from django.urls import resolve


def urlName(request):
    url_name = resolve(request.path).url_name
    print(url_name == 'index')
    return {'url_path': url_name}
