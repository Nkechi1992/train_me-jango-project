from django.shortcuts import render, redirect
from django.http import HttpResponse
from my_traime_app.models import  *
from django.contrib.auth.models import User


def home_page(request):
    print("This is me testing this app for my project")
    return render(request, 'homepage.html')

def program_page(request):
    print("This is my program page")
    return render(request, 'programs.html')

def form_page(request):
    if request.method =="GET":
        print("Form page testing")
        return render(request, 'form_res.html')
    if request.method == "POST":
        res_files= request.FILES['res_image']
        print(res_files.name)
        responders_data_info = web_responders(
            R_name = request.POST.get("res_name"),
            R_age = request.POST.get("res_age"),
            R_city = request.POST.get("res_city"),
            R_gender = request.POST.get("res_gender"),
            R_academy = request.POST.get("res_academic"),
            R_phone = request.POST.get("res_phone"),
            R_email = request.POST.get("res_email"),  
            R_program = request.POST.get("res_program"),
            R_image= res_files.name,
            )
        responders_data_info.save()
        imagefolder = r"C:/My_jango_Proj/trainme_jango/my_traime_app/static/img/" + res_files.name
        with open(imagefolder, "wb+") as img_file:
            for chunk in res_files.chunks():
                img_file.write(chunk)
        return render(request, 'submit.html' )
        
    
def responders(request):
    if request.method == "GET":
        part_res = web_responders.objects.all().values()
        return render(request, 'responders_display.html', {'res_form': (part_res)})
    

def profile_id(request, id):
        profile_res = web_responders.objects.filter( id = id ).values()
        print(profile_res)
        return render(request, 'profile_res.html', {'profile_display': list(profile_res)})

def sign_up(request):
    if request.method == "GET":
       return render(request, 'signup_page.html') 
    if request.method == "POST":
       username = request.POST.get('res_username')
       password = request.POST.get('res_password')
       Re_password = request.POST.get('res_repassword')
       if password == Re_password:
           user = User.objects.create_user(username=username, password = password)
           return redirect(home_page)
       else:
           return render(request, 'signup_page.html', {'error message: The password does not match, check and retype'})
