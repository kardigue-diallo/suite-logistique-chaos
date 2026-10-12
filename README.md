# 🌌 Étude de la Suite Logistique : De la Stabilité au Chaos Numérique

> Projet de Fin d'Études (PFE) en vue de l'obtention de la **Licence en Mathématiques et Informatique**  
> **Faculté des Sciences de Bizerte (FSB) — Université de Carthage**  
> **Soutenu le :** 20 Mai 2026 | **Mention :** Bien 

---

## 👥 Équipe & Encadrement
* **Étudiants :** Kardigue Diallo & Eulogio Mbu Mbu Angono  
* **Encadrante :** Mme Siwar Saidani  
* **Jury :** Mr. Chaouki Aouiti, Mme Sonia Chaari, Mme Siwar Saidani  

---

## 📖 1. Présentation du Projet
Ce projet explore la transition vers le chaos à travers l'étude approfondie d'un système dynamique discret fondamental : **la suite logistique** ($x_{n+1} = \mu x_n(1 - x_n$). 

L'objectif principal est de lier la rigueur de l'analyse mathématique (points fixes, stabilité, théorie de Coppel, cascade de Feigenbaum) au développement d'une application logicielle interactive de simulation et de cryptographie chaotique (testée sur poste de travail et sur terminal mobile via Pydroid 3).

---

## 🛠️ 2. Stack Technologique & Outils
* **Langage principal :** Python 
* **Bibliothèques scientifiques :** NumPy, Matplotlib, PIL (Pillow)
* **Interface & Web Dashboard :** Streamlit
* **Environnement Mobile :** Pydroid 3 (Android)
* **Rédaction académique & Mise en forme :** LaTeX (Overleaf / WinEdt)

---

## 📂 3. Structure du Dépôt
```text
├── app.py                      # Application interactive Streamlit (Dashboard complet)
├── requirements.txt            # Dépendances et bibliothèques requises
├── assets/                     # Graphiques, schémas théoriques et captures d'écran
│   ├── bifurcation.png
│   ├── lyapunov.png
│   └── chiffrement_image.png
└── README.md                   # Documentation technique et académique du projet
```

---

## Stack Technique

* **Langage :** Python 3.9+
* **Interface Web :** Streamlit
* **Calcul Numérique :** NumPy
* **Visualisation Graphique :** Plotly Express / Graph Objects, Matplotlib

---

## Installation & Exécution en Local

Pour exécuter l'application sur votre machine :

1. **Cloner le dépôt :**
```bash
git clone [https://github.com/kardigue-diallo/suite-logistique-chaos.git](https://github.com/kardigue-diallo/suite-logistique-chaos.git)
cd suite-logistique-chaos
```

2. **Installer les dépendances :**
```bash
pip install -r requirements.txt
```

3. **Lancer l'application Streamlit :**
```bash
streamlit run app.py
```

---

## Déploiement en Ligne

L'application est déployée et accessible publiquement sur Streamlit Community Cloud :
👉 **[Accéder à l'application en ligne](https://suite-logistique-chaos.streamlit.app)**
