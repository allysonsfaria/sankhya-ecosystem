---
id: "42427451867671"
titulo: "Preservando ou resetando fórmulas ao editar a integração Sankhya"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427451867671-Preservando-ou-resetando-f%C3%B3rmulas-ao-editar-a-integra%C3%A7%C3%A3o-Sankhya"
trilha: "PLOOMES: Automação de propostas  > Geral"
atualizado_em: "2026-08-10T18:01:56Z"
rotulos: ["sync_hc", "ploomes", "ploomes_14741545", "sync_hash_c33afaf3932a"]
---

# Preservando ou resetando fórmulas ao editar a integração Sankhya

## Sobre o comportamento de fórmulas na edição da integração Sankhya

A integração Sankhya utiliza **fórmulas em campos do tipo desenvolvedor** para realizar consultas em tempo real ao ERP e para calcular automaticamente valores em documentos como Propostas e Vendas. Essas fórmulas são fundamentais para o funcionamento da integração e muitas vezes são customizadas durante a implementação para atender a regras específicas de cada cliente.

Ao aplicar uma edição na configuração da integração Sankhya, o administrador tem a possibilidade de **manter as fórmulas atuais** da conta ou **resetá-las para o padrão** da integração. Essa escolha é apresentada em um modal no momento da confirmação da edição.

![Imagem 1: Ao aplicar uma edição na configuração da integração Sankhya, o administrador tem a possibilidade de manter as fórmulas…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2311902341/377b8040b7ab325e3d715553fbe0/reset-formula-sankhya.png?expires=1786536000&signature=a9cd1ee8ceb9d3e0d9dbfd568a1f11c31daa2011786109586824c70de9b59660&req=diMmF8B%2Bn4JbWPMW3nq%2BgeZI4fNSUp8Qbi9LRXvlgC0HtuB8CJ0gX7GZNmIG%0AwU0amnUvkeBztD%2FVyQ6HRzlpL0k%3D%0A)

A decisão entre manter ou resetar deve ser tomada **caso a caso**, pois cada opção tem implicações diretas no comportamento da integração. Este artigo explica o que são essas fórmulas, onde elas existem e como escolher a opção adequada para a sua operação.

---

## Pré-requisitos

- Ser **usuário administrador** da conta Ploomes.
- Estar aplicando uma **edição na configuração da integração Sankhya**.

---

## Entendendo as fórmulas utilizadas pela integração Sankhya

## 1) O que são essas fórmulas

As fórmulas utilizadas pela integração Sankhya cumprem dois papéis principais:

**Consultas em tempo real ao Sankhya:** Durante a criação e edição de documentos no Ploomes, algumas fórmulas realizam consultas diretas ao Sankhya para trazer informações atualizadas do ERP. Essas consultas incluem:

- Verificação de **limites financeiros** dos clientes.
- Consulta de **restrições e exceções de TOPs** (Tipo de Operação).
- Obtenção de **detalhes de estoque** dos produtos.
- Listagem de **unidades de medida alternativas** disponíveis para produtos.
- Listagem de **controles disponíveis** para um produto.
- Em contas mais antigas: consulta de **preço e imposto** dos produtos.

**Cálculos automáticos em documentos:** Outras fórmulas são responsáveis por calcular valores automaticamente em campos de Propostas, Vendas e seus produtos. Exemplos:

- **Total do Produto**: cálculo baseado em valor unitário × quantidade, descontando o valor definido.
- **Total do Bloco**, **Total da Proposta/Venda**, entre outros cálculos financeiros do documento.

**Exemplo prático:** uma conta pode ter customizado a fórmula do campo "Total do Produto" para incluir um imposto específico no cálculo, ou ter ajustado a fórmula de "Consulta única" para engatilhar apenas em determinado momento do fluxo comercial. Ao resetar as fórmulas, essas customizações são perdidas e o comportamento padrão da integração é restaurado.

## 2) Onde essas fórmulas existem

As fórmulas estão presentes nos seguintes campos da integração:

**Em Produto da Proposta e Produto da Venda:**

- Consulta única
- Valor unitário (Sankhya)
- Unidade de medida (Sankhya)
- Controle (Sankhya)
- Total do Produto (Sankhya)
- Total do Bloco

**Em Proposta e Venda:**

- Total da Proposta/Venda
- Detalhes financeiros
- Restrições da TOP

---

## Escolhendo entre manter ou resetar as fórmulas

## 1) Quando o modal aparece

Ao confirmar qualquer edição na configuração da integração Sankhya, um modal será exibido solicitando que o administrador escolha entre **manter as fórmulas atuais** ou **resetar para o padrão** da integração. A escolha é feita antes da aplicação efetiva da edição.

![Imagem 2: Ao confirmar qualquer edição na configuração da integração Sankhya, um modal será exibido solicitando que o…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2311919108/00d65ba1c6c5b8e76693f8b12777/reset-formula-sankhya.png?expires=1786536000&signature=ace1c4a021eced5251f42afe6c7915fc0fcbb415486eed56d7881a47fcbfbf21&req=diMmF8B%2FlIBfUfMW3nq%2BgYYWKIfelcnIKj4Jemgb7e%2FLmvzxOiIZnUTN8ZOX%0AAHIUqSXdWL7swyi1XQFkfMSe2JA%3D%0A)

Exemplo do modal com a opção de escolha preenchida para "manter as fórmulas atuais"

## 2) Opção "Manter as fórmulas atuais"

Ao selecionar essa opção, marcando o checkbox, **nenhum campo com fórmula da integração será alterado**. Todas as fórmulas permanecem exatamente como estavam antes da edição, incluindo eventuais customizações feitas ao longo da implementação ou operação.

**Prós:**

- As **customizações e ajustes** realizados em fórmulas para atender a regras específicas da operação do cliente são **preservados**.
- Fluxos e processos que dependem das fórmulas customizadas continuam funcionando sem necessidade de reconfiguração.

**Contras:**

- As fórmulas **não recebem atualizações** eventualmente publicadas pela Ploomes no padrão da integração. Correções, melhorias e adaptações evolutivas aplicadas ao padrão não serão refletidas na conta enquanto a opção de manter for selecionada.

## 3) Opção "Resetar as fórmulas para o padrão"

Ao selecionar essa opção, desmarcando o checkbox, **todas as fórmulas dos campos utilizados pela integração serão retornadas ao padrão** vigente da integração Sankhya. Quaisquer customizações existentes serão substituídas pelas fórmulas padrão.

**Prós:**

- Garante que a conta esteja **100% alinhada ao padrão atual** da integração.
- A conta passa a receber automaticamente **correções, melhorias e adaptações evolutivas** publicadas pela Ploomes no comportamento padrão das fórmulas.

**Contras:**

- Todas as **customizações anteriores são perdidas** e precisarão ser reconfiguradas manualmente caso ainda sejam necessárias.

## 4) Como decidir qual opção escolher

A decisão deve ser tomada **caso a caso**, considerando o contexto da conta e o histórico de customizações. Algumas orientações práticas:

- **Se a conta possui customizações em fórmulas que estão funcionando corretamente:** geralmente a opção mais segura é **manter**, preservando o comportamento configurado.
- **Se a conta não possui customizações ou está com comportamento inesperado em fórmulas após uma evolução da integração:** vale considerar **resetar** para alinhar a conta ao padrão mais recente.
- **Antes de qualquer edição:** é altamente recomendável **documentar as customizações existentes** (copiando as fórmulas atuais para um local seguro). Isso garante que, em caso de reset, seja possível reaplicar manualmente as customizações necessárias.
- **Em caso de dúvida:** opte por manter e, em um segundo momento, avalie junto ao time responsável pela implementação se faz sentido resetar para receber atualizações do padrão.

---

## Limitações

- **A escolha é binária:** ou todas as fórmulas são mantidas, ou todas são resetadas. Não é possível escolher campo a campo quais fórmulas preservar e quais resetar.
- **O reset é irreversível pela integração:** uma vez que as fórmulas são resetadas para o padrão, as customizações anteriores não podem ser recuperadas automaticamente. Será necessário reaplicá-las manualmente, caso sejam necessárias.
- **Aplica-se apenas aos campos da integração:** a opção afeta exclusivamente os campos de fórmula utilizados pela integração Sankhya listados neste artigo. Outros campos da conta não são impactados por essa escolha.

---

## F.A.Q.

**Se eu sempre optar por manter, nunca receberei evoluções das fórmulas?**

Correto. Ao optar por manter, as fórmulas da conta permanecem inalteradas. Eventuais correções, melhorias ou adaptações evolutivas publicadas pela Ploomes no padrão da integração não serão aplicadas automaticamente enquanto a opção de manter continuar sendo selecionada nas edições.

**Posso resetar apenas uma fórmula específica?**

Não. A escolha é válida para todas as fórmulas utilizadas pela integração de uma só vez. Caso seja necessário resetar apenas uma fórmula específica, o caminho recomendado é resetar todas e reaplicar manualmente as customizações que precisam ser preservadas.

**Como saber se minha conta tem fórmulas customizadas?**

Recomenda-se verificar os campos listados neste artigo (Consulta única, Total do Produto, Total da Proposta/Venda, entre outros) e comparar o conteúdo das fórmulas com o padrão da integração. Caso haja dúvidas, consulte o time que realizou a implementação da integração ou acione o suporte Ploomes.

**Como recuperar uma fórmula customizada após o reset?**

A recuperação automática não é possível após o reset. Para evitar perdas, recomenda-se **documentar as fórmulas atuais antes de aplicar qualquer edição**. Com essa documentação em mãos, as customizações podem ser reaplicadas manualmente após o reset.

**O que acontece com campos customizados que eu criei manualmente na conta?**

A opção de manter ou resetar fórmulas afeta apenas os **campos utilizados pela integração Sankhya** listados neste artigo. Campos customizados criados manualmente na conta, que não fazem parte da integração, não são impactados por essa escolha.

**Preciso fazer essa escolha em todas as edições?**

Sim. O modal de escolha entre manter ou resetar as fórmulas é exibido em **toda edição aplicada** na configuração da integração Sankhya. A decisão é tomada em cada aplicação e não fica salva como preferência.

**Se eu resetar as fórmulas e depois perceber que perdi uma customização importante, o que faço?**

Será necessário reaplicar manualmente a customização no campo correspondente. Por isso é tão importante documentar as fórmulas antes de qualquer edição — especialmente quando houver a possibilidade de reset.

---

## Glossário

- **Fórmula:** expressão configurada em um campo do Ploomes que define como o valor do campo é calculado ou consultado automaticamente. Na integração Sankhya, as fórmulas realizam consultas em tempo real ao ERP e cálculos automáticos em documentos.
- **Campo de desenvolvedor:** tipo de campo no Ploomes destinado a receber fórmulas e lógicas customizadas. É utilizado pela integração Sankhya para orquestrar consultas e cálculos.
- **TOP (Tipo de Operação):** classificação no Sankhya que define o tipo de uma operação comercial ou fiscal (ex: venda, devolução, bonificação) e suas regras associadas.
- **Consulta em tempo real:** chamada que a integração realiza diretamente ao Sankhya no momento em que um evento ocorre no Ploomes, trazendo informações atualizadas do ERP.
- **Customização:** ajuste ou modificação feita em uma fórmula padrão da integração para atender a uma regra específica da operação do cliente.
- **Reset:** ação de retornar uma ou mais fórmulas ao padrão atual da integração, descartando quaisquer customizações anteriores.
- **Padrão da integração:** comportamento e fórmulas definidos pela Ploomes como referência para o funcionamento da integração Sankhya. É o estado "de fábrica" das fórmulas, sem customizações.
