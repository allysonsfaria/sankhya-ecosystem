---
id: "44010568961175"
titulo: "[TMS] Como Importar Pessoas via Planilha"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010568961175--TMS-Como-Importar-Pessoas-via-Planilha"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T18:41:31Z"
rotulos: ["sync_hc", "lincros", "lincros_15139750", "sync_hash_ebb07b7e1741"]
---

# [TMS] Como Importar Pessoas via Planilha

## O que é a importação via planilha?

A importação de Pessoas via planilha permite cadastrar ou atualizar múltiplos registros de uma só vez, sem a necessidade de editar cada cadastro individualmente. É a forma indicada para realizar cargas iniciais de cadastros ou para corrigir dados em lote, como razão social ou endereço.

O sistema oferece dois modos de operação:

- **Persistir** — cria novos registros de Pessoas que ainda não existem no sistema.
- **Sobrescrever** — atualiza os dados de Pessoas já existentes, identificadas pelo CNPJ/CPF.

⚠️ Nas importações automáticas de NF-e e CT-e, o nome da Pessoa **não é sobrescrito automaticamente** — isso é uma proteção intencional do sistema. Para corrigir o nome de uma Pessoa, utilize este processo com o modo **Sobrescrever**.

## 1. Acessar a tela de Pessoas

No menu principal, navegue até:

`Cadastros Gerais > Cadastros Gerais Pessoas > Cadastro`

## 2. Baixar o modelo da planilha

Na tela de listagem de Pessoas, clique no botão **"Modelo"**. O sistema fará o download de um arquivo **.xlsx** com as abas e colunas no formato correto esperado para a importação.

💡 Sempre utilize o modelo baixado diretamente do sistema para garantir compatibilidade.

## 3. Preencher a planilha

A planilha possui três abas:

| Aba | Descrição |
| --- | --- |
|  |  |
| **ABA\_PESSOA** | Onde os dados das Pessoas devem ser preenchidos. |
| **ABA\_EXEMPLO** | Exemplo preenchido para referência. Não enviar dados reais aqui. |
| **ABA\_COD\_IBGE** | Tabela de códigos IBGE de municípios para preenchimento correto da cidade. |

**Campos principais da ABA\_PESSOA:**

| Campo | Obrigatório | Descrição |
| --- | --- | --- |
| CNPJ / CPF | Sim | Documento da Pessoa (14 dígitos para CNPJ, 11 para CPF) |
| Razão Social | Sim | Nome da Pessoa conforme deve aparecer no sistema |
| Nome Fantasia | Não | Nome fantasia |
| CEP | Não | CEP do endereço |
| Logradouro | Não | Rua / Avenida |
| Bairro | Não | Bairro |
| Código IBGE | Não | Código IBGE do município (consultar ABA\_COD\_IBGE) |
| UF | Não | Estado (sigla, ex: SP) |

💡 Preencha apenas as linhas com dados reais. Não altere os cabeçalhos das colunas.

## 4. Importar a planilha

Na tela de listagem de Pessoas, clique no botão **"Importar"**. Uma janela será exibida com as seguintes opções:

1. Selecionar o arquivo — escolha a planilha preenchida no passo anterior.
2. Escolher o modo de importação:

   - **Persistir** — para criar novas Pessoas.
   - **Sobrescrever** — para atualizar Pessoas já existentes.
3. Clicar em **Confirmar** para iniciar a importação.

## 5. Verificar o resultado

Após a importação, o sistema exibirá um resumo indicando quantos registros foram criados ou atualizados com sucesso, e se houve erros em alguma linha com a indicação do motivo. Corrija os erros apontados e reimporte apenas as linhas com problema, se necessário.
