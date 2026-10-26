---
id: "44010314401047"
titulo: "Como integrar a Shopify com a Flowbiz."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010314401047-Como-integrar-a-Shopify-com-a-Flowbiz"
trilha: "Flowbiz > Integrações"
atualizado_em: "2026-10-05T18:34:59Z"
rotulos: ["sync_hc", "flowbiz", "flowbiz_96", "sync_hash_495bedf35e1e"]
---

# Como integrar a Shopify com a Flowbiz.

Para realizar a integração da Shopify V3, precisamos de alguns dados importantes.
É necessário **gerar as credenciais** do aplicativo no **Dev Dashboard da Shopify** e **liberar** os **escopos necessários da API.**

Para conseguir essas informações você pode seguir este passo a passo, dentro do seu painel da **Shopify**:

**1.** No painel inicial, no menu esquerdo, clique sobre **Apps** e em seguida, clique em **Desenvolver apps** **para sua loja**.

![Imagem 1: 2. Agora, clique em Desenvolver apps no Dev Dashboard](https://ajuda.sankhya.com.br/hc/article_attachments/44010281463191)**2.** Agora, **clique em Desenvolver apps no Dev Dashboard**

![Imagem 2: Será aberta uma nova aba com acesso ao Dev Dashboard da Shopify.](https://ajuda.sankhya.com.br/hc/article_attachments/44010330643735)Será aberta uma nova aba com acesso ao Dev Dashboard da Shopify.

**3.** Na sequência, no canto superior direito clique em **Create App**, ou em **Criar um aplicativo**:

![Imagem 3: 4. Dê um nome para seu aplicativo, exemplo: Flowbiz.](https://ajuda.sankhya.com.br/hc/article_attachments/44010315135639)**4.** Dê um nome para seu aplicativo, exemplo: Flowbiz.

Em seguida, clique em **criar aplicativo**.

![Imagem 4: 5. Após criar o aplicativo, na mesma tela de configuração. Entre na seção Acesso > Escopos e clique em Selecionar…](https://ajuda.sankhya.com.br/hc/article_attachments/44010331091607)**5.** Após criar o aplicativo, na mesma tela de configuração. Entre na seção **Acesso > Escopos e** clique em **Selecionar escopos.**

![Imagem 5: 6. Marque os seguintes escopos:](https://ajuda.sankhya.com.br/hc/article_attachments/44010315660567)**6.** **Marque** os seguintes **escopos:**

- ## ✅ Ler todos os Pedidos (read\_all\_orders)
- ## ✅ Ler Pedidos (read\_orders)
- ## ✅ Ler Clientes (read\_customers)
- ## ✅ Ler Produtos (read\_products)

![Imagem 6: ✅ Ler Produtos (read_products)](https://ajuda.sankhya.com.br/hc/article_attachments/44010315880471)![Imagem 7: ✅ Ler Produtos (read_products)](https://ajuda.sankhya.com.br/hc/article_attachments/44010316136087)![Imagem 8: ✅ Ler Produtos (read_products)](https://ajuda.sankhya.com.br/hc/article_attachments/44010316307479)![Imagem 9: ✅ Ler Produtos (read_products)](https://ajuda.sankhya.com.br/hc/article_attachments/44010332407703)![Imagem 10: ✅ Ler Produtos (read_products)](https://ajuda.sankhya.com.br/hc/article_attachments/44010283217431)

**⚠ IMPORTANTE:
Habilite apenas esses quatro escopos.** Não é necessário conceder permissões adicionais.

**7.** Confirme a seleção.

**8.** Clique em Concluir.

## As demais configurações e escopos podem permanecer como padrão.

**9.** Após configurar os escopos:

- Role até o final da tela.
- **Clique em Lançar** (Release)**.**

![Imagem 11: 10. No menu lateral esquerdo , clique em Configurações (Settings).](https://ajuda.sankhya.com.br/hc/article_attachments/44010283439895)**10.** No menu lateral esquerdo**, clique em Configurações (Settings).**

## Copie as seguintes credenciais geradas para enviar ao time de suporte:

- ## Client ID
- ## Secret Key

![Imagem 12: Secret Key](https://ajuda.sankhya.com.br/hc/article_attachments/44010317147415)

**11.** Agora, iremos Instalar o Aplicativo

- Acesse novamente o menu Aplicativos.
- Abra o aplicativo criado para a Flowbiz.
- Clique em Instalar App.
- Confirme a instalação

![Imagem 13: E por fim, basta copiar a chave "Client ID" e "Client Secret" e enviar ao time de suporte técnico , pelo e-mail:…](https://ajuda.sankhya.com.br/hc/article_attachments/44010333320087)![Imagem 14: E por fim, basta copiar a chave "Client ID" e "Client Secret" e enviar ao time de suporte técnico , pelo e-mail:…](https://ajuda.sankhya.com.br/hc/article_attachments/44010317438871)E por fim, basta copiar a chave "Client ID" e "Client Secret" e **enviar ao time de suporte técnico**, pelo e-mail: [tokens@flowbiz.com.br](mailto:tokens@flowbiz.com.br)

Após o envio das credenciais, o time técnico dará continuidade ao processo de integração.
