# DM1 - Zero-Knowledge - ENKIRCHE Elias
## Vous trouverez dans ce repo tous les documents et fichier nécessaire à la réalisation du DM
### Préliminaire
Afin de réaliser ce DM, j'ai du installer docker sur mon Pc, merci au site ci-dessous: 
https://dataedo.com/docs/installing-docker-on-windows-via-wsl

Aussi j'ai installer Flask et  pycryptodome

### Lancement de Docker Daemon
La commande sudo dockerd démarre le démon Docker (aussi appelé Docker Daemon), qui est un service en arrière-plan responsable de la gestion des conteneurs Docker sur une machine.
![image](https://github.com/user-attachments/assets/ef561a2a-2373-479e-a451-0de844dc68d7)

### Lancement d'un conteneur Docker 
Lancement du conteneur Docker à partir d'une image. Ici, l'image utilisée est nommée schnorr_server. Le conteneur exécutera l'application encapsulée dans cette image.

![image](https://github.com/user-attachments/assets/ac4abce6-51f2-48c8-8a9a-61e93dfcd271)

### Récupération de la preuve de Schnorr
Elle envoie une requête GET à ton serveur Flask à l'adresse http://localhost:5000/schnorr-proof.
Le serveur Flask génère une preuve de Schnorr (comme spécifié dans le code), incluant des valeurs comme 
r, 𝑒, 𝑠, la clé publique 𝑦, le générateur 𝑔, et le module premier 𝑝, puis renvoie ces informations sous forme de JSON.
curl affiche ensuite cette réponse dans le terminal.
![image](https://github.com/user-attachments/assets/217b2cf1-82ed-434a-ae04-6c54d8e864e5)

### Vérification de la preuve de Schnorr
Elle envoie les paramètres `r`, `e`, `s`, `y`, `g`, et `p` au serveur Flask via une requête **POST**.

Le serveur Flask reçoit ces données et utilise la fonction `verify_proof` pour vérifier si la preuve de Schnorr est valide.

Le serveur effectue la vérification en calculant les deux côtés de l'équation de vérification Schnorr :

- \( g^s mod p \) (côté gauche),
- \( r * y^e mod p \) (côté droit).

Si les deux côtés sont égaux, la preuve est considérée comme valide.

Ensuite, le serveur renvoie un résultat **JSON** avec une indication si la preuve est valide ou non.

![image](https://github.com/user-attachments/assets/2ca05fd9-c1ad-4354-903a-64e71f099ee3)
Dans notre cas c'est bien valide.
