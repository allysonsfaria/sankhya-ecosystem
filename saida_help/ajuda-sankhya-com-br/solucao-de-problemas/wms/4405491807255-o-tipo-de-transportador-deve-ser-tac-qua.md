---
id: "4405491807255"
titulo: "O tipo de transportador deve ser TAC quando informado CPF do proprietário do veículo de tração"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4405491807255-O-tipo-de-transportador-deve-ser-TAC-quando-informado-CPF-do-propriet%C3%A1rio-do-ve%C3%ADculo-de-tra%C3%A7%C3%A3o"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T15:22:39Z"
rotulos: ["MDF-e", "Configuração", "SEFAZ", "Transporte", "#publicadoHyago", "Sistema atende NT 2021.001 e 2021.00", "Parâmetro \"GERATPTRANSPPF\" deve estar ligado", "Após ajustar gere um novo MDF-e", "Documentos Eletrônicos"]
---

# O tipo de transportador deve ser TAC quando informado CPF do proprietário do veículo de tração

Como é mostrado na OS 1777242, o sistema foi criado e planejado para atender a norma técnica NT 2021.001 e 2021.002, ficando nas versões 4.7 - 4.7b717 ou superior 4.8 - 4.8b386 ou superior. Desta forma, o parâmetro **"GERATPTRANSPPF"** deve estar ligado, de forma que  se o veículo não for próprio e o proprietário for pessoa física, o sistema irá gerar automaticamente a tag **tpTransp.** Caso o veículo seja de pessoa jurídica, buscará de acordo com a marcação do campo **'Transportadora de cargas'** das preferência da empresa

**![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/16369910049175) OBSERVAÇÃO:** Após ligar o parâmetro, gere um novo MDF-e.
