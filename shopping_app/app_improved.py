import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go

# Configuração da página
st.set_page_config(
    page_title="🛒 Controle de Compras da Família",
    page_icon="🧺",
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

# Estilos CSS
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
.stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>select {
    font-size: 18px;
    padding: 8px;
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
</style>
""", unsafe_allow_html=True)

# Caminhos de arquivos
DATA_DIR = "shopping_app/data"
LISTAS_FILE = os.path.join(DATA_DIR, "listas_familia.json")
COMPRAS_FILE = os.path.join(DATA_DIR, "compras_realizadas.json")
RESPONSAVEIS_FILE = os.path.join(DATA_DIR, "responsaveis.json")

# === FUNÇÕES DE PERSISTÊNCIA ===

def carregar_listas():
    """Carrega listas do JSON"""
    if os.path.exists(LISTAS_FILE):
        with open(LISTAS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar_listas(listas):
    """Salva listas no JSON"""
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(LISTAS_FILE, 'w', encoding='utf-8') as f:
        json.dump(listas, f, ensure_ascii=False, indent=2)

def carregar_compras():
    """Carrega compras realizadas do JSON"""
    if os.path.exists(COMPRAS_FILE):
        with open(COMPRAS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar_compras(compras):
    """Salva compras no JSON"""
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(COMPRAS_FILE, 'w', encoding='utf-8') as f:
        json.dump(compras, f, ensure_ascii=False, indent=2)

def carregar_responsaveis():
    """Carrega lista de responsáveis"""
    if os.path.exists(RESPONSAVEIS_FILE):
        with open(RESPONSAVEIS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return ["Cuidadora Ana", "Cuidadora Maria", "Filho(a) João", "Filho(a) Paula", "Vizinho(a)", "Outro"]

def salvar_responsaveis(responsaveis):
    """Salva lista de responsáveis"""
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(RESPONSAVEIS_FILE, 'w', encoding='utf-8') as f:
        json.dump(responsaveis, f, ensure_ascii=False, indent=2)

def adicionar_item_lista(item, quantidade, preco, responsavel, categoria="Geral"):
    """Adiciona item à lista atual"""
    listas = carregar_listas()

    # Procura lista ativa (Pendente)
    lista_ativa = next((l for l in listas if l['status'] == 'Pendente'), None)

    if not lista_ativa:
        # Cria nova lista
        lista_ativa = {
            "id": len(listas) + 1,
            "data_criacao": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "Pendente",
            "itens": [],
            "total_estimado": 0
        }
        listas.append(lista_ativa)

    # Adiciona item
    novo_item = {
        "item": item,
        "quantidade": quantidade,
        "preco": preco,
        "responsavel": responsavel,
        "categoria": categoria,
        "status": "Falta comprar",
        "total": quantidade * preco
    }

    lista_ativa['itens'].append(novo_item)
    lista_ativa['total_estimado'] = sum(i['total'] for i in lista_ativa['itens'])

    salvar_listas(listas)
    return True

def obter_lista_ativa():
    """Retorna a lista ativa (Pendente) ou cria uma nova"""
    listas = carregar_listas()
    lista_ativa = next((l for l in listas if l['status'] == 'Pendente'), None)

    if not lista_ativa:
        return {"itens": [], "total_estimado": 0}

    return lista_ativa

def atualizar_status_item(lista_id, item_index, novo_status):
    """Atualiza status de um item específico"""
    listas = carregar_listas()
    for lista in listas:
        if lista['id'] == lista_id:
            if 0 <= item_index < len(lista['itens']):
                lista['itens'][item_index]['status'] = novo_status
                salvar_listas(listas)
                return True
    return False

def finalizar_compras(lista_id, valor_real, observacoes=""):
    """Finaliza a lista de compras e move para histórico"""
    listas = carregar_listas()
    compras = carregar_compras()

    for lista in listas:
        if lista['id'] == lista_id:
            lista['status'] = "Finalizada"
            lista['data_finalizacao'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            lista['valor_real'] = valor_real
            lista['observacoes'] = observacoes

            # Adiciona ao histórico
            compras.append(lista.copy())

            salvar_listas(listas)
            salvar_compras(compras)
            return True

    return False

def limpar_lista_ativa():
    """Remove a lista ativa"""
    listas = carregar_listas()
    listas = [l for l in listas if l['status'] != 'Pendente']
    salvar_listas(listas)

# === INICIALIZAÇÃO ===

if 'pagina' not in st.session_state:
    st.session_state.pagina = "Lista Atual"

if 'perfil' not in st.session_state:
    st.session_state.perfil = "Família"

# === CABEÇALHO ===

col_header1, col_header2 = st.columns([4, 1])

with col_header1:
    st.title("🛒 Controle de Compras da Família")
    st.write("Organize as compras do idoso junto com a família e as cuidadoras. Tudo no mesmo lugar 💛")

with col_header2:
    perfil = st.selectbox(
        "👤 Perfil:",
        ["Família", "Cuidadora"],
        key='perfil'
    )

st.markdown("---")

# === MENU DE NAVEGAÇÃO ===

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("🛒 Lista Atual", use_container_width=True):
        st.session_state.pagina = "Lista Atual"

with col2:
    if st.button("📋 Histórico", use_container_width=True):
        st.session_state.pagina = "Histórico"

with col3:
    if st.button("📊 Relatórios", use_container_width=True):
        st.session_state.pagina = "Relatórios"

with col4:
    if st.button("👥 Responsáveis", use_container_width=True):
        st.session_state.pagina = "Responsáveis"

with col5:
    if st.button("ℹ️ Ajuda", use_container_width=True):
        st.session_state.pagina = "Ajuda"

st.markdown("---")

# === PÁGINA: LISTA ATUAL ===

if st.session_state.pagina == "Lista Atual":

    st.subheader("🛒 Lista de Compras Atual")

    # Adicionar novo item
    with st.expander("➕ Adicionar novo item", expanded=True):
        col1, col2, col3 = st.columns(3)

        with col1:
            item = st.text_input("🧺 Nome do item", key="novo_item")

        with col2:
            qtd = st.number_input("🔢 Quantidade", min_value=1, value=1, key="nova_qtd")

        with col3:
            preco = st.number_input("💰 Preço unitário (R$)", min_value=0.0, step=0.5, key="novo_preco")

        col4, col5 = st.columns(2)

        with col4:
            responsaveis = carregar_responsaveis()
            responsavel = st.selectbox("👩‍👩‍👧 Quem vai comprar?", responsaveis, key="novo_resp")

        with col5:
            categoria = st.selectbox(
                "📁 Categoria",
                ["Alimentação", "Medicamentos", "Higiene", "Limpeza", "Outros"],
                key="nova_cat"
            )

        if st.button("✅ Adicionar à lista", use_container_width=True, type="primary"):
            if item:
                adicionar_item_lista(item, qtd, preco, responsavel, categoria)
                st.success(f"✅ {item} adicionado à lista!")
                st.rerun()
            else:
                st.warning("⚠️ Digite o nome do item antes de adicionar.")

    st.markdown("---")

    # Exibir lista atual
    lista_ativa = obter_lista_ativa()

    if lista_ativa['itens']:
        st.subheader("📝 Itens na lista:")

        # Criar DataFrame para exibição
        df = pd.DataFrame(lista_ativa['itens'])
        df['Total'] = df['quantidade'] * df['preco']

        # Exibir tabela
        st.dataframe(
            df[['item', 'quantidade', 'preco', 'responsavel', 'categoria', 'status', 'Total']].rename(columns={
                'item': 'Item',
                'quantidade': 'Qtd',
                'preco': 'Preço (R$)',
                'responsavel': 'Responsável',
                'categoria': 'Categoria',
                'status': 'Status'
            }),
            use_container_width=True,
            hide_index=True
        )

        # Resumo
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("📦 Total de itens", len(df))

        with col2:
            faltam = len(df[df['status'] == 'Falta comprar'])
            st.metric("🟡 Faltam comprar", faltam)

        with col3:
            comprados = len(df[df['status'] == 'Já comprei'])
            st.metric("✅ Já comprados", comprados)

        with col4:
            st.metric("💰 Total estimado", f"R$ {lista_ativa['total_estimado']:.2f}")

        st.markdown("---")

        # Atualizar status dos itens
        st.subheader("📦 Atualizar status dos itens")

        for idx, item_data in enumerate(lista_ativa['itens']):
            col1, col2, col3 = st.columns([3, 2, 1])

            with col1:
                st.write(f"**{item_data['item']}** - {item_data['quantidade']}x - R$ {item_data['total']:.2f}")

            with col2:
                status_atual = item_data['status']
                novo_status = st.selectbox(
                    "Status",
                    ["Falta comprar", "Já comprei"],
                    index=0 if status_atual == "Falta comprar" else 1,
                    key=f"status_{idx}",
                    label_visibility="collapsed"
                )

                if novo_status != status_atual:
                    atualizar_status_item(lista_ativa['id'], idx, novo_status)
                    st.rerun()

            with col3:
                st.write(f"👤 {item_data['responsavel']}")

        st.markdown("---")

        # Ações
        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("🧹 Limpar lista", use_container_width=True):
                limpar_lista_ativa()
                st.success("Lista limpa com sucesso! 🧽")
                st.rerun()

        with col2:
            valor_real = st.number_input(
                "💵 Valor real gasto (R$)",
                min_value=0.0,
                value=float(lista_ativa['total_estimado']),
                step=0.5,
                key="valor_real"
            )

        with col3:
            if st.button("✅ Finalizar compras", use_container_width=True, type="primary"):
                observacoes = st.text_input("Observações (opcional)", key="obs_final")
                if finalizar_compras(lista_ativa['id'], valor_real, observacoes):
                    st.success("🎉 Compras finalizadas e salvas no histórico!")
                    st.balloons()
                    st.rerun()

    else:
        st.info("📭 Lista vazia. Adicione itens usando o formulário acima!")

# === PÁGINA: HISTÓRICO ===

elif st.session_state.pagina == "Histórico":

    st.subheader("📋 Histórico de Compras")

    compras = carregar_compras()

    if not compras:
        st.info("📭 Ainda não há compras finalizadas no histórico.")
    else:
        # Filtros
        col1, col2, col3 = st.columns(3)

        with col1:
            df_compras = pd.DataFrame(compras)
            if 'data_finalizacao' in df_compras.columns:
                df_compras['data_finalizacao'] = pd.to_datetime(df_compras['data_finalizacao'])

            periodo = st.selectbox(
                "📅 Período",
                ["Últimos 7 dias", "Últimos 30 dias", "Últimos 90 dias", "Todos"]
            )

        with col2:
            # Extrair responsáveis únicos
            todos_resp = set()
            for compra in compras:
                for item in compra.get('itens', []):
                    todos_resp.add(item.get('responsavel', 'Não informado'))

            filtro_resp = st.selectbox(
                "👤 Responsável",
                ["Todos"] + sorted(list(todos_resp))
            )

        with col3:
            ordem = st.selectbox(
                "🔄 Ordenar por",
                ["Mais recentes", "Mais antigas", "Maior valor", "Menor valor"]
            )

        # Aplicar filtros
        compras_filtradas = compras.copy()

        # Filtro de período
        if periodo != "Todos" and 'data_finalizacao' in df_compras.columns:
            dias = {"Últimos 7 dias": 7, "Últimos 30 dias": 30, "Últimos 90 dias": 90}[periodo]
            data_limite = datetime.now() - timedelta(days=dias)
            compras_filtradas = [
                c for c in compras_filtradas
                if datetime.strptime(c['data_finalizacao'], "%Y-%m-%d %H:%M:%S") >= data_limite
            ]

        # Filtro de responsável
        if filtro_resp != "Todos":
            compras_filtradas = [
                c for c in compras_filtradas
                if any(item.get('responsavel') == filtro_resp for item in c.get('itens', []))
            ]

        # Ordenar
        if ordem == "Mais recentes":
            compras_filtradas.sort(key=lambda x: x.get('data_finalizacao', ''), reverse=True)
        elif ordem == "Mais antigas":
            compras_filtradas.sort(key=lambda x: x.get('data_finalizacao', ''))
        elif ordem == "Maior valor":
            compras_filtradas.sort(key=lambda x: x.get('valor_real', 0), reverse=True)
        else:
            compras_filtradas.sort(key=lambda x: x.get('valor_real', 0))

        st.markdown("---")

        # Exibir compras
        for compra in compras_filtradas:
            with st.expander(
                f"🛍️ Compra #{compra['id']} - {compra.get('data_finalizacao', '')[:10]} - R$ {compra.get('valor_real', 0):.2f}"
            ):
                col1, col2 = st.columns(2)

                with col1:
                    st.markdown(f"**📅 Data:** {compra.get('data_finalizacao', 'N/A')}")
                    st.markdown(f"**📦 Itens:** {len(compra.get('itens', []))}")

                with col2:
                    st.markdown(f"**💰 Estimado:** R$ {compra.get('total_estimado', 0):.2f}")
                    st.markdown(f"**💵 Real:** R$ {compra.get('valor_real', 0):.2f}")
                    diferenca = compra.get('valor_real', 0) - compra.get('total_estimado', 0)
                    cor = "🔴" if diferenca > 0 else "🟢"
                    st.markdown(f"**📊 Diferença:** {cor} R$ {diferenca:.2f}")

                if compra.get('observacoes'):
                    st.info(f"📝 {compra['observacoes']}")

                # Tabela de itens
                if compra.get('itens'):
                    df_itens = pd.DataFrame(compra['itens'])
                    st.dataframe(
                        df_itens[['item', 'quantidade', 'preco', 'responsavel', 'categoria', 'total']].rename(columns={
                            'item': 'Item',
                            'quantidade': 'Qtd',
                            'preco': 'Preço',
                            'responsavel': 'Responsável',
                            'categoria': 'Categoria',
                            'total': 'Total'
                        }),
                        use_container_width=True,
                        hide_index=True
                    )

# === PÁGINA: RELATÓRIOS ===

elif st.session_state.pagina == "Relatórios":

    st.subheader("📊 Relatórios da Família")

    compras = carregar_compras()

    if not compras:
        st.info("📭 Ainda não há dados suficientes para gerar relatórios. Finalize pelo menos uma compra!")
    else:
        # Extrair todos os itens
        todos_itens = []
        for compra in compras:
            for item in compra.get('itens', []):
                item_copy = item.copy()
                item_copy['data_compra'] = compra.get('data_finalizacao', '')
                item_copy['compra_id'] = compra.get('id')
                todos_itens.append(item_copy)

        df = pd.DataFrame(todos_itens)

        if not df.empty:
            # Métricas principais
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("🛒 Total de compras", len(compras))

            with col2:
                total_gasto = sum(c.get('valor_real', 0) for c in compras)
                st.metric("💰 Total gasto", f"R$ {total_gasto:.2f}")

            with col3:
                media = total_gasto / len(compras) if compras else 0
                st.metric("📊 Média por compra", f"R$ {media:.2f}")

            with col4:
                total_itens = len(df)
                st.metric("📦 Total de itens", total_itens)

            st.markdown("---")

            # Gráficos
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### 👥 Gastos por Responsável")
                gastos_resp = df.groupby('responsavel')['total'].sum().reset_index()
                gastos_resp = gastos_resp.sort_values('total', ascending=False)

                fig = px.bar(
                    gastos_resp,
                    x='responsavel',
                    y='total',
                    title='',
                    labels={'responsavel': 'Responsável', 'total': 'Gasto (R$)'},
                    color='total',
                    color_continuous_scale='Teal'
                )
                st.plotly_chart(fig, use_container_width=True)

            with col2:
                st.markdown("### 📁 Gastos por Categoria")
                gastos_cat = df.groupby('categoria')['total'].sum().reset_index()

                fig = px.pie(
                    gastos_cat,
                    values='total',
                    names='categoria',
                    title=''
                )
                st.plotly_chart(fig, use_container_width=True)

            st.markdown("---")

            # Evolução temporal
            st.markdown("### 📈 Evolução de Gastos")

            df_tempo = pd.DataFrame(compras)
            if 'data_finalizacao' in df_tempo.columns:
                df_tempo['data_finalizacao'] = pd.to_datetime(df_tempo['data_finalizacao'])
                df_tempo['data'] = df_tempo['data_finalizacao'].dt.date
                gastos_dia = df_tempo.groupby('data')['valor_real'].sum().reset_index()

                fig = px.line(
                    gastos_dia,
                    x='data',
                    y='valor_real',
                    title='',
                    labels={'data': 'Data', 'valor_real': 'Gasto (R$)'},
                    markers=True
                )
                st.plotly_chart(fig, use_container_width=True)

            st.markdown("---")

            # Top 10 itens
            st.markdown("### 🏆 Top 10 Itens Mais Comprados")

            top_itens = df.groupby('item').agg({
                'quantidade': 'sum',
                'total': 'sum'
            }).reset_index().sort_values('total', ascending=False).head(10)

            top_itens_display = top_itens.rename(columns={
                'item': 'Item',
                'quantidade': 'Quantidade Total',
                'total': 'Valor Total (R$)'
            })

            st.dataframe(top_itens_display, use_container_width=True, hide_index=True)

            st.markdown("---")

            # Resumo para divisão
            st.markdown("### 💰 Resumo para Divisão de Gastos")

            col1, col2 = st.columns(2)

            with col1:
                st.write("**Gastos por Responsável:**")
                resumo_resp = df.groupby('responsavel')['total'].sum().reset_index()
                resumo_resp['total'] = resumo_resp['total'].apply(lambda x: f"R$ {x:.2f}")
                st.dataframe(resumo_resp.rename(columns={'responsavel': 'Responsável', 'total': 'Total Gasto'}), hide_index=True)

            with col2:
                num_filhos = st.number_input("Número de filhos para dividir:", min_value=1, value=2)
                valor_por_filho = total_gasto / num_filhos

                st.write(f"**Total gasto:** R$ {total_gasto:.2f}")
                st.write(f"**Dividindo por {num_filhos} filhos:**")
                st.success(f"### Cada filho paga: R$ {valor_por_filho:.2f}")

# === PÁGINA: RESPONSÁVEIS ===

elif st.session_state.pagina == "Responsáveis":

    st.subheader("👥 Gerenciar Responsáveis")

    responsaveis = carregar_responsaveis()

    st.write("### Lista de Responsáveis Cadastrados")

    for i, resp in enumerate(responsaveis):
        col1, col2 = st.columns([4, 1])

        with col1:
            st.markdown(f"**{i+1}.** {resp}")

        with col2:
            if st.button("🗑️", key=f"del_resp_{i}"):
                responsaveis.pop(i)
                salvar_responsaveis(responsaveis)
                st.success("Removido!")
                st.rerun()

    st.markdown("---")

    st.write("### Adicionar Novo Responsável")

    col1, col2 = st.columns([3, 1])

    with col1:
        novo_resp = st.text_input("Nome do responsável", placeholder="Ex: Cuidadora Clara")

    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("➕ Adicionar", use_container_width=True):
            if novo_resp and novo_resp not in responsaveis:
                responsaveis.append(novo_resp)
                salvar_responsaveis(responsaveis)
                st.success(f"✅ {novo_resp} adicionado!")
                st.rerun()
            elif novo_resp in responsaveis:
                st.warning("⚠️ Este responsável já está cadastrado!")
            else:
                st.error("⚠️ Digite um nome válido!")

# === PÁGINA: AJUDA ===

elif st.session_state.pagina == "Ajuda":

    st.subheader("ℹ️ Como Usar o App")

    st.markdown("""
    ### 🛒 Lista Atual
    - **Adicione itens** que precisam ser comprados
    - **Defina responsável** (cuidadora, filho, etc.)
    - **Marque status** (Falta comprar / Já comprei)
    - **Finalize** quando terminar as compras

    ### 📋 Histórico
    - Veja todas as compras anteriores
    - Filtre por período ou responsável
    - Compare valores estimados vs reais

    ### 📊 Relatórios
    - Veja gráficos de gastos
    - Gastos por pessoa e categoria
    - Top 10 itens mais comprados
    - **Divisão de gastos** entre filhos

    ### 👥 Responsáveis
    - Cadastre cuidadoras e familiares
    - Gerencie a lista de responsáveis

    ### 💾 Dados Salvos
    - Todos os dados ficam salvos automaticamente
    - Mesmo fechando o app, tudo fica guardado
    - Backup: copie a pasta `shopping_app/data/`

    ### 📱 Instalar no Celular
    - **Android:** Chrome → Menu → "Adicionar à tela inicial"
    - **iPhone:** Safari → Compartilhar → "Adicionar à Tela de Início"
    """)

    st.markdown("---")
    st.success("💛 App desenvolvido para facilitar o cuidado com idosos e organização familiar!")

# Rodapé
st.markdown("---")
st.caption("💛 Dica: esse app foi pensado para idosos, cuidadoras e filhos que dividem o cuidado. Pode instalar no celular (PWA) e usar toda semana.")
