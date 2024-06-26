from django import forms
from .models import Workout

class CreateWorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'description', 'video_file', 'type', 'image', 'duration']
