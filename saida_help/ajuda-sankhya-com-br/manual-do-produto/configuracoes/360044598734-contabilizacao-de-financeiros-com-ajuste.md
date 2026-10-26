---
id: "360044598734"
titulo: "Contabilização de Financeiros com Ajuste ao Valor Presente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598734-Contabiliza%C3%A7%C3%A3o-de-Financeiros-com-Ajuste-ao-Valor-Presente"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:48:04Z"
rotulos: ["Configuração", "Contabilização de Financeiros com Ajuste ao Valor Presente", "Contabilização de Financeiros com Ajuste ao Valor Presente manual", "TOP", "Contabilização", "Financeiro", "Valor Presente"]
---

# Contabilização de Financeiros com Ajuste ao Valor Presente

O Conselho Federal de Contabilidade – CFC, através do Comitê de Pronunciamentos Contábeis - CPF tem o objetivo de adequar a nossa legislação às normas internacionais da contabilidade e determinou a adequação da contabilização de financeiros ajustada ao valor presente.

O Ajuste ao Valor Presente refere-se a todos aqueles elementos de longo prazo do ativo ou passivo ou de curto prazo, mas relevantes à entidade, que devem ser contabilizadas pelo seu valor presente, isso quer dizer que se retiram as parcelas dos juros do valor do financeiro conforme taxas de mercado.

Além da separação do valor principal dos juros na contabilização da receita/despesas/imobilizado, os valores constantes do realizável/exigível deverão inicialmente ser compostos apenas do valor principal (valor presente) e os juros em conta específica.  A contabilidade deverá ser capaz de periodicamente apropriar parcelas de juros ao realizável/exigível até que ao vencimento (ou antecipação) estes se igualem ao valor total da transação.

Essas questões influenciam diretamente na análise do balanço, principalmente ao analisarmos o **"Valor da Empresa"**, pois influenciam diretamente no ativo e passivo.

Para facilitar sua navegação nessa documentação, acesse os links abaixo:

[Configurações Necessárias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598734-Contabiliza%C3%A7%C3%A3o-de-Financeiros-com-Ajuste-ao-Valor-Presente#configura%C3%A7%C3%B5esnecess%C3%A1rias)                                            [Cálculo do Valor Presente](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598734-Contabiliza%C3%A7%C3%A3o-de-Financeiros-com-Ajuste-ao-Valor-Presente#c%C3%A1lculodovalorpresente)

[Contabilização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598734-Contabiliza%C3%A7%C3%A3o-de-Financeiros-com-Ajuste-ao-Valor-Presente#contabiliza%C3%A7%C3%A3o)                                                                   [Imobilizado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598734-Contabiliza%C3%A7%C3%A3o-de-Financeiros-com-Ajuste-ao-Valor-Presente#imobilizado)

---

#### Configurações Necessárias

Na tela [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral) você deve efetuar a marcação **"Ajusta Valor Presente"**.

![Imagem 1: Na tela Tipos de Título , aba Geral você deve efetuar a marcação "Ajusta Valor Presente" .](https://ajuda.sankhya.com.br/hc/article_attachments/4407180888983)

Informe o tipo de título valor presente ao [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o):

![Imagem 2: Informe o tipo de título valor presente ao Tipo de Negociação :](https://ajuda.sankhya.com.br/hc/article_attachments/4407194535447)

Após isso, na tela [Valores de Moedas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604754-Valores-de-Moedas), cadastre uma moeda do tipo **"Índice"** e na aba **"Cotação de Moeda"** insira os índices da Data do Movimento com o último dia de cada mês.

Na [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abafinanceiro), seção **"Ajuste Valor Presente"** é necessário inserir o **"Cód. Moeda Ajusta Valor Presente"** cadastrado anteriormente e indicar uma das opões abaixo no campo **"Ajusta Valor Presente"**:

- **Mensal:** O sistema realiza o calculo mês a mês entre a data de negociação e a data de vencimento; o juro é calculado e inserido na tabela TGFAVP.
- **Ajuste no Vencimento:** Será gravada uma única linha com a data de referência da parcela de juros igual ao vencimento do título.
- **Ajuste Anual:** Partindo da data de negociação, serão calculados os juros para cada competência mensal da mesma forma que no ajuste mensal porém, acumula-se cada conjunto de 12 meses gerando registro na TGFAVP com a soma do valor dos juros gravando como referência a última data.
- **Ajuste fim de exercício:** O processo é mesmo do Ajuste anual porém, calcula-se primeiro até o final do exercício (Ano) e a partir daí a cada 12 meses.

![Imagem 3: Ajuste fim de exercício : O processo é mesmo do Ajuste anual porém, calcula-se primeiro até o final do exercício (Ano)…](https://ajuda.sankhya.com.br/hc/article_attachments/4407180972311)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598734-Contabiliza%C3%A7%C3%A3o-de-Financeiros-com-Ajuste-ao-Valor-Presente#top)

#### Cálculo do Valor Presente

Após realizar as configurações acima, o sistema realiza o cálculo na inserção e/ou alteração do financeiro. Por exemplo:

Foram lançados os títulos;

| ``` Índices lançados ao final de cada mês: ``` |
| --- |

| **Data do movimento** | **Índice** |
| --- | --- |
| 31/12/2013 | 1,50 |
| 31/01/2014 | 2,00 |
| 28/02/2014 | 2,50 |
| 31/03/2014 | 3,00 |
| 30/04/2014 | 3,50 |
| 31/05/2014 | 4,00 |
| 30/06/2014 | 4,50 |

**Financeiro 1**

| ``` ![Imagem 4: Financeiro 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310682039191) ``` |
| --- |

| **Data de Negociação** | 10/03/2014 |
| --- | --- |
| **Data de Vencimento** | 09/04/2014 |
| **Valor de Desdobramento** | R$1.000,00 |
| **Valor Presente** | R$970,70 |
| **Juros Valor Presente** | R$29,30 |

| ``` Memória de cálculo – Tabela TGFAVP (Ajusta Valor Presente) ``` |
| --- |

| **Data de Referência** | **Índice** | **Juros Valor Presente** |
| --- | --- | --- |
| 31/03/2014 | 2,1 | 20,38 |
| 09/04/2014 | 0,9 | 8,92 |
| Juros Valor Presente | 13,17 |  |

**Financeiro 2**

| ``` ![Imagem 5: Financeiro 2](https://ajuda.sankhya.com.br/hc/article_attachments/42310682039703) ``` |
| --- |

| **Data de Negociação** | 10/03/2014 |
| --- | --- |
| **Data de Vencimento** | 09/05/2014 |
| **Valor de Desdobramento** | R$1.000,00 |
| **Valor Presente** | R$936,47 |
| **Juros Valor Presente** | R$63,53 |

| ``` Memória de cálculo – Tabela TGFAVP (Ajusta Valor Presente) ``` |
| --- |

| **Data de Referência** | **Índice** | **Juros Valor Presente** |
| --- | --- | --- |
| 31/03/2014 | 2,1 | 19,67 |
| 30/04/2014 | 3,5 | 33,47 |
| 05/09/2014 | 1,05 | 10,39 |
| Juros Valor Presente | 38,17 |  |

**Financeiro 3**

| ``` ![Imagem 6: Financeiro 3](https://ajuda.sankhya.com.br/hc/article_attachments/42310682040087) ``` |
| --- |

| **Data de Negociação** | 10/03/2014 |
| --- | --- |
| **Data de Vencimento** | 09/06/2014 |
| **Valor de Desdobramento** | R$1.000,00 |
| **Valor Presente** | R$899,12 |
| **Juros Valor Presente** | R$100,88 |

| ``` Memória de cálculo – Tabela TGFAVP (Ajusta Valor Presente) ``` |
| --- |

| **Data de Referência** | **Índice** | **Juros Valor Presente** |
| --- | --- | --- |
| 31/03/2014 | 2,1 | 18,88 |
| 30/04/2014 | 3,5 | 32,13 |
| 31/05/2014 | 4,0 | 38,01 |
| 06/09/2014 | 1,2 | 11,86 |
| Juros Valor Presente | 100,88 |  |

Quando é realizado o estorno dos títulos, a TGFAVP retorna ao estado inicial.

**Nota:** da forma como foi apresentada a memória de cálculo da TGFAVP, o tipo de inserção do ajuste é **"Mensal"**, ou seja, mês a mês entre a data de negociação e a data de vencimento o juro é calculado e inserido na tabela TGFAVP; essa configuração é inserida da TOP, conforme citamos acima.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598734-Contabiliza%C3%A7%C3%A3o-de-Financeiros-com-Ajuste-ao-Valor-Presente#top)

#### Contabilização

Após calcular o financeiro com os valores presentes e as tabelas dos juros se apresentarem com valores presentes, é hora de realizar a contabilização.

Na tela [TOP de contabilização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174-TOP-Contabiliza%C3%A7%C3%A3o), indique no campo **"Tipo de data"** a opção **"Ajusta Valor Presente"**:

![Imagem 7: Na tela TOP de contabilização , indique no campo "Tipo de data" a opção "Ajusta Valor Presente" :](https://ajuda.sankhya.com.br/hc/article_attachments/4407194627351)

Para a contabilização da nota serão disponibilizadas as fórmulas:

- **ValorPresente:** Somatória do campo TGFFIN.VALORPRESENTE dos títulos do financeiro da nota.
- **TotalJurosValorPresente:** Somatória do campo TGFFIN.JUROSAVP dos títulos do financeiro da nota.

Para a contabilização do financeiro/baixa e renegociação serão disponibilizadas as fórmulas:

- **ValorPresente (TGFFIN.VALORPRESENTE)**
- **TotalJurosValorPresente (TGFFIN.JUROSAVP)**

Na tela de [Agendamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608294-Agendamento), na aba **"Filtros"**, é possível agendar a contabilização filtrando por **"Juros AVP"**:

![Imagem 8: Na tela de Agendamento , na aba "Filtros" , é possível agendar a contabilização filtrando por "Juros AVP" :](https://ajuda.sankhya.com.br/hc/article_attachments/4407181075479)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598734-Contabiliza%C3%A7%C3%A3o-de-Financeiros-com-Ajuste-ao-Valor-Presente#top)

#### Imobilizado

Para que seja feita a aquisição de um imobilizado, a TOP de Compra deve estar configurada para atualizar o bem e as configurações do cálculo do valor presente (ajusta valor presente diferente de **'N'** e moeda maior que zero); o produto deve ser de imobilizado.

Ao gerar o financeiro da nota de compra do produto imobilizado, todos os financeiros terão o valor presente gerado e os juros gerados na tabela TGFAVP. Após gerar os financeiros, o valor presente e o valor de depreciação da tabela do imobilizado (TCIBEM) serão gerados.

Primeiro o índice:

Índice = Soma(TGFFIN.VALORPRESENTE)/ SOMA(TGFFIN.VLRDESDOBR)

TCIBEM.VALORPRESENTE = TCIBEM.VLRAQUISICAO \* INDICE

TCIBEM.VLRDEP = TCIBEM.VLRDEPORIG \* INDICE

**TCIBEM**

| **CODBEM** | **NUNOTA** | **CODPROD** | **VALORPRESENTE** | **VLRDEP** |
| --- | --- | --- | --- | --- |
| 00006621-008179-0001 | 6621 | 8179 | 144,32 | 144,32 |

O campo **"VLRDEPORIG"** serve para armazenar o valor de depreciação antes de aplicar o índice do valor presente. Portanto, deve-se preencher o campo **"VLRDEP"** via trigger ou qualquer outra maneira fora do Sankhya Om, sendo que o campo VLRDEPORIG deve ter o mesmo valor de VLRDEP quando inserir ou alterar o campo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598734-Contabiliza%C3%A7%C3%A3o-de-Financeiros-com-Ajuste-ao-Valor-Presente#top)
