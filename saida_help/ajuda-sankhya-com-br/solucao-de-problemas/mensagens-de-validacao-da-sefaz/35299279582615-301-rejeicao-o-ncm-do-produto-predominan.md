---
id: "35299279582615"
titulo: "301 Rejeição: O NCM do produto predominante da carga lotação deve ser informado - MDF-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35299279582615-301-Rejei%C3%A7%C3%A3o-O-NCM-do-produto-predominante-da-carga-lota%C3%A7%C3%A3o-deve-ser-informado-MDF-e"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:25:35Z"
rotulos: ["ERROMDFE", "MDF-e", "SEFAZ", "Transporte", "NCM", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Prestador de Serviço de Transporte (tpEmit=1)", "Viagens de Transporte (MDF-e)", "Transportador com CT-e Globalizado (tpEmit=3)", "301 Rejeição", "Rejeição 301", "O NCM do produto predominante da carga lotação deve ser informado", "Tipo de Emitente (tpEmit)", "Modal for rodoviário", "Transportador Próprio (tpEmit=2) que informou o tipo de transportador (tpTransp)", "MDF-e tiver apenas um documento fiscal (DF-e) no grupo infDoc", "tpEmit", "infDoc", "Documentos Eletrônicos"]
---

# 301 Rejeição: O NCM do produto predominante da carga lotação deve ser informado - MDF-e

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/35299279573527) **MENSAGEM:**

301 Rejeição: O NCM do produto predominante da carga lotação deve ser informado

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/35299279574551)SOLUÇÃO:**

**(1)** Acesse a tela de **"Viagens de Transporte (MDF-e)"** (Comercial » Rotinas » Viagens de Transporte (MDF-e)), em seguida, abra a viagem que está sendo apresentada a rejeição.

**(2)** Depois, na viagem em questão, vá até a aba **"MDF-e",** sub aba **"Produto Predominante"** e preencha as informações referente ao produto predominante que está sendo transportado.

![Imagem 3: (2) Depois, na viagem em questão, vá até a aba "MDF-e", sub aba "Produto Predominante" e preencha as informações…](https://ajuda.sankhya.com.br/hc/article_attachments/35299257550615)

**Após o preenchimento dessas informações, será gerado o grupo de TAGs <prodPred> no arquivo XML do MDF-e.**

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/35299257551895)CAUSA:**

A rejeição acontece se o campo NCM do grupo "produto predominante" (prodPred) não for informado nos casos em que:

- **Modal for rodoviário e o Tipo de Emitente (tpEmit) for:**
  - Prestador de Serviço de Transporte (tpEmit=1) ou
  - Transportador com CT-e Globalizado (tpEmit=3) ou
  - Transportador Próprio (tpEmit=2) que informou o tipo de transportador (tpTransp)
- E o **MDF-e tiver apenas um documento fiscal (DF-e) no grupo infDoc**

**(1)** Para **mais informações sobre os ajustes necessários para adequação à Nota Técnica 2025.001 v1.02** acesse o artigo: [**Nota Técnica 2025.001 v1.02 (MDF-e) - Guia de Referência.**](https://ajuda.sankhya.com.br/hc/pt-br/articles/35309948500503)
