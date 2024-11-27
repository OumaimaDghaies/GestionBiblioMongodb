from django.test import TestCase
from .models import Abonne, Document, Emprunt
from datetime import date

#model
class AbonneTest(TestCase):
    def setUp(self):
        self.abonne = Abonne.objects.create(
            cin=12345678,
            nom="Doe",
            prenom="John",
            adresse="123 Main St",
            date_inscription=date.today()
        )

    def test_abonne_creation(self):
        abonne = self.abonne
        self.assertEqual(abonne.nom, "Doe")
        self.assertEqual(abonne.prenom, "John")
        self.assertTrue(isinstance(abonne, Abonne))
        self.assertEqual(str(abonne), "Doe John")

class DocumentTest(TestCase):
    def setUp(self):
        self.document = Document.objects.create(
            titre="Document Title",
            type="Livre",
            auteur="Auteur X",
            date_publication=date.today(),
            disponibilite=True
        )

    def test_document_creation(self):
        document = self.document
        self.assertEqual(document.titre, "Document Title")
        self.assertTrue(document.disponibilite)

class EmpruntTest(TestCase):
    def setUp(self):
        self.abonne = Abonne.objects.create(
            cin=12345678,
            nom="Doe",
            prenom="John",
            adresse="123 Main St",
            date_inscription=date.today()
        )
        self.document = Document.objects.create(
            titre="Document Title",
            type="Livre",
            auteur="Auteur X",
            date_publication=date.today(),
            disponibilite=True
        )
        self.emprunt = Emprunt.objects.create(
            abonne=self.abonne,
            document=self.document,
            date_emprunt=date.today(),
            date_retour=date.today(),
            statut_emprunt="En cours"
        )

    def test_emprunt_creation(self):
        emprunt = self.emprunt
        self.assertEqual(emprunt.statut_emprunt, "En cours")
        self.assertEqual(emprunt.abonne.nom, "Doe")
        self.assertEqual(emprunt.document.titre, "Document Title")
        self.assertTrue(isinstance(emprunt, Emprunt))






#Vue
from django.urls import reverse
from django.test import TestCase

class EmpruntViewTest(TestCase):
    def setUp(self):
        self.abonne = Abonne.objects.create(
            cin=12345678,
            nom="Doe",
            prenom="John",
            adresse="123 Main St",
            date_inscription=date.today()
        )
        self.document = Document.objects.create(
            titre="Document Title",
            type="Livre",
            auteur="Auteur X",
            date_publication=date.today(),
            disponibilite=True
        )
        self.emprunt = Emprunt.objects.create(
            abonne=self.abonne,
            document=self.document,
            date_emprunt=date.today(),
            date_retour=date.today(),
            statut_emprunt="En cours"
        )

    def test_emprunt_create_view(self):
        # Tester la vue de création d'emprunt
        url = reverse('emprunt_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'emprunt_create.html')
        self.assertContains(response, 'Créer un Emprunt')

    def test_emprunt_list_view(self):
        # Tester la vue de liste d'emprunts
        url = reverse('emprunt_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'emprunt_list.html')
        self.assertContains(response, 'Document Title')
        self.assertContains(response, 'Doe')


#formulaire
from django.test import TestCase
from .forms import EmpruntForm

class EmpruntFormTest(TestCase):
    from django.test import TestCase
from .forms import EmpruntForm

class EmpruntFormTest(TestCase):
    def test_emprunt_form_valid(self):
        data = {
            'abonne': 1,  # Assure-toi que l'ID d'un abonné valide existe
            'document': 1,  # Assure-toi que l'ID d'un document valide existe
            'date_emprunt': '2024-11-23',
            'date_retour': '2024-11-30',
            'statut_emprunt': 'En cours',
        }
        form = EmpruntForm(data)
        if not form.is_valid():
            print(form.errors)  # Affiche les erreurs du formulaire
        self.assertTrue(form.is_valid())


    def test_emprunt_form_invalid(self):
        data = {
            'abonne': '',  # Champ manquant
            'document': '',  # Champ manquant
            'date_emprunt': '',
            'date_retour': '',
            'statut_emprunt': '',
        }
        form = EmpruntForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5)  # Vérifie le nombre d'erreurs
