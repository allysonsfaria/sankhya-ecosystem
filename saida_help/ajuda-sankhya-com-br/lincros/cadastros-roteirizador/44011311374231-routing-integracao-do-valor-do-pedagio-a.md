---
id: "44011311374231"
titulo: "[Routing] - Integração do Valor do Pedágio ao TMS como Taxa Adicional"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011311374231--Routing-Integra%C3%A7%C3%A3o-do-Valor-do-Ped%C3%A1gio-ao-TMS-como-Taxa-Adicional"
trilha: "Lincros > Roteirizador > Cadastros - Roteirizador"
atualizado_em: "2026-10-05T19:01:13Z"
rotulos: ["sync_hc", "lincros", "lincros_13438599", "sync_hash_ffe67a71022c"]
---

# [Routing] - Integração do Valor do Pedágio ao TMS como Taxa Adicional

**Menu Routing**: Cadastros > Empresa

**Menu TMS**: Cadastros gerais > Configurações da empresa > Componentes de frete

**Menu TMS**: Cadastros gerais > Configurações da empresa > Tipos de movimento

**Objetivo**: Realizar o cadastro para integração do valor do pedágio entre o Router e o TMS como taxa adicional.

## Considerações:

- Para realizar a integração do valor do pedágio entre o Router com o TMS, primeiramente deve ser cadastrado um novo componente;
- O vínculo do componente no cadastro de empresa deve ser feito pela equipe do suporte após abertura de um chamado;

Abaixo segue o passo a passo:

1. Acessar o TMS no menu: Cadastros gerais > Configurações da empresa > Tipos de movimento, deve-se cadastrar um novo movimento. Este movimento será vinculado ao componente que será cadastrado;
2. Acessar o TMS no menu: Cadastros gerais > Configurações da empresa > Componentes de frete, deve-se cadastrar um novo componente com as informações básicas, como Código, TaxaRouter, Ordem de Exibição e o Código de Movimento;

**Obs**.: É aconselhável utilizar um nome que referencia a taxa ao Routing. Após criar o componente, revise o cadastro do movimento para certificar se o componente está associado a ele.

      3. Com o componente cadastrado, este deve ser associado no Routing (Cadastros > Empresa);

      4. Descrição da taxa adicional de pedágio no Embarque TMS: Descrição que será utilizada na tela de taxas adicionais;

      5. Componente de frete da taxa adiconal no Embarque TMS: Neste campo deve ser informado o nome do componente cadastrado;

      6. Ao finalizar o cadastro e integrar uma sessão com valores de pedágio nas rotas, os valores serão integrados ao TMS, como taxa adicional sendo realizado o rateio entre os documentos;

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
