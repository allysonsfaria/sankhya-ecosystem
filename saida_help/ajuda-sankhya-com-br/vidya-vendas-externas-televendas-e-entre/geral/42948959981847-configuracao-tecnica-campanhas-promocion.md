---
id: "42948959981847"
titulo: "Configuração Técnica - Campanhas Promocionais por Grupo de Desconto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42948959981847-Configura%C3%A7%C3%A3o-T%C3%A9cnica-Campanhas-Promocionais-por-Grupo-de-Desconto"
trilha: "VIDYA: Vendas externas, televendas e entregas > Geral"
atualizado_em: "2026-08-24T16:56:18Z"
rotulos: ["sync_hc", "vidya", "vidya_593063", "sync_hash_bebbc099f0c5"]
---

# Configuração Técnica - Campanhas Promocionais por Grupo de Desconto

## Configuração Técnica - Campanhas Promocionais por Grupo de Desconto

### Objetivo

Este documento tem como objetivo orientar consultores técnicos na habilitação e configuração da funcionalidade de campanhas promocionais por grupo de desconto de produtos.

---

## Pré-requisitos

Antes de iniciar a configuração, valide os seguintes requisitos:

#### Backend

O cliente deve estar utilizando o **Backend Unificado**.

#### Frontend

A versão mínima homologada para utilização da funcionalidade é: **5.2.125**

Caso o ambiente esteja em versão inferior, será necessária a atualização antes da configuração.

---

## Configurações Necessárias

### 1. Criação do campo AD\_OBSERVACAO na TGFDES

Criar no dicionário de dados o campo:

| Tabela | Campo |
| --- | --- |
| TGFDES | AD\_OBSERVACAO |

![Imagem 1: AD_OBSERVACAO](https://ajuda.sankhya.com.br/hc/article_attachments/42957386876951)

#### Finalidade

Este campo habilita a aba **Campos Adicionais** na tela de **Descontos Promocionais**.

Nessa aba será exibido o campo **Observação do Desconto**, permitindo que o usuário final informe informações complementares sobre a campanha.

#### Exemplo de utilização

- "Campanha válida apenas para produtos selecionados."
- "Desconto não cumulativo com outras promoções."
- "Ação promocional do mês."

O conteúdo informado poderá ser apresentado aos usuários finais durante a utilização da campanha.

---

### 2. Importação do Metadados AD\_TVDYDESPROD

Importar o metadados:

**AD\_TVDYDESPROD**

#### Finalidade

Este metadado habilita a aba **Produtos Obrigatórios** na tela de **Descontos Promocionais**.

Através desta aba, o usuário poderá definir quais produtos e quantidades mínimas devem estar presentes no pedido para que a campanha seja validada.

#### Exemplo

Produto obrigatório: 123

Quantidade mínima: 2 unidades

Neste cenário, mesmo que a quantidade total dos produtos da campanha atinja a faixa de desconto configurada, o desconto somente será aplicado caso o pedido contenha pelo menos 2 unidades do produto 123.

---

## Validação da Configuração

Após concluir as configurações:

1. Acesse a tela de Descontos Promocionais.
2. Verifique se a aba **Campos Adicionais** está disponível.
3. Verifique se a aba **Produtos Obrigatórios** está disponível.
4. Crie uma campanha utilizando o tipo de desconto **Grupo de Produto**.
5. Realize um teste no aplicativo utilizando o filtro **Campanhas**.
6. Valide a aplicação automática do desconto conforme as faixas configuradas.
7. Caso existam produtos obrigatórios, valide também o comportamento com e sem o atendimento dos requisitos mínimos.

---

## Fluxo Resumido

1. Validar Backend Unificado.
2. Validar versão mínima do Frontend (5.2.125).
3. Criar o campo **AD\_OBSERVACAO** na TGFDES.
4. Importar o metadado **AD\_TVDYDESPROD**.
5. Configurar os grupos de desconto nos produtos.
6. Criar a campanha promocional.
7. Configurar faixas de desconto.
8. Configurar produtos obrigatórios (quando necessário).
9. Realizar testes de validação no aplicativo.
