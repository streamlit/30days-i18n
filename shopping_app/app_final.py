import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime, date, timedelta
import plotly.express as px
import plotly.graph_objects as go

# ====== CONFIGURAÇÃO ======
st.set_page_config(
    page_title="🧺 Lista Compartilhada da Família",
    page_icon="🧺",
    layout="wide"
)

# PWA
st.markdown("""
    <link rel="manifest" href="manifest.json">
    <meta name="theme-color" content="#0f766e">
    <script>
    if ('serviceWorker' in navigator) {
      window.addEventListener('load', function() {
        navigator.serviceWorker.register('service_worker.js');
      });
    }
    </script>
    """, unsafe_allow_html=True)

# ====== ESTILO ======
st.markdown("""
<style>
body { background-color: #f7f7f5; }
h1, h2, h3 { color: #0f766e; font-family: 'Arial Rounded MT Bold', sans-serif; }
.stButton>button {
    background-color: #0f766e !important;
    color: white !important;
    font-size: 20px !important;
    border-radius: 10px !important;
    padding: 10px 25px !important;
}
.stTextInput>div>div>input, .stSelectbox>div>div>select, .stNumberInput>div>div>input {
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# ====== DADOS ======
DATA_DIR = "shopping_app/data"
LISTA_ATUAL_FILE = os.path.join(DATA_DIR, "lista_atual.json")
HISTORICO_FILE = os.path.join(DATA_DIR, "historico_listas.json")
RESPONSAVEIS_FILE = os.path.join(DATA_DIR, "responsaveis.json")

def carregar_lista_atual():
    """Carrega a lista atual"""
    if os.path.exists(LISTA_ATUAL_FILE):
        with open(LISTA_ATUAL_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return pd.DataFrame(data) if data else pd.DataFrame(columns=[
                "Data", "Item", "Quantidade", "Preço (R$)",
                "Responsável", "Status", "Observação"
            ])
    return pd.DataFrame(columns=[
        "Data", "Item", "Quantidade", "Preço (R$)",
        "Responsável", "Status", "Observação"
    ])

def salvar_lista_atual(df):
    """Salva a lista atual"""
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(LISTA_ATUAL_FILE, 'w', encoding='utf-8') as f:
        json.dump(df.to_dict('records'), f, ensure_ascii=False, indent=2)

def carregar_historico():
    """Carrega histórico de listas"""
    if os.path.exists(HISTORICO_FILE):
        with open(HISTORICO_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar_historico(historico):
    """Salva histórico"""
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(HISTORICO_FILE, 'w', encoding='utf-8') as f:
        json.dump(historico, f, ensure_ascii=False, indent=2)

def carregar_responsaveis():
    """Carrega responsáveis"""
    if os.path.exists(RESPONSAVEIS_FILE):
        with open(RESPONSAVEIS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return ["Cuidadora Ana", "Cuidadora Maria", "Filho(a) João", "Filho(a) Paula", "Vizinho(a)", "Outro"]

def salvar_responsaveis(responsaveis):
    """Salva responsáveis"""
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(RESPONSAVEIS_FILE, 'w', encoding='utf-8') as f:
        json.dump(responsaveis, f, ensure_ascii=False, indent=2)

def finalizar_lista_atual():
    """Move lista atual para histórico"""
    df = carregar_lista_atual()
    if not df.empty:
        historico = carregar_historico()
        df['Total item'] = df['Quantidade'] * df['Preço (R$)']

        lista_finalizada = {
            "id": len(historico) + 1,
            "data_finalizacao": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "itens": df.to_dict('records'),
            "total": float(df['Total item'].sum()),
            "qtd_itens": len(df)
        }

        historico.append(lista_finalizada)
        salvar_historico(historico)

        # Limpa lista atual
        df_vazio = pd.DataFrame(columns=[
            "Data", "Item", "Quantidade", "Preço (R$)",
            "Responsável", "Status", "Observação"
        ])
        salvar_lista_atual(df_vazio)
        return True
    return False

# ====== INICIALIZAÇÃO ======
if 'lista' not in st.session_state:
    st.session_state.lista = carregar_lista_atual()

if 'pagina' not in st.session_state:
    st.session_state.pagina = "Lista"

# ====== CABEÇALHO ======
st.title("🧺 Lista Compartilhada da Família")
st.write("Feita com carinho para idosos, cuidadoras e filhos organizarem as compras juntos 💛")

# ====== MENU ======
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🧺 Lista Atual", use_container_width=True):
        st.session_state.pagina = "Lista"

with col2:
    if st.button("📜 Listas Antigas", use_container_width=True):
        st.session_state.pagina = "Histórico"

with col3:
    if st.button("📊 Ver Gastos", use_container_width=True):
        st.session_state.pagina = "Relatórios"

with col4:
    if st.button("👥 Pessoas", use_container_width=True):
        st.session_state.pagina = "Responsáveis"

st.markdown("---")

# ====== PÁGINA: LISTA ATUAL ======
if st.session_state.pagina == "Lista":

    # Modo de visualização
    modo = st.radio(
        "Como você vai usar agora?",
        ["📝 Tô organizando a lista", "🛒 Tô no mercado comprando"],
        horizontal=True
    )

    st.markdown("---")

    # Formulário
    st.subheader("➕ Colocar mais uma coisinha")

    col1, col2, col3 = st.columns(3)
    with col1:
        item = st.text_input("🧺 Nome do item", key="novo_item")
    with col2:
        qtd = st.number_input("🔢 Quantidade", min_value=1, value=1, key="nova_qtd")
    with col3:
        preco = st.number_input("💰 Preço (R$)", min_value=0.0, step=0.5, key="novo_preco")

    col4, col5 = st.columns(2)
    with col4:
        responsaveis = carregar_responsaveis()
        responsavel = st.selectbox("👩‍👩‍👧 Quem vai comprar?", responsaveis, key="novo_resp")
    with col5:
        status = st.selectbox("📦 Status", ["Falta comprar", "Já comprei"], key="novo_status")

    obs = st.text_input("🗒️ Observação (opcional)",
                       help="Ex: marca carne, sem sal, da marca X, para sábado",
                       key="nova_obs")

    data_compra = st.date_input("📅 Data dessa lista", value=date.today(), key="nova_data")

    if st.button("✨ Adicionar na lista", type="primary", use_container_width=True):
        if item:
            novo = pd.DataFrame(
                [[str(data_compra), item, qtd, preco, responsavel, status, obs]],
                columns=["Data", "Item", "Quantidade", "Preço (R$)", "Responsável", "Status", "Observação"]
            )
            st.session_state.lista = pd.concat([st.session_state.lista, novo], ignore_index=True)
            salvar_lista_atual(st.session_state.lista)
            st.success(f"✅ {item} entrou na lista!")
            st.rerun()
        else:
            st.warning("Opa! Coloca o nome do item primeiro 😉")

    st.markdown("---")

    # Visualização
    st.subheader("📝 Sua lista de compras")

    if st.session_state.lista.empty:
        st.info("💭 Ainda não tem nada na lista. Coloca pelo menos um item lá em cima.")
    else:
        df = st.session_state.lista.copy()
        df["Total item"] = df["Quantidade"] * df["Preço (R$)"]

        if modo == "🛒 Tô no mercado comprando":
            st.write("🛒 **Modo mercado:** mostrando só o que falta comprar")
            faltando = df[df["Status"] == "Falta comprar"]

            if not faltando.empty:
                # Lista simplificada para o mercado
                for idx, row in faltando.iterrows():
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.markdown(f"### 🧺 {row['Item']}")
                        st.write(f"**Quantidade:** {row['Quantidade']}")
                        if row['Observação']:
                            st.info(f"📝 {row['Observação']}")
                        st.write(f"👤 {row['Responsável']}")

                    with col2:
                        if st.button(f"✅ Comprei", key=f"comprei_{idx}"):
                            st.session_state.lista.loc[idx, 'Status'] = 'Já comprei'
                            salvar_lista_atual(st.session_state.lista)
                            st.rerun()

                    st.markdown("---")

                total_faltando = faltando['Total item'].sum()
                st.success(f"💰 Ainda falta: **R$ {total_faltando:.2f}**")
            else:
                st.success("🎉 Tá tudo comprado! Pode ir pra casa 💛")
        else:
            # Modo organizando - tabela completa
            st.dataframe(df, use_container_width=True, hide_index=True)

            # Botão para marcar como comprado
            st.write("**Marcar itens como comprados:**")
            itens_faltando = df[df["Status"] == "Falta comprar"]

            if not itens_faltando.empty:
                for idx in itens_faltando.index:
                    col1, col2 = st.columns([4, 1])
                    with col1:
                        st.write(f"{df.loc[idx, 'Item']} - {df.loc[idx, 'Quantidade']}x")
                    with col2:
                        if st.button("✅", key=f"mark_{idx}"):
                            st.session_state.lista.loc[idx, 'Status'] = 'Já comprei'
                            salvar_lista_atual(st.session_state.lista)
                            st.rerun()

        # Total
        total_geral = df["Total item"].sum()
        st.markdown(f"### 💵 Total estimado: **R$ {total_geral:.2f}**")

        # Download
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Baixar lista (pra mandar no WhatsApp)",
            data=csv,
            file_name=f"lista_compras_{date.today()}.csv",
            mime="text/csv"
        )

        st.markdown("---")

        # Resumo rápido
        st.subheader("📊 Resumo rapidinho")

        col1, col2, col3, col4 = st.columns(4)

        qtd_itens = len(df)
        qtd_falta = len(df[df["Status"] == "Falta comprar"])
        qtd_ok = len(df[df["Status"] == "Já comprei"])

        with col1:
            st.metric("🧺 Itens na lista", qtd_itens)
        with col2:
            st.metric("✅ Já comprados", qtd_ok)
        with col3:
            st.metric("🟡 Faltando", qtd_falta)
        with col4:
            st.metric("💰 Total", f"R$ {total_geral:.2f}")

        st.markdown("---")

        # Ações
        col1, col2 = st.columns(2)

        with col1:
            if st.button("🧽 Começar lista nova", use_container_width=True):
                if not st.session_state.lista.empty:
                    finalizar_lista_atual()
                    st.session_state.lista = carregar_lista_atual()
                    st.success("✨ Lista antiga guardada! Bora começar outra 💛")
                    st.rerun()

        with col2:
            if st.button("🗑️ Apagar tudo (cuidado!)", use_container_width=True):
                st.session_state.lista = pd.DataFrame(columns=[
                    "Data", "Item", "Quantidade", "Preço (R$)",
                    "Responsável", "Status", "Observação"
                ])
                salvar_lista_atual(st.session_state.lista)
                st.info("Lista apagada!")
                st.rerun()

# ====== PÁGINA: HISTÓRICO ======
elif st.session_state.pagina == "Histórico":

    st.subheader("📜 Listas Antigas da Família")

    historico = carregar_historico()

    if not historico:
        st.info("💭 Ainda não tem listas antigas guardadas. Quando terminar uma lista, ela vem pra cá!")
    else:
        st.write(f"💾 Você tem **{len(historico)}** listas guardadas")

        for lista in reversed(historico):  # Mais recente primeiro
            with st.expander(
                f"📋 Lista #{lista['id']} - {lista['data_finalizacao'][:10]} - R$ {lista['total']:.2f}"
            ):
                col1, col2, col3 = st.columns(3)

                with col1:
                    st.write(f"**📅 Data:** {lista['data_finalizacao'][:10]}")
                with col2:
                    st.write(f"**📦 Itens:** {lista['qtd_itens']}")
                with col3:
                    st.write(f"**💰 Total:** R$ {lista['total']:.2f}")

                # Tabela de itens
                df_lista = pd.DataFrame(lista['itens'])
                if 'Total item' not in df_lista.columns:
                    df_lista['Total item'] = df_lista['Quantidade'] * df_lista['Preço (R$)']

                st.dataframe(
                    df_lista[['Item', 'Quantidade', 'Responsável', 'Status', 'Total item']],
                    use_container_width=True,
                    hide_index=True
                )

# ====== PÁGINA: RELATÓRIOS ======
elif st.session_state.pagina == "Relatórios":

    st.subheader("📊 Ver Como Está os Gastos")

    historico = carregar_historico()

    if not historico:
        st.info("💭 Ainda não tem listas finalizadas pra gerar relatórios. Termine pelo menos uma lista!")
    else:
        # Extrair todos os itens
        todos_itens = []
        for lista in historico:
            for item in lista['itens']:
                item_copy = item.copy()
                item_copy['data_lista'] = lista['data_finalizacao']
                item_copy['lista_id'] = lista['id']
                todos_itens.append(item_copy)

        df = pd.DataFrame(todos_itens)

        if 'Total item' not in df.columns:
            df['Total item'] = df['Quantidade'] * df['Preço (R$)']

        # Métricas
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("📋 Listas feitas", len(historico))

        with col2:
            total_gasto = sum(l['total'] for l in historico)
            st.metric("💰 Total gasto", f"R$ {total_gasto:.2f}")

        with col3:
            media = total_gasto / len(historico)
            st.metric("📊 Média/lista", f"R$ {media:.2f}")

        with col4:
            st.metric("🧺 Total itens", len(df))

        st.markdown("---")

        # Gráficos
        col1, col2 = st.columns(2)

        with col1:
            st.write("### 👥 Quem mais comprou")
            gastos_resp = df.groupby('Responsável')['Total item'].sum().sort_values(ascending=False)

            fig = px.bar(
                x=gastos_resp.index,
                y=gastos_resp.values,
                labels={'x': 'Pessoa', 'y': 'Gasto (R$)'},
                color=gastos_resp.values,
                color_continuous_scale='Teal'
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.write("### 📦 O que comprou")
            status_count = df['Status'].value_counts()

            fig = px.pie(
                values=status_count.values,
                names=status_count.index,
                color_discrete_sequence=['#28a745', '#ffc107']
            )
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")

        # Top 10
        st.write("### 🏆 Top 10 coisas que mais compraram")
        top_itens = df.groupby('Item').agg({
            'Quantidade': 'sum',
            'Total item': 'sum'
        }).sort_values('Total item', ascending=False).head(10)

        top_itens_display = top_itens.reset_index()
        top_itens_display.columns = ['Item', 'Vezes que comprou', 'Gastou (R$)']
        top_itens_display['Gastou (R$)'] = top_itens_display['Gastou (R$)'].apply(lambda x: f"R$ {x:.2f}")

        st.dataframe(top_itens_display, use_container_width=True, hide_index=True)

        st.markdown("---")

        # Calculadora de divisão
        st.write("### 💰 Dividir entre os filhos")

        num_filhos = st.number_input("Quantos filhos vão dividir?", min_value=1, value=2)
        valor_por_filho = total_gasto / num_filhos

        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Total gasto:** R$ {total_gasto:.2f}")
        with col2:
            st.success(f"**Cada um paga:** R$ {valor_por_filho:.2f}")

# ====== PÁGINA: RESPONSÁVEIS ======
elif st.session_state.pagina == "Responsáveis":

    st.subheader("👥 Quem Ajuda nas Compras")

    responsaveis = carregar_responsaveis()

    st.write("**Pessoas cadastradas:**")

    for i, resp in enumerate(responsaveis):
        col1, col2 = st.columns([4, 1])

        with col1:
            st.markdown(f"**{i+1}.** {resp}")

        with col2:
            if st.button("🗑️", key=f"del_{i}"):
                responsaveis.pop(i)
                salvar_responsaveis(responsaveis)
                st.success("Removido!")
                st.rerun()

    st.markdown("---")

    st.write("**Adicionar alguém novo:**")

    col1, col2 = st.columns([3, 1])

    with col1:
        novo_resp = st.text_input("Nome da pessoa", placeholder="Ex: Cuidadora Clara")

    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("➕ Adicionar", use_container_width=True):
            if novo_resp and novo_resp not in responsaveis:
                responsaveis.append(novo_resp)
                salvar_responsaveis(responsaveis)
                st.success(f"✅ {novo_resp} foi adicionado!")
                st.rerun()
            elif novo_resp in responsaveis:
                st.warning("Essa pessoa já tá na lista!")

# ====== RODAPÉ ======
st.markdown("---")
st.caption("✨ Feito com carinho pra quem cuida. Pode instalar no celular e usar sempre 💛")
