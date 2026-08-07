# 📊 Bot de Controle de Gastos no Telegram com Excel

Este é um projeto em Python que cria um assistente pessoal no Telegram para gerenciar suas finanças. Cada pessoa que baixar este código pode criar seu próprio robô e gerar planilhas de gastos exclusivas de forma totalmente independente.

---

## 🚀 Como Usar o Projeto

Siga os passos abaixo para baixar, configurar e rodar o assistente no seu próprio computador.

### Passo 1: Baixar os arquivos
1. No topo desta página do GitHub, clique no botão verde **"Code"**.
2. Selecione **"Download ZIP"** e extraia os arquivos na pasta de sua preferência.

### Passo 2: Criar o seu Bot no Telegram
Cada usuário precisa gerar o seu próprio token de acesso:
1. Abra o Telegram e pesquise por **@BotFather** (o robô oficial com selo azul).
2. Envie o comando `/newbot`.
3. Escolha um nome para o seu bot (Ex: `Meus Gastos`).
4. Escolha um nome de usuário que termine obrigatoriamente com `bot` (Ex: `meus_gastos_financeiro_bot`).
5. O @BotFather vai te enviar uma mensagem contendo o seu **Token de Acesso** (uma sequência longa de letras e números). Copie esse código.

### Passo 3: Instalar as Dependências no Computador
Abra o terminal do seu computador (Prompt de Comando, PowerShell ou Terminal do Mac) dentro da pasta onde você extraiu os arquivos do projeto e rode o comando abaixo:
```bash
pip install -r Requirements.txt.txt
```

### Passo 4: Configurar o Token e Rodar o Bot
Para proteger os seus dados, o código lê o seu token do sistema operacional. Escolha o comando abaixo dependendo do seu sistema e execute-o no terminal:

* **No Windows (Prompt de Comando / CMD):**
  ```cmd
  set TELEGRAM_BOT_TOKEN=COLE_O_SEU_TOKEN_AQUI
  ```
* **No Linux / Mac (ou terminais Git Bash):**
  ```bash
  export TELEGRAM_BOT_TOKEN="COLE_O_SEU_TOKEN_AQUI"
  ```

Após configurar a variável acima, inicie o robô digitando:
```bash
python BotAlemao.py
```

---

## 📈 Como Alimentar a Planilha

Com o terminal aberto e o robô rodando, abra o Telegram, procure pelo `@usuario_do_seu_bot` que você criou no Passo 2 e clique em **Começar** (`/start`).

Para registrar novos gastos, envie mensagens sempre seguindo o padrão **Item - Valor**:
* `Almoço - 25.50`
* `Supermercado - 120`
* `Gasolina - 80.00`

O robô responderá confirmando o registro e criará automaticamente um arquivo chamado `planilha_gastos.xlsx` na mesma pasta do código, salvando a data atual, o nome do item e o valor digitado.
