---
id: "360045114753"
titulo: "Movimentação Financeira"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-10-07T19:21:23Z"
rotulos: ["CT-e", "AJUDA DO SKW", "manual", "CMC7", "Despesa", "Estorno", "Rateio", "Movimentação Financeira", "CONFMODGRDPESQ", "ORDENAFILTROS", "Apresentação de Valores em Moeda", "Financeiro", "Renegociação", "ALTERAFIN", "ALTERATIPTIT", "ALTERMULTABLOQ", "BXJUROMULTBRUTO", "CONCAUTBAIXA", "EXCLIBORC", "Fechamento Baixa em Moeda", "Lançamento de Títulos na  Movimentação  Financeira", "Liberações", "moeda estrangeira", "MTJUROBAIXPEND", "Negações", "OFEROPCBAIXTIT", "Orçamentárias", "Parâmetros que influenciam a rotina de Baixa", "Parcelamento de Títulos na Movimentação Financeira", "PERDESVFINREM", "PROIBTRCPARFIN", "Validação de alteração/exclusão de títulos originados do Módulo MGE Importação", "VARCAMBIALNEG", "br.com.sankhya.fin.cad.movimentacaofinanceira", "Movimentação Financeira manual", "CONSJURMULNEG", "DECVLRMOEDA", "Receita", "br.com.sankhya.fin.cad.movimentacaoFinanceira", "Receitas Despesas Provisões Juros Multas", "Baixa Estorno Rateio de títulos", "Registra operações internas e externas", "Provisão"]
---

# Movimentação Financeira

```
 Módulo: Financeiro > Rotinas
```

---

A tela Movimentação Financeira é utilizada para registrar e manter todas as operações que movimentam os recursos financeiros de sua empresa; operações estas, que irão alterar os saldos das Contas Bancárias da empresa e de seus respectivos colaboradores.

Alguns conceitos facilitarão o uso da Movimentação Financeira e serão tratados sobre eles logo abaixo:

| Conceitos |
| --- |
| [O que são Receitas e Despesas?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira#oquesoreceitasedespesas) |
| [O que é uma Provisão?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira#oqueumaproviso) |
| [Como um título é exibido na Movimentação Financeira?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira#comoumttuloexibidonamovimentaofinanceira) |
| [O que é, e como efetuar uma Renegociação?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira#oqueecomoefetuarumarenegociao) |
| [O que são Juros e Multas?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira#oquesojurosemultas) |
| [O que é realizar a baixa de um título?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira#oquerealizarabaixadeumttulo) |
| [O que é efetuar o estorno de um título?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira#oqueefetuaroestornodeumttulo) |
| [O que é um rateio financeiro?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira#oqueumrateiofinanceiro) |
| Funcionalidades da Tela |
| [Movimentação Financeira - Atributos da Tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874) |
| [Movimentação Financeira - Baixa de Títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600534) |
| [Movimentação Financeira - Botão Mais Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111893) |

---

## Conceitos

### O que são Receitas e Despesas?

#### Receita:

É tudo aquilo que é arrecadado pela empresa, à título de pagamento pela venda de um produto ou prestação de um serviço.

A receita representará todas as entradas de recursos que ocorreram na organização em um determinado período. Uma receita é caracterizada pela relação Empresa x Cliente.

#### Despesa:

Para prestar qualquer serviço, ou vender um produto, é necessário que a empresa se disponha de recursos. Contas de luz, água, internet, salários de funcionários, entre outras.

Além disso, no nosso contexto, aquisições diversas realizadas pela empresa também irão compor suas despesas, compras de produtos para posterior revenda, por exemplo.

Uma despesa é caracterizada pela relação Empresa x Fornecedor. Desse modo, o cálculo se torna simples:

```
 Receita = Despesa = Resultado Nulo
```

```
 Receita > Despesa = Superávit (Lucro) 
```

```
 Receita < Despesa = Déficit (Prejuízo)
```

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira#top)

### O que é uma Provisão?

É uma reserva de um valor que visa atender despesas esperadas. A provisão tem por objetivo a cobertura de um gasto já considerado certo ou de grande possibilidade de ocorrência. As provisões representam expectativas de perdas de ativos ou estimativas de valores à desembolsar que, apesar de financeiramente ainda não efetivadas, derivam de fatos geradores contábeis já ocorridos.

A partir do momento que essas perdas de ativos ou obrigações se tornam totalmente definidas, deixam de ser consideradas como provisões. Provisão, trata-se de de despesas ou receitas que, ainda que não pagas ou recebidas, configuram-se como ocorridas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira#top)

### Como um título é exibido na Movimentação Financeira?

Pode-se incluir um título na Movimentação Financeira de duas formas:

![Imagem 1: Através do lançamento de pedidos e/ou notas que provisionam ou incluem financeiro (esta definição é feita no Cadastro…](https://ajuda.sankhya.com.br/hc/article_attachments/16372715133207) Através do lançamento de pedidos e/ou notas que provisionam ou incluem financeiro (esta definição é feita no [Cadastro de Tipo de Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) utilizado no lançamento do documento, [aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), campo **"Atualização do financeiro"**). Uma vez o pedido/nota incluído na Central de [Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793)/[Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414), este posteriormente poderá ser localizado e trabalhado na Movimentação Financeira.

![Imagem 2: Por meio da inclusão direta na Movimentação Financeira , onde várias informações localizadas na guia "Lançamento" são…](https://ajuda.sankhya.com.br/hc/article_attachments/16372761669911) Por meio da inclusão direta na Movimentação Financeira, onde várias informações localizadas na guia **"Lançamento"** são de preenchimento obrigatório, sendo elas:

| - Parceiro; - Empresa; - Dt. Negociação; - Dt. Vencimento; - Tipo de Título; | - Receita/Despesa; - Nro. Nota; - Vlr do Desdobramento; - Banco; - Natureza. |
| --- | --- |

Quando for realizada o início na inclusão de um título, pode ser que o **"Parceiro"** para o qual o título está sendo gerado não esteja cadastrado no sistema; pressionando a tecla **[F2]** no teclado, será aberto o pop-up [Cadastro Simplificado de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598454).

Os demais preenchimentos presentes na guia Lançamento devem ser realizados de acordo com o processo de sua empresa. Confira o detalhamento dos campos presentes nesta guia através do link [Movimentação Financeira - Atributos da Tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874).

Uma vez um lançamento confirmado através do botão **"Salvar"**, o sistema irá gerar automaticamente o **"Nr. Único"** do título.

---

![Imagem 3: Informações adicionais](https://ajuda.sankhya.com.br/hc/article_attachments/21343390941975) **Informações adicionais**

**(1)** Para que ocorra da maneira correta o fluxo de cadastro na Movimentação Financeira, a paginação deve ser cancelada, ou deve-se esperar o final do carregamento da paginação para que se possa iniciar um novo cadastro pois, caso contrário, poderá ocorrer a perda dos dados digitados se a busca/paginação ainda esteja em execução. 

**(1)** O botão Duplicar da tela Movimentação Financeira ignora o controle de acessos; pode-se duplicar os títulos de acordo com a definição realizada no parâmetro **"Permite Duplicar Financeiro? - PERDUPLFIN"**; se estiver ligado, será possível duplicar; se desligado, não será possível efetuar este procedimento.

**(1)** Feita a contabilização dos lançamentos, não será possível alterar os Valores, a Natureza, os Históricos e o campo Receita/Despesa.

#### Alteração de Títulos Originados das Centrais

Títulos gerados a partir do Portal de Compras, Vendas ou Movimentações Internas possuem o campo **Origem = Estoque**. O comportamento de edição desses títulos é controlado pelos parâmetros **ALTERAFIN** e **PROIBTRCPARFIN**.

**Bloqueio Total (Parâmetro ALTERAFIN ligado):** Se o parâmetro "Qdo originado da Central não permitir alterar nada - ALTERAFIN" estiver ativo, o sistema impedirá qualquer modificação direta no financeiro, exibindo a mensagem:

> Título com origem no estoque, e conforme o parâmetro 'ALTERAFIN' não pode ser alterado! (Código: FIN\_E00530).

- **O que isso significa?** Esta é uma medida de segurança para garantir a integridade entre o financeiro e o documento fiscal de origem. O bloqueio impede mudanças em valores, datas, naturezas e centros de resultado.
- **Como proceder?** O ajuste deve ser realizado preferencialmente na Central de origem (Portal). Caso a edição direta seja necessária, o parâmetro deve ser avaliado pelo gestor financeiro (não recomendado em produção sem análise).
- **Exceção:** O processo de **Baixa** (botão Baixar) permanece permitido, pois não altera a estrutura original do título.

**Bloqueio Parcial (Configuração de parâmetros):**

- Se **ALTERAFIN** estiver desligado e **PROIBTRCPARFIN** (Proíbe a troca de parceiro em financeiro de nota) estiver ligado: O sistema bloqueia a edição de campos críticos como Vlr. Desdobramento, Dt. Negociação, Empresa, Moeda, Parceiro e Tipo de Operação.
- Se ambos estiverem desligados: O bloqueio persiste para campos estruturais de origem (Vlr. Desdobramento, Empresa, Tipo de Operação), mas permite flexibilidade em outros campos informativos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira#top)

### O que é, e como efetuar uma Renegociação?

A renegociação de dívidas é um processo que consiste na geração de um novo título de receita ou despesa com base no título original (ou títulos originais, uma vez que na renegociação vários títulos podem ser agrupados para geração de um único documento), alterando-se os vencimentos e valores conforme necessário.

Pode-se renegociar um título em consequência de seu vencimento, reajuste de parcelas do título, agrupamento de dois ou mais títulos em um único documento, de acordo com o processo e demanda da empresa.

A renegociação de um documento é realizada na tela [Renegociação de Títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393); na Movimentação Financeira pode-se visualizar os títulos renegociados, bem como proceder sua baixa.

**Observação:** após realizar uma renegociação de CT-e na Movimentação Financeira, os valores de crédito de PIS/COFINS serão atualizados no [Gerente On-Line](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109613-Gerente-On-line), aba **"PIS/COFINS"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira#top)

### O que são Juros e Multas?

#### Juros:

Podemos entender os juros como uma taxa percentual sobre o atraso do pagamento de um título de crédito em um determinado período de tempo. São a pena imposta ao devedor pelo atraso no cumprimento de sua obrigação.

Os juros funcionam como uma espécie de indenização pelo retardamento na execução do débito; podem ainda ser convencionados entre as partes ou, na ausência de convenção, serem aplicados seguindo determinações por lei.

#### Multa:

A multa pode ser entendida em vários contextos; é um dispositivo de permanência ou fidelidade; em um contrato, a multa prevê um percentual que será retido pelo fornecedor do valor total pago. A cobrança é formalizada quando acontece uma rescisão sem motivos do contrato pelo consumidor. No direito público, é a sanção empreendida pelo Estado ao particular que descumprir uma norma jurídica; como por exemplo, ultrapassar o limite de velocidade rodoviária.

![Imagem 4: Os juros e multas calculados para os títulos, e visualizados no ato de sua baixa, são previamente configurados na tela…](https://ajuda.sankhya.com.br/hc/article_attachments/21344068106391) Os juros e multas calculados para os títulos, e visualizados no ato de sua baixa, são previamente configurados na tela de [Cálculo de Juros e Multa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115373 "Cálculo de juros e multa").

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira#top)

### O que é realizar a baixa de um título?

A baixa de um título consiste em transformá-lo de conta à receber ou à pagar, em conta efetivamente paga ou recebida; o procedimento de baixa irá concretizar a inserção ou retirada dos valores monetários das contas bancárias da empresa.

O procedimento de baixa de títulos está detalhadamente descrito no tópico [Movimentação Financeira - Baixa de Títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600534).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira#top)

### O que é efetuar o estorno de um título?

É a ação de devolver uma quantia cobrada indevidamente, como o estorno do cartão de crédito ou o estorno bancário. No contexto de nosso sistema, estornar significa retornar um título do status Baixado para Pendente; assim como a baixa inclui ou retira das contas bancárias os valores correspondentes ao procedimento em questão, o estorno efetua o processo inverso, ou seja, a baixa de uma receita insere valores às contas, o estorno retira; a baixa de uma despesa remove valores das contas, o estorno reinsere.

**Observação:** só é possível efetuar um processo de estorno de um título gerado pela compensação financeira, se ele não estiver conciliado.

O procedimento de estorno de títulos está descrito no tópico [Movimentação Financeira - Baixa de Títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600534).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira#top)

### O que é um rateio financeiro?

O rateio financeiro corresponde à uma divisão proporcional; trata-se de uma forma direta de segregar os recursos consumidos pelos objetos principais de custos em determinado estágio de sua ocorrência. Considere o exemplo a seguir:

Temos 3 (três) departamentos em um escritório, e a energia elétrica deve ser rateada por estes 3 departamentos. Para isso, devemos utilizar uma base para o rateio, pode ser o número de pessoas por departamento. Com a energia custando R$100,00, temos o seguinte rateio:

- Departamento 1 possui 3 pessoas - paga R$ 30,00
- Departamento 2 possui 5 pessoas - paga R$ 50,00
- Departamento 3 possui 2 pessoas - paga R$ 20,00

Isso com base no número de pessoas de cada departamento, mas há outros critérios. No nosso sistema, estes critérios são determinados através da tela [Critérios de Rateio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606574).

Na Movimentação Financeira, o rateio é realizado através do botão **"Ratear"**. O detalhamento de suas funcionalidades pode ser acessado através do link [Movimentação Financeira - Atributos da Tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874).

### Solução de problemas

**Erro: "EntityPrimaryKey não pode ser nulo"**
Ao tentar alterar informações de um título (como a Conta Bancária) originado do Portal de Compras no layout HTML5, o sistema pode apresentar este erro.

**Causa:** Este incidente geralmente está relacionado a uma falha de sincronização de chaves primárias entre a interface e o banco de dados em versões específicas.

**Como resolver:**

1. Certifique-se de que o título não possui restrições pelos parâmetros de bloqueio citados acima (ALTERAFIN).
2. Caso o erro persista, tente realizar a alteração utilizando o layout Design System ou verifique se há atualizações pendentes para o componente Financeiro BFF.
3. Verifique se todos os campos obrigatórios da aba "Lançamento" estão devidamente preenchidos antes de salvar.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira#top)
