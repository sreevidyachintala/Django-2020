from django.shortcuts import render,redirect
from crudapp.forms import PersonForm
from crudapp.models import Person


# Create your views here.
def add(request):
    if request.method == "POST":
        form = PersonForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = PersonForm()
    return render(request,'index.html',{'form':form})


def show(request):
    person = Person.objects.all()
    return render(request,"show.html",{'person':person})

def edit(request, id):
    person = Person.objects.get(id=id)
    return render(request,'edit.html', {'person':person})

def update(request, id):
    person = Person.objects.get(id=id)
    form = PersonForm(request.POST, instance = person)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'person': person})


def destroy(request, id):
    employee = Person.objects.get(id=id)
    employee.delete()
    return redirect("/show")

