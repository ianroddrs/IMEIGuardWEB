from django import forms
from .models import *

Inst = {
    (None,''),
    ('DETRAN','DETRAN'),
    ('PM','PM'),
    ('PC','PC'),
    ('SEGUP','SEGUP')
}

class FormUser(forms.ModelForm):
    nome_completo = forms.CharField(required=True, label="Nome completo", widget=forms.TextInput(attrs={'class':'form-control text-capitalize'}))
    instituicao = forms.ChoiceField(required=True,choices=Inst,widget=forms.Select(attrs={'class':'form-select'}),initial='')
    matricula_funcional = forms.IntegerField(required=True,widget=forms.TextInput(attrs={'class':'form-control', 'mask':'number'}))
    
    
    class Meta:
        model = ModelUsuarios
        fields = ['nome_completo', 'instituicao', 'matricula_funcional']