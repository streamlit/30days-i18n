# 📱 GUIA PASSO A PASSO - Do Zero ao App Funcionando

## ✅ PASSO 1: Verificar se tem Python Instalado

### Windows:
1. Pressione `Win + R`
2. Digite `cmd` e aperte Enter
3. Digite: `python --version`
4. Se aparecer algo como "Python 3.x.x" → ✅ TEM PYTHON
5. Se der erro → ❌ PRECISA INSTALAR (vá para PASSO 1B)

### Mac:
1. Abra o Terminal (Cmd + Espaço, digite "Terminal")
2. Digite: `python3 --version`
3. Se aparecer "Python 3.x.x" → ✅ TEM PYTHON
4. Se der erro → ❌ PRECISA INSTALAR (vá para PASSO 1B)

### PASSO 1B: Instalar Python (se não tiver)

**Windows:**
1. Acesse: https://www.python.org/downloads/
2. Clique em "Download Python 3.x.x"
3. Execute o instalador
4. ⚠️ **IMPORTANTE**: Marque a opção "Add Python to PATH"
5. Clique em "Install Now"
6. Aguarde a instalação

**Mac:**
1. Acesse: https://www.python.org/downloads/
2. Baixe o instalador para Mac
3. Execute e siga as instruções

---

## ✅ PASSO 2: Baixar os Arquivos do App

### Opção A: Já tem o projeto no computador?
- Se você já clonou este repositório, pule para o PASSO 3
- A pasta deve ser algo como: `C:\Users\SeuNome\30days-i18n` ou `/Users/SeuNome/30days-i18n`

### Opção B: Precisa baixar do GitHub
1. Acesse: https://github.com/MariSaliba/30days-i18n
2. Clique no botão verde "Code"
3. Clique em "Download ZIP"
4. Extraia o arquivo ZIP para uma pasta de sua escolha
5. Anote o caminho da pasta (ex: `C:\Users\SeuNome\30days-i18n`)

---

## ✅ PASSO 3: Instalar as Dependências

### Windows:
1. Abra o Prompt de Comando (Win + R, digite `cmd`, Enter)
2. Navegue até a pasta do projeto:
   ```
   cd C:\Users\SeuNome\30days-i18n
   ```
   (Substitua pelo caminho real da sua pasta)

3. Instale as bibliotecas necessárias:
   ```
   pip install streamlit pandas plotly pillow
   ```

4. Aguarde a instalação (pode demorar alguns minutos)
5. Quando terminar, verá "Successfully installed..."

### Mac/Linux:
1. Abra o Terminal
2. Navegue até a pasta:
   ```
   cd /Users/SeuNome/30days-i18n
   ```

3. Instale as dependências:
   ```
   pip3 install streamlit pandas plotly pillow
   ```

4. Aguarde a instalação

---

## ✅ PASSO 4: Executar o App

### Windows:
1. No mesmo Prompt de Comando (ainda na pasta do projeto)
2. Digite:
   ```
   streamlit run shopping_app/app.py
   ```

3. Pressione Enter
4. Aguarde alguns segundos
5. O navegador abrirá AUTOMATICAMENTE! 🎉

### Mac/Linux:
1. No Terminal (ainda na pasta do projeto)
2. Digite:
   ```
   streamlit run shopping_app/app.py
   ```

3. Pressione Enter
4. O navegador abrirá automaticamente

---

## ✅ PASSO 5: Usar o App

Quando o navegador abrir, você verá:

### Tela Inicial:
```
🛒 Controle de Compras Familiar
Sistema de controle e aprovação de listas de compras

👤 Perfil: [Família ▼] ou [Cuidadora ▼]

[⏳ Pendentes]  [✅ Aprovadas]  [🛍️ Histórico]  [📊 Relatórios]
```

### Testar como CUIDADORA:

1. **Selecione "Cuidadora" no menu Perfil** (canto superior direito)

2. **Clique em "➕ Nova Lista"**

3. **Selecione o nome da cuidadora**
   - Por padrão: Ana, Maria ou João
   - Pode adicionar novos nomes depois

4. **Adicione itens à lista:**
   - Item: "Leite integral"
   - Categoria: "Alimentação"
   - Quantidade: 2
   - Preço estimado: 5.50
   - Clique em "➕ Adicionar"

5. **Adicione mais alguns itens**
   - Pão francês - Alimentação - 3 unidades - R$ 1.00
   - Açúcar - Alimentação - 1 unidade - R$ 4.50

6. **Veja o total calculado automaticamente**

7. **Adicione observações (opcional)**
   - Ex: "Leite sem lactose de preferência"

8. **Clique em "📤 ENVIAR PARA APROVAÇÃO"**

9. **Verá uma mensagem de sucesso e balões! 🎈**

### Testar como FAMÍLIA:

1. **Troque para perfil "Família"** (menu superior direito)

2. **Clique em "⏳ Pendentes"**
   - Verá a lista que a cuidadora criou!

3. **Revise os itens**
   - Pode editar quantidades
   - Pode mudar preços
   - Pode adicionar/remover itens

4. **Digite seu nome** no campo

5. **Clique em "✅ Aprovar"**
   - A lista vai para "Aprovadas"

6. **Vá em "✅ Aprovadas"**
   - Aqui você vê as listas prontas para comprar

7. **Simule uma compra:**
   - Digite o valor total que pagou (ex: R$ 25.00)
   - Adicione observações se quiser
   - Clique em "✅ Confirmar Compra"

8. **Vá em "🛍️ Histórico"**
   - Veja todas as compras registradas
   - Use filtros por período, cuidadora, etc.

9. **Vá em "📊 Relatórios"**
   - Veja gráficos de gastos
   - Gastos por cuidadora
   - Gastos por categoria
   - Resumo mensal (para dividir entre os filhos!)

---

## ✅ PASSO 6: Acessar de Outros Dispositivos (Celular dos Filhos)

### Mesma Rede WiFi (Casa):

1. **No computador onde o app está rodando:**
   - Windows: Abra o Prompt e digite `ipconfig`
   - Mac: Abra Terminal e digite `ifconfig`
   - Procure por "IPv4" ou "inet" (ex: 192.168.1.100)

2. **Pare o app atual:** Pressione `Ctrl + C` no terminal

3. **Execute novamente com acesso remoto:**
   ```
   streamlit run shopping_app/app.py --server.address 0.0.0.0
   ```

4. **No celular dos filhos:**
   - Conecte na MESMA WiFi da casa
   - Abra o navegador (Chrome/Safari)
   - Digite: `http://192.168.1.100:8501`
   - (Substitua pelo IP que você descobriu)

5. **Instalar como App no Celular:**
   - **Android (Chrome):** Menu (⋮) → "Adicionar à tela inicial"
   - **iPhone (Safari):** Compartilhar (□↑) → "Adicionar à Tela de Início"

### Acesso pela Internet (De Qualquer Lugar):

**Opção 1: Streamlit Cloud (GRÁTIS - RECOMENDADO)**

1. Acesse: https://share.streamlit.io
2. Clique em "Sign in" (use conta Google/GitHub)
3. Clique em "New app"
4. Selecione:
   - Repository: `MariSaliba/30days-i18n`
   - Branch: `claude/elderly-shopping-control-app-011CUdJUrW7qVX3Xdok9XCx1`
   - Main file path: `shopping_app/app.py`
5. Clique em "Deploy!"
6. Aguarde 2-5 minutos
7. Você receberá uma URL tipo: `https://seu-app.streamlit.app`
8. Compartilhe essa URL com os filhos!
9. Todos podem acessar de qualquer lugar! 📱

---

## ❓ PROBLEMAS COMUNS

### "streamlit: command not found"
- Solução: Execute `pip install streamlit` novamente
- No Mac, tente: `pip3 install streamlit`

### "Permission denied" ou erro de permissão
- Solução: Feche o terminal e abra como Administrador
- Windows: Clique com botão direito no Prompt → "Executar como Administrador"

### Navegador não abre automaticamente
- Solução: Abra manualmente e digite: `http://localhost:8501`

### "Address already in use"
- Solução: Outra coisa está usando a porta 8501
- Use: `streamlit run shopping_app/app.py --server.port 8502`
- Depois acesse: `http://localhost:8502`

### Não consigo acessar do celular
- Certifique-se que:
  - Celular está na MESMA WiFi
  - Firewall do Windows não está bloqueando
  - Usou `--server.address 0.0.0.0` ao executar

---

## 📞 PRECISA DE AJUDA?

1. Leia novamente este passo a passo
2. Veja se pulou alguma etapa
3. Verifique as mensagens de erro
4. Tente reiniciar o computador

---

## 🎉 PRONTO!

Agora você tem:
- ✅ App rodando no computador
- ✅ Testou criar listas (Cuidadora)
- ✅ Testou aprovar listas (Família)
- ✅ Viu os relatórios
- ✅ Pode acessar do celular

**Próximos passos:**
1. Cadastre as cuidadoras reais (Menu Cuidadoras)
2. Ensine as cuidadoras a criar listas
3. Configure acesso remoto para os filhos
4. Comece a usar no dia a dia!

---

## 💡 DICA EXTRA: Deixar Rodando Sempre

Para o app ficar disponível 24/7:

1. Use um computador que fica ligado sempre (servidor caseiro)
2. OU faça deploy no Streamlit Cloud (grátis, sempre online)
3. OU use Raspberry Pi (computador pequeno e barato que fica ligado)

---

**BOA SORTE! 🍀**
