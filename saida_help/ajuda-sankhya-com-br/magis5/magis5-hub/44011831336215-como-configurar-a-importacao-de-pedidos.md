---
id: "44011831336215"
titulo: "Como configurar a importação de pedidos Fulfillment do Casas Bahia Marketplace no Magis5 Hub?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011831336215-Como-configurar-a-importa%C3%A7%C3%A3o-de-pedidos-Fulfillment-do-Casas-Bahia-Marketplace-no-Magis5-Hub"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T19:12:02Z"
rotulos: ["sync_hc", "magis5", "magis5_204050497928", "sync_hash_b5db5dfcc82e"]
---

# Como configurar a importação de pedidos Fulfillment do Casas Bahia Marketplace no Magis5 Hub?

## O Fulfillment é um serviço logístico disponibilizado pelo Casas Bahia Marketplace, onde você vende e a Casas Bahia emite a Nota Fiscal, embala o produto, realiza a entrega e cuida do pós-venda.

---

Caso possua uma conta Casas Bahia Marketplace que esteja no programa [Envvias](https://suportemarketplace.viavarejo.com.br/lojista/artigo/?kbid=KA-01543&title=O%20que%20%C3%A9%20Envvias) e também no [Fulfillment,](https://suportemarketplace.viavarejo.com.br/pt-BR/lojista/artigo/?kbid=KA-01924&title=Via%20Fulfillment&cat=Envvias) será necessário que ela possua duas integrações no Magis5 Hub.
Uma integração para o programa Envvias, que é possível acompanhar o passo a passo através [deste link](https://sankhya.zendesk.com/hc/pt-br/articles/44011398314647) e outra para a logística Fulfillment que as instruções estarão no manual abaixo:

**Requisito**

- Abra um chamado pelo [Suporte ao Lojista](https://suportemarketplace.viavarejo.com.br/lojista/) com a categoria 'Token' e o assunto 'Solicitação de token' e solicite o token para os **pedidos Fulfillment**para integração com o Magis5 Hub.

Para isso no Magis5 Hub clique em **"Configurações"** e depois em **"Marketplaces".**

![Imagem 1: Para isso no Magis5 Hub clique em "Configurações" e depois em "Marketplaces".](https://ajuda.magis5.com.br/hubfs/undefined-Feb-21-2023-12-04-10-6564-AM.png)

Após isso clique em**"Adicionar nova integração".**

Selecione "Casas Bahia" no campo marketplace e preencha os campos conforme abaixo: 

**Nome da sua loja:** O nome da sua preferência e que refira Fulfillment(Ex: Magis5 Store Full)
**Token de acesso:**O token informado no [chamado aberto](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011831336215-Como-configurar-a-importa%C3%A7%C3%A3o-de-pedidos-Fulfillment-do-Casas-Bahia-Marketplace-no-Magis5-Hub#requisito).

![Imagem 2: Nome da sua loja: O nome da sua preferência e que refira Fulfillment(Ex: Magis5 Store Full) Token de acesso: O token…](https://ajuda.magis5.com.br/hubfs/undefined-Feb-21-2023-12-04-10-8260-AM.png)

Após isso clique em **"Notas fiscais"** e selecione um ERP para os pedidos serem puxados e processados corretamente no Magis5 Hub.

A emissão da Nota Fiscal será de responsabilidade da Casas Bahia e, por conta disso, não se faz necessário ativar as flags de **"Gerar Nota Fiscal de forma automática"** e **"Emitir Nota Fiscal de forma automática"**.

Após cadastrar todas as informações, basta clicar no botão **"Realizar Integração"**

![Imagem 3: Após cadastrar todas as informações, basta clicar no botão "Realizar Integração"](https://ajuda.magis5.com.br/hubfs/undefined-Feb-21-2023-12-04-10-5247-AM.png)

E pronto! Essa integração será responsável por buscar apenas os pedidos com logística Fulfillment da Casas Bahia Marketplace, enquanto a integração antiga irá continuar fazendo a gestão dos pedidos que não possuem a logística Fulfillment.

[![Universidade Magis5](https://ajuda.magis5.com.br/hs-fs/hubfs/Banner%20Universidade%20Magis5.png?width=688&height=68&name=Banner%20Universidade%20Magis5.png)](https://download.magis5.com.br/universidade-magis5?utm_source=central_de_ajuda&utm_medium=link&utm_campaign=central_de_ajuda&hsLang=pt-br)
