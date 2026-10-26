---
id: "42950783401879"
titulo: "Parâmetro \"is + Nome do Cliente\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950783401879-Par%C3%A2metro-is-Nome-do-Cliente"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Configurações"
atualizado_em: "2026-09-14T14:16:37Z"
rotulos: ["sync_hc", "vidya", "sync_hash_758a142a7e8a", "vidya_600138"]
---

# Parâmetro "is + Nome do Cliente"

## 1. Contexto — Como funcionava antes

Para o aplicativo acessar o ERP, ele depende de um **Base64** com as informações necessárias de acesso. Esse Base64 era composto por duas informações:

1. **Link do RP (ERP)** — essa parte se mantém igual até hoje.
2. **Link do cliente** — basicamente o nome do cliente somado às informações fixas do sistema. Exemplo, para o cliente Junco:`junco.force.vidyacode.com.br`

Como cada cliente possuía seu próprio ambiente na AWS, o **link da AWS já vinha com o nome do cliente embutido**. Isso era usado como referência: sempre que era necessário localizar ajustes, customizações ou qualquer modificação feita para aquele cliente, o sistema usava o nome presente no link da AWS para saber "isso é da Junco, então busque os ajustes da Junco".

## 2. O que mudou — Ambiente unificado

Atualmente o cadastro de clientes passou a ser feito em um **ambiente único e unificado** dentro da AWS, feito via **Postman**. Isso trouxe dois problemas para a identificação do cliente:

- O **link da AWS deixou de ser individual por cliente** — agora todo mundo aponta para o mesmo endereço unificado, algo como `api.force.vidyacode.com.br`, sem nenhuma referência ao nome do cliente.
- Em muitos casos, o **link do ERP do próprio cliente também não tem o nome dele** — pode conter o nome de outra empresa (ex.: ambiente de terceiros) ou até mesmo um IP.

Com isso, o sistema **perde a referência de qual cliente está acessando**, e não consegue mais localizar automaticamente os ajustes, customizações e modificações específicas daquele cliente — porque não há mais nenhum lugar (nem no link do ERP, nem no link da AWS) onde o nome dele apareça de forma confiável.

## 3. Solução — Parâmetro "is + Nome do Cliente"

Para resolver isso, foi criado um novo método de identificação, feito diretamente no Sankhya:

1. Acessar o **Navegador Sankhya** → **Construtor de Telas**.
2. Ir até a **tela de Configurações**.
3. Criar um novo parâmetro no formato: **`IS` + nome do cliente**
   - Exemplo, para o cliente Junco: **`ISJUNCO`**
4. Esse parâmetro deve ter o tipo **Sim/Não**.
5. **Marcar o parâmetro como "Sim"** para o cliente correspondente.

Na prática, isso funciona como uma validação: o sistema pergunta "isso é da Junco?" — e, com o parâmetro `ISJUNCO` marcado como "Sim", ele confirma que sim, e passa a buscar corretamente todos os ajustes, customizações e modificações feitas para aquele cliente, mesmo estando no ambiente unificado.

## 4. Resultado esperado

Depois de criado e marcado o parâmetro `IS + nome do cliente` na tela de Configurações:

- O sistema volta a identificar corretamente o cliente, mesmo sem depender do nome dele estar presente no link do ERP ou no link da AWS.
- Os ajustes, customizações e modificações específicas daquele cliente voltam a ser aplicados normalmente.
- O cliente volta a funcionar normalmente dentro do ambiente unificado, sem necessidade de reverter para um ambiente AWS individual.

## 5. Observação

Esse ajuste deve ser feito **cliente a cliente**, criando o parâmetro correspondente (`IS` + nome) para cada um que apresentar esse problema de identificação no ambiente unificado.
