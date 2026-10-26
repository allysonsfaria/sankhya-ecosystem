---
id: "34935562996119"
titulo: "Título emitido não aparece na tela de Acompanhamento de Boletos – API. Saiba como resolver"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34935562996119-T%C3%ADtulo-emitido-n%C3%A3o-aparece-na-tela-de-Acompanhamento-de-Boletos-API-Saiba-como-resolver"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:26:25Z"
rotulos: ["Configuração", "Contas", "Movimentação Financeira", "Financeiro", "API", "não aparece", "tela de Acompanhamento de Boletos", "Job's", "Título emitido não aparece na tela de Acompanhamento de Boletos", "Título emitido", "Ocorrências de Remessa", "título via API"]
---

# Título emitido não aparece na tela de Acompanhamento de Boletos – API. Saiba como resolver

**SITUAÇÃO**

Após credenciar a conta como **API**, foi emitido um título, porém ele **não aparece na tela de "Acompanhamento de Boletos – API"**.

**SOLUÇÃO**

**(1)**  **Verifique os Job's responsáveis pela rotina:**

Acesse a tela **"Controle de Job's"** (Configurações » Avançado » Controle de Jobs)

- Confirme se os seguintes Jobs existem na base:

  - **10044** – Responsável pela remessa bancária e envio dos títulos ao banco. Também é responsável por levar os títulos presentes na tabela **TGFRAF** para a **TGFHBA**.
  - **10057** – Responsável pela baixa automática dos títulos liquidados. Só é executado se houver uma conta credenciada, se a opção de credenciamento da conta é **"Baixa Automática"** e se houverem títulos na TGFHBA com o status = ‘E’.
  - **10062** – Responsável por popular o PIX Copia e Cola no campo **"emvpix"** da **TGFFIN**, que reflete no campo **"Pix Copia e Cola"** na **"Movimentação Financeira"**.

**Caso os Jobs não existam, verifique se o parâmetro abaixo está preenchido.**

**SERVERHOSTSCHED** – **Servidor para executar schedule**

- Se estiver preenchido, **limpe o valor e reinicie o servidor**.

**(2)**  **Valide as ocorrências da conta**

- Acesse a tela **"Ocorrências de Remessa"** (Financeiro » EDI Bancário » Ocorrências de Remessa)
- Confirme se a conta configurada como **API** consta corretamente, com todos os códigos e campos preenchidos conforme o modelo esperado (veja print de exemplo).

![Imagem 1: Confirme se a conta configurada como API consta corretamente, com todos os códigos e campos preenchidos conforme o…](https://ajuda.sankhya.com.br/hc/article_attachments/34935600196503)

**(3)**  **Verifique os requisitos para envio do título via API**

 **Importante:** Para que um título seja **enviado através da API**, ele deve atender às seguintes condições:

- Ser um **título de receita**;
- Não ser **provisão** e não estar **baixado**;
- Os campos **Nosso Número**, **Linha Digitável** e **Código de Barras**, na aba **"Cobrança"** da **"Movimentação Financeira"**, devem estar preenchidos;
- A **Data de Negociação** deve ser **igual ou posterior** à data de registro da conta como API.

Execute o **SELECT** abaixo e consulte o campo `DTREGCONTA` para identificar a data que a conta em questão foi credenciada como API:

```
SELECT CODCTABCOINT,IDAPIBANCO,STATUSAPI,DTREGCONTA,IDSEQBOL FROM TSICTA
WHERE STATUSAPI = 'S' AND IDAPIBANCO IS NOT NULL
```

Ao credenciar a conta, caso já existam títulos vinculados a ela e **em aberto no banco**, a API irá **atualizar automaticamente o status desses títulos** na tela de **"Acompanhamento de Boletos – API"**.

**CAUSA**

Ocorre quando as configurações não estão compatíveis com os requisitos necessários para o envio de títulos pela API do banco.
