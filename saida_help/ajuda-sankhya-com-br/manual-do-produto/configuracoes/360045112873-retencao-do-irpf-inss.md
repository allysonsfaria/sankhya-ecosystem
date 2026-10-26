---
id: "360045112873"
titulo: "Retenção do IRPF/INSS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112873-Reten%C3%A7%C3%A3o-do-IRPF-INSS"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-10-15T13:17:21Z"
rotulos: ["Configuração", "Parceiro", "Impostos", "TOP", "Financeiro", "Física", "INSS", "IRPF", "Jurídica", "Retenção", "Retenção do IRPF/INSS manual", "Procedimento de Retenção Retenção do IRPF/INSS"]
---

# Retenção do IRPF/INSS

As informações apresentadas abaixo, prestam a orientação necessária para que o sistema realize a retenção do IRPF/INSS, calculados por meio da Tabela Progressiva, de lançamentos de RPA e notas fiscais geradas na [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793). A saber:

| [Configurações para Retenção do IRPF/INSS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112873-Reten%C3%A7%C3%A3o-do-IRPF-INSS#configuraespararetenodoirpfinss-tabelaprogressiva-nacentraldecompras) |
| --- |
| [Retenção do IRPF/INSS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112873-Reten%C3%A7%C3%A3o-do-IRPF-INSS#retenodoirpfinss-tabelaprogressiva-nacentraldecompras) |

## Configurações para Retenção do IRPF/INSS

Na tela [Cadastro de Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114), para o Tipo de Movimento **"C-Compra"**, temos na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos) as seguintes marcações: 

[GIF animado: Imagem 1: Na tela Cadastro de Tipos de Operação - TOP , para o Tipo de Movimento "C-Compra" , temos na aba Impostos as seguintes…](https://ajuda.sankhya.com.br/hc/article_attachments/4409114045079)

Com a marcação **"Aplicar tabela de IRPF/INSS"** efetuada na TOP de Compra, o sistema usa os valores da tabela de IRPF/INSS nos lançamentos. É importante ressaltar que as marcações **"Tem IRF"** e **"Tem FUNRURAL/INSS"** também devem estar ativadas.

Ao lançar uma nota com a TOP que se enquadre nas características citadas acima, o sistema irá verificar se o parceiro é pessoa Física; caso afirmativo, irá aplicar a Tabela de IRPF/INSS para retenção do IRPF/INSS.

Para que o sistema calcule a retenção do IRPF/INSS aplicando a tabela, é necessário cadastrar o Parceiro na aba [Parceiros sujeitos a tabela progressiva](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108293-Tabela-de-IRPF-INSS#abaparceirossujeitosatabelaprogressiva) presente na tela [Tabela de IRPF/INSS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108293-Tabela-de-IRPF-INSS).

Com a marcação **"Usar serviço p/ cálculo com tabela de IRPF/INSS"** efetuada, é determinado o serviço que será considerado para realização do cálculo juntamente à tabela de IRPF/INSS. Ao lançar um serviço na Central para fins de cálculo de INSS e IRF, serão respeitadas as configurações do serviço na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o#abaimpostos) do [Cadastro de Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553). Neste caso, os campos do Cadastro de Serviços que o sistema irá analisar são:

- **Tem INSS;**
- **% Red.Base INSS;**
- **Tem IRF;**
- **% Red.Base IRF**.

**Nota:** se a marcação **Usar serviço p/ cálculo com tabela de IRPF/INSS** não estiver efetuada, o sistema não irá considerar os campos citados acima.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112873-Reten%C3%A7%C3%A3o-do-IRPF-INSS#top)

## Retenção do IRPF/INSS

Nesta seção, você configura as regras para que o sistema realize o cálculo e a retenção automática do Imposto de Renda Pessoa Física (IRPF) e do INSS nas suas operações.

> **Atenção:** As configurações descritas nesta rotina aplicam-se **exclusivamente** ao cálculo de IRPF e INSS. Elas não são válidas para o cálculo do Funrural. Caso você precise configurar o Funrural para um Produtor Rural, deve utilizar as parametrizações específicas de comercialização rural disponíveis nos cadastros de Parceiros e Produtos.

- Efetuando o lançamento de uma nota com a TOP cujo Tipo de movimento é C - Compras, e realizando a marcação Aplicar Tabela de IRPF/INSS, o sistema irá verificar se o parceiro da nota é pessoa Física; caso seja, será aplicada a Tabela de IRPF/INSS para retenção do IRPF e INSS;
- Para a base de cálculo do IRPF e INSS, será considerado o valor do serviço;
- Porém, se a marcação Usar Serviço para cálculo da Tabela de IRPF/INSS? estiver assinalada, será analisado o Serviço, na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o#abaimpostos), os seguintes campos:

**-** **Tem INSS:** Irá calcular o INSS; e para isso verificará se há redução conforme consta percentual no campo **"% Red.Base INSS"**;

**-** **Tem IRF:** Será calculado o IRPF; e para isso verificará se existe redução conforme consta percentual no campo **"% Red.Base IRF"**.

Se existir redução de 15% por exemplo para INSS, e o valor do serviço for R$ 10.000,00 - então a Base de Cálculo do INSS para aplicação da Tabela Progressiva será de R$ 8.500,00.

O mesmo acontecerá para o IRPF, e após encontrado este valor de R$ 8.500,00 – para o IRPF será aplicado os cálculos da Tabela Progressiva, com suas deduções, conforme cálculos já existentes para o Financeiro.

- As bases serão cumulativas conforme data de movimento, como é atualmente dentro do Financeiro. Se existe mais de um documento lançado no próprio mês, este será acumulado com os outros de origem Estoque ou Financeiro.
- O valor do desdobramento Financeiro será o valor líquido, já deduzido os valores de IRPF e INSS; ou seja, será o valor a ser pago ao prestador de serviços. Os valores do IRPF e INSS irão popular as tabelas TGFFIN\_VLRIRF e TGFFIN\_VLRINSS, respectivamente.
- Se a TOP utilizada no lançamento estiver com a marcação Aplicar Tabela de IRPF/INSS assinalada, porém o parceiro for pessoa Jurídica, o sistema irá realizar os cálculos normais de retenção do IRPF e INSS, conforme alíquotas configuradas no Serviço ou em [Outros Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o#abaoutrosimpostos); não aplicando a Tabela Progressiva.
- O cálculo do ISS continuará obedecendo as regras atuais; estas não são alteradas com o comportamento mencionado até aqui.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112873-Reten%C3%A7%C3%A3o-do-IRPF-INSS#top)

![Imagem 2: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16747022864919) Acesse também:

[Tabela de IRPF/INSS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108293-Tabela-de-IRPF-INSS) (rotina ligada à [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira)).
