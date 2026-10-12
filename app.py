import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from PIL import Image

# Configuration de la page Streamlit
st.set_page_config(
    page_title="PFE - Suite Logistique & Chaos", page_icon="🌌", layout="wide"
)

st.title(
    "🌌 Étude de la Suite Logistique : De la Stabilité au Chaos Numérique"
)
st.markdown(
    "*Projet de Fin d'Études (PFE) — Faculté des Sciences de Bizerte (FSB)*"
)
st.markdown(
    "**Auteurs :** Kardigue Diallo & Eulogio Mbu Mbu Angono | **Encadrante :** Mme Siwar Saidani"
)
st.markdown("---")

# Menu de navigation latéral
menu = st.sidebar.selectbox(
    "Navigation du PFE",
    [
        "1. Évolution Temporelle & Stabilité",
        "2. Diagramme de Bifurcation",
        "3. Exposant de Lyapunov & Chaos",
        "4. Cryptographie Chaotique",
    ],
)

# ==========================================
# 1. ÉVOLUTION TEMPORELLE & STABILITÉ
# ==========================================
if menu == "1. Évolution Temporelle & Stabilité":
    st.header("1. Évolution Temporelle de la Suite Logistique")
    st.latex(r"x_{n+1} = \mu x_n (1 - x_n)")

    col1, col2 = st.columns(2)
    with col1:
        mu = st.slider("Paramètre de contrôle μ", 0.0, 4.0, 3.2, 0.01)
    with col2:
        x0 = st.slider("Condition initiale x₀", 0.01, 0.99, 0.2, 0.01)

    n_iter = st.slider("Nombre d'itérations N", 10, 200, 50)

    # Calcul de la suite
    x = x0
    orbite = [x]
    for _ in range(n_iter):
        x = mu * x * (1 - x)
        orbite.append(x)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(
        range(len(orbite)),
        orbite,
        marker="o",
        markersize=4,
        color="steelblue",
        linewidth=1,
    )
    ax.set_title(f"Évolution de la suite pour μ = {mu} et x₀ = {x0}")
    ax.set_xlabel("Itérations (n)")
    ax.set_ylabel("xₙ")
    ax.grid(True, linestyle="--", alpha=0.5)
    st.pyplot(fig)

# ==========================================
# 2. DIAGRAMME DE BIFURCATION
# ==========================================
elif menu == "2. Diagramme de Bifurcation":
    st.header("2. Diagramme de Bifurcation de la Suite Logistique")
    st.markdown(
        "Ce diagramme met en évidence la transition vers le chaos via la cascade de doublement de période (Feigenbaum)."
    )

    if st.button("Générer le diagramme de bifurcation"):
        with st.spinner("Calcul en cours..."):
            r_values = np.linspace(2.5, 4.0, 1000)
            iterations = 600
            last = 100
            x = 1e-5 * np.ones(len(r_values))

            fig, ax = plt.subplots(figsize=(10, 6))
            for i in range(iterations):
                x = r_values * x * (1 - x)
                if i >= (iterations - last):
                    ax.plot(r_values, x, ",", color="black", alpha=0.3)

            ax.set_title("Diagramme de bifurcation de la suite logistique")
            ax.set_xlabel("Paramètre μ")
            ax.set_ylabel("x")
            ax.grid(True, linestyle="--", alpha=0.5)
            st.pyplot(fig)

# ==========================================
# 3. EXPOSANT DE LYAPUNOV & CHAOS
# ==========================================
elif menu == "3. Exposant de Lyapunov & Chaos":
    st.header("3. Sensibilité aux conditions initiales & Exposant de Lyapunov")
    st.latex(
        r"\lambda = \lim_{n \to +\infty} \frac{1}{n} \sum_{k=0}^{n-1} \ln|\mu(1 - 2x_k)|"
    )

    st.subheader(
        "Simulation de l'effet papillon (μ = 4.0 avec un écart de 10⁻⁴)"
    )
    n_iterations = 50
    x0_1 = 0.4
    x0_2 = 0.4001

    traj1, traj2 = [x0_1], [x0_2]
    x1, x2 = x0_1, x0_2
    for _ in range(n_iterations):
        x1 = 4.0 * x1 * (1 - x1)
        x2 = 4.0 * x2 * (1 - x2)
        traj1.append(x1)
        traj2.append(x2)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(traj1, label="x₀ = 0.4", color="blue", linewidth=1)
    ax.plot(
        traj2, label="y₀ = 0.4 + 10⁻⁴", color="red", linestyle="--", linewidth=1
    )
    ax.axvspan(
        0, 15, alpha=0.1, color="green", label="Trajectoires proches"
    )
    ax.axvspan(15, 50, alpha=0.1, color="red", label="Divergence totale")
    ax.set_title("Sensibilité aux conditions initiales (μ = 4)")
    ax.set_xlabel("Itérations (n)")
    ax.set_ylabel("xₙ")
    ax.legend(fontsize=8)
    ax.grid(True, linestyle="--", alpha=0.5)
    st.pyplot(fig)

# ==========================================
# 4. CRYPTOGRAPHIE CHAOTIQUE
# ==========================================
elif menu == "4. Cryptographie Chaotique":
    st.header("4. Application au Chiffrement d'Images (Pixel XOR)")
    st.markdown(
        "Masquage d'une image convertie en niveaux de gris à l'aide d'un masque chaotique généré par la suite logistique."
    )

    # Choix de l'image
    src = st.radio(
        "Source de l'image :",
        ("Image par défaut (Carré géométrique)", "Importer ma propre photo"),
    )

    image_pil = None
    if src == "Image par défaut (Carré géométrique)":
        img_array = np.zeros((128, 128), dtype=np.uint8)
        img_array[32:96, 32:96] = 255
        image_pil = Image.fromarray(img_array)
    else:
        uploaded_file = st.file_uploader(
            "Sélectionnez une image (PNG, JPG)...", type=["png", "jpg", "jpeg"]
        )
        if uploaded_file is not None:
            image_pil = Image.open(uploaded_file).convert("L")

    if image_pil is not None:
        st.image(
            image_pil, caption="Image Originale (Niveaux de gris)", width=300
        )

        if st.button("Lancer le Chiffrement / Déchiffrement XOR"):
            # Traitement image en tableau numpy
            img_gray = image_pil.convert("L")
            data = np.array(img_gray)
            forme = data.shape
            pixels = data.flatten()

            # Paramètres de la clé chaotique
            mu_val = 4.0
            u0 = 0.6

            # Génération du masque chaotique
            masque = np.zeros(pixels.size, dtype=np.uint8)
            u = u0
            for i in range(pixels.size):
                u = mu_val * u * (1 - u)
                masque[i] = int(u * 255)

            # Chiffrement XOR
            crypte = np.bitwise_xor(pixels, masque)
            img_cryptee_array = crypte.reshape(forme)
            img_cryptee = Image.fromarray(img_cryptee_array)

            # Déchiffrement XOR (vérification de la réversibilité)
            dechiffre = np.bitwise_xor(crypte, masque)
            img_dechiffree_array = dechiffre.reshape(forme)
            img_dechiffree = Image.fromarray(img_dechiffree_array)

            # Affichage des résultats en colonnes
            col1, col2 = st.columns(2)
            with col1:
                st.image(
                    img_cryptee,
                    caption="Image Chiffrée (Bruit blanc)",
                    width=300,
                )
            with col2:
                st.image(
                    img_dechiffree,
                    caption="Image Déchiffrée (Restaurée sans perte)",
                    width=300,
                )

            st.success(
                "Chiffrement et déchiffrement effectués avec succès ! Réversibilité validée par l'opérateur XOR."
            )
