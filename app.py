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
        "3. Exposant de Lyapunov & Sensibilité",
        "4. Cryptographie (Textes & Images RVB/Gris)",
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
        mu = st.slider(
            "Paramètre de contrôle μ",
            0.0,
            4.0,
            3.2,
            0.01,
            key="mu_ev_slider",
        )
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
        "Ce diagramme met en évidence la transition vers le chaos via la cascade de doublement de période de Feigenbaum."
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
# 3. EXPOSANT DE LYAPUNOV & SENSIBILITÉ
# ==========================================
elif menu == "3. Exposant de Lyapunov & Sensibilité":
    st.header("3. Analyse de Lyapunov & Sensibilité aux conditions initiales")
    st.markdown(
        "L'exposant de Lyapunov $\\lambda$ quantifie la divergence exponentielle des trajectoires. Si $\\lambda > 0$, le système est chaotique."
    )

    tab1, tab2 = st.tabs(
        [
            "📊 Graphe de l'Exposant de Lyapunov",
            "🦋 Simulation de l'Effet Papillon",
        ]
    )

    with tab1:
        st.subheader("Exposant de Lyapunov en fonction de μ")
        if st.button("Calculer le spectre de Lyapunov"):
            with st.spinner("Calcul du spectre en cours..."):
                mu_vals = np.linspace(2.5, 4.0, 800)
                lyap = np.zeros(len(mu_vals))
                n_burn = 200
                n_steps = 300

                for idx, m in enumerate(mu_vals):
                    x = 0.5
                    for _ in range(n_burn):
                        x = m * x * (1 - x)
                    val = 0.0
                    for _ in range(n_steps):
                        deriv = abs(m * (1 - 2 * x))
                        if deriv > 0:
                            val += np.log(deriv)
                        x = m * x * (1 - x)
                    lyap[idx] = val / n_steps

                fig, ax = plt.subplots(figsize=(10, 4))
                ax.plot(mu_vals, lyap, color="purple", linewidth=1)
                ax.axhline(0, color="red", linestyle="--", label="λ = 0 (Seuil)")
                ax.set_title("Exposant de Lyapunov λ en fonction de μ")
                ax.set_xlabel("Paramètre μ")
                ax.set_ylabel("λ")
                ax.legend()
                ax.grid(True, linestyle="--", alpha=0.5)
                st.pyplot(fig)

    with tab2:
        st.subheader("Sensibilité aux conditions initiales (μ = 4.0)")
        mu_sens = st.slider(
            "Paramètre μ pour l'effet papillon", 3.5, 4.0, 4.0, 0.01
        )
        n_iterations = 50
        x0_1 = 0.4
        x0_2 = 0.4 + 1e-4

        traj1, traj2 = [x0_1], [x0_2]
        x1, x2 = x0_1, x0_2
        for _ in range(n_iterations):
            x1 = mu_sens * x1 * (1 - x1)
            x2 = mu_sens * x2 * (1 - x2)
            traj1.append(x1)
            traj2.append(x2)

        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(
            traj1,
            label=f"x₀ = {x0_1}",
            color="blue",
            linewidth=1.2,
        )
        ax.plot(
            traj2,
            label="y₀ = x₀ + 10⁻⁴",
            color="red",
            linestyle="--",
            linewidth=1.2,
        )
        ax.axvspan(
            0, 15, alpha=0.1, color="green", label="Trajectoires proches"
        )
        ax.axvspan(
            15, 50, alpha=0.1, color="red", label="Divergence totale"
        )
        ax.set_title(f"Sensibilité aux conditions initiales (μ = {mu_sens})")
        ax.set_xlabel("Itérations (n)")
        ax.set_ylabel("xₙ")
        ax.legend(fontsize=8)
        ax.grid(True, linestyle="--", alpha=0.5)
        st.pyplot(fig)

# ==========================================
# 4. CRYPTOGRAPHIE CHAOTIQUE (GRIS, COULEUR & TEXTE)
# ==========================================
elif menu == "4. Cryptographie (Textes & Images RVB/Gris)":
    header_tab1, header_tab2 = st.tabs(
        ["🖼️ Chiffrement d'Images (Gris & Couleur)", "✉️ Chiffrement de Texte"]
    )

    with header_tab1:
        st.header("Chiffrement Chaotique d'Images (Pixel XOR)")
        mode_couleur = st.radio(
            "Mode de traitement de l'image :",
            ("Niveaux de gris (1 canal)", "Couleur RVB (3 canaux R, V, B)"),
        )

        src = st.radio(
            "Source de l'image :",
            ("Image géométrique par défaut", "Importer ma propre photo"),
        )

        image_pil = None
        if src == "Image géométrique par défaut":
            if mode_couleur == "Niveaux de gris (1 canal)":
                img_array = np.zeros((128, 128), dtype=np.uint8)
                img_array[32:96, 32:96] = 255
                image_pil = Image.fromarray(img_array)
            else:
                img_array = np.zeros((128, 128, 3), dtype=np.uint8)
                img_array[32:96, 32:96, 0] = 255  # Rouge
                img_array[32:96, 32:96, 1] = 128  # Vert
                image_pil = Image.fromarray(img_array)
        else:
            uploaded_file = st.file_uploader(
                "Sélectionnez une image (PNG, JPG)...",
                type=["png", "jpg", "jpeg"],
            )
            if uploaded_file is not None:
                image_pil = Image.open(uploaded_file)
                if mode_couleur == "Niveaux de gris (1 canal)":
                    image_pil = image_pil.convert("L")
                else:
                    image_pil = image_pil.convert("RGB")

        if image_pil is not None:
            st.image(image_pil, caption="Image Originale", width=300)

            if st.button("Exécuter Chiffrement et Déchiffrement XOR (Image)"):
                mu_val = 4.0
                u0 = 0.6

                if mode_couleur == "Niveaux de gris (1 canal)":
                    data = np.array(image_pil)
                    forme = data.shape
                    pixels = data.flatten()

                    masque = np.zeros(pixels.size, dtype=np.uint8)
                    u = u0
                    for i in range(pixels.size):
                        u = mu_val * u * (1 - u)
                        masque[i] = int(u * 255)

                    crypte = np.bitwise_xor(pixels, masque)
                    img_cryptee = Image.fromarray(crypte.reshape(forme))

                    dechiffre = np.bitwise_xor(crypte, masque)
                    img_dechiffree = Image.fromarray(dechiffre.reshape(forme))

                else:  # Couleur RVB
                    data = np.array(image_pil)
                    forme = data.shape
                    h, w, c = forme
                    total_pixels = h * w * c

                    masque = np.zeros(total_pixels, dtype=np.uint8)
                    u = u0
                    for i in range(total_pixels):
                        u = mu_val * u * (1 - u)
                        masque[i] = int(u * 255)

                    pixels = data.flatten()
                    crypte = np.bitwise_xor(pixels, masque)
                    img_cryptee = Image.fromarray(crypte.reshape(forme))

                    dechiffre = np.bitwise_xor(crypte, masque)
                    img_dechiffree = Image.fromarray(dechiffre.reshape(forme))

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
                        caption="Image Déchiffree (Restaurée sans perte)",
                        width=300,
                    )

                st.success(
                    "Chiffrement et déchiffrement multicanal validés avec succès !"
                )

    with header_tab2:
        st.header("Chiffrement Chaotique de Texte (Masque Jetable XOR)")
        st.markdown(
            "Le texte est converti en octets (ASCII), puis combiné via un opérateur XOR avec un flux chaotique généré par la suite logistique."
        )

        texte_clair = st.text_input(
            "Entrez le texte à chiffrer :", "Faculte des Sciences de Bizerte"
        )
        u0_texte = st.slider("Clé initiale u₀", 0.01, 0.99, 0.5, 0.01)

        if st.button("Lancer le Chiffrement & Déchiffrement du Texte"):
            if texte_clair:
                # Conversion du texte en octets
                bytes_clair = texte_clair.encode("utf-8")
                n_bytes = len(bytes_clair)

                # Génération du masque chaotique
                mu_val = 4.0
                u = u0_texte
                masque_bytes = bytearray()
                for _ in range(n_bytes):
                    u = mu_val * u * (1 - u)
                    masque_bytes.append(int(u * 255) % 256)

                # Chiffrement XOR
                bytes_crypte = bytes(
                    b1 ^ b2 for b1, b2 in zip(bytes_clair, masque_bytes)
                )

                # Affichage sous forme hexadécimale pour représenter le texte chiffré
                texte_hex = bytes_crypte.hex()

                # Déchiffrement XOR (vérification de la réversibilité)
                bytes_dechiffre = bytes(
                    b1 ^ b2 for b1, b2 in zip(bytes_crypte, masque_bytes)
                )
                texte_restaure = bytes_dechiffre.decode("utf-8", errors="ignore")

                st.info(f"**Texte Clair :** {texte_clair}")
                st.warning(
                    f"**Texte Chiffré (Hexadécimal) :** `{texte_hex}`"
                )
                st.success(f"**Texte Déchiffré (Restauré) :** {texte_restaure}")
            else:
                st.error("Veuillez entrer un texte valide.")
