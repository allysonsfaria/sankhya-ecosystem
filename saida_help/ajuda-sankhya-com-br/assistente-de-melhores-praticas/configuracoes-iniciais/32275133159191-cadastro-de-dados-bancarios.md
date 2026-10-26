---
id: "32275133159191"
titulo: "Cadastro de Dados Bancários"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32275133159191-Cadastro-de-Dados-Banc%C3%A1rios"
trilha: "Assistente de Melhores Práticas > Configurações Iniciais"
atualizado_em: "2026-07-22T16:17:24Z"
rotulos: ["Configuração", "Contas", "Parceiro", "Financeiro", "Cadastro"]
---

# Cadastro de Dados Bancários

### Descrição

Configuração de dados bancários com precisão. Integra informações validadas por **APIs** e bases de dados internas, garantindo **consistência e conformidade**.

**Coleta e Validação de Dados**

Para dados inseridos manualmente, o sistema utiliza as seguintes **APIs** para validação e complementação das informações:

- **API Receita Federal** – Consulta os dados bancários informados e preenche automaticamente a razão **social, CNPJ e endereço** na tela de parceiros.
- **API BACEN** – Valida o **número da agência** e insere automaticamente o nome correspondente na tela de agências.
- **Banco de dados interno** – Verifica a existência de bancos e agências já cadastrados no sistema.

### Como instalar

1. Clique em "**Iniciar**".

2. Clique em "**+**" para adicionar uma conta bancária.

3. Preencha os campos do formulário com as seguintes informações:

**• Empresa**

**• Banco**

**• Agência (sem DV - dígito verificador)**

**• DV da Agência**

**• Número da Conta (sem DV)**

**• DV da Conta**

**• Tipo de Conta**

4. Clique no ícone "**Salvar**".

5. Clique em "**Avançar**".

6. Selecione se deseja a criação de conta "Tesouraria" para cada empresa (caso ainda não tenha).

7. Clique em "**Avançar**" novamente.

8. Verifique o resumo com as contas bancárias configuradas.

9. Clique em "**Instalar**" para concluir a configuração.

### Detalhes da instalação

Com base nos dados consultados pela **API da Receita Federal / Speedio** e **BACEN**, o sistema verifica se os endereços das agências e bancos já estão cadastrados. Caso contrário, ocorre a **atualização sequencial** das seguintes tabelas:

#### 1. Cadastro de endereço (se ainda não registrado)

- TSITEND – Tipo de endereço
- TSIEND – Endereço
- TSIBAI – Bairro
- TSICID – Cidade

#### 2. Outras tabelas atualizadas

- TSIAGE – Cadastro de agências
- TSICTA – Cadastro de contas bancárias
- TSIREGMOD – Auditoria de modificações
- TGFPAR – Cadastro de parceiros, incluindo os dados de cada banco

### Como simular

Para acessar o cadastro realizado:

1. Acesse a tela **“Contas”**:

- vá até Configurações > Cadastros > Bancários > Contas;
- confira os dados inseridos conforme as informações de contas e agências.

**2.** Acesse a tela **“Parceiros”**:

- vá até Configurações > Cadastros > Parceiros;
- clique em "Mostrar grade" e "Atualizar".

**Vale saber**
Preencheu os dados da conta? O sistema valida tudo automaticamente com Receita e BACEN. Isso evita erros, como agência inexistente ou dados do parceiro incompletos. Se for cadastrar contas para várias empresas, vale ativar a opção da conta tesouraria — ela facilita o controle financeiro no dia a dia!
