from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from urllib.parse import quote

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


def send_destination_email(request):
    if request.method == 'POST':
        try:
            # Récupérer les données du formulaire
            nom = request.POST.get('nom', '').strip()
            adresse = request.POST.get('adresse', '').strip()
            email = request.POST.get('email', '').strip()
            phone = request.POST.get('phone', '').strip()
            nb_personnes = request.POST.get('nb_personnes', '').strip()
            date_depart = request.POST.get('date_depart', '').strip()
            date_retour = request.POST.get('date_retour', '').strip()
            destination = request.POST.get('destination', '').strip()
            commentaire = request.POST.get('commentaire', '').strip()

            # Valider les données importantes
            if not (nom and email and phone and date_depart and date_retour and destination):
                messages.error(request, "Veuillez remplir tous les champs obligatoires.")
                return render(request, 'madot/home.html')

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
                settings.DEFAULT_FROM_EMAIL,  # Adresse de l'expéditeur
                [settings.DEFAULT_FROM_EMAIL],  # Liste des destinataires
                fail_silently=False,
            )

            # Ajouter un message de succès
            messages.success(request, "Votre réservation a été envoyée avec succès !")

            # Rediriger vers la page de confirmation (ou une autre page)
            return redirect('home')

        except Exception as e:
            # En cas d'erreur, afficher un message d'erreur
            messages.error(request, f"Une erreur s'est produite : {str(e)}")
            return render(request, 'madot/home.html')

    # Si la requête n'est pas POST, simplement afficher la page
    return render(request, 'madot/home.html')


from urllib.parse import quote
from django.shortcuts import redirect
from django.contrib import messages

def send_to_whatsapp(request):
    if request.method == "POST":
        # Récupérer les données du formulaire
        destination = request.POST.get("destination1", "").strip()
        name = request.POST.get("yourname", "").strip()
        address = request.POST.get("youradresse", "").strip()
        email = request.POST.get("yourmail-adresse", "").strip()
        phone = request.POST.get("yourphone", "").strip()
        num_people = request.POST.get("nombre_personnes", "").strip()
        depart_date = request.POST.get("depart_date", "").strip()
        return_date = request.POST.get("retour_date", "Non spécifiée").strip()
        comments = request.POST.get("comments", "").strip()

        # Vérifier les champs obligatoires
        if not all([destination, name, phone, depart_date]):
            messages.error(request, "Veuillez remplir tous les champs obligatoires.")
            return redirect("/")

        # Numéro WhatsApp de l'agence
        agency_number = "261383073841"

        # Construire le message avec des sauts de ligne
        message = (
            f"Bonjour, je souhaite réserver un voyage :\n"
            f"Destination : {destination}\n"
            f"Nom : {name}\n"
            f"Adresse : {address}\n"
            f"Email : {email}\n"
            f"Téléphone : {phone}\n"
            f"Nombre de personnes : {num_people}\n"
            f"Date de départ : {depart_date}\n"
            f"Date de retour : {return_date}\n"
            f"Commentaires : {comments}"
        )

        # Encoder le message
        encoded_message = quote(message)

        # Vérifier l'OS pour déterminer si on redirige vers WhatsApp Desktop ou Web
        whatsapp_url = f"whatsapp://send?phone={agency_number}&text={encoded_message}"

        # Si le schéma whatsapp:// échoue, rediriger vers WhatsApp Web
        if not check_if_whatsapp_installed():
            whatsapp_url = f"https://web.whatsapp.com/send?phone={agency_number}&text={encoded_message}"

        # Rediriger vers l'URL WhatsApp
        return redirect(whatsapp_url)

    messages.error(request, "Méthode non autorisée.")
    return redirect("/")

# Fonction pour vérifier si WhatsApp est installé sur le système (placeholder, nécessite d'être implémentée dans un contexte adapté)
def check_if_whatsapp_installed():
    # Cette fonction peut vérifier l'installation de WhatsApp en fonction du système d'exploitation
    return False  # Placeholder pour une implémentation plus avancée



