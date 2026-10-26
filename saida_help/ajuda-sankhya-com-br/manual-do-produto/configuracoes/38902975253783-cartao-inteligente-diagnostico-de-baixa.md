---
id: "38902975253783"
titulo: "Cartão Inteligente — Diagnóstico de Baixa (Boleto Rápido)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38902975253783-Cart%C3%A3o-Inteligente-Diagn%C3%B3stico-de-Baixa-Boleto-R%C3%A1pido"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T14:01:03Z"
rotulos: ["Configuração", "Movimentação Financeira", "Financeiro", "Baixa Automática", "Cartões Inteligentes", "Boleto Rápido", "Diagnóstico"]
---

# Cartão Inteligente — Diagnóstico de Baixa (Boleto Rápido)

Este artigo explica como interpretar o **Cartão Inteligente de Diagnóstico de Baixa do Boleto Rápido** e como realizar a análise quando existem boletos pagos no banco que ainda não foram baixados no ERP.

Esse cartão auxilia usuários e equipes de suporte a identificar rapidamente possíveis problemas no processo de **baixa automática de boletos**.

Tópicos deste artigo:

| Tópico | Tópico | Tópico |
| --- | --- | --- |
| [Como interpretar o cartão de diagnóstico](https://ajuda.sankhya.com.br/hc/pt-br/articles/38902975253783-Cart%C3%A3o-Inteligente-Diagn%C3%B3stico-de-Baixa-Boleto-R%C3%A1pido#h_01KK9CTBPTYZDHN6TVQ0G8MZCG) | [Como funciona o processo de liquidação](https://ajuda.sankhya.com.br/hc/pt-br/articles/38902975253783-Cart%C3%A3o-Inteligente-Diagn%C3%B3stico-de-Baixa-Boleto-R%C3%A1pido#h_01KK9CTBQSBV7HAH4DY6N18601) | [Status que indicam liquidação do título](https://ajuda.sankhya.com.br/hc/pt-br/articles/38902975253783-Cart%C3%A3o-Inteligente-Diagn%C3%B3stico-de-Baixa-Boleto-R%C3%A1pido#h_01KK9CTBQTXB5AGZV0759FKZJG) |
| [Como a baixa deve funcionar no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/38902975253783-Cart%C3%A3o-Inteligente-Diagn%C3%B3stico-de-Baixa-Boleto-R%C3%A1pido#h_01KK9CTBR1MPRHVFSC5DKJWFF3) | [Diagnóstico crítico — boletos liquidados sem baixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/38902975253783-Cart%C3%A3o-Inteligente-Diagn%C3%B3stico-de-Baixa-Boleto-R%C3%A1pido#h_01KK9CTBQ5Q2886TZX1HFGD4P1) | [Como resolver quando o cartão está vermelho](https://ajuda.sankhya.com.br/hc/pt-br/articles/38902975253783-Cart%C3%A3o-Inteligente-Diagn%C3%B3stico-de-Baixa-Boleto-R%C3%A1pido#h_01KK9CTBRAHAZKQ00TY3ND89HS) |
| [Cartão em verde — diagnóstico normal](https://ajuda.sankhya.com.br/hc/pt-br/articles/38902975253783-Cart%C3%A3o-Inteligente-Diagn%C3%B3stico-de-Baixa-Boleto-R%C3%A1pido#h_01KK9CTBRHB5P0DPHF6YJPYSG7) | [Cartão em cinza — serviço não contratado](https://ajuda.sankhya.com.br/hc/pt-br/articles/38902975253783-Cart%C3%A3o-Inteligente-Diagn%C3%B3stico-de-Baixa-Boleto-R%C3%A1pido#h_01KK9CTBRKN8TVWEENK22CA77P) | [Perguntas frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/38902975253783-Cart%C3%A3o-Inteligente-Diagn%C3%B3stico-de-Baixa-Boleto-R%C3%A1pido#h_01KK9CTBRMCY0P4E8R8NV4PXQE) |

---

# Como interpretar o cartão de diagnóstico

Os cartões exibidos no painel indicam a situação das baixas de boletos registradas pelo banco e processadas no ERP.

| Cor | Status | Significado | Ação |
| --- | --- | --- | --- |
| 🔴 Vermelho | Boletos liquidados não baixados | O banco informou que o boleto foi pago, mas o ERP ainda não realizou a baixa do título | Verificação necessária |
| 🟢 Verde | Nenhum problema encontrado | Todas as baixas de boletos foram processadas corretamente | Nenhuma ação necessária |
| ⚪ Cinza | Serviço não contratado | A empresa não utiliza a funcionalidade de baixa automática via Boleto Rápido | Nenhuma ação necessária |

(Inserir aqui imagem do cartão no Figma)

---

# Diagnóstico crítico — boletos liquidados sem baixa no ERP

Quando o cartão aparece em **vermelho**, significa que existem boletos que o banco já confirmou como pagos, porém o título continua em aberto no ERP.

Isso indica que:

- o banco registrou a liquidação do boleto
- o sistema recebeu (ou deveria receber) essa informação
- mas a baixa financeira não foi processada

---

## Causas mais frequentes

Alguns cenários podem gerar essa situação:

- Baixa automática desabilitada
- Conciliação automática desabilitada
- Job de processamento de baixas não executando (**job -10057**)
- Trigger ou evento customizado bloqueando a baixa
- Erro no retorno da API bancária
- Diferença entre valor pago e valor esperado
- Registros pendentes nas tabelas internas de baixa

---

# Como funciona o processo de liquidação

Quando um cliente realiza o pagamento de um boleto, o processo ocorre da seguinte forma:

1️⃣ O banco registra a liquidação
2️⃣ O banco envia o retorno da liquidação via API ou arquivo bancário
3️⃣ O ERP recebe a informação
4️⃣ O sistema executa o processo de baixa do título

---

## Status que indicam liquidação do título

Um título é considerado liquidado quando o retorno bancário informa um dos seguintes status:

| Status | Descrição |
| --- | --- |
| 6 | Liquidado |
| 11 | Título liquidado / protestado |
| 12 | Título liquidado |
| 14 | Liquidado via QR Code |
| 16 | Título creditado |

Quando um desses status é recebido, o sistema inicia o processo de baixa financeira.

---

# Como a baixa deve funcionar no sistema

O comportamento depende da configuração da conta do **Boleto Rápido**.

---

## Quando Baixa Automática e Conciliação Automática NÃO estão habilitadas

Nesse cenário o sistema **não executa a baixa automaticamente**.

Fluxo esperado:

1. O banco informa a liquidação
2. O título permanece em aberto no ERP
3. O usuário deve realizar a baixa manualmente

### Como validar essa configuração

Acesse:

**Financeiro → Boleto Rápido → Contas**

Verifique os parâmetros:

- Baixa Automática
- Conciliação Automática

Se ambos estiverem desabilitados, a baixa deverá ser realizada manualmente.

---

## Quando Baixa Automática e Conciliação Automática estão habilitadas

Quando essas opções estão ativas, o processo ocorre automaticamente.

Após o retorno da liquidação do banco, a API executa:

- baixa do título
- conciliação financeira
- atualização de valores pagos (juros, multa ou desconto)

---

## Como identificar uma baixa realizada com sucesso

No histórico do título financeiro será registrada a mensagem:

✔ **"Baixado automaticamente pela API do Banco."**

Isso indica que:

- a liquidação foi recebida
- a baixa foi processada corretamente

---

## Quando ocorre erro na baixa automática

Se houver falha no processo, o histórico pode apresentar mensagens como:

❌ **"Não foi possível realizar a baixa automática. Verificar triggers e processos de baixa."**

Isso indica que o sistema recebeu a liquidação, mas algum processo bloqueou a execução da baixa.

---

# Como o ERP registra a baixa internamente

Quando o banco informa a liquidação, o ERP registra o evento em tabelas internas responsáveis pelo processamento da baixa.

## Tabela TGFRAF

Essa tabela controla as **requisições de baixa financeira**.

Fluxo esperado:

1️⃣ Quando o retorno do banco chega
→ é criada uma linha com:

status **A — Aguardando processamento**

2️⃣ O job de baixa executa

3️⃣ O status é alterado para:

status **B — Baixa processada**

---

## Tabela TGFHBA

Essa tabela registra o **histórico da baixa financeira**.

Quando a baixa é concluída:

- uma nova linha é criada
- com status **B — Baixa realizada**

Essa tabela permite rastrear quando e como a baixa foi executada.

---

# Como resolver quando o cartão está vermelho

Siga o diagnóstico abaixo.

![Imagem 1: Siga o diagnóstico abaixo.](https://ajuda.sankhya.com.br/hc/article_attachments/38902975243671)

---

## Passo 1 — Verificar configuração da conta

Acesse:

**Financeiro → Boleto Rápido → Contas**

Verifique se os parâmetros estão habilitados:

✔ Baixa Automática
✔ Conciliação Automática

Se estiverem desabilitados, a baixa deverá ser manual.

---

## Passo 2 — Verificar execução do job de baixa

O processamento automático depende do **job -10057**.

Esse job é responsável por:

- processar liquidações
- executar baixas automáticas
- atualizar o financeiro

Se o job não estiver executando, as baixas ficam pendentes.

---

## Passo 3 — Verificar o histórico do título

Acesse o título financeiro e consulte o **Histórico**.

Verifique se existem mensagens como:

- erro na baixa automática
- inconsistência de dados
- bloqueio por processo customizado

---

## Passo 4 — Validar tabelas de processamento

Para análise técnica, consulte:

### TGFRAF

Verifique registros com:

status **A**

Isso indica que a baixa ainda está pendente de processamento.

### TGFHBA

Confirme se existe registro de baixa.

Se não houver registro, a baixa não foi executada.

---

## Passo 5 — Verificar triggers ou customizações

Em alguns ambientes podem existir:

- triggers personalizadas
- eventos de validação
- customizações financeiras

Esses elementos podem impedir a execução da baixa automática.

---

## Passo 6 — Reprocessar a baixa

Após corrigir o problema identificado:

- execute novamente o processamento
  ou
- aguarde a próxima execução do job de baixa

Isso deve concluir o processamento pendente.

---

# Diagnóstico normal — nenhum problema encontrado

Quando o cartão aparece em **verde**, significa que:

- não existem boletos liquidados pendentes
- as baixas foram executadas corretamente
- o job de processamento está funcionando
- a conciliação está funcionando normalmente

**Ação necessária:** nenhuma.

![Cartão com um check verde na tela e escrito: "nenhum problema encontrado"](https://ajuda.sankhya.com.br/hc/article_attachments/38902975244695)

---

# Serviço não contratado

Quando o cartão aparece em **cinza**, significa que:

- a empresa não utiliza baixa automática
- não existe integração ativa para processamento de baixas

Nesse cenário, os títulos devem ser baixados manualmente.

**Ação necessária:** nenhuma.

![Imagem 3: Ação necessária: nenhuma.](https://ajuda.sankhya.com.br/hc/article_attachments/38902954552855)

---

## Perguntas frequentes

### O que significa quando o banco informa que o boleto foi pago, mas o título continua em aberto no ERP?

Isso indica que o banco registrou a liquidação do boleto, mas a baixa financeira ainda não foi processada no sistema.

As causas mais comuns são:

- baixa automática desabilitada
- conciliação automática desabilitada
- falha no job de processamento de baixas
- bloqueio por trigger ou customização

---

### Como saber se a baixa automática está habilitada?

Acesse:

**Financeiro → Boleto Rápido → Contas**

Verifique os parâmetros:

- Baixa Automática
- Conciliação Automática

---

### Em quais casos a baixa precisa ser manual?

A baixa deve ser realizada manualmente quando:

- Baixa Automática não está habilitada
- Conciliação Automática não está habilitada
- a empresa optou por não utilizar a integração de baixa automática

---

> 📌Conheça mais [Cartões Inteligentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044355393-Cart%C3%B5es-Inteligentes#h_01KK2GB7X9R8E27DYCHM2NEY81)!
