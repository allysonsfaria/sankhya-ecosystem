---
id: "32482896112279"
titulo: "Controle e Liberação de Limites de Crédito"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32482896112279-Controle-e-Libera%C3%A7%C3%A3o-de-Limites-de-Cr%C3%A9dito"
trilha: "Assistente de Melhores Práticas > Vendas"
atualizado_em: "2026-07-22T14:31:06Z"
rotulos: ["Configuração", "Parceiro", "Liberação de Limites", "Crédito", "Financeiro"]
---

# Controle e Liberação de Limites de Crédito

### Descrição

A funcionalidade **Controle e Liberação de Limites de Crédito** permite configurar os processos de validação e concessão de limites de crédito para clientes, definindo os critérios de validação e os responsáveis pela liberação.

Ela oferece os seguintes recursos:

- **Gestão de Limites de Crédito**: Permite aos usuários consultar, ajustar e gerenciar os limites de crédito definidos para os parceiros, além de acompanhar as liberações e solicitações.
- **Configuração de Validação de Limite de Crédito**: Libera a criação e personalização das regras de validação, como "Valida todo a receber", "Valida a receber e provisões no mês", entre outras opções, para garantir a conformidade com os critérios financeiros estabelecidos.
- **Gerenciamento de Usuários Liberadores**: Libera o acesso para configurar e gerenciar os usuários responsáveis por aprovar ou rejeitar as solicitações de liberação de crédito quando um valor excede o limite preestabelecido.

### Como instalar

1. Clique em **"Iniciar"**.
2. Escolha o tipo de validação de crédito desejado e defina os critérios de análise (ex: considerar provisões, validar todo o a receber etc.).
3. Selecione os grupos e/ou usuários responsáveis por aprovar as solicitações de crédito.
4. Defina os valores limites e tipo de limite (evento ou mensal) para cada usuário liberador.
5. Clique em **"Avançar"** para revisar as configurações.
6. Clique em **"Instalar"** para concluir a instalação.

### Detalhes da instalação

**Acessos liberados**

- **Liberação de Limites**
  - Caminho: Configurações » Rotinas » Liberação de Limites.
  - Permissões: Consultar, Incluir, Alterar, Excluir.

**Parâmetros atualizados**

- **VALLIMCRED**: Define o tipo de validação de crédito (**"bloqueia"**, **"alerta"** ou **"desativa"**).
- **LIMCREDMATRIZ**: Define se o crédito será avaliado por matriz do parceiro.
- **VALLIMCREDZERO**: Ativa a validação mesmo quando o limite de crédito do parceiro for igual a zero.

**Tabelas atualizadas**

- **TSILIM – Limites de Liberação**: Cadastro e atualização dos usuários liberadores para o evento de atraso (**"Evento 3"**).
