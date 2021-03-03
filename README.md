# CAS-PRATIQUE-1

## Contexte
Une entreprise qui analyse des commentaires youtube a viré pour incompétence un employé. 
Vous arrivez dans l'entreprise et vous devez réutiliser son code qui est une api flask et qui utilise un mysterieux joblib pour faire ces prédictions de sentiment sur des commentaires.

## Les données
Il s’agit d’un corpus (fichier “comments_train.csv”) de 1617 avis/commentaires d’utilisateurs sur des restaurants en Français :
Il est composé d’une colonne “comment” contenant les commentaires et d’une colonne “sentiment” indiquant si le commentaire est négatif ou positif.

Distribution des avis: négatif 598 (37%) | positif 1019 (63%)

### Pipelines testées
#### Pré-traitement du texte
- Aucun prétraitement  (“No tokenizer”)
- Tokenisation (“Simple tokenizer”)
- Tokenisation + stemming (“Stemm tokenizer”)
- Tokenisation + lemmatisation (“Spacy lemma tokenizer”)

#### Vectorisation 
- Countvectorizer (unigram ou bigram) 
- TF-IDF (unigram ou bigram) 

#### Classification
- Logistic regression 
- Naive Baye 
- Random Forest  
- SVM
