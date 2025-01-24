import yagmail

sender_email = "remi.meson@gmail.com"
receiver_email = "fuoko.fr@gmail.com"
subject = "Vouz avez gagné un jambon de bayonne au porc noir de bigorre"
content = "Eh non pas de chance !"
fichier = '/home/spanmail/cle_mail.txt'

# Lire le fichier et stocker son contenu dans une variable 
with open(fichier, 'r', encoding='utf-8') as fichier: 
    password = fichier.read()

for i in range(10) :
    yag = yagmail.SMTP(sender_email, password)
    yag.send(to=receiver_email, subject=subject, contents=content)
print("Email envoyé avec succès !")