from django.shortcuts import render, redirect
from .models import Task


def home(request):
    query = Task.objects.all()
    if request.method == "POST":
        task = Task()
        if len(request.POST["title"]) > 0 and len(request.POST["due_date"]) > 0:
            task.title = request.POST["title"]
            task.due_date = request.POST["due_date"]
            task.save()
    if "filter" in request.POST:
        if request.POST["filter"] in ["e","c","h"] :
            query = query.filter(status=request.POST["filter"])
        elif "a" in request.POST["filter"]:
            query = Task.objects.all()
    
    if "sort" in request.POST:
        if request.POST["sort"] == "added_date":
            query = query.order_by("-datetime_created")
        elif request.POST["sort"] == "due_date":
            query = query.order_by("-due_date")
    return render(request, "pages/home.html", context={"tasks":query})



def mark_task(request, pk):
    task = Task.objects.get(id=pk)
    task.mark_task()
    print(task.status)
    return redirect("home_page")


def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("home_page")
    
    
def edit_task(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        if len(request.POST["title"]) > 0 and len(request.POST["due_date"]) > 0:
            task.title = request.POST["title"]
            task.due_date = request.POST["due_date"]
            task.save()
            context= {"task":task}
            return redirect("home_page")
    else:    
        splited_date = str(task.due_date).split("-")
        year = splited_date[0]
        month = splited_date[2]
        day = splited_date[1]
        context = {
        "task":task,
        "month":month,
        "day":day,
        "year":year
        }
    return render(request, "pages/edit.html", context=context)