from django import forms
from musicboxapp.models import Review

class ReviewForm(forms.ModelForm):
    Album = forms.CharField(max_length=50)
    Rating = forms.FloatField(default=0)
    Review = forms.TextField(max_length=1000)

    class Meta:
        model = Review
        feilds = ('Album', 'User', 'Rating', 'Review', 'Date_Of_Review')
