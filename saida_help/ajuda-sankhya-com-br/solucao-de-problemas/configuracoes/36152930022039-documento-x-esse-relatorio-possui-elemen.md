---
id: "36152930022039"
titulo: "Documento X: Esse relatório possui elementos de banco de dados, portanto precisa ser autorizado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36152930022039-Documento-X-Esse-relat%C3%B3rio-possui-elementos-de-banco-de-dados-portanto-precisa-ser-autorizado"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:23:39Z"
rotulos: ["Configuração", "Impressão", "Relatórios", "NF-e", "Modelos de Nota Fiscal/Duplicatas/Boleto(s)", "TOP", "Tipos de Operação - TOP", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Imprimir pedido/nota", "'NF-e/NFC-e/CF-e", "Modelo de impressão de nota fiscal'", "Documento", "Squad Plataforma", "Documentos Eletrônicos"]
---

# Documento X: Esse relatório possui elementos de banco de dados, portanto precisa ser autorizado

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/36152930008087) **MENSAGEM:**

Documento 80229: Esse relatório possui elementos de banco de dados, portanto precisa ser autorizado

**SITUAÇÃO:**

Ao tentar imprimir um pedido/nota a mensagem de erro é apresentada:

![Imagem 2: Ao tentar imprimir um pedido/nota a mensagem de erro é apresentada:](https://p23.zdusercontent.com/attachment/9618168/ORGrgRAJVhi1F4HCPtf8yKRPW?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..xgHdQx9O6sTKxdLVCYN32Q.eWRLbFczUYLpZopZepBhs4RnqaHoTxBUnxVboEaQcoduFysX8CoMlCF5XD3By0VmHbiYOM1RYE-Bto5jQnMGTkOJfYgoYO7p6yQi6KRuIqYynXY6PVDw1oKBpjVq2P_MAMs3ssCqtpK7fH2x7bUPHWjd8c3QmFsfAwwRxU5Ew0lBY_QTrQ0fbOR4iZp2FtBuhYIsFopPzJCouzGupB2I2KOZzd6IwB7hc8IO-UudipuEo3_fkjQtv-h2IwlShpk8xv5XvVqmxbO32Cwh8eU_HUXA__-zONXLgPBzr1HCunL-i6xEToXTrAJ_R2wkvE9F.cSH2XsmnNmectyo9uGD0gw)

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/36152946476951)SOLUÇÃO:**

**(1)** Acesse a tela [**''Tipos de Operação - TOP''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

**(2)** Localize a ''TOP'**'** utilizada no processo.

**(3)** Em seguida, clique na aba **''NF-e/NFC-e/CF-e''** e localize no campo **''Modelo de impressão de nota fiscal''** o modelo atual utilizado no processo.

![Imagem 4: (3) Em seguida, clique na aba ''NF-e/NFC-e/CF-e'' e localize no campo ''Modelo de impressão de nota fiscal'' o modelo…](https://ajuda.sankhya.com.br/hc/article_attachments/36622276974999)

**(4)** Após verificar qual modelo está configurado na ''TOP'', acesse a tela [**''Modelos de Nota Fiscal/Duplicatas/Boleto(s)''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913-Modelos-de-Nota-Fiscal-Duplicatas-Boleto-s) ( Configurações » Avançado » Modelos de Nota Fiscal/Duplicatas/Boleto(s)).

**(5)** **Pesquise** pelo **código do modelo** encontrado no passo 3.

**(6)** Em seguida, na aba **''Geral'**' verifique qual relatório formatado está associado no campo **''Número do relatório modelo”**.

(Este é o relatório que requer autorização para permitir a impressão).

![Imagem 5: (Este é o relatório que requer autorização para permitir a impressão).](https://ajuda.sankhya.com.br/hc/article_attachments/36622276977047)![Imagem 6: (Este é o relatório que requer autorização para permitir a impressão).](https://ajuda.sankhya.com.br/hc/article_attachments/36152930009879)

**(7)** Após identificar qual relatório formatado está sendo utilizado, acesse a tela [**''Autorização de Customizações''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/21517622604567-Autoriza%C3%A7%C3%A3o-de-Customiza%C3%A7%C3%B5es) (Configurações » Avançado » Autorização de Customizações), e realize a liberação na aba **''Relatórios''**.

![Imagem 7: (7) Após identificar qual relatório formatado está sendo utilizado, acesse a tela ''Autorização de Customizações''…](https://ajuda.sankhya.com.br/hc/article_attachments/36622293242391)

**(8)** Feito a liberação será possível a impressão.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/36152946483863)CAUSA:**

A mensagem ocorre porque o relatório formatado utilizado pela TOP para impressão requer liberação na tela ''Autorização de Customizações''.

Sem essa liberação, o sistema impede a execução do relatório.
