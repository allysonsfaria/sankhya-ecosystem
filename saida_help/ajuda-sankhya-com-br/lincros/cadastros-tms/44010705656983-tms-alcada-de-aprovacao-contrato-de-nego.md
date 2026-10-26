---
id: "44010705656983"
titulo: "[TMS] - Alçada de aprovação Contrato de Negociação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010705656983--TMS-Al%C3%A7ada-de-aprova%C3%A7%C3%A3o-Contrato-de-Negocia%C3%A7%C3%A3o"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T18:45:01Z"
rotulos: ["sync_hc", "lincros", "lincros_13432630", "sync_hash_46f55fc5af9e"]
---

# [TMS] - Alçada de aprovação Contrato de Negociação

**Menu**: Cadastros gerais > Configurações da empresa > Workflow > Alçadas de aprovação

**Objetivo**: O objetivo da alçada de aprovação no contrato de negociação, é ter um fluxo no workflow do mesmo para definir os aprovadores de acordo com os valores definidos no tipo de alçada;

**Considerações**:

- No menu Cadastros gerais > Configurações da empresa > Parâmetros - Empresa, é necessário estar com o parâmetro "usarAlcadaAprovacaoContrato" como true;
- Esse parâmetro indica que o sistema usará alçada de aprovação para contrato de negociações;

Abaixo segue os procedimentos

## Para cadastrar a alçada de aprovação

1. A alçada de aprovação é cadastrada em Cadastros gerais > Configurações da empresa > Workflow - Alçadas de aprovação;
2. Ao clicar em "Novo" para cadastrar uma nova alçada, é necessário selecionar o "Tipo de restrição" como "Contrato de negociações", definir o tipo da alçada que pode ser valor, viagem, cubagem ou peso nominal e os perfis do aprovador e próximo perfil a aprovar.

![Imagem 1: Ao clicar em "Novo" para cadastrar uma nova alçada, é necessário selecionar o "Tipo de restrição" como "Contrato de…](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963050648/252dbc5ea8be56202880ce8bd2a4/6DD577130E6E510835B6C75DE3DAD3B1?expires=1791331200&signature=9be348a7e4393f0a491e20bbd4c80edc2d2fea19ad75185fc7363d726eacb4b2&req=dSkhFcl7nYdbUfMW3nq%2BgTL4uGLb8cQvwisOnd07EBbhA3CQOu3fNg7%2BA3UB%0AJcrciYmyqpuLT5fwlOjb%2BgmEGQo%3D%0A)

3. Em seguida verificar a necessidade de habilitar as opções de Justificativas e Envio de e-mail;

![Imagem 2: 3. Em seguida verificar a necessidade de habilitar as opções de Justificativas e Envio de e-mail;](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963050661/3dabd6ab77dd959b14ee5dad9b12/1D0C0669FC0AAEAD71284DAB8A8B9A53?expires=1791331200&signature=b3e87fb96126ce1d7e87c3a7459f74bd75eb357e8f26388594e6e50fae120067&req=dSkhFcl7nYdZWPMW3nq%2BgUKm1hQ%2FARhKWyi9RnPEg8AMrDVElYNau70KTPmS%0An9ZHnSy4vwqR4350NMlGF2NNZOA%3D%0A)

**Obs:** A alçada por hierarquia possui o comportamento de níveis obrigatórios de aprovação, ou seja, ela exige que cada nível aprove, respeitando sempre os níveis anteriores; Para isso, é necessário que o parâmetro "usarAlcadaAprovacaoRespeitandoHierarquia" esteja cadastrado como true, e os níveis de aprovação informados no cadastro da alçada: Perfil e Próximo perfil a aprovar;

## Exemplo:

Tipo de alçada: Valor, com faixa de 0 a 100,00;

Primeiro nível de aprovação: Gerencial;

Segundo nível de aprovação: Administrador.

Após informar os níveis é possível visualizar no final da tela a árvore de aprovação.

![Imagem 3: Após informar os níveis é possível visualizar no final da tela a árvore de aprovação.](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963050670/ac328f9d9ee3dec1f3c9fd7138ec/F9EE647690E3AF8266DD9E52F666116C?expires=1791331200&signature=28e25aa710fce258694fb39a8ff6d2266af22824a302b74bb0bf6ceacb1cb39d&req=dSkhFcl7nYdYWfMW3nq%2BgQRdt4RPsvFHsXCYdneSNPfqYZL3QxUWaiw2W6Be%0AfutrdnoW%2F4%2F3NersrDVbDUCwrYs%3D%0A)

- Se o parâmetro para respeitar hierarquia estiver cadastrado como true, o Administrador só poderá deferir/indeferir um contrato de negociações caso o usuário de perfil Gerencial já tenha deferido o mesmo.
- O usuário gerencial só poderá deferir/indeferir contratos que possuam tipo de controle com valor até R$ 100,00.

![Imagem 4: O usuário gerencial só poderá deferir/indeferir contratos que possuam tipo de controle com valor até R$ 100,00.](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963050679/035e8cebc4024b2894dada7806f1/60EEEBA3913BD4C324A08353C6A02C51?expires=1791331200&signature=2e836599416fcc2d039a5b508aee89944df30d440bfe8651e3a75d8c2f732223&req=dSkhFcl7nYdYUPMW3nq%2BgcDw4mCM8myF1ywa5G6uke5ufDbiwSau0ZkbbbaT%0Ap4j68mZbTSrHbP4eAxr8v60fNbo%3D%0A)

- Se o parâmetro para respeitar hierarquia estiver cadastrado como false, o usuário de perfil Administrador poderá deferir/indeferir o contrato sem ter sido deferido pelo usuário de perfil Gerencial.

![Imagem 5: Se o parâmetro para respeitar hierarquia estiver cadastrado como false, o usuário de perfil Administrador poderá…](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963050684/6cef02200f87abe419a2cebb7e0f/387A0327D6779AC891707E142E3698E8?expires=1791331200&signature=d7509ae0be9bd300c23ac3f6857bdd1a6a514eec4fd71dce5a531b010bd2a47e&req=dSkhFcl7nYdXXfMW3nq%2BgTnc%2FYAd5nq%2BdZ1aZri%2Fr8Y1UnmxePngQAXzAIK3%0Axlr8Xi3kkcZMBazM0CnBz74lOKc%3D%0A)

O contrato de negociações é acessado através do menu: Cadastros gerais > Transportadoras > Negociações > Contrato de negociações, onde há maiores informações sobre seu funcionamento no artigo [[TMS] - Contratos de Negociação](https://sankhya.zendesk.com/hc/pt-br/articles/44010705656983).

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
