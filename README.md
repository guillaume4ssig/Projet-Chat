# Projet Technologies Web II / Programmation Web - Site de chat centralisé
Ce projet consiste en la réalisation d’un site de chat en ligne développé avec **Django**.  
Il combine :

- **l’aspect serveur** : gestion des utilisateurs, des salons et des messages, conception des modèles, des vues et des URLs, stockage et modification des données.
- **l’aspect client** : rendu dynamique des pages HTML, rafraîchissement automatique des messages via Javascript et AJAX pour un fonctionnement en quasi-temps réel.

---

## Auteurs

PASTRES Nolan, SCHOSSIG Guillaume, MALEGUE Gabriel  (1A IR)
---

## Description

L’application permet à des utilisateurs de s’inscrire, se connecter et participer à des salons de discussion.  
Chaque salon possède un administrateur capable de gérer les membres (exclusion) et la suppression du salon.  
Les messages sont affichés dynamiquement sans rechargement de la page grâce à une communication AJAX entre le client et le serveur.

Le projet repose sur le framework **Django**, en utilisant :
- le système d’authentification intégré (Django Auth),
- une base de données **SQLite**,
- du Javascript pour le rafraîchissement dynamique des messages.

---

## Organisation du projet
```bash
Projet_Chat/
│
├── accounts/            # Gestion des utilisateurs (signup, login, logout)
├── chat_messages/       # Gestion des salons, messages et modération
├── Projet_Chat/         # Configuration globale du projet Django
│   ├── settings.py      # Configuration globale de Django
│   ├── urls.py          # Routage principal
│   ├── wsgi.py          # Point d’entrée WSGI
├── static/              # Fichiers statiques (CSS, JS)
├── requirement.txt      # Pour créer l’environnement virtuel
├── manage.py            # Point d’entrée de Django
├── venv/                # Environnement virtuel (à générer)
├── db.sqlite3           # Base de données SQLite (à générer)
├── staticfiles          # Fichiers statiques pour le widget des emojis (à générer)
└── README.md
```

## Lancement du projet

### 1. Création et activation de l’environnement virtuel

```bash
python -m venv venv
source venv/bin/activate
```

### 2. Installation des dépendances

```bash
pip install -r requirements.txt
```

### 3. Génération de la base de données, application des migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Génération des fichiers statiques

```bash
python manage.py collectstatic
```

### 5. Serveur

Serveur de développment

```bash
python manage.py runserver
```

Pour un serveur, compléter dans le fichier `settings.py`

```bash
ALLOWED_HOSTS = ["nom_de_domaine_ou_ip_du_serveur"]
```

Penser à stocker dans une variable d’environnement la `SECRET_KEY`, enlever le debug…

## Fonctionnalités principales

- Inscription, connexion et déconnexion des utilisateurs
- Création et suppression de salons
- Gestion des membres (rejoindre/exclure)
- Envoi et affichage des messages
- Rafraîchissement dynamique du chat via AJAX
- Distinction visuelle entre les messages de l’utilisateur courant et ceux des autres

## Améliorations possibles
- Mise en place de WebSockets (Django Channels) pour un vrai temps réel
- Ajout de notifications
- Renforcement de la gestion des permissions
- Beauté globale du site avec Bootstrap