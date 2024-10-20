from pioneros.models import *


def dashboard(request):
    return {
        "companyinfos": CompanyInfo.objects.first(),
    }
