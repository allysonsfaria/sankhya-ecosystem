---
id: "44010341155479"
titulo: "Entendendo as Regras de Crossdocking para Anúncio e Produto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010341155479-Entendendo-as-Regras-de-Crossdocking-para-An%C3%BAncio-e-Produto"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T18:36:14Z"
rotulos: ["sync_hc", "magis5", "magis5_215439169094", "sync_hash_332abc0b667e"]
---

# Entendendo as Regras de Crossdocking para Anúncio e Produto

## Saiba como funciona o Crossdocking para a Shopee e Mercado Livre e confira as regras para gestão de anúncios e produtos no Magis5 HUB

---

💡 O **Crossdocking (prazo de fabricação)** corresponde ao período necessário para produzir, separar ou disponibilizar o produto para envio após confirmação da venda.
Esse prazo indica quantos dias você precisa para preparar o produto antes que ele seja efetivamente despachado ao cliente.

- O envio dos prazos e valores de Crossdocking para os canais de venda segue lógicas específicas que dependem da disponibilidade de estoque do item e de onde a configuração de prazo foi preenchida (no cadastro do Produto ou no Fornecedor).

Confira abaixo as regras de funcionamento do sistema relacionadas à aplicação do Crossdocking 

### Cenários com Estoque

 Quando o produto possui estoque disponível, o sistema considera exclusivamente as configurações definidas no próprio produto

- **Campo preenchido no Produto:** O sistema utiliza o valor configurado diretamente no Produto.
- **Campo não preenchido no Produto:** O sistema enviará o valor **0** para o marketplace.

![Imagem 1: Campo não preenchido no Produto: O sistema enviará o valor 0 para o marketplace.](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Jun-19-2026-08-38-57-1073-PM.png?width=670&height=189&name=image-png-Jun-19-2026-08-38-57-1073-PM.png)

### Cenários sem Estoque

 Quando o produto **não possui estoque**, o sistema busca primeiro a configuração definida no produto e, caso não a encontre, utiliza a configuração do fornecedor

- **Campo preenchido no Produto:** O sistema utiliza o valor configurado no Produto. Qualquer valor que esteja no **Fornecedor** será ignorado.
- **Campo não preenchido no Produto, mas preenchido no Fornecedor:** O sistema utiliza o valor configurado no **Fornecedor**
- **Campo não preenchido em nenhum dos dois:** Se o prazo não estiver nem no Produto e nem no **Fornecedor**, o sistema enviará o valor **0**

![Imagem 2: Campo não preenchido em nenhum dos dois: Se o prazo não estiver nem no Produto e nem no Fornecedor , o sistema enviará…](https://ajuda.sankhya.com.br/hc/article_attachments/44010341412247)

⚠️ **Exceções Importantes:**

As regras de prazo descritas acima não se aplicam a anúncios que exigem entregas rápidas. Para os seguintes tipos de anúncio, o sistema sempre enviará o valor **0** de **CrossDocking**, independentemente das configurações de cadastro.

- Full
- Flex
- Turbo

💡**Funcionalidades disponíveis atualmente apenas para os canais de venda** **Mercado Livre e Shopee.**
