import pandas as pd
import os
from django.core.management.base import BaseCommand
from djangoprac2.models import School, Class, AssessmentArea, Student, Answer, Award, Subject, Summary
from django.conf import settings


class Command(BaseCommand):
    help = 'Import data from multiple CSV files'
    csv_file_path = os.path.join(settings.BASE_DIR, 'csv_files', 'Ganison_dataset_1.csv')
    df = pd.read_csv(csv_file_path)
  #  CSV file path
    print(df.columns.tolist())

    def handle(self, *args, **kwargs):
        folder_path = os.path.join(settings.BASE_DIR, 'csv_files') 

        for filename in os.listdir(folder_path):
            if filename.endswith('.csv'):
                file_path = os.path.join(folder_path, filename)
                data = pd.read_csv(file_path)

                for index, row in data.iterrows():
                    
                    school, _ = School.objects.get_or_create(school_name=row['school_name'])
                    class_obj, _ = Class.objects.get_or_create(Class=row['Class'])
                    student, _ = Student.objects.get_or_create(
                        #S_Id=row['StudentID'],  
                        Fullname=f"{row['First Name']} {row['Last Name']}"
                    )
                    subject, _ = Subject.objects.get_or_create(
                        Subject=row['Subject'], 
                        Subject_score=row['student_score'] 
                    )
                    assessment_area, _ = AssessmentArea.objects.get_or_create(Name=row['Assessment Areas'])
                    answer, _ = Answer.objects.get_or_create(Answer=row['Answers'])
                    award, _ = Award.objects.get_or_create(Name=row['award'])  

                      # Summary instance
                    Summary.objects.create(
                        School_Id=school,
                        Sydney_Participant=row['sydney_participants'] == 'Yes',
                        Sydney_Percentile=row['sydney_percentile'],
                        Assessment_Area_Id=assessment_area,
                        Award_Id=award,
                        Class_Id=class_obj,
                        Correct_Answer=row['Correct Answers'],
                        Correct_answer_percentage_per_class=row['correct_answer_percentage_per_class'],
                        Student_Id=student,
                        Participant=row['participant'] == 'Yes',
                        Student_score=row['student_score'],
                        Subject_Id=subject,
                        Category_Id=row['student_area_assessed_score'],  
                        Year_level_name=row['year'],  
                        Answer_Id=answer,
                        Correct_answer_id=row['Correct Answers']  
                    )