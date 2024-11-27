from django.test import TestCase
from BibliothequeApp.models import Abonne, Document, Emprunt

class AbonneModelTest(TestCase):
    def setUp(self):
        self.abonne = Abonne.objects.create(nom="Dupont", prenom="Jean", cin="12345678")

    def test_abonne_creation(self):
        self.assertEqual(self.abonne.nom, "Dupont")
        self.assertEqual(self.abonne.cin, "12345678")

class DocumentModelTest(TestCase):
    def setUp(self):
        self.document = Document.objects.create(titre="Livre Test", type="Livre")

    def test_document_creation(self):
        self.assertEqual(self.document.titre, "Livre Test")

class EmpruntModelTest(TestCase):
    def setUp(self):
        abonne = Abonne.objects.create(nom="Test", prenom="User", cin="87654321")
        document = Document.objects.create(titre="Document Test", type="Magazine")
        self.emprunt = Emprunt.objects.create(
            abonne=abonne,
            document=document,
            date_emprunt="2024-01-01",
            date_retour="2024-01-15",
            statut_emprunt="En cours"
        )

    def test_emprunt_creation(self):
        self.assertEqual(self.emprunt.statut_emprunt, "En cours")
