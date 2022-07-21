from django import forms

class PostForm(forms.Form):
	cName = forms.CharField(max_length=20,initial='Willy_guo')
	cSex = forms.CharField(max_length=2,initial='M')	
	cBirthday = forms.DateField()
	cEmail = forms.EmailField(max_length=100,initial='',required=False)
	cPhone = forms.CharField(max_length=50,initial='',required=False)
	cAddr = forms.CharField(max_length=255,initial='',required=False)

class Requisition(forms.Form):
    cName = forms.CharField(max_length=20, initial= '',)
    cNumber = forms.CharField(max_length=20, initial= '',)
    cProjectname = forms.CharField(max_length=20, initial= '')
    cCusetername = forms.CharField(max_length=20, initial='')
    cProjectcode = forms.CharField(max_length=20, initial='')
    cLocation = forms.CharField(max_length=100, initial='',required=False)
    cContent = forms.CharField(max_length=100, initial='',required=False)
    cLastproject = forms.CharField(max_length=100, initial='',required=False)
    cAbility = forms.CharField(max_length=100, initial='',required=False)
    cType = forms.CharField(max_length=100, initial='',required=False)
    cCotpye = forms.CharField(max_length=100, initial='',required=False)
    cProjecttype = forms.CharField(max_length=100, initial='',required=False)
    cStage = forms.CharField(max_length=100, initial='',required=False)
    cNoted = forms.CharField(max_length=100,initial='',required=False) 