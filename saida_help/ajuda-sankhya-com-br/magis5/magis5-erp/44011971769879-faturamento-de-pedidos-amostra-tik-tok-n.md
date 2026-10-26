---
id: "44011971769879"
titulo: "Faturamento de pedidos Amostra Tik Tok no Magis5 ERP"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011971769879-Faturamento-de-pedidos-Amostra-Tik-Tok-no-Magis5-ERP"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:16:29Z"
rotulos: ["sync_hc", "magis5", "sync_hash_8726f079c49c", "magis5_204516592231"]
---

# Faturamento de pedidos Amostra Tik Tok no Magis5 ERP

## Neste tópico vamos explicar como funciona o fluxo de pedidos amostra no Magis5 HUB utilizando o faturamento com o Magis5 ERP

---

⚠️ Para evitar que os pedidos de Amostra Tik Tok fiquem travados em **“Ag. logística”** no Magis5 HUB, **sem definição de transportadora**, é necessário habilitar no [Tik Tok Shop Seller Center](https://seller-br.tiktok.com/account/login), na aba “Envio”, a opção “**Utilizar Enviado pela Plataforma para encomendas sem cobrança?”.**

![image (47)-1](https://ajuda.sankhya.com.br/hc/article_attachments/44011979926167)

Essa configuração garante que os pedidos sejam importados corretamente para o Magis5 HUB e sigam normalmente o **fluxo de faturamento e expedição.**

### Configurando o faturamento de pedido Amostra

Para os pedidos de **Amostra Tik Tok Shop**, cujo faturamento é realizado diretamente em nosso **ERP**, os pedidos serão integrados ao **Magis5 HUB** e não permanecerão mais com o status **“Pendência”**. Eles seguirão normalmente o fluxo de **faturamento e expedição**, assim como os demais canais de venda.

- Os pedidos de **amostra** entrarão com o status **“Ag. Separação”** no **HUB**. Em seguida, serão criados no **Magis5 ERP**, no empreendimento indicado conforme a configuração de faturamento do canal de venda.

  Após a criação no ERP, o sistema identificará automaticamente se o cliente é de **fora do estado** e se é **contribuinte ou não**, aplicando o **CFOP** configurado para pedidos de amostra.

Para cadastrar um novo **CFOP** (operação) para **“Amostra”** ou **“Brinde”**, acesse o ERP e navegue até **"Configurações"**, **"NF-e - Operações"**.

![Imagem 2: Para cadastrar um novo CFOP (operação) para “Amostra” ou “Brinde” , acesse o ERP e navegue até "Configurações" , "NF-e…](https://ajuda.sankhya.com.br/hc/article_attachments/44011993766807)

Na tela de **Operações**, clique em **“Nova Operação”**, informe a descrição da operação e selecione o **CFOP** correspondente.
⚠️ Recomendamos que esse ajuste seja realizado com o acompanhamento da sua **contabilidade**.

(Caso já exista uma operação cadastrada para esse tipo de venda, não é necessário realizar um novo cadastro).

![Imagem 3: (Caso já exista uma operação cadastrada para esse tipo de venda, não é necessário realizar um novo cadastro).](https://ajuda.sankhya.com.br/hc/article_attachments/44011993888663)

![Imagem 4: (Caso já exista uma operação cadastrada para esse tipo de venda, não é necessário realizar um novo cadastro).](https://ajuda.sankhya.com.br/hc/article_attachments/44011963863703)

No fim da tela terá opção **"Operação de Bonificação em caso de venda bonificada"** onde é possível selecionar:

- **"Manter valores do pedido"**
- **"Exibir preço de custo do pedido"**
- **"Zerar valores da nota"**

Finalizado a configuração da operação clique em **"Salvar".**

![Imagem 5: Após criar a operação, finalize a configuração acessando o menu "Configurações" , "Configurações Gerais" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/44011994073751)

Após criar a operação, finalize a configuração acessando o menu **"Configurações"**, **"Configurações Gerais"**, **"Integrações"** e por fim **"Magis5**". Role a página até a seção **"Configurações para pedidos de amostra"**e vincule as operações criadas de acordo com cada determinação fiscal.

![Imagem 6: Após criar a operação, finalize a configuração acessando o menu "Configurações" , "Configurações Gerais" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/44011972429207)
![Imagem 7: Após criar a operação, finalize a configuração acessando o menu "Configurações" , "Configurações Gerais" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/44011980650135)

![Imagem 8: Após criar a operação, finalize a configuração acessando o menu "Configurações" , "Configurações Gerais" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/44011994450967)

Em **"Mensagem para Observações da NF-e (Pedidos de Amostra)"** digite a mensagem que será inserida nas observações da nota fiscal para pedidos de amostra e salve os ajustes.

É necessário também configurar um filtro dentro da **Regra Fiscal**. Esse filtro servirá para determinar os parâmetros e as diretrizes tributárias que o **CFOP** selecionado deverá seguir.

Para isso acesse **"Configurações"**, **"NF-e - Regras de tributo v2"** edite a Regra Fiscal

![Imagem 9: Em "Mensagem para Observações da NF-e (Pedidos de Amostra)" digite a mensagem que será inserida nas observações da nota…](https://ajuda.sankhya.com.br/hc/article_attachments/44011994561559)
Você poderá criar um novo filtro para essa operação, ou incluí-la em um já existente.
⚠️ **Indicamos que esse ajuste seja realizado com o acompanhamento da sua contabilidade.**

![Imagem 10: Em "Mensagem para Observações da NF-e (Pedidos de Amostra)" digite a mensagem que será inserida nas observações da nota…](https://ajuda.sankhya.com.br/hc/article_attachments/44011984365847)

Pronto! O sistema utilizará essa Operação e Filtro para emissão da NF-e considerando:

- Regra de valor (venda, custo ou zero).
- CFOP específico.
- Mensagem fiscal padrão.

Caso essas configurações não tiverem sido feitas, os pedidos de amostra cairão no Magis5 ERP com o **erro de faturamento**:

**" Operação Fiscal de bonificação não configurada para pedidos de amostra (Não Contribuinte Fora do Estado). Configure a operação nas configurações do empreendimento."**

![Captura de tela 2026-01-08 134418](https://ajuda.sankhya.com.br/hc/article_attachments/44011994825367)

O pedido será **faturado**, a **NF** será vinculada ao pedido no **Magis5 HUB** e seguirá o fluxo padrão, conforme mencionado acima: **“Aguardando Separação → Expedição”**

**Tratamento financeiro dentro do Magis5 ERP**

- Valor zerado.
- Não gera contas a pagar.
- Não gera movimentações contábeis.
- Baixa de estoque ocorre normalmente.
