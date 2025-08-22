from django.urls import path
from . import views

urlpatterns=[
    path("login/recipe/",views.recipe,name="recipe"),
    path("delete_Recipe/<int:id>/",views.delete_Recipe,name="delete_Recipe"),
    path("Update_Recipe/<int:id>/",views.Update_Recipe,name="Update_Recipe"),
    path("login/",views.login_page,name="login_page"),
    path("login/Register/",views.register_page,name="register_page"),
    path("logout/",views.logout_page,name="logout_page"),
]

