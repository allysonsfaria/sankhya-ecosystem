# Metamodelo do Dicionário de Dados (Sankhya OM)

O Dicionário de Dados é o coração do Sankhya OM, definindo todas as tabelas, campos, chaves primárias, relacionamentos e regras de validação consumidas pelo JAPE, DWF e interfaces.

---

## 1. Tabelas de Metadados Principais

| Tabela | Nome da Entidade | Descrição |
|---|---|---|
| `TDDTAB` | `TabelaDicionario` | Metadados das tabelas (nome físico, entidade JAPE, descrição, tipo de acesso) |
| `TDDCAM` | `CampoDicionario` | Metadados dos campos (nome físico, rótulo, tipo de dado, tamanho, casas decimais, obrigatório) |
| `TDDLIG` | `LigacaoDicionario` | Relacionamentos e chaves estrangeiras entre tabelas (ligações 1-N, N-1) |
| `TDDOPC` | `OpcaoCampoDicionario` | Enums / opções de valores aceitos em campos de múltipla escolha (ex: `A=Ativo`, `I=Inativo`) |

---

## 2. Prefixo de Campos e Tabelas Customizadas

| Cenário | Regra de Prefixo | Exemplo |
|---|---|---|
| **Campo criado pelo usuário na tela Dicionário de Dados** | Prefixo obrigatório `AD_` | `AD_STATUS_EXT`, `AD_OBSERVACAO` |
| **Tabela criada pelo usuário na tela Dicionário de Dados** | Prefixo obrigatório `AD_` | `AD_HISTORICO` |
| **Artefatos gerados via Addon Studio (AutoDDL)** | **NUNCA usar `AD_`**. Usar prefixo de 3 a 5 letras da empresa/solução | `XYZ_HISTORICO`, `XYZ_CODREF` |

> **Aviso Crítico:** O Sankhya reserva o prefixo `AD_` para customizações manuais de clientes finais. Addons distribuíveis que utilizam `AD_` geram conflito no deploy em clientes que já possuem campos com mesmo nome.

---

## 3. Tipos de Dados Suportados no Metamodelo
- `S` (Texto / String)
- `I` (Inteiro)
- `F` (Ponto Flutuante / Decimal / Moeda)
- `H` (Data e Hora / Timestamp)
- `D` (Data)
- `C` (Opção / Lista com opções em `TDDOPC`)
- `E` (Expressão SQL / Campo Calculado `#type.sql#`)
