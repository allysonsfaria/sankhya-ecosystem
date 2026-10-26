---
id: "42950999414807"
titulo: "Preenchimento do orçamento por modelos: visão geral e utilização"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950999414807-Preenchimento-do-or%C3%A7amento-por-modelos-vis%C3%A3o-geral-e-utiliza%C3%A7%C3%A3o"
trilha: "MITRA: Planejamento orçamentário  > Preenchimento do orçamento"
atualizado_em: "2026-08-24T13:48:26Z"
rotulos: ["sync_hc", "mitra", "mitra_2", "sync_hash_3b3bd5b22360"]
---

# Preenchimento do orçamento por modelos: visão geral e utilização

## Preenchimento do orçamento por modelos: visão geral e utilização

**Módulo:** Preenchimento do orçamento

**Acesso:** pelo aplicativo ou pelo link exclusivo de preenchimento enviado ao gestor por e-mail.

### O que é e para que serve

A tela de preenchimento é onde o gestor lança os valores do orçamento de um centro de resultado (CR) dentro de um ciclo orçamentário. O conteúdo é organizado em **abas, uma para cada modelo de preenchimento** ativo no CR. Cada modelo define como os valores das contas daquela aba são construídos:

| Modelo | Como os valores são construídos |
| --- | --- |
| **Receita** | Lançamento por quantidade e valor unitário |
| **Base Zero** | Digitação direta dos valores mês a mês, partindo do zero |
| **Base Histórico** | Aplicação de um percentual de crescimento sobre o realizado do ano anterior da conta, com possibilidade de ajuste do valor |
| **Pessoal** | Calculado automaticamente a partir da folha projetada (salários, benefícios, encargos e movimentações), gravado nas contas de pessoal |
| **Modelos de pacote** | Contas orçadas de forma centralizada por um responsável de pacote (por exemplo, Custos de Software), com rateio entre CRs |

As contas que aparecem em cada aba são definidas pela configuração de regras contábeis do projeto (vínculo conta × modelo por CR). Exceções configuradas para um CR específico prevalecem sobre a regra geral.

> **Nota:** as abas exibidas variam por CR, conforme os modelos ativos e as contas vinculadas. Um CR sem contas vinculadas a um modelo não exibe a aba correspondente.

### Visão geral da aba

Toda aba de modelo segue a mesma estrutura:

1. **Cabeçalho** com o nome do modelo, um subtítulo explicativo e o controle de confirmação da aba.
2. **Grade de lançamento** com uma linha por conta e as colunas: **Conta**, os **12 meses** do exercício e o **Total** anual. A última linha é a linha **Total**, que soma todas as contas da aba.
3. **Gráfico Comparativo**, ao final da aba: barras mensais comparando o **Realizado anterior** (ano anterior) com o **Vigente** (meses realizados + meses orçados do ciclo atual). Nas abas de pacote, o gráfico possui alternância entre **Total** e **Por CR**.

### Comportamentos da grade

- Os valores são exibidos no formato numérico brasileiro, sem casas decimais.
- **Meses já realizados ficam travados** (somente leitura). A quantidade de meses travados segue o último mês realizado do ciclo — por exemplo, em um forecast 5+7, os meses de janeiro a maio mostram o realizado e não aceitam edição; o preenchimento ocorre de junho a dezembro.
- **Linhas calculadas por fórmula** são identificadas com um selo (chip) com ícone de calculadora e não aceitam digitação direta — o valor resulta do cálculo configurado no modelo.
- **Linhas personalizadas** do modelo possuem campos de entrada próprios para os valores que alimentam a fórmula.
- Avisos e inconsistências da aba são exibidos em um **banner âmbar** acima da grade.

### Confirmação da aba

Cada aba possui um controle de confirmação. Ao concluir o lançamento de um modelo, confirme a aba: o progresso do CR (modelos confirmados em relação ao total) é atualizado e registrado na trilha de auditoria. A confirmação pode ser desfeita enquanto o CR não for submetido.

> **Importante:** a confirmação de todas as abas é pré-requisito para submeter o CR para aprovação. Consulte o artigo relacionado sobre submissão.

### Comportamentos e pontos de atenção

- Com o CR nos status **SUBMETIDO** ou **APROVADO**, ou com o ciclo **fechado**, a grade fica bloqueada para edição.
- No modelo Pessoal, os valores são recalculados a partir da folha projetada; alterações em colaboradores, benefícios, encargos e movimentações (contratações, desligamentos e aumentos projetados) exigem recálculo para refletir nas contas.
- Desligamentos projetados registrados na versão são considerados no detalhe do preenchimento.
- Nas abas de pacote, o lançamento é do pacote como um todo; a distribuição por CR segue a configuração de rateio do pacote.

### Resultado esperado

Ao concluir o preenchimento de uma aba e confirmá-la, a linha Total reflete a soma das contas, o gráfico Comparativo exibe os meses orçados junto ao realizado, e o progresso de modelos confirmados do CR aumenta. Com todas as abas confirmadas, o CR fica apto à submissão.

### Artigos relacionados

- Como submeter o orçamento de um centro de resultado para aprovação?

---

### Pendências para validação

1. Confirmar os rótulos exatos exibidos na interface para: controle de confirmação da aba, título do gráfico ("Comparativo") e nomes das abas nativas como aparecem para o usuário (Base Zero, Base Histórico, Pessoal, Receita).
2. Confirmar o comportamento exato do recálculo do modelo Pessoal na tela (se automático ou acionado por botão).
