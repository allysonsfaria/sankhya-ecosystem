---
id: "4411152539287"
titulo: "Alterações da Sefaz para o cálculo  do Difal - Rejeição 815"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4411152539287-Altera%C3%A7%C3%B5es-da-Sefaz-para-o-c%C3%A1lculo-do-Difal-Rejei%C3%A7%C3%A3o-815"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T15:21:11Z"
rotulos: ["Configuração", "NF-e", "DIFAL", "SEFAZ", "Impostos", "Erro"]
---

# Alterações da Sefaz para o cálculo  do Difal - Rejeição 815

#### Imagem 1: Introdução Introdução

Os erros que ensejam essas rejeições, ocorrem devido as alterações da Sefaz para o calculo do Difal.  Segundo a NT 2015.003, o Cálculo do Difal era realizado seguindo o cálculo Por Dentro (de acordo com a determinação de cada UF) e com Base única. A seguir, um exemplo que demonstra a fórmula.

![Imagem 2: Os erros que ensejam essas rejeições, ocorrem devido as alterações da Sefaz para o calculo do Difal. Segundo a NT…](https://ajuda.sankhya.com.br/hc/article_attachments/15696276836375)

Caso fosse retornado uma fórmula diferente para o cálculo, retornaria a seguinte mensagem de erro:

| **815- Rejeição: Valor do ICMS Interestadual para UF de Destino difere do calculado [nItem: 999]**  **815- Rejeição: Erro não catalogado [nItem: 999]** |
| --- |

####

#### Imagem 3: Nova nota técnica/ NT 2020.005 Nova nota técnica/ NT 2020.005

Entrou em vigor no dia 04/10/2021 as regulamentações da NT 2020.005 que alteram novamente o cálculo do Difal, realizando o cálculo. Por dentro (de acordo com a determinação de cada UF) e com Base Dupla:

![Imagem 4: Entrou em vigor no dia 04/10/2021 as regulamentações da NT 2020.005 que alteram novamente o cálculo do Difal,…](https://ajuda.sankhya.com.br/hc/article_attachments/15696328125975)

####

#### Imagem 5: Solução Solução

Caso uma nota apresente a rejeição 815 mostrada acima, siga os seguintes passos para a correção:

**(1)** No **portal de Vendas** Localize a nota Rejeitada;

**(1)** Abra a nota na **Central de Vendas**;

**(1)** Na grade de itens, verifique no item da nota a alíquota de ICMS que cada item buscou:

![Imagem 6: (1) Na grade de itens, verifique no item da nota a alíquota de ICMS que cada item buscou:](https://ajuda.sankhya.com.br/hc/article_attachments/15696325043351)

**(1)** No cadastro de alíquota de ICMS, localize a alíquota do ICMS conforme a imagem anterior;

![Imagem 7: (1) No cadastro de alíquota de ICMS, localize a alíquota do ICMS conforme a imagem anterior;](https://ajuda.sankhya.com.br/hc/article_attachments/15696326620055)

**(1)** No cadastro de **“Alíquotas de ICMS”** verifique o campo **“Tipo de Calculo DIFAL”;**

![Imagem 8: (1) No cadastro de “Alíquotas de ICMS” verifique o campo “Tipo de Calculo DIFAL”;](https://ajuda.sankhya.com.br/hc/article_attachments/15696362544535)

Caso este campo esteja marcado com a Opção: **“4- Calculo do DIFAL com ICMS Destino Por dentro”.** Deve-se optar por outra fórmula para o calculo do Difal, pois esta opção não é mais aceita pela Sefaz.

![Imagem 9: Caso este campo esteja marcado com a Opção: “4- Calculo do DIFAL com ICMS Destino Por dentro”. Deve-se optar por outra…](https://ajuda.sankhya.com.br/hc/article_attachments/15696352332311)

**![Imagem 10: ATENÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16136809349143) ATENÇÃO:**

Qualquer validação da regra de cálculo deve ser feita pela contabilidade, caso nenhuma das opções atenda será necessário nos enviar a nova regra de cálculo.

Para mais informações sobre a correção, acesse o artigo: [815 - Rejeição: Valor do ICMS Interestadual para UF de Destino difere do calculado [nItem:999] (Valor Informado: XXX, Valor Calculado:XXX) (NT2015/003)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043050513-815-Rejei%C3%A7%C3%A3o-Valor-do-ICMS-Interestadual-para-UF-de-Destino-difere-do-calculado-nItem-999-Valor-Informado-XXX-Valor-Calculado-XXX-NT2015-003-Como-resolver-)
