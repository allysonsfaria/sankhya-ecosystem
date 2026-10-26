---
id: "44013420018199"
titulo: "[TMS] - Como Resolver o Erro de Código de Ocorrência 99 no TMS para Transportadora"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013420018199--TMS-Como-Resolver-o-Erro-de-C%C3%B3digo-de-Ocorr%C3%AAncia-99-no-TMS-para-Transportadora"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:57:32Z"
rotulos: ["sync_hc", "lincros", "lincros_13432496", "sync_hash_26cca3942619"]
---

# [TMS] - Como Resolver o Erro de Código de Ocorrência 99 no TMS para Transportadora

## 1º Problema Relatado pelo Cliente:

O cliente relatou um erro relacionado à ocorrência de entrega de uma transportadora no sistema TMS, onde o código de ocorrência informado pelo transportador estava sendo registrado automaticamente como 99, em vez do código correto (01 - Entrega). O cliente mencionou que o arquivo EDI estava no padrão 3.0 e questionou se isso poderia ser a causa do erro, sugerindo a utilização do padrão 3.1 para resolver o problema.

## 2º Passo a Passo para Resolver o Problema:

## Identificação do Problema:

O erro de código 99 ocorre quando o sistema TMS não consegue identificar o código de ocorrência fornecido pela transportadora, devido à falta de informações de "De/Para". Isso impede a correlação do código com os códigos de ocorrência cadastrados no sistema, fazendo com que o TMS registre automaticamente o código 99.

## Verificação de Acesso:

Para solucionar o problema, é necessário garantir que o usuário tenha acesso à funcionalidade de cadastro de ocorrências no sistema. Se o acesso não estiver disponível, o perfil de usuário precisa ser verificado.

Essa verificação pode ser feita pelo usuário "administrador".

Caminho: Sistema > Acesso > Usuário > Usuários da empresa.

## Cadastro das Ocorrências:

O cliente pode cadastrar as ocorrências manualmente para a transportadora, mas isso pode ser demorado se houver muitas ocorrências a serem registradas, como o código 99.

## Solução para Cadastro em Massa:

Para agilizar o processo, o TMS oferece uma funcionalidade chamada "Copiar Empresa", que permite copiar ocorrências cadastradas de uma transportadora para outra.

Caminho: "Cadastros Gerais > Transportadoras > Ocorrências > Transportadora".

Ao clicar no botão "Copiar Empresa", o sistema abrirá a tela "Copiar Ocorrências".

O usuário deve escolher a transportadora de destino e selecionar as ocorrências correspondentes, clicando em "Copiar" para concluir o processo.

## Finalização:

Usando a funcionalidade "Copiar Empresa", o usuário pode rapidamente importar as ocorrências para a transportadora sem precisar cadastrá-las manualmente uma a uma.
