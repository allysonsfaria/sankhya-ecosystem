---
id: "44010580255639"
titulo: "[Tracking] Cadastro de motoristas via Upload"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010580255639--Tracking-Cadastro-de-motoristas-via-Upload"
trilha: "Lincros > Tracking"
atualizado_em: "2026-10-05T18:41:02Z"
rotulos: ["sync_hc", "lincros", "lincros_15556339", "sync_hash_5cd2778bc0ad"]
---

# [Tracking] Cadastro de motoristas via Upload

## Objetivo

Realizar o cadastro de motoristas em massa no Tracking por meio do envio de um arquivo CSV, sem a necessidade de preencher os dados manualmente um a um.

## Caminho

Menu > Cadastros > Motoristas

## Pré-Requisitos

A integração de importação de motoristas deve estar ativa no ambiente. Caso não esteja habilitada, é necessário abrir chamado com o suporte Lincros para solicitar a ativação.

## Cadastro de Motoristas via Upload

É possível cadastrar motoristas em massa pela tela de Cadastros de Motoristas, utilizando o botão Upload para enviar um arquivo CSV com os dados dos motoristas.

## Como realizar o Procedimento

Passo 1 - Menu

Passo 2 - Cadastros

Passo 3 - Motoristas

Passo 4 - Upload: Clique no botão Upload.

Passo 5 - Preparar o arquivo CSV

O arquivo deve seguir o padrão abaixo:

```
Nome,CPF JOAO DA SILVA,12345678901 MARIA DE SOUZA,98765432100
```

Observações sobre o arquivo:

O nome do arquivo deve iniciar com motorista (ex: motoristas.csv).

O CPF deve conter exatamente 11 dígitos numéricos, sem pontos ou traços.

Somente arquivos no formato .csv são aceitos.

Passo 6 - Selecionar o arquivo: Escolha o arquivo CSV preparado e confirme o envio.

Após o upload, os motoristas serão cadastrados automaticamente no sistema e marcados como Ativos. Os demais dados, como unidade de negócio, transportadora e código de acesso ao aplicativo, serão preenchidos automaticamente quando o motorista for associado a uma rota.
