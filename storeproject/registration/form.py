
from django import forms
from .models import Department, Course

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    dob = forms.DateField(input_formats=['%d/%m/%Y'])
    age = forms.IntegerField()
    gender=forms.ChoiceField(choices=[('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),])
    phone_number = forms.CharField(max_length=15)
    mail_id = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    course = forms.ChoiceField(choices=(), required=False)
    purpose = forms.ChoiceField(choices=[('Enquiry', 'For Enquiry'), ('Order', 'Place Order'), ('Return', 'Return')])
    materials_provide = forms.MultipleChoiceField(
        choices=[('Notebook', 'Debit Note Book'), ('Pen', 'Pen'), ('ExamPaper', 'Exam Papers')],
        widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].choices = []

        if 'department' in self.data:
             department_id = int(self.data['department'])
             courses = Course.objects.filter(department_id=department_id).values_list('id', 'name')
             self.fields['course'].choices = courses

             print("Department ID:", department_id)
             print("Course Choices:", courses)
