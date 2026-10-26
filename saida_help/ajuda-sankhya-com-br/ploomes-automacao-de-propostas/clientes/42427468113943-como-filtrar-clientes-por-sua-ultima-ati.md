---
id: "42427468113943"
titulo: "Como filtrar clientes por sua última atividade?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427468113943-Como-filtrar-clientes-por-sua-%C3%BAltima-atividade"
trilha: "PLOOMES: Automação de propostas  > Clientes"
atualizado_em: "2026-08-11T16:14:51Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452145", "sync_hash_7ad99c071ae5"]
---

# Como filtrar clientes por sua última atividade?

Na tela de **Clientes**, é possível configurar uma aba para filtrar registros com base na última atividade, como **última venda**, **último contato** ou **último negócio**. Dessa forma, você passa a ter maior controle sobre sua base de clientes.

## Como configurar?

Acesse a tela de **Clientes**. Como primeiro exemplo, vamos configurar uma aba para buscar **Empresas** que realizaram compras nos últimos 6 meses, utilizando o campo **Última venda**.

## Primeiro exemplo:

- Clique em **Nova aba**;
- Defina o **título da aba** e escolha quem poderá visualizá-la;
- Como filtro, adicione:

  - **Cliente > Tipo > Igual a > Empresa**;
- Adicione outro filtro:

  - **Cliente > Última venda > Data > Igual a > Data Relativa > Últimos N meses > 6**;
- Clique em **Criar aba**.

[GIF animado: primeiro exemplo](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2052697891/9949c7732289a4ba4c2566ef3f3f/primeiraAba.gif?expires=1786536000&signature=d38943fe4d681ddfd136deebfb262660a2e8958f74c829074defed67158ee403&req=diAiFM93molWWPMW3nq%2BgfNw1j9vcR%2Fh8EduEsa3f8LEBiNaMkX2ubYMD%2F2B%0AB%2FFhJOQYOuQaKhV3A0mgL4jisJU%3D%0A)

Você também pode configurar uma aba para identificar **Empresas que não compraram nos últimos 6 meses**. Para isso, utilize a mesma configuração anterior e altere apenas o operador do filtro de data:

- **Cliente > Última venda > Data > Diferente de > Data Relativa > Últimos N meses > 6**

[GIF animado: segundo exemplo](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2052855723/88a40081a3512a785d2135944555/segundaAba.gif?expires=1786536000&signature=e23d51c6b3da68b2d0c8fbdfa78129e80945d984ed182afa71b42f5c0d9d4f7c&req=diAiFMF7mIZdWvMW3nq%2BgZLYNstp6R0qWW61PakfunLs0JCe3gy4AoNhR6Es%0ATon0WH0JcH5hpbr2o%2B1T4aKYC0E%3D%0A)

Como segundo exemplo, vamos configurar uma aba para buscar **Empresas que não possuem contato neste ano**, utilizando o campo **Último contato**.

## Segundo exemplo:

- Clique em **Nova aba**;
- Defina o **título da aba** e escolha quem poderá visualizá-la;
- Como filtro, adicione:

  - **Cliente > Tipo > Igual a > Empresa**;
- Adicione outro filtro:

  - **Cliente > Último contato > Data > Diferente de > Data Relativa > Este ano;**
- Clique em **Criar aba**.

[GIF animado: terceiro exemplo](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2052877183/d35234d001f0ab3570172f316d30/terceiraAba.gif?expires=1786536000&signature=fd204c850b553a415f1c7b89a3c4244edc92816d9410abd686281e2b77396ce6&req=diAiFMF5moBXWvMW3nq%2BgcUa8xYwMxThQmNVSDefhYJq2UtHMluf3YgtHgL%2B%0Ai04wIuEGwqy2WmufpQhhCgk3DTM%3D%0A)

Como terceiro exemplo, vamos configurar uma aba para buscar **Contatos que negociaram neste ano**, utilizando o campo **Último negócio**.

## Terceiro exemplo:

- Clique em **Nova aba**;
- Defina o **título da aba** e escolha quem poderá visualizá-la;
- Como filtro, adicione:

  - **Cliente > Tipo > Igual a > Pessoa**;
- Adicione outro filtro:

  - **Cliente > Último negócio > Data de criação > Igual a > Data Relativa > Este ano;**
- Clique em **Criar aba**.

[GIF animado: quarto exemplo](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2052894542/8e80ffb31c810e20ad02e98cdda9/quartaAba.gif?expires=1786536000&signature=f0e9425e1b0e34250da71bb16901fa192326a17bfd8522fdff6eb0bad9f34427&req=diAiFMF3mYRbW%2FMW3nq%2BgbhI0shAvbRy919bpL7fEHqnNwoUyAA86%2FaOnqi%2F%0ACKnCfQ9MyzzdCyQlRujC%2FRaYJ7c%3D%0A)

Veja também:

[Diferença entre o filtro "Data" e "Data relativa"](https://sankhya.zendesk.com/hc/pt-br/articles/42427574409751)

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
