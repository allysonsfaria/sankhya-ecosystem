---
id: "42613709084567"
titulo: "Guia Usuário Simulação de Preços"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42613709084567-Guia-Usu%C3%A1rio-Simula%C3%A7%C3%A3o-de-Pre%C3%A7os"
trilha: "Sankhya Official Pack - SOP > ImpEx"
atualizado_em: "2026-09-08T11:30:05Z"
---

# Guia Usuário Simulação de Preços

Guia do Usuário — Simulação de Custos e Preços (TCESIM)

ImpEx — Comércio Exterior

Simulação de Preços · TCESIM

### Simulação de Custos e Preços de Importação

Módulo: ImpEx

Comércio Exterior

Tabela: TCESIM

Instância: CustoPrecoImportacao

Analistas de importação, compradores e responsáveis por formação de preço

**O que você vai fazer aqui:** transformar o preço pago ao fornecedor no exterior no **custo real** do produto nacionalizado — já com todos os impostos e despesas — e definir o **preço de venda sugerido**. No final, vira um pedido com um clique. O ponto-chave: você quase nunca cria a simulação; ela nasce sozinha. Seu trabalho é conferir e ajustar.

Você lança os itens da importação

→

Sistema cria a simulação e calcula o custo

→

Você define a margem

→

Sistema calcula o preço sugerido

→

Você gera o pedido

#### Onde a simulação aparece

A simulação está amarrada a um **processo de importação** (NUIMP). Cada linha representa **um produto** daquele processo, com seu custo apurado e seu preço sugerido. A chave que identifica cada linha é:

| Campo | Significado |
| --- | --- |
| `CODSIMU` | Código sequencial da simulação (gerado automaticamente) |
| `NUIMP` | Número do processo de importação a que a linha pertence |

**O que estou vendo em cada linha?**

O produto (`CODPROD`), o lote (`CONTROLE`), o custo simulado já com impostos, a margem de lucro e o preço sugerido. Os campos de custo, empresa, produto e local vêm travados para leitura — são calculados, não digitados.

#### Etapa 1 — A simulação nasce sozinha

Você **não abre** a tela para criar uma linha do zero. Ela é criada automaticamente no momento em que um **item da importação** (tabela TCEITE) é lançado no processo.

**O que acontece nos bastidores quando você insere um item:**

1. O sistema soma todos os tributos daquele item.
2. Divide pela quantidade negociada para chegar ao **custo por unidade**.
3. Cria a linha na simulação já com o custo preenchido.
4. Puxa a **margem de lucro padrão do cadastro do produto** como ponto de partida.

**Por que é automático?**

O custo de importação só é conhecido depois que os impostos e despesas do item estão calculados. Deixar o sistema criar a simulação garante que o custo sempre reflita o que foi lançado no item — sem redigitação e sem erro de conta.

E se você **alterar** o item depois (mudar quantidade, corrigir um imposto)? O sistema **recalcula o custo** e atualiza a linha automaticamente. Você não precisa fazer nada.

#### Etapa 2 — Entendendo o custo simulado

O campo **Custo Simulado (CUSSIMU)** é o coração da tela: o custo real, por unidade, do produto já nacionalizado. Entender como ele é montado explica por que o número muda conforme a empresa e os incoterms.

#### O que sempre entra na conta

O sistema soma, para o item: Base do II (`BASEII`), Imposto de Importação (`VLRII`), taxa SISCOMEX (`VLRSISCOMEX`), AFRMM (`VLRAFRMM`), Destaque (`VLRDESTAQUE`), ICMS (`VLRICMS`) e IPI (`VLRIPI`).

#### O que entra dependendo da empresa

**Empresa do Simples × empresa normal**Se a empresa **não é do Simples** (`SIMPLES = N`), o sistema também soma **PIS e COFINS** e considera as **despesas complementares**. Se a empresa **é do Simples**, PIS/COFINS não entram no custo e o cálculo é mais direto.

#### Despesas complementares e rateio por Incoterms

Para empresas fora do Simples, se o processo tem despesas marcadas como **complementares de custo** (`CUSTOCOMP = 'S'` na tabela TCEDESP), o sistema rateia essas despesas entre os itens conforme o critério do **Incoterms**:

| Critério (no Incoterms) | Como o sistema distribui |
| --- | --- |
| **P** — por peso | Proporcional ao peso líquido de cada item |
| **V** — por valor | Proporcional ao valor total de cada item |

**Incoterms sem critério = erro**

Se o Incoterms do processo não tiver um critério de rateio definido, o sistema **interrompe o cálculo com erro**. Verifique o cadastro do Incoterms antes de lançar as despesas.

###

### O passo final

Depois de somar tudo, o sistema **divide pela quantidade negociada (QTDNEG)** para chegar ao custo unitário, usando o número de casas decimais do cadastro do produto (`DECVLR`).

#### Etapa 3 — Definindo sua margem e o preço de venda

Aqui você **entra em ação**. Na linha da simulação, informe a **Margem de Lucro (MARGEMLUCRO)** em percentual. Ao salvar, o sistema calcula o **Preço Sugerido (PRECOVENDA)**:

```
Preço Sugerido = Custo Simulado × (1 + Margem% / 100)
```

| Custo Simulado | Margem informada | Preço Sugerido |
| --- | --- | --- |
| R$ 100,00 | 30% | R$ 130,00 |
| R$ 100,00 | 50% | R$ 150,00 |
| R$ 100,00 | 0% (ou em branco) | R$ 100,00 |

- **Margem zero = preço igual ao custo**

Útil quando você quer só transferir o custo sem markup (transferências entre filiais, por exemplo).

- **O preço se recalcula toda vez que você mexe na margem.**

Não há botão de "calcular" — basta alterar a margem e salvar.

#### Etapa 4 — Gerando o pedido a partir da simulação

Com custos apurados e preços definidos, você transforma a simulação em um **pedido de verdade** usando o botão de ação **Gerar Pedido**.

#### O que você informa

| Campo | O que é |
| --- | --- |
| **TOP (CODTIPOPER)** | O tipo de operação do pedido que será gerado |
| **Processo (NUIMP)** | A importação de onde os itens e preços virão |
| **Parceiro (CODPARC)** | O parceiro (cliente/fornecedor) do pedido |

###

#### O que o sistema faz por você

1. Localiza o **pedido de compra original** vinculado ao processo e o **duplica** como base do novo pedido.
2. Cria o novo cabeçalho de nota, zerando número, datas e série (é um pedido novo).
3. Para cada produto da simulação, insere um item usando a quantidade e a unidade do item de importação, o **Preço Sugerido** como valor unitário, o lote e o local de origem.
4. Grava no processo o número da nota gerada (em `NUNOTASIMU` ou `NUNOTAPEDIMP`, conforme a TOP).

**Regras que a TOP precisa respeitar**A rotina só aceita TOPs de **Pedido de Venda** (`TIPMOV = P`) ou TOPs de **Compra que geram Importação** (`TIPMOV = O` com `GERAIMP = S`). Qualquer outro tipo é recusado com a mensagem: "Permitido apenas TOPs do tipo pedido de venda! ou Tops de compra que geram Importação".

**Outras validações que você pode encontrar:**

- **"Processo não possui pedido de compras"** — a geração só funciona para processos com um pedido de compra de origem.
- **"Já existe Pedido de Importação vinculado a esse processo"** — o sistema bloqueia para não duplicar o pedido de importação.
- Se já existia uma nota de simulação (`NUNOTASIMU`) e você gera um novo pedido de venda, o sistema remove a nota antiga e refaz o vínculo.

#### Etapa 5 — Se precisar refazer: excluir a nota gerada

Errou a margem? Escolheu a TOP errada? Sem problema. Ao **excluir a nota** gerada a partir da simulação, o sistema automaticamente **limpa o vínculo** no processo de importação (zera o `NUNOTASIMU`). O processo volta a ficar liberado para você **gerar o pedido novamente**, com os valores corrigidos.

**A simulação não é apagada**A linha TCESIM (custo, margem e preço) continua lá para você ajustar e regerar. Apenas o vínculo com a nota é desfeito.

#### Os campos da simulação, um por um

| Campo | Nome na tela | O que é | Edita? |
| --- | --- | --- | --- |
| `CODSIMU` | Cód. Simulação | Código sequencial da simulação | Não (automático) |
| `NUIMP` | Nro. Importação | Processo de importação da linha | Não |
| `SEQUENCIA` | Sequência | Sequência do item dentro do processo | Não (travado) |
| `CODEMP` | Cód. Empresa | Empresa da importação | Não (travado) |
| `CODPROD` | Cód. Produto | Produto simulado | Não (travado) |
| `CODLOCAL` | Cód. Local | Local financeiro / estoque | Não (travado) |
| `CONTROLE` | Lote | Lote do produto | Não |
| `CUSSIMU` | Custo Simulado | Custo unitário real com impostos e despesas | Não (calculado) |
| `MARGEMLUCRO` | % Margem de Lucro | Percentual de markup sobre o custo | **Sim** ✏️ |
| `PRECOVENDA` | Preço Sugerido | Preço de venda calculado a partir da margem | Não (calculado) |

**Relacionamentos:** Cada linha se conecta ao **Produto**, ao **Cabeçalho de Importação** (via NUIMP), à **Empresa** e ao **Local Financeiro**.

- **Na prática, o único campo que você digita é a Margem de Lucro**

Todo o resto é preenchido ou calculado pelo sistema.

#### Situações comuns e como resolver

| O que aconteceu | Por que | O que fazer |
| --- | --- | --- |
| A linha de simulação não apareceu | A simulação nasce junto com o item da importação | Verifique se o item (TCEITE) foi realmente lançado |
| O custo veio diferente do esperado | Simples × normal muda a conta (PIS/COFINS e despesas) | Confira o campo `SIMPLES` da empresa e as despesas complementares |
| Uma despesa não entrou no custo | A despesa não está marcada como complementar | Marque a despesa com `CUSTOCOMP = 'S'` |
| Erro sobre critério de rateio não definido | O Incoterms não tem critério (P ou V) | Ajuste o cadastro do Incoterms com o critério de rateio |
| O preço não mudou após editar a margem | A alteração não foi salva | Salve a linha após digitar a margem |
| "Processo não possui pedido de compras" | O processo não tem pedido de compra de origem | Só é possível gerar pedido para processos com pedido de compra |
| "Permitido apenas TOPs do tipo pedido de venda..." | A TOP não é de venda nem de compra que gera importação | Use TOP com `TIPMOV = P` ou `TIPMOV = O` + `GERAIMP = S` |
| "Já existe Pedido de Importação vinculado" | O processo já tem pedido de importação gerado | Exclua o pedido/nota anterior antes de gerar de novo |
| Quero refazer o pedido gerado | O vínculo trava a nova geração | Exclua a nota gerada — o vínculo é limpo |

### FAQ - Perguntas e erros mais frequentes

#### Sobre a criação da simulação

**1. Preciso criar a linha de simulação manualmente?**
Não. A simulação é criada automaticamente quando você lança um **item da importação (TCEITE)**. Se a linha não apareceu, o item ainda não foi lançado.

**2. Lancei o item, mas a linha de simulação não apareceu. Por quê?**
Confirme se o item foi realmente **gravado** no processo. A simulação só é criada depois que o item é efetivamente salvo. Se o lançamento deu erro no meio, a simulação não chega a ser gerada.

**3. Alterei a quantidade do item depois. Preciso refazer a simulação?**
Não. Ao alterar o item, o sistema **recalcula o custo** e atualiza a linha da simulação sozinho.

#### Sobre o custo simulado

**4. Por que o custo simulado veio diferente do que eu esperava?**
O cálculo depende do regime da empresa. Para empresa **fora do Simples**, entram PIS, COFINS e despesas complementares; para empresa do **Simples**, esses valores não entram. Verifique o campo `SIMPLES` da empresa.

**5. Uma despesa que eu paguei não entrou no custo. O que houve?**
Só entram no custo as despesas marcadas como **complementares de custo** (`CUSTOCOMP = 'S'`). Marque a despesa dessa forma na tela de despesas do processo e o custo será recalculado.

**6. O que significa o erro "Critério de rateio de Outras Despesas não foi definido no incoterms"?**
O **Incoterms** do processo não tem critério de rateio configurado. Abra o cadastro do Incoterms e defina o critério: **P** (por peso) ou **V** (por valor). Sem isso, o sistema não consegue distribuir as despesas complementares entre os itens.

**7. O custo mudou depois que alterei o Incoterms do processo. É normal?**
Sim. O critério do Incoterms (por peso ou por valor) muda a forma como as despesas complementares são rateadas, alterando o custo de cada item.

#### Sobre a margem e o preço

**8. Editei a margem, mas o preço sugerido não mudou. Por quê?**
O preço só é recalculado **ao salvar** a linha. Digite a margem e salve — o preço sugerido é atualizado automaticamente.

**9. Deixei a margem em branco/zero e o preço ficou igual ao custo. É erro?**
Não, é o comportamento esperado. Margem zero significa "sem markup": o preço sugerido fica igual ao custo simulado.

**10. Posso digitar o preço sugerido direto, sem informar margem?**
Não é o fluxo previsto. O preço sugerido é **calculado** a partir do custo e da margem. Para chegar a um preço específico, ajuste a margem até obtê-lo.

#### Sobre a geração do pedido

**11. O que significa o erro "Processo não possui pedido de compras"?**
A geração de pedido só funciona para processos com um **pedido de compra de origem** vinculado. Sem esse pedido, o sistema não tem uma nota-base para duplicar.

**12. O que significa o erro "Permitido apenas TOPs do tipo pedido de venda! ou Tops de compra que geram Importação"?**
A TOP escolhida não é compatível. Use uma TOP de **Pedido de Venda** (`TIPMOV = P`) **ou** uma TOP de **Compra que gera Importação** (`TIPMOV = O` com `GERAIMP = S`).

**13. O que significa o erro "Já existe Pedido de Importação vinculado a esse processo"?**
O processo já tem um pedido de importação gerado. Para gerar novamente, exclua antes o pedido/nota anterior.

**14. Gerei o pedido, mas com valores errados. Como refaço?**
Exclua a **nota gerada**. Ao excluí-la, o sistema limpa automaticamente o vínculo no processo, e a simulação fica liberada para você ajustar a margem e **gerar o pedido novamente**.

**15. O que acontece com a simulação quando eu excluo a nota gerada?**
A simulação (custo, margem e preço) **não é apagada** — apenas o vínculo com a nota é desfeito. Você pode reaproveitá-la para regerar o pedido.

**16. Com que preço o pedido é gerado?**
Cada item do pedido usa o **Preço Sugerido (PRECOVENDA)** da simulação como valor unitário, junto com a quantidade e a unidade do item de importação.
