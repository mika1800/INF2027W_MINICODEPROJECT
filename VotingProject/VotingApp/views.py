from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.urls import reverse
from .models import Question, Choice, Choice_collection, Question_collection #Importing question and choice classes from models and collections for the no sql mongo DB

#Function created to retrieve questions and displays those
def index (request):
    recent_question_list = Question.objects.order_by('-pub_date')[:5] #Taking questions and ordering them by date but in reverse so most recent questions are displayed
    context = {'recent_question_list': recent_question_list}       
    return render(request, 'polls/index.html', context)  



#Function created to display a question and its specific associated choices
def detail(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404('The following question does not exist')
    return render(request, 'polls/detail.html', 
                    {'question': question})


                          
#Function created to get question and display results
def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/results.html',                  
                    {'question':question})



#Function created to gather the number of votes per question choice
def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', 
                      { 'question': question,
                        'error_message': 'Please select a choice below.'})
    
    else:
        selected_choice.votes += 1
        selected_choice.save()
        choices = {
            'Question': question.question_text, #This is to 
            'Choice': selected_choice.choice_text
        }
        Choice_collection.insert_one(choices)
        return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))
    