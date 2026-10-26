---
id: "44010258579351"
titulo: "Faturamento de pedidos Amostra Tik Tok com ERP Sankhya"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010258579351-Faturamento-de-pedidos-Amostra-Tik-Tok-com-ERP-Sankhya"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T18:33:39Z"
rotulos: ["sync_hc", "magis5", "magis5_209142102928", "sync_hash_839a8682d2c1"]
---

# Faturamento de pedidos Amostra Tik Tok com ERP Sankhya

## Neste tópico vamos explicar como funciona o fluxo de pedidos amostra no Magis5 HUB utilizando o faturamento com ERP Sankhya.

---

⚠️ Para evitar que os pedidos de Amostra Tik Tok fiquem travados em **“Ag. logística”** no Magis5 HUB, **sem definição de transportadora**, é necessário habilitar no [Tik Tok Shop Seller Center](https://seller-br.tiktok.com/account/login), na aba “Envio”, a opção “**Utilizar Enviado pela Plataforma para encomendas sem cobrança?”.**

![image (47)-1](https://ajuda.sankhya.com.br/hc/article_attachments/44010258733975)

Essa configuração garante que os pedidos sejam importados corretamente para o Magis5 HUB e sigam normalmente o **fluxo de faturamento e expedição.**

### Configurando o faturamento de pedido Amostra

Para os pedidos de **Amostra Tik Tok Shop**, cujo faturamento é realizado pelo ERP Sankhya, os pedidos serão integrados ao **Magis5 HUB** e não permanecerão mais com o status **“Pendência”**. Eles seguirão normalmente o fluxo de **faturamento e expedição**, assim como os demais canais de venda.

- Os pedidos de **amostra** entrarão com o status **“Ag. Separação”** no **HUB**. Em seguida, serão criados no **ERP Sankhya**, indicado conforme a configuração de faturamento do canal de venda.

💡 Para que os pedidos do tipo **Amostra** sejam faturados corretamente, é indispensável criar e configurar uma **Natureza de Operação específica** dentro do **Sankhya ERP**.

Toda a parametrização fiscal, incluindo definição de **CFOP, impostos (ICMS, IPI, PIS, COFINS), regras de destaque, finalidade da operação e demais configurações tributárias,**devem ser realizada **exclusivamente dentro do Sankhya**.

Feita a parametrização fiscal para pedido Amostra Tik Tok, é necessário que configure previamente qual **natureza de operação** deverá ser utilizada nesses pedidos.

Para isso, acesse o Magis5 HUB vá até a opção **"Configurações"**, selecione a opção **"Integrações"**e, em seguida, clique em **"ERPs & Faturador".**

![Captura de tela 2026-02-25 130055](https://ajuda.sankhya.com.br/hc/article_attachments/44010264751511)

Na tela, selecione o ERP Sankhya responsável pelo faturamento dos pedidos Tik Tok e clique em**"Editar"**.

![Captura de tela 2026-03-12 110425](https://ajuda.sankhya.com.br/hc/article_attachments/44010275293207)

Em "**Dados adicionais"**, você pode definir qual preço será utilizado na emissão das Notas Fiscais dos pedidos **Amostra TikTok**. Basta selecionar a opção desejada:

- **Preço de Custo**
- **Preço de Venda**

![Captura de tela 2026-02-27 105957](https://ajuda.sankhya.com.br/hc/article_attachments/44010275437335)

⚠️ **Ação necessária:**

Ainda em **"Dados Adicionais"**é necessário preencher com o**"ID da Natureza de Operação de Amostras"** (código fiscal utilizado exclusivamente para operações de amostras).

![Captura de tela 2026-02-27 133620](https://ajuda.sankhya.com.br/hc/article_attachments/44010275541143)

Para preencher esse campo, é necessário acessar novamente o **ERP Sankhya,** a criação de uma **Natureza de Operação** é realizada por meio do **TOP (Tipo de Operação)**, que é definido e configurado pelo próprio usuário dentro do sistema. acesse o manual na Central de [Ajuda do sistema.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#:~:text=Na%20TOP%2C%20s%C3%A3o%20definidos%20os,as%20novas%20configura%C3%A7%C3%B5es%20sejam%20validadas.)

![Captura de tela 2026-03-12 111519](https://ajuda.sankhya.com.br/hc/article_attachments/44010259360023)

**Caso nenhum código de natureza de operação seja informado, o sistema irá continuar utilizando o fluxo padrão atual.**
