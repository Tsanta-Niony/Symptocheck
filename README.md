# SymptoCheck 🩺

## 1. Présentation du projet

**SymptoCheck** est une application web de prédiction diagnostique basée sur le Machine Learning. Elle permet aux utilisateurs de renseigner leur âge, leur origine ethnique et les symptômes qu'ils présentent afin d'obtenir une prédiction parmi neuf maladies.

Le projet utilise un modèle de **régression logistique (Logistic Regression)** entraîné à partir de données relatives aux symptômes et aux maladies.

SymptoCheck a pour objectif de contribuer à l'amélioration de l'accès aux outils d'aide à l'orientation médicale, notamment dans des contextes où l'accès aux professionnels de santé peut être limité.

> **Avertissement médical :** SymptoCheck est un prototype expérimental d'aide à l'orientation. Ses prédictions ne constituent pas un diagnostic médical et ne remplacent ni une consultation ni l'avis d'un professionnel de santé.

## 2. Objectifs du projet

- Développer une application web de prédiction diagnostique à l'aide du Machine Learning.
- Exploiter les symptômes déclarés par l'utilisateur pour générer une prédiction.
- Présenter les résultats de prédiction dans une interface simple et accessible.
- Explorer les possibilités de l'intelligence artificielle dans le domaine de la santé à Madagascar.
- Encourager les utilisateurs à consulter des professionnels de santé pour une évaluation médicale appropriée.

## 3. Maladies prises en compte

Le modèle vise à prédire neuf catégories de maladies :

1. Asthme (Asthma)
2. Bronchopneumopathie chronique obstructive (COPD/BPCO)
3. Diabète (Diabetes)
4. Maladies cardiaques (Heart Disease)
5. Hypertension (Hypertension)
6. Paludisme (Malaria)
7. Fièvre typhoïde (Typhoid)
8. Ulcère (Ulcer)
9. Infection par le VIH (HIV)

Les catégories exactes retournées dépendent des étiquettes utilisées lors de l'entraînement du modèle.

## 4. Technologies utilisées

- **Python** : langage de programmation principal.
- **Flask** : framework web pour le serveur et la gestion des requêtes.
- **Scikit-learn** : entraînement et utilisation du modèle de Machine Learning.
- **Pandas** : manipulation des données.
- **NumPy** : traitement des données numériques.
- **Joblib** : chargement du modèle entraîné.
- **HTML5** : structure des pages web.
- **CSS3** : mise en forme de l'interface.
- **JavaScript** : interactions côté client.

## 5. Structure du projet

```text
SymptoCheck/
│
├── app.py
├── requirements.txt
│
├── model/
│   └── 9_diseases_logistic_regression_model.pkl
│
├── templates/
│   ├── home.html
│   ├── Key_objectives.html
│   ├── the_9_diseases.html
│   ├── About.html
│   ├── start_diagnosis.html
│   └── Answer.html
│
├── static/
│   ├── css/
│   │   
│   ├── js/
│   │   
│   └── images/
│
└── README.md
```


## 6. Installation

### Prérequis

Installer :

- Python 3.10 ou une version compatible avec les dépendances du projet.
- pip, le gestionnaire de paquets Python.

### Étape 1 : Cloner le projet

```bash
git clone <URL_DU_DEPOT>
cd SymptoCheck
```

Remplacer `<URL_DU_DEPOT>` par l'adresse réelle du dépôt.

### Étape 2 : Créer un environnement virtuel

Sous Windows :

```bash
python -m venv venv
venv\Scripts\activate
```

Sous Linux ou macOS :

```bash
python3 -m venv venv
source venv/bin/activate
```

### Étape 3 : Installer les dépendances

```bash
pip install -r requirements.txt
```

Ou installer les principales bibliothèques nécessaires :

```bash
pip install Flask numpy pandas scikit-learn joblib
```

Il est recommandé de conserver les versions des bibliothèques compatibles avec celles utilisées pour entraîner le modèle.

## 7. Lancement de l'application

Vérifiez que le modèle entraîné se trouve dans le dossier `model/` et que son nom correspond à celui indiqué dans `app.py`.

Lancez ensuite le serveur Flask :

```bash
python app.py
```

Ouvrez votre navigateur et accédez à :

```text
http://127.0.0.1:5000/
```

Vous pourrez alors naviguer dans l'application et accéder au formulaire de diagnostic.

## 8. Fonctionnement de l'application

Le parcours utilisateur se déroule en plusieurs étapes :

1. **Accueil :** présentation de SymptoCheck.
2. **Saisie des informations :** l'utilisateur renseigne son nom, son âge et son origine ethnique.
3. **Sélection des symptômes :** les symptômes présents sont indiqués dans le formulaire.
4. **Préparation des données :** Flask récupère les réponses et les convertit au format attendu par le modèle.
5. **Prédiction :** le modèle de régression logistique estime la classe prédite.
6. **Affichage du résultat :** la page `Answer.html` affiche le nom de l'utilisateur, la maladie prédite et, si elle est disponible, la probabilité associée.

La cohérence entre les champs HTML, leur encodage et l'ordre des caractéristiques utilisées pendant l'entraînement est essentielle au bon fonctionnement de la prédiction.

## 9. Modèle de Machine Learning

Le modèle utilisé est une régression logistique multiclasse enregistrée au format `.pkl`.

Le processus général comprend :

- La collecte et la préparation des données.
- L'encodage des caractéristiques.
- L'entraînement du modèle.
- L'enregistrement du modèle entraîné.
- Le chargement du modèle dans Flask.
- La prédiction à partir des réponses du formulaire.

Les performances réelles du modèle doivent être évaluées sur un jeu de données indépendant. Une probabilité élevée affichée par le modèle ne garantit pas qu'une prédiction soit médicalement correcte.

## 10. Améliorations possibles

Plusieurs évolutions peuvent être envisagées :

- Enrichir et diversifier le jeu de données.
- Évaluer les performances pour chaque maladie.
- Améliorer la validation des informations saisies.
- Ajouter une interface multilingue, notamment en français et en malgache.
- Améliorer l'accessibilité et l'expérience utilisateur.
- Collaborer avec des professionnels de santé pour évaluer la pertinence clinique du système.
- Renforcer la protection des données personnelles et médicales.

## 11. Limites et précautions

SymptoCheck est un projet expérimental. La fiabilité des résultats dépend notamment de la qualité, de la représentativité et de la pertinence des données utilisées pour entraîner le modèle.

L'application ne doit pas être utilisée seule pour prendre des décisions médicales, commencer ou arrêter un traitement, ou retarder une consultation.

Les données de santé étant sensibles, leur collecte, leur stockage et leur traitement doivent respecter les règles applicables en matière de confidentialité et de protection des données.

## 12. Auteur et contribution

**Projet :** SymptoCheck  
**Domaine :** Intelligence artificielle et santé numérique  
**Technologies principales :** Python, Flask et Machine Learning

Ce projet s'inscrit dans une démarche d'exploration de l'intelligence artificielle au service de la santé et de l'amélioration de l'accès aux outils numériques d'aide à l'orientation médicale à Madagascar.

---

*SymptoCheck — Exploring Machine Learning for Healthcare Support.*
