from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Emplyee

def employees(request):
    employees=Emplyee.objects.all().values()
    temp=loader.get_template("employees.html")

    context={
        'employees':employees,
    }
    return HttpResponse(temp.render(context,request))

def emp_details(request,id):
    emp_details=Emplyee.objects.get(id=id)
    temp=loader.get_template("emp_details.html")

    context={
        "emp_details":emp_details,
    }

    return HttpResponse(temp.render(context,request))

def main(request):
    template=loader.get_template("main.html")
    return HttpResponse(template.render())

def testing(request):
    temp=loader.get_template("testing.html")
    context={
        "firstname":"Umair",
        "greeting":2,
    }
    return HttpResponse(temp.render(context,request))

def student_data(request):
    template=loader.get_template("student_d.html")

    students=[
        {"Name":"Shahriyar Khan","Age":20,"Degree":"BSSE"},
        {"Name":"Umair Khan","Age":17,"Degree":"MLT"},
        {"Name":"Ali Khan","Age":24,"Degree":"CS"},
        {"Name":"Eng. Usman","Age":14,"Degree":"ICS"},
        {"Name":"Yaseen Khan","Age":22,"Degree":"BSSE"}
    ]
    text=""" 
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Nulla reprehenderit minima distinctio consequuntur quia, nihil culpa eaque inventore sunt ratione laboriosam dignissimos earum labore quisquam facere doloremque laudantium obcaecati, sapiente temporibus corporis laborum. Ullam quis laudantium quia doloremque mollitia doloribus rem? Qui consequatur nobis optio repellendus reprehenderit explicabo illo! Eligendi nostrum cumque illum tempore iusto sit odit saepe omnis non voluptates dolorum corporis, aspernatur molestias eos odio, aut quia quaerat nam adipisci soluta ab doloribus quo? Commodi facilis dolore repudiandae quo ea incidunt voluptatum a harum reiciendis voluptate eum fuga dolor, praesentium expedita, saepe consectetur excepturi dolorem aliquam necessitatibus? Similique?
"""
    return HttpResponse(template.render(context={"students":students,"text":text}))