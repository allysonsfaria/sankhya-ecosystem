---
id: "4405506231703"
titulo: "Informações dos tomadores é obrigatória para esta operação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4405506231703-Informa%C3%A7%C3%B5es-dos-tomadores-%C3%A9-obrigat%C3%B3ria-para-esta-opera%C3%A7%C3%A3o"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T15:22:38Z"
rotulos: ["ERROMDFE", "MDF-e", "Parceiro", "CIOT", "Transporte", "Erro 578 - Dados dos tomadores obrigatórios", "Dados dos tomadores não preenchidos no MDF-e", "Preencher CIOT Vale pedágio e Contratantes", "Documentos Eletrônicos"]
---

# Informações dos tomadores é obrigatória para esta operação

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16369915894935) MENSAGEM:**

Rejeição 578 - Informações dos tomadores é obrigatória para esta operação. Saiba mais!

E não estiverem preenchidos os dados abaixo

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16369907239063) SOLUÇÃO:**

Para a resolução do incidente, informe uma das opções abaixo.

**(1)** O parceiro Responsável pela Geração do **CIOT (Código Identificador de Operação de Transporte)** na aba CIOT.

![Imagem 3: (1) O parceiro Responsável pela Geração do CIOT (Código Identificador de Operação de Transporte) na aba CIOT.](https://ajuda.sankhya.com.br/hc/article_attachments/4405506217879)

**(1)**O parceiro Responsável pelo pagamento do Vale pedágio, na aba **"Vale pedágio"**:

![Imagem 4: (1) O parceiro Responsável pelo pagamento do Vale pedágio, na aba "Vale pedágio" :](https://ajuda.sankhya.com.br/hc/article_attachments/4405494109079)

**(1)**Informe o parceiro  contratante proprietário do veículo na aba Contratantes.

![Imagem 5: (1) Informe o parceiro contratante proprietário do veículo na aba Contratantes.](https://ajuda.sankhya.com.br/hc/article_attachments/4405493988503)

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16369907247895) CAUSA:**

A rejeição ocorre quando é inserido no MDF-e **(Manifesto Eletrônico de Documento Fiscal)** de modal Rodoviário)o tipo do Emitente como:

- Prestador de Serviço de Transporte <**tpEmit=1>;**
- Conhecimento de Transporte Eletrônico globalizado **<tpEmit=3>;**
- Transportador Próprio que informou o Tipo de Transportador <**tpEmi=2>** (com tag tpTransp informada)

E não são preenchidos os dados acima.
