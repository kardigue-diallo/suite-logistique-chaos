import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuration de la page Streamlit
st.set_page_config(
    page_title="PFE - Suite Logistique & Chaos Numérique",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Étude de la Suite Logistique : De la Stabilité au Chaos Numérique")
st.markdown("**Projet de Fin d'Études (PFE)** — Realisé par *Kardigue Diallo* & *Eulogio Mbu Mbu Angono* | Encadré par *Mme Siwar Saidani*")

# Navigation par onglets
tab1, tab2, tab3 = st.tabs(["1. Évolution Temporelle", "2. Diagramme de Bifurcation", "3. Attracteur de Hénon (2D)"])

# ---------------------------------------------------------
# ONGLET 1 : ÉVOLUTION TEMPORELLE DE LA SUITE LOGISTIQUE
# ---------------------------------------------------------
with tab1:
    st.header("1. Évolution Temporelle $x_{n+1} = r x_n (1 - x_n)$")
    st.write("Visualisez la transition entre état stable, cycle périodique et régime chaotique selon la valeur du paramètre de croissance $r$.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        r_val = st.slider("Paramètre $r$", min_value=0.5, max_value=4.0, value=3.2, step=0.01)
    with col2:
        x0_val = st.slider("Condition initiale $x_0$", min_value=0.01, max_value=0.99, value=0.2, step=0.01)
    with col3:
        n_iter = st.slider("Nombre d'itérations", min_value=20, max_value=200, value=60, step=10)
        
    # Calcul de la suite
    x_vals = [x0_val]
    curr_x = x0_val
    for _ in range(n_iter):
        curr_x = r_val * curr_x * (1 - curr_x)
        x_vals.append(curr_x)
        
    # Tracé
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(x_vals, marker='o', linestyle='-', color='#003366', markersize=4)
    ax.set_title(f"Orbites de la suite pour r = {r_val} et x0 = {x0_val}")
    ax.set_xlabel("n (Itérations)")
    ax.set_ylabel("$x_n$")
    ax.grid(True, linestyle='--', alpha=0.6)
    st.pyplot(fig)

# ---------------------------------------------------------
# ONGLET 2 : DIAGRAMME DE BIFURCACTION
# ---------------------------------------------------------
with tab2:
    st.header("2. Diagramme de Bifurcation")
    st.write("Visualisation des états asymptotiques (élimination du transitoire) et de la cascade de doublement de période de Feigenbaum.")
    
    n_r = st.slider("Résolution en $r$ (nombre de points)", min_value=500, max_value=2000, value=1000, step=100)
    
    # Bouton pour générer (éviter les recalculs automatiques trop lourds)
    if st.button("Générer le Diagramme de Bifurcation"):
        with st.spinner("Calcul des bifurcations en cours..."):
            r_space = np.linspace(2.5, 4.0, n_r)
            iterations = 500
            last_n = 100
            
            r_list = []
            x_list = []
            
            for r in r_space:
                x = 0.5
                # Élimination du régime transitoire
                for _ in range(iterations - last_n):
                    x = r * x * (1 - x)
                # Conservation des états stables/chaotiques
                for _ in range(last_n):
                    x = r * x * (1 - x)
                    r_list.append(r)
                    x_list.append(x)
                    
            fig2, ax2 = plt.subplots(figsize=(10, 5))
            ax2.plot(r_list, x_list, ',k', alpha=0.25)
            ax2.set_title("Diagramme de Bifurcation de la Suite Logistique")
            ax2.set_xlabel("Paramètre r")
            ax2.set_ylabel("États asymptotiques $x_n$")
            ax2.grid(True, linestyle='--', alpha=0.4)
            st.pyplot(fig2)

# ---------------------------------------------------------
# ONGLET 3 : ATTRACTEUR DE HÉNON
# ---------------------------------------------------------
with tab3:
    st.header("3. Attracteur de Hénon (Chaos en 2D)")
    st.write("Extension du chaos en 2D : $x_{n+1} = 1 - a y_n^2 + y_n$ et $y_{n+1} = b x_n$.")
    
    col_a, col_b, col_pts = st.columns(3)
    with col_a:
        a_param = st.number_input("Paramètre a", value=1.4, step=0.05)
    with col_b:
        b_param = st.number_input("Paramètre b", value=0.3, step=0.05)
    with col_pts:
        pts_count = st.slider("Nombre de points", min_value=1000, max_value=50000, value=10000, step=5000)
        
    x_henon = np.zeros(pts_count)
    y_henon = np.zeros(pts_count)
    
    x_henon[0], y_henon[0] = 0.1, 0.1
    for i in range(pts_count - 1):
        x_henon[i+1] = 1 - a_param * (y_henon[i] ** 2) + y_henon[i]
        y_henon[i+1] = b_param * x_henon[i]
        
    fig3, ax3 = plt.subplots(figsize=(8, 5))
    ax3.plot(x_henon, y_henon, ',m', alpha=0.6)
    ax3.set_title(f"Attracteur de Hénon (a = {a_param}, b = {b_param})")
    ax3.set_xlabel("x")
    ax3.set_ylabel("y")
    ax3.grid(True, linestyle='--', alpha=0.4)
    st.pyplot(fig3)
