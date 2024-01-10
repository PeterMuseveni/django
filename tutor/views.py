from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    if response.method == "POST":
     print(response.POST)
     if response.POST.get("save"):
        for Item in ls.item_set.all():
           if response.POST.get("c" + str(Item.id)) == "clicked":
              Item.complete = True
           else:
                Item.complete = False

                Item.save()

     elif response.POST.get("newItem"):
       txt = response.POST.get("new")
       if len(txt) > 2:
          ls.item_set.create(text=txt, complete = False)
       else:
          print("invalid")

    return render(response, "tutor/list.html", {"ls": ls})


def home(response):
    return render(response, "tutor/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

            return HttpResponseRedirect("/%i" %t.id)
        

    else:
        form = CreateNewList()
    return render(response, "tutor/create.html", {"form":form} )


def login(request):
    if request.method == 'POST':
        form = CreateNewList(request.POST)
        if form.is_valid():
            # Your login logic here
            pass
    else:
        form = CreateNewList()

    return render(request, "registration/login.html", {'form': form})

