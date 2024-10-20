from django.urls import path
from .views import *

urlpatterns = [
    # --------------------------------------------------------------------------------------------------------------------#
    path("", dashboard, name="admin-dashboard"),
    # --------------------------------------------------------------------------------------------------------------------#
    path('homecontenttitle/', HomeContentTitleView.as_view(), name='dashboard-homecontenttitle'),
    path('homecontenttitleedit/<int:pk>', homecontenttitleedit, name='dashboard-homecontenttitleedit'),
    # --------------------------------------------------------------------------------------------------------------------#
    path('homecontent/', HomeContentView.as_view(), name='dashboard-homecontent'),
    path('homecontentedit/<int:pk>', homecontentedit, name='dashboard-homecontentedit'),
    # --------------------------------------------------------------------------------------------------------------------#
    path('carousel/', CarouselView.as_view(), name='dashboard-carousel'),
    path('carouseledit/<int:pk>', carouseledit, name='dashboard-carouseledit'),
    # --------------------------------------------------------------------------------------------------------------------#
    path("companyinfo/", CompanyView.as_view(), name='dashboard-companyinfo'),
    path("companyinfoedit/<int:pk>/", companyinfoedit, name='dashboard-companyinfo-edit'),
    # --------------------------------------------------------------------------------------------------------------------#
    path("service/", ServiceView.as_view(), name="dashboard-service"),
    path("serviceedit/<int:pk>", serviceedit, name="dashboard-serviceedit"),
    path("servicedelete/<int:pk>", servicedelete, name="dashboard-servicedelete"),
    path("servicebackground/", ServicesBackgroundImageView.as_view(), name="dashboard-ServicesBackground"),
    path("servicebackgroundedit/<int:pk>/", servicebackgroundedit, name="dashboard-servicebackgroundedit"),
    # --------------------------------------------------------------------------------------------------------------------#
    path("product/", ProductView.as_view(), name='dashboard-product'),
    path("productedit/<int:pk>", productedit, name="dashboard-productedit"),
    path("productdelete/<int:pk>", productdelete, name="dashboard-productdelete"),
    path("productbackground/", ProductBackgroundImageView.as_view(), name="dashboard-ProductBackground"),
    path("productbackgroundedit/<int:pk>/", productbackgroundedit, name="dashboard-productbackgroundedit"),
    # --------------------------------------------------------------------------------------------------------------------#
    path("warehouse/", WarehouseView.as_view(), name='dashboard-warehouse'),
    path('warehouseedit/<int:pk>/', warehouseedit, name='warehouse-edit'),
    path('warehousedelete/<int:pk>/', warehousedelete, name='warehouse-delete'),
    # --------------------------------------------------------------------------------------------------------------------#
    path("testimonial/", TestimonialView.as_view(), name="dashboard-testimonials"),
    path("testimonialedit/<int:pk>/", testimonialedit, name="testimonial-edit"),
    path("testimonialdelete/<int:pk>/", testimonialdelete, name="testimonial-delete"),
    # --------------------------------------------------------------------------------------------------------------------#
    # path("admin/appointment-post/", appointment_post, name="appointment-post"),
    # path("admin/appointment-get/", appointment_get, name="appointment-get"),
    # --------------------------------------------------------------------------------------------------------------------#
    path("about/", AboutView.as_view(), name="dashboard-about"),
    path("aboutedit/<int:pk>", aboutedit, name="dashboard-aboutedit"),
    path("aboutcontent/", AboutContentView.as_view(), name="dashboard-about-content"),
    path("aboutcontentedit/<int:pk>/", aboutcontentedit, name="dashboard-aboutcontentedit"),
    path("aboutcontentdelete/<int:pk>/", aboutcontentdelete, name="dashboard-aboutcontentdelete"),
    # --------------------------------------------------------------------------------------------------------------------#
    path("socialmedia/", SocialMediaView.as_view(), name="dashboard-socialmedia"),
    path("socialmediaedit/<int:pk>", socialmediaedit, name="dashboard-socialmediaedit"),
    # --------------------------------------------------------------------------------------------------------------------#
    path('contact/', ContactBackgroundImageView.as_view(), name="dashboard-contact"),
    path('contactedit/<int:pk>/', contactbackgroundedit, name="dashboard-contactedit"),
    # --------------------------------------------------------------------------------------------------------------------#
    path("feature/", FeatureView.as_view(), name="dashboard-feature"),
    path("featureedit/<int:pk>/", featureedit, name="dashboard-featureedit"),
    path("featurecontent/", FeaturesContentView.as_view(), name="dashboard-featurecontent"),
    path("featurecontentedit/<int:pk>/", featurecontentedit, name="dashboard-featurecontentedit"),
    path("featurecontentdelete/<int:pk>/", featurecontentdelete, name="dashboard-featurecontentdelete"),
    # --------------------------------------------------------------------------------------------------------------------#
]

