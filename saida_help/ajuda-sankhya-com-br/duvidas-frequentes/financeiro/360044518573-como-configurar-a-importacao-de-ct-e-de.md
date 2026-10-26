---
id: "360044518573"
titulo: "Como configurar a Importação de CT-e de terceiros com ICMS?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044518573-Como-configurar-a-Importa%C3%A7%C3%A3o-de-CT-e-de-terceiros-com-ICMS"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-07-22T15:56:01Z"
rotulos: ["CT-e", "Configuração", "Importação", "ICMS", "TOP", "Financeiro", "Importação de CT-E de terceiros", "Criar TOP específica", "Configurar preferências"]
---

# Como configurar a Importação de CT-e de terceiros com ICMS?

(1)** Abaixo listamos as configurações necessárias para esta Importação**

![Imagem 1: Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/article_attachments/16831451948183) Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

Crie uma TOP com Tipo de Movimento: 'I-Financeiro'

Modelo de Documento: 57 ou 8 para Tipo de Operação no Portal de Importação de XML ou Modelo de Documento: 67 para Tipo de Operação CT-e OS.

![Imagem 2: Modelo de Documento: 57 ou 8 para Tipo de Operação no Portal de Importação de XML ou Modelo de Documento: 67 para Tipo…](https://ajuda.sankhya.com.br/hc/article_attachments/14661190430743)

As atualizações de Tipo de Livro / Tipo de ICMS/ CFOP's / Modelo de documento (Livro Fiscal) ficam a critério do contador da empresa para selecionar a melhor opção.

![Imagem 3: As atualizações de Tipo de Livro / Tipo de ICMS/ CFOP's / Modelo de documento (Livro Fiscal) ficam a critério do…](https://ajuda.sankhya.com.br/hc/article_attachments/14661212071319)

![Imagem 4: As atualizações de Tipo de Livro / Tipo de ICMS/ CFOP's / Modelo de documento (Livro Fiscal) ficam a critério do…](https://ajuda.sankhya.com.br/hc/article_attachments/14661253847959)

![Imagem 5: Acesse: Comercial » Rotinas » Portal de importação de XML](https://ajuda.sankhya.com.br/hc/article_attachments/16831461282199) Acesse: Comercial » Rotinas » Portal de importação de XML

Botão Outras Opções...» Preferencias para importar CT-e

Aba: **"CT-e de Terceiros"**

Preencha devidamente os principais campos obrigatórios e os demais que forem necessário.

![Imagem 6: Preencha devidamente os principais campos obrigatórios e os demais que forem necessário.](https://ajuda.sankhya.com.br/hc/article_attachments/14661311026455)

![Imagem 7: Acesse: Financeiro » Rotinas » Movimentação Financeira](https://ajuda.sankhya.com.br/hc/article_attachments/16831451950615) Acesse: Financeiro » Rotinas » Movimentação Financeira

Ao importar o CT-e será gerado um financeiro na tela de **"Movimentação Financeira"** contendo todas as informações do CT-e (chave, CST, valores). Caso algum campo não apareça, basta colocá-lo como disponível na grade.

**![Imagem 8: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16831461283863) OBSERVAÇÃO:**

Caso as alíquotas de ICMS não sejam sejam puxadas automaticamente, podem ser informadas na aba **"Geral"** do financeiro gerado, nos campos **"Base ICMS"**  e **"%ICMS"**.

Ao informar os campos e confirmar a alteração, automaticamente é calculado o campo **"Vlr ICMS",** da aba Geral.

![Imagem 9: Ao informar os campos e confirmar a alteração, automaticamente é calculado o campo " Vlr ICMS", da aba Geral .](https://ajuda.sankhya.com.br/hc/article_attachments/14661338846231)

Os valores apresentados nesses campos devem ser levados para a Apuracão de ICMS, por conta da marcação de Atualização dos Livros Fiscais da TOP de Lançamento do titulo.

**(1)Campos de ICMS no financeiro de CT-e:**

- **"Base ICMS"**
- **"%ICMS"**
- **"Vlr ICMS"**

Os campos indicados acima podem ser preenchidos no ato do lançamento do financeiro da CT-e ou derivar dos cálculos previamente configurado, quando o lançamento for da Central de Notas-Origem E-Estoque.
