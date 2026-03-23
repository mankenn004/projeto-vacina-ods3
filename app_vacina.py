import streamlit as st

# Configuração da página
st.set_page_config(page_title="Minhas Vacinas - ODS 3", page_icon="💉", layout="centered")

# --- NOVO CABEÇALHO COM LETRAS GIGANTES ---
st.markdown("""
    <div style="text-align: center; padding-bottom: 20px;">
        <h1 style="font-size: 60px; color: #0056b3; margin-bottom: 0px;">💉 Portal de Imunização</h1>
        <h2 style="font-size: 32px; color: #333333; margin-top: 10px;">Verifique as vacinas recomendadas para a sua faixa etária</h2>
        <p style="font-size: 22px; color: #555555;"><i>Este é um projeto de extensão (Biomedicina) para promover o ODS 3 e combater a desinformação vacinal.</i></p>
    </div>
    <hr style="margin-top: 0px;">
""", unsafe_allow_html=True)

# Entrada de dados do usuário
st.markdown("<h3 style='font-size: 24px;'>Informe seus dados:</h3>", unsafe_allow_html=True)
idade = st.number_input("Digite a sua idade (em anos):", min_value=0, max_value=120, value=25, step=1)

# Botão para verificar
st.write("") # Espaço extra
if st.button("Verificar Vacinas Pendentes", use_container_width=True):
    st.markdown("### 📋 Resultados:")
    
    # Lógica simplificada do PNI (Programa Nacional de Imunizações)
    if idade <= 9:
        st.info("**Fase: Criança (0 a 9 anos)**")
        st.write("Verifique na caderneta se a criança já tomou:")
        st.markdown("""
        * **BCG** (Tuberculose) - Dose única
        * **Poliomielite** (VIP/VOP) - 3 doses + reforços
        * **Pentavalente** (DTP/Hib/Hep B) - 3 doses
        * **Rotavírus** - 2 ou 3 doses
        * **Tríplice Viral** (Sarampo, Caxumba, Rubéola) - 2 doses
        """)
        st.warning("⚠️ Atenção Pais: Crianças têm um calendário denso. Levem a caderneta ao posto para conferência exata.")

    elif 10 <= idade <= 19:
        st.info("**Fase: Adolescente (10 a 19 anos)**")
        st.write("As principais vacinas para esta idade são:")
        st.markdown("""
        * **HPV** - 2 doses (Protege contra cânceres)
        * **Meningocócica ACWY** - Reforço ou dose única
        * **Hepatite B** - 3 doses (se não tomou na infância)
        * **Dupla Adulto (dT)** - Difteria e Tétano (Reforço a cada 10 anos)
        """)
        
    elif 20 <= idade <= 59:
        st.info("**Fase: Adulto (20 a 59 anos)**")
        st.write("Na fase adulta, você precisa manter atualizadas:")
        st.markdown("""
        * **Hepatite B** - 3 doses (se nunca tomou)
        * **Dupla Adulto (dT)** - Reforço a cada 10 anos (Muito importante em caso de acidentes!)
        * **Tríplice Viral** - Se não tomou na infância (até 29 anos: 2 doses; 30 a 59 anos: 1 dose)
        * **Febre Amarela** - Dose única (dependendo da região)
        """)

    else:
        st.info("**Fase: Idoso (60 anos ou mais)**")
        st.write("Para a terceira idade, o foco é prevenir infecções graves:")
        st.markdown("""
        * **Influenza (Gripe)** - Anualmente
        * **Pneumocócica 23-valente** - Protege contra pneumonias graves
        * **Hepatite B** - 3 doses (se não tomou antes)
        * **Dupla Adulto (dT)** - Reforço a cada 10 anos
        """)

    st.markdown("---")
    st.success("✅ **Lembrete:** Este aplicativo é um guia simplificado. Consulte sempre o ConecteSUS ou vá até uma UBS com seu documento e caderneta.")