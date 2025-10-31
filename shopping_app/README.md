# 🛒 Sistema de Controle de Compras Familiar

## 📋 Contexto

Sistema desenvolvido para famílias que precisam controlar compras de uma casa onde mora uma idosa acamada com cuidadoras que revezam a cada 24 horas.

### Situação Atendida:
- **Idosa acamada** mora na residência
- **Cuidadoras** revezam a cada 24 horas
- **Cuidadoras se alimentam na casa** (compras incluem alimentação delas)
- **Família não tem controle** sobre o que está sendo solicitado e comprado
- **Compras via delivery** (ex: Shopper, iFood Mercado, etc.)

### Problema Resolvido:
✅ Transparência total sobre o que está sendo pedido
✅ Aprovação prévia antes de comprar
✅ Controle de gastos por cuidadora
✅ Comparação entre valores estimados e reais
✅ Histórico completo para auditoria
✅ Identificação de padrões de consumo

## ✨ Funcionalidades

### 👥 Dois Perfis de Acesso

#### 🟦 Perfil CUIDADORA
1. **Criar Listas de Compras**
   - Adicionar itens necessários (comida, medicamentos, higiene, etc.)
   - Estimar preços
   - Categorizar produtos
   - Adicionar observações
   - Enviar para aprovação da família

2. **Visualizar Minhas Listas**
   - Ver status (Pendente, Aprovada, Comprada, Rejeitada)
   - Acompanhar valores
   - Ver histórico de listas criadas

#### 🟩 Perfil FAMÍLIA
1. **Aprovar/Rejeitar Listas**
   - Visualizar listas pendentes
   - Editar itens e quantidades
   - Aprovar ou rejeitar
   - Rastrear quem aprovou

2. **Comprar e Registrar**
   - Ver listas aprovadas prontas para compra
   - Comprar via app de delivery
   - Registrar valor real pago
   - Comparar com estimativa

3. **Histórico Completo**
   - Ver todas as compras realizadas
   - Filtrar por cuidadora
   - Filtrar por período
   - Ver diferenças entre estimado vs real

4. **Relatórios e Análises**
   - Gastos por cuidadora
   - Gastos por categoria
   - Evolução temporal
   - Resumo mensal
   - Itens mais comprados

## 🔄 Fluxo de Trabalho

```
1. CUIDADORA → Cria lista de compras
                ↓
2. CUIDADORA → Envia para aprovação
                ↓
3. FAMÍLIA → Recebe notificação de lista pendente
                ↓
4. FAMÍLIA → Revisa, edita se necessário
                ↓
5. FAMÍLIA → Aprova ou Rejeita
                ↓
6. FAMÍLIA → Compra via Shopper (se aprovada)
                ↓
7. FAMÍLIA → Registra valor real pago
                ↓
8. SISTEMA → Armazena no histórico para auditoria
```

## 🚀 Como Usar

### Instalação

1. Certifique-se de ter Python 3.7+ instalado
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Executar o Aplicativo

No diretório raiz do projeto:

```bash
streamlit run shopping_app/app.py
```

O aplicativo abrirá em `http://localhost:8501`

## 📱 Guia de Uso

### Para CUIDADORAS:

#### 1. Criar uma Nova Lista
1. Selecione "Cuidadora" no perfil (canto superior direito)
2. Clique em "➕ Nova Lista"
3. Selecione seu nome
4. Adicione os itens necessários:
   - Digite o nome do produto
   - Escolha a categoria
   - Informe quantidade
   - Estime o preço (pode deixar R$ 0,00 se não souber)
5. Adicione observações se necessário (ex: "Leite sem lactose", "Pão integral")
6. Clique em "📤 ENVIAR LISTA PARA APROVAÇÃO"

#### 2. Acompanhar Suas Listas
1. Clique em "📋 Minhas Listas"
2. Veja o status de cada lista:
   - ⏳ **Pendente**: Aguardando aprovação
   - ✅ **Aprovada**: Família vai comprar
   - 🛍️ **Comprada**: Já foi comprada
   - ❌ **Rejeitada**: Não foi aprovada

### Para FAMÍLIA:

#### 1. Aprovar Listas Pendentes
1. Selecione "Família" no perfil
2. Clique em "⏳ Pendentes"
3. Revise cada lista
4. Se necessário, edite itens, quantidades ou preços
5. Digite seu nome
6. Clique em "✅ Aprovar" ou "❌ Rejeitar"

#### 2. Comprar via Shopper
1. Acesse o app de delivery (Shopper, iFood, etc.)
2. Compre os itens da lista aprovada
3. Anote o valor total pago

#### 3. Registrar a Compra
1. Clique em "✅ Aprovadas"
2. Encontre a lista que você comprou
3. Digite o valor total pago
4. Adicione observações se houver (trocas, substituições)
5. Clique em "✅ Confirmar Compra"

#### 4. Consultar Histórico
1. Clique em "🛍️ Histórico"
2. Use os filtros:
   - Por cuidadora
   - Por período
   - Ordenação
3. Veja detalhes de cada compra

#### 5. Analisar Gastos
1. Clique em "📊 Relatórios"
2. Veja:
   - Métricas gerais (total gasto, média, economia)
   - Gastos por cuidadora
   - Gastos por categoria
   - Evolução no tempo
   - Resumo mensal
   - Itens mais comprados

## 💾 Armazenamento de Dados

Dados salvos localmente em JSON:
- `shopping_app/data/listas.json` - Listas de compras
- `shopping_app/data/compras.json` - Compras realizadas
- `shopping_app/data/cuidadoras.json` - Cadastro de cuidadoras

### Backup
Copie a pasta `shopping_app/data/` regularmente para segurança.

## 📊 Categorias

1. 🍎 **Alimentação** - Comida para a idosa e cuidadoras
2. 💊 **Medicamentos** - Remédios, suplementos
3. 🧴 **Higiene** - Produtos de higiene pessoal
4. 🧹 **Limpeza** - Produtos de limpeza da casa
5. 📦 **Outros** - Outros itens necessários

## 🎯 Benefícios

### Para a Família:
✅ Controle total do que está sendo comprado
✅ Aprovação prévia evita surpresas
✅ Comparação de preços estimados vs reais
✅ Identificação de gastos excessivos
✅ Histórico completo para auditoria
✅ Relatórios mensais automáticos

### Para as Cuidadoras:
✅ Processo organizado para solicitar compras
✅ Registro de suas solicitações
✅ Transparência sobre aprovações
✅ Facilita o trabalho do dia a dia

## 📈 Casos de Uso Reais

### Exemplo 1: Compra Semanal
1. **Segunda-feira**: Cuidadora Ana cria lista com itens da semana
2. **Segunda-feira**: Família revisa e aprova
3. **Terça-feira**: Família compra via Shopper - R$ 280,00
4. **Terça-feira**: Família registra compra (estimado era R$ 250,00)
5. **Sistema**: Registra diferença de +R$ 30,00 para análise

### Exemplo 2: Compra de Emergência
1. **Quinta-feira 20h**: Cuidadora Maria nota falta de medicamento
2. **Quinta-feira 20h05**: Cria lista urgente só com o remédio
3. **Quinta-feira 20h10**: Família aprova rapidamente
4. **Quinta-feira 20h30**: Família compra via delivery rápido
5. **Quinta-feira 21h**: Registra compra

### Exemplo 3: Análise Mensal
1. **Fim do mês**: Família acessa "Relatórios"
2. **Visualiza**: Gastou R$ 1.200 no mês
3. **Identifica**: Cuidadora X fez mais compras que outras
4. **Conversa**: Entende que X trabalhou mais dias
5. **Descobre**: Categoria "Alimentação" é 60% do gasto

## ❓ Perguntas Frequentes

**Como as cuidadoras acessam o sistema?**
- Pelo mesmo navegador, selecionando o perfil "Cuidadora"

**E se a cuidadora não souber o preço?**
- Pode deixar R$ 0,00 que a família ajusta antes de aprovar

**Posso editar uma lista depois de enviar?**
- Não, mas a família pode editar antes de aprovar

**O que acontece se rejeitar uma lista?**
- A cuidadora vê que foi rejeitada e pode criar uma nova

**Como sei quem está gastando mais?**
- Vá em "Relatórios" → "Gastos por Cuidadora"

**Posso comparar meses diferentes?**
- Sim, use o "Resumo Mensal" em "Relatórios"

**Os dados ficam na nuvem?**
- Não, ficam salvos localmente no computador

**Posso acessar de vários dispositivos?**
- Sim, se instalar em cada um OU usar compartilhamento de rede

## 🔒 Privacidade e Segurança

- Dados armazenados localmente (não vão para internet)
- Sem login/senha (confie em quem tem acesso ao computador)
- Faça backups regulares da pasta `data/`
- Não compartilhe arquivos JSON publicamente

## 🛠️ Tecnologias

- **Streamlit**: Interface web interativa
- **Pandas**: Análise de dados
- **Plotly**: Gráficos e visualizações
- **Python JSON**: Armazenamento persistente

## 📞 Suporte

Para dúvidas:
1. Consulte este README
2. Veja os exemplos práticos acima
3. Teste com dados fictícios primeiro

## 📝 Dicas de Uso

### Para Melhores Resultados:

1. **Cuidadoras**: Sejam específicas nos nomes dos itens
   - ✅ "Leite integral Parmalat 1L"
   - ❌ "Leite"

2. **Família**: Revise as listas diariamente
   - Configure alertas para não acumular

3. **Todos**: Use observações quando necessário
   - "Paciente prefere marca X"
   - "Produto Y estava em falta, comprei Z"

4. **Gestão**: Analise relatórios mensalmente
   - Identifique padrões
   - Ajuste orçamentos
   - Converse com cuidadoras sobre gastos

## 🚀 Próximos Passos

Após instalação:
1. Cadastre todas as cuidadoras
2. Faça um teste com lista fictícia
3. Treine as cuidadoras no uso
4. Estabeleça rotina de aprovação
5. Defina quem da família aprova
6. Configure backup automático

---

**Desenvolvido com ❤️ para facilitar o cuidado familiar**
