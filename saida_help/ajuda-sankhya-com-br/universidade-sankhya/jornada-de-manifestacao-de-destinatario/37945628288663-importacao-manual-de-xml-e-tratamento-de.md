---
id: "37945628288663"
titulo: "Importação manual de XML e tratamento de  divergências"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37945628288663-Importa%C3%A7%C3%A3o-manual-de-XML-e-tratamento-de-diverg%C3%AAncias"
trilha: "Universidade Sankhya > Jornada de Manifestação de Destinatário (MD-e)"
atualizado_em: "2026-08-18T12:12:05Z"
rotulos: ["Produtos", "Configuração", "Parceiro", "XML", "Importação", "Financeiro"]
---

# Importação manual de XML e tratamento de  divergências

1. **Acesse a rotina Portal de Importação de XML**

**Menu:** Comercial » Rotinas » Portal de Importação de XML 

- Clique no botão “**+**” (**Cadastrar Importação de XML de Notas**)
- Selecione e envie o XML baixado na preparação
- Clique no botão “**Processar Arquivo(s)**”

Para tratamento de:

**Divergência de pedidos ligados**

- Acesse a aba **Pedidos** e localize o pedido na parte inferior da tela.
- No campo **Vinculado**, insira manualmente a quantidade de produtos.
- Verifique se o sistema atualizou as informações no campo correspondente na grade superior e clique novamente em **Validar Importação**.

**Divergência de financeiro**

- Acesse a aba "**Financeiro**", selecione a opção "**Usar Financeiro do Arquivo**" no campo correspondente e clique no botão "**Validar Importação**".

**Divergência Lotes de Produtos não informados**

- Acesse a aba **Produtos por Parceiro**, insira o código do produto e clique em **Validar Importação**.

**Divergências de produtos não encontrados**

- Acesse a aba “**Produtos por Parceiro**” e preencha as colunas indicadas com as informações correspondentes.

  - **Produto**
  - **Controle**, se necessário

Esta ação preencherá automaticamente a aba Produtos Equivalentes na rotina Parceiros. 

O sistema vincula o produto enviado pelo parceiro ao produto já cadastrado na sua base 

de dados, gerando a equivalência entre eles.

**Aviso:** **"Importado com sucesso!**

Se não houver divergências durante a importação, o sistema exibirá o aviso: **"Importado com sucesso!"**
Neste caso:

- Verifique as informações nas abas **Cabeçalho**, **Parceiro**, **Empresa** e **Transportadora**.
- Clique em **Abrir Documento** para ser direcionado à **Central de Compras**.
- Na Central, revise os dados e clique em **Confirmar Nota de Compra** para concluir o processo.

**Aviso:** **“Aguardando liberação para variação do vlr. unitário acima do permitido.-Divergência de valor unitário entre pedido e nota”**

Esse aviso indica uma divergência no valor unitário entre o pedido e a nota fiscal.

- Dentro do **Portal de Importação de XML.**
- Clique no botão **Liberações**.
- Selecione o **Usuário Gestor** como liberador.
- Clique em **Confirmar**.

**Liberação de Limites**

- Acesse a tela  **Liberação de Limite**
  Menu: Configurações »  Avançado »  Liberação de Limite
- Insira os dados do **Liberador** (usuário e senha).
- Clique em **Aplicar**.

O sistema exibirá todas as solicitações pendentes para o liberador.

- Localize o **Pedido de Compra** correspondente.
- Selecione e clique em **Liberar**.

**Validação da Importação**

- Retorne ao **Portal de Importação de XML**.
- Clique no botão “**Validar Importação**”.
- O sistema exibirá a mensagem **"Importado com sucesso"**.
- Clique em **Ok**.
