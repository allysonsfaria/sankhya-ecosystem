---
id: "44011181934103"
titulo: "Como integrar a VTEX com o Magis5 Hub?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011181934103-Como-integrar-a-VTEX-com-o-Magis5-Hub"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T18:57:01Z"
rotulos: ["sync_hc", "magis5", "magis5_204051623044", "sync_hash_e549f5b1e768"]
---

# Como integrar a VTEX com o Magis5 Hub?

## Entenda como integrar a VTEX ao Magis5 Hub, de forma prática e objetiva.

---

### 1) Gerando token API

Tendo já feito seu login na VTEX, acesse **"Configurações da conta" > "Gerenciamento da conta" > "Chaves de aplicação"** pelo menu na lateral esquerda.

![Imagem 1: Tendo já feito seu login na VTEX, acesse "Configurações da conta" > "Gerenciamento da conta" > "Chaves de aplicação"…](https://ajuda.sankhya.com.br/hc/article_attachments/44011165372311)

Na tela que for aberta, clique no botão "**Gerenciar minhas chaves"** localizado no canto superior direito.

![Imagem 2: Na tela que for aberta, clique no botão " Gerenciar minhas chaves" localizado no canto superior direito.](https://ajuda.sankhya.com.br/hc/article_attachments/44011149781655)

Após isso, clique em **"Adicionar"** e defina um nome para a chave no campo **"Rótulo"**.

![Imagem 3: Após isso, clique em "Adicionar" e defina um nome para a chave no campo "Rótulo" .](https://ajuda.sankhya.com.br/hc/article_attachments/44011149982487)

Uma dica é sempre colocar no rótulo o nome do **Magis5 Hub**. Com isso, ficará mais fácil para você identificar o nosso token na hora de integrar ao hub.

Após definir o rótulo, clique em **"Adicionar perfis"** e adicione o perfil **"Owner (Admin Super)".**

![Imagem 4: Após definir o rótulo, clique em "Adicionar perfis" e adicione o perfil "Owner (Admin Super)".](https://ajuda.sankhya.com.br/hc/article_attachments/44011165753623)

**Copie os dados** que foram gerados nos campos **"Token de aplicação" e "Chave de aplicação"** e guarde-os.

![Imagem 5: Copie os dados que foram gerados nos campos "Token de aplicação" e "Chave de aplicação" e guarde-os.](https://ajuda.sankhya.com.br/hc/article_attachments/44011140961047)

Uma dica é abrir um **Bloco de Notas** no seu computador e separar os dados necessários para a integração. Assim, fica mais fácil você se guiar durante o processo!

Ao finalizar, clique em **"Voltar"** no topo da tela, depois no botão **"Visite a loja"** e, por último, **copie a URL da Loja**, que fica no lado direito do topo da VTEX.

![Imagem 6: Ao finalizar, clique em "Voltar" no topo da tela, depois no botão "Visite a loja" e, por último, copie a URL da Loja ,…](https://ajuda.sankhya.com.br/hc/article_attachments/44011153808535)

### 2) Integrando a VTEX ao Magis5 Hub

No Magis5, vá para**"Configurações" > "Integrações"**e clique em **"Lojas Virtuais"**.

![Imagem 7: No Magis5, vá para "Configurações" > "Integrações" e clique em "Lojas Virtuais" .](https://ajuda.sankhya.com.br/hc/article_attachments/44011141091095)

Na tela que será aberta, clique no botão **"Adicionar nova integração"**.

![Imagem 8: Na tela que será aberta, clique no botão "Adicionar nova integração" .](https://ajuda.sankhya.com.br/hc/article_attachments/44011153953943)

Selecione **VTEX** no campo **"Marketplace"** e preencha os seguintes campos conforme demonstrado:

![image-png-Jun-03-2024-05-46-34-2405-PM](https://ajuda.sankhya.com.br/hc/article_attachments/44011182849047)

**Nome da sua loja:** O nome da sua preferência (Ex: Magis5 Store)
**Email/Código da loja:** A ["Chave de aplicação"](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011181934103-Como-integrar-a-VTEX-com-o-Magis5-Hub#chave) que você copiou da Vtex.
**Token de acesso:** O token copiado no item ["Token de Aplicação"](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011181934103-Como-integrar-a-VTEX-com-o-Magis5-Hub#chave) da Vtex.
**Url da Loja:** O link copiado no ["visite a loja"](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011181934103-Como-integrar-a-VTEX-com-o-Magis5-Hub#visite-a-loja) da Vtex.

O campo **"Código da sua loja no ERP"**é necessário para quem utiliza **ERPs externos. Atente-se se este for seu caso!**

O preenchimento deste campo não é nesessário para vendedores que utilizam o faturador do Magis5.

Para o **ERP Bling!**, siga nosso tutorial de [como preencher o campo "Código da sua loja no ERP" utilizando o Bling!](https://ajuda.magis5.com.br/para-que-serve-o-campo-c%C3%B3digo-da-sua-loja-no-erp-e-como-utiliza-lo?hsLang=pt-br)

A seguir, clique em **"Notas fiscais"** e **selecione um ERP** para a emissão de Notas Fiscais, além de ativar as opções **"Gerar Nota Fiscal de forma automática"** e **"Emitir Nota Fiscal de forma automática"**. Verifique também as outras abas e os demais campos, preenchendo-os se necessário.

![image-png-Jun-03-2024-05-50-07-5884-PM](https://ajuda.sankhya.com.br/hc/article_attachments/44011132744343)

É obrigatória a ativação dos campos citados para a integração Vtex.

Finalize clicando em **"Realizar Integração"**.

![Imagem 11: Finalize clicando em "Realizar Integração" .](https://ajuda.sankhya.com.br/hc/article_attachments/44011132799383)

Após isto, sua integração com a Loja Integrada será concluída. Caso encontrar quaisquer problemas, não hesite em [entrar em contato com nosso suporte](https://ajuda.magis5.com.br/como-abrir-um-suporte-por-bate-papo-na-magis5?hsLang=pt-br).
[![Universidade Magis5](https://ajuda.sankhya.com.br/hc/article_attachments/44011154216087)](https://download.magis5.com.br/universidade-magis5?utm_source=central_de_ajuda&utm_medium=link&utm_campaign=central_de_ajuda&hsLang=pt-br)
