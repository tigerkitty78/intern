from django.db import models

from django.db import models

# Ttble 1:School
class School(models.Model):
    Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Name

# Table 2: Class
class Class(models.Model):
    Class = models.CharField(max_length=100)

    def __str__(self):
        return self.Class

# table 3:assessment Areas
class AssessmentArea(models.Model):
    Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Name

# Table 4: student
class Student(models.Model):
    Fullname = models.CharField(max_length=200)
    #S_Id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.Fullname

# table 5:answers
class Answer(models.Model):
    Answer = models.TextField()

    def __str__(self):
        return self.Answer

# table 6: awards
class Award(models.Model):
    Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Name

# Table 7: Subject
class Subject(models.Model):
    Subject = models.CharField(max_length=200)
    Subject_score = models.FloatField()

    def __str__(self):
        return self.Subject
        
    #9
class School(models.Model):
    school_name = models.CharField(max_length=200)

    def __str__(self):
        return self.school_name  


# Table 8: Summary
class Summary(models.Model):
    School_Id = models.ForeignKey(School, on_delete=models.CASCADE)
    Sydney_Participant = models.BooleanField(default=False)
    Sydney_Percentile = models.FloatField()
    Assessment_Area_Id = models.ForeignKey(AssessmentArea, on_delete=models.CASCADE)
    Award_Id = models.ForeignKey(Award, on_delete=models.CASCADE)
    Class_Id = models.ForeignKey(Class, on_delete=models.CASCADE)
    Correct_Answer = models.TextField()
    Correct_answer_percentage_per_class = models.FloatField()
    Student_Id = models.ForeignKey(Student, on_delete=models.CASCADE)
    Participant = models.BooleanField(default=False)
    Student_score = models.FloatField()
    Subject_Id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Category_Id = models.IntegerField()  
    Year_level_name = models.CharField(max_length=100)
    Answer_Id = models.ForeignKey(Answer, on_delete=models.CASCADE)
    Correct_answer_id = models.TextField()

    def __str__(self):
        return f'Summary for {self.Student_Id.Fullname} in {self.Class_Id.Class}'
