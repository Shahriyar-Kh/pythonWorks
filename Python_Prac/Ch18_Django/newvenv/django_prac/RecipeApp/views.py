from django.shortcuts import render ,redirect
from .models import *

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
#***************************** login Form ************************************************
def login_page(request):
    if request.method=="POST":
        username=request.POST.get("Username")
        password=request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.error(request,"Invalid Username")
            return redirect("/RecipeApp/login")
        user=authenticate(username=username,password=password)

        if user is None:
            messages.error(request,"Invalid Password")
            return redirect("/RecipeApp/login")
        else:
            login(request,user)
            return redirect("/RecipeApp/login/recipe")
    
    return render(request,"login.html")
#******************************** Logout page *************************************** 
def logout_page(request):
    logout(request)
    return redirect("/login")
    
#***************************** Register Form *********************************************************
def register_page(request):
    if request.POST:
        first_name=request.POST.get("firstname")
        last_name=request.POST.get("lastname")
        user_name=request.POST.get("email")
        password=request.POST.get("password")
        
        
        user=User.objects.filter(username=user_name)
        if user.exists:
            messages.info(request,"Username Already Exists")
            return redirect("/RecipeApp/login/Register")
        
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=user_name
        )
        user.set_password(password)
        user.save()

        messages.info(request,"Account Successfully Created!")
        return redirect("/RecipeApp/login/Register")
    return render(request,"register.html")


#********************************* Add Records ************************************************
def recipe(request):
    if request.method == "POST":
        data=request.POST
    
        R_name=data.get("Recipe_Name")
        R_Desc=data.get("Recipe_Description") 
        R_img=request.FILES.get("Recipe_Image")

        Recipe_tb.objects.create(
            Recipe_Name=R_name,
            Recipe_Description=R_Desc,
            Recipe_Image=R_img
        )
        return redirect("/RecipeApp/login/recipe")
    
    queryset=Recipe_tb.objects.all()
    context={
        "recipe_q":queryset,
    }
#********************************************* Search Button *************************************************
    if request.GET.get("Search"):
        queryset=queryset.filter(Recipe_Name__icontains=request.GET.get("Search"))
    return render(request,"recipe.html",context)

#********************************* delete Records ************************************************
def delete_Recipe(request,id):
    data=Recipe_tb.objects.get(id=id)
    data.delete()

    return redirect("/RecipeApp/login/recipe")
#********************************* Update Records ************************************************
def Update_Recipe(request,id):
    queryset=Recipe_tb.objects.get(id=id)

    if request.method=="POST":
        dataset=request.POST
        data_img=request.FILES

        R_name=dataset.get("Recipe_Name")
        R_Desc=dataset.get("Recipe_Description") 
        R_img=data_img.get("Recipe_Image")

       
        queryset.Recipe_Name=R_name,
        queryset.Recipe_Description=R_Desc,
        if R_img:
            queryset.Recipe_Image=R_img,
        queryset.save()
        return redirect("/RecipeApp/login/recipe")

    context={
        "update_recipe":queryset
    }
    return render(request,"Update_Recipe.html",context)
