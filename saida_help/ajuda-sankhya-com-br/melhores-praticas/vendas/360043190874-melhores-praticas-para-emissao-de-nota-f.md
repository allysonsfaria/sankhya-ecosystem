---
id: "360043190874"
titulo: "Melhores práticas para emissão de nota fiscal de complemento [Emissão Própria]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043190874-Melhores-pr%C3%A1ticas-para-emiss%C3%A3o-de-nota-fiscal-de-complemento-Emiss%C3%A3o-Pr%C3%B3pria"
trilha: "Melhores Práticas > Vendas"
atualizado_em: "2026-07-31T13:56:09Z"
rotulos: ["DUVIDANF", "Configuração", "Fiscal", "NF-e", "br.com.sankhya.mgecom.mov.selecaodedocumento", "Impostos", "TOP", "Adiciona dados e valores", "Configure \"ACEITARUNITZERO\" e \"QTDZEROCPL\"", "Defina tipo de movimento e custo", "Emissão Própria"]
---

# Melhores práticas para emissão de nota fiscal de complemento [Emissão Própria]

| A Nota Fiscal Complementar é emitida para acrescentar dados e valores antes não informados no documento fiscal original, observando as definições da legislação;  **Fonte:** [Orientação de Preenchimento da NF-e](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=VCrU5SRXeEk=) |
| --- |

![Imagem 1: Caso sua necessidade seja apenas lançar uma nota de complemento já emitida por terceiros, acesse o seguinte artigo:…](https://ajuda.sankhya.com.br/hc/article_attachments/16166137560855) Caso sua necessidade seja apenas lançar uma nota de complemento já emitida por terceiros, acesse o seguinte artigo: [Como lançar uma nota fiscal de complemento emitida por terceiros ?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049467193)

**![Imagem 2: Parâmetros que influenciam:](https://ajuda.sankhya.com.br/hc/article_attachments/16166137563287) Parâmetros que influenciam:**

Antes de iniciar o processo de lançamento, acesse a tela **"[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)"** e verifique os seguintes parâmetros:

- **"ACEITARUNITZERO** **- Aceitar valor unitário igual a zero na venda?": ligado.** Caso o lançamento seja em uma NF-e e o produto realmente tenha que ter valor unitário 0 (zero), o Tipo de Emissão deve ser: 'Complementar' ou 'Ajuste' e o parâmetro **"ACEITARVLRZERO"** ligado.
- **"QTDZEROCPL - Aceita quantidade zero em notas de complemento?": ligado.** Caso seu Contador oriente a lançar o item com quantidade = 0, na nota complementar.
- **"ACEITARVLRZERO - Aceitar valor total igual a zero?"** Caso o lançamento seja em uma NF-e e o produto realmente tenha que ter valor total 0 (zero), o Tipo de Emissão deve ser: 'Complementar' ou 'Ajuste' e o parâmetro **"ACEITARVLRZERO"** ligado.

**![Imagem 3: Como emitir a nota de complemento no sistema ?](https://ajuda.sankhya.com.br/hc/article_attachments/16166154170775) Como emitir a nota de complemento no sistema ?**

- Para geração da nota de complemento é necessário acessar o "**Portal"** ao qual a nota a ser complementada foi lançada. (Portal de Compras/Portal de Vendas).
- Selecione essa nota » **"Outras Opções"** » **"Complemento..."**, conforme imagem abaixo:

![Imagem 4: Selecione essa nota » "Outras Opções" » "Complemento..." , conforme imagem abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/14707388460055)

- Nessa Opção defina a TOP a ser utilizada para esse processo.
- Inserida a TOP, será gerada a nota Complementar.

**(2)** Realize os lançamentos nessa de acordo com as orientações de seu Contador, informando nos respectivos campos os valores a serem complementados.

**(2)** De forma "padrão" costuma-se manter nessa apenas 1 dos itens da nota de origem, excluindo os demais. Além disso, os campos de valor são zerados, mantendo valor apenas nos campos a serem complementados. Exemplo: Complemento de ICMS, inserir valor nos campos **"Base de ICMS"**, **"Alíquota de ICMS"** e **"Vlr. ICMS",** conforme orientações do Contador.

**![Imagem 5: Lançou a nota, mas o imposto inserido não foi destacado?](https://ajuda.sankhya.com.br/hc/article_attachments/16166154173463) Lançou a nota, mas o imposto inserido não foi destacado?**

- Caso a empresa emissora seja **Optante pelo Simples Nacional**, para **destacar o valor do imposto a ser complementado**, deverá ser realizado o lançamento com o **CSOSN = 900**.
- Em caso de **NF-e complementar de ICMS ST,** atente se o Código de Situação Tributária do item está informando, se possui **Substituição Tributária** para que seja destacado os valores.

**![Imagem 6: Quantidade do produto precisa ser 0, mas não está gerando financeiro?](https://ajuda.sankhya.com.br/hc/article_attachments/16166137571479) Quantidade do produto precisa ser 0, mas não está gerando financeiro?**

Possivelmente você está informando o valor unitário do produto na nota. Verifique na tela **"Produtos"**, filtrando pelo produto que será informado na nota, a aba **Venda**, campo **"Digitação na nota:"**.
Para que seja possível gerar o financeiro sem que a quantidade seja informada é necessário (além da ativação dos parâmetros já citados) digitar o Valor Total no item da nota. Portanto, se o campo citado não estiver permitindo 'Quant. e Valor Total', não poderá informar o valor total na nota, e por consequência, não terá financeiro.

**![Imagem 7: Configurações da TOP :](https://ajuda.sankhya.com.br/hc/article_attachments/16166137572631) Configurações da TOP :**

Caso não exista essa TOP parametrizada em sua base, vale ressaltar que a configuração/validação dessa não é uma alçada do Service Desk. E, em caso de necessidade de validações, o consultor de sua Franquia deverá ser acionado. Se optar por proceder com as configurações sem esse apoio, abaixo seguem as orientações principais:

Tela **"[Tipos de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)"** (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de Operação-TOP):

Aba **Geral:**

- O campo **"Tipo de movimento"** deve estar com a mesma opção que está marcada na TOP que está sendo utilizada na nota que será complementada. Ex: Se a nota de origem for com o tipo de movimento venda, a nota complementar deverá ter o tipo de movimento venda.
- Financeiro: 'Não atualizar' (\*\*)

(\*\*)Existem situações em que a nota de complemento deverá gerar atualização de financeiro. Para esses casos além de configurar o campo **"Financeiro"** da aba **Propriedades** conforme desejado, marque o campo **"Atualiza Financeiro na TOP de Origem' da aba Validações"**.

- Atualização do Estoque: **"Nenhuma"**
- Comissão: **"Não calcular"**
- Precifica: **"Não atualiza custo nem preço de venda"** \*\* [ver detalhes no quadro abaixo]

| **![Imagem 8: IMPORTANTE: Cálculo de CUSTO em notas Complementares:](https://ajuda.sankhya.com.br/hc/article_attachments/16166137560855) IMPORTANTE:** Cálculo de CUSTO em notas Complementares:   - Suponhamos uma nota de compra que ATUALIZOU custo, com o item X tendo como custo um valor de R$ 100,00. - Posteriormente, percebeu-se que essa nota foi emitida sem um valor devido de algum imposto que influencia no valor do custo do produto.   Sendo assim, será necessário lançar uma nota complementar para o devido ajuste desse imposto. Como fazer com que o custo do produto em questão fique correto?  ![Imagem 9: Sendo assim, será necessário lançar uma nota complementar para o devido ajuste desse imposto. Como fazer com que o…](https://ajuda.sankhya.com.br/hc/article_attachments/16166137563287) Lance uma nota complementar que atualize custo.  ![Imagem 10: Sendo assim, será necessário lançar uma nota complementar para o devido ajuste desse imposto. Como fazer com que o…](https://ajuda.sankhya.com.br/hc/article_attachments/16166154170775) A fórmula de custos do produto deverá prever essa situação. O conceito é o seguinte:  Deverá ter uma condição para que se a nota for de complemento faça o cálculo conforme necessidade da empresa. Obs.: Um consultor Sankhya poderá auxiliar na criação da fórmula em questão.  ![Imagem 11: Sendo assim, será necessário lançar uma nota complementar para o devido ajuste desse imposto. Como fazer com que o…](https://ajuda.sankhya.com.br/hc/article_attachments/16166154173463) E **qual a data que será atualizada na tabela de custos** no lançamento da nota complementar?  Essa questão é definida através do parâmetro **"DTCOMPCALCCUSTO"**, que pode ser a "Data da Nota de Complemento" ou a "Data da Nota de Origem". |
| --- |

**(3)**Aba **validações:**

- Opção **"Buscar NF de Origem p/ Referenciar?"** marcada, pois toda nota de complemento deve ter uma nota de origem.

**(3)**Aba **Livro Fiscal:**

- Campo **"Modelo do Documento"**, informe o modelo 55 se for uma NF-e.
- Os demais campos desta aba devem ser preenchidos conforme orientações do contador da empresa.

**(3)**Aba **Impostos:**

- Campo **"Tipo de Emissão"** definido como **"Complementar"**
- No campo **"Cálculo de ICMS, IPI e ISS"** deve estar marcada a opção **"Não calcula e Digita"**, pois os impostos serão informados manualmente  conforme valor a ser complementado.
- Os demais campos desta aba devem ser preenchidos conforme orientações do contador da empresa.

![Imagem 12: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/16166137580567) **OBSERVAÇÕES:**

**(2)** Só e possível a marcação do campo **"Cálculo de ICMS, IPI e ISS"** com a opção **"Não calcula e Digita"**, se os campos 'Tem ICMS' ou 'Tem IPI' ou 'Tem ISS' estiverem marcadas. 
 
Caso contrário  o sistema dará um aviso: 

**Passando 'Cálculo de ICMS e IPI' para 'Não calcula e não digita' por que 'Tem ICMS' ou 'Tem IPI' ou 'Tem ISS' estão desmarcados.**

**(2)** Caso a empresa emissora seja **Optante pelo Simples Nacional**, para destacar o valor do imposto a ser complementado, deverá ser realizado o lançamento com o **CSOSN = 900**.

**(3)**Aba **Impressão:**

- 'Base de numeração' deve ser a mesma de venda, pois o cliente está emitindo a nota, se usar outra base de numeração com a mesma série das vendas a SEFAZ irá considerar como uma duplicidade de NF-e;
- A opção **"Numeração somente automática?"** deve estar marcada;
- Tipo de numeração: Empresa/Série;
- NF-e: Complementar.
