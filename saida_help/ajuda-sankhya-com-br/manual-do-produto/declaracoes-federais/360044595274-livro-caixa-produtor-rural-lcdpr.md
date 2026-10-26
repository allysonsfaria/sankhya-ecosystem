---
id: "360044595274"
titulo: "Livro Caixa Produtor Rural - LCDPR"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274-Livro-Caixa-Produtor-Rural-LCDPR"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Escriturações e Declarações   > Declarações federais"
atualizado_em: "2026-09-15T17:36:08Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "br.com.sankhya.mgeliv.mov.geracaoarquivolcdpr", "Geração do Arquivo LCDPR manual", "Impostos", "Financeiro", "Declaração", "Define versão indicadores e apuração do Livro Caixa Digital", "Dados do registro de abertura e identificação do produtor", "Parâmetros de tributação dados cadastrais imóveis rurais terceiros e contas bancárias", "Produtor Rural", "Livro Caixa"]
---

# Livro Caixa Produtor Rural - LCDPR

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/16315781336087) Módulo: Livros Fiscais > Conexão
```

---

Através desta rotina, será possível incluir as informações, realizar configurações e gerar o Arquivo do Livro Caixa Digital do Produtor Rural.

| [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274-Livro-Caixa-Produtor-Rural-LCDPR#painelprincipal) |  | [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274-Livro-Caixa-Produtor-Rural-LCDPR#abageral) |
| --- | --- | --- |
| [Aba 0000](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274-Livro-Caixa-Produtor-Rural-LCDPR#aba0000) |  | [Aba 0010](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274-Livro-Caixa-Produtor-Rural-LCDPR#aba0010) |
| [Aba 0040](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274-Livro-Caixa-Produtor-Rural-LCDPR#aba0040) |  | [Aba 0050](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274-Livro-Caixa-Produtor-Rural-LCDPR#aba0050) |
| [Aba Q100](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274-Livro-Caixa-Produtor-Rural-LCDPR#abaq100) |  | [Aba Q200](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274-Livro-Caixa-Produtor-Rural-LCDPR#abaq200) |
| [Aba 9999](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274-Livro-Caixa-Produtor-Rural-LCDPR#aba9999) |  | [Botões no topo da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274-Livro-Caixa-Produtor-Rural-LCDPR#botesnotopodatela) |

## Painel Principal

![Imagem 2: Painel Principal](https://ajuda.sankhya.com.br/hc/article_attachments/4415575433751)

Neste Painel, deve-se configurar a **"Empresa"** que terá o Arquivo do Livro Caixa Digital do Produtor Rural gerado, bem como, informar a **"Dt. Inicial"** e a **"Dt. Final"** para a geração.

## Aba Geral

No campo **"Versão do Layout"** encontra-se a versão definida pela Receita, a qual será entregue o Arquivo do Livro Caixa Digital do Produtor Rural.

O campo **"Indicador do Início do Período"** possui as seguintes opções:

- **Início de obrigatoriedade da escrituração no curso do ano calendário:** Esta opção deverá ser selecionada quando o produtor rural, no curso do ano caléndário, adquiriu algum processo administrativo.
- **Abertura:** Deve-se selecionar esta opção quando o produtor rural obteve operações com a atividade rural naquele ano da entrega do livro.
- **Regular:** Seleciona-se esta opção quando o produtor rural já realiza operações da atividade rural, ou seja, suas operações não são recentes.

Deve-se preencher o campo **"Indicador de Situação Especial e Outros Eventos"** para indicar a situação do produtor rural no ano calendário da entrega do livro. Neste campo, tem-se as opções a seguir:

- Espólio;
- Falecimento;
- Normal;
- Saída definitiva do País.

O campo **"Data da Situação Especial"** possui relação com o campo Indicador de Situação Especial e Outros Eventos, ou seja, deve-se selecionar a data em que ocorreu a situação especial.

No campo **"Forma de Apuração"** seleciona-se a forma escolhida pelo produtor rural para executar a apuração de suas atividades rurais, sendo elas:

- Apuração do lucro pelo disposto no art. 5º da Lei nº 8.023, de 1990;
- Livro Caixa.

Se você não realizar a habilitação da marcação **"Construir histórico do registro Q100 de forma automática?"**, o histórico do registro Q100 será obtido a partir da tela [Movimentação financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753); caso contrário ocorrerá da seguinte forma:

- **Se Receita:** Recebimento ref. - NF Nº XXX - Razão Social do Parceiro + Histórico do financeiro;
- **Se Despesa:** Pagamento ref. - NF Nº XXX - Razão Social do Parceiro + Histórico do financeiro.

Quando a marcação **"Considerar naturezas do rateio da Movimentação Financeira para gerar o Q100?"** for habilitada, o sistema exibirá as informações de despesas/receitas considerando as naturezas do rateio do título lançado na Movimentação Financeira da seguinte forma:

- Caso exista no rateio mais de uma natureza e uma delas estiver com a marcação **"Gera informações para o Livro Caixa Digital Produtor Rural"** da tela [Natureza de Receitas e Despesas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas) desabilitada, o valor rateado referente a essa natureza não será considerado na declaração;
- Se a marcação Considerar naturezas do rateio da Movimentação Financeira para gerar o Q100? for selecionada, e o lançamento não possuir rateio, o sistema utilizará a informação do campo **"Natureza"** da aba [Lançamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874#abalanamento) da [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira), desde que esta seja configurada para gerar LCDPR.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274-Livro-Caixa-Produtor-Rural-LCDPR#top)

## Aba 0000

Esta aba tratará sobre informações relativas ao **"Registro 0000 - Abertura do Arquivo Digital e Identificação da Pessoa Física"**.

![Imagem 3: Esta aba tratará sobre informações relativas ao "Registro 0000 - Abertura do Arquivo Digital e Identificação da Pessoa…](https://ajuda.sankhya.com.br/hc/article_attachments/4408238522007)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274-Livro-Caixa-Produtor-Rural-LCDPR#top)

## Aba 0010

Nesta aba, teremos as informações referentes ao **"Registro 0010 - Parâmetros de Tributação"**:

![Imagem 4: Nesta aba, teremos as informações referentes ao "Registro 0010 - Parâmetros de Tributação" :](https://ajuda.sankhya.com.br/hc/article_attachments/4408238561815)

No campo **"Forma de Apuração"** deve-se selecionar se a apuração será realizada de acordo com o **"Livro Caixa"** ou com a **"Apuração do lucro pelo disposto no art. 5º da Lei nº 8.023, de 1990"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274-Livro-Caixa-Produtor-Rural-LCDPR#top)

## Aba 0030

Essa aba, refere-se ao **"Registro 0030 - Dados Cadastrais do Contribuinte"**.

![Imagem 5: Essa aba, refere-se ao "Registro 0030 - Dados Cadastrais do Contribuinte" .](https://ajuda.sankhya.com.br/hc/article_attachments/4408249562391)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274-Livro-Caixa-Produtor-Rural-LCDPR#top)

## Aba 0040

Tem-se nesta aba as informações referentes ao **"Registro 0040 - Cadastro dos Imóveis Rurais"**; assim, esta aba tem por objetivo controlar as aquisições, as quantidades e preencher o Registro 0040 do arquivo LCDPR.

**Observação:** o registro 0040 buscará as informações de todos os imóveis rurais definidos no Q100 e o registro 0045 carregará os dados da aba **"Livro Caixa Digital Produtor Rural"** da tela Preferências da Empresa para cada um dos imóveis.

![Imagem 6: Observação: o registro 0040 buscará as informações de todos os imóveis rurais definidos no Q100 e o registro 0045…](https://ajuda.sankhya.com.br/hc/article_attachments/4408238614935)

---

**Sub-aba 0045**

Quando configurados os campos desta sub-aba, será preenchido o **"Registro 0045 - Cadastro de Terceiros"**. Nesta sub-aba deve-se realizar o cadastro das informações relativas a contratos e dados da contraparte do imóvel.

![Imagem 7: Quando configurados os campos desta sub-aba, será preenchido o "Registro 0045 - Cadastro de Terceiros" . Nesta sub-aba…](https://ajuda.sankhya.com.br/hc/article_attachments/4408249584535)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274-Livro-Caixa-Produtor-Rural-LCDPR#top)

## Aba 0050

Nesta aba, deve-se inserir as informações relativas às contas bancárias do produtor rural, para que o **"Registro 0050 - Cadastro das Contas Bancárias do Produtor Rural"**.

![Imagem 8: Nesta aba, deve-se inserir as informações relativas às contas bancárias do produtor rural, para que o "Registro 0050 -…](https://ajuda.sankhya.com.br/hc/article_attachments/4408238637207)

Para a obtenção do **"Código Sequencial da Conta Bancária"** e **"Código da conta bancária"** dos registros [Q100](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274#abaq100) e [0050](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274#aba0050), teremos a seguinte hierarquia de busca caso estes estejam preenchidos:

- Campo **"Classificação da conta Produtor Rural"**;
- O campo **"Número da conta Produtor Rural"**;
- Os três primeiros dígitos do **"Código da Conta Bancária"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274-Livro-Caixa-Produtor-Rural-LCDPR#top)

## Aba Q100

Esta aba, refere-se ao **"Registro Q100 - Demonstrativo do Resultado da Atividade Rural"** e trará informações dos financeiros para os imóveis rurais associados à empresa em questão, no intervalo definido no cabeçalho da Movimentação Financeira.

![Imagem 9: Esta aba, refere-se ao "Registro Q100 - Demonstrativo do Resultado da Atividade Rural" e trará informações dos…](https://ajuda.sankhya.com.br/hc/article_attachments/4408238652823)

---

Para que você efetue a geração do Registro Q100, primeiramente, realize as configurações abaixo:

| **(1)** | Na tela [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros), defina da seguinte forma os campos: |
| --- | --- |

- Defina o campo **"Classificação ICMS"** com a opção **"Produtor Rural"**;
- Habilite a marcação **"Produtor tem NF"**;
- Preencha o campo **"CPF Prod. Rural"**.

| **(1)** | Logo depois, na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa): |
| --- | --- |

- Acione a marcação **"Gera informações para o Livro Caixa Digital Produtor Rural"**;
- Nos campos **"Cód. CAFIR"** e **"Cód. CAEPF"**, informe os códigos correspondentes a eles;
- Defina ainda um **"Tipo de Exploração"**;
- Depois, na sub-aba desta aba, inclua o parceiro produtor rural vinculado e determine um **"Percentual de Exploração"**, uma vez que, essa informação será utilizada no Registro Q100 quando o sistema efetuar o cálculo do valor de entrada e saída.

| **(1)** | Logo após, na tela [Natureza de Receitas e Despesas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas): |
| --- | --- |

- Adicione uma natureza com característica de receita e nesta, acione a marcação **"Gera informações para o Livro Caixa Digital Produtor Rural"**.

| **(1)** | Já na tela [Cadastro de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas): |
| --- | --- |

- Lembre-se de desabilitar a marcação **"Desconsiderar Conta na Geração do Livro Caixa Digital do Produtor Rural"** no registro da conta bancária utilizada para a baixa.

| **(1)** | No [Cadastro de Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos): |
| --- | --- |

- Realize a criação de um imposto com o **"Nome"** igual a SENAR;
- Depois, defina o campo **"Tipo"** com a opção **"apenas os que tenham a coluna “calcular” MARCADA"**;
- No campo **"Tipo Imposto"**, escolha a opção **"SENAR"**;
- Configure o campo **"Usar para itens da nota"** com a opção **"Preço da Nota"**;
- Realize a definição da opção **"Valor do Pagamento"** no campo **"Base para Impostos do Financeiro"**.

| **(1)** | Na aba [Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos#abaparceiro) ainda na tela Cadastro de Impostos, configure os campos da seguinte forma: |
| --- | --- |

- **Parceiro:** parceiro criado anteriormente;
- **Na nota:** Já incluso;
- **No Financeiro Origem Financeiro:** Nenhum;
- **No Financeiro Origem Estoque:** Subtrair;

| **(1)** | Posteriormente, na aba [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos#abatop) da mesma tela: |
| --- | --- |

- **Alíquota:** 0,20;
- **Na nota:** Já incluso;
- **No Financeiro Origem Financeiro:** Nenhum;
- **No Financeiro Origem Estoque:** Subtrair;

| **(1)** | Ainda na mesma tela, na aba [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos#abaempresa): |
| --- | --- |

- Informe a **"Empresa"** a ser utilizada na venda;
- **Alíquota:** 0,20;
- **Na nota:** Já incluso;
- **No Financeiro Origem Financeiro:** Nenhum;
- **No Financeiro Origem Estoque:** Subtrair;
- Habilitar marcação **"Calcular"**.

| **(1)** | Na mesma tela, aba [Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos#abaproduto), configure: |
| --- | --- |

- O **"Produto"** que será utilizado na venda;
- **Alíquota:** 0,20;
- **Na nota:** Já incluso.

| **(1)** | Já na tela [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral): |
| --- | --- |

- Preencha o campo **"Tipo Documentado Rural"**;
- Configure também o registro do título a ser lançado na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira).

| **(1)** | Em [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), aba [Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas): |
| --- | --- |

- Após criar um Tipo de Negociação, informe o Tipo de Título criado anteriormente;
- Em seguida, na Parcela 1, defina o campo **"Natureza Padrão"** da receita cadastrada para a geração do LCDPR;
- No campo **"Tipo de Financeiro (REC/DESP)"**, utilize a opção **"Usar da Natureza Padrão"**;
- Já na Parcela 2, cadastre a Natureza Padrão da despesa para o imposto;
- Realize a configuração do campo **"Tipo de Parceiro"** com a opção **"C - Constante"**;
- No **"Parceiro"**, defina o Parceiro responsável pelo recebimento do imposto;
- Já o campo **"Fórmula"** deve ser utilizado para que a parcela seja gerada considerando os outros impostos;
- Em seguida, configure a opção **"Usar da Natureza Padrão"** no campo **"Tipo de Fincanceira (REC/DESP)"**.

| ![Imagem 10: Em seguida, configure a opção "Usar da Natureza Padrão" no campo "Tipo de Fincanceira (REC/DESP)" .](https://ajuda.sankhya.com.br/hc/article_attachments/16315843318423) | Caso tenha dúvidas referentes ao preenchimento do campo, consulte a documentação deste nesta aba. |
| --- | --- |

| **(1)** | Nas [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) do sistema: |
| --- | --- |

- No parâmetro **"Naturezas de títulos não apresentados na nota - NATTITNAONOT"**, insira a natureza de despesa criada e informada na Parcela 2 do Tipo de Negociação.

```
                                                                               ![Imagem 11: No parâmetro "Naturezas de títulos não apresentados na nota - NATTITNAONOT" , insira a natureza de despesa criada e…](https://ajuda.sankhya.com.br/hc/article_attachments/16315843319191)
       Caso a natureza não seja inserida no parâmetro, ao emitir uma Nota Fiscal para a SEFAZ, será
       apresentada a seguinte mensagem:
       "866 - Rejeição: Ausência de troco quando o valor dos pagamentos informados for maior
       que o total da nota"
```

- Em seguida, caso queira que o Registro Q100 e o campo **"Valor de entrada dos recursos"** desta aba sejam gerados com o valor bruto quando o título possuir um, ou mais lançamentos conforme a opção **"Vlr. do Desdobramento"** da Movimentação Financeira, ligue o parâmetro **"Gerar valor bruto de receita no Q100 do LCDPR - GERVLRBRTLCDPR"**.

| **(1)** | Na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira): |
| --- | --- |

- Confira se o título está baixado;
- Além disso, certifique-se que a data da baixa está entre o período informado no LCDPR, e se esta foi gravada, pois não pode ser nula;
- Tenha a certeza que o título lançado não é uma provisão.

| **(1)** | Por fim, na tela Livro Caixa Produtor Rural - LCDPR: |
| --- | --- |

- No campo **"Produtor"**, informe o parceiro utilizado;
- Em seguida, preencha o campo **"Versão do Layout"** com a Versão 0013;
- Defina o campo **"Indicador do início do período"** com a opção **"Regular"**;
- Referente ao campo **"Indicador de Situação Especial"**, defina-o com a opção **"Normal"**;
- Configure no campo **"Forma de Apuração"**, a opção **"Livro Caixa"**.

---

A seguir, teremos os seguintes campos na aba Q100:

Nos campos **"Valor de entrada dos recursos"** e **"Valor de saída dos recursos"**, o desdobramento do financeiro será proporcionalizado conforme o que foi definido na aba [Livro Caixa Produtor Rural](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abalivrocaixaprodutorrural) nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa).

O campo **"Valor total do lançamento"** exibe o total do desdobramento de cada financeiro, para conferência.

**Nota:** acionando-se os botões **"Conciliar"** e **"Desfazer Conciliação"**, tem-se o seguinte comportamento, executando-se a funcionalidade em todos os registros Q100 do mês escolhido:

[GIF animado: Imagem 12: Nota: acionando-se os botões "Conciliar" e "Desfazer Conciliação" , tem-se o seguinte comportamento, executando-se a…](https://ajuda.sankhya.com.br/hc/article_attachments/4408255520919)

**Importante:** os registros Q100 conciliados, não poderão ser editados ou excluídos e serão encaminhados para o arquivo, diferentemente dos que não foram conciliados.

Para a obtenção do **"Código Sequencial da Conta Bancária"** e **"Código da conta bancária"** dos registros Q100 e 0050, teremos a seguinte hierarquia de busca caso estes estejam preenchidos:

- Campo **"Classificação da conta Produtor Rural"**;
- O campo **"Número da conta Produtor Rural"**;
- Os três primeiros dígitos do **"Código da Conta Bancária"**.

**Observação:** os campos **"Conta Bancária"** e **"Cód. Natureza"** farão ligação com o Cadastro de [Conta Bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113) e a Natureza respectivamente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274-Livro-Caixa-Produtor-Rural-LCDPR#top)

## Aba Q200

Nesta aba deve-se realizar o preenchimento das informações relativas ao **"Registro Q200 - Resumo Mensal do Demonstrativo do Resultado da Atividade Rural"**.

**Nota:** o registro Q200 faz o resumo mensal dos lançamentos no Q100.

![Imagem 13: Nota: o registro Q200 faz o resumo mensal dos lançamentos no Q100 .](https://ajuda.sankhya.com.br/hc/article_attachments/4408249716119)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274-Livro-Caixa-Produtor-Rural-LCDPR#top)

## Aba 9999

Tem-se nesta aba as informações referentes ao **"Registro 9999 - Identificação do Contador e Encerramento do Arquivo Digital"**.

![Imagem 14: Tem-se nesta aba as informações referentes ao "Registro 9999 - Identificação do Contador e Encerramento do Arquivo…](https://ajuda.sankhya.com.br/hc/article_attachments/4408249826071)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274-Livro-Caixa-Produtor-Rural-LCDPR#top)

## Botões no topo da tela

A Geração do Arquivo LCDPR é composta por abas, as quais descrevemos até aqui e também por botões que executam diversas funções dentro desta rotina. Vejamos sobre eles:

Por meio do botão ![Imagem 15: Por meio do botão "Filtros" , o assistente de configuração de filtros personalizados para a tela será exibido.](https://ajuda.sankhya.com.br/hc/article_attachments/16315843320983) **"Filtros"**, o assistente de configuração de filtros personalizados para a tela será exibido.

No botão ![Imagem 16: No botão "Modo grade (F8)" , alterna-se a visualização da tela entre modo grade e modo formulário; além disto,…](https://ajuda.sankhya.com.br/hc/article_attachments/16315781342359) **"Modo grade [F8]"**, alterna-se a visualização da tela entre modo grade e modo formulário; além disto, configura-se a grade da maneira almejada, ou seja, pode-se selecionar, ordenar ou ocultar as colunas conforme sua preferência.

Em ![Imagem 17: Em "Cadastrar Livro Caixa Digital do Produtor Rural (F8)" , tem-se a inicialização da Geração do Arquivo LCDPR .](https://ajuda.sankhya.com.br/hc/article_attachments/16315843324823) **"Cadastrar Livro Caixa Digital do Produtor Rural [F8]"**, tem-se a inicialização da Geração do Arquivo LCDPR.

Por meio dos botões ![Imagem 18: Por meio dos botões "Próxima" e "Anterior" , o sistema que você navegue entre os registros já cadastrados.](https://ajuda.sankhya.com.br/hc/article_attachments/16315781351319) **"Próxima"** e **"Anterior"**, o sistema que você navegue entre os registros já cadastrados.

No botão ![Imagem 19: No botão "Excluir (F9)" , realiza-se a exclusão do registro selecionado na tela.](https://ajuda.sankhya.com.br/hc/article_attachments/16315781354903) **"Excluir [F9]"**, realiza-se a exclusão do registro selecionado na tela.

Ao acionar o botão ![Imagem 20: Ao acionar o botão "Duplicar" , o registro selecionado será duplicado, de forma que um novo registrado será adicionado…](https://ajuda.sankhya.com.br/hc/article_attachments/16315843334423) **"Duplicar"**, o registro selecionado será duplicado, de forma que um novo registrado será adicionado à tela com as configurações equivalentes àquele primeiramente selecionado.

Quando você utilizar o botão ![Imagem 21: Quando você utilizar o botão "Atualizar" , recarrega-se toda a tela de Geração do Arquivo LCDPR .](https://ajuda.sankhya.com.br/hc/article_attachments/16315843335831) **"Atualizar"**, recarrega-se toda a tela de Geração do Arquivo LCDPR.

Por meio do botão ![Imagem 22: Por meio do botão "Processar" , a apuração ou processamentos dos dados LCDPR, referente às tabelas que contemplam cada…](https://ajuda.sankhya.com.br/hc/article_attachments/16315781359383) **"Processar"**, a apuração ou processamentos dos dados LCDPR, referente às tabelas que contemplam cada registro do layout será realizado. Assim, após esse processamento, o sistema emitirá uma mensagem o confirmando.

Quando você acionar o botão ![Imagem 23: Quando você acionar o botão "Gerar" , será gerado o arquivo .txt exigido pela Instrução Normativa RFB N. 1848/2018.](https://ajuda.sankhya.com.br/hc/article_attachments/16315843339287) **"Gerar"**, será gerado o arquivo .txt exigido pela Instrução Normativa RFB N. 1848/2018.

**Nota:** ao acionar este botão, será exibido um pop-up para confirmação da geração do arquivo LCDPR; confirmando esta ação, será exibido o pop-up **"Processos"** para acompanhamento da geração do arquivo. Esse pop-up trará informações detalhadas referentes ao processo de geração do arquivo, como os dados da empresa, o período e andamento dos registros.

O botão ![Imagem 24: O botão "Histórico de Gerações" , exibirá todo o histórico de dados os últimos arquivos gerados.](https://ajuda.sankhya.com.br/hc/article_attachments/16344182124311) **"Histórico de Gerações"**, exibirá todo o histórico de dados os últimos arquivos gerados.

Por meio do botão ![Imagem 25: Por meio do botão "Exportar grade para PDF" , apresenta opções de exportação e visualização das informações da tela.…](https://ajuda.sankhya.com.br/guide-media/01H6743AM7C5181E5VX745E5ZA) **"Exportar grade para PDF"**, apresenta opções de exportação e visualização das informações da tela. Pode-se **"Exportar para PDF"**, **"Exportar para planilha"** ou **"Exportar para cubo"**.

Em ![Imagem 26: Em "Anexo" , pode-se anexar qualquer documento que seja relevante para a rotina de Geração do Arquivo LCDPR .](https://ajuda.sankhya.com.br/guide-media/01H6748806TF4YTBWEJSKWJX68) **"Anexo"**, pode-se anexar qualquer documento que seja relevante para a rotina de Geração do Arquivo LCDPR.

O botão ![Imagem 27: O botão "Outras opções..." , possui as funcionalidades "Marcar Arquivo como Confirmado" , "Desmarcar Arquivo como…](https://ajuda.sankhya.com.br/hc/article_attachments/16344182131735) **"Outras opções..."**, possui as funcionalidades **"Marcar Arquivo como Confirmado"**, **"Desmarcar Arquivo como Confirmado"** e **"Reprocessar Registros Totalizadores"**.

Quando o botão ![Imagem 28: Quando o botão "Configurações da Tela" for acionado, pode-se realizar a configuração da tela e suas respectivas abas e…](https://ajuda.sankhya.com.br/hc/article_attachments/16344182133783) **"Configurações da Tela"** for acionado, pode-se realizar a configuração da tela e suas respectivas abas e campos de forma mais proveitosa e adequada para o usuário. Além disto, será possível determinar como ocorrerá a geração da numeração da tela, seja **"Automática"** ou **"Manual"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274-Livro-Caixa-Produtor-Rural-LCDPR#top)
