
from django import forms
from matriapp.models import Step1,Step2,Step3,Step4
from django.forms.widgets import Media,MediaDefiningClass,Widget,TextInput,NumberInput,EmailInput,URLInput,PasswordInput,HiddenInput,MultipleHiddenInput,FileInput,ClearableFileInput,Textarea,DateInput,DateTimeInput,TimeInput,CheckboxInput,Select,NullBooleanSelect,SelectMultiple,RadioSelect,CheckboxSelectMultiple,MultiWidget,SplitDateTimeWidget,SplitHiddenDateTimeWidget,SelectDateWidget


dosham=(
    ('yes',"YES"),
    ('no','NO'),
    ("don't","Don't know")
)
maritalstatus=(
    ('Never Married ','Never Married '),
    ('Widowed ','Widowed '),
    ('Divorced','Divorced'),
    ('Awaiting divorce','Awaiting divorce')
)

messages.error(request, "Invalid credentials")

class Step1_Form(forms.ModelForm):
    Dosham=forms.ChoiceField(choices=dosham, widget=forms.RadioSelect(attrs={'class': 'special',}),)
    MaritalStatus=forms.ChoiceField(choices=maritalstatus,widget=forms.RadioSelect(attrs={'class':'special'}))
    class Meta:
        model=Step1
        fields = "__all__"
        

class Step2_Form(forms.ModelForm):
    class Meta:
        model=Step2
        fields="__all__"

class Step3_Form(forms.ModelForm):
    class Meta:
        model=Step3
        fields="__all__"

class Step4_Form(forms.ModelForm):
    class Meta:
        model=Step4
        fields="__all__"                

