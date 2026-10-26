---
id: "44010754196759"
titulo: "[TMS] - Integração VTEX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010754196759--TMS-Integra%C3%A7%C3%A3o-VTEX"
trilha: "Lincros > TMS > VTEX - TMS"
atualizado_em: "2026-10-05T18:46:13Z"
rotulos: ["sync_hc", "lincros", "sync_hash_3c6da7a9ff95", "lincros_13434455"]
---

# [TMS] - Integração VTEX

## Contexto:

A VTex é uma plataforma de e-commerce SaaS. Na prática, isso significa que ela é responsável por toda estrutura necessária para que os lojistas possam cadastrar seus produtos, integrar meios de pagamento, calcular frete, etc.

A integração do Lincros com plataforma de e-commerce Vtex tem o objetivo de facilitar os processos logísticos na plataforma do cliente, como a atualização de valores de fretes, recebimento do pedido (NF-e) para gerenciamento no Lincros e envio de régua de rastreio.

## Pré-requisitos:

Utilizar a plataforma VTEX

---

## Instrucional:

1 - Solicitar a um consultor Lincros que habilite a funcionalidade da integração com a VTEX.

2 - Realizar o cadastro do [integrador VTEX](https://intercom.help/ajudalincros/pt-BR/articles/13434452-tms-integrador-vtex).

3 - [Exportar as tabelas de frete no modelo VTEX](https://sankhya.zendesk.com/hc/pt-br/articles/44010661832215).

- A VTEX não permite consultar valores de frete em outras fontes, como um webservice de cálculo.
- O TMS possibilita exportar as tabelas de frete cadastradas neste modelo para importação na VTEX, e depois é possível atualizar a tabela via TMS.

  - Desta forma é possível incluir a tabela na sua plataforma VTEX.

4 - [Cadastrar a tabela na plataforma VTEX](https://intercom.help/ajudalincros/pt-BR/articles/13432582-tms-cadastrar-tabela-tms-na-plataforma-vtex).

- Após importar a tabela, é possível atualizar os ajustes feitos no TMS através do botão [Atualizar tabela VTEX](https://intercom.help/ajudalincros/pt-BR/articles/13438855-tms-atualizar-tabela-vtex).

5 - A integração do pedido no TMS ocorre, por padrão, quando o status do pedido na plataforma VTEX estiver como faturado.

- O número do pedido da VTex é populado na nota fiscal, no campo Order Id (Vtex)

![Imagem 1: O número do pedido da VTex é populado na nota fiscal, no campo Order Id (Vtex)](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963626089/e570cfd510eff1cb51d00b19918a/9EFDBB710925780A58753B607A03D852?expires=1791331200&signature=ec9f4012ac6cf00771587bb7048357fdfe986714a77da5b62b8b35df05f2a4dc&req=dSkhFc98m4FXUPMW3nq%2BgcZQoKaLdSOtPq7MVXw%2FWmBJNU6Ck%2Fn9d7OMI24X%0AZts0hrh0ZMOkL0VaWBFUjsgXuSY%3D%0A)

6 - Com o pedido integrado, o acompanhamento de rastreio é enviado ao cliente, na forma de régua de rastreio.

![Imagem 2: 6 - Com o pedido integrado, o acompanhamento de rastreio é enviado ao cliente, na forma de régua de rastreio.](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963626108/bb2fdd1102b146a1c7b2390fc5c4/C3F27956D7399DCA978543C1048F222D?expires=1791331200&signature=31e8f95fb1f0d0227a0dc9c6b9d0c83866b9952cee71435e4465ba8be143de91&req=dSkhFc98m4BfUfMW3nq%2BgZaBOU4ELOcjXWWjrNnKz2niO%2B%2BIpjukgX2gKplR%0AReXcEFE707aS%2B3pq4vAES2OMT%2F8%3D%0A)

![Imagem 3: 6 - Com o pedido integrado, o acompanhamento de rastreio é enviado ao cliente, na forma de régua de rastreio.](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963626128/f9443834577938e6321f8b26abb9/28F4A012A98B23C89221F49387F37659?expires=1791331200&signature=800b7c7289e2d554cdff40a6b8e64d455d602a2955925530c207eef04db9a696&req=dSkhFc98m4BdUfMW3nq%2BgUzRrSrsq8aVq7xBXRmrJaRTm%2FPhf3VwlJAuERij%0AaZwOAelOZrTJ5OtkChFcZcMGVLM%3D%0A)

7 - Quando a transportadora enviar a ocorrência de entregue ao TMS Lincros, a situação do pedido na plataforma VTEX também é alterada para "entregue".

![Imagem 4: 7 - Quando a transportadora enviar a ocorrência de entregue ao TMS Lincros, a situação do pedido na plataforma VTEX…](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963626146/34cff93a8f21bc203c13a3a00e1f/9A8561D65E8EDB7B0EE5B478F680E074?expires=1791331200&signature=99e2d5fd7271516972962ac78413faa9fc0f9a82d76974994b5985b1a2b9dd41&req=dSkhFc98m4BbX%2FMW3nq%2Bgcq%2FNAWPhc80wxI3p3AB7GXEUw3aWA1vYBQv4M9Y%0A9lc92exVkAFdm%2FYpl8IuoBBExE4%3D%0A)
