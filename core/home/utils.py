from .models import Student

def find_student_by_name(name):
    try:
        return Student.objects.get(name=name)
    except Student.DoesNotExist:
        return None
