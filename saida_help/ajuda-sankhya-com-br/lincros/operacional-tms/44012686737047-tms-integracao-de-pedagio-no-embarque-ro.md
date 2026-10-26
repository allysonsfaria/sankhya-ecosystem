---
id: "44012686737047"
titulo: "[TMS] - Integração de pedágio no embarque (Routing X TMS)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012686737047--TMS-Integra%C3%A7%C3%A3o-de-ped%C3%A1gio-no-embarque-Routing-X-TMS"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T19:35:44Z"
rotulos: ["sync_hc", "lincros", "lincros_13433387", "sync_hash_4da4337fa34e"]
---

# [TMS] - Integração de pedágio no embarque (Routing X TMS)

**Menu**: Operacional > Cargas > Embarques

**Objetivo:**Integrar os valores de pedágio informados nas sessões do Routing para o embarque no TMS

## Considerações:

- Possuir pedágio cadastrado no Routing;
- Possuir o componente 'TaxaRouter' no cadastro da empresa no Routing;
- Possuir este mesmo componente cadastrado no TMS;

## Configurando o Routing

       1. Informar o componente 'TaxaRouter' no cadastro da empresa no menu: Cadastro > Empresa;

**Obs**.: Essa tela somente o Helpdesk possui acesso, portanto é necessário que seja aberto um chamado junto ao HelpDesk solicitando essa inclusão no cadastro.

       2. Possuir cadastro de pedágio no Routing para o seu depósito, acessar o menu: Cadastros > Pedágio;

![Imagem 1: 2. Possuir cadastro de pedágio no Routing para o seu depósito, acessar o menu: Cadastros > Pedágio;](https://ajuda.sankhya.com.br/hc/article_attachments/44012680051223)

## Configurando o TMS

1. Cadastrar o componente 'TaxaRouter' no menu: Cadastros gerais > Configurações da empresa > Componentes de frete;

![Imagem 2: Cadastrar o componente 'TaxaRouter' no menu: Cadastros gerais > Configurações da empresa > Componentes de frete;](https://ajuda.sankhya.com.br/hc/article_attachments/44012680192663)

       2. No campo 'Código movimento' será necessário criar um novo tipo de movimento no menu: Cadastros gerais > Configurações da empresa > Tipos de movimento, e vincular o componente criado acima, para posteriormente preencher esse campo no cadastro do componente;

![Imagem 3: 2. No campo 'Código movimento' será necessário criar um novo tipo de movimento no menu: Cadastros gerais >…](https://ajuda.sankhya.com.br/hc/article_attachments/44012651812375)

![Imagem 4: 2. No campo 'Código movimento' será necessário criar um novo tipo de movimento no menu: Cadastros gerais >…](https://ajuda.sankhya.com.br/hc/article_attachments/44012672234775)

![Imagem 5: 2. No campo 'Código movimento' será necessário criar um novo tipo de movimento no menu: Cadastros gerais >…](https://ajuda.sankhya.com.br/hc/article_attachments/44012652003991)

![Imagem 6: 2. No campo 'Código movimento' será necessário criar um novo tipo de movimento no menu: Cadastros gerais >…](https://ajuda.sankhya.com.br/hc/article_attachments/44012680674583)

## Abaixo segue um Passo a passo

1. No Routing, criar uma sessão onde uma rota passe pelo pedágio já cadastrado, conforme passos anteriores;

   ![Imagem 7: No Routing, criar uma sessão onde uma rota passe pelo pedágio já cadastrado, conforme passos anteriores;](https://ajuda.sankhya.com.br/hc/article_attachments/44012680880279)
2. Exportar a sessão para o TMS;

   ![Imagem 8: Exportar a sessão para o TMS;](https://ajuda.sankhya.com.br/hc/article_attachments/44012702902807)
3. Verificar no LOG do embarque no TMS se o embarque importou com sucesso. Acessar o menu: Operacional > Importação > Cargas > Embarques > Log;

   ![Imagem 9: Verificar no LOG do embarque no TMS se o embarque importou com sucesso. Acessar o menu: Operacional > Importação >…](https://ajuda.sankhya.com.br/hc/article_attachments/44012688029463)
4. Se no LOG sinalizar que foi importado com sucesso, o embarque já ira aparecer no menu: Operacional > Cargas > Embarques, e na aba 'Taxas adicionais' irá aparecer o valor do pedágio do Routing;

   ![Imagem 10: Se no LOG sinalizar que foi importado com sucesso, o embarque já ira aparecer no menu: Operacional > Cargas >…](https://ajuda.sankhya.com.br/hc/article_attachments/44012673154071)

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
