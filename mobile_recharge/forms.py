from secrets import choice
from django import forms
from .models import recharge


demo_choice=(
    ('154','Unlimited data/ 30 days validaty'),
    ('99','validaty 28 days/ RS 89'),
)

class recharge_form(forms.ModelForm):
    class Meta:
        model=recharge
        fields=['number']
        Widgets={
            'number':forms.TextInput(attrs={'class':'form-control'}),
            'provider':forms.CharField(max_length=20),
            'plans':forms.MultipleChoiceField(choices=demo_choice),
        }

# class optr(forms.Form):
#     provider=forms.CharField(max_length=8)
