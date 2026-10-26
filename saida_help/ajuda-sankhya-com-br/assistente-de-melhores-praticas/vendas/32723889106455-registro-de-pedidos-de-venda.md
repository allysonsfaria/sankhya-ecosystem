---
id: "32723889106455"
titulo: "Registro de Pedidos de Venda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32723889106455-Registro-de-Pedidos-de-Venda"
trilha: "Assistente de Melhores Práticas > Vendas"
atualizado_em: "2026-07-22T14:30:37Z"
rotulos: ["Configuração", "Portal de Vendas", "TOP", "Vendas", "Cadastro"]
---

# Registro de Pedidos de Venda

### Descrição

A funcionalidade **Registro de Pedidos de Venda** permite configurar os processos de registro de pedidos de venda, definindo os responsáveis pela operação e liberando os acessos necessários para sua execução.
Ele libera acesso a:

- **Gestão de Pedidos de Venda**: Permite aos usuários consultar, incluir, alterar e excluir registros relacionados ao lançamento de pedidos de venda.
- **Configuração de Tipos de Operação (TOP)**: Libera a criação e personalização do tipo de operação **"Pedido de Venda"**, caso não exista. A TOP 1001 - Pedido de Venda é criada para controlar e categorizar todas as operações de pedidos de venda no sistema.

### Como instalar

1. Clique em **"Iniciar"**.
2. Selecione os **usuários que são gerentes de vendas**, responsáveis por liderar a equipe de vendas.
3. Selecione os **usuários que são vendedores**, responsáveis diretos pelo registro de pedidos.
4. Informe, se houver, os **vendedores externos**, que não são usuários do sistema.
5. Preencha os **dados complementares** da equipe de vendas para o correto vínculo com o gerente correspondente.
6. Revise o resumo das configurações e clique em **"Instalar"** para concluir.

### Detalhes da instalação

**Acessos liberados**

- **Portal de Vendas**
  **Caminho:** Comercial » Pedidos
  - Permissões para gerentes: consultar, incluir, alterar, excluir, alterar ligação entre documentos, rateio, imprimir/reimprimir.
  - Permissões para vendedores: consultar, incluir, alterar, alterar ligação entre documentos, rateio, imprimir/reimprimir, consultar limites de liberação.

**Tabelas atualizadas**

**TGFVEN – Cadastro de Vendedores**

- Alteração de tipo de vendedor (comprador → gerente ou vendedor) para usuários existentes.
- Criação de novos vendedores a partir dos dados coletados.
- Vínculo entre usuários e vendedores criados.
- Criação de vendedores externos conforme informado no passo 3.

**TGFTOP – Tipos de Operação**

- Inclusão e ativação da **"TOP 1001 – Pedido de Venda"**, com base no modelo padrão.

**TGFNUM – Controle de Numeração**

- Criação da base de numeração **"Pedido de Venda"** para todas as empresas ativas na base, sem série.
- Configuração de impressora, modelo fiscal e numeração automática.

**![Imagem 1: Vale saber](https://ajuda.sankhya.com.br/hc/article_attachments/32723889103511) Vale saber**

Ao realizar o vínculo entre usuários e vendedores, certifique-se de que os dados complementares da equipe de vendas foram preenchidos corretamente para garantir a correta vinculação com o gerente correspondente.
