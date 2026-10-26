---
id: "360045112013"
titulo: "Alíquotas de IPI"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013-Al%C3%ADquotas-de-IPI"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:31:20Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "Fiscal", "NF-e", "Super Sintegra", "Alíquotas de IPI manual", "Importação", "IPI", "Impostos", "Sintegra", "Alíquotas de IPI", "br.com.sankhya.com.cad.aliquotasipi", "IPINFEREDVALOR", "INTTRIBDESCRIPI", "Funcionalidades de Tela", "Classificação Fiscal", "Configuração de IPI"]
---

# Alíquotas de IPI

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42312084231063) Módulo: Comercial > Arquivo > Cadastros > Alíquotas
```

---

Essa tela é utilizada para definir o percentual e a classificação fiscal de IPI dos produtos industrializados. Inicialmente, preencha os seguintes campos contidos no topo da tela:

No campo **"Código do IPI"**, informe a numeração referente ao IPI que está sendo cadastrado. Esse preenchimento pode ser realizado automaticamente ou de forma manual; essa definição é feita através do botão ![Imagem 2: No campo "Código do IPI" , informe a numeração referente ao IPI que está sendo cadastrado. Esse preenchimento pode ser…](https://ajuda.sankhya.com.br/hc/article_attachments/16342968928407) **"Configuração da Tela"**, opção **"Numeração"**, localizado no lado superior direito da tela.

A **"Descrição"** se refere à nomenclatura do IPI; essa informação deve ser simples e de fácil entendimento, pois juntamente com o Código do IPI irá identificar o cadastro perante todas as rotinas do sistema.

Para verificar sobre as informações importantes dessa tela de maneira mais fácil, acesse os links abaixo:

| Funcionalidades da Tela | |
| --- | --- |
| [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013-Al%C3%ADquotas-de-IPI#abageral) | [Aba Dados para Importação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013-Al%C3%ADquotas-de-IPI#abadadosparaimportao) |
| [Aba NCM](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013-Al%C3%ADquotas-de-IPI#abaNCM) | [Aba Produto x Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013-Al%C3%ADquotas-de-IPI#abaprodutoxparceiro) |
| [Aba Config. Suspensão IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013-Al%C3%ADquotas-de-IPI#abaconf.suspens%C3%A3oipi) | [Aba Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013-Al%C3%ADquotas-de-IPI#abaprodutos) |
| [Botão Edição múltipla](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013-Al%C3%ADquotas-de-IPI#BotaoEdi%C3%A7%C3%A3oMultipla) | [Cálculo do IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013-Al%C3%ADquotas-de-IPI#clculodoipi) |
| [Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013-Al%C3%ADquotas-de-IPI#Par%C3%A2metrosqueinfluenciamestarotina) |  |

### Aba Geral

![Imagem 3: Aba Geral](https://ajuda.sankhya.com.br/hc/article_attachments/21222345917847)

Referente ao **"Valor de Pauta"**, normalmente, o valor de IPI é calculado pelo valor de venda, porém para determinados produtos, como bebidas e chocolate, por exemplo, o IPI é cobrado sobre a unidade vendida. Sendo assim, defina o Valor de Pauta, que será um valor fixo a ser cobrado por unidade.

No campo **"Percentual"** é definido o percentual de IPI.

O campo **"% Redução de Vlr. IPI"** possibilitará a redução do IPI na emissão da NF-e.

**Nota:** o campo acima será habilitado apenas se o parâmetro **"Habilita configuração de redução de IPI? - IPINFEREDVALOR"** estiver ligado. Quando ligado na Central de Notas o sistema permitirá que se digite os valores deste imposto conforme sua necessidade.

Em **"Código Fiscal (NPC, NBM)"** informe a classificação fiscal do IPI.

O conteúdo do campo **"Cód. Exceção NCM"** refere-se ao campo 11 do Super Sintegra, conforme NCM da tabela TIPI.

A informação do campo **"Cód. Exceção II"** é referente ao campo 12 do Super Sintegra, conforme tabela NCM da tabela TIPI.

No campo **"Cód. Sit. Trib. IPI Entrada"** selecione o código de IPI de Entrada que irá usar, de acordo com uma das opções abaixo:

- 00 - Entrada c/ Recuperação de Crédito;
- 01 - Entrada c/ Alíquota zero;
- 02 - Entrada Isenta;
- 03 - Entrada Não Tributada;
- 04 - Entrada Imune;
- 05 - Entrada c/ Suspensão;
- 49 - Outras entradas.

No campo **"Cód. Sit. Trib. IPI Saída"** selecione o código de IPI de Saída que irá utilizar, conforme as opções abaixo:

- 50 - Saída Tributada;
- 51 - Saída c/ Alíquota zero;
- 52 - Saída Isenta;
- 53 - Saída Não Tributada;
- 54 - Saída Imune;
- 55 - Saída c/ Suspensão;
- 99 - Outras Saídas.

A seguir confira o enquadramento (Cód. Enq. Legal IPI Entrada ou Saída) adequado para cada tipo de Código Sit. Trib. IPI de Entrada ou Código Sit. Trib. IPI de Saída:

| **Código Sit. Trib. IPI Entrada ou Saída** | **Cód. Enq. Legal IPI Entrada ou Saída** |
| --- | --- |
| Cód.Sit.Trib.IPI Entrada = 02 ou  Cód.Sit.Trib.IPI Saída = 52 | Enquadramento de 301 a 399 |
| Cód.Sit.Trib.IPI Entrada = 04 ou  Cód.Sit.Trib.IPI Saída = 54 | Enquadramento de 001 a 099 |
| Cód.Sit.Trib.IPI Entrada = 05 ou  Cód.Sit.Trib.IPI Saída = 55 | Enquadramento de 101 a 199 |

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/16025388733975) Para mais informações relacionadas à tabela de códigos de enquadramento legal de IPI, consulte a NT 2015.002 disponível no link: <http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=mCnJajU4BKU=>

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013-Al%C3%ADquotas-de-IPI#top)

### Aba Dados para Importação

Essa aba comportará os percentuais de alíquotas para importação.

![Imagem 5: Essa aba comportará os percentuais de alíquotas para importação.](https://ajuda.sankhya.com.br/hc/article_attachments/21222454735255)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013-Al%C3%ADquotas-de-IPI#top)

### Aba NCM

Referente a essa aba, no parâmetro **"Descrição do imposto IPI na Int. Tributária - INTTRIBDESCRIPI"**, insira a descrição da Alíquota de IPI cadastrada. Assim, todos os NCMs vinculados serão inseridos nessa tela.

![Imagem 6: Referente a essa aba, no parâmetro "Descrição do imposto IPI na Int. Tributária - INTTRIBDESCRIPI" , insira a descrição…](https://ajuda.sankhya.com.br/hc/article_attachments/21222485571095)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013-Al%C3%ADquotas-de-IPI#top)

### Aba Produtos x Parceiro

Através dessa aba vincula-se o parceiro ao produto para determinar qual Alíquota de IPI será utilizada na operação, ou seja, ao efetuar um lançamento contendo o parceiro e o produto aqui informados, terá a aplicação dessa Alíquota de IPI.

![Imagem 7: Através dessa aba vincula-se o parceiro ao produto para determinar qual Alíquota de IPI será utilizada na operação, ou…](https://ajuda.sankhya.com.br/hc/article_attachments/21222584852631)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013-Al%C3%ADquotas-de-IPI#top)

### Aba Config. Suspensão IPI

![Imagem 8: Aba Config. Suspensão IPI](https://ajuda.sankhya.com.br/hc/article_attachments/21222584866711)

Inicialmente, preencha os campos **"Cód Tipo Operação"**, **"Cód Parceiro"** e **"Cód. Produto"**.

Os campos **"Cód. Sit. trib. IPI Entrada"** e **"Cód. Sit. Trib. IPI Saída"** permanecerão desabilitados para edição, pois sua configuração de suspensão de IPI permite que os valores sejam 05 para entrada e 55 para saída.

Referente aos campos **"Cód. Enq. Legal IPI Entrada"** e **"Cód. Enq. Legal IPI Saída"**, os valores permitidos neles são de 101 a 199, respectivamente. Caso seja informado um número diferente desses, a seguinte mensagem será exibida:

**"Código de Enquadramento Legal do IPI incompatível com CST de Suspensão (05 ou 55). Deve possuir enquadramento de 101 a 199, para maiores informações consulte a tabela de Código de Enquadramento Legal do IPI disponível na NT 2015 002 da NF-e."**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013-Al%C3%ADquotas-de-IPI#top)

### Aba Produtos

Nessa aba realiza-se a associação dos produtos à alíquota. Ao informar o código do produto, os demais campos serão preenchidos conforme o Cadastro do Produto.

![Imagem 9: Nessa aba realiza-se a associação dos produtos à alíquota. Ao informar o código do produto, os demais campos serão…](https://ajuda.sankhya.com.br/hc/article_attachments/21222619641111)

Para facilitar a sua usabilidade, a aba Produtos conta com os filtros **"Produtos"**, **"Grupo de Produtos"**, **"Marca"** e **"Referência"**.

**Importante:** as alterações feitas nessa tela afetam diretamente o Cadastro dos Produtos. Para checar se o IPI está sendo calculado corretamente, observe os seguintes itens:

1. Verifique no [Cadastro da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913) se ela trabalha com IPI.
2. Verifique no [Cadastro do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113) se o produto possui IPI na venda ou na compra.
3. Verifique qual código de Alíquota de IPI está cadastrado para o mesmo.
4. No cadastro de Alíquota de IPI, verifique se existe a alíquota com código encontrado no cadastro de produto e seu percentual.
5. Verifique se na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114#abaimpostos) da [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) está selecionada a opção para calcular ICMS e IPI.

Verifique informações sobre o processo de devolução de compra envolvendo empresas comerciais e industriais acessando a documentação [Devolução de IPI ao Fornecedor Industrial](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108273-Devolu%C3%A7%C3%A3o-de-IPI-ao-Fornecedor-Industrial).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013-Al%C3%ADquotas-de-IPI#BotaoEdi%C3%A7%C3%A3oMultipla)

### Botão Edição múltipla

O botão ![Edição](https://ajuda.sankhya.com.br/hc/article_attachments/15993419539351)**"Edição múltipla"** permite a edição simultânea de vários registros a partir do modo grade. Ou seja, ao selecionar um conjunto de registros e clicar no botão será possível editar os campos correspondentes de todos os registros de uma só vez. 

Por exemplo, com as alíquotas em modo grade na tela Alíquotas de IPI selecione-as e em seguida clique no botão Edição múltipla, assim os campos poderão ser editados simultaneamente para todas as selecionadas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013-Al%C3%ADquotas-de-IPI#top)

### Cálculo do IPI

Abaixo, tem-se um exemplo de como é efetuado o cálculo do IPI pelo sistema:

Considerando que o preço seja de R$100 reais, a alíquota de IPI 5% e o IPI embutido, o valor do IPI somado ao preço deve resultar em 100. Sendo assim, o cálculo não poderá ser 95 + 5 pelo fato de que 5% \* 95 resultaria em um IPI de 4,75 e a soma de 95 + 4,75 resulta em 99,75 que não fecha nos R$100 reais do preço de tabela.

Portanto, o sistema calcula o preço com um valor de 95,24 e o IPI de 4,76, onde 95,24 \* 5% resulta em um IPI de 4,76 que, somado aos 95,24, fechará nos R$100 reais.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013-Al%C3%ADquotas-de-IPI#top)

### Parâmetros que influenciam esta rotina

**Gera percentual Tag Aliquota IPI - GERPERCALIQIPI:** quando este parâmetro estiver ligado, o campo **"Alíq. IPI."** na grade [Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens) da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) não será preenchido. No entanto, quando o parâmetro estiver desligado, o campo será automaticamente preenchido com a alíquota de IPI configurada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013-Al%C3%ADquotas-de-IPI#top)
