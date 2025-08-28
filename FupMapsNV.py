import streamlit as st
import os
#Usabilidade, tempo e desenvolvimento e maturação
# ========== CONFIGURAÇÕES INICIAIS ==========
st.set_page_config(page_title="FUPMAPS", layout="centered")

# ========== ESTILO CSS: FUNDO AZUL E TEXTO CENTRALIZADO ==========
st.markdown("""
    <style>
        body {
            background-color: #003366;
            color: white;
        }
        .stApp {
            background-color: #003366;
            color: white;
        }
        h1, h2, h3, .stSelectbox label {
            text-align: center !important;
            color: white !important;
        }
        .stSelectbox {
            margin: 0 auto;
            display: table;
        }
    </style>
""", unsafe_allow_html=True)

# ========== LISTA DE OPÇÕES ==========
opcoes_uma_imagem = [
    "Casa Digital",
    "Laboratório de Artes",
    "Biblioteca",
    "AT-42/30",
    "AT-48/22",
    "AT-48/20",
    "AT-42/12",
    "Laboratório de Informática",
    "T.I FUP",
    "Laboratório de Química"
]

opcoes_duas_imagens = [
    "Enfermagem",
    "A1-42/62",
    "A1-42/60",
    "A1-48/52",
    "A1-48/50",
    "A1-42/42",
    "A1-48/40",
    "A1-48/32",
    "A1-42/34",
    "A1-48/22",
    "A1-42/30",
    "A1-48/20",
    "A1-48/10",
    "A1-42/12",
    "A1-82/8"
]

todas_opcoes = opcoes_uma_imagem + opcoes_duas_imagens

# ========== TÍTULO ==========
st.title("FuPMaps")

st.subheader("Chega mais, use o suporte de navegação visual...")


# ========== SELECTBOX ==========
selecao = st.selectbox("Selecione um ambiente ou sala:", todas_opcoes)

#Instruções de Navegação 
st.title("O mapa está orientado com as direções que você deve seguir em azul...")
st.subheader("Noções básicas do nosso espaço:")
st.text("A sigla AT se refere ao térro.")
st.text("A sigla A1 se refere ao 1° andar.")
st.text("Ao escolher uma sala do 1°andar, considere a foto da escada como um indicativo de via de acesso; se já estiver no 1° andar desconsidere-a.")
st.title("Considere a 'bola verde' como ponto de partida, siga a rota em azul.")

# ========== FUNÇÃO PARA GERAR NOMES DE ARQUIVO ==========
def gerar_nome_arquivo(nome_opcao):
    nome = nome_opcao.lower().replace(" ", "_").replace('"', '').replace("/", "-").replace(".", "").replace("–", "-")
    return nome

# ========== EXIBIÇÃO DE IMAGEM ==========
nome_base = gerar_nome_arquivo(selecao)
caminho_img = f"imagens/{nome_base}.jpg"
caminho_img1 = f"imagens/{nome_base}_1.jpg"
caminho_img2 = f"imagens/{nome_base}_2.jpg"

st.subheader(f"Visualização de: {selecao}")

if selecao in opcoes_uma_imagem:
    if os.path.exists(caminho_img):
        st.image(caminho_img, caption=selecao, use_container_width=True)
    else:
        st.warning("⚠️ Imagem não encontrada.")

elif selecao in opcoes_duas_imagens:
    col1, col2 = st.columns(2)
    with col1:
        if os.path.exists(caminho_img1):
            st.image(caminho_img1, caption="Vista 1", use_container_width=True)
        else:
            st.warning("⚠️ Imagem 1 não encontrada.")
    with col2:
        if os.path.exists(caminho_img2):
            st.image(caminho_img2, caption="Vista 2", use_container_width=True)
        else:
            st.warning("⚠️ Imagem 2 não encontrada.") 