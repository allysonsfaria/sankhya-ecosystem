---
id: "360044618253"
titulo: "Erro 311 - A rubrica não é compatível com o tipo de regime previdenciário. Como resolver?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044618253-Erro-311-A-rubrica-n%C3%A3o-%C3%A9-compat%C3%ADvel-com-o-tipo-de-regime-previdenci%C3%A1rio-Como-resolver"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:34:14Z"
rotulos: ["eSocial", "Configuração Funcionários", "Central do eSocial", "Regime Previdenciário", "Definir regime previdenciário", "Transmissão do eSocial", "Erro"]
---

# Erro 311 - A rubrica não é compatível com o tipo de regime previdenciário. Como resolver?

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16996772735895) MENSAGEM:**

"401 - Conteúdo do evento inválido.Erro 311 - A rubrica não é compatível com o tipo de regime previdenciário.
Ação Sugerida: Verifique as compatibilidades das rubricas com o Regime Previdenciário do trabalhador. Elemento:/eSocial/evtRemun/dmDev/infoPerApur/ideEstabLot/remunPerApur/itensRemun[1]/codRubr [1] "

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16996749165975) SITUAÇÃO:**

Ao tentar transmitir o arquivo do eSocial, apresenta a rejeição abaixo:

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16996772741911)SOLUÇÃO:**

Para correção deste erro, siga os passos abaixo:

![Imagem 4: Acesse: MGEPessoal>>Arquivos>>Funcionários](https://ajuda.sankhya.com.br/hc/article_attachments/16996749170967) Acesse: MGEPessoal>>Arquivos>>Funcionários

Aba: **"Contrato"**

Marque uma das opções do campo: **"Regime Previdenciário"** e salve a alteração.

![Imagem 5: Acesse: MGEPessoal>>Avançado>>Central do eSocial.](https://ajuda.sankhya.com.br/hc/article_attachments/16996749174935) Acesse: MGEPessoal>>Avançado>>Central do eSocial.

Transmita novamente as obrigações.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16996772750871)CAUSA:**

Ocorre quando no cadastro do Funcionário não está marcada uma das opções do Regime Previdenciário.

**![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16996772752151) OBSERVAÇÃO:**

Evento: S-1200 - [Manual Orientação do eSocial](https://portal.esocial.gov.br/manuais/mos-v-2-4-02-publicada-cg.pdf)
