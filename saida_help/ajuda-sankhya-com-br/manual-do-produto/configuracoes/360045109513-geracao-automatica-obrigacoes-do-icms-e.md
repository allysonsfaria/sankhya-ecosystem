---
id: "360045109513"
titulo: "Geração Automática - Obrigações do ICMS e ICMS ST a Recolher"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109513-Gera%C3%A7%C3%A3o-Autom%C3%A1tica-Obriga%C3%A7%C3%B5es-do-ICMS-e-ICMS-ST-a-Recolher"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:55:46Z"
rotulos: ["Configuração", "XML", "ICMS", "Geração de Lote GNRE", "GEROBGICMSSTAUT", "Obrigações de ICMS e ICMS ST a Recolher", "Geração Automática - Obrigações do ICMS e ICMS ST a Recolher manual", "GNRE", "Financeiro", "Automatização da Geração de Obrigações de ICMS e ICMS ST", "ICMS ST"]
---

# Geração Automática - Obrigações do ICMS e ICMS ST a Recolher

No sistema, é possível realizar uma alimentação automática da tela [Obrigações do ICMS e ICMS ST a Recolher](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116133) por meio de procedimentos realizados na tela [Geração de Lote GNRE](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115053). Observe:

Primeiramente, ligue o parâmetro **"Gera obrigações do ICMS e ICMS ST automaticamente. - GEROBGICMSSTAUT"**e após isso, na tela Geração de Lote GNRE, no botão **"Novo Lote"**, efetue uma busca pelos financeiros que deverão compor o XML:

![Imagem 1: Primeiramente, ligue o parâmetro "Gera obrigações do ICMS e ICMS ST automaticamente. - GEROBGICMSSTAUT" e após isso, na…](https://ajuda.sankhya.com.br/hc/article_attachments/4411316760087)

Ao clicar no referido botão o pop-up **"Gerar XML do Lote de GNRE"** será aberto:

![Imagem 2: Ao clicar no referido botão o pop-up "Gerar XML do Lote de GNRE" será aberto:](https://ajuda.sankhya.com.br/hc/article_attachments/4411316803351)

Após a geração do lote, o lançamento da obrigação de ICMS e ST só será realizado na tela Obrigações do ICMS e ICMS ST a Recolher nos impostos listados no campo **"Tipo Apuração"** quando o **"Status do lote"** for retornado como **"Lote processado com sucesso"**. Caso esse status seja apresentado com alguma pendência, erro de validação ou apenas de Lote enviado, o referido lançamento não será gerado.

![Imagem 3: Após a geração do lote, o lançamento da obrigação de ICMS e ST só será realizado na tela Obrigações do ICMS e ICMS ST a…](https://ajuda.sankhya.com.br/hc/article_attachments/12801072426391)

**Atenção Consultor Sankhya:** Na tela Geração de Lote GNRE é possível gerar o lote de financeiros que já possuam lote gerado. Nesse caso, novos registros serão gerados na tela Obrigações do ICMS e ICMS ST a Recolher. Não existe uma relação dos registros criados na TGFOIR com o lote gerado, logo não é possível excluir estes registros.

Dessa forma, caso seja gerado o lote de financeiros que já possuam lote gerado e possuam registros na TGFOIR, se desejado, a exclusão desses registros deverá ser feita manualmente na tela Obrigações do ICMS e ICMS ST a Recolher.
