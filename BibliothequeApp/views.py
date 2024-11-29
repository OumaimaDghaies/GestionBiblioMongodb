from pyexpat.errors import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Abonne, Document, Emprunt
from .forms import AbonneForm, DocumentForm, EmpruntForm  
from django.contrib.auth import authenticate, login, logout


# Vues pour Abonne
from django.contrib import messages

def abonne_list(request):
    query = request.GET.get('q', '').strip()  # Récupère le paramètre 'q' depuis l'URL
    if query:  # Si une recherche est effectuée
        abonnes = Abonne.objects.filter(nom__icontains=query)  # Recherche insensible à la casse
    else:  # Si aucune recherche, renvoyer tous les abonnés
        abonnes = Abonne.objects.all()

    return render(request, 'abonne_list.html', {'abonnes': abonnes, 'query': query})

def abonne_create(request):
    if request.method == 'POST':
        form = AbonneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('abonne_list')  
    else:
        form = AbonneForm()
    return render(request, 'abonne_create.html', {'form': form})

def abonne_update(request, id):
    abonne = get_object_or_404(Abonne, id=id) 
    if request.method == 'POST':
        form = AbonneForm(request.POST, instance=abonne)
        if form.is_valid():
            form.save()
            return redirect('abonne_list')  
    else:
        form = AbonneForm(instance=abonne)
    return render(request, 'abonne_update.html', {'form': form, 'abonne': abonne})

def abonne_delete(request, id):
    abonne = get_object_or_404(Abonne, id=id) 
    if request.method == 'POST':
        abonne.delete()  
        return redirect('abonne_list')  
    return render(request, 'abonne_delete.html', {'abonne': abonne})

# Vues pour Document
def document_list(request):
    documents = Document.objects.all()  
    return render(request, 'document_list.html', {'documents': documents})

def document_create(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)  # Ajoute request.FILES pour gérer les fichiers
        if form.is_valid():
            form.save()
            return redirect('document_list')  
    else:
        form = DocumentForm()
    return render(request, 'document_create.html', {'form': form})

def document_update(request, id):
    document = get_object_or_404(Document, id=id)  # Récupère l'objet à modifier
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=document)  # Lie l'instance au formulaire
        if form.is_valid():
            form.save()
            return redirect('document_list')  
    else:
        form = DocumentForm(instance=document)  # Pré-remplit le formulaire avec les données existantes
    return render(request, 'document_update.html', {'form': form, 'document': document})

def document_delete(request, id):
    document = get_object_or_404(Document, id=id)  
    if request.method == 'POST':
        document.delete()  
        return redirect('document_list')  
    return render(request, 'document_delete.html', {'document': document})

# Vues pour Emprunt
def emprunt_list(request):
    emprunts = Emprunt.objects.all()  
    return render(request, 'emprunt_list.html', {'emprunts': emprunts})

def emprunt_create(request):
    from .models import Abonne, Document  # S'assurer que les modèles sont correctement importés
    
    abonnes = Abonne.objects.all()  # Récupère tous les abonnés
    documents = Document.objects.all()  # Récupère tous les documents
    
    if request.method == 'POST':
        # Récupération des données du formulaire
        abonne_id = request.POST.get('abonne')
        document_id = request.POST.get('document')
        date_emprunt = request.POST.get('date_emprunt')
        date_retour = request.POST.get('date_retour')
        statut_emprunt = request.POST.get('statut_emprunt')

        # Création de l'emprunt
        if abonne_id and document_id:
            Emprunt.objects.create(
                abonne_id=abonne_id, 
                document_id=document_id,
                date_emprunt=date_emprunt,
                date_retour=date_retour,
                statut_emprunt=statut_emprunt
            )
            return redirect('emprunt_list')
    return render(request, 'emprunt_create.html', {
        'abonnes': abonnes,
        'documents': documents,
    })

def emprunt_update(request, id):
    emprunt = get_object_or_404(Emprunt, id=id)
    abonnes = Abonne.objects.all()
    documents = Document.objects.all()
    if request.method == 'POST':
        form = EmpruntForm(request.POST, instance=emprunt)
        if form.is_valid():
            form.save()
            return redirect('emprunt_list')
    else:
        form = EmpruntForm(instance=emprunt)
    return render(request, 'emprunt_update.html', {'form': form, 'abonnes': abonnes, 'documents': documents})

def emprunt_delete(request, id):
    emprunt = get_object_or_404(Emprunt, id=id)  
    if request.method == 'POST':
        emprunt.delete() 
        return redirect('emprunt_list')  
    return render(request, 'emprunt_delete.html', {'emprunt': emprunt})


def dashboard(request):
   
    count_abonne = Abonne.objects.count()
    count_document = Document.objects.count()
    count_emprunt = Emprunt.objects.count()

    
    return render(request, 'dashboard.html', {
        'count_abonne': count_abonne,
        'count_document': count_document,
        'count_emprunt': count_emprunt,
    })

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Récupère le champ 'username'
        password = request.POST.get('password')  # Récupère le champ 'password'

        # Vérification des champs vides
        if not username or not password:
            messages.error(request, "Veuillez remplir tous les champs.")
            return render(request, 'login.html')

        # Authentification de l'utilisateur
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Connecte l'utilisateur
            next_url = request.GET.get('next', 'dashboard')  # Redirige vers 'next' ou la page 'dashboard'
            return redirect(next_url)
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
            return render(request, 'login.html')
    
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')  