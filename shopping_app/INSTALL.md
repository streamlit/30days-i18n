# 📱 Guia de Instalação - App de Controle de Compras

## 🚀 Instalação e Configuração

### 1. Requisitos
- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### 2. Instalação das Dependências

No diretório raiz do projeto (`30days-i18n`), execute:

```bash
pip install -r requirements.txt
```

### 3. Executar o Aplicativo

```bash
streamlit run shopping_app/app.py
```

O aplicativo abrirá automaticamente em `http://localhost:8501`

## 📱 Instalando como PWA (Progressive Web App)

### No Android (Chrome/Edge):

1. Abra o app no navegador Chrome
2. Toque no menu (⋮) no canto superior direito
3. Selecione "Adicionar à tela inicial" ou "Instalar app"
4. Confirme a instalação
5. O ícone do app aparecerá na tela inicial do seu celular

### No iPhone (Safari):

1. Abra o app no Safari
2. Toque no botão de compartilhar (□↑)
3. Role para baixo e selecione "Adicionar à Tela de Início"
4. Confirme o nome e toque em "Adicionar"
5. O ícone aparecerá na tela inicial

### No Desktop (Chrome/Edge):

1. Abra o app no navegador
2. Clique no ícone de instalação (+) na barra de endereços
3. OU vá em Menu → "Instalar Controle de Compras"
4. O app será instalado e poderá ser aberto como aplicativo nativo

## 🌐 Acesso Remoto (Para os Filhos Acompanharem)

### Opção 1: Rede Local (mesma WiFi)

1. No computador onde o app está rodando, descubra o IP local:

**Windows:**
```cmd
ipconfig
```
Procure por "Endereço IPv4" (ex: 192.168.1.100)

**Mac/Linux:**
```bash
ifconfig
```
Procure por "inet" (ex: 192.168.1.100)

2. Execute o app com:
```bash
streamlit run shopping_app/app.py --server.address 0.0.0.0
```

3. Os filhos podem acessar pelo celular usando:
```
http://IP_DO_COMPUTADOR:8501
```
Exemplo: `http://192.168.1.100:8501`

### Opção 2: Streamlit Cloud (Grátis, acesso pela internet)

1. Crie uma conta gratuita em https://share.streamlit.io
2. Conecte seu repositório GitHub
3. Faça deploy do app
4. Você receberá uma URL pública (ex: `app-compras.streamlit.app`)
5. Compartilhe essa URL com os filhos

### Opção 3: Ngrok (Acesso temporário pela internet)

1. Instale o ngrok: https://ngrok.com/download
2. Execute o app normalmente
3. Em outro terminal:
```bash
ngrok http 8501
```
4. Use a URL fornecida pelo ngrok
5. **Nota**: URL muda toda vez que reinicia, use apenas para testes

## 👨‍👩‍👧‍👦 Configuração para Múltiplos Filhos

### Sistema de Divisão de Gastos

O app possui controle completo de gastos que podem ser divididos entre os filhos:

1. **Visualizar Gastos Mensais**:
   - Perfil Família → Relatórios
   - Veja o total do mês em "Gasto Total"

2. **Dividir Gastos**:
   - Anote o valor total do mês
   - Divida pelo número de filhos
   - Ex: R$ 1.200 ÷ 3 filhos = R$ 400 por filho

3. **Relatório Detalhado**:
   - Cada filho pode acessar o app
   - Ver histórico completo
   - Consultar compras individuais
   - Verificar quais cuidadoras gastaram mais

## 🔐 Dicas de Segurança

1. **Senha WiFi**: Mantenha sua rede WiFi protegida com senha forte
2. **Backup**: Faça backup regular da pasta `shopping_app/data/`
3. **Privacidade**: Não compartilhe a URL pública em redes sociais
4. **Atualizações**: Mantenha o Python e dependências atualizados

## 📊 Fluxo de Uso Recomendado

### Para Cuidadoras:
1. Acessam pelo computador ou celular (mesma rede)
2. Perfil: Cuidadora
3. Criam listas de compras
4. Enviam para aprovação

### Para Família (Filhos):
1. Cada filho acessa pelo celular (instala como PWA)
2. Perfil: Família
3. Recebem notificação de listas pendentes
4. Aprovam e compram
5. Registram valores reais
6. Acompanham gastos mensais
7. Dividem o valor no final do mês

## 🛠️ Solução de Problemas

### App não abre
```bash
# Verifique se as dependências estão instaladas
pip install -r requirements.txt

# Tente executar com verbose
streamlit run shopping_app/app.py --logger.level=debug
```

### Erro de permissão na pasta data
```bash
# No diretório do app
mkdir -p shopping_app/data
chmod 755 shopping_app/data
```

### Não consigo acessar de outro dispositivo
- Verifique se ambos estão na mesma rede WiFi
- Verifique o firewall do computador
- Certifique-se de usar `--server.address 0.0.0.0`

### PWA não instala
- Use Chrome ou Edge (melhor suporte a PWA)
- Certifique-se que está usando HTTPS ou localhost
- Limpe o cache do navegador

## 📞 Suporte

Para dúvidas:
1. Consulte o README.md principal
2. Verifique a documentação do Streamlit: https://docs.streamlit.io
3. Teste com dados fictícios primeiro

## 🎯 Checklist de Implantação

- [ ] Instalou Python 3.7+
- [ ] Instalou dependências (`pip install -r requirements.txt`)
- [ ] Executou o app localmente
- [ ] Testou criar lista como Cuidadora
- [ ] Testou aprovar lista como Família
- [ ] Configurou acesso remoto (escolha uma opção)
- [ ] Ensinou as cuidadoras a usar
- [ ] Compartilhou URL com os filhos
- [ ] Todos instalaram como PWA nos celulares
- [ ] Configurou rotina de backup da pasta data/
- [ ] Definiu dia do mês para divisão de gastos

## 🎉 Tudo Pronto!

Agora o sistema está funcionando e todos os filhos podem acompanhar os gastos em tempo real pelo celular!
