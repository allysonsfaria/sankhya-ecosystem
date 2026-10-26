---
id: "44013466887063"
titulo: "[TMS] - Importação de Faixas de CEP no TMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013466887063--TMS-Importa%C3%A7%C3%A3o-de-Faixas-de-CEP-no-TMS"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:57:55Z"
rotulos: ["sync_hc", "lincros", "lincros_13432436", "sync_hash_dfe7479e86a4"]
---

# [TMS] - Importação de Faixas de CEP no TMS

## 1º Problema Relatado pelo Cliente:

O cliente relatou a necessidade de cadastrar um novo parceiro de transporte utilizando faixas de CEP. O cliente questionou a possibilidade de importar uma planilha contendo as faixas de CEP e solicitou instruções sobre como realizar esse procedimento.

## 2º Passo a Passo para Resolver o Problema:

## Fazer Download da Planilha

Acesse Cadastros Gerais > Modelo de Distribuição > Faixas de CEP.

Após acessar a tela de faixas de CEP, filtre uma faixa de CEP qualquer, selecione o botão exportar e escolha a opção Excel.

A planilha será exportada e enviada ao e-mail do usuário.

## Preenchimento da Planilha

Na aba FaixaCEP, você precisa informar os seguintes campos:

- CEP Inicial: Insira o CEP inicial da faixa.
- CEP Final: Insira o CEP final da faixa.
- Nome: Indique o nome da região à qual a faixa de CEP pertence.
- Ativo: Informe VERDADEIRO ou FALSO para indicar se a faixa de CEP está ativa.

**Observação:** Verifique se todos os campos estão preenchidos corretamente para garantir uma importação bem-sucedida.

## Importação da Planilha

No mesmo menu anterior onde foi realizado o download da planilha deve ser realizado a importação (caminho: Cadastros Gerais > Modelo de Distribuição > Faixas de CEP.)

Na tela de faixa de CEP,  clique no botão Importar. Na tela de importação, selecione o arquivo que contém as faixas de CEP a serem importadas e clique em Adicionar para carregar o arquivo. Após adicionar o arquivo, clique em Upload para iniciar a importação, o sistema validará os dados e exibirá o resultado da importação.

## Verificar os Resultados

Após o upload, o sistema exibirá:

- Quantidade de Linhas Importadas com Sucesso: Número de registros válidos importados.
- Quantidade de Linhas com Erro: Caso algum erro tenha ocorrido durante a importação, o sistema mostrará a quantidade de falhas.
- Correção de Erros: Caso existam erros, revise a planilha, corrija as inconsistências e repita o processo de importação.

**Importante:** Após a importação, será necessário associar as faixas de CEP às regiões correspondentes dentro do TMS.
