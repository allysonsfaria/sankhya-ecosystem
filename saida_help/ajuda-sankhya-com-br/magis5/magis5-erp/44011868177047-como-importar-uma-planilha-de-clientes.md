---
id: "44011868177047"
titulo: "Como importar uma planilha de Clientes?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011868177047-Como-importar-uma-planilha-de-Clientes"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:13:19Z"
rotulos: ["sync_hc", "magis5", "magis5_204048155922", "sync_hash_03151d598b87"]
---

# Como importar uma planilha de Clientes?

## Neste tutorial, você aprenderá a formatar sua planilha de clientes para importá-la com sucesso no Magis5 ERP. Siga os passos abaixo para garantir que sua base de dados esteja corretamente configurada.

#### Passo 1: Preparando a Planilha

### 1.1 Estrutura da Planilha

- **Coluna A**: Nome do Cliente ou Razão Social
- **Coluna B**: Tipo de pessoa
- **Coluna C**: CNPJ
- **Coluna D**: CPF
- **Coluna E**: Inscrição Estadual (IE)
- **Coluna F**: RG
- **Coluna G**: Data de Nascimento
- **Coluna H**: Nome Fantasia
- **Coluna I**: Rua
- **Coluna J**: Número
- **Coluna K**: Complemento
- **Coluna L**: Bairro
- **Coluna M**: CEP
- **Coluna N**: Cidade
- **Coluna O**: Estado
- **Coluna P**: Telefone
- **Coluna Q**: Celular
- **Coluna R:** Email
- **Coluna S**: Regime Tributário
- Coluna T: ID Perfil

![Imagem 1: Coluna T: ID Perfil](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/06/image-10.png)

### 1.2 Formato dos Dados

Certifique-se de que cada coluna contenha apenas os dados correspondentes:

- **Nome do Cliente ou Razão Social**: Campo de Texto (exemplo: João Silva)
- **Tipo de pessoa:** "PF" para Pessoa Física ou "PJ" para Pessoa Jurídica
- **CNPJ:** Formato 11.111.111/0001-11 (preencher com pontos, barra e hífen)
- **CPF:** Formato 11111111111 (preencher sem pontos)
- **Inscrição Estadual (IE):** Formato 11111111111 (preencher sem pontos)
- **RG:** Formato 111111111 (preencher sem pontos)
- **Data de Nascimento:** Formato 01012000 (sem barras)
- **Nome Fantasia:** Texto (exemplo: João Silva)
- **Rua:** Não preencher, o CEP fará a busca automática
- **Número:** Campo numérico (não inserir letras ou caracteres especiais)
- **Complemento:** Campo de texto (exemplo: Casa branca, de esquina)
- **Bairro:** Não preencher, o CEP fará a busca automática
- **CEP:** Formato 11111111 (Preencher sem o hífen)
- **Cidade**: Não preencher, o CEP fará a busca automática
- **Estado**: Não preencher, o CEP fará a busca automática
- **Telefone**: Campo numérico com DDD e número (9 a 11 caracteres), sem hífen e DDI. Não deve começar com zero (exemplo: 1935333333)
- **Celular**: Campo numérico com DDD e número (11 a 12 caracteres), sem hífen e DDI. Não deve começar com zero (exemplo: 19999999999)
- **Email**: Campo de texto (exemplo: teste@teste.com.br)
- **Regime Tributário:** Para PJ, usar "21" (Simples Nacional), "22" (Simples Nacional com Excesso de Sub-Limite), ou "23" (Regime Normal)
- **ID Perfil:**  Identificar o ID do perfil do cliente no empreendimento de cadastro (acessar: Configurações → Usuário → Perfis de Acesso). Os perfis serão “atacado”, “parceiro”, “varejo”, “intermediário I” ou “intermediário II”.

#### Passo 2: Salvando a Planilha

Após organizar e revisar os dados, salve a planilha no formato **XLSX**:

1. Clique em **Arquivo**.
2. Selecione **Salvar Como**.
3. Escolha o formato **XLSX.**
4. Nomeie o arquivo e clique em **Salvar.**

#### Dicas Adicionais

- **Verifique Duplicatas**: Antes de importar, assegure-se de que não há registros duplicados na sua planilha.
