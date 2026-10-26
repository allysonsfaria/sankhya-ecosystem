---
id: "360044607634"
titulo: "Contabilização de Devedores Duvidosos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607634-Contabiliza%C3%A7%C3%A3o-de-Devedores-Duvidosos"
trilha: "Manual do Produto > Fiscal e Contábil > Contábil > Contabilização"
atualizado_em: "2026-07-29T16:01:21Z"
rotulos: ["AJUDA DO SKW", "manual", "Parceiro", "Movimentação Financeira", "Centro de Resultado", "Gerência de Cobrança", "PDD", "Cálculo de Juros e Multa", "Contabilização de Devedores Duvidosos", "br.com.sankhya.contabilizacao.devedores.duvidosos", "Contabilização de Devedores Duvidosos manual", "Crédito", "Contabilização", "Financeiro", "Contabilização de Devedores Duvidosos: Processo e Configurações"]
---

# Contabilização de Devedores Duvidosos

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42314898503703) Módulo: Contabilização > Arquivos
```

---

![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/7175337972375)

Em diversas atividades empresariais, é comum a empresa ter títulos de clientes que já estão vencidos a algum tempo. Estes títulos podem constituir **"Perdas no Recebimento de Créditos"**, esta é a caracterização da **"Provisão de Devedores Duvidosos" (PDD)**.

No fim de cada exercício social, é facultado às empresas considerar, em seus demonstrativos contábeis, uma parcela de seus recebíveis como perda do período.

Nesta tela, são listados apenas títulos não contabilizados e que possuam a marcação **"PDD"** realizada.

Os títulos poderão ser marcados como PDD através das telas [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874), [Gerência de Cobrança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606894) e [Cálculo de Juros e Multas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115373-C%C3%A1lculo-de-Juros-e-Multas).

Nesta tela, a **"Empresa do Lote"** trará as empresas ativas pelo módulo MGE Contabilidade (ainda não implementado no Sankhya Om).

Informe em **"Data Movimento"**, a data em que o sistema deverá verificar para trazer os títulos.

O **"Número Lote"** corresponde ao número do lote a ser contabilizado. Se para a empresa e período informados já tiver lote com o número informado e movimentos já contabilizados, o sistema emitirá uma mensagem informando que o número do lote já foi utilizado.

No campo **"Debitar"** será informado a conta contábil de Débito.

Em **"Creditar"**, informe a conta contábil de Crédito.

Ao habilitar a marcação **"Usar Centro de Resultado?"**, o sistema buscará o Centro de Resultado informado no campo **"Centro de Resultado"** da aba [Lançamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874#abalanamento) da [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira). Porém, se esse campo não estiver preenchido, o sistema irá considerar o valor **"0"** para a contabilização.

Além disso, se a marcação **"Centro de Resultado obrigatório"** do [Plano de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608054-Plano-de-Contas) utilizado estiver selecionada, a marcação Usar Centro de Resultado, também deve ser habilitada.

**Observação:** a marcação Usar Centro de Resultado? será apresentada na tela Contabilização de Devedores Duvidosos, quando a marcação **"Utiliza centro de resultado"** da aba [Lançamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa#abalanamentos) da tela [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa) (Contabilidade > Preferências) estiver ligada.

No campo **"Dias Atraso"** virá informado o número de Dias incluído no parâmetro **"Dias considerar atraso de devedores duvidosos - DIASDEVDUVIDOSO"**. Este campo influenciará no filtro, ao trazer os títulos para serem contabilizados. Sendo assim, considere o exemplo:

      Parâmetro DIASDEVDUVIDOSO: 180

      Data do movimento: 01/08/2012

      Dias atraso: 180

      Último dia do mês da data de movimento: 31/08/2012 menos 180 dias.

      Os títulos com data de vencimento menor ou igual a 31/08/2012 menos 180 dias.

**Fórmula:** Data de Vencimento menor ou igual Último Dia do mês da Data de Movimento – Dias de Atraso.

Informe o **"Histórico"** para contabilização. Estes são cadastrados previamente no MGE Contabilidade > Arquivos > Históricos Padrões.

Caso seja necessário informar um complemento do histórico, insira-o no campo **"Complemento"**. Ele pode ser preenchido com as seguintes variáveis:

- **Dados do Financeiro:** HH, NF, DN, DV, DM, DB, NS, NC, CE, DD
- **Dados do Parceiro:** NP, RP, NO, RS
- **Dados Conta Bancária:** CC, CD
- **Dados Contato:** CT
- **Dados Tipo de Título:** ED

**Seção Lançamentos**

Se a marcação **"Agrupar"** for selecionada, todos os títulos selecionados na grade serão agrupados em um lançamento (crédito e débito) na Contabilidade.

**Importante:** O MGE e o Sankhya Om possuem o mesmo comportamento na visualização e geração dos lotes na contabilidade mas, internamente, na tabela TCBINT as informações serão gravadas de forma diferente: No MGE, nesta tabela, grava-se uma linha para o Débito e outra para o Crédito e, no Sankhya Om, mesmo configurada para agrupar, será gravado uma linha para cada.

Se você efetuar a marcação **"Não Agrupar"**, o sistema gerará na Contabilidade um lançamento (crédito e débito) para cada título.

**Observação:** A quantidade de títulos na grade é informada na parte superior da tela, no lado direito, através do balão.

No campo **"Valor Total de Títulos"** será exibido o valor total dos títulos que estiverem selecionados na grade.

No alto da tela, temos o botão **"Exportar grade para PDF" ![Imagem 3: No alto da tela, temos o botão "Exportar grade para PDF" , onde você define como será realizada a visualização dos…](https://ajuda.sankhya.com.br/hc/article_attachments/360082845814)**, onde você define como será realizada a visualização dos resultados da tela, podendo utilizar as seguintes opções:

- **Exportar como PDF:** Por esta opção, teremos as informações no formato PDF.
- **Exportar como planilha:** Através desta opção, os dados serão baixados automaticamente no formato XLS.
- **Visualizar em cubo...:** Por esta alternativa, será aberta uma tela referente ao visualizador de arquivos contendo as informações em cubo.
