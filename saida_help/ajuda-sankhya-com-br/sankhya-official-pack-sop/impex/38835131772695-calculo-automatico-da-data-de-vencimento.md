---
id: "38835131772695"
titulo: "Cálculo Automático da Data de Vencimento das Despesas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38835131772695-C%C3%A1lculo-Autom%C3%A1tico-da-Data-de-Vencimento-das-Despesas"
trilha: "Sankhya Official Pack - SOP > ImpEx"
atualizado_em: "2026-07-22T14:01:05Z"
rotulos: ["Configuração", "Movimentação Financeira", "Importação", "Preferências", "Financeiro", "Cálculo Automático da Data de Vencimento das Despesas", "Follow Up", "Dias Para Vencimento", "IMP_DTVENDESPIN", "Naturezas dos Incoterms", "Data Prevista", "Data de Vencimento da Despesa"]
---

# Cálculo Automático da Data de Vencimento das Despesas

#### 1. Objetivo da Rotina

Automatizar o cálculo da **Data de Vencimento das Despesas** de Importação, utilizando como base as datas previstas registradas no **Follow-Up** do processo. Essa automatização tem como objetivo reduzir erros de digitação e garantir que o vencimento das despesas permaneça alinhado ao cronograma logístico da operação.

#### 2. Ativação da Funcionalidade

**Preferência do Sistema**: IMP\_DTVENDESPIN

**Descrição**: Utilizar datas previstas de vencimento das despesas.

Quando ativada, o sistema passa a calcular automaticamente o vencimento das despesas.

#### 3. Configuração - Naturezas dos Incoterms

Após ativar a preferência, deve-se acessar o cadastro de Naturezas dos Incoterms e configurar os seguintes campos:

- **Data Prevista Base** (lista suspensa);
- **Dias para Vencimento** (campo numérico).

#### 4. Funcionamento do Cálculo

O cálculo será realizado da seguinte forma:

> Data Prevista (Follow-Up) + Dias Para Vencimento = Data de Vencimento da Despesa.

###

#### 5. Atualização Automática

Sempre que a data base configurada for alterada no Follow-Up, o sistema realizará automaticamente o recálculo do vencimento das despesas vinculadas.

#### 6. Regras de Validação

A data de vencimento não será atualizada caso a despesa esteja **vinculada a uma Nota de Nacionalização autorizada** ou quando o **financeiro correspondente já estiver baixado**.

#### 7. Benefícios da Rotina

- ##### Redução de erros manuais;
- ##### Padronização dos vencimentos;
- ##### Integração com planejamento logístico;
- ##### Maior controle financeiro.
