# DM1 - Zero-Knowledge - ENKIRCHE Elias
## Les exercices ont été réalisé avec l'aide d'une IA (ChatGPT) afin de bien comprendre et de faire une rédaction compréhensible 

### Exercice 1 : Non-résiduosité quadratique 

**Problème** :  
Construire un protocole à divulgation nulle de connaissance permettant à un prouveur, qui connaît la factorisation du module RSA \( N = p * q \), de prouver à un vérifieur honnête que \( x \in Z^*_N \) n'est **pas un carré modulo \( N \)**, sans révéler d'autres informations.

#### Protocole proposé

1. **Préliminaires** :
   - \( N = p * q \), où \( p \) et \( q \) sont deux grands nombres premiers.
   - \( x \in Z^*_N \) n’est pas un carré modulo \( N \) (c’est-à-dire qu'il n'existe pas de \( y \) tel que \( y^2 \equiv x \mod N \)).
   - Le prouveur connaît la factorisation de \( N \), ce qui lui permet de déterminer si un nombre est un carré modulo \( N \) en utilisant le symbole de Jacobi.

2. **Étapes du protocole** :
   - **Étape 1 : Engagement**  
     Le prouveur choisit un nombre aléatoire \( r \in Z^*_N \) et calcule \( a = r^2 \mod N \), qu'il envoie au vérifieur.
   
   - **Étape 2 : Défi**  
     Le vérifieur envoie un bit aléatoire \( e \in \{0, 1\} \) au prouveur.

   - **Étape 3 : Réponse**  
     - Si \( e = 0 \), le prouveur envoie \( r \).
     - Si \( e = 1 \), le prouveur envoie \( r * x \mod N \).

   - **Étape 4 : Vérification**  
     - Si \( e = 0 \), le vérifieur vérifie que \( r^2 = a \mod N \).
     - Si \( e = 1 \), il vérifie que \( (r * x)^2 = a * x \mod N \).

3. **Propriétés** :
   - **Complétude** : Si \( x \) n'est pas un carré, le prouveur pourra toujours répondre correctement.
   - **Solidité** : Si \( x \) est un carré, un prouveur malhonnête ne pourra pas tromper le vérifieur sans connaître la racine carrée de \( x \).
   - **Divulgation nulle de connaissance** : Le vérifieur n'apprend rien de plus que le fait que \( x \) n'est pas un carré, grâce à l'utilisation du nombre aléatoire \( r \), garantissant la confidentialité.

---

### Exercice 2 : Preuve de connaissance d'une représentation

**Problème** :  
On considère un groupe \( G \) d'ordre premier \( q \), avec \( g \) et \( h \) deux générateurs de \( G \). Un prouveur doit prouver de façon à divulgation nulle de connaissance (zero-knowledge proof) qu'il connaît les valeurs \( s \) et \( t \) telles que :
\[ y = g^s * h^t \]
sans révéler ces valeurs au vérifieur.

#### Protocole proposé (Sigma-protocole)

1. **Étape 1 : Engagement**  
   Le prouveur choisit deux valeurs aléatoires \( r_1 \) et \( r_2 \) dans \( \mathbb{Z}_q \).  
   Il calcule :
   \[
   a = g^{r_1} * h^{r_2}
   \]
   puis envoie \( a \) au vérifieur.

2. **Étape 2 : Défi**  
   Le vérifieur envoie un défi aléatoire \( e \in \mathbb{Z}_q \) au prouveur.

3. **Étape 3 : Réponse**  
   Le prouveur calcule deux réponses :
   \[
   z_1 = r_1 + e * s \mod q
   \]
   \[
   z_2 = r_2 + e * t \mod q
   \]
   Il envoie \( z_1 \) et \( z_2 \) au vérifieur.

4. **Étape 4 : Vérification**  
   Le vérifieur vérifie que l'égalité suivante est respectée :
   \[
   g^{z_1} * h^{z_2} = a * y^e
   \]
   Si l'égalité est vraie, il accepte la preuve.

#### Propriétés

- **Complétude** : Si le prouveur connaît \( s \) et \( t \), il pourra toujours répondre correctement au défi du vérifieur.
- **Solidité** : Si le prouveur ne connaît pas \( s \) et \( t \), il ne pourra pas deviner les réponses \( z_1 \) et \( z_2 \) correspondant à un engagement aléatoire \( a \).
- **Divulgation nulle de connaissance** : Le vérifieur n'apprend rien d'autre que le fait que le prouveur connaît \( s \) et \( t \), grâce à l'utilisation des valeurs aléatoires \( r_1 \) et \( r_2 \).

---

### Exercice 3 : Un vote électronique simple

Supposons que \( n \) personnes votent entre deux candidats, avec le protocole suivant :

- Une autorité de confiance choisit un chiffrement à clé publique avec une paire clé privée/clé publique ElGamal \((sk = x, pk = g^x)\) et publie \( pk \).
- Chaque votant \( i \) choisit son candidat \( v_i \in \{0, 1\} \), chiffre \( g^{v_i} \) avec ElGamal, et publie le résultat.
- Le résultat du vote est le produit des messages chiffrés (grâce à l'homomorphisme multiplicatif d'ElGamal). L'autorité de confiance déchiffre le résultat \( g^{v_1 + ... + v_n} \) et publie une preuve que c'est bien le déchiffrement du produit des messages chiffrés.

#### 1. Comment récupérer le résultat effectif du vote \( v_1 + ... + v_n \) ?

L'autorité de confiance utilise sa clé privée \( sk = x \) pour déchiffrer le produit des votes chiffrés \( C = g^{v_1 + ... + v_n} \). Le déchiffrement d'ElGamal permet de retrouver directement \( v_1 + ... + v_n \) en calculant l'exposant du générateur \( g \) dans \( C \). Autrement dit, le déchiffrement donne l'expression \( g^{v_1 + ... + v_n} \), et connaissant la clé privée, l'autorité de confiance peut récupérer la somme des votes \( v_1 + ... + v_n \).

#### 2. Argumenter que la dernière étape doit être correcte, sûre, et à divulgation nulle de connaissance.

- **Correcte** : La dernière étape est correcte car elle s'appuie sur le chiffrement homomorphique d'ElGamal. Le produit des votes chiffrés \( C = g^{v_1 + ... + v_n} \) est déchiffré correctement en utilisant la clé privée \( sk \), garantissant que le résultat correspond bien à la somme des votes.
  
- **Sûre** : La sécurité repose sur la difficulté de résoudre le logarithme discret dans \( G \). Sans la clé privée \( sk \), un attaquant ne peut pas déchiffrer le produit des votes ni obtenir des informations sur les votes individuels. Ainsi, la confidentialité des votes est préservée.
  
- **À divulgation nulle de connaissance** : L'autorité de confiance publie une preuve à divulgation nulle de connaissance (zero-knowledge) pour démontrer qu'elle a correctement déchiffré le produit \( C \). Cette preuve permet de vérifier que le résultat est correct sans révéler d'informations supplémentaires sur les votes individuels.

#### 3. Proposer une manière de réaliser cette dernière étape qui assure ces propriétés.

Pour assurer que la dernière étape est correcte, sûre, et à divulgation nulle de connaissance, on peut utiliser un **protocole de Schnorr** adapté au contexte. Voici comment procéder :

1. **Preuve à divulgation nulle de connaissance (protocole de Schnorr)** :
   - L'autorité de confiance prouve qu'elle connaît la clé privée \( x \) correspondant à la clé publique \( pk = g^x \), sans révéler \( x \).
   - Elle choisit un nombre aléatoire \( r \in \mathbb{Z}_q \), calcule \( a = g^r \), et envoie \( a \) au vérifieur.
   - Le vérifieur envoie un défi aléatoire \( e \in \mathbb{Z}_q \).
   - L'autorité de confiance répond en calculant \( z = r + e * x \mod q \) et envoie \( z \).
   - Le vérifieur vérifie que \( g^z = a * pk^e \). Si cette égalité est vérifiée, cela prouve que l'autorité de confiance connaît \( x \) sans le révéler.

2. **Propriétés du protocole** :
   - **Correcte** : Le vérifieur peut s'assurer que l'autorité de confiance connaît bien \( x \), et donc que le déchiffrement est correct.
   - **Sûre** : La sécurité repose sur la difficulté du logarithme discret ; même avec cette preuve, le vérifieur ne peut pas découvrir \( x \).
   - **Divulgation nulle de connaissance** : Le protocole de Schnorr garantit que le vérifieur n'apprend rien d'autre que le fait que l'autorité de confiance connaît \( x \), respectant ainsi la propriété de divulgation nulle de connaissance.

Ainsi, ce protocole de Schnorr adapté permet de prouver correctement, en toute sécurité, et à divulgation nulle de connaissance, que l'autorité de confiance a bien effectué le déchiffrement du produit des votes.

