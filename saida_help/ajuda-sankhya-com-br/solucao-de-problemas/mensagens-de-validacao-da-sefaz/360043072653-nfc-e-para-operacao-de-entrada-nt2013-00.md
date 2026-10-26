---
id: "360043072653"
titulo: "NFC-e para operação de entrada (NT2013/005)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043072653-NFC-e-para-opera%C3%A7%C3%A3o-de-entrada-NT2013-005"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-08-08T17:40:05Z"
rotulos: ["ERRONF", "Configuração", "SEFAZ", "TOP", "CFOP", "706", "Rejeição 706: NFC-e para Operação de Entrada", "Erro"]
---

# NFC-e para operação de entrada (NT2013/005)

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16309491533079) **MENSAGEM:**

[706 - Rejeição]: NFC-e para operação de entrada (NT2013/005).

![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16309543555095) **SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse a tela Tipos de Operação - TOP ( Comercial » Arquivo » Cadastros » Tipos de Operação - TOP), a ba: "Livro…](https://ajuda.sankhya.com.br/hc/article_attachments/16309543556759) Acesse a tela [**Tipos de Operação - TOP**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP), aba: **"Livro Fiscal".**Verifique as CFOPs inseridas para **"Dentro/Fora do Estado":**

- CFOPs de Saída, iniciada por 5, 6, 7, para operações de Venda
- CFOPs de Entrada, iniciada por 1, 2, 3, para operações de Entrada

![Imagem 4: CFOPs de Entrada, iniciada por 1, 2, 3, para operações de Entrada](https://ajuda.sankhya.com.br/hc/article_attachments/14337825968151)

Em operações acobertadas por NFC-e é permitido apenas que sejam de saída (Venda). 
Para operações de entrada, opte pela emissão de uma NF-e de Terceiro (modelo 55).

![Imagem 5: Acesse a nota novamente, inutilize a numeração e fature novamente a NFC-e.](https://ajuda.sankhya.com.br/hc/article_attachments/16309491542551) Acesse a nota novamente, inutilize a numeração e fature novamente a NFC-e.

![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16309576618007) **CAUSA:**

Quando for emitida uma NFC-e e o Tipo da Operação de Entrada (TpNF = 0) será retornado a rejeição.

![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16309543572247) **OBSERVAÇÃO:**

([**NT2013/005**](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=%20tq7zNwy6jo=)) - Nota Técnica.
