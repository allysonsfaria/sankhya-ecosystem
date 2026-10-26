---
id: "360058162293"
titulo: "Relatório Razão analítico está sendo exportado em Excel com quebras de linhas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360058162293-Relat%C3%B3rio-Raz%C3%A3o-anal%C3%ADtico-est%C3%A1-sendo-exportado-em-Excel-com-quebras-de-linhas"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:27:16Z"
rotulos: ["Configuração", "Relatórios", "Movimentação Financeira", "Preferências", "não apagar", "Excel", "Ação: Ative o parâmetro em \"Preferências\" para evitar quebras.", "Problema: Relatório Razão analítico em Excel com quebras de linha.", "Solução: Parâmetro GERRELEXCSEMQUE controla quebras."]
---

# Relatório Razão analítico está sendo exportado em Excel com quebras de linhas

Recentemente foi realizada uma melhoria na usabilidade de lançamentos manuais, criando um novo arquivo (jrxml) para gerar os dados no formato de planilha.

Esse relatório foi criado como um facilitador para o usuário que necessitava manipular os dados direto na planilha. A ideia foi gerar os dados diretamente sem considerar as quebras que o relatório em PDF considerava.

Dessa forma, temos:

- Quem deseja utilizar o relatório em Excel da forma antiga, considerando as quebras conforme configuração da tela, deverá manter o parâmetro **GERRELEXCSEMQUE** **desligado**.
- Quem deseja **visualizar o relatório sem quebras, deverá ligar o parâmetro**;

![Imagem 1: Acesse a tela "Preferências" ('Configurações » Avançado » Preferências') e ligue o parâmetro citado:](https://ajuda.sankhya.com.br/hc/article_attachments/17269505167511) Acesse a tela **"Preferências"**  ('Configurações » Avançado » Preferências') e ligue o parâmetro citado:

- Chave **"GERRELEXCSEMQUE -** G**era relatório em excel sem considerar quebras"**.

![Imagem 2: Chave " GERRELEXCSEMQUE - G era relatório em excel sem considerar quebras" .](https://ajuda.sankhya.com.br/hc/article_attachments/13048954814487)

![Imagem 3: Feche a tela do relatório e abra novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/17269482266263) Feche a tela do relatório e abra novamente.
