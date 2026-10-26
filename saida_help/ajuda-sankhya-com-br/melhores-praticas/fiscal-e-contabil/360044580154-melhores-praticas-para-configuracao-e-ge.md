---
id: "360044580154"
titulo: "Melhores Práticas para configuração e geração de ajuste automático para fins de Apuracão de IPI, registro E530 e E531 (Ajustes de IPI)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044580154-Melhores-Pr%C3%A1ticas-para-configura%C3%A7%C3%A3o-e-gera%C3%A7%C3%A3o-de-ajuste-autom%C3%A1tico-para-fins-de-Apurac%C3%A3o-de-IPI-registro-E530-e-E531-Ajustes-de-IPI"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:51:13Z"
rotulos: ["#RevisadoJR", "Configuração", "Fiscal", "IPI", "Impostos", "EFD", "Ajuste e credite o imposto com base reduzida", "Gere e verifique registros no EFD-Fiscal", "Configure parceiros produtos e ajustes no sistema"]
---

# Melhores Práticas para configuração e geração de ajuste automático para fins de Apuracão de IPI, registro E530 e E531 (Ajustes de IPI)

O Imposto sobre Produtos Industrializados, cuja sigla é IPI, é um imposto federal, sobre produtos industrializados no Brasil e está previsto no art. 153, IV, da Constituição Federal. Suas disposições estão descritas no Decreto nº 7.212, de 15 de junho de 2010, que regulamenta a cobrança, fiscalização, arrecadação e administração desse imposto. 

De acordo com o art. 227 desse mesmo decreto existem algumas situações onde o cálculo do imposto deve ser realizado utilizando uma base reduzida.

“Art. 227. Os estabelecimentos industriais, e os que lhes são equiparados, poderão, ainda, creditar-se do imposto relativo a matéria-prima, produto intermediário e material de embalagem, adquiridos de comerciante atacadista não contribuinte, calculado pelo adquirente, mediante aplicação da alíquota a que estiver sujeito o produto, sobre cinquenta por cento do seu valor, constante da respectiva nota fiscal (Decreto-Lei no 400, de 1968, art. 6o).”  

Para atender a legislação e se creditar desse valor seria necessário realizar o cálculo do imposto utilizando a redução sem que o mesmo seja apresentado na nota e posteriormente esse valor ser repassado para a apuração do mesmo como um ajuste. 

- **Vejamos as Configurações:**

![Imagem 1: Configurações » Cadastros » Parceiros](https://ajuda.sankhya.com.br/hc/article_attachments/19196715566359) Configurações » Cadastros » Parceiros

Aba: Fiscal
Campo: **Enquadro no Art. 227. para cálculo de IPI?: [marcado]**

![Imagem 2: Configurações » Cadastros » Produtos » Produtos](https://ajuda.sankhya.com.br/hc/article_attachments/19196751020951) Configurações » Cadastros » Produtos » Produtos

Aba: Geral
Campo: **Usado Como = ['Materia Prima']**

![Imagem 3: Livros Fiscais » Arquivos » Geração ICMS/IPI Os ajustes serão gerados ao executar a rotina 'Geração ICMS/IPI'; - Serão…](https://ajuda.sankhya.com.br/hc/article_attachments/19196751030039) Livros Fiscais » Arquivos » Geração ICMS/IPI

Os ajustes serão gerados ao executar a rotina 'Geração ICMS/IPI';
- Serão consideradas para o ajuste notas de entradas com origem estoque cujo o parceiro e o produto estejam devidamente configurados.

![Imagem 4: Livros Fiscais » Arquivos » Ajuste do IPI](https://ajuda.sankhya.com.br/hc/article_attachments/19196751031959) Livros Fiscais » Arquivos » Ajuste do IPI

Na tela 'Ajuste do IPI' os valores serão registrados por documento e item;
- Os ajustes também podem ser registrados manualmente.

![Imagem 5: Comercial » Preferências » Empresa](https://ajuda.sankhya.com.br/hc/article_attachments/19196715576471) Comercial » Preferências » Empresa

Aba: EFD-Escrituração Fiscal Digital
Tipo de Escrituração = EFD
Blocos e Registros  = Selecione o Bloco 'E'
Registros: **Marque para gerar os Registros E530 e E531** (Não possui os registros, vá para final deste artigo e saiba como inserir manual)

![Imagem 6: Executar a rotina na seguinte ordem: 6.1- Geração ICMS/IPI (Em: Livros Fiscais » Arquivos » Geração ICMS/IPI ) 6.2-…](https://ajuda.sankhya.com.br/hc/article_attachments/19196751042071) Executar a rotina na seguinte ordem:
     6.1- Geração ICMS/IPI [Em: Livros Fiscais » Arquivos » Geração ICMS/IPI ]
     6.2- Consultar as informações na tela 'Ajuste do IPI' [Em: Livros Fiscais » Arquivos » Ajuste do IPI ]
     6.3- Gerar o EFD-Fiscal [Em: Livros Fiscais » Conexão » EFD - Escrituração Fiscal Digital - ICMS/IPI ]

- **Vejamos os registros no Arquivo txt gerado do EFD-Fiscal, antes e depois da configuração.**

**Exemplo:**

**Registro gerado antes** da configuração:

|E500|0|01012019|31012019|
|E510|0000|49|321,00|0,00|0,00|
|E510|0000|99|600,00|0,00|0,00|
|E510|1101|49|44500,00|0,00|0,00|
|E510|3102|49|9425,32|0,00|0,00|
|E510|5152|99|290,00|0,00|0,00|
|E510|6551|99|300,00|300,00|15,00|
|E520|0,00|15,00|0,00|0,00|20,00|5,00|0,00|
|E530|1|20,00| 99|1|323458|Outros Créditos|

**Registro gerado após** a configuração:

|E500|0|01012019|31012019|
|E510|0000|49|321,00|0,00|0,00|
|E510|0000|99|600,00|0,00|0,00|
|E510|1101|00|10500,00|10000,00|500,00|
|E510|1101|49|44500,00|0,00|0,00|
|E510|3102|49|9425,32|0,00|0,00|
|E510|5152|99|290,00|0,00|0,00|
|E510|6551|99|300,00|300,00|15,00|
|E520|0,00|15,00|500,00|0,00|770,00|1255,00|0,00|
|E530|1|20,00| 99|1|323458|Outros Créditos|
**|E530|1|500,00| 99|3|112015|CRÉDITO IPI ART. 227|**
**|E531|000003518|55|||112015|28012019|8951|500,00|11111111111111111111111111111111111111111111|**
**|E530|1|250,00| 99|3|112626|CRÉDITO IPI ART. 227|**
**|E531|000003518|55|10||112626|28012019|8562|250,00|11111111111111111111111111111111111111111111|**

![Imagem 7: Como inserir os registros 'faltantes' de forma manual.](https://ajuda.sankhya.com.br/hc/article_attachments/19196751043095) Como inserir os registros 'faltantes' de forma manual.

7.1-Acesse: Comercial » Preferências » Empresa, aba:EFD-Escrituração Fiscal Digital

Tipo de Escrituração = **EFD** ou EFD-Contibuições.

Na sub-aba: Blocos e Registros, com apoio do [Guia Pratico](http://sped.rfb.gov.br/)

- Se precisar inserir um novo bloco, na Sub-aba: Blocos clique em (+), insira a letra do Bloco, sequencia, Descrição e marque 'Gerar Bloco
- Se precisar inserir um novo Registro dentro do bloco, na sub-aba: Registros, clique em (+), e digite a sigla do registro, descrição e marque 'Gerar Registro'
