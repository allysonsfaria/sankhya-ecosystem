---
id: "32614866107671"
titulo: "Escrituração de Frete de origem Financeira com CFOP inválido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32614866107671-Escritura%C3%A7%C3%A3o-de-Frete-de-origem-Financeira-com-CFOP-inv%C3%A1lido"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:30:55Z"
rotulos: ["CT-e", "Configuração", "Relatórios", "CFOP", "Estoque", "Financeiro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Escrituração de Frete de origem Financeira com CFOP inválido", "Lançamentos de \"Fretes\"", "origem financeira", "escriturados de forma indevida no \"Livro Fiscal\"", "não utilizando o CFOP correto"]
---

# Escrituração de Frete de origem Financeira com CFOP inválido

Lançamentos de **"Fretes"** com origem financeira estão sendo escriturados de forma indevida no **"Livro Fiscal"**, não utilizando o CFOP correto.

**CASO DE USO**

Ao gerar um lançamento financeiro de frete e, em seguida, escriturar este lançamento no **"Livro Fiscal"**, observa-se que o CFOP utilizado não corresponde ao esperado. No exemplo abaixo é utilizado o CFOP **"1353"** ao invés do **"2353"**. Além disso, as UFs não são preenchidas corretamente.

![Imagem 1: Ao gerar um lançamento financeiro de frete e, em seguida, escriturar este lançamento no "Livro Fiscal" , observa-se que…](https://ajuda.sankhya.com.br/hc/article_attachments/34121105641623)

**SOLUÇÃO**

Para corrigir o CFOP e garantir o correto preenchimento das UFs, siga o passo a passo:

**(1)** Acesse a tela **"Movimentação Financeira"** (Financeiro » Rotinas » Movimentação Financeira).

**(2)** Na aba **"Informações Fiscais"**, preencha corretamente os campos fiscais necessários para o lançamento de frete.

![Imagem 2: (2) Na aba "Informações Fiscais" , preencha corretamente os campos fiscais necessários para o lançamento de frete.](https://ajuda.sankhya.com.br/hc/article_attachments/34121105642903)

**(3)** Após o correto preenchimento, gere novamente o **"Livro Fiscal"** e verifique se o CFOP e as UFs foram preenchidos conforme esperado.

![Imagem 3: (3) Após o correto preenchimento, gere novamente o "Livro Fiscal" e verifique se o CFOP e as UFs foram preenchidos…](https://ajuda.sankhya.com.br/hc/article_attachments/34121105644823)![Imagem 4: (3) Após o correto preenchimento, gere novamente o "Livro Fiscal" e verifique se o CFOP e as UFs foram preenchidos…](https://ajuda.sankhya.com.br/attachments/token/ctojkCHwmGG0zm1W8MV6uPzo6/?name=image.png)

**(4)** Para lançamentos com origem **"Estoque"**, insira os campos **"Cód. CID. Início CT-E"** e **"Cód. CID. Fim CT-E"** no layout da nota, pela tela **"Configurador de Layout da Nota"** (Comercial » Configuração » Configurador de Layout da Nota).

**CAUSA**

Os campos **"Cód. CID. Início CT-E"** e **"Cód. CID. Fim CT-E"** não estavam devidamente configurados nos lançamentos, ocasionando o uso incorreto do CFOP e o não preenchimento das UFs no **"Livro Fiscal"**.
