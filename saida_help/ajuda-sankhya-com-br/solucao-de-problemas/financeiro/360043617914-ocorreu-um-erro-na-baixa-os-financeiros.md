---
id: "360043617914"
titulo: "Ocorreu um erro na BAIXA: Os financeiros estão vinculados a uma NF-e 'X' não autorizada pela Sefaz"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043617914-Ocorreu-um-erro-na-BAIXA-Os-financeiros-est%C3%A3o-vinculados-a-uma-NF-e-X-n%C3%A3o-autorizada-pela-Sefaz"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:01:10Z"
rotulos: ["#PUBLIFER", "Configuração", "NF-e", "Movimentação Financeira", "SEFAZ", "Financeiro", "ORA-20101", "Títulos vinculados a NF-e não autorizada não são baixáveis", "Verifique e corrija o status da NF-e; só é possível baixar se \"Aprovada\"", "NF-e não \"Aprovada\" bloqueia a baixa do título", "Erro"]
---

# Ocorreu um erro na BAIXA: Os financeiros estão vinculados a uma NF-e 'X' não autorizada pela Sefaz

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16106466940439) MENSAGEM:**

ORA-20101: Ocorreu um erro na BAIXA: Os financeiros estão vinculados a uma NF-e 'X' não autorizada pela Sefaz. Não é possível baixá-los.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16106466942103) SOLUÇÃO:**

![Imagem 3: Localize na tela "Movimentação Financeira" o Número Nota correspondente ao título. Através da tela "Portal de Vendas" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/16106472368279) Localize na tela [**"Movimentação Financeira"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753) o Número Nota correspondente ao título. Através da tela [**"Portal de Vendas"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654), selecionando a nota, busque pelo campo **"Status NF-e"**.

![Imagem 4: Localize na tela "Movimentação Financeira" o Número Nota correspondente ao título. Através da tela "Portal de Vendas" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/14555254200855)

![Imagem 5: De acordo com o Status NF-e apresentado, proceda com as devidas tratativas. Somente será possível baixar tal título…](https://ajuda.sankhya.com.br/hc/article_attachments/16106466943383) De acordo com o Status NF-e apresentado, proceda com as devidas tratativas. Somente será possível baixar tal título diante do status **"APROVADA"**. 

Seguem orientações conforme status Nf-e apresentado:

- Aguardando Autorização: [Nota Fiscal Eletrônica com status 'Aguardando Autorização'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043004833)
- Enviada: [Nota Fiscal Eletrônica com status 'Enviada'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044128313)
- Denegada: [Saiba mais sobre nota fiscal eletrônica denegada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043229553)
- Enviada EPEC: [Nota Fiscal Eletrônica status 'Enviada em Ambiente de Contingência'(EPEC)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042626354)
- Pendente de Retorno: [Nota Fiscal Eletrônica com status 'Pendente de Retorno'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042507454)

**![Imagem 6: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16106466946199) OBSERVAÇÃO:**

Caso não se trate de uma nota fiscal eletrônica:

- Acesse o cadastro da TOP utilizada e revise junto ao implantador da empresa as configurações do campo **"NF-e",** da aba **Impressão;**
- Verifique a configuração do Tipo de Negociação e do Tipo de Título utilizado;
- Certifique-se que o Tipo de Título esteja corretamente configurado com base no parâmetro TIPTITCREDCLI, evitando inconsistências na validação.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16106466947095) CAUSA:**

Ao tentar baixar um título vinculado a nota fiscal eletrônica com Status NF-e diferente de Aprovada será apresentada a mensagem.
