---
id: "360052120514"
titulo: "Programa não está preparado para juntar com Provisão Financeira diferentes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360052120514-Programa-n%C3%A3o-est%C3%A1-preparado-para-juntar-com-Provis%C3%A3o-Financeira-diferentes"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:29:26Z"
rotulos: ["#criadoroger", "Configuração", "Movimentação Financeira", "TOP", "Financeiro", "#AGUARDANDOVALIDAÇÃO", "Gerenciamento de Provisão Financeira em Pedidos", "Erro"]
---

# Programa não está preparado para juntar com Provisão Financeira diferentes

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/18603786441879) MENSAGEM**:

Programa não está preparado para juntar com Provisão Financeira diferentes.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18603786448919) CAUSA:**

Ocorre quando um documento de Pedido, foi criado, quando a TOP estava configurado para Gerar Provisão Financeira, e outro documento de Pedido de Venda, foi criado 'com mesma TOP', porem a TOP foi agora configurado para Não Gerar Provisão Financeira.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18603754907799) SOLUÇÃO:**

Para faturamento de mais de um documento de forma agrupada, é necessário que o campo **"Atualização do financeiro"** tenha sido "alimentado" com a mesma informação, para todos os documentos de origem envolvidos nesse faturamento.

Dessa forma faz-se necessário compreender qual documento está com essa informação "inconsistente" e efetuar o lançamento do documento novamente para que todos os pedidos possam ser faturados agrupados. Caso esse ajuste não deva ocorrer, recomenda-se faturá-los separadamente.

**Compreenda de que forma esse campo é preenchido:**

Acesse a tela **'Tipos de Operação - TOP'** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)

- Selecione a TOP utilizada;
- Aba: Geral
- Opção: **Atualização do financeiro**: [ Incluir / Provisionar]
  A alteração desta opção é histórica, então sempre houver alteração, se faz necessário lançar novo documento.
  ![Imagem 4: Opção: Atualização do financeiro : ( Incluir / Provisionar) A alteração desta opção é histórica, então sempre houver…](https://ajuda.sankhya.com.br/hc/article_attachments/360086922294)

**Exemplo**: Se na data 28/08/2020 14:13 a TOP estava configurado para Não Provisionar Financeiro, e for lançado um documento após essa data, essa informação/registro, será gravado em um campo próprio no banco de dados por questões de integridade. Mostrando assim que o documento foi gerado sem provisão.

Se ocorrer alteração do campo na TOP e efetuar o lançamento de um novo documento, esta informação/registro, será gravado novamente neste documento novo.

**Importante** lembrar que não é recomendado efetuar qualquer intervenção via banco de dados.
