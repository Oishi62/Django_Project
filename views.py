from django.shortcuts import render
def functions(request):
    return render(request,"form.html")

def functions2(request):
    return render(request,"fo2.html")

def assignment_home(request):
    return render(request,"homepage.html")

def assignment_register(request):
    return render(request,"registration.html")
def assignment_about(request):
    return render(request,"about-us.html")