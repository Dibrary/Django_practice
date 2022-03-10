from django.contrib import admin
from polls.models import Question, Choice

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline): # 이렇게 하면 테이블 형식으로 바뀜
    model = Choice
    extra = 2 # 추가로 2개의 항목? 이 더 나오게 함.

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text'] # 순서를 date, text로 변경함.
    fieldsets = [
        ('Question Statement', {'fields':['question_text']}),
        ('Date Information', {'fields':['pub_date'], 'classes':['collapse']})
    ]
    inlines = [ChoiceInline] # Choice 입력 화면도 Question에 같이 나타나게 함.
    list_display = ('question_text', 'pub_date') # question 화면에서 date도 같이 나오게 함.
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

