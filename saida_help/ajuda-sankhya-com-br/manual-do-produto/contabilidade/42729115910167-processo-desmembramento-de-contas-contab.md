---
id: "42729115910167"
titulo: "Processo Desmembramento de Contas Contábeis"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42729115910167-Processo-Desmembramento-de-Contas-Cont%C3%A1beis"
trilha: "Manual do Produto > Fiscal e Contábil > Contábil > Contabilidade"
atualizado_em: "2026-08-14T18:27:24Z"
---

# Processo Desmembramento de Contas Contábeis

Módulo: Contabilidade

Caminho de acesso: **Menu Principal › Contabilidade › Cadastros › Plano de Contas**

Telas associadas a esta jornada: [Plano de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608054-Plano-de-Contas) · [Lançamentos Contábeis](https://ajuda.sankhya.com.br/hc/pt-br/articles/42729115910167-Processo-Desmembramento-de-Contas-Cont%C3%A1beis) · [Importação de Lote](https://ajuda.sankhya.com.br/hc/pt-br/articles/42729115910167-Processo-Desmembramento-de-Contas-Cont%C3%A1beis) · [Balancete de Verificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/42729115910167-Processo-Desmembramento-de-Contas-Cont%C3%A1beis) · [Plano de Contas Referencial](https://ajuda.sankhya.com.br/hc/pt-br/articles/42729115910167-Processo-Desmembramento-de-Contas-Cont%C3%A1beis)

## O que é e para que serve

O Processo Desmembramento de Contas Contábeis orienta você a separar uma conta contábil existente em várias contas novas (1 para N), transpondo o saldo da conta original para as novas e remapeando tudo o que apontava para ela. Ele é voltado a contadores, controllers e consultores de implantação, e atende principalmente à adequação de apresentação exigida pelo CPC 51. Este processo não executa o rateio do saldo por você nem classifica contas automaticamente na nova estrutura de apresentação: a decisão de rateio e de classificação é sempre do contador responsável.

**💡 Dica**

Se você só precisa classificar as contas na nova estrutura de apresentação do CPC 51 (categoria/subcategoria), talvez não precise desmembrar nenhuma conta — basta classificar as existentes e abrir contas novas já classificadas para o próximo exercício. O desmembramento com transposição de saldo só é necessário quando uma única conta reúne saldos que precisam ser fisicamente separados. Na dúvida, confirme com o contador.

## Antes de começar

Reestruturar o plano de contas mexe em saldo, lançamentos e obrigações acessórias (ECD/ECF). Resolva os pré-requisitos abaixo, todos fora da tela de execução:

- Faça o procedimento na virada de exercício: inative a conta antiga na data-corte e abra as novas no exercício seguinte.
- Faça uma cópia de segurança da base e valide primeiro em homologação.
- Envolva o contador responsável: o sistema executa, mas a decisão de rateio e classificação é dele.
- Confira o bloqueio do período: períodos com fechamento contábil ou fiscal bloqueado não aceitam lançamento.

**🚨 Risco operacional**

Não reescreva período já escriturado. Se a ECD do período anterior já foi entregue, alterações retroativas podem exigir arquivo de substituição, com impacto fiscal. Avalie com o Fiscal antes de qualquer ativação ou inativação retroativa.

## Visão geral do processo

| Passo | O que fazer | Tela |
| --- | --- | --- |
| 1 | Cadastrar as contas novas (filhas) | Plano de Contas |
| 2 | Inativar a conta antiga (mãe) | Plano de Contas |
| 3 | Transpor o saldo da mãe para as filhas | Lançamentos Contábeis ou Importação de Lote |
| 4 | Remapear tudo que apontava para a conta antiga | Diversas telas |
| 5 | Reamarrar o referencial ECD/ECF das contas novas | Plano de Contas (aba Conta Contábil Referencial) |
| 6 | Conferir os saldos e, se preciso, reverter | Balancete de Verificação / Lançamentos Contábeis |

## Passo 1 — Cadastrar as contas novas

Cadastre as contas-filhas na tela Plano de Contas. Antes, confirme a máscara das contas em **Contabilidade › Preferências ›** [**Empresa**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa) › aba [**Plano de Contas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa#abaplanodecontas) — o código precisa respeitar a máscara e o grau analítico (último grau da máscara).

Para cada conta-filha, clique em **Novo** e preencha:

- **Descrição** — informe o nome da conta (obrigatório).
- **Conta Contábil** — informe o código conforme a máscara (obrigatório).
- **Aceita Lançamento Manual** — marque para permitir o lançamento de transposição do Passo 3.

### Geral

Nesta aba, replique os atributos da conta antiga:

- **Analítica** — marque quando a conta recebe lançamento (sintética não recebe e exige filhas).
- **Grupo de Conta** — selecione a opção correspondente (01-Ativo, 02-Passivo, 03-Patrimônio Líquido, 04-Resultado, 05-Compensação, 09-Outras).
- **Tipo** — apresentado quando o grupo é de resultado; selecione Receita ou Despesa.
- **Centro de Resultado obrigatório** e **Projeto obrigatório** — marque se a antiga exigia.
- **Ativa** — marque para ativar a conta.
- **Natureza para EFD**, **Tipo de Saldo e-LALUR**, **Cód. Razão Auxiliar** e **Possui Razão Auxiliar SPED** — replique conforme a original.

**💡 Dica**

No botão **Outras Opções**, a opção **Gerar código da conta contábil automático** preenche o código a partir da conta-pai, e **Inclusão Contínua** permite cadastrar várias contas sem clicar em **Novo** a cada uma.

## Passo 2 — Inativar a conta antiga (mãe)

Na tela [Plano de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608054-Plano-de-Contas), localize a conta-mãe, clique em **Editar** e abra a aba **Geral**:

- **Referência de Inativação** — informe a data-corte (ex.: 31/12 do exercício que encerra). A partir dela, a conta não recebe mais lançamento. A data deve ser posterior à de ativação.
- **Conta Substituta** — opcional, mas recomendado. Informe a conta que passa a receber as referências que ainda apontem para a antiga.

A conta-mãe não é excluída: fica inativa e preservada, mantendo o histórico. Se deixar a conta como **Ativa** ao informar a substituta, o sistema alerta que isso só faz sentido para lançamentos em datas anteriores.

**⚠️ Atenção**

O campo **Conta Substituta** depende de **Referência de Inativação**: sem a referência, o sistema exibe "Para substituir uma conta, é necessário informar uma referência de inativação" e não aceita a substituta.

## Passo 3 — Transpor o saldo da conta antiga para as novas

Não há rotina automática de quebra de saldo. A transposição é feita por um lançamento contábil de transferência, com o rateio calculado pelo contador. Existem dois caminhos: manual (para poucas contas) e de volume (para várias contas).

**⚠️ Atenção**

Para os dois caminhos, o lote contábil de destino já deve existir e estar dentro do Intervalo de Lotes para Lançamento Manual definido em **Contabilidade › Preferências › Empresa** › aba **Lançamentos**. Sem esse intervalo, o sistema recusa lançamentos manuais.

### Caminho A — Lançamentos Contábeis

Ideal para operações manuais e poucas contas. Na tela Lançamentos Contábeis, clique em **Novo Lançamento**. No cabeçalho, preencha **Referência**, **Núm. Lote** (o existente), **Data Movimento** (data-corte) e **Núm. Documento**. Use Múltiplas Partidas.

Exemplo com uma conta credora de R$ 1.200.000,00:

| Conta Contábil (Red.) | Valor Débito | Valor Crédito | Cód. Histórico |
| --- | --- | --- | --- |
| 2.02.001 (mãe) | 1.200.000,00 | — | Desmembramento CPC 51 |
| 2.02.001.01 Financiamento | — | 600.000,00 | Desmembramento CPC 51 |
| 2.02.001.02 Operacional | — | 450.000,00 | Desmembramento CPC 51 |
| 2.02.001.03 Tributos | — | 150.000,00 | Desmembramento CPC 51 |

O **Total Débito** deve ser igual ao **Total Crédito** (R$ 1.200.000,00). Se houver diferença, o sistema exibe "O valor da soma dos créditos deve ser igual ao valor da soma dos débitos" e não salva. Preencha **Centro de Resultado** e **Projeto** se exigidos e clique em **Salvar**.

### Caminho B — Importação de Lote

Ideal para volume e várias contas. Na tela [Importação de Lote](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116513-Importa%C3%A7%C3%A3o-de-Lote), selecione **Tipo de Arquivo** = **Arquivo XLS**, marque as opções aplicáveis e clique em **Importar**. Utilize a planilha de importação de lançamentos em lote padrão do sistema. Remova a linha descritiva antes de importar. Colunas principais:

| Coluna | Conteúdo | Regra |
| --- | --- | --- |
| `NUMLOTE` | Número do lote | 1 a 32767 |
| `NUMLAN` | Número do lançamento | Diferente de zero |
| `CODCTACTB` | Conta contábil | Extenso, sem pontuação (ex.: 202001) |
| `CODCONPAR` | Conta de contrapartida | Texto Simples |
| `REFERENCIA` | Mês de referência | 1 a 12 |
| `DTMOV` | Dia do movimento | 1 a 31 |
| `CODCENCUS` | Centro de Resultado | Numérico |
| `VLRLANC` | Valor | Em centavos, sem separador (R$ 1.200.000,00 = 120000000) |
| `CODHISTCTB` | Código do histórico padrão | Até 32700 |
| `COMPLHIST` | Complemento do histórico | Até 140 caracteres |
| `TIPLANC` | Tipo | D (débito) ou R (crédito) |
| `VENCIMENTO` | Data | dd/mm/aaaa |

**⚠️ Atenção**

O campo `VLRLANC` é em centavos. Formate as colunas de conta e contrapartida como Texto Simples no Excel. Salve o nome do arquivo sem acentos, espaços ou caracteres especiais.

## Passo 4 — Mapear as referências à conta antiga

Percorra cada tela e aponte para as novas contas. Para saber mais, acesse os artigos de cada rotina:

- [**TOP (Tipo de Operação)**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) **— Contabilização:** TOPs de faturamento/compras que usavam a conta como contrapartida.
- [**Integração Contábil × Financeiro:**](https://ajuda.sankhya.com.br/hc/pt-br/articles/37829431700759-Como-configurar-e-executar-a-contabiliza%C3%A7%C3%A3o-financeira) relação empresa × natureza × conta contábil.
- [**Integração da Folha**](https://ajuda.sankhya.com.br/hc/pt-br/articles/7080867168151-Integra%C3%A7%C3%A3o-Cont%C3%A1bil-da-Folha-de-Pagamento)**:** contas de débito/crédito por evento e exceções por tipo de folha/departamento.
- [**Imobilizado / Depreciação**](https://ajuda.sankhya.com.br/hc/pt-br/articles/37827266925207-Como-calcular-deprecia%C3%A7%C3%A3o-de-bens-patrimoniais)**:** conta contábil do bem.
- **Provisões e rotinas específicas:** devedores duvidosos, férias/13º, IFRS 15/16, se aplicável.
- [**Demonstrativos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/39229659689239-Demonstrativos-Cont%C3%A1beis-DRE)**:** contas do DRE, Balanço e DFC.
- [**Orçamento Contábil**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111473-Planejamento-Or%C3%A7ament%C3%A1rio-Cont%C3%A1bil)**:** metas e orçamento por conta.

**⚠️ Atenção**

Este passo é manual, feito conta a conta. Se uma conta ficar sem remapear, a contabilização passa a falhar ou a cair em conta errada.

## Passo 5 — Amarrar o referencial ECD/ECF

Na tela [Plano de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608054-Plano-de-Contas), para cada conta nova abra a aba **Conta Contábil Referencial** e informe o **Tipo** e o **Código da Conta Referencial** correspondente (CFC/RFB), conforme cadastrado na tela Plano de Contas Referencial. Sem esse vínculo, a geração do SPED pode ser rejeitada.

**ℹ️ Nota**

Contas dos grupos 05-Compensação e 09-Outras não devem ter conta referencial vinculada.

## Passo 6 — Conferir e, se necessário, reverter

Para conferir, emita o Balancete de Verificação e a Razão e confirme que o saldo saiu integralmente da conta antiga e entrou nas novas (a soma das filhas deve ser igual ao saldo original da mãe).

Para reverter, exclua o lote gerado no Passo 3 e o lançamento de transposição volta a zero. Para ajustar um lançamento já contabilizado sem apagá-lo, clique em **Estornar** na tela [Lançamentos Contábeis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173-Lan%C3%A7amentos-Cont%C3%A1beis) — isso gera um lançamento inverso, preserva o original e mantém o rastreamento.

**⚠️ Atenção**

A exclusão do lote reverte apenas os lançamentos, não os remapeamentos. Se você já reapontou referências no Passo 4, desfaça esses reapontamentos manualmente.

## Checklist final

- Cópia de segurança feita e teste em homologação concluído.
- Contas novas cadastradas com todos os atributos (grupo, CR/Projeto, Natureza EFD, e-LALUR).
- Conta antiga inativada na data-corte, com conta substituta informada.
- Lote de transposição gerado, com débitos iguais aos créditos.
- Saldo conferido no Balancete (soma das filhas = saldo da mãe).
- Referências remapeadas (TOP, financeiro, folha, imobilizado, demonstrativos, orçamento).
- Referencial ECD/ECF das novas contas reamarrado.
- Bloqueio de período verificado; ECD anterior avaliada com o Fiscal.

## Perguntas frequentes

### Posso desmembrar várias contas de uma vez?

Sim. Pela tela Importação de Lote você monta o lançamento de transposição de todas as contas em uma planilha e importa de uma vez.

### Preciso mesmo mover o saldo histórico?

Nem sempre. Se a adequação se resolve classificando as contas existentes e abrindo contas novas para o próximo exercício, o desmembramento com transposição pode não ser necessário. Confirme com o contador.

### A conta antiga é apagada?

Não. É inativada por data e preservada, com o histórico intacto.

### Dá para desfazer?

O lançamento de transposição é reversível ao excluir o lote. Os remapeamentos do Passo 4 precisam ser desfeitos manualmente.
