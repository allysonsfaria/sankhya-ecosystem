---
id: "9636542409111"
titulo: "Rejeição 435 NF-e Não pode ter indicativos do intermediador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9636542409111-Rejei%C3%A7%C3%A3o-435-NF-e-N%C3%A3o-pode-ter-indicativos-do-intermediador"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-08-14T19:04:31Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "TOP", "não apagar", "435", "Rejeição 435 NF-e: Correção do Indicador de Presença", "Erro"]
---

# Rejeição 435 NF-e Não pode ter indicativos do intermediador

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19581014247447) MENSAGEM:**

Rejeição 435 NF-e Não pode ter indicativos do intermediador.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19581014254487) SITUAÇÃO:**

Ao tentar confirmar uma NF-e de devolução a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19581014262935) CAUSA:**

Ocorre quando o campo **"Indicador de Presença para NF-e/NFC-e"** está preenchido incorretamente.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19581014264855) SOLUÇÃO:**

Defina no campo **"Indicador de Presença para NF-e/NFC-e"** (Caminho: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP, **aba "NF-e/NFC-e/CF-e"**) a forma como a operação envolvendo a NF-e ou a NFC-e foi realizada de acordo com as seguintes opções:

- 0 - Não se aplica (utilizado para Nota Fiscal complementar ou de ajuste, por exemplo);
- 1 - Operação presencial;
- 2 - Não presencial, internet;
- 3 - Não presencial, teleatendimento;
- 4 - NFC-e com entrega em domicílio;
- 5 - Presencial, fora do estabelecimento;
- 9 - Não presencial, outros.

De acordo com os modelos de documento utilizados, 55 (NF-e) ou 65 (NFC-e), possuímos determinados indicadores:

- Sendo uma **"NF-e (Modelo = 55)"**, são válidos os indicadores de presença 0,1,2,3ou9;
- No caso de uma **"NFC-e (Modelo = 65)"**, são válidos os indicadores de presença 1ou 4;
- Orientamos que a opção5 seja utilizada por vendedores ambulantes, para indicador de presença do comprador no estabelecimento.
