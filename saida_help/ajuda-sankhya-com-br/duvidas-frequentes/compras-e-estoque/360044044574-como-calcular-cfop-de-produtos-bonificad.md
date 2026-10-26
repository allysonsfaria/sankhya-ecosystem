---
id: "360044044574"
titulo: "Como calcular CFOP de produtos bonificados, doação ou brinde e não bonificados na mesma nota"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044044574-Como-calcular-CFOP-de-produtos-bonificados-doa%C3%A7%C3%A3o-ou-brinde-e-n%C3%A3o-bonificados-na-mesma-nota"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-07-22T15:55:25Z"
rotulos: ["Produtos", "Configuração", "NF-e", "XML", "Impostos", "Bonificação", "CFOP", "#AGUARDANDOVALIDAÇÃO", "Configuração de CFOP para Bonificação"]
---

# Como calcular CFOP de produtos bonificados, doação ou brinde e não bonificados na mesma nota

![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18849225651863) **SOLUÇÃO:**

Para lançamento de notas no sistema, onde serão destacados CFOP'S de bonificação, doação ou brinde para determinados itens, o campo abaixo deverá ser configurado:

Se informar **100**no campo **"% Desc.Bonif."** (TGFITE.PERCDESCBONIF) a CFOP será alterada para:

- Entrada Dentro do Estado -> CFOP = 1910
- Entrada Fora do Estado -> CFOP = 2910
- Saída Dentro do Estado -> CFOP = 5910
- Saída Fora do Estado -> CFOP = 6910

 Para valores menor ou igual que 99,99% informado no campo "% Desc.Bonif.", o sistema irá manter a regra de cálculo atual do CFOP, de acordo com o que esteja configurado.

**Importante:**

Caso o produto esteja configurado na tela Cadastro de Produtos, aba Geral, com o campo "Usado como" selecionado com a opção "Brinde", é necessário preencher o campo %Desc. Bonif para garantir que o CFOP seja calculado corretamente.

Caso não localize o campo "% Desc.Bonif." no respectivo lançamento, adicione o mesmo através da grade de itens, na tela "Configurador de Layout da nota".

**Observação:**

Caso o parâmetro: **"DESCBONIF - Usa Desc.Bonificação?"** esteja **ligado** e a Nota Fiscal seja do tipo de Movimento de Vendas, com o preenchimento do campo: "% Desc.Bonif." informado o valor menor ou igual que 99,99%, o sistema além de converter o CFOP da operação para Bonificado, ainda aplicará o valor referente ao percentual da bonificação como Desconto no total da Nota.

E caso o movimento da TOP seja de Compras, mesmo com o parâmetro: **DESCBONIF - Usa Desc.Bonificação? ligado**, não será aplicado o desconto no total da NF, pois o sistema entende que o valor unitário do produto prevalecerá o que consta no XML importado ou o valor que foi digitado manualmente, fazendo assim apenas a conversão do CFOP Bonificado.
