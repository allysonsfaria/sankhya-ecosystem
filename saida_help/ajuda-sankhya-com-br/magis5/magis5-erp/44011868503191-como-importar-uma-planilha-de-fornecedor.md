---
id: "44011868503191"
titulo: "Como importar uma planilha de Fornecedores?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011868503191-Como-importar-uma-planilha-de-Fornecedores"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:13:21Z"
rotulos: ["sync_hc", "magis5", "magis5_204048115778", "sync_hash_ec61f7e34029"]
---

# Como importar uma planilha de Fornecedores?

## Neste tutorial, você aprenderá a formatar sua planilha de fornecedores para importá-la com sucesso no Magis5 ERP.

#### Passo 1: Preparando a Planilha

### 1.1 Estrutura da Planilha

- **Coluna A**: Tipo de Cadastro
- **Coluna B**: CPF
- **Coluna C**: CNPJ
- **Coluna D**: IE
- **Coluna E**: Nome Fornecedor / Razão Social
- **Coluna F**: Nome Fantasia
- **Coluna G**: CEP
- **Coluna H**: Logradouro
- **Coluna** I: Número
- **Coluna J**: Bairro
- **Coluna K**: Estado
- **Coluna L**: Cidade
- **Coluna M**: Complemento
- **Coluna N**: Telefone 1
- **Coluna O**: Telefone 2
- **Coluna P**: E-mail
- **Coluna Q**: Natureza Padrão
- **Coluna R**: Banco
- **Coluna S**: Agência
- **Coluna T**: Conta Corrente

![Imagem 1: Coluna T : Conta Corrente](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/08/image-1.png)

### 1.2 Formato dos Dados

Certifique-se de que cada coluna contenha apenas os dados correspondentes:

- **Tipo de Cadastro**: “PF” para Pessoa Física ou “PJ” para Pessoa Jurídica
- **CPF**: Formato 111.111.111-00 (preencher com pontos e hífen)
- **CNPJ**: Formato 11.111.111/0001-11 (preencher com pontos, barra e hífen)
- **IE**: Formato 11111111111 (preencher sem pontos)
- **Nome Fornecedor / Razão Social**: Campo de Texto (exemplo: João Silva)
- **Nome Fantasia**: Campo de Texto (exemplo: João Silva)
- **CEP**: Formato 11111111 (Preencher sem o hífen)
- **Logradouro**: Não preencher, o CEP fará a busca automática
- **Número**: Campo numérico (não inserir letras ou caracteres especiais)
- **Bairro**: Não preencher, o CEP fará a busca automática
- **Estado**: Não preencher, o CEP fará a busca automática
- **Cidade**: Não preencher, o CEP fará a busca automática
- **Complemento**: Campo de texto (exemplo: Casa branca, de esquina)
- **Telefone 1**: Campo numérico com DDD, número e hífen (9 a 12 caracteres). Não deve começar com zero (exemplo: 1935333333 ou 19999999999)
- **Telefone 2**: Campo numérico com DDD, número e hífen (9 a 12 caracteres). Não deve começar com zero (exemplo: 1935333333 ou 19999999999)
- **E-mail**: Campo de texto (exemplo: teste@teste.com.br)
- **Natureza Padrão**: É o plano de contas cadastrado no empreendimento (exemplo: 1000.1)
- **Banco**: Utilizar a planilha de [referência - bancos](https://docs.google.com/spreadsheets/d/e/2PACX-1vSv-R0QpI2jRbF3Knd7X1djpNy3zYQG0NFHXlHYeA_z4WgJmFKJmejT_34z40r0bxKWnYuc3bbNtjXR/pubhtml?gid=1516312806&single=true)
- **Agência**: Campo numérico (não inserir letras ou caracteres especiais)
- **Conta Corrente**: Campo numérico (não inserir letras ou caracteres especiais).

#### Passo 2: Salvando a Planilha

Após organizar e revisar os dados, salve a planilha no formato **XLSX**:

1. Clique em **Arquivo**.
2. Selecione **Salvar Como**.
3. Escolha o formato **XLSX.**
4. Nomeie o arquivo e clique em **Salvar**.

#### Dicas Adicionais

- Quantidade média de itens por planilha: 20 mil linhas
