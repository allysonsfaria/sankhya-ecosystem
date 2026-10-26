---
id: "360044579854"
titulo: "Melhores práticas para Configuração e Movimentação de Estoque com/de Terceiros"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044579854-Melhores-pr%C3%A1ticas-para-Configura%C3%A7%C3%A3o-e-Movimenta%C3%A7%C3%A3o-de-Estoque-com-de-Terceiros"
trilha: "Melhores Práticas > Vendas"
atualizado_em: "2026-09-24T17:19:20Z"
rotulos: ["#RevisadoJR", "Configuração", "Nota Fiscal", "Terceiros", "CFOP", "Estoque", "Estoque: Próprio e com terceiros", "Consignação e Industrialização: Notas e processos", "Conserto: Envio e retorno"]
---

# Melhores práticas para Configuração e Movimentação de Estoque com/de Terceiros

**![Imagem 1: DEFINIÇÕES](https://ajuda.sankhya.com.br/hc/article_attachments/19196941731863) DEFINIÇÕES**

- Estoque Próprio:

-Estoque pertencente à empresa e que se encontram em seu poder (posse e propriedade).

- Estoque COM Terceiros:

-Estoques pertencentes à empresa (propriedade), porém se encontram nas mãos de outra empresa (posse);

-Não pertencem ao ativo imobilizado;

-Continuam contabilmente fazendo parte dos estoques da empresa;

-Processos mais comuns:

- Envio em consignação;
- Envio de matéria-prima para industrialização;
- Envio para conserto.
- Diferente de “aluguel” onde estão envolvidos os bens do ativo imobilizado;

- Estoque DE Terceiros:

 -Estoques que se encontram nas mãos da empresa (posse), porém são pertencentes a outra empresa (propriedade). ;

-Não fazem parte contabilmente dos estoques da empresa, sendo necessária sua contabilização deverão utilizar contas separadas;

-Não podem afetar os custos do estoque próprio da empresa;

-Processos mais comuns:

- Recebimento em consignação;
- Industrialização para terceiros;
- Recebimento para conserto.

- Consignante:

-Proprietário do estoque que envia em consignação concretizando a venda somente quando o consignatário vende o produto.

- Consignatário:

-Quem recebe o produto em consignação, só pagando por este após a efetiva venda ou utilização na produção.

**![Imagem 2: ROTEIRO PARA CONFIGURAÇÃO DO PROCESSO DE CONSIGNAÇÃO](https://ajuda.sankhya.com.br/hc/article_attachments/19196941736471) ROTEIRO PARA CONFIGURAÇÃO DO PROCESSO  DE CONSIGNAÇÃO**

 2.1- CONSIGNANTE

  2.1.1-Envio em consignação: Nota Fiscal de remessa em consignação.

- Emissão: Própria
- Estoque Próprio: Baixa
- Estoque com/de Terceiros: Somar ao estoque próprio em poder de terceiros
- Financeiro: Não
- Custo: Não, o estoque continua sendo propriedade da empresa
- Kardex: Não
- CFOP: 5917, 6917

2.1.2-Faturamento do produto vendido pelo consignatário: Nota Fiscal de Simples Faturamento.

- Emissão: Própria
- Estoque Próprio: Não
- Estoque com/de Terceiros: Subtrair do Estoque próprio em poder de terceiros.
- Financeiro: Sim
- Custo: Afeta o custo médio da próxima compra em função da baixa no estoque
- Kardex: Saída
- CFOP: 5111, 5112, 5113, 5114, 6111, 6112, 6113, 6114

2.1.3-Recebimento de devolução: Nota Fiscal de devolução.

- Emissão: Terceiro (consignatário)
- Estoque Próprio: Entra
- Estoque com/de Terceiros: Subtrair do Estoque próprio em poder de terceiros
- Financeiro: Não
- Custo: Não
- Kardex: Não
- CFOP: 1918, 2918

 2.2- CONSIGNATÁRIO

2.2.1-Cadastro de Produtos (Configurações » Cadastros » Produtos » Produtos)

- Aba: Geral, Campo “Parceiro Consignante” deverá estar preenchido com o código do parceiro que enviará o produto em consignação.
- Um produto que é recebido em consignação só poderá ser movimento no estoque de um único parceiro, isto devido à necessidade de se controlar de forma separada o custo médio.
- Caso a empresa possua estoque próprio do mesmo produto **deverão existir dois códigos** de forma a não misturar o estoque próprio do estoque recebido em consignação. A contabilização destes estoques também deverá ser feita separada.

2.2.2-Recebimento em consignação: Nota Fiscal de remessa em consignação.

- Emissão: Terceiro
- Estoque Próprio: Entra
- Estoque com/de Terceiros: Somar ao Estoque de terceiros em poder da empresa
- Financeiro: Não
- Custo: Sim
- Kardex: Entrada
- CFOP: 1917, 2917

2.2.3-Venda do produto: Nota Fiscal de Venda.

- Emissão: Própria
- Estoque Próprio: Baixa
- Estoque com/de Terceiros: Não
- Financeiro: Sim
- Custo: Afeta o custo médio da próxima compra em função da baixa no estoque
- Kardex: Saída
- CFOP: 5115, 6115

2.2.4-Faturamento pelo consignante relativo ao produto vendido: Nota Fiscal de simples faturamento.

- Emissão: Terceiro (consignante)
- Estoque Próprio: Não
- Estoque com/de Terceiros: Subtrair do Estoque de terceiros em poder da empresa
- Financeiro: Sim
- Custo: Não
- Kardex: Não
- CFOP: 1111, 1113, 2111, 2113

2.2.5-Devolução de produto recebido em consignação: Nota Fiscal de Devolução.

- Emissão: Própria
- Estoque Próprio: Baixa
- Estoque com/de Terceiros: Subtrair do Estoque de terceiros em poder da empresa
- Financeiro: Não
- Custo: Afeta o custo médio da próxima compra em função da baixa no estoque
- Kardex: Saída
- CFOP: 5918, 6918

**![Imagem 3: ROTEIRO PARA CONFIGURAÇÃO DO PROCESSO DE INDUSTRIALIZAÇÃO PARA TERCEIROS](https://ajuda.sankhya.com.br/hc/article_attachments/19196953462935) ROTEIRO PARA CONFIGURAÇÃO DO PROCESSO DE INDUSTRIALIZAÇÃO PARA TERCEIROS**

3.1- TOMADOR DO SERVIÇO DE INDUSTRIALIZAÇÃO

3.1.1- Envio para industrialização: Nota Fiscal de remessa para industrialização.

- Emissão: Própria
- Estoque Próprio: Baixa
- Estoque com/de Terceiros: Somar ao estoque próprio em poder de terceiros
- Financeiro: Não
- Custo: Não, o estoque continua sendo propriedade da empresa
- Kardex: Não
- CFOP: 5901, 6901

3.1.2-Recebimento de retorno da industrialização: Nota Fiscal de retorno.

- Emissão: Terceiro
- Estoque Próprio: Entra
- Estoque com/de Terceiros: Subtrair do estoque próprio em poder de terceiros
- Financeiro: Sim – Parcela dos serviços prestados
- Custo: Não para mercadorias retornadas. Para os serviços prestados ou Produto acabado vai depender do processo implantado.
- Kardex: Não
- CFOP: 1902, 2902 (Mercadorias utilizadas no processo) / 1903, 2903 (Mercadorias não utilizadas no processo / 1124, 2124 (Serviços prestados de industrialização).

3.1.3 - Operação de Remessa de Industrialização triangular.

O sistema esta preparado para esta operação.

Para que a atualização ocorra adequadamente tem que atender aos pré-requisitos a seguir:

- No campo 'Parceiro Destinatário' do cabeçalho da Nota preencher com o 'Parceiro' que seria o industrializador, onde o sistema atualizará o código de parceiro (CODPARC) da TGFEST com o parceiro destinatário .
- O usuário lançará no sistema uma nota referente a compra para industrialização, em que a mercadoria foi remetida pelo fornecedor ao industrializador sem transitar pelo estabelecimento adquirente - CFOP 1122 ou 2122.

Assim quando a CFOP da TOP estiver configurada para 1122/2122 e as devidas opções acima estiverem configuradas, ao realizar a compra o sistema dará entrada no estoque em poder de terceiros para o 'Parceiro destinatário' e não para o 'Parceiro da Nota'.

3.2- PRESTADOR DO SERVIÇO DE INDUSTRIALIZAÇÃO.

3.2.1-Cadastro de Produtos (Configurações » Cadastros » Produtos » Produtos)

- Usado Como: Sempre “Terceiro”.
- A movimentação do estoque de terceiros poderá ser feita com mais de um parceiro, porém caso a empresa possua estoque próprio **deverá utilizar outro código** por questões de custo médio.

3.2.1-Recebimento para industrialização: Nota Fiscal de remessa para industrialização.

- Emissão: Terceiro
- Estoque Próprio: Entra (opcional)
- Estoque com/de Terceiros: Somar ao Estoque de terceiros em poder da empresa
- Financeiro: Não
- Custo: Não
- Kardex: Não
- CFOP: 1901, 2901

3.2.2-Retorno da industrialização: Nota Fiscal de retorno.

- Emissão: Própria
- Estoque Próprio: Sai (opcional dependendo da configuração do recebimento, se entrou tem de sair)
- Estoque com/de Terceiros: Subtrair do estoque de terceiros em poder da empresa
- Financeiro: Sim – Parcela dos serviços prestados
- Custo: Não
- Kardex: Não
- CFOP: 5902, 6902 (Mercadorias utilizadas no processo) / 5903, 6903 (Mercadorias não utilizadas no processo / 5124, 6124 (Serviços prestados de industrialização).

**Observação:** Na **operação triangular**, a Nota de Retorno da Industrialização deve ser lançada manualmente, pois é uma operação direta entre a empresa (industrializadora) e o parceiro. O sistema **não utilizará a nota fiscal original** que gerou o estoque de terceiros como base para esse lançamento. O estoque de terceiros em seu poder será atualizado diretamente por meio da nota de retorno, desde que a **TOP** esteja configurada para **subtrair** do estoque de terceiros em poder da empresa.

Isso explica por que a opção **'Dev./Est.'** no Portal de Compras não efetua a baixa automática para esse tipo de operação.

![9b9087f0-c329-4e14-b4cf-dd5f134049e0](https://ajuda.sankhya.com.br/hc/article_attachments/32431060958871)**ATENÇÃO!** Para Notas de industrialização com **CFOP 1924 e 2924**, utilizadas especialmente em situações triangulares, o lançamento deve ocorrer da seguinte forma:

**1.** Cadastro do produto
O produto deve estar classificado como **Tipo: Terceiro**, indicando que está em poder de terceiros.

**2.** Emissão da nota
Acesse o **Portal de Compras ou Vendas** e preencha os campos:

| **Campo** | **Preenchimento obrigatório** |
| --- | --- |
| CFOP | 1924 (entrada) ou 2924 (retorno) |
| Tipo de produto | Terceiro |
| Parceiro | Empresa remetente (quem emitiu ou recebeu a nota) |
| Parceiro destinatário | Empresa que deve receber ou devolver o material |

![Imagem 5: O campo Parceiro Destinatário é essencial para que o estoque seja vinculado à empresa correta.](https://ajuda.sankhya.com.br/hc/article_attachments/32431060961303) O campo **Parceiro Destinatário** é essencial para que o estoque seja vinculado à empresa correta.

**3.** Validação do estoque
Após o lançamento:

- Acesse o menu Gerência de Produtos ou relatório de Posição de Estoque em Terceiros.
- Verifique que o estoque do produto foi movimentado para o Parceiro Destinatário.

**![Imagem 6: ROTEIRO PARA CONFIGURAÇÃO DO PROCESSO DE ENVIO PARA CONSERTO](https://ajuda.sankhya.com.br/hc/article_attachments/19196917976087) ROTEIRO PARA CONFIGURAÇÃO DO PROCESSO DE ENVIO PARA CONSERTO**

4.1-PROPRIETÁRIO

4.1.1-Envio para conserto: Nota Fiscal de remessa para conserto.

- Emissão: Própria
- Estoque Próprio: Baixa
- Estoque com/de Terceiros: Somar ao estoque próprio em poder de terceiros
- Financeiro: Não
- Custo: Não, o estoque continua sendo propriedade da empresa
- Kardex: Não
- CFOP: 5915, 6915

4.1.2-Recebimento de retorno do conserto: Nota Fiscal de retorno.

- Emissão: Terceiro
- Estoque Próprio: Entra
- Estoque com/de Terceiros: Subtrair do estoque próprio em poder de terceiros
- Financeiro: Não
- Custo: Não
- Kardex: Não
- CFOP: 1916, 2916.

4.2-PRESTADOR DO SERVIÇO DE CONSERTO

4.2.1-Cadastro de Produtos (Configurações » Cadastros » Produtos » Produtos)

- Usado Como: Sempre “Terceiro”.
- A movimentação do estoque de terceiros poderá ser feita com mais de um parceiro, porém caso a empresa possua estoque próprio deverá utilizar outro código por questões de custo médio.

4.2.2-Recebimento para conserto: Nota Fiscal de remessa para conserto.

- Emissão: Terceiro
- Estoque Próprio: Entra (opcional)
- Estoque com/de Terceiros: Somar ao estoque próprio em poder de terceiros
- Financeiro: Não
- Custo: Não
- Kardex: Não
- CFOP: 1915, 2915

4.2.3-Retorno do conserto: Nota Fiscal de retorno.

- Emissão: Própria
- Estoque Próprio: Sai (opcional dependendo da configuração do recebimento, se entrou tem de sair)
- Estoque com/de Terceiros: Subtrair do estoque próprio em poder de terceiros
- Financeiro: Não
- Custo: Não
- Kardex: Não
- CFOP: 5916, 6916

**Observação:** O serviço de conserto não foi descrito no processo, pois caso exista (não for garantia) deverá ser emitida NF de serviços não tributado de ICMS.
