---
id: "7222003717527"
titulo: "Existe EPEC registrado para esta Série e Numero"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7222003717527-Existe-EPEC-registrado-para-esta-S%C3%A9rie-e-Numero"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-09-17T15:17:04Z"
rotulos: ["EPEC", "NF-e", "SEFAZ", "Contingência", "692", "Rejeição 692 por EPEC registrado", "Verifique cNF e consulte Service Desk", "EPEC registrado com mesmos dados", "Erro", "Artigo atualizado KCS", "Docs Eletrônicos - KCS", "Documentos Eletrônicos"]
---

# Existe EPEC registrado para esta Série e Numero

**Mensagem**

[692] Rejeição: Existe EPEC registrado para esta Série e Número

**Situação**

Esta rejeição ocorre ao tentar transmitir uma NF-e à SEFAZ após a emissão em **"Contingência EPEC"**. O erro indica que já existe um registro de EPEC para a mesma série e número da nota fiscal que está sendo transmitida, porém com dados divergentes entre o EPEC registrado e a NF-e que está sendo enviada.

**Solução**

Ao enviar uma NF-e em EPEC, antes que a Sefaz devolva o retorno do documento, pode ocorrer o reenvio da mesma NF-e, mas com o cNF (Código Numérico) diferente do primeiro envio. Como o cNF faz parte da Chave de Acesso, a divergência gera a rejeição.

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Verifique se houve **"alteração nos dados da nota"** após o envio do EPEC. Compare as informações da NF-e com os dados registrados no EPEC junto à SEFAZ.

**(2)** Caso tenha ocorrido alteração nos dados, será necessário **"anular o EPEC"** diretamente no portal da SEFAZ do seu estado.

**(3)** Após anular o EPEC, **"exclua a nota fiscal"** no sistema Sankhya (esta exclusão deve ser realizada pela equipe de tecnologia via banco de dados, devido ao vínculo com o EPEC).

**(4)"Gere novamente a nota fiscal"** com os dados corretos e transmita-a à SEFAZ.

Caso o problema persista, entre em contato com a equipe do Service Desk para análise técnica.

**Atenção**

Evite utilizar a mesma numeração para emissão normal e para contingência, pois isso causa conflitos e EPECs pendentes de Conciliação. Para mais informações, consulte: [Ambiente de Contingência EPEC bloqueado para o Emitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043102893-Status-de-retorno-142-motivo-Ambiente-de-Contingencia-EPEC-bloqueado-para-o-Emitente-Como-resolver-).

**Causa**

A rejeição ocorre quando, para uma NF-e (modelo 55) em contingência, já existe na SEFAZ um EPEC registrado com o mesmo número, série, modelo, CNPJ e UF.

- Divergência de dados (valores, produtos, impostos) após envio do EPEC.
- Reutilização de numeração.
- Falhas de sincronização sistema/SEFAZ.

**Regra de Validação da Sefaz:**

![Regra de Validação](https://www.oobj.com.br/bc/assets/Articles/830/RV692.PNG)
