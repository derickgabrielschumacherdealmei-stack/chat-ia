import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="Assistente de IA",
    page_icon="🤖",
    layout="centered"
)

st.markdown("<h2 style='color: #000000;'>🤖 Assistente de IA - Rigoroso</h2>", unsafe_allow_html=True)

try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception:
    st.error("Erro crítico: A chave 'GEMINI_API_KEY' não foi configurada nos Secrets.")
    st.stop()

system_instruction = (
    "Você é um assistente de IA extremamente sério, literal e obediente. "
    "Siga rigorosamente as instruções e não invente informações."
)

generation_config = {
    "temperature": 0.1,
}

model = genai.GenerativeModel(
    model_name='gemini-1.0-pro',
    system_instruction=system_instruction,
    generation_config=generation_config,
)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = model.start_chat(history=[])

for message in st.session_state.chat_history.history:
    role = "user" if message.role == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(f"<div style='color: #000000;'>{message.parts[0].text}</div>", unsafe_allow_html=True)

if prompt_usuario := st.chat_input("Digite sua mensagem aqui..."):
    with st.chat_message("user"):
        st.markdown(f"<div style='color: #000000;'>{prompt_usuario}</div>", unsafe_allow_html=True)
    
    with st.chat_message("assistant"):
        with st.spinner("Processando..."):
            try:
                response = st.session_state.chat_history.send_message(prompt_usuario)
                st.markdown(f"<div style='color: #000000;'>{response.text}</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Erro na execução: {e}")
