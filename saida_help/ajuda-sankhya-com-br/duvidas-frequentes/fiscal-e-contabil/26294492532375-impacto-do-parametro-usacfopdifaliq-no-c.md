---
id: "26294492532375"
titulo: "Impacto do parâmetro USACFOPDIFALIQ no Calculo DIFAL ( diferencial de alíquotas ) em notas de compras"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26294492532375-Impacto-do-par%C3%A2metro-USACFOPDIFALIQ-no-Calculo-DIFAL-diferencial-de-al%C3%ADquotas-em-notas-de-compras"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:42:38Z"
rotulos: ["Configuração", "DIFAL", "ICMS", "Impostos", "Nota Fiscal", "CFOP"]
---

# Impacto do parâmetro USACFOPDIFALIQ no Calculo DIFAL ( diferencial de alíquotas ) em notas de compras

Esse parâmetro foi criado para ter impacto **apenas** no lançamento na Central de Compras. Ou seja, quando salvamos o item na nota, o sistema vai analisar o parâmetro citado. Se ele estiver desligado, o sistema **não** validará a marcação de cálculo de diferencial, presente na tela de CFOP, e efetuará o cálculo seguinte apenas para as demais regras/configurações:

![Imagem 1: Esse parâmetro foi criado para ter impacto apenas no lançamento na Central de Compras. Ou seja, quando salvamos o item…](https://ajuda.sankhya.com.br/hc/article_attachments/26329801300375)

Porém, sabemos que o parâmetro **"MOMCALCDIFALIQ"** é crucial para o funcionamento da rotina de cálculo de diferencial nas compras e na tela **"Cadastro Livro ICMS/IPI"** (Caminho: Livros Fiscais » Arquivos » Cadastro Livro ICMS/IPI). Assim, quando temos uma situação na qual o parâmetro **"USACFOPDIFALIQ"** está **desligado** e a nota de compra foi lançada, o sistema procederá normalmente com o cálculo e apresentará o valor na tabela de impostos da nota. Entretanto, se o parâmetro MOMCALCDIFALIQ estiver com a opção de **"Na central e recálculo no livro",** o sistema precisa que no cadastro do CFOP esteja com o referido campo (print) marcado e, dessa forma, nos livros ficará sem o valor do imposto.

Para solucionar esse problema, trabalhe com o parâmetro MOMCALCDIFALIQ com a opção na central. Assim, o sistema levará apenas o valor que já está pronto na nota, para os livros fiscais.

Mais detalhes e configurações sobre a rotina, [CLIQUE AQUI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044465693-Configura%C3%A7%C3%B5es-necess%C3%A1rias-para-c%C3%A1lculo-do-Diferencial-de-Al%C3%ADquotas-autom%C3%A1tico-na-entrada-da-NF).
