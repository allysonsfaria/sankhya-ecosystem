---
id: "44010780393239"
titulo: "Faturamento de pedidos Amostra Tik Tok com ERP Omie"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010780393239-Faturamento-de-pedidos-Amostra-Tik-Tok-com-ERP-Omie"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T18:47:11Z"
rotulos: ["sync_hc", "magis5", "sync_hash_15d6f9fdab70", "magis5_209179531363"]
---

# Faturamento de pedidos Amostra Tik Tok com ERP Omie

## Neste tópico vamos explicar como funciona o fluxo de pedidos amostra no Magis5 HUB utilizando o faturamento com ERP Omie.

---

⚠️ Para evitar que os pedidos de Amostra Tik Tok fiquem travados em **“Ag. logística”** no Magis5 HUB, **sem definição de transportadora**, é necessário habilitar no [Tik Tok Shop Seller Center](https://seller-br.tiktok.com/account/login), na aba “Envio”, a opção “**Utilizar Enviado pela Plataforma para encomendas sem cobrança?”.**

![image (47)-1](https://ajuda.sankhya.com.br/hc/article_attachments/44010787627159)

Essa configuração garante que os pedidos sejam importados corretamente para o Magis5 HUB e sigam normalmente o **fluxo de faturamento e expedição.**

### Configurando o faturamento de pedido Amostra

Para os pedidos de **Amostra Tik Tok Shop**, cujo faturamento é realizado pelo ERP Omie, os pedidos serão integrados ao **Magis5 HUB** e não permanecerão mais com o status **“Pendência”**. Eles seguirão normalmente o fluxo de **faturamento e expedição**, assim como os demais canais de venda.

- Os pedidos de **amostra** entrarão com o status **“Ag. Separação”** no **HUB**. Em seguida, serão criados no **ERP Omie**, indicado conforme a configuração de faturamento do canal de venda.

💡 Para que os pedidos do tipo **Amostra** sejam faturados corretamente, é indispensável criar e configurar uma **Natureza de Operação específica** dentro do **Omie ERP**.

Toda a parametrização fiscal, incluindo definição de **CFOP, impostos (ICMS, IPI, PIS, COFINS), regras de destaque, finalidade da operação e demais configurações tributárias,**devem ser realizada **exclusivamente dentro do Omie**.

Feita a parametrização fiscal para pedido Amostra Tik Tok, é necessário que configure previamente qual **natureza de operação** deverá ser utilizada nesses pedidos.

Para isso, acesse o Magis5 HUB vá até a opção **"Configurações"**, selecione a opção **"Integrações"**e, em seguida, clique em **"ERPs & Faturador".**

![Captura de tela 2026-02-25 130055](https://ajuda.sankhya.com.br/hc/article_attachments/44010780590487)

Na tela, selecione o ERP Omie responsável pelo faturamento dos pedidos Tik Tok e clique em**"Editar"**.

![Captura de tela 2026-03-12 113524](https://ajuda.sankhya.com.br/hc/article_attachments/44010803674007)

Em "**Dados adicionais"**, você pode definir qual preço será utilizado na emissão das Notas Fiscais dos pedidos **Amostra TikTok**. Basta selecionar a opção desejada:

- **Preço de Custo**
- **Preço de Venda**

![Captura de tela 2026-02-27 105957](https://ajuda.sankhya.com.br/hc/article_attachments/44010810206103)

⚠️ **Ação necessária:**

Ainda em **"Dados Adicionais"**é necessário preencher com o**"ID da Natureza de Operação de Amostras"** (código fiscal utilizado exclusivamente para operações de amostras).

![Captura de tela 2026-02-27 133620](https://ajuda.sankhya.com.br/hc/article_attachments/44010825205911)

Para localizar o ID, acesse o [**Portal do Desenvolvedor Omie**](https://developer.omie.com.br/) vá em **Lista das APIs** > **Compras, Estoque e Produção** > **Cadastros Auxiliares** > **Cenário de Impostos**

![Imagem 6: Para localizar o ID, acesse o Portal do Desenvolvedor Omie vá em Lista das APIs > Compras, Estoque e Produção >…](https://ajuda.sankhya.com.br/hc/article_attachments/44010788139031)

![Imagem 7: Para localizar o ID, acesse o Portal do Desenvolvedor Omie vá em Lista das APIs > Compras, Estoque e Produção >…](https://ajuda.sankhya.com.br/hc/article_attachments/44010810472343)

Em **Cenários de Impostos** clique em **“Teste agora mesmo”** no método **ListarCenarios** e execute a requisição.

![Imagem 8: Em Cenários de Impostos clique em “Teste agora mesmo” no método ListarCenarios e execute a requisição.](https://ajuda.sankhya.com.br/hc/article_attachments/44010825526935)

No resultado (**Response**), localize o cenário desejado pelo campo **cNome** e copie o valor do campo **nCodigo**, que corresponde ao ID do cenário e cole na opção **"ID da Natureza de Operação de Amostras"**

**Caso nenhum código de natureza de operação seja informado, o sistema irá continuar utilizando o fluxo padrão atual.**
