---
id: "4402308533143"
titulo: "Rejeição: Informações dos tomadores é obrigatória para esta operação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4402308533143-Rejei%C3%A7%C3%A3o-Informa%C3%A7%C3%B5es-dos-tomadores-%C3%A9-obrigat%C3%B3ria-para-esta-opera%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Distribuição"
atualizado_em: "2026-07-22T15:24:22Z"
rotulos: ["ERROMDFE", "MDF-e", "Parceiro", "SEFAZ", "Transporte", "Informar CIOT ou Vale-Pedágio.", "Emitir MDF-e corretamente.", "Preencher tomador do serviço"]
---

# Rejeição: Informações dos tomadores é obrigatória para esta operação

**![Imagem 1: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16341977163927) CAUSA:**

Se modal Rodoviário e tipo emitente forem igual a Prestador de Serviço de Transporte (tpEmit = 1) e não estiverem preenchidos:

![Imagem 2: Responsável pela geração do CIOT;](https://ajuda.sankhya.com.br/hc/article_attachments/16341977167895) Responsável pela geração do CIOT;

Ou

![Imagem 3: Responsável pelo pagamento do Vale-Pedágio.](https://ajuda.sankhya.com.br/hc/article_attachments/16341963989143) Responsável pelo pagamento do Vale-Pedágio.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16341977171735) SOLUÇÃO:**

Essa rejeição será apresentada, se modal Rodoviário/Tipo de Prestador for Prestador de Serviço de Transporte  e **não estiver preenchido pelo menos um Tomador de Serviço** (infContratante);

![Imagem 5: Nesse caso, ou as informações de Vale Pedágio devem estar preenchidas (Tela "Viagens de Transporte" , Aba "MDF-e" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/16341977167895) Nesse caso, ou as informações de Vale Pedágio devem estar preenchidas  (Tela **"Viagens de Transporte"**, Aba **"MDF-e"**, Sub-Aba **"Vale Pedágio"**);

**Ou**

![Imagem 6: Verifique se o Cód. Parceiro Contratante' (Tela "Viagens de Transporte" , aba "MDF-e" , sub-aba "Contratante" ) está…](https://ajuda.sankhya.com.br/hc/article_attachments/16341963989143) Verifique se o Cód. Parceiro Contratante' (Tela **"Viagens de Transporte"**, aba **"MDF-e"**, sub-aba  **"Contratante"**) está preenchido;

- Após preenchê-lo com a informação do último parceiro que irá realizar a entrega, gere um novo lote;

![Imagem 7: Após preenchê-lo com a informação do último parceiro que irá realizar a entrega, gere um novo lote;](https://ajuda.sankhya.com.br/hc/article_attachments/15080030064279)
