---
id: "32723265365015"
titulo: "Outras Operações de Saídas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32723265365015-Outras-Opera%C3%A7%C3%B5es-de-Sa%C3%ADdas"
trilha: "Assistente de Melhores Práticas > Vendas"
atualizado_em: "2026-07-22T14:30:40Z"
rotulos: ["Configuração", "Movimentação Financeira", "Portal de Vendas", "TOP", "Venda Mais"]
---

# Outras Operações de Saídas

### Descrição

A funcionalidade **Outras Operações de Saídas** permite configurar as regras e liberar os acessos necessários para o lançamento de operações específicas de saída, como bonificações, entrega futura, simples remessa e remessa para conserto.

Ela oferece os seguintes recursos:

- **Portal de Vendas – Pedidos:** Consultar, incluir, alterar, alterar ligação entre documentos, realizar rateios e imprimir/reimprimir.
- **Portal de Vendas – Notas:** Consultar, incluir, alterar, alterar ligação entre documentos, realizar rateios e imprimir/reimprimir.
- **Configuração de Tipos de Operação (TOP):** Cadastra automaticamente os tipos necessários para cada operação.
- **Controle de Numeração:** Criação das bases de numeração adequadas às operações selecionadas.
- **Liberação de Acessos:** Permissões concedidas automaticamente aos usuários selecionados.

### Como instalar

1. Clique em **"Iniciar"**.
2. Selecione as operações de saída que são realizadas na empresa.
3. Escolha os grupos e/ou usuários responsáveis pelo lançamento dessas operações.
4. Clique em **"Avançar"** para revisar as seleções.
5. Clique em **"Instalar"** para concluir a instalação.

### Detalhes da instalação

**Acessos liberados**

- **Portal de Vendas**: Incluir, Alterar, Consultar
- **Notas**: Incluir, Alterar, Consultar, Configurar, Numeração, Filtro Avançado, Cancelar, Imprimir/Reimprimir, Rateio, Salvar Observações e Campos Adicionais
- **Devoluções**: Incluir, Alterar, Consultar, Configurar, Numeração, Filtro Avançado, Cancelar, Imprimir/Reimprimir, Rateio, Salvar Observações e Campos Adicionais
- **Pedidos**: Incluir, Alterar, Consultar, Configurar, Numeração, Filtro Avançado, Cancelar, Imprimir/Reimprimir, Rateio, Salvar Observações e Campos Adicionais

**Tabelas atualizadas**

- **TGFTOP – Tipos de Operação**
  Inclusão e ativação das TOPs:
  - 1251, 1151, 1051 (Bonificações)
  - 1207, 1157, 1107, 1007 (Entrega Futura)
  - 1158 (Outras Saídas)
  - 1159, 1259 (Remessa para Conserto)

- **TGFNUM – Numeração**
  Criação das bases:
  - **SEMNUM** – Para operações sem numeração
  - **PEDVEN** – Para pedidos de venda (TOP 1007 e 1051)
  - **VENDA** – Para operações com NF-e (modelo 55, série 1)

- **TSIUSU – Usuários**
  Atualização do campo **Inibe acesso às vendas** para Não, permitindo que os usuários selecionados visualizem lançamentos do Tipo de Movimento Venda.

**![Imagem 1: Vale saber Ao configurar as regras e liberar os acessos para o lançamento de operações específicas de saída, como…](https://ajuda.sankhya.com.br/hc/article_attachments/32723224601751) Vale saber**
Ao configurar as regras e liberar os acessos para o lançamento de operações específicas de saída, como bonificações, entrega futura, simples remessa e remessa para conserto, lembre-se de que é crucial ter uma visão clara de quais usuários ou grupos precisam de permissões para realizar cada tipo de operação. Isso evita problemas de segurança e garante que cada um faça o que é necessário!

![Imagem 2: Ao planejar o lançamento dessas operações, verifique se os usuários estão devidamente treinados e familiarizados com os…](https://ajuda.sankhya.com.br/hc/article_attachments/32723224602391) Ao planejar o lançamento dessas operações, verifique se os usuários estão devidamente treinados e familiarizados com os processos, minimizando erros.
