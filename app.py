import streamlit as st

# Configuração da página - Visual romântico
st.set_page_config(page_title="Para O Meu Amor ❤️", page_icon="💖")

# --- MEMÓRIA DO SITE (SESSION STATE) ---
if "logado" not in st.session_state:
    st.session_state["logado"] = False

if "mostrar_surpresa" not in st.session_state:
    st.session_state["mostrar_surpresa"] = False

st.title("Olá! Seja bem-vinda ao nosso cantinho 🌹")

# --- TELA DE LOGIN ---
if not st.session_state["logado"]:
    st.subheader("🔒 Área Privada (Apenas para nós dois)")
    
    nome_usuario = st.text_input("Digite seu nome de usuário:")
    senha = st.text_input("Digite a nossa senha:", type="password")

    if st.button("Entrar"):
        if nome_usuario == "Maitê" and senha == "GATITO":
            st.session_state["logado"] = True
            st.rerun()
        else:
            st.error("Usuário ou senha incorretos. Tente novamente, meu amor! 💕")

# --- SITE LIBERADO ---
else:
    if st.button("Sair/Bloquear"):
        st.session_state["logado"] = False
        st.session_state["mostrar_surpresa"] = False 
        st.rerun()

    # Criando as abas
    aba1, aba2, aba3 = st.tabs(["💝 Nossa Declaração", "📸 Fotos e Figurinhas", "🎵 Dedicatoria"])

    # --- ABA 1: A DECLARAÇÃO DE AMOR + SUA FIGURINHA SURPRESA ---
    with aba1:
        st.subheader("Para a pessoa mais especial do mundo... 💕")
        
        st.info("""
        **Ma,**

        Criar este site foi a forma que encontrei de usar a tecnologia para te dizer o quanto você é importante para mim. 
        Cada linha de código aqui foi escrita pensando no quanto você me faz feliz. 
        
        Obrigado por ser essa pessoa incrível e por fazer os meus dias muito mais felizes. 
        Eu amo você hoje, amanhã e pra sempre! 🌹✨
        """)
        
        if st.button("Clique aqui para ver o meu amor por você"):
            st.session_state["mostrar_surpresa"] = True
            st.toast("Eu te amo muito! ❤️", icon="💖")
        
        if st.session_state["mostrar_surpresa"]:
            st.write("---")
            st.image("figurinha.webp", caption="Um pouquinho do meu amor por você! 🥰", width=200)

    # --- ABA 2: FOTO DA MAITÊ ---
    with aba2:
        st.subheader("A pessoa mais linda do universo 👑")
        st.image("foto_maitê.jpg", caption="Minha pessoa mais linda no mundo! ❤️", width=350)

    # --- ABA 3: DEDICATORIA + MÚSICA (TEXTO DO GUSTAVO ADD!) ---
    with aba3:
        st.subheader("Nossa Música Especial 🎵")
        st.write("Dê o play para ouvir enquanto lê:")
        
        # Player de música
        st.audio("nuts.mp3", format="audio/mp3")
        
        st.write("---")
        
        # Sua linda dedicação para a Maitê
        st.write("### DEDICATORIA")
        
        st.write("Eu, Gustavo, amo muito você. ❤️")
        
        st.write("""
        Eu faço esses tipos de demonstração de amor porque eu gostaria de fazer mais, Maitê. 
        Eu prometo tentar te fazer feliz e eu nunca quero te deixar triste ou magoada, 
        então eu prometo dar o meu melhor para que você seja feliz estando comigo.
        """)
        
        st.write("**Eu te amo.** ✨")