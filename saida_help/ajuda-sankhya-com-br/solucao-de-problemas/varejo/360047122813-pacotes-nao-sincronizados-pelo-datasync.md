---
id: "360047122813"
titulo: "Pacotes não sincronizados pelo Datasync"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360047122813-Pacotes-n%C3%A3o-sincronizados-pelo-Datasync"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-07-22T15:32:16Z"
rotulos: ["Produtos", "Configuração", "WMS", "Fast Service", "avulsa", "Verifique pacotes pendentes no Console Datasync", "Corrija pacotes corrompidos ou ignore pendências", "Produto não localizado no Fast Service", "Erro", "Datasync"]
---

# Pacotes não sincronizados pelo Datasync

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16426738345623) SITUAÇÃO:**

Na tentativa de realizar uma venda de determinado produto incluído recentemente no W, através do Fast Service, o mesmo não é localizado. 

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16426738351255) SOLUÇÃO:**

![Imagem 3: Na máquina do caixa (onde o Fast está instalado), acesse no navegador o endereço do Console Datasync (o endereço…](https://ajuda.sankhya.com.br/hc/article_attachments/16426738355607) Na máquina do caixa (onde o Fast está instalado), acesse no navegador o endereço do Console Datasync (o endereço inicia-se com "localhost") seguido da porta (por exemplo: 8080).

![Imagem 4: Informe o usuário e senha:](https://ajuda.sankhya.com.br/hc/article_attachments/16426754065687) Informe o usuário e senha:

![Imagem 5: Informe o usuário e senha:](https://ajuda.sankhya.com.br/hc/user_images/ZdUrLv3VaCqKMNcU6zTIfA.png)

![Imagem 6: Selecione a aba Monitoramento , em seguida, clique na sub-aba Pacotes com pendências .](https://ajuda.sankhya.com.br/hc/article_attachments/16426754069015) Selecione a aba **Monitoramento**, em seguida, clique na sub-aba **Pacotes com pendências**.

![Imagem 7: Verifique se há pacotes listados como pendentes, em caso afirmativo, guarde a informação da coluna nó de origem .](https://ajuda.sankhya.com.br/hc/article_attachments/16426738363543) Verifique se há pacotes listados como pendentes, em caso afirmativo, guarde a informação da coluna **nó de origem**.

![Imagem 8: É provável que esse pacote em questão esteja corrompido, por isso não foi recepcionado pelo datasync da filial.](https://ajuda.sankhya.com.br/hc/article_attachments/16426738365847) É provável que esse pacote em questão esteja corrompido, por isso não foi recepcionado pelo datasync da filial.

![Imagem 9: Para solucionar a questão, existem duas alternativas:](https://ajuda.sankhya.com.br/hc/article_attachments/16426754077335) Para solucionar a questão, existem duas alternativas:

**(2)** Identifique o pacote que está corrompido no computador onde o Datasync está instalado na máquina da matriz, e insira o manualmente na pasta do Datasync da filial, esse procedimento fará que os pacotes pendentes sejam sincronizados

**(2)** Na hipótese do pacote estar corrompido também na matriz, a ação recomendada é  na aba Monitoramento, na sub-aba Pacotes com pendências, selecione cada um dos itens pendentes, clique no botão **"ignorar pendência"** e confirme. O ato de ignorar a pendência permitirá que o Datasync recepcione os demais pacotes que não estão corrompidos, o que acarretará no aparecimento do produto, pois os pacotes acumulados por pendências impede a correta sincronização do Datasync entre a matriz e filial.

Caso ainda apresente erro, entre em contato com o Service Desk.
