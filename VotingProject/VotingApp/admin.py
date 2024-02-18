from django.contrib import admin

#This code enables the functionality of the administrator to add questions and choices for users to vote for
#Code enabling changes that users can view on the site when voting 


#importing questions and choice classes from models
from .models import Question, Choice


#Headings on the admin page
admin.site.site_header = "Ballot Box"
admin.site.site_title = "Administrator Dashboard"
admin.site.index_title = "Welcome to Ballot Box's Administrator Dashboard. You are authorized to edit voting content here! :)"

#Creation of class: choiceInLine and questionAdmin, so that questions with respective choices can be created and added

class choiceInLineAdmin (admin.TabularInline):
    model = Choice #assigning model to choice class
    extra = 4 #specifying number of choices for each question


class questionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['question_text']}), ('Date Information', {'fields': ['pub_date'], 'classes':['collapse']}),] #Mapping fields to question text and relevant information about hwen question is created as a control measure
    inlines = [choiceInLineAdmin] #Declaring a variable assigned to the choiceInLineAdmin Class

    

admin.site.register(Question, questionAdmin)
# Registering the Question model with the questionAdmin class.
# This connects the Question model with the custom administration interface defined in questionAdmin.