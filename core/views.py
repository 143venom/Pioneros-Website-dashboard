from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib import auth, messages
from .models import *
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.views import View

# Create your views here.


# handel user registration and login/logout views here.
# def user_Create(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         first_name = request.POST.get("first_name")
#         last_name = request.POST.get("last_name")
#         password = request.POST.get("password")
#         confirm_password = request.POST.get("confirm_password")

#         # Check if all fields are filled
#         if (
#             not email
#             or not first_name
#             or not last_name
#             or not password
#             or not confirm_password
#         ):
#             messages.error(request, "All fields are required.")
#             return render(request, "user_create.html")

#         # Check if passwords match
#         if password != confirm_password:
#             messages.error(request, "Passwords do not match.")
#             return render(request, "user_create.html")

#         # Check if the email already exists
#         if User.objects.filter(email=email).exists():
#             messages.error(request, "Email already exists.")
#             return render(request, "user_create.html")

#         # Create the user
#         user = User.objects.create_user(
#             email=email, password=password, first_name=first_name, last_name=last_name
#         )
#         user.save()
#         return redirect("user_login")

#     return render(request, "user_create.html")


# def user_login(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         password = request.POST.get("password")

#         # Authenticate the user
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect("index")  # Redirect to the home page or any other page
#         else:
#             messages.error(request, "Invalid email or password.")

#     return render(request, "user_login.html")


# def user_logout(request):
#     auth.logout(request)
#     return redirect("index")


# handel_super_user and staff login_logout_views_dashboard


def superuser_or_staff_required(user):
    return user.is_superuser or user.is_staff


@method_decorator(user_passes_test(superuser_or_staff_required), name="dispatch")
class UsersView(View):
    def get(self, request):
        obj = User.objects.all().order_by("-id")[:5]
        context = {"objs": obj}
        return render(request, "dashboard/user.html", context)
    
    def post(self, request):
        if request.method == "POST":
            email = request.POST.get("email")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get(
                "last_name"
            )  # Ensure last_name is retrieved from POST data
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")
            image_file = request.FILES.get("image")

            # Check if all fields are filled
            if not (
                email
                and first_name
                and last_name
                and password
                and confirm_password
                and image_file
            ):
                messages.error(request, "All fields are required.")
                return redirect("dashboard-user")

            # Check if passwords match
            if password != confirm_password:
                messages.error(request, "Passwords do not match.")
                return redirect("dashboard-user")

            # Check if the email already exists
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists.")
                return redirect("dashboard-user")

            # Create the superuser
            user = User.objects.create_staff(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                image=image_file,
            )

            messages.success(request, "Staff user created successfully.")
            return redirect("dashboard-user")

        return render(request, "dashboard/user.html")
    



def admin_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Authenticate the user
        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.is_staff or user.is_superuser:
                login(request, user)
                return redirect(
                    reverse("admin-dashboard")
                )  # Redirect to the admin dashboard or another page
            else:
                messages.error(request, "You do not have admin privileges.")
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, "admin_login.html")


def admin_logout(request):
    auth.logout(request)
    return redirect("admin-login")
