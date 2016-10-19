from django import forms

from .models import Directory


class StatisticsFiltersForm(forms.Form):
    directory = forms.ModelChoiceField(
        queryset=Directory.objects.filter(ignore=False), empty_label='(All)'
    )