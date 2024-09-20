from django.shortcuts import render
from .models import School, Class, AssessmentArea, Student, Answer, Award, Subject, Summary

def display_tables(request):
   
    schools = School.objects.all()
    classes = Class.objects.all()
    assessment_areas = AssessmentArea.objects.all()
    students = Student.objects.all()
    answers = Answer.objects.all()
    awards = Award.objects.all()
    subjects = Subject.objects.all()
    summaries = Summary.objects.all()

   
    context = {
        'schools': schools,
        'classes': classes,
        'assessment_areas': assessment_areas,
        'students': students,
        'answers': answers,
        'awards': awards,
        'subjects': subjects,
        'summaries': summaries,
    }

    return render(request, 'tables/tables.html', context)
