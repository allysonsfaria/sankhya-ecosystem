---
id: "44012570426903"
titulo: "[TMS] - Como utilizar a Calculadora de Frete"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012570426903--TMS-Como-utilizar-a-Calculadora-de-Frete"
trilha: "Lincros > TMS > Planejamento Logístico - TMS"
atualizado_em: "2026-10-05T19:32:32Z"
rotulos: ["sync_hc", "lincros", "lincros_13433455", "sync_hash_a43e62ba7dbb"]
---

# [TMS] - Como utilizar a Calculadora de Frete

## 1 - Problema Relatado pelo Cliente

O cliente deseja entender mais sobre a funcionalidade "Calculadora de Frete" do TMS, para realizar o cálculo de fretes de maneira ágil e precisa, utilizando as tabelas previamente cadastradas na plataforma, com base nas informações de origem, destino e características da carga. Além disso, busca compreender como utilizar corretamente os filtros e funcionalidades da calculadora de frete, incluindo a simulação de redespacho e a solicitação direta do frete após a simulação. Na Calculadora de Fretes, é possível simular frete mesmo com a tabela em situação "Aguardando Aprovação".

---

## 2 - Passo a Passo para Resolver o Problema

## Pré-requisitos:

- Tabelas de frete cadastradas na plataforma (por Região, Rota ou Negociação).
- Informar obrigatoriamente o CEP de Origem e o CEP de Destino.

---

## Passo 1: Acessar a Calculadora de Frete

- Navegue até o menu: **Planejamento Logístico > Seleção de Transportadora > Calculadora de Frete**.

---

## Passo 2: Preencher os Filtros Básicos

- **Tipo de Operação**: Selecione se será uma operação de Entrada ou Saída.
- **Origem**: Informe o local de origem da carga.
- **Destino**: Informe o local de destino da carga.
- **Data de Coleta**: Informe a previsão de coleta.

---

## Passo 3: Preencher os Filtros Avançados (opcional, conforme necessidade)

**Localização:**

- **Unidade**: Informe a unidade da empresa responsável.
- **Remetente**: Informe quem enviará a mercadoria.
- **Destinatário**: Informe quem receberá a mercadoria.

**Frete:**

- **Modal**: Escolha o modal de transporte (Ex.: Rodoviário, Aéreo).
- **Tipo de Pagador**: Selecione quem será o pagador (Remetente, Destinatário ou Consignatário).
- **Placa**: Informe a placa do veículo, se necessário.
- **Grupo de Veículo**: Identifique o tipo de veículo.
- **Marcador**: Utilize para buscar tabelas restritas a determinado marcador.
- **Simular Redespacho**: Se houver redespacho, marque "SIM".
- **CEP Intermediário**: Informe o CEP do início do segundo trecho.
- **Simular com Centro de Distribuição**: Marque "SIM" se desejar considerar um centro de distribuição.
- **Centro de Distribuição**: Informe o centro de distribuição.
- **CEP Centro de Distribuição**: Informe o respectivo CEP.

---

## Passo 4: Informar os Dados da Mercadoria

**Valores Abertos:**

- **Produto**: Informe o nome do produto.
- **Peso Nominal (KG)**: Informe o peso total da mercadoria.
- **Cubagem**: Informe a cubagem total da mercadoria.
- **Valor das NF-es**: Informe o valor total das notas fiscais (com impostos).
- **Valor Produtos**: Informe o valor apenas dos produtos.
- **Volumes**: Informe a quantidade de volumes a serem enviados.

**Detalhar Produtos:**

- Informe os detalhes de cada produto: Nome, Quantidade de Itens, Peso, Cubagem, Valor e Volumes.
- Após preencher, clique no botão **"Adicionar"** para incluir os dados.

---

## Passo 5: Realizar a Simulação

- Após preencher todas as informações, clique no botão **"Simular Valores"**.
- O sistema apresentará o resultado da simulação, listando as transportadoras em ordem crescente de valor de frete.

---

## Passo 6: Analisar o Resultado da Simulação

- Serão exibidas as seguintes informações:

  - **Transportadora**: Nome da transportadora.
  - **Tabela de Frete**: Utilizada no cálculo.
  - **Prazo e Previsão de Entrega**.
  - **Valor, Impostos e Total do Frete**.
- Para visualizar o detalhamento do cálculo, clique na seta ao lado do nome da transportadora.

**Observações:**

- **Simulações de cargas fracionadas:** Quando o Tipo de Negociação selecionado na tabela de fretes for pré-conhecimento.
- **Simulações de cargas fechadas:** Quando o Tipo de Negociação selecionado na tabela de fretes for embarque.

---

## Passo 7: Solicitar o Frete

- Após escolher a opção desejada, clique no botão **"Solicitar Frete"**.
- O sistema direcionará automaticamente para o módulo de Solicitação de Frete, transferindo todas as informações da simulação.
