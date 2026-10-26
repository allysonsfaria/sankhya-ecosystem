---
id: "44011276077079"
titulo: "[TMS] - Como Cadastrar, Alterar e Importar Rotas de Transportadoras"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011276077079--TMS-Como-Cadastrar-Alterar-e-Importar-Rotas-de-Transportadoras"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:00:57Z"
rotulos: ["sync_hc", "lincros", "lincros_13438746", "sync_hash_3feff788ba26"]
---

# [TMS] - Como Cadastrar, Alterar e Importar Rotas de Transportadoras

## 1 - Problema Relatado pelo Cliente

O cliente relatou dúvidas ou dificuldades relacionadas ao cadastro de rotas de transportadoras na Plataforma. A necessidade consiste em entender como criar rotas de maneira unitária ou em massa, bem como alterar rotas já existentes, garantindo que a configuração esteja correta para uso na tabela de frete.

---

## 2 - Passo a Passo para Resolver o Problema

## Considerações Iniciais

- Antes de iniciar o cadastro, é necessário que a transportadora esteja previamente cadastrada na Plataforma.
- O conceito de Rotas está sempre associado a uma “Origem” e um “Destino”, ambos relacionados à tabela de frete da transportadora.

Na tela de rotas das transportadoras, é possível:

- Visualizar informações como origem, destino, transportadora e descrição da rota.
- Exportar e importar rotas.
- Aplicar filtros de busca e organizar colunas.

Existem três formas de cadastrar uma rota: unitária, em massa e diretamente pela tabela de frete. Neste artigo, abordaremos as duas primeiras.

---

## Cadastro Unitário (Via Plataforma)

1. Acessar o menu:
   **Cadastros Gerais > Transportadoras > Negociações > Rotas > Transportadora**.
2. Selecionar o botão **"Novo"**.
3. Preencher as seguintes informações:

   - **Descrição:** Nome da rota.
   - **Transportadora:** Transportadora à qual a rota está vinculada.
   - **Origem:** Local de partida da mercadoria (cidade, estado ou região pré-cadastrada).
   - **Destino:** Local de entrega da mercadoria (cidade, estado ou região pré-cadastrada).
   - **Peso:** Peso permitido na rota.
   - **Pedágio:** Indicar se há pedágio na rota.
   - **Ativa:** Indicar se a rota está ativa.
4. Salvar o cadastro.

---

## Cadastro em Massa (Via Planilha)

1. Acessar a tela de Rotas.
2. Clicar no botão **“Modelo”**.

   - O download do modelo de planilha será iniciado automaticamente.
3. Preencher a planilha conforme as abas disponíveis:

   - **Rotas:** Informações principais como transportadora, origem, destino, peso (opcional), existência de pedágio e se a rota está ativa.
   - **Exemplo:** Demonstração de preenchimento correto da aba “Rotas”.
   - **Códigos IBGE:** Glossário com os códigos de todas as cidades do Brasil, utilizado como base para preenchimento.
   - **Siglas UF:** Lista de siglas de todos os estados do Brasil, também para consulta no preenchimento.
4. Após o preenchimento, importar a planilha:

   - Clicar em **“Importar”** na tela inicial de Rotas.
   - Adicionar o arquivo e clicar em **“Upload”**.
   - Aguardar o processamento.
5. Após a importação:

   - O campo **“Resultado da importação”** exibirá automaticamente o status, incluindo a quantidade de linhas com erro, se houver.
   - Abaixo do resultado, será apresentada a **“Relação de ocorrências”**, contendo detalhes dos erros encontrados.

---

## Alteração de Rotas em Massa (Via Planilha)

1. Na tela de Rotas, selecionar as rotas desejadas e ir na opção **“Exportar em Excel”**.
2. Informar um e-mail.

   - A Plataforma enviará uma planilha com todas as rotas cadastradas para o e-mail informado.
3. Fazer o download da planilha.
4. Realizar as alterações desejadas diretamente na planilha.
5. Salvar as modificações.
6. Importar novamente a planilha:

   - Acessar a tela de Rotas, clicar em **“Importar”**, adicionar o arquivo e clicar em **“Upload”**.
   - Aguardar o resultado e verificar a **Relação de ocorrências**, se houver.
