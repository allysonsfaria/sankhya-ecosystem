---
id: "44011868739223"
titulo: "[Tracking] - Versão 4.3.0 Tracking"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011868739223--Tracking-Vers%C3%A3o-4-3-0-Tracking"
trilha: "Lincros > Releases (Atualizações) > Tracking (Releases)"
atualizado_em: "2026-10-05T19:13:31Z"
rotulos: ["sync_hc", "lincros", "lincros_13434704", "sync_hash_53fa7c419882"]
---

# [Tracking] - Versão 4.3.0 Tracking

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/44011882833559)

## Release Notes Versão 4.3.0

**NOVIDADES**
 **Iniciar rota via código QR/Token**

Foi disponibilizado na versão 4.3.0 uma nova forma de realizar o login/inicio de viagem via aplicativo utilizando a leitura de um QRCode.

![Imagem 2: Foi disponibilizado na versão 4.3.0 uma nova forma de realizar o login/inicio de viagem via aplicativo utilizando a…](https://ajuda.sankhya.com.br/hc/article_attachments/44011860594455)

O QRCode só pode ser usado uma vez, e caso seja necessário realizar o login novamente é possível utilizar a opção adicional de login por token;

No smartphone, basta selecionar a opção “**NÃO POSSUI UM CÓDIGO QR?**” e informar a placa e o respectivo token gerado. Uma vez utilizado (tanto o token quanto o código QR) eles ficarão inutilizáveis.

## Premissas para utilização desta funcionalidade

- Versão Web 4.3.0 ou superior;
- Versão Mobile 02.01.00061 ou superior;

## MELHORIAS

## Reorganizar modal de Cadastro de Unidades de Negócio

Foi realizada uma alteração de layout na tela de cadastro de unidades para melhorar a visualização das informações, distribuindo as configurações em seções no modo acordeom (abre e fecha)

![Imagem 3: Foi realizada uma alteração de layout na tela de cadastro de unidades para melhorar a visualização das informações,…](https://ajuda.sankhya.com.br/hc/article_attachments/44011891899927)

## MDM001 - Importar rotas com motorista sem cpf

A partir da versão 4.3.0 será possível importar rotas utilizando o Modelo MDM001 sem a informação do CPF do motorista desde que:

1. Não seja utilizada a integração com Gamification
2. Não utiliza cpf do motorista como senha no login do app Gestão de entregas.

## CORREÇÕES

## Atualizar pacote do ApacheNMS no projeto da Pósitron

Realizada atualização de biblioteca ApacheNMS do projeto Pósitron.
 **Erro ao realizar Login: não possui nenhuma transportadora vinculada** Realizado tratamento de exceção em alguns casos onde ocorria a mensagem “ não possui nenhuma transportadora vinculada“ mesmo o usuário possuindo transportadora vinculada.

## Nulos não tratados no método AtualizarInformacoes do IMobil

Realizados tratamentos de exceção para nulos não tratados no método AtualizarInformacoes do WS IMobile.

## Relatório de aderência com erro

Corrigido divergência de informações entre o relatório e a tela de monitoramento.

## WS de Retroalimentação não está retornando a nível de item

Corrigido o valor dos parâmetros pnp e itemNF quando não passados na requisições, terem valor padrão true

![Imagem 4: Corrigido o valor dos parâmetros pnp e itemNF quando não passados na requisições, terem valor padrão true](https://ajuda.sankhya.com.br/hc/article_attachments/44011861027991)
