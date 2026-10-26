---
id: "44011651508119"
titulo: "Como conferir se a sincronização do meu estoque entre o Bling e o Magis5 Hub está ativa ?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011651508119-Como-conferir-se-a-sincroniza%C3%A7%C3%A3o-do-meu-estoque-entre-o-Bling-e-o-Magis5-Hub-est%C3%A1-ativa"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T19:08:09Z"
rotulos: ["sync_hc", "magis5", "magis5_204055206968", "sync_hash_fe1510e83ee7"]
---

# Como conferir se a sincronização do meu estoque entre o Bling e o Magis5 Hub está ativa ?

## A configuração do callback é a responsável pela sincronização do seu estoque do Bing para o Magis5 Hub.

---

⚠️ Antes de seguir este guia, verifique se você já preencheu o campo **"código da sua loja no ERP"** dentro da integração de seu marketplace no Magis5 Hub Hub. Entenda como fazer isto [clicando aqui](https://sankhya.zendesk.com/hc/pt-br/articles/44011376979607).

Se você usa a Magis5 Hub junto com o Bling! ERP e quer ativar ou verificar a comunicação de estoque com o Bling!, siga os seguintes passos.

### 1) Encontrando a URL de callback

Acesse sua conta Magis5 Hub, leve o mouse até **"Configurações"**, depois **"Integrações"** e por último clique em **"Marketplaces".**

![Imagem 1: Acesse sua conta Magis5 Hub, leve o mouse até "Configurações" , depois "Integrações" e por último clique em…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Jan-18-2024-12-47-01-9846-PM.png?width=618&height=470&name=image-png-Jan-18-2024-12-47-01-9846-PM.png)

Na lista exibida, encontre a integração de marketplace na qual você controla o estoque pelo Bling!. Clique no botão "Editar" localizado no lado direito do bloco desta integração.

![Imagem 2: Na lista exibida, encontre a integração de marketplace na qual você controla o estoque pelo Bling!. Clique no botão…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Jan-18-2024-12-53-57-6029-PM.png?width=606&height=141&name=image-png-Jan-18-2024-12-53-57-6029-PM.png)

Lembre-se que esta integração deverá ter Status Ativo. Se sua integração está com token expirado, entenda como reativar seu token [clicando aqui.](https://sankhya.zendesk.com/hc/pt-br/articles/44011179364503)

Com a tela de edição aberta, clique no bloco de instruções para sincronizar seu ERP.

![Imagem 3: Com a tela de edição aberta, clique no bloco de instruções para sincronizar seu ERP.](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Jan-18-2024-12-56-39-2933-PM.png?width=688&height=54&name=image-png-Jan-18-2024-12-56-39-2933-PM.png)

No texto exibido, encontre a URL exibida abaixo de "URL de callback para alterações de estoque". **Cada integração possui uma URL própria** com uma série de números diferente. **Copie** esta URL e, se necessário, guarde-a em um bloco de notas, pois iremos utilizá-la no próximo passo.

![Imagem 4: No texto exibido, encontre a URL exibida abaixo de "URL de callback para alterações de estoque". Cada integração possui…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Jan-18-2024-01-00-27-0756-PM.png?width=579&height=77&name=image-png-Jan-18-2024-01-00-27-0756-PM.png)

---

### 2) Ativando o callback

Acesse o Bling!, vá até o **ícone da engrenagem ![Imagem 5: Acesse o Bling!, vá até o ícone da engrenagem localizado na parte de cima da tela e clique em "Configurações de…](https://ajuda.bling.com.br/hc/article_attachments/360066638134/cog.png)** localizado na parte de cima da tela e clique em **"Configurações de integração"**.

![1.1-1](https://ajuda.magis5.com.br/hs-fs/hubfs/1.1-1.png?width=669&height=310&name=1.1-1.png)

Encontre a opção de integração e clique nela.

![2.2](https://ajuda.magis5.com.br/hs-fs/hubfs/2.2.png?width=688&height=304&name=2.2.png)

Na página que foi aberta, clique em **"Configurações de integração com lojas virtuais e marletplaces"**.

![3.3](https://ajuda.magis5.com.br/hs-fs/hubfs/3.3.png?width=675&height=299&name=3.3.png)

Agora selecione "**Minhas Instalações".**

![4.4](https://ajuda.magis5.com.br/hs-fs/hubfs/4.4.png?width=688&height=314&name=4.4.png)

**Atenção ao preenchimento correto da URL!** Se você copiou a URL do **Mercado Livre**, ela deve ser inserida na integração do **Mercado Livre no Bling!**. O mesmo vale para Shopee, Amazon e outros marketplaces.

![5.5](https://ajuda.magis5.com.br/hs-fs/hubfs/5.5.png?width=688&height=311&name=5.5.png)

Agora, siga os seguintes passos:

1. Verifique se a opção **JSON (urlencoded)** está selecionada como tipo de retorno.
2. Se a opção de **Callback de estoque** estiver desativada, **ative-a**.
3. Na caixa de texto exibida **abaixo** da opção de Callback de estoque, **cole e insira a URL que guardamos.**

A configuração deve ser mostrada conforme a imagem abaixo. **Quando tudo estiver pronto**, clique em **"Salvar"**.

![Imagem 11: A configuração deve ser mostrada conforme a imagem abaixo. Quando tudo estiver pronto , clique em "Salvar" .](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Jan-18-2024-01-12-09-0407-PM.png?width=685&height=464&name=image-png-Jan-18-2024-01-12-09-0407-PM.png)

Caso você encontrar quaisquer problemas com integrações ou sincronia de estoque com o Bling!, não hesite em [entrar em contato com nosso suporte.](https://ajuda.magis5.com.br/como-abrir-um-suporte-por-bate-papo-na-magis5?hsLang=pt-br)
