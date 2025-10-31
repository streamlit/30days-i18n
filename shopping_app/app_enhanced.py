import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
from collections import defaultdict

# Configuração da página
st.set_page_config(
    page_title="Controle de Compras - Família",
    page_icon="🛒",
    layout="wide"
)

# Estilos CSS
st.markdown("""
    <style>
    .stButton>button {
        font-size: 18px;
        height: 3em;
        width: 100%;
    }
    .price-suggestion {
        background-color: #E7F3FF;
        padding: 8px;
        border-radius: 4px;
        border-left: 3px solid #2196F3;
        margin: 5px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Caminhos dos arquivos
DATA_DIR = "shopping_app/data"
LISTAS_FILE = os.path.join(DATA_DIR, "listas.json")
COMPRAS_FILE = os.path.join(DATA_DIR, "compras.json")
CUIDADORAS_FILE = os.path.join(DATA_DIR, "cuidadoras.json")
PRECOS_FILE = os.path.join(DATA_DIR, "historico_precos.json")

# Funções de dados
def carregar_listas():
    if os.path.exists(LISTAS_FILE):
        with open(LISTAS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar_listas(listas):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(LISTAS_FILE, 'w', encoding='utf-8') as f:
        json.dump(listas, f, ensure_ascii=False, indent=2)

def carregar_compras():
    if os.path.exists(COMPRAS_FILE):
        with open(COMPRAS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar_compras(compras):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(COMPRAS_FILE, 'w', encoding='utf-8') as f:
        json.dump(compras, f, ensure_ascii=False, indent=2)

def carregar_cuidadoras():
    if os.path.exists(CUIDADORAS_FILE):
        with open(CUIDADORAS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return ["Ana", "Maria", "João"]

def salvar_cuidadoras(cuidadoras):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(CUIDADORAS_FILE, 'w', encoding='utf-8') as f:
        json.dump(cuidadoras, f, ensure_ascii=False, indent=2)

def carregar_historico_precos():
    """Carrega histórico de preços dos produtos"""
    if os.path.exists(PRECOS_FILE):
        with open(PRECOS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def salvar_historico_precos(historico):
    """Salva histórico de preços"""
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(PRECOS_FILE, 'w', encoding='utf-8') as f:
        json.dump(historico, f, ensure_ascii=False, indent=2)

def atualizar_historico_precos(item_nome, preco, categoria):
    """Atualiza o histórico de preços com um novo preço"""
    historico = carregar_historico_precos()

    # Normalizar nome do item (minúsculas, sem espaços extras)
    item_key = item_nome.lower().strip()

    if item_key not in historico:
        historico[item_key] = {
            "nome_original": item_nome,
            "categoria": categoria,
            "precos": [],
            "ultimo_preco": preco,
            "preco_medio": preco
        }

    # Adicionar novo preço
    historico[item_key]["precos"].append({
        "preco": preco,
        "data": datetime.now().strftime("%Y-%m-%d")
    })

    # Manter apenas últimos 10 registros
    historico[item_key]["precos"] = historico[item_key]["precos"][-10:]

    # Calcular preço médio
    precos = [p["preco"] for p in historico[item_key]["precos"]]
    historico[item_key]["preco_medio"] = sum(precos) / len(precos)
    historico[item_key]["ultimo_preco"] = preco
    historico[item_key]["categoria"] = categoria

    salvar_historico_precos(historico)

def obter_preco_sugerido(item_nome):
    """Retorna o preço sugerido baseado no histórico"""
    historico = carregar_historico_precos()
    item_key = item_nome.lower().strip()

    if item_key in historico:
        return {
            "preco_medio": historico[item_key]["preco_medio"],
            "ultimo_preco": historico[item_key]["ultimo_preco"],
            "categoria_sugerida": historico[item_key]["categoria"],
            "tem_historico": True
        }

    # Buscar similar
    for key, data in historico.items():
        if item_key in key or key in item_key:
            return {
                "preco_medio": data["preco_medio"],
                "ultimo_preco": data["ultimo_preco"],
                "categoria_sugerida": data["categoria"],
                "tem_historico": True,
                "nome_similar": data["nome_original"]
            }

    return {"tem_historico": False}

def buscar_produtos_similares(termo):
    """Busca produtos similares no histórico"""
    historico = carregar_historico_precos()
    termo_lower = termo.lower().strip()

    resultados = []
    for key, data in historico.items():
        if termo_lower in key or any(palavra in key for palavra in termo_lower.split()):
            resultados.append({
                "nome": data["nome_original"],
                "preco_medio": data["preco_medio"],
                "ultimo_preco": data["ultimo_preco"],
                "categoria": data["categoria"]
            })

    return resultados[:5]  # Retorna até 5 resultados

def criar_lista(cuidadora, itens, observacoes="", imagem_pedido=None):
    listas = carregar_listas()
    lista = {
        "id": len(listas) + 1,
        "data_criacao": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cuidadora": cuidadora,
        "status": "Pendente",
        "itens": itens,
        "observacoes": observacoes,
        "valor_estimado": sum(item['preco_estimado'] * item['quantidade'] for item in itens),
        "valor_real": 0,
        "tem_imagem": imagem_pedido is not None
    }
    listas.append(lista)
    salvar_listas(listas)
    return lista['id']

def atualizar_status_lista(lista_id, novo_status, usuario="", valor_real=None):
    listas = carregar_listas()
    for lista in listas:
        if lista['id'] == lista_id:
            lista['status'] = novo_status
            if novo_status == "Aprovada":
                lista['data_aprovacao'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                lista['aprovada_por'] = usuario
            elif novo_status == "Comprada":
                lista['data_compra'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                if valor_real:
                    lista['valor_real'] = valor_real
            break
    salvar_listas(listas)

def atualizar_itens_lista(lista_id, novos_itens):
    listas = carregar_listas()
    for lista in listas:
        if lista['id'] == lista_id:
            lista['itens'] = novos_itens
            lista['valor_estimado'] = sum(item['preco_estimado'] * item['quantidade'] for item in novos_itens)
            break
    salvar_listas(listas)

def registrar_compra_realizada(lista_id, valor_total, observacoes_compra="", atualizar_precos=True):
    listas = carregar_listas()
    compras = carregar_compras()

    lista = next((l for l in listas if l['id'] == lista_id), None)
    if lista:
        # Atualizar histórico de preços se solicitado
        if atualizar_precos:
            for item in lista['itens']:
                atualizar_historico_precos(
                    item['item'],
                    item['preco_estimado'],
                    item['categoria']
                )

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

# Estado da sessão
if 'pagina' not in st.session_state:
    st.session_state.pagina = "Listas Pendentes"
if 'perfil' not in st.session_state:
    st.session_state.perfil = "Família"
if 'itens_lista' not in st.session_state:
    st.session_state.itens_lista = []
if 'modo_criacao' not in st.session_state:
    st.session_state.modo_criacao = "manual"  # "manual" ou "imagem"

# Interface
col1, col2 = st.columns([4, 1])
with col1:
    st.markdown("# 🛒 Controle de Compras Familiar")
    st.markdown("### Sistema com previsão de preços e upload de pedidos")

with col2:
    perfil = st.selectbox("👤 Perfil:", ["Família", "Cuidadora"], key='perfil')

st.markdown("---")

# Menu
if st.session_state.perfil == "Cuidadora":
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("➕ Nova Lista", use_container_width=True):
            st.session_state.pagina = "Nova Lista"
    with col2:
        if st.button("📋 Minhas Listas", use_container_width=True):
            st.session_state.pagina = "Minhas Listas"
    with col3:
        if st.button("📊 Catálogo de Preços", use_container_width=True):
            st.session_state.pagina = "Catalogo"
    with col4:
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

# PÁGINAS CUIDADORA
if st.session_state.perfil == "Cuidadora":

    if st.session_state.pagina == "Nova Lista":
        st.markdown("## ➕ Criar Nova Lista de Compras")

        cuidadoras = carregar_cuidadoras()
        cuidadora = st.selectbox("👤 Seu nome:", cuidadoras)

        # Escolher modo de criação
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📝 Modo Manual", use_container_width=True, type="secondary" if st.session_state.modo_criacao == "imagem" else "primary"):
                st.session_state.modo_criacao = "manual"
        with col2:
            if st.button("📸 Upload de Pedido", use_container_width=True, type="secondary" if st.session_state.modo_criacao == "manual" else "primary"):
                st.session_state.modo_criacao = "imagem"

        st.markdown("---")

        # MODO IMAGEM
        if st.session_state.modo_criacao == "imagem":
            st.markdown("### 📸 Upload do Print do Pedido")
            st.info("💡 **Dica**: Tire um print da tela do carrinho do Shopper/iFood e faça upload aqui. Depois preencha os itens manualmente baseado na imagem.")

            uploaded_file = st.file_uploader("Escolha a imagem do pedido", type=['png', 'jpg', 'jpeg'])

            if uploaded_file:
                col1, col2 = st.columns([1, 1])

                with col1:
                    st.markdown("#### 📱 Imagem do Pedido:")
                    st.image(uploaded_file, use_container_width=True)

                with col2:
                    st.markdown("#### ✍️ Preencha os itens baseado na imagem:")
                    st.markdown("Use o formulário abaixo para adicionar cada item que aparece na imagem")

        # FORMULÁRIO DE ITENS (comum para ambos os modos)
        st.markdown("### 🛍️ Itens da Lista")

        col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 1])

        with col1:
            novo_item = st.text_input("Item", placeholder="Digite o nome do produto", key="novo_item")

            # Mostrar sugestões se houver
            if novo_item and len(novo_item) >= 3:
                sugestoes = buscar_produtos_similares(novo_item)
                if sugestoes:
                    st.markdown('<div class="price-suggestion">', unsafe_allow_html=True)
                    st.markdown("**💡 Produtos similares encontrados:**")
                    for sug in sugestoes:
                        st.markdown(f"• {sug['nome']} - R$ {sug['ultimo_preco']:.2f} (média: R$ {sug['preco_medio']:.2f})")
                    st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            # Sugerir categoria baseada no histórico
            preco_info = obter_preco_sugerido(novo_item) if novo_item else {"tem_historico": False}
            categorias = ["Alimentação", "Medicamentos", "Higiene", "Limpeza", "Outros"]

            if preco_info.get("tem_historico") and preco_info.get("categoria_sugerida"):
                try:
                    idx_default = categorias.index(preco_info["categoria_sugerida"])
                except:
                    idx_default = 0
            else:
                idx_default = 0

            categoria = st.selectbox("Categoria", categorias, key="nova_categoria", index=idx_default)

        with col3:
            quantidade = st.number_input("Qtd", min_value=1, value=1, key="nova_qtd")

        with col4:
            # Sugerir preço baseado no histórico
            if preco_info.get("tem_historico"):
                preco_sugerido = preco_info["ultimo_preco"]
                st.caption(f"Último: R$ {preco_info['ultimo_preco']:.2f}")
            else:
                preco_sugerido = 0.0

            preco_est = st.number_input("Preço (R$)", min_value=0.0, value=float(preco_sugerido), format="%.2f", key="novo_preco")

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

            observacoes = st.text_area("📝 Observações", placeholder="Observações sobre os produtos...")

            st.markdown("---")
            col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                if st.button("📤 ENVIAR PARA APROVAÇÃO", use_container_width=True, type="primary"):
                    lista_id = criar_lista(cuidadora, st.session_state.itens_lista, observacoes)
                    st.success(f"✅ Lista #{lista_id} enviada!")
                    st.session_state.itens_lista = []
                    st.balloons()
                    st.rerun()

    elif st.session_state.pagina == "Catalogo":
        st.markdown("## 📊 Catálogo de Preços")

        historico = carregar_historico_precos()

        if not historico:
            st.info("📭 Ainda não há produtos no catálogo. Os preços serão salvos automaticamente após as compras.")
        else:
            st.markdown(f"### Total de produtos cadastrados: {len(historico)}")

            # Filtros
            col1, col2 = st.columns(2)
            with col1:
                categorias_disponiveis = list(set([p["categoria"] for p in historico.values()]))
                filtro_cat = st.selectbox("Filtrar por categoria:", ["Todas"] + sorted(categorias_disponiveis))

            with col2:
                busca = st.text_input("🔍 Buscar produto:", placeholder="Digite para buscar...")

            # Criar DataFrame
            dados_catalogo = []
            for key, data in historico.items():
                if filtro_cat != "Todas" and data["categoria"] != filtro_cat:
                    continue
                if busca and busca.lower() not in data["nome_original"].lower():
                    continue

                dados_catalogo.append({
                    "Produto": data["nome_original"],
                    "Categoria": data["categoria"],
                    "Último Preço": f"R$ {data['ultimo_preco']:.2f}",
                    "Preço Médio": f"R$ {data['preco_medio']:.2f}",
                    "Nº Registros": len(data["precos"])
                })

            if dados_catalogo:
                df_catalogo = pd.DataFrame(dados_catalogo)
                st.dataframe(df_catalogo, use_container_width=True, hide_index=True)
            else:
                st.info("Nenhum produto encontrado com os filtros selecionados.")

    # Outras páginas da cuidadora (Minhas Listas, Cuidadoras) - mantém código anterior
    elif st.session_state.pagina == "Minhas Listas":
        st.markdown("## 📋 Minhas Listas de Compras")
        listas = carregar_listas()
        if not listas:
            st.info("📭 Você ainda não criou nenhuma lista.")
        else:
            for lista in sorted(listas, key=lambda x: x['data_criacao'], reverse=True):
                with st.expander(f"📋 Lista #{lista['id']} - {lista['cuidadora']} - {lista['status']} - R$ {lista['valor_estimado']:.2f}"):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**👤 Cuidadora:** {lista['cuidadora']}")
                        st.markdown(f"**📅 Criada:** {lista['data_criacao']}")
                        st.markdown(f"**📊 Status:** {lista['status']}")
                    with col2:
                        st.markdown(f"**💰 Estimado:** R$ {lista['valor_estimado']:.2f}")
                        if lista['status'] == 'Comprada':
                            st.markdown(f"**💵 Real:** R$ {lista.get('valor_real', 0):.2f}")

                    df_itens = pd.DataFrame(lista['itens'])
                    df_itens['total'] = df_itens['quantidade'] * df_itens['preco_estimado']
                    st.dataframe(df_itens, use_container_width=True, hide_index=True)

# PÁGINAS FAMÍLIA (mantém código anterior com pequenas melhorias)
else:
    if st.session_state.pagina == "Listas Pendentes":
        st.markdown("## ⏳ Listas Pendentes")
        listas = carregar_listas()
        listas_pendentes = [l for l in listas if l['status'] == 'Pendente']

        if not listas_pendentes:
            st.success("✅ Não há listas pendentes!")
        else:
            for lista in sorted(listas_pendentes, key=lambda x: x['data_criacao'], reverse=True):
                with st.expander(f"📋 Lista #{lista['id']} - {lista['cuidadora']} - R$ {lista['valor_estimado']:.2f}", expanded=True):
                    col1, col2 = st.columns([2, 1])
                    with col1:
                        st.markdown(f"**👤 Solicitada por:** {lista['cuidadora']}")
                        st.markdown(f"**📅 Data:** {lista['data_criacao']}")
                    with col2:
                        st.markdown(f"### 💰 R$ {lista['valor_estimado']:.2f}")

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

                    total = sum(item['quantidade'] * item['preco_estimado'] for item in itens_editados)
                    st.markdown(f"### 💰 Total: R$ {total:.2f}")

                    st.markdown("---")
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        if st.button("💾 Salvar", key=f"save_{lista['id']}", use_container_width=True):
                            atualizar_itens_lista(lista['id'], itens_editados)
                            st.success("✅ Atualizado!")
                            st.rerun()
                    with col2:
                        nome = st.text_input("Seu nome", key=f"nome_{lista['id']}", placeholder="Nome", label_visibility="collapsed")
                    with col3:
                        if st.button("✅ Aprovar", key=f"apr_{lista['id']}", use_container_width=True, type="primary"):
                            if nome:
                                atualizar_status_lista(lista['id'], "Aprovada", nome)
                                st.success("✅ Aprovada!")
                                st.rerun()
                    with col4:
                        if st.button("❌ Rejeitar", key=f"rej_{lista['id']}", use_container_width=True):
                            if nome:
                                atualizar_status_lista(lista['id'], "Rejeitada", nome)
                                st.rerun()

    elif st.session_state.pagina == "Listas Aprovadas":
        st.markdown("## ✅ Listas Aprovadas - Pronto para Comprar")
        listas = carregar_listas()
        listas_aprovadas = [l for l in listas if l['status'] == 'Aprovada']

        if not listas_aprovadas:
            st.info("📭 Não há listas aguardando compra.")
        else:
            for lista in sorted(listas_aprovadas, key=lambda x: x.get('data_aprovacao', ''), reverse=True):
                with st.expander(f"📋 Lista #{lista['id']} - {lista['cuidadora']} - R$ {lista['valor_estimado']:.2f}", expanded=True):
                    st.markdown(f"**👤 Solicitada por:** {lista['cuidadora']}")
                    st.markdown(f"**💰 Valor Estimado:** R$ {lista['valor_estimado']:.2f}")

                    df_itens = pd.DataFrame(lista['itens'])
                    df_itens['total'] = df_itens['quantidade'] * df_itens['preco_estimado']
                    st.dataframe(df_itens[['item', 'categoria', 'quantidade', 'preco_estimado', 'total']], use_container_width=True, hide_index=True)

                    st.markdown("---")
                    st.markdown("### 💳 Registrar Compra")

                    col1, col2, col3 = st.columns([2, 2, 1])
                    with col1:
                        valor_real = st.number_input("Valor pago (R$)", min_value=0.0, value=lista['valor_estimado'],
                                                    format="%.2f", key=f"val_{lista['id']}")
                    with col2:
                        obs = st.text_input("Observações", placeholder="Trocas, etc...", key=f"obs_{lista['id']}")
                    with col3:
                        st.markdown("<br>", unsafe_allow_html=True)
                        if st.button("✅ Confirmar", key=f"conf_{lista['id']}", use_container_width=True):
                            registrar_compra_realizada(lista['id'], valor_real, obs, atualizar_precos=True)
                            st.success("✅ Compra registrada! Preços atualizados no catálogo.")
                            st.balloons()
                            st.rerun()

                    diferenca = valor_real - lista['valor_estimado']
                    if diferenca > 0:
                        st.warning(f"⚠️ R$ {abs(diferenca):.2f} a mais que o estimado")
                    elif diferenca < 0:
                        st.success(f"✅ Economia de R$ {abs(diferenca):.2f}")

st.markdown("---")
st.markdown("<div style='text-align: center; color: gray;'>Sistema de Controle de Compras Familiar com Previsão de Preços</div>", unsafe_allow_html=True)
