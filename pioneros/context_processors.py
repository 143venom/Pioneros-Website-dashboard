from .models import *


def header(request):
    return {
        "companyinfo": CompanyInfo.objects.first(),
        "objs": Services.objects.all(),
        "socialmedia": SocialMedia.objects.all(),
    }
