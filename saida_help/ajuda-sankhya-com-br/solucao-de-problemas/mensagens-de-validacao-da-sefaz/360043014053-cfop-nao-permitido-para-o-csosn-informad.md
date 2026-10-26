---
id: "360043014053"
titulo: "CFOP não permitido para o CSOSN informado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043014053-CFOP-n%C3%A3o-permitido-para-o-CSOSN-informado"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:10:11Z"
rotulos: ["ERRONF", "#PUBLIFER", "#RevisadoClaudio", "CSOSN", "Configuração", "NF-e", "SEFAZ", "Impostos", "CFOP", "386", "386 - Rejeição: CFOP não permitido para o CSOSN informado.", "CSOSN e CFOP", "NFC-e com CSOSN e CFOP inválido"]
---

# CFOP não permitido para o CSOSN informado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16314633851799) MENSAGEM:**

386 - Rejeição: CFOP não permitido para o CSOSN informado.

(1)** Validação 1**

Para CSOSN igual à:

(2)** 102** - Tributada pelo Simples Nacional sem permissão de crédito;

(2)** 103** - Isenção do ICMS no Simples Nacional para faixa de receita bruta;

(2)** 300** - Imune;

(2)** 400** - Não tributada pelo Simples Nacional;

(2)** 900** - Outros (a critério da UF).

CFOP'S não poderão ser diferentes de: 5.101, 5.102, 5.103, 5.104 ou 5.115

(1)** Validação 2**

Para CSOSN igual à:

(2)** 500** - ICMS cobrado anteriormente por substituição tributária (substituído) ou por antecipação.

CFOP'S não poderão ser diferentes de: 5.404, 5.656 ou 5.667.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16314667107991) SOLUÇÃO:**

Conforme validações acima, será necessário que o **Contador da empresa** reporte qual será o CSOSN e o CFOP correto para o respectivo lançamento. Após sintonias, recomenda-se que o usuário certificado na utilização do sistema, proceda com os devidos ajustes cadastrais:

![Imagem 3: Para ajustes referente ao campo CSOSN ('Código de Situação da Operação' – Simples Nacional):](https://ajuda.sankhya.com.br/hc/article_attachments/16314633857943) Para ajustes referente ao campo **CSOSN** ('Código de Situação da Operação' – Simples Nacional):

 Tela **"[Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS)"**, aba **"Simples Nacional".**

![Imagem 4: Tela " Alíquotas de ICMS " , a ba "Simples Nacional".](https://ajuda.sankhya.com.br/hc/article_attachments/15661416115863)

No lançamento, essa informação poderá ser visualizada da seguinte forma: Linha do item » botão **"Outras Opções"** [...] » **"Consultar/alterar dados dos impostos do Item".**

![Imagem 5: Para ajustes referente ao CFOP: Código Fiscal de Operações e de Prestações, vinculado na tela " Tipos de Operação-TOP "…](https://ajuda.sankhya.com.br/hc/article_attachments/16314667110679) Para ajustes referente ao CFOP: Código Fiscal de Operações e de Prestações, vinculado na tela **"[Tipos de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"**, aba **"[Livro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal)"**. Atente-se ao fato do código CFOP ser transformado conforme informações específicas do cadastro do produto, tal como: ST, Usado como.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16314633859735) CAUSA:**

NFC-e com CSOSN=102, 103, 300, 400 ou 900 e CFOP diferente de 5.101, 5.102, 5.103, 5.104, 5.115 ou NFC-e com CSOSN=500 (ICMS cobrado anteriormente) e CFOP diferente de 5.405, 5.656, 5.667.
