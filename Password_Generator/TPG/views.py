from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from TPG import algorithm 
import random 
import os

def index(request):
    return render(request, "index.html")

def generate(request):
    
    files = ['TPG/static/Questions1.txt','TPG/static/Questions2.txt','TPG/static/Questions3.txt']

    questions = []

    for file_name in files:
    #     Open the file and read all the questions
        with open(file_name, 'r') as f:
            all_questions = f.read().splitlines()
            
        selected_question = random.choice(all_questions)
        questions.append(selected_question)
        all_questions.clear()


    question1 = questions[0]
    question2 = questions[1]
    question3 = questions[2]

    return render(request, 'generate.html', {'question1': question1, 'question2': question2, 'question3': question3 })

def results(request):
    #this could b ethe could then return the password at the end

    # Process the form submission and generate the password
   
    answer1 = request.POST.get('answer1')
    answer2 = request.POST.get('answer2')
    answer3 = request.POST.get('answer3')
    answers = [[answer1],[answer2,'happy'],[answer3]]
    password = algorithm.generate_password(answers)

    # Save the password in the session
    request.session['password'] = password

    # Render the results template with the password
    return render(request, "results.html",{'password':password})