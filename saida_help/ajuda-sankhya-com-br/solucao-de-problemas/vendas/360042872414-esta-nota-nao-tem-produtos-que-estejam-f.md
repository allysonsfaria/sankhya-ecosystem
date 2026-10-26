---
id: "360042872414"
titulo: "Esta nota não tem produtos que estejam fora da promoção para poder dar desconto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042872414-Esta-nota-n%C3%A3o-tem-produtos-que-estejam-fora-da-promo%C3%A7%C3%A3o-para-poder-dar-desconto"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:05:17Z"
rotulos: ["#PUBLIFER", "CORE_E02362", "Produtos", "Configuração", "NF-e", "Desconto", "Preferências", "Nota sem produtos para desconto promocional", "Configuração do parâmetro não permite desconto no rodapé de notas com produtos em promoção", "Verificar e ajustar o parâmetro \"VALDESCMAX\""]
---

# Esta nota não tem produtos que estejam fora da promoção para poder dar desconto

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16108779284631) MENSAGEM:**

[CORE\_E02362] Esta nota não tem produtos que estejam fora da promoção para poder dar desconto.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16108779287063) SOLUÇÃO:**

Quando o parâmetro **"VALDESCMAX - Valida desconto máximo"** estiver definido com a opção "**VALIDA E NÃO ACEITA (EXCETO PROD. PROMOÇÃO)"** e o produto inserido no lançamento fizer parte de uma regra de **Desconto Promocional**, ao aplicar um desconto no rodapé da nota, esse não será permitido. Visto que não existirá no lançamento produtos para rateio deste desconto.

Dessa forma, avalie junto ao responsável pela definição/parametrização de desconto promocional em sua empresa, se a configuração do parâmetro encontra-se coerente com o processo. Em caso negativo, realize os devidos ajustes.

**(2)** Tela **"[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)"** (Caminho de acesso: Configurações » Avançado), Chave VALDESCMAX:

![Imagem 3: (2) Tela " Preferências " (Caminho de acesso: Configurações » Avançado), Chave VALDESCMAX :](https://ajuda.sankhya.com.br/hc/article_attachments/14532763472407)

Caso o parâmetro esteja adequado, o desconto aplicado no rodapé não será permitido, sendo necessário retirar esse valor de seu lançamento. Após esse ajuste, teste a confirmação da nota.

**![Imagem 4: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16108733547799) OBSERVAÇÃO:**

No cenário acima, o desconto no rodapé será permitido apenas se houver outros itens na nota, não vinculados a descontos promocionais, que permitam o rateio do desconto.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16108779297559) CAUSA:**

Quando o parâmetro VALDESCMAX estiver definido com a opção VALIDA E NÃO ACEITA (EXCETO PROD. PROMOÇÃO) e o produto inserido no lançamento fizer parte de uma regra de Desconto Promocional, ao aplicar um desconto no rodapé da nota, esse não será permitido.
