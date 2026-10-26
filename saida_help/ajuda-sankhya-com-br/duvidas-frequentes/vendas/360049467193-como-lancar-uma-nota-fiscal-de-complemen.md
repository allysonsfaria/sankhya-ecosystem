---
id: "360049467193"
titulo: "Como lançar uma nota fiscal de complemento emitida por terceiros"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360049467193-Como-lan%C3%A7ar-uma-nota-fiscal-de-complemento-emitida-por-terceiros"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-09-29T15:59:11Z"
rotulos: ["Configuração", "NF-e", "Impostos", "Estoque", "Financeiro", "Lançar nota fiscal de complemento", "Lançar e confirmar dados", "Selecionar nota original", "Documentos Eletrônicos"]
---

# Como lançar uma nota fiscal de complemento emitida por terceiros

| **Observação:** Se a sua dúvida é sobre como **EMITIR** uma nota fiscal de complemento, você deverá acessar o seguinte artigo: [Melhores práticas para emissão de nota fiscal de complemento.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043190874)  Nesse artigo trataremos o **lançamento** de nota fiscal de complemento já emitida por terceiros. |
| --- |

**Parametrizações recomendadas:**

Para emissão de “Nota de Complemento de terceiros” deve existir uma TOP específica, para o lançamento destas.

![Imagem 1: Comercial » Arquivo » Cadastros » ' Tipos de Operação - TOP'](https://ajuda.sankhya.com.br/hc/article_attachments/18942975945495) Comercial » Arquivo » Cadastros » '**Tipos de Operação - TOP'**

**Aba Geral:**

- O campo 'Tipo de movimento' deve estar com a mesma opção que está marcada na TOP que está sendo utilizada na nota que será complementada. Ex: Se a nota de origem for com o tipo de movimento venda, a nota complementar deverá ter o tipo de movimento venda.
- Financeiro = 'Não atualizar' (\*\*)

(\*\*)Existem situações onde a nota de complemento deverá gerar atualização de financeiro. Para esses casos além de configurar o campo 'Financeiro' da aba 'Propriedades' conforme desejado, será necessário marcar o campo 'Atualiza Financeiro na TOP de Origem' da aba Validações.

- Atualização do Estoque = 'Nenhuma'
- Comissão = 'Não calcular'
- Precifica= 'Não atualiza custo nem preço de venda' (\*\*) Verificar exceções na 'Observação 2' ao final do artigo

**Aba Validações:**

- Opção 'Buscar NF de Origem p/ Referenciar?' marcada, pois toda nota de complemento deve ter uma nota de origem.

**Aba Livro Fiscal:**

- Campo 'Modelo do Documento', informar o modelo 55 se for uma NF-e.
- Os demais campos desta aba devem ser preenchidos conforme orientações do contador da empresa.

**Aba Impostos:**

- Campo **"Tipo de Emissão" definido como "Complementar"**
- No campo 'Cálculo de ICMS, IPI e ISS' deve estar marcada a opção 'Não calcula e Digita', pois os impostos serão informados manualmente  conforme valor a ser complementado.
- Os demais campos desta aba devem ser preenchidos conforme orientações do contador da empresa.

**Aba Impressão:**

- A "Base de numeração" da ‘Nota de Complemento de Terceiros’ deve ser "Manual", pois a empresa está recebendo a 'Nota' de um terceiro e terá que dar entrada manualmente.
- Tipo de numeração será "Empresa/Série".
- Campo **'NF-e' : Terceiros**

![Imagem 2: Antes de iniciar o processo de lançamento, acesse a tela 'Preferências' e verifique os seguintes parâmetros:](https://ajuda.sankhya.com.br/hc/article_attachments/18942936246423) Antes de iniciar o processo de lançamento, acesse a tela 'Preferências' e verifique os seguintes parâmetros:

- **QTDZEROCPL** - Aceita quantidade zero em notas de complemento? [**LIGADO**], caso seu Contador oriente a lançar o item com quantidade = 0, na nota complementar.

![Imagem 3: Para lançamento da nota de complemento é necessário acessar o 'Portal' ao qual a nota a ser complementada foi lançada.…](https://ajuda.sankhya.com.br/hc/article_attachments/18942936250775) Para lançamento da nota de complemento é necessário acessar o 'Portal' ao qual a nota a ser complementada foi lançada. ('Portal de Compras'/'Portal de Vendas').

- Selecione essa nota >>'Outras Opções' >> **"Complemento..."**,

![Imagem 4: Nessa Opção defina a TOP a ser utilizada para esse processo. Inserida a TOP, será gerada a nota Complementar.](https://ajuda.sankhya.com.br/hc/article_attachments/18942936255127) Nessa Opção defina a TOP a ser utilizada para esse processo. Inserida a TOP, será gerada a nota Complementar.

![Imagem 5: Lance as informações, conforme nota de terceiros recebida. Por fim, confirme o lançamento.](https://ajuda.sankhya.com.br/hc/article_attachments/18942936258071) Lance as informações, conforme nota de terceiros recebida. Por fim, confirme o lançamento.

**Observações:**

![Imagem 6: Em complementos de importação, as informações da importação são necessárias, logo, na geração da “Nota de Complemento”…](https://ajuda.sankhya.com.br/hc/article_attachments/18942975945495) Em complementos de importação, as informações da importação são necessárias, logo, na geração da “Nota de Complemento” o sistema copiará, automaticamente, as informações referentes a importação, direto da "Declaração de Importação e Adições", deixando zerados os valores, que são referentes apenas ao item da “Nota Original”.

| ![Imagem 7: Cálculo de CUSTO em notas Complementares:](https://ajuda.sankhya.com.br/hc/article_attachments/18942936246423)Cálculo de CUSTO em notas Complementares:   - Suponhamos uma nota de compra que ATUALIZOU custo, com o item X tendo como custo um valor de R$ 100,00. - Posteriormente, percebeu-se que essa nota foi emitida sem um valor devido de algum imposto que influencia no valor do custo do produto.   Sendo assim será necessário lançar uma nota complementar para o devido ajuste desse imposto. Como fazer com que o custo do produto em questão fique correto?  ![Imagem 8: Sendo assim será necessário lançar uma nota complementar para o devido ajuste desse imposto. Como fazer com que o custo…](https://ajuda.sankhya.com.br/hc/article_attachments/18942936250775) Deverá ser lançada uma nota complementar que ATUALIZE CUSTO.  ![Imagem 9: Sendo assim será necessário lançar uma nota complementar para o devido ajuste desse imposto. Como fazer com que o custo…](https://ajuda.sankhya.com.br/hc/article_attachments/18942936255127) A fórmula de custos do produto deverá prever essa situação. O conceito é o seguinte:  Deverá ter uma condição para que se a nota for de complemento faça o cálculo conforme necessidade da empresa. **Observação:** Um consultor Sankhya poderá auxiliar na criação da fórmula em questão.  ![Imagem 10: Sendo assim será necessário lançar uma nota complementar para o devido ajuste desse imposto. Como fazer com que o custo…](https://ajuda.sankhya.com.br/hc/article_attachments/18942936258071) E **qual a data que será atualizada na tabela de custos** no lançamento da nota complementar?  Essa questão é definida através do parâmetro **"Data para cálculo de custos de nota de complemento - DTCOMPCALCCUSTO"**, que pode ser a "Data da Nota de Complemento" ou a "Data da Nota de Origem". |
| --- |
