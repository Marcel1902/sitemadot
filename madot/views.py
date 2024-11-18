from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404

from sitemadot import settings
from .models import Destination
# Create your views here.
def home(request):
    destinations = Destination.objects.all()
    return render(request, 'madot/home.html', {'destinations': destinations})

def destination_details(request, id):
    destination = get_object_or_404(Destination, id=id)
    return render(request, 'madot/destination.html', {'destination': destination})


def send_contact_email(request):
    if request.method == 'POST':
        name = request.POST.get('nom')
        email = request.POST.get('email')
        sujet = request.POST.get('sujet')
        message = request.POST.get('message')

        # Envoie l'email
        send_mail(
            sujet,  # Sujet de l'email
            f"Nom : {name}\nEmail : {email}\nMessage : {message}",  # Contenu du message
            email,  # Adresse e-mail de l'expéditeur
            [settings.DEFAULT_FROM_EMAIL],  # Liste des destinataires
        )

    return render(request, 'madot/home.html')

from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render

def send_destination_email(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        nom = request.POST.get('nom')
        adresse = request.POST.get('adresse')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        nb_personnes = request.POST.get('nb_personnes')
        date_depart = request.POST.get('date_depart')
        date_retour = request.POST.get('date_retour')
        destination = request.POST.get('destination')
        commentaire = request.POST.get('commentaire')

        # Sujet de l'email
        sujet = "Nouvelle réservation de destination"

        # Contenu du message
        message = (
            f"Nom : {nom}\n"
            f"Adresse : {adresse}\n"
            f"Email : {email}\n"
            f"Téléphone : {phone}\n"
            f"Nombre de personnes : {nb_personnes}\n"
            f"Date de départ : {date_depart}\n"
            f"Date de retour : {date_retour}\n"
            f"Destination : {destination}\n"
            f"Commentaire : {commentaire}"
        )

        # Envoi de l'email
        send_mail(
            sujet,  # Sujet de l'email
            message,  # Contenu du message
            email,  # Adresse e-mail de l'expéditeur (utilisateur)
            [settings.DEFAULT_FROM_EMAIL],  # Liste des destinataires (vous)
        )

        # Ajouter un message de confirmation ou rediriger vers une page de succès
        return render(request, 'madot/home.html', {'success_message': 'Votre réservation a été envoyée avec succès !'})

    # Si la requête n'est pas POST, retournez simplement la page
    return render(request, 'madot/home.html')
