from . import models
def siteinfo(request):
    info = models.Info.objects.all().first()
    print(info)
    return {'info':info}

def categories(request):
    categories = models.Category.objects.all()
    return {'categories':categories}