from django import forms

class QuestionsForm(forms.Form):
    question1 = forms.CharField(max_length=100)
    question2 = forms.ChoiceField(choices=[('option1', 'Option 1'), ('option2', 'Option 2'), ('option3', 'Option 3')])
    question3 = forms.IntegerField(min_value=10, max_value=99)