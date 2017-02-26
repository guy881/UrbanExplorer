# -*- coding: utf-8 -*-
from django import forms



class QuestionsForm(forms.Form):
    question_id = forms.IntegerField(widget=forms.HiddenInput)
    answer = forms.CharField(label='', widget=forms.TextInput, required=True)

    def __init__(self, *args, **kwargs):
        super(QuestionsForm, self).__init__(*args, **kwargs)
        if (kwargs.get('initial',False)):
            self.fields['answer'].label = kwargs['initial']['question_content']

from django.forms import formset_factory
QuestionsFormSet = formset_factory(QuestionsForm, extra=0)