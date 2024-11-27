# gestion_bibliotheque/forms.py
from django import forms
from .models import Abonne, Document, Emprunt

class AbonneForm(forms.ModelForm):
    class Meta:
        model = Abonne
        fields = ['cin', 'nom', 'prenom', 'adresse', 'date_inscription']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['titre', 'type', 'auteur', 'date_publication', 'disponibilite', 'fichier']

class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ['abonne', 'document', 'date_emprunt', 'date_retour', 'statut_emprunt']
        widgets = {
            'date_publication': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ajoute des classes Bootstrap pour la mise en forme
        self.fields['abonne'].widget.attrs.update({'class': 'form-select'})
        self.fields['document'].widget.attrs.update({'class': 'form-select'})
        self.fields['date_emprunt'].widget.attrs.update({'class': 'form-control', 'type': 'date'})
        self.fields['date_retour'].widget.attrs.update({'class': 'form-control', 'type': 'date'})
        self.fields['statut_emprunt'].widget.attrs.update({'class': 'form-select'})
