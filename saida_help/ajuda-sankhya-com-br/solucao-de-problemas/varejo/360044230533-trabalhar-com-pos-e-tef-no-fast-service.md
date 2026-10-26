---
id: "360044230533"
titulo: "Trabalhar com POS e TEF no Fast Service"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044230533-Trabalhar-com-POS-e-TEF-no-Fast-Service"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-07-22T15:59:38Z"
rotulos: ["Configuração", "Fast Service", "TEF", "Financeiro", "Tipos de Título", "POS", "Ative para padronizar descrições e limpar campos", "Preencha \"Forma pagamento TEF\" com a rede", "Não use \"Forma pagamento TEF\"; utilize Grupos"]
---

# Trabalhar com POS e TEF no Fast Service

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16199715203607) SITUAÇÃO:**

Como configurar Fast Service para trabalhar com POS e TEF?

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16199753611671) SOLUÇÃO:**

Considere o comportamento da aplicação, conforme abaixo:

**![Imagem 3: Solução TEF:](https://ajuda.sankhya.com.br/hc/article_attachments/16199753614231) Solução TEF:**

Acesse: Financeiro » Arquivos » Cadastros » Tipos de Título » Tipos de Título:

- Para o FastService acionar o gerenciador do TEF é necessário que no cadastro do tipo de título esteja com o campo **"Forma pagamento TEF"** preenchido:
- Forma pagamento TEF: com a REDE que aquele tipo de título pertence (REDECARD,CIELO,ETC..)

![Imagem 4: Forma pagamento TEF : com a REDE que aquele tipo de título pertence (REDECARD,CIELO,ETC..)](https://ajuda.sankhya.com.br/hc/article_attachments/14535475292695)

**![Imagem 5: Forma pagamento TEF : com a REDE que aquele tipo de título pertence (REDECARD,CIELO,ETC..)](https://ajuda.sankhya.com.br/hc/article_attachments/16199715215767) OBSERVAÇÃO:**

Lembrando que o cliente pode ter contrato com mais de uma rede tef e neste caso o sistema também irá enviar a descrição do cadastro de tipo de titulo até que o parâmetro: "**IMPDESCTEFHOMOL-Usar forma de pagamento padrão para TEF?"** seja ativado.

Com o parâmetro ligado, o Fast mandará para a ECF a descrição padrão CARTÃO para tipos de títulos com o campo Forma pagamento TEF: preenchido com uma das redes já cadastradas.

**![Imagem 6: Forma pagamento TEF : com a REDE que aquele tipo de título pertence (REDECARD,CIELO,ETC..)](https://ajuda.sankhya.com.br/hc/article_attachments/16199715217559) Solução POS:**

Neste caso a única diferença com o TEF é que o campo Forma pagamento TEF não poderá ser preenchido, uma vez que esta modalidade não é integrada ao sistema.

Sem este campo preenchido o sistema não irá chamar o TEF ao passar uma venda com este tipo de título.

**(2)**Acesse: Financeiro » Arquivos » Cadastros » Tipos de Título » Grupos de Tipos de Título

**![Imagem 7: Forma pagamento TEF : com a REDE que aquele tipo de título pertence (REDECARD,CIELO,ETC..)](https://ajuda.sankhya.com.br/hc/article_attachments/16199715215767) OBSERVAÇÃO:**

Uma forma mais ágil e fácil de trabalhar com POS e TEF é realizar o cadastro de um Grupo de tipo de títulos com o nome **Cartão** e vincular ao cadastro dos tipos de títulos para POS, assim seguindo a mesma descrição do TEF na ECF.

![Imagem 8: Forma pagamento TEF : com a REDE que aquele tipo de título pertence (REDECARD,CIELO,ETC..)](https://ajuda.sankhya.com.br/hc/article_attachments/12826606044439)

**![Imagem 9: Forma pagamento TEF : com a REDE que aquele tipo de título pertence (REDECARD,CIELO,ETC..)](https://ajuda.sankhya.com.br/hc/article_attachments/16199715215767) OBSERVAÇÃO:**

Caso o campo Forma de pagamento TEF esteja preenchido e a marcação Utiliza POS esteja marcada, para limpar o campo Forma de pagamento TEF desabilite o parâmetro "**HABFISCALPOSTIT";**

![Imagem 10: Forma pagamento TEF : com a REDE que aquele tipo de título pertence (REDECARD,CIELO,ETC..)](https://ajuda.sankhya.com.br/hc/article_attachments/7604169559063)

Para trabalhar com o parâmetro: "**USADESCGRUPOTIT-Utiliza descrição do grupo do tipo de titulo?"**, neste caso o sistema enviará à ECF a descrição do cadastro do grupo de tipos de títulos vinculado ao tipo de titulo em questão.

![Imagem 11: Para trabalhar com o parâmetro: " USADESCGRUPOTIT-Utiliza descrição do grupo do tipo de titulo?" , neste caso o sistema…](https://ajuda.sankhya.com.br/hc/article_attachments/14535500363927)

**![Imagem 12: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16199715215767) OBSERVAÇÃO:**

A possibilidade do parâmetro USADESCGRUPOTIT da descrição do grupo de tipo de título pode ser utilizada para padronizar qualquer tipo de título para varias ECF's.

**![Imagem 13: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16199715222167) CAUSA:**

Quando não se está configurado corretamente, as opções de TEF/POS nos Tipos de Titulo podem afetar a forma de apresentação das bandeiras.
