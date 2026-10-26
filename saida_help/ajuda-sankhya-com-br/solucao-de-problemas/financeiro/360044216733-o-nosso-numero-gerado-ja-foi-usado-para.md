---
id: "360044216733"
titulo: "O nosso número gerado já foi usado para outro parceiro: nosso nro= xxxxxx, conta xx"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044216733-O-nosso-n%C3%BAmero-gerado-j%C3%A1-foi-usado-para-outro-parceiro-nosso-nro-xxxxxx-conta-xx"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:00:27Z"
rotulos: ["#RevisadoBraga", "Contas", "Movimentação Financeira", "Boleto", "Financeiro", "Cheque", "ORA-20101", "Procedimento de correção: Baixa Título Boleto", "Erro SQL: ORA-20101 ORA-06512 ORA-04088", "Causa do problema: Pagamento Cheque Nosso Número", "Erro", "Artigo atualizado KCS", "Financeiro - KCS"]
---

# O nosso número gerado já foi usado para outro parceiro: nosso nro= xxxxxx, conta xx

**MENSAGEM:**

General SQL error.
[ORA-20101]: O nosso número gerado já foi usado para outro parceiro: nosso nro= xxxxxx, conta xxx
[ORA-06512]: em 'SANKHYA.TRG\_INC\_UPD\_TGFFNNH\_TGFFIN', line 74
[ORA-04088]: erro durante a execução do gatilho 'SANKHYA.TRG\_INC\_UPD\_TGFFNNH\_TGFFIN'

**SITUAÇÃO:**

Ao acessar a baixa de um título utilizando a opção **CMC7**, ou ao realizar a impressão de um boleto, o sistema apresenta a mensagem informada.

**SOLUÇÃO:**

Para correção, siga os passos abaixo:

**(1)** Acesse: Financeiro » Rotinas » Movimentação Financeira

**(2)** Pesquise pelo titulo e verifique se o tipo de Título é 'Boleto'. Caso seja boleto e o pagamento seja feito com cheque, limpe as informações dos campos:

**"Nosso Número":**
**"Linha Dig. Receb":**
**"Cód. Barras Receb":**

Proceda com a baixa com Cheque.

Caso o Tipo de Título seja Cheque e o pagamento seja feito com cheque, informe os dados do Cheque no ato da baixa.

**(3)** Caso seja o Tipo de titulo 'Boleto' e o pagamento Boleto também, verifique no cadastro da Conta Bancaria (Caminho de acesso: Configurações » Cadastros » Bancários » Contas, aba: Intercâmbio Eletrônico de Dados(EDI), se no campo "**Último boleto**" contém o valor do último número de boleto, para que o próximo número esteja disponível e não se repita, **ajuste caso seja necessário.**

![Imagem 1: (3) Caso seja o Tipo de titulo 'Boleto' e o pagamento Boleto também, verifique no cadastro da Conta Bancaria (Caminho…](https://ajuda.sankhya.com.br/hc/article_attachments/42080069612567)

**CAUSA:**

Ocorre quando o Tipo de Titulo do registro financeiro é **boleto**e foi gerado Nosso Número, porém o cliente não liquidou o pagamento pelo banco e resolveu pagar com Cheque.
