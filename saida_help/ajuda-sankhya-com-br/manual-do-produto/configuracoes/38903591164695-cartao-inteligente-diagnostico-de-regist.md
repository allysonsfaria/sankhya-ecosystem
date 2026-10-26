---
id: "38903591164695"
titulo: "Cartão Inteligente — Diagnóstico de Registro (Boleto Rápido)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38903591164695-Cart%C3%A3o-Inteligente-Diagn%C3%B3stico-de-Registro-Boleto-R%C3%A1pido"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T14:01:07Z"
rotulos: ["Boleto", "Financeiro", "Registro", "Cartões Inteligentes", "API", "Erro"]
---

# Cartão Inteligente — Diagnóstico de Registro (Boleto Rápido)

Este artigo explica como interpretar o **Cartão Inteligente de Diagnóstico de Registro do Boleto Rápido** e como identificar problemas no processo de registro de boletos enviados ao banco via API.

O cartão auxilia usuários e equipes de suporte a identificar rapidamente falhas no registro de boletos e orientar as ações necessárias para correção.

Tópicos deste artigo:

| Tópico | Tópico | Tópico |
| --- | --- | --- |
| [Como interpretar o cartão](https://ajuda.sankhya.com.br/hc/pt-br/articles/38903591164695-Cart%C3%A3o-Inteligente-Diagn%C3%B3stico-de-Registro-Boleto-R%C3%A1pido#h_01KK9EDXJ9D0JZJ3SKNS11PKX9) | [Diagnóstico crítico — boletos com erro de registro](https://ajuda.sankhya.com.br/hc/pt-br/articles/38903591164695-Cart%C3%A3o-Inteligente-Diagn%C3%B3stico-de-Registro-Boleto-R%C3%A1pido#h_01KK9EDXJJJWYTXP0F2M3ZFC3W) | [Como localizar boletos com erro](https://ajuda.sankhya.com.br/hc/pt-br/articles/38903591164695-Cart%C3%A3o-Inteligente-Diagn%C3%B3stico-de-Registro-Boleto-R%C3%A1pido#h_01KK9EDXJKHJRAET17J0N6JQZM) |
| [Cenário 1 — Status 100 (falha no registro)](https://ajuda.sankhya.com.br/hc/pt-br/articles/38903591164695-Cart%C3%A3o-Inteligente-Diagn%C3%B3stico-de-Registro-Boleto-R%C3%A1pido#h_01KK9EDXJTCDS1PEQSXFA15EKN) | [Como resolver erro de registro](https://ajuda.sankhya.com.br/hc/pt-br/articles/38903591164695-Cart%C3%A3o-Inteligente-Diagn%C3%B3stico-de-Registro-Boleto-R%C3%A1pido#h_01KK9EDXJY36HA195KWFTBYM2R) | [Quando utilizar o botão Reprocessar Registro](https://ajuda.sankhya.com.br/hc/pt-br/articles/38903591164695-Cart%C3%A3o-Inteligente-Diagn%C3%B3stico-de-Registro-Boleto-R%C3%A1pido#h_01KK9EDXKCFK33F85J467WAV7Q) |
| [Cenário 2 — Status 0 (aguardando registro)](https://ajuda.sankhya.com.br/hc/pt-br/articles/38903591164695-Cart%C3%A3o-Inteligente-Diagn%C3%B3stico-de-Registro-Boleto-R%C3%A1pido#h_01KK9EDXKE0D13PV5WTVBND8FY) | [Prazo esperado de retorno do banc](https://ajuda.sankhya.com.br/hc/pt-br/articles/38903591164695-Cart%C3%A3o-Inteligente-Diagn%C3%B3stico-de-Registro-Boleto-R%C3%A1pido#h_01KK9EDXKSB5FSKG6RE5Y7B3YV)o | [Diagnóstico normal — registro realizado com sucesso](https://ajuda.sankhya.com.br/hc/pt-br/articles/38903591164695-Cart%C3%A3o-Inteligente-Diagn%C3%B3stico-de-Registro-Boleto-R%C3%A1pido#h_01KK9EDXKV1428DGEYV114QV4V) |
| [Serviço não contratado](https://ajuda.sankhya.com.br/hc/pt-br/articles/38903591164695-Cart%C3%A3o-Inteligente-Diagn%C3%B3stico-de-Registro-Boleto-R%C3%A1pido#h_01KK9EDXKYRQXPSZ5FZRM6H4W2) | [Perguntas frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/38903591164695-Cart%C3%A3o-Inteligente-Diagn%C3%B3stico-de-Registro-Boleto-R%C3%A1pido#h_01KK9EDXM0JRVFCN6YNN1QCNE3) |  |

---

# Como interpretar o cartão

Os cartões exibidos no painel indicam o status geral das tentativas de registro de boletos enviadas ao banco.

| Cor | Status | Significado |
| --- | --- | --- |
| 🔴 Vermelho | Erros de registro | Existem boletos que tentaram registrar no banco, porém ocorreu falha |
| 🟢 Verde | Registro realizado com sucesso | Todos os boletos foram registrados corretamente |
| ⚪ Cinza | Serviço não contratado | A empresa não possui integração ativa para registro automático via API |

(Inserir imagem do cartão do Figma)

---

# 🔴 Diagnóstico crítico — boletos com erro de registro

Esse cenário indica que existem boletos enviados ao banco para registro, porém o banco retornou erro.

![Imagem 1: Esse cenário indica que existem boletos enviados ao banco para registro, porém o banco retornou erro.](https://ajuda.sankhya.com.br/hc/article_attachments/38903591151639)

---

## Como localizar os boletos com erro

Acesse:

**Financeiro → Acompanhamento de Boletos – API**

Utilize os filtros da tela para localizar os boletos desejados.

No grid de resultados, verifique os campos:

- **Status**
- **Status do boleto**

O erro será identificado quando:

| Campo | Valor |
| --- | --- |
| Status | 100 |
| Status do boleto | Erro ao registrar boleto |

---

# Cenário 1 — Status 100 (Falha no registro do boleto)

## O que significa

Quando o boleto apresenta **Status = 100**, isso indica que:

- o boleto foi enviado ao banco
- o banco retornou erro no processamento
- o registro do boleto não foi realizado
- o título continua sem registro bancário

⚠️ Nesse estado, o boleto **não pode ser pago**, pois ainda não existe no banco.

---

## Como resolver

### 1. Consultar a mensagem de erro

Na tela **Acompanhamento de Boletos – API**:

1. Localize o boleto no grid
2. Verifique a mensagem de erro exibida

A mensagem retornada pelo banco indica o motivo da rejeição.

### Exemplos de erros comuns

- CPF/CNPJ do sacado inválido
- Conta bancária não credenciada
- Carteira de cobrança inválida
- Nosso número fora do padrão
- Dados obrigatórios do título não preenchidos

Após identificar o erro, corrija as informações necessárias no título financeiro.

---

### 2. Reprocessar o registro

Após corrigir o problema:

1. Acesse novamente **Acompanhamento de Boletos – API**
2. Selecione o boleto
3. Clique em **Reprocessar Registro**

O sistema irá:

- reenviar o boleto ao banco
- tentar novamente o registro
- manter o mesmo **Nosso Número**

Não é necessário excluir ou gerar um novo boleto.

---

## Quando utilizar o botão Reprocessar Registro

O botão **Reprocessar Registro** só pode ser utilizado quando:

✔ **Status = 100 (erro de registro)**

Não estará disponível quando:

❌ o boleto estiver aguardando retorno do banco.

---

# Cenário 2 — Status 0 (Aguardando registro)

## Como identificar

Na tela **Acompanhamento de Boletos – API**, o boleto apresentará:

| Campo | Valor |
| --- | --- |
| Status | 0 |
| Status do boleto | Aguardando registro |

---

## O que significa

Nesse cenário:

- o boleto já foi enviado ao banco
- o banco ainda não retornou o resultado do registro

Isso pode ocorrer devido a:

- fila de processamento da API bancária
- retorno bancário assíncrono
- processamento via **EDI bancário (D+1)**

Esse cenário **não representa erro**.

---

## Ação recomendada

Quando o boleto estiver com **Status = 0**:

- aguarde o retorno do banco
- nenhuma ação é necessária no sistema

O botão **Reprocessar Registro** não ficará disponível nesse status.

---

## Prazo esperado de retorno

O tempo de retorno pode variar conforme o banco.

De forma geral, recomenda-se aguardar até **24 horas** para que o banco retorne o resultado do registro.

Caso o boleto permaneça sem atualização após esse período:

- verifique se a conta bancária está configurada corretamente
- confirme se existe credenciamento para registro de boletos
- valide se os dados do título estão completos

Se necessário, consulte o suporte responsável pela integração bancária.

---

# 🟢 Diagnóstico normal — registro realizado com sucesso

O cartão verde indica que os boletos foram registrados corretamente no banco.

Isso significa que:

- o envio ao banco foi concluído
- o banco confirmou o registro
- o boleto está válido para pagamento

  ![Imagem 2: o boleto está válido para pagamento](https://ajuda.sankhya.com.br/hc/article_attachments/38903607527831)

---

## Como validar o registro

Acesse:

**Financeiro → Acompanhamento de Boletos – API**

Localize o boleto desejado e verifique no grid ou no histórico que o registro foi concluído.

Nenhuma ação é necessária.

---

# ⚪ Serviço não contratado

O cartão cinza indica que:

- a empresa não possui contratação do registro automático de boletos
  ou
- a conta bancária não possui integração via API

Nesse cenário, os boletos não serão registrados automaticamente no banco.

Nenhuma ação é necessária dentro deste processo.

![Imagem 3: Nenhuma ação é necessária dentro deste processo.](https://ajuda.sankhya.com.br/hc/article_attachments/38903607531671)

---

## Perguntas frequentes

### O que significa o status 100 no registro do boleto?

Indica que o boleto foi enviado ao banco, porém ocorreu erro no registro.
É necessário verificar a mensagem retornada pelo banco, corrigir os dados do título e utilizar a opção **Reprocessar Registro**.

---

### O que significa o status 0 no acompanhamento de boletos?

Indica que o boleto foi enviado ao banco, mas o banco ainda não retornou o resultado do registro.

Isso pode ocorrer devido ao processamento interno do banco ou filas de processamento da API.

---

### Quanto tempo leva para o banco registrar um boleto?

O prazo pode variar conforme o banco, mas normalmente o retorno ocorre em até **24 horas**.

Em alguns casos o processamento pode ocorrer em **D+1**, dependendo da integração bancária.

---

### Como saber se o boleto foi registrado com sucesso?

O registro pode ser validado na tela:

**Financeiro → Acompanhamento de Boletos – API**

Verifique o status do boleto no grid ou consulte o histórico do registro.

---

> 📌Conheça mais [Cartões Inteligentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044355393-Cart%C3%B5es-Inteligentes#h_01KK2GB7X9R8E27DYCHM2NEY81)!
