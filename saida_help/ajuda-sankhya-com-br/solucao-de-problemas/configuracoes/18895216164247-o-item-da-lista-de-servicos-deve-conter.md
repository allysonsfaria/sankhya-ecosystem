---
id: "18895216164247"
titulo: "O item da lista de serviços deve conter 5 digitos com formatação (ex XX.YY, XX.YY)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/18895216164247-O-item-da-lista-de-servi%C3%A7os-deve-conter-5-digitos-com-formata%C3%A7%C3%A3o-ex-XX-YY-XX-YY"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:51:59Z"
rotulos: ["Configuração", "Cidades", "Prefeituras", "NFS-e", "Formatação Exigida para Item da Lista de Serviços", "Erro"]
---

# O item da lista de serviços deve conter 5 digitos com formatação (ex XX.YY, XX.YY)

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18895216150423) **MENSAGEM:**

O item da lista de serviços deve conter 5 digitos com formatação (ex XX.YY, XX.YY).

**![Imagem 2: O item da lista de serviços deve conter 5 digitos com formatação (ex XX.YY, XX.YY).](https://ajuda.sankhya.com.br/hc/article_attachments/18895187156503)CAUSA:**

Isso se da por exigência de algumas prefeituras por envio da informação do Item Lista Serviço nesse padrão.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18895163265559)SOLUÇÃO:**

A mensagem citada acima acontece quando a prefeitura usa em seu layout a tag "ItemListaServiço"  com o "ponto" (.) ou seja, 14.04 por exemplo, ao invés de 1404 no JSON, dessa forma e necessário ajusta o parâmetro **'Cds LC116 convert NFSe JSON (ibge-de:para;) - NFSECONVLC116'** com a seguinte configuração: "3301702-1405:14.05; com o seguinte padrão  (Códs LC116 convert NFSe JSON (ibge-de:para;) ou seja do padrão antigo para o novo.

Para as cidades que devem sair sem o ponto, tem que configurar o parâmetro: **'Cds LC116 convert NFSe JSON (ibge-de:para;) - NFSECONVLC116'** e o parâmetro **'Validar item LC116 na NFS-e? - VALIDLC116NFSE'** também deve estar ligado.
 
No exemplo do Serviço da lista 14.01 e município de Rio Verde - GO onde o código do IBGE = 3134202, caso tenha mais cidades separar por ponto e virgula;
 
![Imagem 4: Para as cidades que devem sair sem o ponto, tem que configurar o parâmetro: 'Cds LC116 convert NFSe JSON…](https://ajuda.sankhya.com.br/hc/article_attachments/19056842067863)
 

Verifique também no cadastro de cidades como está a opção Não formatar LC116: que deverá estar desmarcada conforme imagem abaixo.

![Imagem 5: Para as cidades que devem sair sem o ponto, tem que configurar o parâmetro: 'Cds LC116 convert NFSe JSON…](https://ajuda.sankhya.com.br/hc/article_attachments/19056801646231)
