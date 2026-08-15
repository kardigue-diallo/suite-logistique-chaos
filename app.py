import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# ---------------------------------------------------------
# CONFIGURATION DE LA PAGE
# ---------------------------------------------------------
st.set_page_config(
    page_title="PFE - Suite Logistique & Chaos",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Style CSS personnalisé
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #00D4FF;
        text-align: center;
        margin-bottom: 0px;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #A0AAB0;
        text-align: center;
        margin-bottom: 25px;
    }
    .stCodeBlock {
        border: 1px solid #00D4FF !important;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-title">🌌 Étude de la Suite Logistique : De la Stabilité au Chaos Numérique</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Projet de Fin d\'Études (PFE) — Faculté des Sciences de Bizerte</div>', unsafe_allow_html=True)

# Sidebar
st.sidebar.image("https://img.icons8.com/fluency/96/chaos.png", width=70)
st.sidebar.title("📌 Informations PFE")
st.sidebar.markdown("""
* **Auteurs :** Kardigue Diallo & Eulogio Mbu Mbu Angono
* **Encadrante :** Mme Siwar Saidani
* **Institution :** Faculté des Sciences de Bizerte
* **Domaine :** Mathématiques Appliquées & Informatique
""")
st.sidebar.divider()
st.sidebar.info("💡 Navigation à travers la théorie, les preuves visuelles et les applications de cryptographie chaotique.")

# Navigation par Onglets
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 1. Évolution & Cobweb",
    "🔀 2. Bifurcation & Effet Papillon",
    "📊 3. Exposant de Lyapunov",
    "🔐 4. Cryptographie Chaotique (Image & Texte)",
    "🌀 5. Attracteur de Hénon (2D)"
])

# ---------------------------------------------------------
# ONGLET 1 : ÉVOLUTION TEMPORELLE & DIAGRAMME COBWEB
# ---------------------------------------------------------
with tab1:
    st.header("1. Évolution Temporelle & Diagramme en Escalier (Cobweb)")
    st.latex(r"x_{n+1} = f_\mu(x_n) = \mu x_n (1 - x_n), \quad x_n \in [0, 1], \; \mu \in [0, 4]")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        mu_val = st.slider("Paramètre de contrôle $\\mu$", min_value=0.1, max_value=4.0, value=3.46, step=0.01, key="mu_tab1")
    with col2:
        x0_val = st.slider("Condition initiale $x_0$", min_value=0.01, max_value=0.99, value=0.46, step=0.01, key="x0_tab1")
    with col3:
        n_iter = st.slider("Nombre d'itérations $N$", min_value=20, max_value=200, value=60, step=10, key="n_tab1")

    # Calcul de la suite
    x_vals = [x0_val]
    curr = x0_val
    for _ in range(n_iter):
        curr = mu_val * curr * (1 - curr)
        x_vals.append(curr)

    col_left, col_right = st.columns(2)

    with col_left:
        fig_time = go.Figure()
        fig_time.add_trace(go.Scatter(y=x_vals, mode='lines+markers', name='x_n',
                                     line=dict(color='#00D4FF', width=2),
                                     marker=dict(size=5, color='#FF4B4B')))
        fig_time.update_layout(title=f"Orbites Temporelles (μ = {mu_val})",
                              xaxis_title="Itérations (n)", yaxis_title="x_n",
                              template="plotly_dark", height=400)
        st.plotly_chart(fig_time, use_container_width=True)

    with col_right:
        x_arr = np.linspace(0, 1, 500)
        y_arr = mu_val * x_arr * (1 - x_arr)

        fig_cobweb = go.Figure()
        fig_cobweb.add_trace(go.Scatter(x=x_arr, y=y_arr, mode='lines', name=f'f(x) = {mu_val}x(1-x)', line=dict(color='#00D4FF', width=2)))
        fig_cobweb.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode='lines', name='y = x', line=dict(color='#A0AAB0', dash='dash')))

        cx, cy = [x0_val], [0]
        for i in range(min(n_iter, 50)):
            cx.append(x_vals[i])
            cy.append(x_vals[i+1])
            cx.append(x_vals[i+1])
            cy.append(x_vals[i+1])

        fig_cobweb.add_trace(go.Scatter(x=cx, y=cy, mode='lines', name='Trajectoire', line=dict(color='#FF4B4B', width=1.5)))
        fig_cobweb.update_layout(title="Diagramme Cobweb (Toile d'araignée)",
                                 xaxis_title="x_n", yaxis_title="x_{n+1}",
                                 template="plotly_dark", height=400)
        st.plotly_chart(fig_cobweb, use_container_width=True)

# ---------------------------------------------------------
# ONGLET 2 : DIAGRAMME DE BIFURCACTION & EFFET PAPILLON
# ---------------------------------------------------------
with tab2:
    st.header("2. Diagramme de Bifurcation & Sensibilité aux Conditions Initiales")
    
    st.subheader("A. Cascade de Doublement de Période (Feigenbaum)")
    n_mu = st.slider("Résolution du diagramme (points en $\\mu$)", min_value=500, max_value=2500, value=1200, step=100)
    
    if st.button("🔄 Générer / Rafraîchir le Diagramme de Bifurcation"):
        with st.spinner("Calcul des bifurcations asymptotiques en cours..."):
            mu_space = np.linspace(2.5, 4.0, n_mu)
            iterations = 400
            last_n = 80
            
            mu_list, x_list = [], []
            for mu in mu_space:
                x = 0.5
                for _ in range(iterations - last_n):
                    x = mu * x * (1 - x)
                for _ in range(last_n):
                    x = mu * x * (1 - x)
                    mu_list.append(mu)
                    x_list.append(x)
                    
            fig_bif = go.Figure()
            fig_bif.add_trace(go.Scattergl(x=mu_list, y=x_list, mode='markers',
                                           marker=dict(size=1, color='#00D4FF', opacity=0.3)))
            fig_bif.update_layout(title="Diagramme de Bifurcation de la Suite Logistique",
                                  xaxis_title="Paramètre μ", yaxis_title="États asymptotiques x_n",
                                  template="plotly_dark", height=450)
            st.plotly_chart(fig_bif, use_container_width=True)

    st.divider()
    st.subheader("B. Sensibilité Extrême aux Conditions Initiales (Effet Papillon)")
    
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        mu_chaos = st.slider("Paramètre $\\mu$ (Régime chaotique si $\\mu=4.0$)", 3.5, 4.0, 3.99, 0.01)
    with col_e2:
        eps = 1e-5
        st.write(f"Condition 1 ($x_0$) : **0.50000** | Condition 2 ($x_0 + \\epsilon$) : **{0.5 + eps:.5f}**")
        
    x1, x2 = [0.5], [0.5 + eps]
    c1, c2 = 0.5, 0.5 + eps
    for _ in range(80):
        c1 = mu_chaos * c1 * (1 - c1)
        c2 = mu_chaos * c2 * (1 - c2)
        x1.append(c1)
        x2.append(c2)
        
    fig_sens = go.Figure()
    fig_sens.add_trace(go.Scatter(y=x1, mode='lines+markers', name='x0 = 0.50000', line=dict(color='#00D4FF')))
    fig_sens.add_trace(go.Scatter(y=x2, mode='lines+markers', name='x0 + 1e-5', line=dict(color='#FF4B4B', dash='dot')))
    fig_sens.update_layout(title="Divergence exponentielle des trajectoires proches",
                           xaxis_title="Itérations (n)", yaxis_title="x_n",
                           template="plotly_dark", height=380)
    st.plotly_chart(fig_sens, use_container_width=True)

# ---------------------------------------------------------
# ONGLET 3 : EXPOSANT DE LYAPUNOV
# ---------------------------------------------------------
with tab3:
    st.header("3. Exposant de Lyapunov : Quantification du Chaos")
    st.latex(r"\lambda(\mu) = \lim_{n \to \infty} \frac{1}{n} \sum_{i=0}^{n-1} \ln \left| \mu (1 - 2x_i) \right|")
    
    if st.button("📊 Calculer le Spectre de Lyapunov"):
        with st.spinner("Calcul numérique en cours..."):
            mu_vals = np.linspace(2.5, 4.0, 1000)
            lyapunov = []
            N = 500
            
            for mu in mu_vals:
                x = 0.5
                result = 0
                for _ in range(100):
                    x = mu * x * (1 - x)
                for _ in range(N):
                    x = mu * x * (1 - x)
                    deriv = abs(mu * (1 - 2 * x))
                    if deriv > 0:
                        result += np.log(deriv)
                lyapunov.append(result / N)
                
            fig_lya = go.Figure()
            fig_lya.add_trace(go.Scatter(x=mu_vals, y=lyapunov, mode='lines', name='λ(μ)', line=dict(color='#00D4FF', width=1.5)))
            fig_lya.add_trace(go.Scatter(x=[2.5, 4.0], y=[0, 0], mode='lines', name='λ = 0 (Seuil)', line=dict(color='#FF4B4B', dash='dash')))
            fig_lya.update_layout(title="Exposant de Lyapunov en fonction de μ",
                                  xaxis_title="Paramètre μ", yaxis_title="Exposant de Lyapunov λ",
                                  template="plotly_dark", height=450)
            st.plotly_chart(fig_lya, use_container_width=True)

# ---------------------------------------------------------
# ONGLET 4 : CRYPTOGRAPHIE CHAOTIQUE (IMAGE & TEXTE)
# ---------------------------------------------------------
with tab4:
    st.header("4. Applications en Cryptographie Chaotique")
    st.write("Exploitation du générateur pseudo-aléatoire chaotique de la suite logistique à $\\mu = 4.0$.")

    # FONCTION DE CHIFFREMENT DE TEXTE
    def text_chaotic_cipher(text, x0):
        bytes_text = text.encode('utf-8')
        cipher_bytes = bytearray()
        keys_used = []
        curr_x = x0
        mu = 4.0
        
        for b in bytes_text:
            curr_x = mu * curr_x * (1 - curr_x)
            key_byte = int(curr_x * 256) % 256
            cipher_bytes.append(b ^ key_byte)
            keys_used.append(key_byte)
            
        return cipher_bytes, keys_used

    subtab_text, subtab_img = st.tabs(["🔤 Chiffrement de Texte", "🖼️ Chiffrement d'Image"])

    # SECTION CHIFFREMENT DE TEXTE
    with subtab_text:
        st.subheader("A. Chiffrement de Texte par Masque Vigenère/XOR Chaotique")
        
        col_t1, col_t2 = st.columns(2)
        with col_t1:
            input_text = st.text_area("Message clair à chiffrer :", value="Faculté des Sciences de Bizerte - PFE Chaos 2026", height=100)
            secret_key_txt = st.number_input("Clé secrète de chiffrement ($x_0$)", value=0.3141592, format="%.7f")
            
        cipher_bytes, keys_used = text_chaotic_cipher(input_text, secret_key_txt)
        hex_cipher = cipher_bytes.hex().upper()

        with col_t2:
            st.write("#### Resultat du Chiffrement :")
            st.code(hex_cipher, language="text")
            st.caption("Le texte est transformé en une suite d'octets hexadécimaux indéchiffrables sans la clé $x_0$.")

        st.divider()
        st.subheader("B. Test de Déchiffrement & Sensibilité à la Clé")
        
        col_d1, col_d2 = st.columns(2)
        with col_d1:
            decrypt_key = st.number_input("Clé pour le déchiffrement ($x_0$ de déchiffrement)", value=0.3141592, format="%.7f")
        
        decrypted_bytes, _ = text_chaotic_cipher(bytes.fromhex(hex_cipher).decode('latin1'), decrypt_key)
        try:
            decrypted_text = decrypted_bytes.decode('utf-8')
        except:
            decrypted_text = decrypted_bytes.decode('latin1', errors='ignore')

        with col_d2:
            if decrypt_key == secret_key_txt:
                st.success(f"**Texte déchiffré avec succès :**\n\n`{decrypted_text}`")
            else:
                st.error(f"**Échec du déchiffrement (Bruit chaotique) :**\n\n`{decrypted_text}`")

    # SECTION CHIFFREMENT D'IMAGE
    with subtab_img:
        st.subheader("Chiffrement d'une Matrice d'Image (Pixel XOR)")
        
        col_img1, col_img2 = st.columns(2)
        with col_img1:
            x0_crypto = st.slider("Clé Secrète Image ($x_0$)", 0.001, 0.999, 0.31415, 0.0001, key="x0_img")
        with col_img2:
            img_size = st.select_slider("Taille de l'image (pixels)", options=[32, 64, 128], value=64)

        original_img = np.zeros((img_size, img_size), dtype=np.uint8)
        original_img[img_size//4:3*img_size//4, img_size//4:3*img_size//4] = 255

        total_pixels = img_size * img_size
        chaos_key = np.zeros(total_pixels, dtype=np.uint8)
        curr_x = x0_crypto
        
        for i in range(total_pixels):
            curr_x = 4.0 * curr_x * (1 - curr_x)
            chaos_key[i] = int(curr_x * 256) % 256
            
        chaos_mask = chaos_key.reshape((img_size, img_size))
        encrypted_img = np.bitwise_xor(original_img, chaos_mask)

        col_i1, col_i2, col_i3 = st.columns(3)
        
        fig_orig, ax1 = plt.subplots()
        ax1.imshow(original_img, cmap='gray')
        ax1.set_title("Image Originale")
        ax1.axis('off')
        col_i1.pyplot(fig_orig)

        fig_mask, ax2 = plt.subplots()
        ax2.imshow(chaos_mask, cmap='magma')
        ax2.set_title("Masque Chaotique (μ=4)")
        ax2.axis('off')
        col_i2.pyplot(fig_mask)

        fig_enc, ax3 = plt.subplots()
        ax3.imshow(encrypted_img, cmap='gray')
        ax3.set_title("Image Chiffrée (XOR)")
        ax3.axis('off')
        col_i3.pyplot(fig_enc)

# ---------------------------------------------------------
# ONGLET 5 : ATTRACTEUR DE HÉNON (CHAOS 2D)
# ---------------------------------------------------------
with tab5:
    st.header("5. Attracteur de Hénon (Extension du Chaos en 2D)")
    st.latex(r"\begin{cases} x_{n+1} = 1 - a x_n^2 + y_n \\ y_{n+1} = b x_n \end{cases}")
    
    col_a, col_b, col_pts = st.columns(3)
    with col_a:
        a_param = st.number_input("Paramètre a", value=1.4, step=0.05)
    with col_b:
        b_param = st.number_input("Paramètre b", value=0.3, step=0.05)
    with col_pts:
        pts_count = st.slider("Nombre de points", min_value=5000, max_value=50000, value=20000, step=5000)
        
    x_henon = np.zeros(pts_count)
    y_henon = np.zeros(pts_count)
    x_henon[0], y_henon[0] = 0.1, 0.1
    
    for i in range(pts_count - 1):
        x_henon[i+1] = 1 - a_param * (x_henon[i] ** 2) + y_henon[i]
        y_henon[i+1] = b_param * x_henon[i]
        
    fig_h = go.Figure()
    fig_h.add_trace(go.Scattergl(x=x_henon, y=y_henon, mode='markers',
                                 marker=dict(size=1.5, color='#FF4B4B', opacity=0.5)))
    fig_h.update_layout(title=f"Attracteur de Hénon (a = {a_param}, b = {b_param})",
                        xaxis_title="X", yaxis_title="Y",
                        template="plotly_dark", height=500)
    st.plotly_chart(fig_h, use_container_width=True)
