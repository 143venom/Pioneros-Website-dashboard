from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from pioneros.models import *
from core.models import *
from .models import *
from django.views import View
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import user_passes_test
from django.contrib.auth.decorators import login_required


# --------------------------------Dashboard------------------------------------------------
def superuser_or_staff_required(user):
    return user.is_superuser or user.is_staff


@user_passes_test(superuser_or_staff_required)
def dashboard(request):
    total_user = User.objects.count()
    total_product = Products.objects.count()
    total_service = Services.objects.count()
    total_testimonial = Testimonial.objects.count()
    product = Products.objects.all().order_by("-id")[:5]
    service = Services.objects.all().order_by("-id")[:5]
    testimonial = Testimonial.objects.all().order_by("-id")[:5]
    user = User.objects.all().order_by("-id")[:5]
    logo = CompanyInfo.objects.all()
    context = {
        "total_users": total_user,
        "total_products": total_product,
        "total_services": total_service,
        "total_testimonials": total_testimonial,
        "products": product,
        "services": service,
        "testimonials": testimonial,
        "users": user,
        "logo": logo,
    }
    return render(request, "dashboard/dashboard.html", context)


# --------------------------------Dashboard------------------------------------------------
# --------------------------------Crud operation of home-containt-Title----------------------------------------------


@method_decorator(user_passes_test(superuser_or_staff_required), name="dispatch")
class HomeContentTitleView(View):
    def get(self, request):
        obj = HomeContentTitle.objects.all()
        context = {"objs": obj}
        return render(request, "dashboard/homecontenttitle.html", context)

    def post(self, request):
        if request.method == "POST":
            title = request.POST.get("title")
        if title:
            HomeContentTitle.objects.create(title=title)
            messages.success(request, "Home Content Title created successfully.")
            return redirect("dashboard-homecontenttitle")
        else:
            messages.error(
                request,
                "Error creating home content title. Please fill out all fields.",
            )
        return render(request, "dashboard/homecontenttitle.html")


def homecontenttitleedit(request, pk):
    obj = HomeContentTitle.objects.get(id=pk)
    context = {"objs": obj, "form_type": "homecontenttitle"}
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            obj.title = title
            obj.save()
            messages.success(request, "Home Content Title updated successfully.")
            return redirect("dashboard-homecontenttitle")
        else:
            messages.error(
                request,
                "Error updating home content title. Please fill out all fields.",
            )

    return render(request, "dashboard/edit/update.html", context)


# --------------------------------Crud operation of home-content-Title-----------------------------------------------
# --------------------------------Crud operation of home-content-----------------------------------------------
@method_decorator(user_passes_test(superuser_or_staff_required), name="dispatch")
class HomeContentView(View):
    def get(self, request):
        obj = HomeContent.objects.all()
        context = {"objs": obj}
        return render(request, "dashboard/homecontent.html", context)

    def post(self, request):
        if request.method == "POST":
            title = request.POST.get("title")
            number = request.POST.get("number")
        if title and number:
            HomeContent.objects.create(title=title, number=number)
            messages.success(request, "Home Content created successfully.")
            return redirect("dashboard-homecontent")
        else:
            messages.error(
                request, "Error creating home content. Please fill out all fields."
            )
        return render(request, "dashboard/homecontent.html")


@user_passes_test(superuser_or_staff_required)
def homecontentedit(request, pk):
    obj = HomeContent.objects.get(pk=pk)
    context = {"objs": obj, "form_type": "homecontent"}
    if request.method == "POST":
        title = request.POST.get("title")
        number = request.POST.get("number")
        if title and number:
            obj.title = title
            obj.number = number
            obj.save()
            messages.success(request, "Home Content updated successfully.")
            return redirect("dashboard-homecontent")
        else:
            messages.error(
                request, "Error updating home content. Please fill out all fields."
            )

    return render(request, "dashboard/edit/update.html", context)


# --------------------------------Crud operation of home-containt-----------------------------------------------


# --------------------------------Dashboard------------------------------------------------
@method_decorator(user_passes_test(superuser_or_staff_required), name="dispatch")
class CarouselView(View):
    def get(self, request):
        obj = Carousel.objects.all().order_by("-id")
        context = {"objs": obj}
        return render(request, "dashboard/carousel.html", context)

    def post(self, request):
        if request.method == "POST":
            title = request.POST.get("title")
            image_file = request.FILES.get("image")
        if title and image_file:
            Carousel.objects.create(title=title, image=image_file)
            messages.success(request, "Carousel created successfully.")
            return redirect("dashboard-carousel")
        else:
            messages.error(
                request, "Error creating carousel. Please fill out all fields."
            )
        return render(request, "dashboard/carousel.html")


@user_passes_test(superuser_or_staff_required)
def carouseledit(request, pk):
    obj = Carousel.objects.get(id=pk)
    context = {"objs": obj, "form_type": "carousel"}
    if request.method == "POST":
        title = request.POST.get("title")
        image_file = request.FILES.get("image")
        if title:
            obj.title = title
            if image_file:
                obj.image = image_file
            obj.save()
            messages.success(request, "Carousel updated successfully.")
            return redirect("dashboard-carousel")
        else:
            messages.error(
                request, "Error updating carousel. Please fill out all fields."
            )

    return render(request, "dashboard/edit/update.html", context)


# --------------------------------Crud operation of Service------------------------------------------------@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(superuser_or_staff_required), name="dispatch")
class ServiceView(View):
    def get(self, request):
        obj = Services.objects.all().order_by("-id")[:5]
        context = {"objs": obj}
        return render(request, "dashboard/service.html", context)

    def post(self, request):
        if request.method == "POST":
            title = request.POST.get("title")
            description = request.POST.get("description")
            image_file = request.FILES.get("image")

        if title and description and image_file:
            Services.objects.create(
                title=title, description=description, image=image_file
            )
            messages.success(request, "Product created successfully.")
            return redirect(
                "dashboard-service"
            )  # Redirect to service list or another view
        else:
            messages.error(
                request, "Error creating product. Please fill out all fields."
            )
        return render(request, "dashboard/service.html")


@user_passes_test(superuser_or_staff_required)
def serviceedit(request, pk):
    obj = Services.objects.get(id=pk)
    context = {"objs": obj, "form_type": "service"}
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        image_file = request.FILES.get("image")
        if title and description:
            obj.title = title
            obj.description = description
            if image_file:
                obj.image = image_file
            obj.save()
            messages.success(request, "service updated successfully.")
            return redirect("dashboard-service")
        else:
            messages.error(
                request, "Error updating service. Please fill out all fields."
            )
    return render(request, "dashboard/edit/update.html", context)


@user_passes_test(superuser_or_staff_required)
def servicedelete(request, pk):
    obj = Services.objects.get(id=pk)
    obj.delete()
    return redirect("dashboard-service")


@method_decorator(user_passes_test(superuser_or_staff_required), name="dispatch")
class ServicesBackgroundImageView(View):
    def get(self, request):
        obj = ServicesBackgroundImage.objects.all()
        context = {"objs": obj}
        return render(request, "dashboard/servicebackgound.html", context)

    def post(self, request):
        if request.method == "POST":
            image_file = request.FILES.get("images")
            if image_file:
                ServicesBackgroundImage.objects.create(image=image_file)
                messages.success(
                    request, "Services Background Image created successfully."
                )
                return redirect("dashboard-ServicesBackground")
            else:
                messages.error(
                    request,
                    "Error creating Services Background Image. Please select any Image.",
                )  # Redirect to service list or another view
        return render(request, "dashboard/servicebackgound.html")


@user_passes_test(superuser_or_staff_required)
def servicebackgroundedit(request, pk):
    obj = ServicesBackgroundImage.objects.get(id=pk)
    context = {"objs": obj, "form_type": "servicebackground"}
    if request.method == "POST":
        image_file = request.FILES.get("images")
        if image_file:
            obj.image = image_file
            obj.save()
            messages.success(request, "Services Background Image updated successfully.")
            return redirect("dashboard-ServicesBackground")
        else:
            messages.error(
                request,
                "Error updating Services Background Image. Please select any Image.",
            )  # Redirect to service list or another view
    return render(request, "dashboard/edit/update.html", context)


# --------------------------------Crud operation of Service------------------------------------------------
# --------------------------------Crud operation of Product------------------------------------------------
@method_decorator(user_passes_test(superuser_or_staff_required), name="dispatch")
class ProductView(View):
    def get(self, request):
        obj = Products.objects.all().order_by("-id")[:5]
        context = {"objs": obj}
        return render(request, "dashboard/product.html", context)

    def post(self, request):
        if request.method == "POST":
            title = request.POST.get("title")
            description = request.POST.get("description")
            image_file = request.FILES.get("image")

        if title and description and image_file:
            Products.objects.create(
                title=title, description=description, image=image_file
            )
            messages.success(request, "Product created successfully.")
            return redirect(
                "dashboard-product"
            )  # Redirect to product list or another view
        else:
            messages.error(
                request, "Error creating product. Please fill out all fields."
            )
        return render(request, "dashboard/product.html")


@user_passes_test(superuser_or_staff_required)
def productedit(request, pk):
    obj = Products.objects.get(id=pk)
    context = {"objs": obj, "form_type": "product"}
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        image_file = request.FILES.get("image")
        if title and description:
            obj.title = title
            obj.description = description
            if image_file:
                obj.image = image_file
            obj.save()
            messages.success(request, "Product updated successfully.")
            return redirect("dashboard-product")
        else:
            messages.error(
                request, "Error updating product. Please fill out all fields."
            )
    return render(request, "dashboard/edit/update.html", context)


@user_passes_test(superuser_or_staff_required)
def productdelete(request, pk):
    obj = Products.objects.get(id=pk)
    obj.delete()
    return redirect("dashboard-product")


@method_decorator(user_passes_test(superuser_or_staff_required), name="dispatch")
class ProductBackgroundImageView(View):
    def get(self, request):
        obj = ProductBackgroundImage.objects.all()
        context = {"objs": obj}
        return render(request, "dashboard/productbackgound.html", context)

    def post(self, request):
        if request.method == "POST":
            image_file = request.FILES.get("images")
            if image_file:
                ProductBackgroundImage.objects.create(image=image_file)
                messages.success(
                    request, "Product Background Image created successfully."
                )
                return redirect("dashboard-ProductBackground")
            else:
                messages.error(
                    request,
                    "Error creating Product Background Image. Please select any Image.",
                )  # Redirect to service list or another view
        return render(request, "dashboard/productbackgound.html")


@user_passes_test(superuser_or_staff_required)
def productbackgroundedit(request, pk):
    obj = ProductBackgroundImage.objects.get(id=pk)
    context = {"objs": obj, "form_type": "productbackground"}
    if request.method == "POST":
        image_file = request.FILES.get("images")
        if image_file:
            obj.image = image_file
            obj.save()
            messages.success(request, "Product Background Image updated successfully.")
            return redirect("dashboard-ProductBackground")
        else:
            messages.error(
                request,
                "Error updating Product Background Image. Please select any Image.",
            )  # Redirect to service list or another view
    return render(request, "dashboard/edit/update.html", context)


# --------------------------------Crud operation of Product------------------------------------------------
# --------------------------------Crud operation of Company-Info-------------------------------------------
@method_decorator(user_passes_test(superuser_or_staff_required), name="dispatch")
class CompanyView(View):
    def get(self, request):
        obj = CompanyInfo.objects.all()
        context = {"objs": obj}
        return render(request, "dashboard/companyinfo.html", context)

    def post(self, request):
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            location = request.POST.get("location")
            phone = request.POST.get("phone")
            open = request.POST.get("open")
            logo = request.FILES.get("logo")
            if name and email and location and phone and open and logo:
                CompanyInfo.objects.create(
                    name=name,
                    email=email,
                    location=location,
                    phone=phone,
                    open=open,
                    logo=logo,
                )
                messages.success(request, "Company Info created successfully.")
                return redirect(
                    "dashboard-companyinfo"
                )  # Redirect to product list or another view
            else:
                messages.error(
                    request, "Error creating Company Info. Please fill out all fields."
                )
        return render(request, "dashboard/companyinfo.html")


@user_passes_test(superuser_or_staff_required)
def companyinfoedit(request, pk):
    obj = CompanyInfo.objects.get(id=pk)
    context = {"objs": obj, "form_type": "companyinfo"}
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        location = request.POST.get("location")
        phone = request.POST.get("phone")
        open = request.POST.get("open")
        logo = request.FILES.get("logo")
        if name and email and location and phone and open:
            obj.name = name
            obj.email = email
            obj.location = location
            obj.phone = phone
            obj.open = open
            if logo:
                obj.logo = logo
            obj.save()
            messages.success(request, "Company Info updated successfully.")
            return redirect(
                "dashboard-companyinfo"
            )  # Redirect to product list or another view
        else:
            messages.error(
                request, "Error updating Company Info. Please fill out all fields."
            )

    return render(request, "dashboard/edit/update.html", context)


# --------------------------------Crud operation of Company-Info-------------------------------------------
# --------------------------------Crud operation of Ware-House-------------------------------------------
@method_decorator(user_passes_test(superuser_or_staff_required), name="dispatch")
class WarehouseView(View):
    def get(self, request):
        obj = WarehouseAndLogistic.objects.all().order_by("-id")[:5]
        context = {"objs": obj}
        return render(request, "dashboard/warehouse.html", context)

    def post(self, request):
        if request.method == "POST":
            image_file = request.FILES.get("image")

        if image_file:
            WarehouseAndLogistic.objects.create(image=image_file)
            messages.success(request, "Warehouse And Logistic created successfully.")
            return redirect(
                "dashboard-warehouse"
            )  # Redirect to product list or another view
        else:
            messages.error(
                request,
                "Error creating Warehouse And Logistic. Please select any image.",
            )
        return render(request, "dashboard/warehouse.html")


@user_passes_test(superuser_or_staff_required)
def warehouseedit(request, pk):
    obj = WarehouseAndLogistic.objects.get(id=pk)
    context = {"objs": obj, "form_type": "warehouseandlogistic"}
    if request.method == "POST":
        image = request.FILES.get("image")
        if image:
            obj.image = image
            obj.save()
            messages.success(request, "Warehouse Image updated successfully.")
            return redirect(
                "dashboard-warehouse"
            )  # Redirect to product list or another view
        else:
            messages.error(
                request, "Error updating Warehouse Image. Please fill out all fields."
            )

    return render(request, "dashboard/edit/update.html", context)


@user_passes_test(superuser_or_staff_required)
def warehousedelete(request, pk):
    obj = WarehouseAndLogistic.objects.get(id=pk)
    obj.delete()
    messages.success(request, "Warehouse And Logistic deleted successfully.")
    return redirect("dashboard-warehouse")


# --------------------------------Crud operation of Ware-House-------------------------------------------
# --------------------------------Crud operation of Testimonials------------------------------------------------
@method_decorator(user_passes_test(superuser_or_staff_required), name="dispatch")
class TestimonialView(View):
    def get(self, request):
        obj = Testimonial.objects.all().order_by("-id")
        context = {"objs": obj}
        return render(request, "dashboard/testimonial.html", context)

    def post(self, request):
        if request.method == "POST":
            name = request.POST.get("name")
            message = request.POST.get("message")
            profession = request.POST.get("profession")
            image_file = request.FILES.get("image")
        if name and message and profession and image_file:
            Testimonial.objects.create(
                patient_name=name,
                message=message,
                profession=profession,
                image=image_file,
            )
            messages.success(request, "Testimonial created successfully.")
            return redirect(
                "dashboard-testimonials"
            )  # Redirect to product list or another view
        else:
            messages.error(
                request, "Error creating product. Please fill out all fields."
            )

            return render(request, "dashboard/testimonial.html")


@user_passes_test(superuser_or_staff_required)
def testimonialedit(request, pk):
    obj = Testimonial.objects.get(id=pk)
    context = {"objs": obj, "form_type": "testimonial"}
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        profession = request.POST.get("profession")
        image_file = request.FILES.get("image")
        if name and message and profession:
            obj.patient_name = name
            obj.message = message
            obj.profession = profession
            if image_file:
                obj.image = image_file
            obj.save()
            messages.success(request, "Testimonial updated successfully.")
            return redirect(
                "dashboard-testimonials"
            )  # Redirect to product list or another view
        else:
            messages.error(
                request, "Error updating Testimonial. Please fill out all fields."
            )

    return render(request, "dashboard/edit/update.html", context)


@user_passes_test(superuser_or_staff_required)
def testimonialdelete(request, pk):
    obj = Testimonial.objects.get(id=pk)
    obj.delete()
    messages.success(request, "Testimonial deleted successfully.")
    return redirect("dashboard-testimonials")


# --------------------------------Crud operation of Testimonials------------------------------------------------
# --------------------------------Crud operation of About------------------------------------------------
class AboutView(View):
    def get(self, request):
        obj = About.objects.all()
        context = {"objs": obj}
        return render(request, "dashboard/about.html", context)

    def post(self, request):
        if request.method == "POST":
            # Handle POST requests (form submission)
            title = request.POST.get("title")
            description = request.POST.get("description")
            
            if title and description:
                About.objects.create(title=title, description=description)
                messages.success(request, "About created successfully.")
                return redirect("dashboard-about")
            else:
                messages.error(request, "Error creating about. Please fill out all fields.")
                return render(request, "dashboard/about.html")


@user_passes_test(superuser_or_staff_required)
def aboutedit(request, pk):
    obj = About.objects.get(id=pk)
    context = {"objs": obj, "form_type": "about"}
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        if title and description:
            obj.title = title
            obj.description = description
            obj.save()
            messages.success(request, "About updated successfully.")
            return redirect("dashboard-about")
        else:
            messages.error(request, "Error updating about. Please fill out all fields.")
    return render(request, "dashboard/edit/update.html", context)


@method_decorator(user_passes_test(superuser_or_staff_required), name="dispatch")
class AboutContentView(View):
    def get(self, request):
        objs = About_Content.objects.all().order_by("-id")
        context = {"objs": objs}
        return render(request, "dashboard/aboutcontent.html", context)

    def post(self, request):
        if request.method == "POST":
            title = request.POST.get("title")
            if title:
                About_Content.objects.create(title=title)
                messages.success(request, "About content created successfully.")
                return redirect("dashboard-about-content")
            else:
                messages.error(
                    request, "Error creating about content. Please fill out all fields."
                )
        return render(request, "dashboard/aboutcontent.html")


@user_passes_test(superuser_or_staff_required)
def aboutcontentedit(request, pk):
    obj = About_Content.objects.get(id=pk)
    context = {"objs": obj, "form_type": "aboutcontent"}
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            obj.title = title
            obj.save()
            messages.success(request, "About content updated successfully.")
            return redirect("dashboard-about-content")
        else:
            messages.error(
                request, "Error updating about content. Please fill out all fields."
            )
    return render(request, "dashboard/edit/update.html", context)


@user_passes_test(superuser_or_staff_required)
def aboutcontentdelete(request, pk):
    obj = About_Content.objects.get(id=pk)
    obj.delete()
    messages.success(request, "About content deleted successfully.")
    return redirect("dashboard-about-content")


# --------------------------------Crud operation of About------------------------------------------------
# --------------------------------Crud operation of Features------------------------------------------------
@method_decorator(user_passes_test(superuser_or_staff_required), name="dispatch")
class FeatureView(View):
    def get(self, request):
        obj = Feature.objects.all()
        context = {"objs": obj}
        return render(request, "dashboard/feature.html", context)

    def post(self, request):
        if request.method == "POST":
            title = request.POST.get("title")
            description = request.POST.get("description")
            image_file = request.FILES.get("image")
            if title and description and image_file:
                Feature.objects.create(title=title, description=description, image=image_file)
                messages.success(request, "Features created successfully.")
                return redirect("dashboard-feature")
            else:
                messages.error(
                    request, "Error creating Features. Please fill out all fields."
                )
        return render(request, "dashboard/feature.html")


@user_passes_test(superuser_or_staff_required)
def featureedit(request, pk):
    obj = Feature.objects.get(id=pk)
    context = {"objs": obj, "form_type": "feature"}
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        image_file = request.FILES.get("image")
        if title and description:
            obj.title = title
            obj.description = description
            if image_file:
                obj.image = image_file
            obj.save()
            messages.success(request, "Features updated successfully.")
            return redirect("dashboard-feature")
        else:
            messages.error(
                request, "Error updating Features. Please fill out all fields."
            )
    return render(request, "dashboard/edit/update.html", context)


@method_decorator(user_passes_test(superuser_or_staff_required), name="dispatch")
class FeaturesContentView(View):
    def get(self, request):
        objs = Features_Content.objects.all().order_by("-id")
        context = {"objs": objs}
        return render(request, "dashboard/featurecontent.html", context)

    def post(self, request):
        title = request.POST.get("title")
        description = request.POST.get("description")
        image_file = request.FILES.get(
            "image"
        )  # Adjust the name to match the form field name

        if title and description and image_file:
            # Assuming Features_Content is your model
            Features_Content.objects.create(
                name=title, department=description, image=image_file
            )
            messages.success(request, "Feature content created successfully.")
            return redirect("dashboard-featurecontent")
        else:
            messages.error(
                request, "Error creating Feature content. Please fill out all fields."
            )

        return render(request, "dashboard/featurecontent.html")


# @user_passes_test(superuser_or_staff_required)
# def featurecontentedit(request, pk):
#     obj = Features_Content.objects.get(id=pk)
#     context = {"objs": obj, "form_type": "featurecontent"}
#     if request.method == "POST":
#         title = request.POST.get("title")
#         description = request.POST.get("description")
#         image_file = request.FILES.get("image")
#         if title and description and image_file:
#             obj.name = title
#             obj.department = description
#             obj.image = image_file
#             obj.save()
#             messages.success(request, "Features content updated successfully.")
#             return redirect("dashboard-featurecontent")
#         else:
#             messages.error(
#                 request, "Error updating Features content. Please fill out all fields."
#             )
#     return render(request, "dashboard/edit/update.html", context)


@user_passes_test(superuser_or_staff_required)
def featurecontentedit(request, pk):
    obj = get_object_or_404(Features_Content, id=pk)
    context = {"objs": obj, "form_type": "featurecontent"}
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        image_file = request.FILES.get("image")
        if title and description:
            obj.name = title
            obj.department = description
            if image_file:
                obj.image = image_file
            obj.save()
            messages.success(request, "Features content updated successfully.")
            return redirect("dashboard-featurecontent")
        else:
            messages.error(request, "Error updating Features content. Please fill out all fields.")
    return render(request, "dashboard/edit/update.html", context)


@user_passes_test(superuser_or_staff_required)
def featurecontentdelete(request, pk):
    obj = Features_Content.objects.get(id=pk)
    obj.delete()
    messages.success(request, "Features content deleted successfully.")
    return redirect("dashboard-featurecontent")


# --------------------------------Crud operation of Features------------------------------------------------
@method_decorator(user_passes_test(superuser_or_staff_required), name="dispatch")
class SocialMediaView(View):
    def get(self, request):
        obj = SocialMedia.objects.all()
        context = {"objs": obj}
        return render(request, "dashboard/socialmedia.html", context)

    def post(self, request):
        if request.method == "POST":
            facebook_url = request.POST.get("facebook_url")
            twitter_url = request.POST.get("twitter_url")
            instagram_url = request.POST.get("instagram_url")
            linkedin_url = request.POST.get("linkedin_url")
            youtube_url = request.POST.get("youtube_url")

            socialmedia = SocialMedia.objects.create(
                facebook_url=facebook_url,
                twitter_url=twitter_url,
                instagram_url=instagram_url,
                linkedin_url=linkedin_url,
                youtube_url=youtube_url,
            )
            socialmedia.save()
            messages.success(request, "Social Media created successfully.")
            return redirect("dashboard-socialmedia")
        return render(request, "dashboard/socialmedia.html")


@user_passes_test(superuser_or_staff_required)
def socialmediaedit(request, pk):
    obj = SocialMedia.objects.get(id=pk)
    context = {"objs": obj, "form_type": "socialmedia"}
    if request.method == "POST":
        facebook_url = request.POST.get("facebook_url")
        twitter_url = request.POST.get("twitter_url")
        instagram_url = request.POST.get("instagram_url")
        linkedin_url = request.POST.get("linkedin_url")
        youtube_url = request.POST.get("youtube_url")
        if (
            facebook_url
            and twitter_url
            and instagram_url
            and linkedin_url
            and youtube_url
        ):
            obj.facebook_url = facebook_url
            obj.twitter_url = twitter_url
            obj.instagram_url = instagram_url
            obj.linkedin_url = linkedin_url
            obj.youtube_url = youtube_url
            obj.save()
            messages.success(request, "Social Media updated successfully.")
            return redirect("dashboard-socialmedia")
        else:
            messages.error(
                request, "Error updating Social Media. Please fill out all fields."
            )

    return render(request, "dashboard/edit/update.html", context)


# --------------------------------Crud operation of Contact-View-----------------------------------------------
@method_decorator(user_passes_test(superuser_or_staff_required), name="dispatch")
class ContactBackgroundImageView(View):
    def get(self, request):
        obj = ContactBackgroundImage.objects.all()
        context = {"objs": obj}
        return render(request, "dashboard/contactbackground.html", context)

    def post(self, request):
        if request.method == "POST":
            image_file = request.FILES.get("images")
            if image_file:
                ContactBackgroundImage.objects.create(image=image_file)
                messages.success(
                    request, "Contact Background Image created successfully."
                )
                return redirect("dashboard-contact")
            else:
                messages.error(
                    request,
                    "Error creating Contact Background Image. Please select any Image.",
                )  # Redirect to service list or another view
        return render(request, "dashboard/contactbackground.html")


@user_passes_test(superuser_or_staff_required)
def contactbackgroundedit(request, pk):
    obj = ContactBackgroundImage.objects.get(id=pk)
    context = {"objs": obj, "form_type": "contactbackground"}
    if request.method == "POST":
        image_file = request.FILES.get("images")
        if image_file:
            obj.image = image_file
            obj.save()
            messages.success(request, "Contact Background Image updated successfully.")
            return redirect("dashboard-contact")
        else:
            messages.error(
                request,
                "Error updating Contact Background Image. Please select any Image.",
            )  # Redirect to service list or another view
    return render(request, "dashboard/edit/update.html", context)