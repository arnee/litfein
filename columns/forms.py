from django import forms
from elephantblog.models import CategoryTranslation as EntryCategoryTranslation


class EntryCategoryTranslationForm(forms.ModelForm):

    class Meta:
        model = EntryCategoryTranslation
        fields = ("title", "slug", "description",)

    def clean(self):
        self.cleaned_data["language_code"] = 'de'
        return self.cleaned_data
