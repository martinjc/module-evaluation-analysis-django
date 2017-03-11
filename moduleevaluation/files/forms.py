# -*- coding: utf-8 -*-

from django import forms

from moduleevaluation.files.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['year', 'block', 'semester', 'docfile']
        labels = {
            'docfile': 'File to Upload'
        }
        help_texts = {
            'docfile': 'Select data file to upload'
        }
