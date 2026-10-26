---
id: "4403469655575"
titulo: "Status 656: Motivo: Consumo Indevido. [Consulte NT 2018.002 V1.OO]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4403469655575-Status-656-Motivo-Consumo-Indevido-Consulte-NT-2018-002-V1-OO"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-07-22T15:23:53Z"
rotulos: ["Requisições", "NF-e", "XML", "SEFAZ", "não apagar", "#AjustadoFer", "656", "Rejeição", "Rejeição por consumo indevido; aguarde liberação", "Excesso de requisições à Sefaz em curto período.", "Aguarde desbloqueio; se recorrente contate o Service Desk", "Erro"]
---

# Status 656: Motivo: Consumo Indevido. [Consulte NT 2018.002 V1.OO]

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16345063249303) MENSAGEM**:

[Status 656]: Motivo: Consumo Indevido. [Consulte NT 2018.002 V1.OO]

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16345063252759)SOLUÇÃO:**

Essa validação, trata-se de uma resposta da Sefaz, que ocorre quando o sistema executa (ou permite que o usuário execute) muitas requisições, pois existe um número limite de requisições por hora para cada WebService e se excedido será gerado o bloqueio.

Dessa forma, recomenda-se aguardar a liberação pela SEFAZ. Caso o problema se torne recorrente, acione o Service Desk Sankhya para análises detalhadas da quantidade de requisições enviadas, e possíveis tratativas de causa raiz.

**OBSERVAÇÃO:**

As principais rejeições que provocam o processamento em looping pelo emissor de notas fiscais são:

- Rejeição “383 – Item com CSOSN indevido”
- Rejeição “204 – Duplicidade de NF-e”
- Rejeição “778 – Informado NCM inexistente”
- Rejeição “766 – Item com CST Indevido”
- Rejeição “291 – Certificado de Assinatura – Data de Validade”
- Rejeição “539 – Duplicidade da NF-e, com diferença na Chave de Acesso”

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16345063258007)CAUSA:**

Este problema ocorre quando há um grande volume de consultas no servidor da Sefaz em um período de tempo muito curto. O limite é de 10 à 50 consultas por hora (dependendo do Estado) para um mesmo certificado. Quando isso ocorre a Sefaz bloqueia as consultas, retornando a Rejeição 656.

Isso pode ocorrer por diversos motivos, dentre eles:

**(1)** Quando o Sistema não tem sucesso na consulta e por algum motivo faz novas consultas num intervalo de tempo muito curto (looping), na tentativa de obter o retorno correto da Sefaz.

**(1)** Quando um volume elevados de documentos é processado num pequeno intervalo de tempo. Isso demandará um volume elevado de consultas, podendo ultrapassar o limite definido. Isso ocorre com muita frequência no Recebimento de DF-e's.

Após 50 bloqueios temporários, a empresa poderá receber um bloqueio definitivo, devendo entrar em contato com a Sefaz.
