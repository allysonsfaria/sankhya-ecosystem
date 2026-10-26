---
id: "360042641594"
titulo: "Dígito verificador da chave de acesso composta inválida"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042641594-D%C3%ADgito-verificador-da-chave-de-acesso-composta-inv%C3%A1lida"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:29Z"
rotulos: ["ERRONF", "#RevisadoGui", "ERROMDFE", "ERROCTE", "NF-e", "XML", "SEFAZ", "253", "Rejeição: dígito inválido", "Inutilizar e emitir nova NF-e", "Garantir formação correta", "Erro", "Documentos Eletrônicos", "Chave de Acesso"]
---

# Dígito verificador da chave de acesso composta inválida

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16081888513431) MENSAGEM:**

253-Rejeição: Digito Verificador da chave de acesso composta inválida.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16081899891351) SOLUÇÃO:**

Considere o Comportamento da Aplicação, conforme abaixo:

![Imagem 3: A chave de acesso é composta por diversos campos e o último dígito corresponde ao cálculo sobre os demais.](https://ajuda.sankhya.com.br/hc/article_attachments/16081899897495) A chave de acesso é composta por diversos campos e o último dígito corresponde ao cálculo sobre os demais.

![Imagem 4: Pode ocorrer o incidente quando o período da emissão foi 2018 e a tentativa de aprovação da NF-e for em 2019, com isso…](https://ajuda.sankhya.com.br/hc/article_attachments/16081888520727) Pode ocorrer o incidente quando o período da emissão foi 2018 e a tentativa de aprovação da NF-e for em 2019, com isso o DV (Digito do Verificador) fica inválido.

![Imagem 5: Considere inutilizar a numeração, excluir a nota e emitir uma nova NF-e.](https://ajuda.sankhya.com.br/hc/article_attachments/16081899902999) Considere inutilizar a numeração, excluir a nota e emitir uma nova NF-e.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16081899905303)CAUSA:**

Tendo em vista que a chave de acesso é composta por diversos campos e o último dígito corresponde ao cálculo sobre os demais, deve-se garantir que tanto a formação da chave de acesso quanto o cálculo do dígito verificar siga a especificação do manual do contribuinte.

A chave de acesso de um Documento Fiscal: NF-e, CT-e, NFC-e e MDF-e é formada pelas seguintes informações:

- cUF - Código da UF do emitente do Documento Fiscal;
- AAMM - Ano e Mês de emissão da NF-e;
- CNPJ - CNPJ do emitente;
- mod - Modelo do Documento Fiscal;
- serie - Série do Documento Fiscal;
- nNF - Número do Documento Fiscal;
- tpEmis – forma de emissão da NF-e;
- cNF - Código Numérico que compõe a Chave de Acesso;
- cDV - Dígito Verificador da Chave de Acesso.
