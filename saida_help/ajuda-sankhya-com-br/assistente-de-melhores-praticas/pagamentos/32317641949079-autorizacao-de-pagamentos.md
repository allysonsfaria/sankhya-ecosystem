---
id: "32317641949079"
titulo: "Autorização de Pagamentos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32317641949079-Autoriza%C3%A7%C3%A3o-de-Pagamentos"
trilha: "Assistente de Melhores Práticas > Pagamentos"
atualizado_em: "2026-07-22T16:11:02Z"
rotulos: ["Configuração", "Eventos", "Segurança", "Movimentação Financeira", "TOP", "Financeiro"]
---

# Autorização de Pagamentos

### Descrição

A funcionalidade **Autorização de Pagamentos** registra e gerencia as autorizações de pagamentos por parte dos usuários responsáveis, garantindo segurança e controle sobre as movimentações financeiras da empresa.

Permite:

- Definir quais tipos de operação exigem autorização de pagamento.
- Estabelecer um valor mínimo a partir do qual a autorização será exigida.
- Cadastrar os usuários autorizadores com respectivos limites e tipos de alçada.
- Liberar os acessos necessários para a rotina de autorização.

### Como instalar

1. Clique em **"Iniciar"**.
2. O sistema verifica se existe ao menos uma **TOP do tipo G** (Pagamento).
   • Caso **não exista**, o processo será finalizado com a seguinte mensagem: "Não é possível instalar melhor prática. Não há Tipos de Operação de Pagamento configurados".
3. Defina os **Tipos de Operação** que exigirão autorização para pagamentos.
4. Defina o **valor mínimo para exigir autorização de pagamento**. Se não desejar exigir um valor mínimo, apenas avance.
5. Cadastre os **usuários autorizadores e seus limites**. Para cada usuário, preencha:
   • Valor limite.
   • Tipo de limite (**Evento** ou **Mensal**).
6. Verifique o resumo com as TOPs, valor mínimo e usuários definidos e clique em **"Instalar"** para concluir a configuração.

### Detalhes da instalação

**Acessos liberados**

**Autorização de Pagamentos**
Caminho: Financeiro » Autorização de Pagamentos
Permissões: Incluir, Alterar, Excluir
Acesso concedido a todos os usuários selecionados

**Tabelas Atualizadas**

- **TGFTOP – Tipos de Operação**
  - Atualização do campo ‘Valor mínimo para Autorização de Pagamentos’ (VLRMINAP)conforme os tipos de operação selecionados e valor mínimo informado.
- **TDDPER – Acessos**
  - Liberação de acessos para a funcionalidade **Autorização de Pagamentos**.
- **TSILIM – Usuários Liberadores**
  - Inserção, atualização ou exclusão das permissões dos usuários responsáveis pela liberação, com o evento: **24 (Autorização de Pagamentos)**.
