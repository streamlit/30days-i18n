# 🛒 Compras da Família - App Completo

> Feito com carinho para quem cuida 💛

Um aplicativo PWA completo para gerenciar despesas familiares, aprovar contas e manter a lista de compras da Dona Judith sempre atualizada.

## ✨ Funcionalidades Principais

### 👨‍👩‍👧‍👦 Para a Família:
- ✅ Aprovar ou rejeitar despesas cadastradas
- 📊 Ver divisão automática de custos entre membros
- 📈 Relatórios por período
- 📝 Histórico completo de despesas aprovadas
- 🛒 Acessar lista fixa de compras

### 💼 Para as Cuidadoras:
- ➕ Cadastrar novas despesas com valor e data
- 📋 Ver status das despesas cadastradas
- 🛒 Marcar itens da lista fixa
- 💾 Todos os dados salvos localmente

### 📝 Lista Fixa da Dona Judith:
- ✓ Lista completa pré-cadastrada
- 🔍 Busca rápida de produtos
- 🏷️ Filtros por categoria
- ✅ Marcar/desmarcar itens comprados
- 💾 Estado salvo automaticamente

## 🚀 Como Usar

### Instalação Local

```bash
# Entre na pasta do projeto
cd compras-familia

# Instale as dependências
npm install

# Rode o projeto localmente
npm run dev
```

O app estará disponível em `http://localhost:5173`

### Build para Produção

```bash
npm run build
```

Os arquivos otimizados estarão em `dist/`

## 📦 Deploy no Vercel

### Opção 1: Via Interface (Mais Fácil)

1. Acesse [vercel.com](https://vercel.com)
2. Faça login com GitHub/GitLab/Bitbucket
3. Clique em **"New Project"**
4. Importe este repositório
5. Configure:
   - **Framework Preset**: Vite
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
6. Clique em **"Deploy"**
7. Pronto! Seu app estará no ar

### Opção 2: Via CLI

```bash
# Instalar Vercel CLI globalmente
npm i -g vercel

# Fazer deploy
vercel

# Deploy para produção
vercel --prod
```

## 📱 Instalar como App no Celular

### Android (Chrome)
1. Abra o app no Chrome
2. Toque no menu (⋮) no canto superior direito
3. Selecione **"Adicionar à tela inicial"**
4. Confirme a instalação
5. Use como app nativo!

### iOS (Safari)
1. Abra o app no Safari
2. Toque no botão de compartilhar (□↑)
3. Selecione **"Adicionar à Tela de Início"**
4. Toque em **"Adicionar"**
5. Pronto! App instalado

### Desktop (Chrome/Edge)
1. Abra o app no navegador
2. Clique no ícone de instalação (+) na barra de endereço
3. Confirme a instalação
4. Use como aplicativo independente

## 🎯 Fluxo de Uso

### Cenário Completo:

1. **Cuidadora cadastra despesa:**
   ```
   Perfil: Cuidadora → Tab "Pendentes"
   → + Nova Despesa → Preenche (descrição, valor, data)
   → Cadastrar
   ```

2. **Família aprova:**
   ```
   Perfil: Família → Tab "Pendentes"
   → Vê a despesa → Clica "✓ Aprovar"
   ```

3. **Sistema gera divisão automática:**
   ```
   Tab "Divisão" → Vê valores divididos por membro
   - João: 50% do valor
   - Maria: 30% do valor
   - Lúcia: 20% do valor
   ```

4. **Despesa vai para histórico:**
   ```
   Tab "Histórico" → Despesa aprovada aparece
   → Filtrar por período → Ver total
   ```

### Usando a Lista Fixa:

```
Qualquer perfil → Tab "Lista Fixa"
→ Buscar produto ou filtrar categoria
→ Marcar os itens necessários
→ Estado salvo automaticamente
```

## ⚙️ Personalização

### Mudar Divisão Familiar

Edite `src/config/familyConfig.js`:

```javascript
export const familyMembers = [
  { id: 'm1', name: 'João', percent: 0.5, color: '#6f8f87' },    // 50%
  { id: 'm2', name: 'Maria', percent: 0.3, color: '#c17c5c' },   // 30%
  { id: 'm3', name: 'Lúcia', percent: 0.2, color: '#f4d4a8' },   // 20%
];
```

**Importante:** A soma dos percentuais deve ser 1.0 (100%)

### Modificar Lista Fixa

Edite `src/data/fixedList.js`:

```javascript
export const FIXED_ITEMS = [
  { id: 'vl-1', name: 'Alface', category: '🥬 Verduras e Legumes', checked: false },
  // Adicione, remova ou edite produtos aqui
];
```

### Mudar Cores do App

Edite `src/App.css` (linhas 1-30):

```css
:root {
  --color-primary: #6f8f87;        /* Verde acolhedor */
  --color-secondary: #c17c5c;      /* Terracota */
  --color-accent: #f4d4a8;         /* Bege claro */
  --color-bg: #f7f3ed;             /* Creme */
}
```

## 🛠️ Estrutura do Projeto

```
compras-familia/
├── public/
│   ├── icons/              # Ícones PWA (gerar)
│   ├── manifest.json       # Config PWA
│   └── service-worker.js   # Cache offline
├── src/
│   ├── components/         # Componentes React
│   │   ├── ProfileSelector.jsx      # Tela de seleção
│   │   ├── PendingExpenses.jsx      # Contas pendentes
│   │   ├── ApprovedExpenses.jsx     # Histórico
│   │   ├── FamilySplit.jsx          # Divisão familiar
│   │   └── FixedList.jsx            # Lista da Dona Judith
│   ├── config/
│   │   └── familyConfig.js          # Membros e percentuais
│   ├── data/
│   │   └── fixedList.js             # Lista fixa completa
│   ├── pages/
│   │   └── Dashboard.jsx            # Dashboard principal
│   ├── App.jsx                      # App principal
│   ├── App.css                      # Estilos (personalize aqui!)
│   ├── main.jsx                     # Entry point
│   └── index.css                    # Reset CSS
├── index.html
├── package.json
├── vite.config.js
├── vercel.json                      # Config Vercel
└── README.md
```

## 🎨 Sobre os Ícones PWA

Para ter um app completo, você precisa gerar ícones PNG. Veja instruções em:
`public/icons/README.md`

**Ferramentas recomendadas:**
- [PWA Builder](https://www.pwabuilder.com/imageGenerator)
- [RealFaviconGenerator](https://realfavicongenerator.net/)

## 💾 Armazenamento de Dados

Todos os dados são salvos em **localStorage** do navegador:

- ✅ Despesas (pendentes e aprovadas)
- ✅ Estado da lista fixa (itens marcados)
- ✅ Não precisa de backend
- ✅ Funciona offline

**Importante:** Os dados ficam no navegador. Se limpar o cache, os dados são perdidos.

## 🔧 Tecnologias

- **React 18.2** - UI moderna e reativa
- **Vite 5.0** - Build ultra-rápido
- **CSS Variáveis** - Personalização fácil
- **LocalStorage** - Persistência local
- **PWA** - Instalável e offline
- **Vercel** - Deploy gratuito

## 📊 Exemplos de Uso

### Cadastrar Despesa (Cuidadora)

```
Descrição: Compras da semana
Valor: R$ 280,00
Data: 28/10/2025

→ Salva como "pendente"
```

### Aprovar Despesa (Família)

```
Vê despesa pendente
→ Clica "Aprovar"
→ Sistema calcula:
   - João paga: R$ 140,00 (50%)
   - Maria paga: R$ 84,00 (30%)
   - Lúcia paga: R$ 56,00 (20%)

→ Despesa vai para histórico
```

### Ver Relatório

```
Filtrar: De 01/10/2025 até 31/10/2025
→ Total do período: R$ 1.450,00
→ Divisão:
   - João: R$ 725,00
   - Maria: R$ 435,00
   - Lúcia: R$ 290,00
```

## ❓ Problemas Comuns

### App não está salvando dados
- Verifique se o navegador permite localStorage
- Não use modo anônimo/privado
- Limpe cache e teste novamente

### PWA não instala
- Certifique-se de estar em HTTPS (ou localhost)
- Gere os ícones PNG necessários
- Verifique se manifest.json está acessível

### Estilos não aparecem
- Limpe cache (Ctrl+Shift+R)
- Verifique console para erros
- Faça rebuild: `npm run build`

## 📝 Próximas Melhorias

Ideias para futuras versões:

- [ ] Exportar relatórios em PDF
- [ ] Upload de comprovantes (fotos)
- [ ] Notificações push
- [ ] Sincronização na nuvem (Firebase)
- [ ] Múltiplas famílias
- [ ] App mobile nativo
- [ ] Integração com WhatsApp

## 💛 Sobre o Projeto

Este app foi desenvolvido especialmente para facilitar a vida de famílias que cuidam de seus entes queridos, com atenção especial às necessidades da Dona Judith e suas cuidadoras.

**Características:**
- ✨ Interface simples e acolhedora
- 📱 Funciona em qualquer dispositivo
- 💪 Não precisa de internet (depois de instalado)
- 🎯 Focado em facilitar o dia a dia
- 💛 Feito com muito carinho

---

## 📞 Suporte

Se tiver dúvidas:

1. Leia este README completamente
2. Verifique a seção de Problemas Comuns
3. Abra uma issue no repositório
4. Entre em contato com o desenvolvedor

---

**Desenvolvido com ❤️ para quem cuida**

*Compras da Família - 2025*
