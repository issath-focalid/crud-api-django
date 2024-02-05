from django.shortcuts import render, redirect, get_object_or_404
from student.forms import StudentForm
from student.models import Student

from rest_framework import viewsets, generics
from .serializers import StudentSerializer


# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


def std(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view')
            except:
                pass
    else:  # Move this part outside the if block
        form = StudentForm()

    return render(request, 'index.html', {'form': form})


def update(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/view')
    else:
        form = StudentForm(instance=student)

    return render(request, 'edit.html', {'form': form, 'student': student})


# def home_page(request):
#     students = Student.objects.all()  # Assuming you want to retrieve all students
#     return render(request, 'view.html', {'students': students})
# def update(request, id):
#     student = get_object_or_404(Student, id=id)

#     if request.method == 'POST':
#         form = StudentForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             return redirect('/view')
#     else:
#         form = StudentForm(instance=student)

#     return render(request, 'update.html', {'form': form, 'student': student})


def view(request):
    student = Student.objects.all()
    return render(request, "view.html", {'student': student})


def delete(request, id):
    try:
        student = Student.objects.get(id=id)
        student.delete()
        return redirect('/view')
    except Student.DoesNotExist:
        return render(request, 'not_found.html')


def edit(request, id):
    try:
        student = Student.objects.get(id=id)
        return render(request, "edit.html", {'student': student})
    except Student.DoesNotExist:
        return render(request, 'not_found.html')
