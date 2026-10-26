---
id: "9783091692951"
titulo: "TOP proíbe impressão de Boleto/Duplicata"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9783091692951-TOP-pro%C3%ADbe-impress%C3%A3o-de-Boleto-Duplicata"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T15:06:11Z"
rotulos: ["Configuração", "Impressão", "Duplicata", "TOP", "Boleto", "Financeiro", "CORE_E01395", "Erro: TOP proíbe impressão.", "Solução: ajustar campo \"Imprime Pix/Boleto/Duplicata\".", "Causa: configuração incorreta na TOP."]
---

# TOP proíbe impressão de Boleto/Duplicata

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18883560913431) MENSAGEM:**

[CORE\_E01395] TOP proíbe impressão de Boleto/Duplicata.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18883560924439) SITUAÇÃO:**

Ao tentar imprimir o boleto de alguns lançamentos a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18883560938775)SOLUÇÃO:**

![Imagem 4: Acesse o cadastro do Tipo de Operação ( Comercial » Arquivo » Cadastros » Tipos de Operação - TOP ) e verifique a…](https://ajuda.sankhya.com.br/hc/article_attachments/18883567495703) Acesse o cadastro do **Tipo de Operação** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique a configuração do campo "Imprime PIX/Boleto/Duplicata", na aba "Impressão"

![Imagem 5: Acesse o cadastro do Tipo de Operação ( Comercial » Arquivo » Cadastros » Tipos de Operação - TOP ) e verifique a…](https://ajuda.sankhya.com.br/hc/article_attachments/9782968684183)

![Imagem 6: Por meio do campo "Imprimir Pix/Boleto/Duplicata" poderá ser emitido boleto ou duplicata após a impressão da nota…](https://ajuda.sankhya.com.br/hc/article_attachments/18883560954647) Por meio do campo **"Imprimir Pix/Boleto/Duplicata"** poderá ser emitido boleto ou duplicata após a impressão da nota fiscal. Para isso, configure também o Tipo de Negociação e a conta bancária.

![Imagem 7: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/18883560966807) **IMPORTANTE:**

Veja abaixo as opções de escolha presentes no campo **"Imprimir Pix/Boleto/Duplicata":**

- **Na confirmação:** será impresso quando efetuar a confirmação da nota, clicando no botão Confirmar.
- **Manual:** Se selecionada, a impressão será efetuada através do botão Imprimir, opção **"Imprimir Pix/Boleto/Duplicata"**.
- **Proibido:** Se selecionado, não será realizada a impressão. Nos Portais se solicitar a impressão do boleto/duplicata o sistema emite o aviso: **"Documento (Número da Nota): TOP proíbe impressão de Boleto/Duplicata."**

Se esta opção estiver como Proibido, os boletos/duplicatas poderão ser impressos pelo menu **"Financeiro » Relatórios » Impressão de Boleto(s)"**.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18883560976023)CAUSA:**

Ocorre quando a TOP não está configurada para permitir a impressão de **Pix/Boleto/Duplicata.**
