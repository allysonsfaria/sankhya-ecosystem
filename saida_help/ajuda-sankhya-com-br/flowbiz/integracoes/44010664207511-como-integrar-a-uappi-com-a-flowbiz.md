---
id: "44010664207511"
titulo: "Como integrar a Uappi com a Flowbiz"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010664207511-Como-integrar-a-Uappi-com-a-Flowbiz"
trilha: "Flowbiz > Integrações"
atualizado_em: "2026-10-05T18:43:13Z"
rotulos: ["sync_hc", "flowbiz", "flowbiz_112", "sync_hash_b0accab5e5a7"]
---

# Como integrar a Uappi com a Flowbiz

Para integrar a **Uappi** com a **Flowbiz**, vamos precisar de alguns dados importantes e fazer **algumas configurações.**
Para acessar as configurações de API na plataforma **Uappi**, siga este caminho:

- **Configurações > Pesquise por “Integrações > Procure por “API”**.

![Imagem 1: Configurações > Pesquise por “Integrações > Procure por “API” .](https://ajuda.sankhya.com.br/hc/article_attachments/44010645078295)

Nessa seção, você verá os tokens já criados, podendo **desativá-los, editá-los ou excluí-los.**

Para adicionar uma nova integração, clique em **“Nova integração”**, insira o nome desejado e clique em **“Enviar”**. A nova integração será listada automaticamente, e o token será gerado pelo sistema.

![Imagem 2: Para adicionar uma nova integração, clique em “Nova integração” , insira o nome desejado e clique em “Enviar” . A nova…](https://ajuda.sankhya.com.br/hc/article_attachments/44010637952023)

## Métodos necessários:

`GET customers/queue`

`DELETE customers/queue`

`DELETE customers/queue/{idCodigoCliente}`

`GET customers/{idCodigoCliente}`

![Imagem 3: GET customers/{idCodigoCliente}](https://ajuda.sankhya.com.br/hc/article_attachments/44010638227607)

Caso tenha nosso módulo **avançado de CRM ativo**, crie outro **token**, e insira os seguintes métodos:

`GET customers/queue`
`DELETE customers/queue`
`DELETE customers/queue/{idCodigoCliente}`
`GET customers/{idCodigoCliente}`
`GET -> products`
`GET → products/{idSkuProduto}`
`GET -> categories`
`GET → categories/{idCategoria}`
`GET -> brands`
`GET -> orders`

![Imagem 4: GET customers/queue DELETE customers/queue DELETE customers/queue/{idCodigoCliente} GET customers/{idCodigoCliente} GET…](https://ajuda.sankhya.com.br/hc/article_attachments/44010676161047)

Pronto! Sua chave **API** foi criada automaticamente.

Basta encaminhar ao time de suporte técnico, pelo e-mail: [tokens@flowbiz.com.br](mailto:tokens@flowbiz.com.br)

Em caso de dúvidas, não hesite em nos acionar no chat da ferramenta!
