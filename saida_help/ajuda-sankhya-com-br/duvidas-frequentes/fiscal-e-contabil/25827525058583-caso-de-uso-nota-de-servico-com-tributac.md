---
id: "25827525058583"
titulo: "Caso de Uso - Nota de Serviço, com tributação de ISS onde a cidade de prestação é diferente do contratante e prestador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25827525058583-Caso-de-Uso-Nota-de-Servi%C3%A7o-com-tributa%C3%A7%C3%A3o-de-ISS-onde-a-cidade-de-presta%C3%A7%C3%A3o-%C3%A9-diferente-do-contratante-e-prestador"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:44:13Z"
rotulos: ["ISS", "Configuração", "Cidades", "Impostos", "Prefeituras", "NFS-e"]
---

# Caso de Uso - Nota de Serviço, com tributação de ISS onde a cidade de prestação é diferente do contratante e prestador

Acesse a tela **"Empresa"** (Caminho: Comercial » Preferências » Empresa) e verifique se o campo **"ISS"** está marcado como **'Tributado'.** Caso não esteja, faça a marcação:

![Imagem 1: Acesse a tela "Empresa" (Caminho: Comercial » Preferências » Empresa) e verifique se o campo "ISS" está marcado como…](https://ajuda.sankhya.com.br/hc/article_attachments/25910456520727)

Em seguida, acesse a tela **"Serviço"** (Caminho: Configurações » Cadastros » Produtos » Serviço) e marque o campo **"Tem ISS"** como **"Tributado"**:

![Imagem 2: Em seguida, acesse a tela "Serviço" (Caminho: Configurações » Cadastros » Produtos » Serviço) e marque o campo "Tem…](https://ajuda.sankhya.com.br/hc/article_attachments/25910456524311)

Realizadas essas configurações básicas, observe o caso no qual a Cidade onde o serviço foi prestado é diferente da cidade da empresa que contratou o serviço e da cidade do prestador do serviço.

Neste exemplo, o parâmetro **"CIDISSCNAEEMP"** estará **desligado** no primeiro momento. Assim não será necessário configurar nas preferências da empresa, na aba **"CNAE Empresa"**.

Voltado ao exemplo, a cidade da empresa que comprou o serviço é Uberlândia-MG:

![Imagem 3: Voltado ao exemplo, a cidade da empresa que comprou o serviço é Uberlândia-MG:](https://ajuda.sankhya.com.br/hc/article_attachments/25910426628375)

A cidade do prestador é Uberaba-MG:

![Imagem 4: A cidade do prestador é Uberaba-MG:](https://ajuda.sankhya.com.br/hc/article_attachments/25910456535831)

E a cidade de prestação é Araguari-MG.

Para a cidade de Uberlândia-MG, foi configurada uma alíquota de 10%, na qual em um processo simples, a retenção ocorreria nela:

![Imagem 5: Para a cidade de Uberlândia-MG, foi configurada uma alíquota de 10%, na qual em um processo simples, a retenção…](https://ajuda.sankhya.com.br/hc/article_attachments/25910426639127)

Veja o resultado no cenário com retenção simples (cidade do contratante):

![Imagem 6: Veja o resultado no cenário com retenção simples (cidade do contratante):](https://ajuda.sankhya.com.br/hc/article_attachments/25910426642967)

Ao lançar a nota de compra, a principal configuração que temos que nos atentar é no campo **"Cidade"** do cabeçalho da nota, pois há outro campo que se chama **"Cidade de Prestação do Serviço:"** que pode causar confusão devido ao seu nome.

Veja agora o que acontece à nota quando preenchemos o campo **"Cidade"** do cabeçalho:

![Imagem 7: Veja agora o que acontece à nota quando preenchemos o campo "Cidade" do cabeçalho:](https://ajuda.sankhya.com.br/hc/article_attachments/25910426645655)

![Imagem 8: Veja agora o que acontece à nota quando preenchemos o campo "Cidade" do cabeçalho:](https://ajuda.sankhya.com.br/hc/article_attachments/25910456552599)

Pode-se notar que a "Triangulação" da tributação ocorreu com sucesso.

Um adendo sobre o parâmetro **"CIDISSCNAEEMP",**  quando ele estiver ligado será demandada a configuração da aba **"CNAE Empresa",** de forma que deve-se definir onde de fato será a tributação para o Serviço e é preciso trabalhar vinculando o cadastro do serviço o CNAE do serviço.

![Imagem 9: Um adendo sobre o parâmetro " CIDISSCNAEEMP", quando ele estiver ligado será demandada a configuração da aba "CNAE…](https://ajuda.sankhya.com.br/hc/article_attachments/25910456555159)

![Imagem 10: Um adendo sobre o parâmetro " CIDISSCNAEEMP", quando ele estiver ligado será demandada a configuração da aba "CNAE…](https://ajuda.sankhya.com.br/hc/article_attachments/25910426654743)
