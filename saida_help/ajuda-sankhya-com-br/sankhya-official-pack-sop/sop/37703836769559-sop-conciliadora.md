---
id: "37703836769559"
titulo: "SOP Conciliadora"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37703836769559-SOP-Conciliadora"
trilha: "Sankhya Official Pack - SOP > SOP"
atualizado_em: "2026-07-22T14:09:34Z"
rotulos: ["Configuração", "produto", "Integração", "Financeiro", "Conciliação", "Transfeera", "SOP conciliadora", "estabelecimento", "meio de captura", "rotina diária SOP Conciliadora", "conciliadora", "ERP", "Cartão de Crédito"]
---

# SOP Conciliadora

### O que é o SOP Conciliadora?

O **SOP Conciliadora** é uma extensão para o sistema ERP **Sankhya OM** que automatiza o processo de conciliação de vendas realizadas com cartão de crédito/débito.

A integração conecta o Sankhya com a API da **Conciliadora**, permitindo:

- Envio automático de vendas
- Busca e baixa de pagamentos
- Identificação de cancelamentos
- Processamento de taxas de aluguel de máquinas

Com isso, a equipe financeira ganha agilidade e confiabilidade no processo de conciliação de cartões.

### Telas

#### **(1)** Estabelecimento

Tela principal do SOP onde são cadastrados os estabelecimentos (pontos de venda) registrados na Conciliadora.

**Abas disponíveis:**

| Aba | Descrição |
| --- | --- |
| **Geral** | Dados do estabelecimento: código da operadora, ID, senha, centro de resultado e naturezas para baixa |
| **Vendas** | Registros de vendas enviadas à Conciliadora |
| **Pagamentos** | Log de pagamentos processados com detalhes da conciliação |
| **Cancelamentos** | Transações canceladas identificadas pela Conciliadora |
| **Locação Ponto de Venda** | Configuração para casos de locação de máquinas a terceiros |
| **Logger Conciliadora** | Logs de erros e eventos do processamento |

**Botões de ação:**

| Botão | Função |
| --- | --- |
| **Enviar Vendas** | Envia as vendas pendentes para a Conciliadora |
| **Buscar Pagamentos** | Consulta pagamentos na API e realiza a baixa automática |
| **Buscar Cancelamentos** | Consulta cancelamentos na API |

#### **(2)** Produto

Tela para cadastro dos produtos de cartão utilizados nas transações.

Permite mapear os produtos entre Sankhya e Conciliadora (crédito à vista, crédito parcelado, débito, etc.).

#### **(3)** Meio Captura

Cadastro dos meios de captura das transações (POS, TEF, e-commerce, etc.).

Utilizado para identificar a origem da venda no processo de conciliação.

#### **(4)** Tipos Título

Configuração do mapeamento entre os tipos de título do Sankhya e as modalidades da Conciliadora.

**Campos obrigatórios na aba Conciliadora:**

- (Conciliadora) Participa da Integração com a Conciliadora
- (Conciliadora) Modalidade Conciliadora
- (Conciliadora) Cód. Meio Captura
- (Conciliadora) Cód. Produto Cartão
- (Conciliadora) Cód. Empresa

### Rotina Diária

#### **(1)** Manhã

Verifique a aba **Logger Conciliadora** para identificar erros do processamento noturno

#### **(1)** Ao longo do dia

- Após fechamento de vendas, execute **Enviar Vendas** na tela Estabelecimento
- Confira a aba **Vendas** para validar o envio

#### **(1)** Final do dia (17:30 - automático)

- O sistema busca pagamentos automaticamente
- Caso necessário, execute manualmente o botão **Buscar Pagamentos**

#### **(1)** Semanalmente

- Consulte a aba **Cancelamentos** e trate os casos identificados
- Verifique divergências na aba **Pagamentos** e corrija na tela **Mov. Financeira**
