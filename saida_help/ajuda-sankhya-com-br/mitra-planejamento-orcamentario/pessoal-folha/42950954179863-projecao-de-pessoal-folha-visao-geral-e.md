---
id: "42950954179863"
titulo: "Projeção de pessoal (folha): visão geral e utilização"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950954179863-Proje%C3%A7%C3%A3o-de-pessoal-folha-vis%C3%A3o-geral-e-utiliza%C3%A7%C3%A3o"
trilha: "MITRA: Planejamento orçamentário  > Pessoal (folha)"
atualizado_em: "2026-08-24T13:48:34Z"
rotulos: ["sync_hc", "mitra", "mitra_8", "sync_hash_8edb832de2ed"]
---

# Projeção de pessoal (folha): visão geral e utilização

## Projeção de pessoal (folha): visão geral e utilização

**Módulo:** Pessoal

### O que é e para que serve

O módulo de Pessoal projeta o custo de folha de cada centro de resultado (CR) para os 12 meses da versão do orçamento, a partir do quadro de colaboradores e das movimentações planejadas. O resultado alimenta automaticamente as contas de pessoal do orçamento — o gestor não digita esses valores conta a conta.

### Pré-requisitos

- Colaboradores cadastrados com CR, empresa, cargo, salário e tipo de contrato.
- Benefícios e encargos configurados para a versão.
- Premissas de dissídio e turnover definidas, quando aplicáveis.

### Visão geral

- **Quadro de colaboradores:** lista por CR, com busca por nome e cargo.
- **Movimentações projetadas:**
- **Contratações:** vagas futuras por cargo, CR, mês de entrada e quantidade;
- **Desligamentos:** o mês informado é o **primeiro mês sem custo** do colaborador;
- **Aumentos salariais:** percentual, mês de aplicação e motivo.
- **Geração da folha:** o cálculo projeta, colaborador a colaborador, os 12 meses da versão — salários, benefícios, encargos e as movimentações acima.
- **Gravação no orçamento:** a folha é agregada por mês e gravada nas contas de pessoal do orçamento (grupo 5.1.01/02/03).

### Comportamentos e pontos de atenção

- **Recálculo:** alterações em colaboradores, benefícios, encargos, premissas ou movimentações **não refletem automaticamente** no orçamento — é preciso recalcular a projeção para o ciclo e CR. O recálculo substitui a projeção anterior daquele ciclo/CR antes de regravar.
- **Desligamentos preservados:** ao duplicar uma versão, os desligamentos projetados são mantidos na nova versão.
- **Movimentações pelo link do gestor:** contratações, desligamentos, aumentos e o recálculo também podem ser feitos pelo link de preenchimento, no escopo do gestor.
- A aba Pessoal do preenchimento exibe o resultado calculado; os valores não são editáveis diretamente na grade.

### Resultado esperado

Após gerar a folha e gravar o orçamento, a aba Pessoal do CR exibe os custos projetados mês a mês, coerentes com o quadro de colaboradores e as movimentações registradas, e a linha Total reflete o custo anual de pessoal do CR.

### Artigos relacionados

- Preenchimento do orçamento por modelos: visão geral e utilização

---

### Pendências para validação

1. Confirmar os rótulos dos botões de gerar folha e gravar no orçamento (se são ações separadas ou uma só na interface).
2. Confirmar os nomes exatos das contas do grupo 5.1.01/02/03 no plano de contas.
