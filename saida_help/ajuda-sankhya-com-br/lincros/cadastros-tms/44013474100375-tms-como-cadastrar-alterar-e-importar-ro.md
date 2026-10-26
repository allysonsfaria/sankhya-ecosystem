---
id: "44013474100375"
titulo: "[TMS] - Como Cadastrar, Alterar e Importar Rotas da Empresa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013474100375--TMS-Como-Cadastrar-Alterar-e-Importar-Rotas-da-Empresa"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:59:18Z"
rotulos: ["sync_hc", "lincros", "lincros_13432359", "sync_hash_4253ee9acf39"]
---

# [TMS] - Como Cadastrar, Alterar e Importar Rotas da Empresa

## 1 - Problema Relatado pelo Cliente:

O cliente deseja realizar o cadastro de Rotas da Empresa na plataforma, que são utilizadas quando a empresa realiza o transporte e distribuição com frota própria ou quando define a tabela de frete para transportadores e para o módulo de BID de fretes. A dúvida envolve como executar esse cadastro de forma unitária ou em massa, bem como como realizar alterações nas rotas já cadastradas.

---

## 2 - Passo a Passo para Resolver o Problema:

## Cadastro Unitário (Via Plataforma)

1. Acessar o menu: **Cadastros Gerais > Modelo de Distribuição > Rotas da Empresa**.
2. Selecionar o botão **'Novo'**.
3. Preencher os seguintes campos:

   - **Descrição**: Nome da rota.
   - **Origem**: Local de partida da mercadoria. Pode ser uma única cidade, um estado ou uma região pré-cadastrada.
   - **Destino**: Até onde essa mercadoria será transportada. Pode ser uma única cidade, um estado ou uma região pré-cadastrada.
   - **Peso**: Peso que a rota permite.
   - **Pedágio**: Informar se existe ou não um pedágio nesta rota.
   - **Ativa**: Informar se a rota está ativa ou não.

---

## Cadastro em Massa (Via Planilha)

1. Na tela de **Rotas da Empresa**, clicar em **'Modelo'**. O download da planilha será iniciado automaticamente.
2. Preencher as abas disponíveis na planilha:

   - **Rotas**: Informar os dados sobre as rotas — a transportadora (caso haja), a origem, o destino, o peso (não obrigatório), se possui pedágio e se está ativa.
   - **Exemplo**: Utilizar como referência o exemplo de preenchimento da aba Rotas.
   - **Códigos IBGE**: Utilizar como base o glossário contendo o código de todas as cidades do Brasil.
   - **Siglas UF**: Utilizar como base a lista de siglas de todos os estados do Brasil.
3. Após o preenchimento, importar a planilha:

   - Clicar em **'Importar'** na tela inicial de Rotas da Empresa.
   - Adicionar o arquivo e clicar em **'Upload'**.
   - Aguardar a finalização da importação.
4. Após a importação:

   - Verificar o **Resultado da importação**, que indicará a quantidade de linhas com erro, se houver.
   - Abaixo do resultado, consultar a **Relação de ocorrências**, que apresenta uma descrição detalhada dos erros encontrados.

---

## Alteração de Rotas em Massa (Via Planilha)

1. Para alterar rotas já cadastradas:

   - Selecionar a opção **'Exportar em Excel'**.
   - Informar um e-mail para receber a planilha com todas as rotas cadastradas.
2. Após receber a planilha:

   - Fazer o download.
   - Realizar as alterações desejadas.
   - Salvar as modificações.
3. Importar novamente a planilha:

   - Seguir o mesmo procedimento descrito anteriormente na importação.
   - Aguardar o processamento e verificar o resultado da importação.
