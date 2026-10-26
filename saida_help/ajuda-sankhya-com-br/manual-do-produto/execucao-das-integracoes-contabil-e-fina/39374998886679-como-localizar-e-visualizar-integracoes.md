---
id: "39374998886679"
titulo: "Como localizar e visualizar integrações financeiras da folha de pagamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39374998886679-Como-localizar-e-visualizar-integra%C3%A7%C3%B5es-financeiras-da-folha-de-pagamento"
trilha: "Manual do Produto > Pessoas+ > Integração Contábil e Financeira > Execução das Integrações Contábil e Financeira"
atualizado_em: "2026-10-02T17:51:01Z"
rotulos: ["Configuração", "Movimentação Financeira", "Financeiro", "Folha de Pagamento", "Gerenciador de Folhas", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Como localizar e visualizar integrações financeiras da folha de pagamento

A integração financeira permite que os valores processados na folha de pagamento sejam transferidos automaticamente para o módulo financeiro do sistema. Este artigo orienta sobre como localizar essas integrações, identificar o número único financeiro (NUFIN) e solucionar problemas comuns durante o processo.

### Como localizar a integração financeira

Após realizar a integração financeira da folha de pagamento por meio da rotina: 'Gerenciador de folhas' **(Pessoal+ » Rotinas Folha » Gerenciador de Folhas), no link abaixo, veja como realizar este processo de integração:**

<https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610374-Integra%C3%A7%C3%A3o-Financeira>

Com a integração efetuada, utilize o **"DBExplorer"** (Configurações » Avançado » DBExplorer) para consultar o número único da integração através da seguinte query:

**SELECT \* FROM TFPBAS WHERE REFERENCIA = 'DD/MM/AAAA'**

![Imagem 1: SELECT * FROM TFPBAS WHERE REFERENCIA = 'DD/MM/AAAA'](https://ajuda.sankhya.com.br/hc/article_attachments/41246569960471)

Substitua **'DD/MM/AAAA'** pela data de referência da folha integrada e clique em 'executar'.

![Imagem 2: Substitua 'DD/MM/AAAA' pela data de referência da folha integrada e clique em 'executar'.](https://ajuda.sankhya.com.br/hc/article_attachments/41246569960983)

No resultado da consulta, localize o campo **"NUFIN"**

![Imagem 3: No resultado da consulta, localize o campo "NUFIN"](https://ajuda.sankhya.com.br/hc/article_attachments/41246569962903)

Ao pesquisar e aparecer o campo procurado, é necessário clicar em cima do mesmo visando que ele seja direcionado: 

![Imagem 4: Ao pesquisar e aparecer o campo procurado, é necessário clicar em cima do mesmo visando que ele seja direcionado:](https://ajuda.sankhya.com.br/hc/article_attachments/41246594284311)

O campo contém o número único da integração financeira.

![Imagem 5: O campo contém o número único da integração financeira.](https://ajuda.sankhya.com.br/hc/article_attachments/41246594288023)

Com esse número, acesse a tela **"Movimentação Financeira"** (Financeiro » Rotinas » Movimentação Financeira) e realize a consulta para conferir se a integração foi realizada corretamente.

![Imagem 6: Com esse número, acesse a tela "Movimentação Financeira" (Financeiro » Rotinas » Movimentação Financeira) e realize a…](https://ajuda.sankhya.com.br/hc/article_attachments/41246569965207)

###
