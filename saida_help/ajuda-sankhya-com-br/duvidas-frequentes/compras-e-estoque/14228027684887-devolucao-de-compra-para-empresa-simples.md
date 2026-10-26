---
id: "14228027684887"
titulo: "Devolução de compra para empresa Simples Nacional "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14228027684887-Devolu%C3%A7%C3%A3o-de-compra-para-empresa-Simples-Nacional"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-07-22T14:59:07Z"
rotulos: ["Configuração", "Devolução de Compra", "Simples Nacional", "ICMS", "Impostos", "TOP", "Devolução", "Destaque de ICMS"]
---

# Devolução de compra para empresa Simples Nacional 

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16912304910103) **SITUAÇÃO:**

Quando uma empresa optante pelo Simples Nacional, realiza a emissão de uma devolução de compra para um parceiro que não é, e precisa que o sistema destaque o ICMS, existem duas opções de parametrização:

![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16912317408791)**SOLUÇÃO:**

![Imagem 3: Se a TOP de devolução utilizada pra emissão estiver configurada como 'Calcula e digita' :](https://ajuda.sankhya.com.br/hc/article_attachments/16912317410071) Se a TOP de devolução utilizada pra emissão estiver configurada como **'Calcula e digita'**:

Tela: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

Aba: **"Impostos"**

Opção **"Cálculo de ICMS, IPI e ISS":** 'Calcula e digita'

Nesse caso, o sistema realizará o calculo do imposto e buscará as informações do ICMS da tela: **"Alíquota de ICMS"**, aba **"Simples Nacional",** campo **"Código de Situação da Operação no Simples Nacional - CSOSN".** Porém, para que ocorra o destaque, a opção selecionada nesse campo deve ser **"900-Outros".**

**![Imagem 4: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16912304913687) IMPORTANTE:**

**(1)** O sistema utiliza as regras de alíquota para cálculo do imposto independente do tipo de movimento. Nesse caso, alterando a regra para '900-Outros', atente-se que essa regra é utilizada para outras emissões, como uma venda por exemplo, pois o imposto será destacado ao buscar a regra com esse CSOSN.

**(1)** O mais indicado, nessa situação, é criar uma regra de alíquota especifica para devolução com a exceção por TOP, por exemplo, e informar o CSOSN '900-Outros'.

![Imagem 5: (1) O mais indicado, nessa situação, é criar uma regra de alíquota especifica para devolução com a exceção por TOP, por…](https://ajuda.sankhya.com.br/hc/article_attachments/15137026261271)

![Imagem 6: Se a TOP de devolução utilizada pra emissão estiver configurada como "Não Calcula e digita" :](https://ajuda.sankhya.com.br/hc/article_attachments/16912317413911) Se a TOP de devolução utilizada pra emissão estiver configurada como **"Não Calcula e digita"**:

Tela: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

Aba: **"Impostos"**

Opção **"Cálculo de ICMS, IPI e ISS":**  Não Calcula e digita

Nesse caso, o sistema o sistema utilizará os impostos da origem, que é a compra emitida pelo fornecedor. Porém, como a emissão do fornecedor não possui o CSOSN e sim CST, o sistema não preencherá o campo CSON da central de compras, sendo necessário alterar manualmente para o '900-Outros'.

![Imagem 7: Nesse caso, o sistema o sistema utilizará os impostos da origem, que é a compra emitida pelo fornecedor. Porém, como a…](https://ajuda.sankhya.com.br/hc/article_attachments/15137011985687)

- Essa é a opção indicada para que a devolução seja um espelho da origem;
- Atualmente. de forma nativa no sistema, não há uma parametrização que automatize esse preenchimento.

**![Imagem 8: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16912304913687) IMPORTANTE:**

Orientamos realizar a parametrização em uma base de teste, para validação dos dados junto a contabilidade da empresa.
