---
id: "360044579994"
titulo: "Melhores práticas para Configuração e Ordenação EDI Comercial."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044579994-Melhores-pr%C3%A1ticas-para-Configura%C3%A7%C3%A3o-e-Ordena%C3%A7%C3%A3o-EDI-Comercial"
trilha: "Melhores Práticas > Configurações"
atualizado_em: "2026-07-22T15:51:18Z"
rotulos: ["#RevisadoGui", "Configuração", "XML", "EDI", "Configuração do EDI Comercial", "Documentos Eletrônicos", "Comercial"]
---

# Melhores práticas para Configuração e Ordenação EDI Comercial.

**Campos de configuração do EDI Comercial que influenciam na rotina:**

Comercial » EDI » Configuração Arquivo Remessa

Aba: Propriedades

**Ordenar Arquivo**: Quando marcada, o sistema ao concluir o processamento dos registros, irá ordenar as linhas processadas de acordo com o conteúdo definido no campo de sequência igual a 1.

Modelo Ficha (No SankhyaW esse campo é a **'Primeira coluna somente p/ ordenação'**): Quando marcada, o sistema retira o conteúdo do campo de sequencia igual a 1 do arquivo. Só faz sentido marcar a opção, caso o arquivo esteja sendo gerado de forma ordenada.

**Caso prático:**

Determinada empresa necessita gerar um EDI com as movimentações de venda, no arquivo devem ser geradas as notas seguidas dos seus respectivos itens.

Por padrão o sistema ao gerar o arquivo segue a hierarquia definida no layout, gerando sequencialmente no arquivo todos os registros retornados em cada nível.

**Configurando o EDI.**

Para que o arquivo seja gerado no formato acima, alem de marcar as opções 'Ordenar Arquivo e 'Modelo Ficha(Primeira coluna somente p/ ordenação), em cada nível foi criado um campo com a sequencia 1, tamanho de 10 posições, utilizando as seguintes expressões previstas na query do EDI.

**-08.01.000.00-HEADER**

**-08.01.001.00-CABEÇALHO**

**-08.01.002.00-ITENS**

**-08.02.000.00-TRAILLER**

**Observação**: Os valores demonstrados acima foram utilizados apenas para exemplificar a funcionalidade, os mesmos podem ser alterados de acordo com a demanda de cada arquivo gerado.

Configurados os campos em todos os níveis do layout o arquivo será gerado.

Quando marcamos a opção 'Ordenar o arquivo' em todos os níveis do EDI, as linhas do arquivo são classificadas segundo o conteúdo do campo de sequencia 1, sendo o arquivo gerado.

Quando marcamos a opção 'Modelo Ficha'(Primeira coluna somente p/ ordenação) em todos os níveis do EDI, o sistema retira todo o conteúdo gerado pelo campo de sequencia 1, gerando o arquivo no formato esperado, sequenciando as notas e seus itens.
