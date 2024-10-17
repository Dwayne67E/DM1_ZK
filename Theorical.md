# DM1 - Zero-Knowledge - ENKIRCHE Elias
## Les exercices ont été réalisé avec ChatGPT afin de bien comprendre et de faire une rédaction compréhensible 

### Exercice 1 : Non-résiduosité quadratique (2 points)

**Problème** :  
Construire un protocole à divulgation nulle de connaissance permettant à un prouveur, qui connaît la factorisation du module RSA \( N = p \cdot q \), de prouver à un vérifieur honnête que \( x \in Z^*_N \) n'est **pas un carré modulo \( N \)**, sans révéler d'autres informations.

#### Protocole proposé

1. **Préliminaires** :
   - \( N = p \cdot q \), où \( p \) et \( q \) sont deux grands nombres premiers.
   - \( x \in Z^*_N \) n’est pas un carré modulo \( N \) (c’est-à-dire qu'il n'existe pas de \( y \) tel que \( y^2 \equiv x \mod N \)).
   - Le prouveur connaît la factorisation de \( N \), ce qui lui permet de déterminer si un nombre est un carré modulo \( N \) en utilisant le symbole de Jacobi.

2. **Étapes du protocole** :
   - **Étape 1 : Engagement**  
     Le prouveur choisit un nombre aléatoire \( r \in Z^*_N \) et calcule \( a = r^2 \mod N \), qu'il envoie au vérifieur.
   
   - **Étape 2 : Défi**  
     Le vérifieur envoie un bit aléatoire \( e \in \{0, 1\} \) au prouveur.

   - **Étape 3 : Réponse**  
     - Si \( e = 0 \), le prouveur envoie \( r \).
     - Si \( e = 1 \), le prouveur envoie \( r \cdot x \mod N \).

   - **Étape 4 : Vérification**  
     - Si \( e = 0 \), le vérifieur vérifie que \( r^2 = a \mod N \).
     - Si \( e = 1 \), il vérifie que \( (r \cdot x)^2 = a \cdot x \mod N \).

3. **Propriétés** :
   - **Complétude** : Si \( x \) n'est pas un carré, le prouveur pourra toujours répondre correctement.
   - **Solidité** : Si \( x \) est un carré, un prouveur malhonnête ne pourra pas tromper le vérifieur sans connaître la racine carrée de \( x \).
   - **Divulgation nulle de connaissance** : Le vérifieur n'apprend rien de plus que le fait que \( x \) n'est pas un carré, grâce à l'utilisation du nombre aléatoire \( r \), garantissant la confidentialité.

---

### Exercice 2 : Preuve de connaissance d'une représentation (4 points)

**Problème** :  
On considère un groupe \( G \) d'ordre premier \( q \), avec \( g \) et \( h \) deux générateurs de \( G \). Un prouveur doit prouver de façon à divulgation nulle de connaissance (zero-knowledge proof) qu'il connaît les valeurs \( s \) et \( t \) telles que :
\[ y = g^s \cdot h^t \]
sans révéler ces valeurs au vérifieur.

#### Protocole proposé (Sigma-protocole)

1. **Étape 1 : Engagement**  
   Le prouveur choisit deux valeurs aléatoires \( r_1 \) et \( r_2 \) dans \( \mathbb{Z}_q \).  
   Il calcule :
   \[
   a = g^{r_1} \cdot h^{r_2}
   \]
   puis envoie \( a \) au vérifieur.

2. **Étape 2 : Défi**  
   Le vérifieur envoie un défi aléatoire \( e \in \mathbb{Z}_q \) au prouveur.

3. **Étape 3 : Réponse**  
   Le prouveur calcule deux réponses :
   \[
   z_1 = r_1 + e \cdot s \mod q
   \]
   \[
   z_2 = r_2 + e \cdot t \mod q
   \]
   Il envoie \( z_1 \) et \( z_2 \) au vérifieur.

4. **Étape 4 : Vérification**  
   Le vérifieur vérifie que l'égalité suivante est respectée :
   \[
   g^{z_1} \cdot h^{z_2} = a \cdot y^e
   \]
   Si l'égalité est vraie, il accepte la preuve.

#### Propriétés

- **Complétude** : Si le prouveur connaît \( s \) et \( t \), il pourra toujours répondre correctement au défi du vérifieur.
- **Solidité** : Si le prouveur ne connaît pas \( s \) et \( t \), il ne pourra pas deviner les réponses \( z_1 \) et \( z_2 \) correspondant à un engagement aléatoire \( a \).
- **Divulgation nulle de connaissance** : Le vérifieur n'apprend rien d'autre que le fait que le prouveur connaît \( s \) et \( t \), grâce à l'utilisation des valeurs aléatoires \( r_1 \) et \( r_2 \).

