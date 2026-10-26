---
id: "35163699510679"
titulo: "Nome de coluna 'VITEM_IBSCBS' inválido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35163699510679-Nome-de-coluna-VITEM-IBSCBS-inv%C3%A1lido"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:25:56Z"
rotulos: ["Portal de Vendas", "Livros Fiscais", "Atualização", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "Nome de coluna", "VITEM_IBSCBS", "Nome de coluna 'VITEM_IBSCBS' inválido", "Importação XML"]
---

# Nome de coluna 'VITEM_IBSCBS' inválido

**MENSAGEM:**

Nome de coluna 'VITEM\_IBSCBS' inválido.

**SITUAÇÃO:**

O erro é apresentado ao abrir os **Portais de Vendas**, **Portal de Compras**, **Portal de Importação XML** ou outras rotinas que utilizam a tabela **TGFITE**.

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/35163677384343)SOLUÇÃO:**

Para correção, **é necessário atualizar o módulo Livros Fiscais** para a versão **5.16.2** ou superior (caso já esteja disponível uma versão mais recente).

**O processo de atualização deve ser realizado da seguinte forma:**

**(1)**  Solicite que **todos os usuários do sistema encerrem sua sessão;**

**(2)** Acesse a **"Administração do Servidor"** e selecione a opção **"Atualização do Sistema"** para abrir o WPM.

![Imagem 2: (2) Acesse a "Administração do Servidor" e selecione a opção "Atualização do Sistema" para abrir o WPM.](https://ajuda.sankhya.com.br/hc/article_attachments/35163916715159)

**(3)**  No **WPM**, acesse a aba **"Atualização de Módulos"**.

**(4)**  Selecione a versão **5.16.2** (ou superior) do módulo **Livros Fiscais**.

**(5)**  **Concluída a atualização, o problema estará corrigido.**

(1)** Observação:** **se o ambiente estiver hospedado em nuvem, a atualização deve ser solicitada à nuvem. Em caso de ambiente local, o processo deve ser conduzido pelo setor de TI da empresa.**

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/35163677388183)CAUSA:**

Erro de criação de script na versão anterior do modulo.
