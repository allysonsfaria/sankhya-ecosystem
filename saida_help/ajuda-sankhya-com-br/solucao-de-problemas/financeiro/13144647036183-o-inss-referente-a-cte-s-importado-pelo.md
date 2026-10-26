---
id: "13144647036183"
titulo: "O INSS referente a CTE-s importado pelo  Portal de importação de XML não foi para a Reinf"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/13144647036183-O-INSS-referente-a-CTE-s-importado-pelo-Portal-de-importa%C3%A7%C3%A3o-de-XML-n%C3%A3o-foi-para-a-Reinf"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T15:00:23Z"
rotulos: ["CT-e", "Configuração", "Movimentação Financeira", "XML", "Importação", "Impostos", "Configure \"Classificação Cessão M.d.Obra\" e ligue GERIMPINCREINF", "Verifique cadastro de impostos", "Informações em \"Movimentação Financeira\"", "Reinf"]
---

# O INSS referente a CTE-s importado pelo  Portal de importação de XML não foi para a Reinf

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17201137159191) SITUAÇÃO:**

O INSS referente a CTE-s importado pelo  Portal de importação de XML não foi para a Reinf.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17156644427927) SOLUÇÃO:**

![Imagem 3: O imposto precisa estar cadastrado na tela "Impostos", com as devidas configurações, para que as informações do imposto…](https://ajuda.sankhya.com.br/hc/article_attachments/17156644431895) O imposto precisa estar cadastrado na tela **"Impostos",** com as devidas configurações, para que as informações do imposto ao importar o XML da CT-e sejam apresentadas  no lançamento financeiro  na **"Movimentação Financeira"**, na opção  **"Outras opções"** em **"Outros impostos"**.

![Imagem 4: Em seguida, o campo "Classificação Cessão M.d.Obra", da aba "Impostos", no cadastro de "Serviço" deve estar…](https://ajuda.sankhya.com.br/hc/article_attachments/17156590476951) Em seguida, o campo **"Classificação Cessão M.d.Obra",** da aba **"Impostos",** no cadastro de **"Serviço"** deve estar configurado. Na tela **"Preferências",** parâmetro **GERIMPINCREINF:** ligado.

![Imagem 5: Em seguida, o campo "Classificação Cessão M.d.Obra", da aba "Impostos", no cadastro de "Serviço" deve estar…](https://ajuda.sankhya.com.br/hc/article_attachments/13162275448599)

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17156590483991) CAUSA:**

Se as informações no lançamento financeiro na tela Movimentação Financeira referente a Outros Impostos não estiverem informadas, o imposto correspondente não registra na tabela  'TGFIMF' (Imposto Financeiro) e, se o serviço não estiver informado no campo Classificação Cessão M.d.Obra, o lançamento não será apresentado no EFD- Reinf para gerar o envio.
