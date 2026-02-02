# 🌱 Smart Irrigation System with Fuzzy Logic (Raspberry Pi)

## 📌 Description
Ce projet est un système d’arrosage intelligent basé sur la **logique floue (Fuzzy Logic)**.  
Le Raspberry Pi prend les décisions automatiquement à partir des capteurs, sans attendre l’application mobile.

---

## 🔄 Architecture Générale
**Capteurs → Raspberry Pi (Fuzzy Logic) → Pompe à eau + Cloud → Application Mobile**

---

## 🧩 Étapes du Système

### 1️⃣ Collecte et Conversion (Hardware)
- Capteurs utilisés :
  - Humidité du sol  
  - Température  
  - Humidité de l’air  
- Les capteurs mesurent des valeurs physiques.
- Le Raspberry Pi lit ces valeurs via un **convertisseur analogique-numérique**.

---

### 2️⃣ Cerveau IA – Logique Floue (Fuzzy Logic)
- Le Raspberry Pi récupère les données des capteurs (antécédents).
- Les données passent dans le moteur de logique floue.
- Application des règles, par exemple :  
  **SI humidité du sol est basse ET température haute ALORS arrosage fort**.
- Calcul automatique du **volume d’eau exact**.

---

### 3️⃣ Action et Stockage (Cloud)
- La pompe à eau est activée via un relais selon la décision.
- Les données des capteurs + volume d’eau sont envoyées en temps réel sur le **Cloud** (Firebase/Firestore).

---

### 4️⃣ Visualisation (Application Mobile)
- L’application mobile affiche les données stockées sur le Cloud.
- Graphiques, météo et état actuel du système.
- Aucun calcul n’est effectué côté application, juste la lecture des données.

---

## ⚡ Technologies utilisées
- **Raspberry Pi**  
- **Capteurs** : humidité, température, humidité de l’air  
- **Logique floue (Fuzzy Logic)**  
- **Relais pour pompe à eau**  
- **Cloud** : Firebase / Firestore  
- **Application Mobile** : lecture des données et visualisation

---

## 🚀 Flux de données

``` bash
Capteurs → Raspberry Pi (Fuzzy Logic) → Action (Pompe) + Envoi Cloud → Application Mobile
```

## 👨‍💻 Auteur
**Abdellah Karani**


