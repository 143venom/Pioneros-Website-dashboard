from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path("", index, name="index"),
    # path("", under_construction, name="under-construction"),
    path("about/", about, name="about"),
    path("logistic/", service, name="logistic"),
    path("logistic/<int:id>/", service_detail, name="logistic"),
    path("product/", product, name="product"),
    path("news&events/", news_events, name="news_events"),
    path("warehouse/", feature, name="warehouse"),
    path("contact/", contact, name="contact"),
    path("submit_newsletter/", submit_newsletter, name="submit_newsletter"),
    path("news-event/<int:id>/", news_events_detail, name="news-event"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
