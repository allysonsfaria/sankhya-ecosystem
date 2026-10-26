---
id: "21733329451287"
titulo: "Regras de cálculo do auxílio-creche"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/21733329451287-Regras-de-c%C3%A1lculo-do-aux%C3%ADlio-creche"
trilha: "Manual do Produto > Pessoas+ > Benefícios > Configurações de Benefícios"
atualizado_em: "2026-09-27T18:35:07Z"
rotulos: ["Configuração", "Eventos", "Funcionários", "CLT", "Folha de Pagamento", "Benefícios"]
---

# Regras de cálculo do auxílio-creche

O Auxílio Creche é um benefício regido pela Consolidação das Leis Trabalhistas (CLT).

Para conceder esse benefício no **Sankhya Om**, realize as seguintes configurações:

![Imagem 1: Primeiramente, na tela Tabela de Faixas , crie uma tabela para informar a quantidade de anos limite e os valores do…](https://ajuda.sankhya.com.br/hc/article_attachments/21733937366679) Primeiramente, na tela [Tabela de Faixas](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405167002519), crie uma tabela para informar a quantidade de anos limite e os valores do Auxílio Creche.

![Imagem 2: Primeiramente, na tela Tabela de Faixas , crie uma tabela para informar a quantidade de anos limite e os valores do…](https://ajuda.sankhya.com.br/hc/article_attachments/21733908157207)

Para a tabela de faixas de Auxílio Creche, o campo **"Limite da Faixa"** deve ser informado em quantidade de meses e não anos.

![Imagem 3: Em seguida, no cadastro do funcionário , acesse a aba Dependentes e na sub-aba Geral , habilite a marcação "Tem Auxílio…](https://ajuda.sankhya.com.br/hc/article_attachments/21734084541335) Em seguida, no [cadastro do funcionário](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639), acesse a aba [Dependentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639-Configura%C3%A7%C3%A3o-Funcion%C3%A1rios#AbaDependentes) e na sub-aba Geral, habilite a marcação **"Tem Auxílio Creche"**. O campo **"Data Limite do Auxílio Creche"** deve ser preenchido manualmente. Caso a marcação **"Não Apresentou Atestado"** esteja ativada, não é feito o cálculo de Auxílio Creche se utilizada a função padrão da Sankhya (FAUXCRECHE):

![Imagem 4: Em seguida, no cadastro do funcionário , acesse a aba Dependentes e na sub-aba Geral , habilite a marcação "Tem Auxílio…](https://ajuda.sankhya.com.br/hc/article_attachments/21734158698007)

![Imagem 5: Agora, na tela Fórmulas , adicione uma fórmula para o cálculo do Auxílio Creche utilizando a função FAUXCRECHE e o…](https://ajuda.sankhya.com.br/hc/article_attachments/21734394131863) Agora, na tela [Fórmulas](https://ajuda.sankhya.com.br/hc/pt-br/articles/13061392411287), adicione uma fórmula para o cálculo do Auxílio Creche utilizando a função FAUXCRECHE e o código da Tabela de Faixa criada previamente, conforme o exemplo abaixo:

   Código da Tabela de Faixa: 21

FAuxCreche(queFuncionario.CODEMP,queFuncionario.CODFUNC,**21**,&Refere,queFuncionario.TIPTAB)

![Imagem 6: FAuxCreche(queFuncionario.CODEMP,queFuncionario.CODFUNC, 21 ,&Refere,queFuncionario.TIPTAB)](https://ajuda.sankhya.com.br/hc/article_attachments/21734567831575)

![Imagem 7: Por fim, configure um Evento nomeado como Auxílio Creche e do "Tipo" de "Provento" , vinculando a Fórmula criada…](https://ajuda.sankhya.com.br/hc/article_attachments/21738164212247) Por fim, configure um [Evento](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767) nomeado como Auxílio Creche e do **"Tipo"** de **"Provento"**, vinculando a Fórmula criada previamente para cálculo e definindo como **"Regra em cálculo"** para a folha **"Normal"**:

![Imagem 8: Por fim, configure um Evento nomeado como Auxílio Creche e do "Tipo" de "Provento" , vinculando a Fórmula criada…](https://ajuda.sankhya.com.br/hc/article_attachments/21738179731991)

Assim, ao calcular a folha mensal do funcionário, o Auxílio Creche será considerado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/21733329451287-Regras-de-c%C3%A1lculo-do-aux%C3%ADlio-creche#top)
