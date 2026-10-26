---
id: "360043606894"
titulo: "Ocorreu um erro na compensação: Os financeiros estão vinculados a uma NF-e: 'X' não autorizada pela Sefaz"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043606894-Ocorreu-um-erro-na-compensa%C3%A7%C3%A3o-Os-financeiros-est%C3%A3o-vinculados-a-uma-NF-e-X-n%C3%A3o-autorizada-pela-Sefaz"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:01:21Z"
rotulos: ["Configuração", "NF-e", "Movimentação Financeira", "SEFAZ", "Financeiro", "ORA-20101", "Erro: NF-e não autorizada", "Verifique e ajuste o status para \"Aprovada\"", "Status NF-e diferente de \"Aprovada\" bloqueia a baixa", "Erro"]
---

# Ocorreu um erro na compensação: Os financeiros estão vinculados a uma NF-e: 'X' não autorizada pela Sefaz

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16171215358743) MENSAGEM:**

ORA-20101: Ocorreu um erro na compensação: Os financeiros estão vinculados a uma NF-e: 'X' não autorizada pela Sefaz. Não é possível baixá-los.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16171214150423) SOLUÇÃO:**

![Imagem 3: Localize na " Movimentação Financeira " o "Número Nota" correspondente ao título. Através do " Portal de Vendas" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/16171215365271) Localize na **"[Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753)"** o **"Número Nota"** correspondente ao título. Através do **"[Portal de Vendas"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654)**, selecionando a nota, busque pelo campo **"Status NF-e**."

![Imagem 4: Localize na " Movimentação Financeira " o "Número Nota" correspondente ao título. Através do " Portal de Vendas" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/14598558253719)

![Imagem 5: Caso não localize esse campo, o mesmo pode ser inserido através do botão "Configuração da Grade" :](https://ajuda.sankhya.com.br/hc/article_attachments/16171215367063) Caso não localize esse campo, o mesmo pode ser inserido através do botão **"Configuração da Grade"**:

![Imagem 6: Caso não localize esse campo, o mesmo pode ser inserido através do botão "Configuração da Grade" :](https://ajuda.sankhya.com.br/hc/article_attachments/14598593909143)

Busque pelo campo Status NF-e em **"Colunas disponíveis"** e arraste para **"Colunas selecionadas"**.

![Imagem 7: De acordo com o Status apresentado, proceda com as devidas tratativas. Somente será possível baixar tal título, diante…](https://ajuda.sankhya.com.br/hc/article_attachments/16171215370263) De acordo com o Status apresentado, proceda com as devidas tratativas. Somente será possível baixar tal título, diante do status **"Aprovada"**. 

Seguem orientações conforme status NF-e apresentado:

- Aguardando Autorização: [Nota Fiscal Eletrônica com status 'Aguardando Autorização'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043004833)
- Aguardando Correção: [Nota Fiscal Eletrônica com status 'Aguardando Correção'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043231613)
- Denegada: [Nota fiscal eletrônica Denegada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043229553)
- Enviada EPEC: [Nota Fiscal Eletrônica status 'Enviada em Ambiente de Contingência'(EPEC)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042626354)
- Pendente de Retorno: [Nota Fiscal Eletrônica com status 'Pendente de Retorno'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042507454)

**![Imagem 8: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16171214159383) OBSERVAÇÃO:**

Caso não se trate de uma NF-e, acesse o cadastro da TOP utilizada e revise junto ao implantador da empresa as configurações do campo **"NF-e"** da aba **Impressão**.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16171215385495) CAUSA:**

Ao tentar baixar um título vinculado a NF-e com Status NF-e diferente de **"Aprovada"** será apresentada a mensagem.
