import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go

# Configuração da página
st.set_page_config(
    page_title="Controle de Compras - Família",
    page_icon="🛒",
    layout="wide"
)

# PWA - Manifesto e Service Worker
st.markdown("""
    <!-- PWA -->
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

# Estilos CSS para melhor visualização
st.markdown("""
    <style>
    .big-font {
        font-size: 24px !important;
        font-weight: bold;
    }
    .medium-font {
        font-size: 20px !important;
    }
    .stButton>button {
        font-size: 18px;
        height: 3em;
        width: 100%;
    }
    .stTextInput>div>div>input {
        font-size: 18px;
    }
    .stSelectbox>div>div>select {
        font-size: 18px;
    }
    .stNumberInput>div>div>input {
        font-size: 18px;
    }
    h1 {
        color: #2E86AB;
    }
    h2 {
        color: #A23B72;
    }
    h3 {
        color: #F18F01;
    }
    .status-pendente {
        background-color: #FFF3CD;
        padding: 10px;
        border-radius: 5px;
        border-left: 5px solid #FFC107;
    }
    .status-aprovada {
        background-color: #D4EDDA;
        padding: 10px;
        border-radius: 5px;
        border-left: 5px solid #28A745;
    }
    .status-comprada {
        background-color: #D1ECF1;
        padding: 10px;
        border-radius: 5px;
        border-left: 5px solid #17A2B8;
    }
    .status-rejeitada {
        background-color: #F8D7DA;
        padding: 10px;
        border-radius: 5px;
        border-left: 5px solid #DC3545;
    }
    </style>
    """, unsafe_allow_html=True)

# Caminhos dos arquivos de dados
DATA_DIR = "shopping_app/data"
LISTAS_FILE = os.path.join(DATA_DIR, "listas.json")
COMPRAS_FILE = os.path.join(DATA_DIR, "compras.json")
CUIDADORAS_FILE = os.path.join(DATA_DIR, "cuidadoras.json")

# Funções auxiliares
def carregar_listas():
    """Carrega as listas de compras do arquivo JSON"""
    if os.path.exists(LISTAS_FILE):
        with open(LISTAS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar_listas(listas):
    """Salva as listas no arquivo JSON"""
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(LISTAS_FILE, 'w', encoding='utf-8') as f:
        json.dump(listas, f, ensure_ascii=False, indent=2)

def carregar_compras():
    """Carrega as compras realizadas do arquivo JSON"""
    if os.path.exists(COMPRAS_FILE):
        with open(COMPRAS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar_compras(compras):
    """Salva as compras no arquivo JSON"""
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(COMPRAS_FILE, 'w', encoding='utf-8') as f:
        json.dump(compras, f, ensure_ascii=False, indent=2)

def carregar_cuidadoras():
    """Carrega as cuidadoras do arquivo JSON"""
    if os.path.exists(CUIDADORAS_FILE):
        with open(CUIDADORAS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return ["Ana", "Maria", "João"]  # Cuidadoras padrão

def salvar_cuidadoras(cuidadoras):
    """Salva as cuidadoras no arquivo JSON"""
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(CUIDADORAS_FILE, 'w', encoding='utf-8') as f:
        json.dump(cuidadoras, f, ensure_ascii=False, indent=2)

def criar_lista(cuidadora, itens, observacoes=""):
    """Cria uma nova lista de compras"""
    listas = carregar_listas()
    lista = {
        "id": len(listas) + 1,
        "data_criacao": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cuidadora": cuidadora,
        "status": "Pendente",  # Pendente, Aprovada, Comprada, Rejeitada
        "itens": itens,
        "observacoes": observacoes,
        "valor_estimado": sum(item['preco_estimado'] * item['quantidade'] for item in itens),
        "valor_real": 0,
        "data_aprovacao": None,
        "data_compra": None,
        "aprovada_por": None,
        "comprada_por": None
    }
    listas.append(lista)
    salvar_listas(listas)
    return lista['id']

def atualizar_status_lista(lista_id, novo_status, usuario="", valor_real=None):
    """Atualiza o status de uma lista"""
    listas = carregar_listas()
    for lista in listas:
        if lista['id'] == lista_id:
            lista['status'] = novo_status
            if novo_status == "Aprovada":
                lista['data_aprovacao'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                lista['aprovada_por'] = usuario
            elif novo_status == "Comprada":
                lista['data_compra'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                lista['comprada_por'] = usuario
                if valor_real:
                    lista['valor_real'] = valor_real
            break
    salvar_listas(listas)

def atualizar_itens_lista(lista_id, novos_itens):
    """Atualiza os itens de uma lista"""
    listas = carregar_listas()
    for lista in listas:
        if lista['id'] == lista_id:
            lista['itens'] = novos_itens
            lista['valor_estimado'] = sum(item['preco_estimado'] * item['quantidade'] for item in novos_itens)
            break
    salvar_listas(listas)

def registrar_compra_realizada(lista_id, valor_total, observacoes_compra=""):
    """Registra uma compra realizada com base em uma lista"""
    listas = carregar_listas()
    compras = carregar_compras()

    lista = next((l for l in listas if l['id'] == lista_id), None)
    if lista:
        compra = {
            "id": len(compras) + 1,
            "lista_id": lista_id,
            "data_compra": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "cuidadora": lista['cuidadora'],
            "itens": lista['itens'],
            "valor_estimado": lista['valor_estimado'],
            "valor_real": valor_total,
            "diferenca": valor_total - lista['valor_estimado'],
            "observacoes": observacoes_compra
        }
        compras.append(compra)
        salvar_compras(compras)
        atualizar_status_lista(lista_id, "Comprada", valor_real=valor_total)

# Inicialização
if 'pagina' not in st.session_state:
    st.session_state.pagina = "Listas Pendentes"

if 'perfil' not in st.session_state:
    st.session_state.perfil = "Família"  # ou "Cuidadora"

# Título principal
col1, col2 = st.columns([4, 1])
with col1:
    st.markdown("# 🛒 Controle de Compras Familiar")
    st.markdown("### Sistema de controle e aprovação de listas de compras")

with col2:
    perfil = st.selectbox(
        "👤 Perfil:",
        ["Família", "Cuidadora"],
        key='perfil'
    )

st.markdown("---")

# Menu de navegação baseado no perfil
if st.session_state.perfil == "Cuidadora":
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("➕ Nova Lista", use_container_width=True):
            st.session_state.pagina = "Nova Lista"

    with col2:
        if st.button("📋 Minhas Listas", use_container_width=True):
            st.session_state.pagina = "Minhas Listas"

    with col3:
        if st.button("👥 Cuidadoras", use_container_width=True):
            st.session_state.pagina = "Cuidadoras"

else:  # Família
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        listas = carregar_listas()
        pendentes = len([l for l in listas if l['status'] == 'Pendente'])
        if st.button(f"⏳ Pendentes ({pendentes})", use_container_width=True):
            st.session_state.pagina = "Listas Pendentes"

    with col2:
        if st.button("✅ Aprovadas", use_container_width=True):
            st.session_state.pagina = "Listas Aprovadas"

    with col3:
        if st.button("🛍️ Histórico", use_container_width=True):
            st.session_state.pagina = "Histórico"

    with col4:
        if st.button("📊 Relatórios", use_container_width=True):
            st.session_state.pagina = "Relatórios"

st.markdown("---")

# ==================== PÁGINAS PARA CUIDADORA ====================

if st.session_state.perfil == "Cuidadora":

    # Página: Nova Lista
    if st.session_state.pagina == "Nova Lista":
        st.markdown("## ➕ Criar Nova Lista de Compras")

        cuidadoras = carregar_cuidadoras()
        cuidadora = st.selectbox("👤 Seu nome:", cuidadoras)

        st.markdown("### 🛍️ Itens da Lista")

        if 'itens_lista' not in st.session_state:
            st.session_state.itens_lista = []

        # Adicionar item
        col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 1])

        with col1:
            novo_item = st.text_input("Item", placeholder="Ex: Leite integral", key="novo_item")
        with col2:
            categoria = st.selectbox("Categoria", ["Alimentação", "Medicamentos", "Higiene", "Limpeza", "Outros"], key="nova_categoria")
        with col3:
            quantidade = st.number_input("Qtd", min_value=1, value=1, key="nova_qtd")
        with col4:
            preco_est = st.number_input("Preço est. (R$)", min_value=0.0, value=0.0, format="%.2f", key="novo_preco")
        with col5:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("➕ Adicionar"):
                if novo_item:
                    st.session_state.itens_lista.append({
                        "item": novo_item,
                        "categoria": categoria,
                        "quantidade": quantidade,
                        "preco_estimado": preco_est
                    })
                    st.rerun()

        # Exibir itens adicionados
        if st.session_state.itens_lista:
            st.markdown("### 📝 Itens Adicionados:")

            for idx, item in enumerate(st.session_state.itens_lista):
                col1, col2, col3, col4, col5, col6 = st.columns([3, 1, 1, 1, 1, 1])

                with col1:
                    st.write(f"**{item['item']}**")
                with col2:
                    st.write(item['categoria'])
                with col3:
                    st.write(f"{item['quantidade']}x")
                with col4:
                    st.write(f"R$ {item['preco_estimado']:.2f}")
                with col5:
                    st.write(f"**R$ {item['quantidade'] * item['preco_estimado']:.2f}**")
                with col6:
                    if st.button("🗑️", key=f"del_{idx}"):
                        st.session_state.itens_lista.pop(idx)
                        st.rerun()

            total_estimado = sum(item['quantidade'] * item['preco_estimado'] for item in st.session_state.itens_lista)
            st.markdown(f"### 💰 Total Estimado: R$ {total_estimado:.2f}")

            observacoes = st.text_area("📝 Observações (opcional)", placeholder="Ex: Preferir marcas específicas, observações sobre a paciente...")

            st.markdown("---")
            col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                if st.button("📤 ENVIAR LISTA PARA APROVAÇÃO", use_container_width=True, type="primary"):
                    lista_id = criar_lista(cuidadora, st.session_state.itens_lista, observacoes)
                    st.success(f"✅ Lista #{lista_id} enviada para aprovação da família!")
                    st.session_state.itens_lista = []
                    st.balloons()
                    st.rerun()

    # Página: Minhas Listas
    elif st.session_state.pagina == "Minhas Listas":
        st.markdown("## 📋 Minhas Listas de Compras")

        listas = carregar_listas()

        if not listas:
            st.info("📭 Você ainda não criou nenhuma lista.")
        else:
            # Filtrar por cuidadora
            cuidadoras = carregar_cuidadoras()
            filtro_cuidadora = st.selectbox("Filtrar por cuidadora:", ["Todas"] + cuidadoras)

            listas_filtradas = listas if filtro_cuidadora == "Todas" else [l for l in listas if l['cuidadora'] == filtro_cuidadora]

            # Estatísticas
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total de Listas", len(listas_filtradas))
            with col2:
                pendentes = len([l for l in listas_filtradas if l['status'] == 'Pendente'])
                st.metric("Pendentes", pendentes)
            with col3:
                aprovadas = len([l for l in listas_filtradas if l['status'] == 'Aprovada'])
                st.metric("Aprovadas", aprovadas)
            with col4:
                compradas = len([l for l in listas_filtradas if l['status'] == 'Comprada'])
                st.metric("Compradas", compradas)

            st.markdown("---")

            # Exibir listas
            for lista in sorted(listas_filtradas, key=lambda x: x['data_criacao'], reverse=True):
                status_class = f"status-{lista['status'].lower()}"

                with st.expander(
                    f"📋 Lista #{lista['id']} - {lista['cuidadora']} - {lista['status']} - R$ {lista['valor_estimado']:.2f}"
                ):
                    col1, col2 = st.columns(2)

                    with col1:
                        st.markdown(f"**👤 Cuidadora:** {lista['cuidadora']}")
                        st.markdown(f"**📅 Criada em:** {lista['data_criacao']}")
                        st.markdown(f"**📊 Status:** {lista['status']}")
                        if lista.get('observacoes'):
                            st.markdown(f"**📝 Observações:** {lista['observacoes']}")

                    with col2:
                        st.markdown(f"**💰 Valor Estimado:** R$ {lista['valor_estimado']:.2f}")
                        if lista['status'] == 'Comprada':
                            st.markdown(f"**💵 Valor Real:** R$ {lista.get('valor_real', 0):.2f}")
                            diferenca = lista.get('valor_real', 0) - lista['valor_estimado']
                            cor = "🔴" if diferenca > 0 else "🟢"
                            st.markdown(f"**📊 Diferença:** {cor} R$ {diferenca:.2f}")

                    st.markdown("#### 🛍️ Itens:")
                    df_itens = pd.DataFrame(lista['itens'])
                    df_itens['total'] = df_itens['quantidade'] * df_itens['preco_estimado']
                    st.dataframe(df_itens, use_container_width=True, hide_index=True)

    # Página: Cuidadoras
    elif st.session_state.pagina == "Cuidadoras":
        st.markdown("## 👥 Gerenciar Cuidadoras")

        cuidadoras = carregar_cuidadoras()

        st.markdown("### Cuidadoras Cadastradas")

        for i, cuidadora in enumerate(cuidadoras):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"#### 👤 {cuidadora}")
            with col2:
                if st.button(f"🗑️ Remover", key=f"rem_cuid_{i}"):
                    cuidadoras.remove(cuidadora)
                    salvar_cuidadoras(cuidadoras)
                    st.rerun()

        st.markdown("---")
        st.markdown("### Adicionar Nova Cuidadora")

        col1, col2 = st.columns([2, 1])
        with col1:
            nova_cuidadora = st.text_input("Nome da cuidadora", placeholder="Digite o nome completo")

        with col2:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("➕ Adicionar", use_container_width=True):
                if nova_cuidadora and nova_cuidadora not in cuidadoras:
                    cuidadoras.append(nova_cuidadora)
                    salvar_cuidadoras(cuidadoras)
                    st.success(f"✅ {nova_cuidadora} adicionada!")
                    st.rerun()
                elif nova_cuidadora in cuidadoras:
                    st.warning("⚠️ Cuidadora já cadastrada!")

# ==================== PÁGINAS PARA FAMÍLIA ====================

else:  # Perfil Família

    # Página: Listas Pendentes
    if st.session_state.pagina == "Listas Pendentes":
        st.markdown("## ⏳ Listas Pendentes de Aprovação")

        listas = carregar_listas()
        listas_pendentes = [l for l in listas if l['status'] == 'Pendente']

        if not listas_pendentes:
            st.success("✅ Não há listas pendentes de aprovação!")
        else:
            st.warning(f"⚠️ Você tem {len(listas_pendentes)} lista(s) aguardando aprovação")

            for lista in sorted(listas_pendentes, key=lambda x: x['data_criacao'], reverse=True):
                with st.expander(
                    f"📋 Lista #{lista['id']} - {lista['cuidadora']} - {lista['data_criacao'][:10]} - R$ {lista['valor_estimado']:.2f}",
                    expanded=True
                ):
                    col1, col2 = st.columns([2, 1])

                    with col1:
                        st.markdown(f"**👤 Solicitada por:** {lista['cuidadora']}")
                        st.markdown(f"**📅 Data:** {lista['data_criacao']}")
                        if lista.get('observacoes'):
                            st.info(f"📝 **Observações:** {lista['observacoes']}")

                    with col2:
                        st.markdown(f"### 💰 R$ {lista['valor_estimado']:.2f}")

                    st.markdown("#### 🛍️ Itens Solicitados:")

                    # Permitir edição dos itens
                    itens_editados = []
                    for idx, item in enumerate(lista['itens']):
                        col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 1])

                        with col1:
                            item_nome = st.text_input("Item", value=item['item'], key=f"item_{lista['id']}_{idx}", label_visibility="collapsed")
                        with col2:
                            item_cat = st.selectbox("Cat", ["Alimentação", "Medicamentos", "Higiene", "Limpeza", "Outros"],
                                                   index=["Alimentação", "Medicamentos", "Higiene", "Limpeza", "Outros"].index(item['categoria']),
                                                   key=f"cat_{lista['id']}_{idx}", label_visibility="collapsed")
                        with col3:
                            item_qtd = st.number_input("Qtd", min_value=1, value=item['quantidade'],
                                                      key=f"qtd_{lista['id']}_{idx}", label_visibility="collapsed")
                        with col4:
                            item_preco = st.number_input("Preço", min_value=0.0, value=item['preco_estimado'], format="%.2f",
                                                        key=f"preco_{lista['id']}_{idx}", label_visibility="collapsed")
                        with col5:
                            st.markdown(f"**R$ {item_qtd * item_preco:.2f}**")

                        itens_editados.append({
                            "item": item_nome,
                            "categoria": item_cat,
                            "quantidade": item_qtd,
                            "preco_estimado": item_preco
                        })

                    total_editado = sum(item['quantidade'] * item['preco_estimado'] for item in itens_editados)
                    st.markdown(f"### 💰 Total: R$ {total_editado:.2f}")

                    st.markdown("---")

                    col1, col2, col3, col4 = st.columns(4)

                    with col1:
                        if st.button("💾 Salvar Alterações", key=f"save_{lista['id']}", use_container_width=True):
                            atualizar_itens_lista(lista['id'], itens_editados)
                            st.success("✅ Lista atualizada!")
                            st.rerun()

                    with col2:
                        nome_aprovador = st.text_input("Seu nome", key=f"nome_apr_{lista['id']}", placeholder="Digite seu nome", label_visibility="collapsed")

                    with col3:
                        if st.button("✅ Aprovar", key=f"apr_{lista['id']}", use_container_width=True, type="primary"):
                            if nome_aprovador:
                                atualizar_status_lista(lista['id'], "Aprovada", nome_aprovador)
                                st.success(f"✅ Lista aprovada! Você pode comprar via Shopper.")
                                st.rerun()
                            else:
                                st.error("⚠️ Digite seu nome para aprovar")

                    with col4:
                        if st.button("❌ Rejeitar", key=f"rej_{lista['id']}", use_container_width=True):
                            if nome_aprovador:
                                atualizar_status_lista(lista['id'], "Rejeitada", nome_aprovador)
                                st.info("Lista rejeitada")
                                st.rerun()
                            else:
                                st.error("⚠️ Digite seu nome para rejeitar")

    # Página: Listas Aprovadas
    elif st.session_state.pagina == "Listas Aprovadas":
        st.markdown("## ✅ Listas Aprovadas - Pronto para Comprar")

        listas = carregar_listas()
        listas_aprovadas = [l for l in listas if l['status'] == 'Aprovada']

        if not listas_aprovadas:
            st.info("📭 Não há listas aprovadas aguardando compra.")
        else:
            st.success(f"✅ {len(listas_aprovadas)} lista(s) aprovada(s) - Compre via Shopper e registre aqui!")

            for lista in sorted(listas_aprovadas, key=lambda x: x['data_aprovacao'], reverse=True):
                with st.expander(
                    f"📋 Lista #{lista['id']} - {lista['cuidadora']} - R$ {lista['valor_estimado']:.2f} (estimado)",
                    expanded=True
                ):
                    col1, col2 = st.columns(2)

                    with col1:
                        st.markdown(f"**👤 Solicitada por:** {lista['cuidadora']}")
                        st.markdown(f"**📅 Criada em:** {lista['data_criacao'][:10]}")
                        st.markdown(f"**✅ Aprovada em:** {lista['data_aprovacao'][:10]}")
                        st.markdown(f"**👤 Aprovada por:** {lista['aprovada_por']}")

                    with col2:
                        st.markdown(f"### 💰 Valor Estimado: R$ {lista['valor_estimado']:.2f}")

                    if lista.get('observacoes'):
                        st.info(f"📝 **Observações:** {lista['observacoes']}")

                    st.markdown("#### 🛍️ Itens para Comprar:")
                    df_itens = pd.DataFrame(lista['itens'])
                    df_itens['total_estimado'] = df_itens['quantidade'] * df_itens['preco_estimado']
                    df_itens_display = df_itens[['item', 'categoria', 'quantidade', 'preco_estimado', 'total_estimado']]
                    df_itens_display.columns = ['Item', 'Categoria', 'Quantidade', 'Preço Estimado', 'Total']
                    st.dataframe(df_itens_display, use_container_width=True, hide_index=True)

                    st.markdown("---")
                    st.markdown("### 💳 Registrar Compra Realizada")

                    col1, col2, col3 = st.columns([2, 2, 1])

                    with col1:
                        valor_real = st.number_input(
                            "Valor total pago no Shopper (R$)",
                            min_value=0.0,
                            value=lista['valor_estimado'],
                            format="%.2f",
                            key=f"valor_real_{lista['id']}"
                        )

                    with col2:
                        obs_compra = st.text_input(
                            "Observações sobre a compra",
                            placeholder="Ex: Trocas, substituições...",
                            key=f"obs_compra_{lista['id']}"
                        )

                    with col3:
                        st.markdown("<br>", unsafe_allow_html=True)
                        if st.button("✅ Confirmar Compra", key=f"conf_{lista['id']}", use_container_width=True):
                            registrar_compra_realizada(lista['id'], valor_real, obs_compra)
                            st.success("✅ Compra registrada com sucesso!")
                            st.balloons()
                            st.rerun()

                    # Mostrar diferença
                    diferenca = valor_real - lista['valor_estimado']
                    if diferenca > 0:
                        st.warning(f"⚠️ Compra ficará R$ {abs(diferenca):.2f} mais cara que o estimado")
                    elif diferenca < 0:
                        st.success(f"✅ Economia de R$ {abs(diferenca):.2f} em relação ao estimado!")

    # Página: Histórico
    elif st.session_state.pagina == "Histórico":
        st.markdown("## 🛍️ Histórico de Compras Realizadas")

        compras = carregar_compras()

        if not compras:
            st.info("📭 Ainda não há compras realizadas.")
        else:
            # Filtros
            col1, col2, col3 = st.columns(3)

            df_compras = pd.DataFrame(compras)

            with col1:
                cuidadoras_lista = ["Todas"] + sorted(df_compras['cuidadora'].unique().tolist())
                filtro_cuidadora = st.selectbox("Filtrar por cuidadora", cuidadoras_lista)

            with col2:
                periodo = st.selectbox("Período", ["Últimos 7 dias", "Últimos 30 dias", "Últimos 90 dias", "Todos"])

            with col3:
                ordem = st.selectbox("Ordenar por", ["Mais recentes", "Mais antigas", "Maior valor", "Menor valor"])

            # Aplicar filtros
            df_filtrado = df_compras.copy()

            if filtro_cuidadora != "Todas":
                df_filtrado = df_filtrado[df_filtrado['cuidadora'] == filtro_cuidadora]

            if periodo != "Todos":
                dias = {"Últimos 7 dias": 7, "Últimos 30 dias": 30, "Últimos 90 dias": 90}[periodo]
                data_limite = (datetime.now() - timedelta(days=dias)).strftime("%Y-%m-%d")
                df_filtrado = df_filtrado[df_filtrado['data_compra'] >= data_limite]

            # Ordenar
            if ordem == "Mais recentes":
                df_filtrado = df_filtrado.sort_values('data_compra', ascending=False)
            elif ordem == "Mais antigas":
                df_filtrado = df_filtrado.sort_values('data_compra', ascending=True)
            elif ordem == "Maior valor":
                df_filtrado = df_filtrado.sort_values('valor_real', ascending=False)
            else:
                df_filtrado = df_filtrado.sort_values('valor_real', ascending=True)

            # Resumo
            st.markdown("### 📊 Resumo")
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("Total de Compras", len(df_filtrado))
            with col2:
                st.metric("Gasto Total", f"R$ {df_filtrado['valor_real'].sum():.2f}")
            with col3:
                st.metric("Média por Compra", f"R$ {df_filtrado['valor_real'].mean():.2f}")
            with col4:
                diferenca_total = df_filtrado['diferenca'].sum()
                label = "Economia Total" if diferenca_total < 0 else "Gasto Extra"
                st.metric(label, f"R$ {abs(diferenca_total):.2f}")

            st.markdown("---")

            # Exibir compras
            for idx, compra in df_filtrado.iterrows():
                with st.expander(
                    f"🛍️ Compra #{compra['id']} - {compra['data_compra'][:10]} - {compra['cuidadora']} - R$ {compra['valor_real']:.2f}"
                ):
                    col1, col2 = st.columns(2)

                    with col1:
                        st.markdown(f"**👤 Cuidadora:** {compra['cuidadora']}")
                        st.markdown(f"**📅 Data:** {compra['data_compra']}")
                        st.markdown(f"**📋 Lista:** #{compra['lista_id']}")

                    with col2:
                        st.markdown(f"**💰 Valor Estimado:** R$ {compra['valor_estimado']:.2f}")
                        st.markdown(f"**💵 Valor Real:** R$ {compra['valor_real']:.2f}")
                        diferenca = compra['diferenca']
                        cor = "🔴" if diferenca > 0 else "🟢"
                        st.markdown(f"**📊 Diferença:** {cor} R$ {diferenca:.2f}")

                    if compra.get('observacoes'):
                        st.info(f"📝 {compra['observacoes']}")

                    st.markdown("#### 🛍️ Itens Comprados:")
                    df_itens = pd.DataFrame(compra['itens'])
                    df_itens['total'] = df_itens['quantidade'] * df_itens['preco_estimado']
                    st.dataframe(df_itens, use_container_width=True, hide_index=True)

    # Página: Relatórios
    elif st.session_state.pagina == "Relatórios":
        st.markdown("## 📊 Relatórios e Análises")

        compras = carregar_compras()

        if not compras:
            st.info("📭 Ainda não há dados suficientes para gerar relatórios.")
        else:
            df = pd.DataFrame(compras)
            df['data_compra'] = pd.to_datetime(df['data_compra'])
            df['mes'] = df['data_compra'].dt.to_period('M').astype(str)
            df['dia'] = df['data_compra'].dt.date

            # Métricas gerais
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("Total de Compras", len(df))
            with col2:
                st.metric("Gasto Total", f"R$ {df['valor_real'].sum():.2f}")
            with col3:
                economia = df['diferenca'].sum()
                label = "Economia Total" if economia < 0 else "Gasto Extra"
                st.metric(label, f"R$ {abs(economia):.2f}")
            with col4:
                st.metric("Média/Compra", f"R$ {df['valor_real'].mean():.2f}")

            st.markdown("---")

            # Gráficos
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### 👥 Gastos por Cuidadora")
                gastos_cuidadora = df.groupby('cuidadora')['valor_real'].sum().reset_index()
                fig = px.bar(
                    gastos_cuidadora,
                    x='cuidadora',
                    y='valor_real',
                    title='Total Gasto por Cuidadora',
                    color='valor_real',
                    color_continuous_scale='Blues'
                )
                fig.update_layout(showlegend=False, xaxis_title="Cuidadora", yaxis_title="Gasto (R$)")
                st.plotly_chart(fig, use_container_width=True)

            with col2:
                st.markdown("### 📊 Estimado vs Real")
                comparacao = df.groupby('cuidadora').agg({
                    'valor_estimado': 'sum',
                    'valor_real': 'sum'
                }).reset_index()

                fig = go.Figure(data=[
                    go.Bar(name='Estimado', x=comparacao['cuidadora'], y=comparacao['valor_estimado']),
                    go.Bar(name='Real', x=comparacao['cuidadora'], y=comparacao['valor_real'])
                ])
                fig.update_layout(barmode='group', xaxis_title="Cuidadora", yaxis_title="Valor (R$)")
                st.plotly_chart(fig, use_container_width=True)

            st.markdown("---")

            # Evolução temporal
            st.markdown("### 📈 Evolução de Gastos no Tempo")
            gastos_dia = df.groupby('dia').agg({
                'valor_real': 'sum',
                'valor_estimado': 'sum'
            }).reset_index()

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=gastos_dia['dia'], y=gastos_dia['valor_estimado'],
                                    mode='lines+markers', name='Estimado'))
            fig.add_trace(go.Scatter(x=gastos_dia['dia'], y=gastos_dia['valor_real'],
                                    mode='lines+markers', name='Real'))
            fig.update_layout(xaxis_title="Data", yaxis_title="Gasto (R$)")
            st.plotly_chart(fig, use_container_width=True)

            # Análise por categoria
            st.markdown("---")
            st.markdown("### 📁 Análise por Categoria")

            # Extrair categorias de todos os itens
            todas_categorias = []
            for _, compra in df.iterrows():
                for item in compra['itens']:
                    todas_categorias.append({
                        'categoria': item['categoria'],
                        'valor': item['quantidade'] * item['preco_estimado']
                    })

            df_categorias = pd.DataFrame(todas_categorias)
            gastos_categoria = df_categorias.groupby('categoria')['valor'].sum().reset_index()

            col1, col2 = st.columns(2)

            with col1:
                fig = px.pie(
                    gastos_categoria,
                    values='valor',
                    names='categoria',
                    title='Distribuição de Gastos por Categoria'
                )
                st.plotly_chart(fig, use_container_width=True)

            with col2:
                fig = px.bar(
                    gastos_categoria.sort_values('valor', ascending=False),
                    x='categoria',
                    y='valor',
                    title='Gastos por Categoria',
                    color='valor',
                    color_continuous_scale='Greens'
                )
                fig.update_layout(showlegend=False)
                st.plotly_chart(fig, use_container_width=True)

            # Resumo mensal
            st.markdown("---")
            st.markdown("### 📅 Resumo Mensal")

            resumo_mensal = df.groupby('mes').agg({
                'valor_real': 'sum',
                'valor_estimado': 'sum',
                'id': 'count',
                'diferenca': 'sum'
            }).reset_index()

            resumo_mensal.columns = ['Mês', 'Gasto Real (R$)', 'Estimado (R$)', 'Nº Compras', 'Diferença (R$)']
            resumo_mensal['Gasto Real (R$)'] = resumo_mensal['Gasto Real (R$)'].apply(lambda x: f"R$ {x:.2f}")
            resumo_mensal['Estimado (R$)'] = resumo_mensal['Estimado (R$)'].apply(lambda x: f"R$ {x:.2f}")
            resumo_mensal['Diferença (R$)'] = resumo_mensal['Diferença (R$)'].apply(lambda x: f"R$ {x:.2f}")

            st.dataframe(resumo_mensal, use_container_width=True, hide_index=True)

            # Top itens mais comprados
            st.markdown("---")
            st.markdown("### 🏆 Itens Mais Comprados")

            todos_itens = []
            for _, compra in df.iterrows():
                for item in compra['itens']:
                    todos_itens.append({
                        'item': item['item'],
                        'categoria': item['categoria'],
                        'quantidade': item['quantidade'],
                        'valor_total': item['quantidade'] * item['preco_estimado']
                    })

            df_itens = pd.DataFrame(todos_itens)
            top_itens = df_itens.groupby('item').agg({
                'quantidade': 'sum',
                'valor_total': 'sum'
            }).reset_index().sort_values('valor_total', ascending=False).head(10)

            top_itens.columns = ['Item', 'Quantidade Total', 'Valor Total (R$)']
            top_itens['Valor Total (R$)'] = top_itens['Valor Total (R$)'].apply(lambda x: f"R$ {x:.2f}")

            st.dataframe(top_itens, use_container_width=True, hide_index=True)

# Rodapé
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>Sistema de Controle de Compras Familiar - Desenvolvido com ❤️ usando Streamlit</div>",
    unsafe_allow_html=True
)
