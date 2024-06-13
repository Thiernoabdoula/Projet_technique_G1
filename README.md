# Projet_technique_G1

=============À propos de l'ensemble de données===============

Il s'agit d'un ensemble de données sur les ventes de produits extrait du site Web d'Amazon.
Ses données produits sont séparées par 142 catégories au format csv, ainsi que par le nom complet de l'ensemble de données Amazon-Products.csv .
Chaque fichier CSV est composé de 10 colonnes et chaque ligne contient les détails des produits en conséquence


===============Présentation pas à pas de l'ensemble de données=============

- Prétraitement des données
- Comprendre la hiérarchie des ensembles de données
- L'analyse exploratoire des données
- Visualisation des données à l'aide de Matlabplot et Searborn
- Visualisation des données à l'aide d'outils BI avec que Tableau
- Faire un système de recommandation

=======Commentaire du code python========================

Ce code est une implémentation d'un modèle de régression pour prédire le prix réduit d'un produit en fonction de ses caractéristiques.
 Le code utilise les bibliothèques suivantes : pandas, matplotlib, numpy, plotly, seaborn, sklearn et xgboost.

Le code commence par télécharger un fichier CSV contenant les données des produits. Ensuite, il lit le fichier CSV et affiche les premières lignes du DataFrame. Il affiche également des informations sur le DataFrame, sa taille et sa description.

Le code supprime ensuite les colonnes inutiles et affiche à nouveau les premières lignes du DataFrame. Il vérifie ensuite les valeurs manquantes et supprime les lignes contenant des valeurs manquantes dans les colonnes
"ratings" et
"no_of_ratings".

Le code nettoie ensuite les données en supprimant les caractères spéciaux et en convertissant les colonnes en
type
float. Il affiche à nouveau les premières lignes du DataFrame.

Le code supprime ensuite les lignes contenant des valeurs manquantes dans les colonnes
"discount_price" et
"actual_price". Il réinitialise ensuite l'index du DataFrame et affiche à nouveau les premières lignes du DataFrame.

Le code crée ensuite un LabelEncoder pour encoder les catégories principales et secondaires. Il affiche à nouveau les premières lignes du DataFrame.

Le code nettoie ensuite les données en supprimant les caractères spéciaux et en convertissant les colonnes en
type
float. Il affiche à nouveau les premières lignes du DataFrame.

Le code supprime ensuite les lignes contenant des valeurs manquantes dans les colonnes
"ratings",
"no_of_ratings",
"discount_price". Il définit ensuite les variables X et y.

Le code sépare ensuite les données en train et en test. Il affiche les tailles des ensembles de train et de test.

Le code affiche ensuite le nombre de notes par catégorie.

Le code implémente ensuite deux modèles de régression : Random Forest et XGBoost. Il entraîne les deux modèles sur l'ensemble de train et prédit les prix réduits sur l'ensemble
 de test.

Le code affiche ensuite les performances des deux modèles et sélectionne le meilleur modèle en fonction de son score.

Le code sauvegarde ensuite le meilleur modèle dans un fichier pickle.

Enfin, le code affiche un readme du code.

