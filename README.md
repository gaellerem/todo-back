# Todo Back

API REST de gestion de tâches et de catégories, construite avec Django et Django REST Framework.

## Prérequis

- Python 3.12 ou une version compatible avec Django 6
- `pip`

## Installation et lancement local

Depuis la racine du dépôt, créez et activez un environnement virtuel, puis installez les dépendances du projet :

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r project/requirements.txt
```

Initialisez la base SQLite et démarrez le serveur de développement :

```powershell
python project/manage.py migrate
python project/manage.py runserver
```

L'API est alors disponible à l'adresse `http://127.0.0.1:8000/api/`.

## Routes principales

| Méthode | Route | Description |
| --- | --- | --- |
| `GET`, `POST` | `/api/categories/` | Lister ou créer des catégories |
| `GET`, `POST` | `/api/tasks/` | Lister ou créer des tâches |
| `GET`, `PUT`, `PATCH`, `DELETE` | `/api/tasks/<id>/` | Consulter, modifier ou supprimer une tâche |
| `GET` | `/api/health/` | Vérifier l'état de l'API |

La liste des tâches peut être filtrée par catégorie avec `GET /api/tasks/?category=<id>`.
Pour créer une tâche, fournissez notamment `description` et `category_id` :

```json
{
  "description": "Préparer le rapport",
  "category_id": 1
}
```

## Tests

Depuis la racine du dépôt :

```powershell
python project/manage.py test api
```

## Déploiement

Le `Procfile` décrit le démarrage avec Gunicorn et les réglages `project.settings.production`. Cette configuration attend notamment `SECRET_KEY`, `ALLOWED_HOSTS` et une URL de base de données compatible avec `dj-database-url`. `CORS_ALLOWED_ORIGINS` et `SENTRY_DSN` sont également configurables par variables d'environnement.