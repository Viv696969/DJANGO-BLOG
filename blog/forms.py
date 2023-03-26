from django import forms
from .models import *
choice=Category.objects.values_list('name','name')
choice_list=[]
for c in choice:
    choice_list.append(c)

gender=[('male','male'),
('female','female'),
('other','other'),
]

class Blogform(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title','body','category','image']
        widgets={
            'title':forms.TextInput(attrs={'placeholder':'enter title','class':"form-control"}),
            'category':forms.Select(choices=choice_list,attrs={'class':"form-control",'placeholder':'select category'}),
            'body':forms.Textarea(attrs={'class':"form-control",'placeholder':'Enter your blog'})
        }


class Profileform(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['profile_pic','bio','email','m_no','sex','website','instagram','twitter']
        widgets={
            'sex':forms.RadioSelect(choices=gender),

            'bio':forms.Textarea(attrs={'class':"form-control"}),
            'email':forms.EmailInput(attrs={'class':"form-control"}),
            'm_no':forms.NumberInput(attrs={'class':"form-control"}),

            
            'website':forms.TextInput(attrs={'placeholder':'Enter your website link','class':"form-control"}),
            'instagram':forms.TextInput(attrs={'placeholder':'Enter your instagram account link link','class':"form-control"}),
            'twitter':forms.TextInput(attrs={'placeholder':'Enter your twitter account link','class':"form-control"})
        }