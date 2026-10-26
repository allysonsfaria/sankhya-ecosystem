---
id: "18192351771415"
titulo: "CT-e emitido em ambiente de homologação com Razão Social do remetente diferente de CT-E EMITIDO EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/18192351771415-CT-e-emitido-em-ambiente-de-homologa%C3%A7%C3%A3o-com-Raz%C3%A3o-Social-do-remetente-diferente-de-CT-E-EMITIDO-EM-AMBIENTE-DE-HOMOLOGACAO-SEM-VALOR-FISCAL"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:52:42Z"
rotulos: ["CT-e", "XML", "SEFAZ", "Transporte", "CST e benefício fiscal", "Incompatibilidade SEFAZ", "Ajuste no cadastro", "Erro", "Documentos Eletrônicos"]
---

# CT-e emitido em ambiente de homologação com Razão Social do remetente diferente de CT-E EMITIDO EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18192351755287) **MENSAGEM:**

Rejeição 646: CT-e emitido em ambiente de homologação com Razão Social do remetente diferente de CT-E EMITIDO EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18192336709911)SOLUÇÃO:**

Deve-se alterar o Nome ou Razão Social do Remetente do CT-e e informar o trecho literal: " **CT-E EMITIDO EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL**". Veja a seguir o exemplo corrigido:

- No XML:

![Imagem 3: No XML:](https://ajuda.sankhya.com.br/hc/article_attachments/18192229737367)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18192290514711)CAUSA:**

Quando for emitido um CT-e em Homologação (tpAmb = 2) e o Remetente for informado com a Razão Social (xNome) diferente do trecho literal: “CT-E EMITIDO EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL”, será retornado a rejeição "646 - CT-e emitido em ambiente de homologação com Razão Social do remetente diferente de CT-E EMITIDO EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL".

 

Exemplo:

Foi emitido um CT-e em Homologação e o Remetente foi informado com a Razão Social "Oobj Tecnologia da Informação Ltda." Nessa situação, o CT-e será rejeitado pelo motivo 646.

- No XML:

![Imagem 5: No XML:](https://ajuda.sankhya.com.br/hc/article_attachments/18192333155735)

Veja validação da Sefaz:

![Imagem 6: Veja validação da Sefaz:](https://ajuda.sankhya.com.br/hc/article_attachments/18192335745175)
