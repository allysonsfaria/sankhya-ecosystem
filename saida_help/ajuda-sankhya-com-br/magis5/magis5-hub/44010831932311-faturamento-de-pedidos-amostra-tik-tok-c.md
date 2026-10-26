---
id: "44010831932311"
titulo: "Faturamento de pedidos Amostra Tik Tok com ERP Bling"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010831932311-Faturamento-de-pedidos-Amostra-Tik-Tok-com-ERP-Bling"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T18:47:26Z"
rotulos: ["sync_hc", "magis5", "magis5_208238491262", "sync_hash_2aadb8767556"]
---

# Faturamento de pedidos Amostra Tik Tok com ERP Bling

## Neste tópico vamos explicar como funciona o fluxo de pedidos amostra no Magis5 HUB utilizando o faturamento com ERP Bling

![image-png-Jun-16-2023-06-01-40-2757-PM](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Jun-16-2023-06-01-40-2757-PM.webp?width=77&height=55&name=image-png-Jun-16-2023-06-01-40-2757-PM.webp)![image-png-Jun-16-2023-06-01-59-5101-PM](https://ajuda.sankhya.com.br/hc/article_attachments/44010811146007)![image-png-Jun-16-2023-06-05-56-6355-PM](https://ajuda.sankhya.com.br/hc/article_attachments/44010817233687)![image-png-Jun-16-2023-06-09-13-9401-PM](https://ajuda.sankhya.com.br/hc/article_attachments/44010826381463)![image-png-Jun-16-2023-06-11-05-6975-PM](https://ajuda.sankhya.com.br/hc/article_attachments/44010832338711)![image-png-Jun-16-2023-06-13-01-8880-PM](https://ajuda.sankhya.com.br/hc/article_attachments/44010811490711)![image-png-Jun-16-2023-06-16-56-1170-PM](https://ajuda.sankhya.com.br/hc/article_attachments/44010789397783)

---

⚠️ Para evitar que os pedidos de Amostra Tik Tok fiquem travados em **“Ag. logística”** no Magis5 HUB, **sem definição de transportadora**, é necessário habilitar no [Tik Tok Shop Seller Center](https://seller-br.tiktok.com/account/login), na aba “Envio”, a opção “**Utilizar Enviado pela Plataforma para encomendas sem cobrança?”.**

![image (47)-1](https://ajuda.sankhya.com.br/hc/article_attachments/44010811678487)

Essa configuração garante que os pedidos sejam importados corretamente para o Magis5 HUB e sigam normalmente o **fluxo de faturamento e expedição.**

### Configurando o faturamento de pedido Amostra

Para os pedidos de **Amostra TikTok Shop**, cujo faturamento é realizado pelo ERP Bling, os pedidos serão integrados ao **Magis5 HUB** e não permanecerão mais com o status **“Pendência”**. Eles seguirão normalmente o fluxo de **faturamento e expedição**, assim como os demais canais de venda.

- Os pedidos de **amostra** entrarão com o status **“Ag. Separação”** no **HUB**. Em seguida, serão criados no **ERP Bling**, indicado conforme a configuração de faturamento do canal de venda.

💡 Para que os pedidos do tipo **Amostra** sejam faturados corretamente, é indispensável criar e configurar uma **Natureza de Operação específica** dentro do **Bling ERP**.

Toda a parametrização fiscal, incluindo definição de **CFOP, impostos (ICMS, IPI, PIS, COFINS), regras de destaque, finalidade da operação e demais configurações tributárias,**devem ser realizada **exclusivamente dentro do Bling**.

Em caso de dúvidas para cadastrar uma nova **Natureza de Operação** no **Bling ERP**, acesse o manual na Central de [Ajuda do sistema.](https://ajuda.bling.com.br/hc/pt-br)

Feita a parametrização fiscal para pedido Amostra Tik Tok, é necessário que configure previamente qual **natureza de operação** deverá ser utilizada nesses pedidos.

Para isso, acesse o Magis5 HUB vá até a opção **"Configurações"**,selecione a opção **"Integrações"** e, em seguida, clique em **"ERPs & Faturador".**

![Captura de tela 2026-02-25 130055](https://ajuda.sankhya.com.br/hc/article_attachments/44010811757207)

Na tela, selecione o ERP Bling responsável pelo faturamento dos pedidos Tik Tok e clique em **"Editar".**

![Imagem 10: Feita a parametrização fiscal para pedido Amostra Tik Tok, é necessário que configure previamente qual natureza de…](https://ajuda.sankhya.com.br/hc/article_attachments/44010789717015)

Em "**Dados adicionais"**, você pode definir qual preço será utilizado na emissão das Notas Fiscais dos pedidos **Amostra TikTok**. Basta selecionar a opção desejada:

- **Preço de Custo**
- **Preço de Venda**

![Captura de tela 2026-02-27 105957](https://ajuda.sankhya.com.br/hc/article_attachments/44010805698455)

⚠️ **Ação necessária:**

Ainda em **"Dados Adicionais"** é necessário preencher com o **"ID da Natureza de Operação de Amostras"** (código fiscal utilizado exclusivamente para operações de amostras).

![Captura de tela 2026-02-27 133620](https://ajuda.sankhya.com.br/hc/article_attachments/44010827229463)

Para preencher esse campo, é necessário acessar novamente o **ERP Bling**, localizar a **Natureza de Operação** previamente cadastrada, editá-la e copiar o código identificador exibido na URL da página.

![Imagem 13: Ainda em "Dados Adicionais" é necessário preencher com o "ID da Natureza de Operação de Amostras" (código fiscal…](https://ajuda.sankhya.com.br/hc/article_attachments/44010812113687)

**Caso nenhum código de natureza de operação seja informado, o sistema irá continuar utilizando o fluxo padrão atual.**
