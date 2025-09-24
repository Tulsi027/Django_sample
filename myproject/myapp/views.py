from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages

def index(request):
    if request.method == "POST":
        # CREATE
        if "create" in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")
            Student.objects.create(name=name, email=email)
            messages.success(request, "Student added successfully!")

        # UPDATE
        elif "update" in request.POST:
            student_id = request.POST.get("id")
            student = Student.objects.get(id=student_id)
            student.name = request.POST.get("name")
            student.email = request.POST.get("email")
            student.save()
            messages.success(request, "Student updated successfully!")

        # DELETE
        elif "delete" in request.POST:
            student_id = request.POST.get("id")
            student = Student.objects.get(id=student_id)
            student.delete()
            messages.success(request, "Student deleted successfully!")

        # SEARCH
        elif "search" in request.POST:
            query = request.POST.get("query")
            students = Student.objects.filter(name__icontains=query)
            return render(request, "index.html", {"students": students, "search_query": query})

        return redirect("index")  # reload to clear POST data

    students = Student.objects.all()
    return render(request, "index.html", {"students": students})
