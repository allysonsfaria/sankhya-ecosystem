---
id: "360045109933"
titulo: "Alíquotas de CSLL"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109933-Al%C3%ADquotas-de-CSLL"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:29:40Z"
rotulos: ["ERRONF", "DUVIDANF", "AJUDA DO SKW", "manual", "Configuração", "Empresa", "Parceiro", "CSLL", "Impostos", "Alíquotas de CSLL", "br.com.sankhya.com.cad.aliquota.cssl", "Alíquotas de CSLL manual", "TOP", "Financeiro", "Cadastro Alíquotas CSLL"]
---

# Alíquotas de CSLL

| ``` ![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42312041869847) Módulo: Comercial > Arquivo > Cadastros > Alíquotas ``` |
| --- |

---

A Alíquota de CSLL trata-se de uma Contribuição Social sobre o Lucro Líquido de uma Empresa. Assim, ela deverá ser cadastrada e configurada nessa tela.

Aqui, tem-se opções para realizar a navegação entre os diversos cadastros.

![Imagem 2: Aqui, tem-se opções para realizar a navegação entre os diversos cadastros.](https://ajuda.sankhya.com.br/hc/article_attachments/21217963728791)

**Nota:** o botão ![Edição](https://ajuda.sankhya.com.br/hc/article_attachments/15992953001623)**"Edição múltipla"** permite a edição simultânea de vários registros a partir do modo grade. Ou seja, ao selecionar um conjunto de registros e clicar no botão, será possível editar os campos correspondentes de todos os registros de uma só vez. 

Por exemplo, com as alíquotas em modo grade na tela Alíquotas de CSLL selecione-as e em seguida clique no botão Edição múltipla, assim os campos poderão ser editados simultaneamente para todas as selecionadas.

Por meio do campo **"Código Alíquota"** será possível identificar qual alíquota é utilizada nos documentos fiscais.

Os campos **"Grupo"**, **"Empresa"**, **"Parceiro"**, **"Tipo Operação"**, **"Tipo"** e **"Tipo alíquota"** são de preenchimento obrigatório e possibilitam a criação de regras de execução para cálculo.

O campo Grupo está ligado diretamente ao [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-) assim, por exemplo, pode-se ter um Grupo chamado **"Rural"** e associar esse Grupo ao cadastro de vários Produtos. Dessa forma, todos os produtos que tiverem o Grupo Rural estarão nessa exceção.

**Importante:** para determinação da alíquota, o sistema observará a combinação dos campos Tipo Operação, Parceiro e Empresa.

**Observação:** se não for encontrada nenhuma exceção, poderá ser utilizada uma configuração com valor padrão como: Empresa 0, Parceiro 0, Tipo Operação 0, Alíquota 6,5. Deve-se observar que a TOP será a exceção mais analítica, ou seja, caso exista uma seguinte situação de exceção: Empresa 1, Parceiro 10 e TOP 100, apenas as vendas dos produtos daquele Grupo pela Empresa 1, para o Parceiro 10 e utilizando a TOP 100 serão tributadas obedecendo às regras definidas. Uma venda para Empresa 1, Parceiro 10 e TOP 99, por exemplo, deverá obedecer à regra geral, desde que não haja outra regra específica para a TOP 99 também.

O campo Tipo indica se o cálculo será considerado nas movimentações de **"Entrada"**, **"Saída"** ou **"Ambas"**.

No campo **"Alíquota"**, informe a alíquota do imposto e em seguida definir o Tipo da Alíquota, que será considerada em **"Percentual"** ou **"Valor"**.

Nos campos **"% Red. Base"** e **"IVA"** informe os percentuais correspondentes, caso necessário.

O campo **"Alíq. p/ Crédito"** é utilizado na movimentação de CSLL.

Utilize o campo **"Retém no financeiro"** assim que a NF-e passar a tratar movimentações de serviço.

Preencha o campo **"Tabela c/ base p/ ST"** com o código da tabela correspondente, se o imposto for por pauta.

Ao ativar a marcação **"IPI incide na base de cálculo"**, o IPI será integrado a base de cálculo de PIS, COFINS e CSLL.

**Observação:** o **Sankhya Om** ainda não realiza a proporcionalização para CSLL dos valores separados, seja para NF-e, SPED Fiscal, dentre outros, assim como para os itens Frete, Seguro, Embalagem, entre outros.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109933-Al%C3%ADquotas-de-CSLL#top)
