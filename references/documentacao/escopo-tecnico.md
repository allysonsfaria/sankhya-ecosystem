# Elaboração de Escopo Técnico de Desenvolvimento

Padrão para especificação de demandas de customização e projetos de integração no ecossistema Sankhya OM.

---

## 1. Estrutura Padrão do Documento de Escopo

Todo escopo técnico para clientes Sankhya deve contemplar os seguintes tópicos estruturados:

```markdown
# Proposta Técnica e Escopo de Desenvolvimento: [Nome da Demanda]

## 1. Objetivo e Contexto da Demanda
- Descrição da dor ou necessidade operacional do cliente.
- Processo de negócio atendido (Vendas, Compras, Financeiro, WMS, etc.).

## 2. Telas e Processos Impactados
- Telas nativas afetadas (ex: Cadastro de Parceiros, Central de Vendas).
- Novas telas personalizadas ou construtores DWF.

## 3. Especificação Técnica dos Artefatos
- **Dicionário de Dados**:
  - Novas tabelas (ex: `XYZ_SOLICITACAO`).
  - Novos campos em tabelas nativas (ex: `TGFCAB.XYZ_STATUS_INTEGRACAO`).
- **Backend Java**:
  - `@ActionButton`: botões de tela com validações e comportamentos.
  - `@Listener`: gatilhos em eventos `beforeInsert`, `afterUpdate`, etc.
  - `@BusinessRule`: validações comerciais no faturamento.
  - `@Job`: rotinas em background e agendamentos.
- **Integração / APIs**:
  - Endpoints consumidos ou expostos.
  - Formato dos payloads (JSON/XML) e autenticação.
- **Relatórios / BI**:
  - Relatórios formatados Jasper (`.jrxml`) ou Gadgets de Dashboard.

## 4. Premissas e Regras de Negócio
- Condições obrigatórias para execução da rotina.
- Parâmetros do sistema requeridos.

## 5. Critérios de Aceite e Homologação
- Cenários de teste para validação pelo usuário chave.
```
