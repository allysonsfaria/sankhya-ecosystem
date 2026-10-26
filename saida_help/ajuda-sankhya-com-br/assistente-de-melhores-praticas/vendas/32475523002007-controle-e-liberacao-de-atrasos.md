---
id: "32475523002007"
titulo: "Controle e Liberação de Atrasos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32475523002007-Controle-e-Libera%C3%A7%C3%A3o-de-Atrasos"
trilha: "Assistente de Melhores Práticas > Vendas"
atualizado_em: "2026-08-21T10:49:52Z"
rotulos: ["Configuração", "Parceiro", "Controle", "Vendas", "Financeiro"]
---

# Controle e Liberação de Atrasos

### Descrição

A funcionalidade **Controle e Liberação de Atrasos** permite configurar e gerenciar a validação de atrasos de clientes, determinando se novas vendas a prazo devem ser bloqueadas ou apenas notificadas.

Ela oferece os seguintes recursos:

- **Gestão de Validação de Atrasos**: Define se operações de venda serão impedidas ou apenas alertadas quando houver inadimplência, com opção de considerar o atraso por matriz ou filial do parceiro.
- **Configuração de Carência e Tolerância**: Permite personalizar prazos de carência para início da contagem de atraso e usar tolerâncias específicas cadastradas em cada parceiro.
- **Gestão de Usuários Liberadores**: Libera o cadastro de usuários autorizados a aprovar vendas a clientes em atraso, com definição do limite de dias de alçada.

### Como instalar

1. Clique em **"Iniciar"**.

2. Escolha se deseja ativar o controle de atrasos, definindo o comportamento do sistema (**"bloqueia"**, **"alerta"** ou **"desativa"**).

3. Caso o controle esteja ativado:

3.1 Defina se o atraso será validado por matriz do parceiro.

3.2 Configure se será utilizada a tolerância de inadimplência dos parceiros.

3.3 Informe o número de dias de carência para início da contagem de atraso (se não utilizar a tolerância individual).

4. Se escolhido o bloqueio com liberação, cadastre os usuários liberadores e seus limites de aprovação.

5. Clique em **"Avançar"** para revisar as configurações.

6. Clique em **"Instalar"** para concluir a instalação.

### Detalhes da instalação

**Acessos liberados**

- **Liberação de Limites**: Consultar, Incluir, Alterar, Excluir

**Parâmetros atualizados**

- **VALCLIENTEATRAS**: Define o tipo de validação (**"bloqueia"**, **"alerta"** ou **"desativa"**)
- **ATRASMATRIZ**: Define se o atraso será avaliado por matriz do parceiro
- **USATOLERINADIMP**: Define se a tolerância de inadimplência individual será utilizada
- **DIASCAR**: Define o número de dias de carência para início da contagem de atraso

**Tabelas atualizadas**

- **TSILIM – Limites de Liberação**: Cadastro e atualização dos usuários liberadores para o evento de atraso (Evento 8).
