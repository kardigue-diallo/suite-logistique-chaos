# Étude de la Suite Logistique : De la Stabilité au Chaos Numérique

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat-square&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

Démonstrateur interactif développé dans le cadre du **Projet de Fin d'Études (PFE)** portant sur la modélisation mathématique du chaos déterministe et ses applications en cryptographie chaotique.

---

## Équipe & Supervision

* **Auteurs :** Kardigue Diallo & Eulogio Mbu Mbu Angono
* **Encadrante :** Mme Siwar Saidani
* **Institution :** Faculté des Sciences de Bizerte
* **Filière :** Licence en Mathématiques et Informatique

---

## Description du Projet

Cette application web interactive permet de visualiser et d'analyser la transition vers le chaos dans les systèmes dynamiques discrets régis par la **suite logistique** :

$$x_{n+1} = \mu x_n (1 - x_n), \quad \text{avec } x_n \in [0, 1] \text{ et } \mu \in [0, 4]$$

### Fonctionnalités principales :

1. **Évolution Temporelle & Cobweb :** Visualisation des orbites et convergence vers les points fixes via le diagramme en toile d'araignée (*Cobweb plot*).
2. **Diagramme de Bifurcation & Effet Papillon :** Démonstration de la cascade de doublement de période de Feigenbaum et de la sensibilité extrême aux conditions initiales ($\epsilon = 10^{-5}$).
3. **Exposant de Lyapunov :** Quantification exacte du chaos ($\lambda > 0$).
4. **Cryptographie Chaotique :**
   * **Chiffrement de Texte :** Masque XOR pseudo-aléatoire basé sur la séquence chaotique ($\mu = 4.0$).
   * **Chiffrement d'Image :** Chiffrement matriciel pixel par pixel.
5. **Attracteur de Hénon :** Modélisation du chaos bidimensionnel (2D).

---

## Structure du Projet

```text
suite-logistique-chaos/
├── .streamlit/
│   └── config.toml          # Configuration du thème Streamlit (sombre)
├── app.py                   # Code source principal de l'application
├── requirements.txt         # Dépendances Python du projet
└── README.md                # Documentation du projet
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
git clone https://github.com/kardigue-diallo/suite-logistique-chaos.git
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
