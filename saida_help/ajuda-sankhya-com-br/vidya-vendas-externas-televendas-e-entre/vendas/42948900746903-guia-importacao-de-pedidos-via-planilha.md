---
id: "42948900746903"
titulo: "Guia: Importação de Pedidos via Planilha (Force WEB)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42948900746903-Guia-Importa%C3%A7%C3%A3o-de-Pedidos-via-Planilha-Force-WEB"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Vendas"
atualizado_em: "2026-08-24T16:55:13Z"
rotulos: ["sync_hc", "vidya", "vidya_574138", "sync_hash_c7c38bfb71cc"]
---

# Guia: Importação de Pedidos via Planilha (Force WEB)

Esta nova funcionalidade permite que o vendedor envie múltiplos pedidos de uma só vez para o sistema, otimizando o tempo de lançamento e reduzindo o trabalho manual.

## 1. Preparando a Planilha Modelo

Para que o sistema entenda os dados, a planilha deve seguir um padrão específico:

![Imagem 1: Para que o sistema entenda os dados, a planilha deve seguir um padrão específico:](https://ajuda.sankhya.com.br/hc/article_attachments/42957329399319)

- **Agrupamento por Ordem de Compra:** O sistema identifica o que pertence a um mesmo pedido através do número da ordem de compra.
- **Linhas por Produto:** Cada produto deve ocupar uma linha individual na planilha.
- **Repetição de Dados:** Para produtos do mesmo pedido, você deve repetir as informações de Parceiro, Tipo de Negociação e TOP em cada linha.

## 2. Realizando a Importação

1. Clique no botão **"Importar Planilha"** no Portal de Vendas.
2. Na tela que abrir, você verá o histórico de importações anteriores. Clique no botão para **realizar novas importações**.
3. Selecione o arquivo da planilha no seu computador.
4. No campo de **Observação/Descrição**, insira uma referência para facilitar a identificação futura (ex: "Pedidos de Segunda-feira").
5. Clique em **Enviar** e aguarde o processamento.

## 3. Gestão de Erros e Correções

O sistema valida os dados em tempo real. Se houver algum erro, o Force WEB impedirá a entrada de dados inválidos para proteger a integridade do sistema.

![Imagem 2: O sistema valida os dados em tempo real. Se houver algum erro, o Force WEB impedirá a entrada de dados inválidos para…](https://ajuda.sankhya.com.br/hc/article_attachments/42957314192535)

- **Validação de Dados:** Se você inserir um código de empresa ou produto inexistente, o sistema acusará "Formato de dado inválido" imediatamente.
- **Regras de Negócio:** Erros também podem ocorrer se o parceiro estiver bloqueado, a TOP estiver inativa ou a empresa não estiver licenciada.
- **Como Corrigir:**

  1. Na tela de histórico, clique no ícone de aviso para ver o motivo do erro.
  2. Clique no botão de **Edição** (lápis) para corrigir a informação diretamente na tela, sem precisar subir a planilha de novo.
  3. Após corrigir (ex: alterando a empresa), salve e clique em **Confirmar** para tentar gerar o pedido novamente.

## 5. Finalização

Assim que o processamento terminar com sucesso, o sistema gerará um **número de pedido válido** no Portal de Vendas.

Você pode clicar no **ícone de detalhes do pedido** para visualizar todos os detalhes do pedido gerado, como produtos, valores e descontos aplicados.
