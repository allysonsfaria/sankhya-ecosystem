---
id: "44010926801175"
titulo: "Faturamento de pedidos Amostra Tik Tok com Faturador Magis5 HUB"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010926801175-Faturamento-de-pedidos-Amostra-Tik-Tok-com-Faturador-Magis5-HUB"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T18:50:02Z"
rotulos: ["sync_hc", "magis5", "magis5_208238491284", "sync_hash_a2f8d2bb1f0a"]
---

# Faturamento de pedidos Amostra Tik Tok com Faturador Magis5 HUB

## Neste tópico, explicaremos como funciona o fluxo de pedidos de amostra no Magis5 HUB, utilizando o nosso Faturador para emissão de Nota Fiscal.

---

⚠️ Para evitar que os pedidos de Amostra Tik Tok fiquem travados em **“Ag. logística”** no Magis5 HUB, **sem definição de transportadora**, é necessário habilitar no [Tik Tok Shop Seller Center](https://seller-br.tiktok.com/account/login), na aba “Envio”, a opção “**Utilizar Enviado pela Plataforma para encomendas sem cobrança?”.**

![image (47)-1](https://ajuda.sankhya.com.br/hc/article_attachments/44010904680727)

Essa configuração garante que os pedidos sejam importados corretamente para o Magis5 HUB e sigam normalmente o **fluxo de faturamento e expedição.**

### Configurando o faturamento de pedido Amostra

Para os pedidos de **Amostra TikTok Shop**, cujo faturamento é realizado diretamente em nosso **Faturador**, os pedidos serão integrados ao **Magis5 HUB** e não permanecerão mais com o status **“Pendência”**. Eles seguirão normalmente o fluxo de **faturamento e expedição**, assim como os demais canais de venda.

- Os pedidos de **amostra** entrarão com o status **“Ag. Separação”** no **HUB**. Em seguida, serão faturados conforme a **"Natureza de operação"** criada para **Bonificação/Amostra**

Para cadastrar uma nova **"Natureza de operação"**para **“Amostra”** ou **“Bonificação”**, acesse o Magis5 HUB vá em **"Configurações"**, depois até **"Notas Fiscais"** e por último clique em **"Natureza de Operação"**

![Captura de tela 2026-02-25 105013](https://ajuda.sankhya.com.br/hc/article_attachments/44010910028439)

Nesta aba, o sistema exibe todas as **Naturezas de Operação** já cadastradas. É possível criar uma nova **Natureza de Operação** para os tipos **"Venda"**. Para isso, clique no botão **"NOVO"**, localizado no canto superior direito da tela.

![Captura de tela 2026-02-25 105614](https://ajuda.sankhya.com.br/hc/article_attachments/44010904912791)

Abaixo temos os seguintes campos disponíveis para preenchimento:

![Captura de tela 2026-02-25 105937](https://ajuda.sankhya.com.br/hc/article_attachments/44010905020311)

**-** **Descrição:** preencha com o nome da Natureza de Operação.

**-** **Indicador de Presença:**lista do **SEFAZ**para categorizar o tipo de operação:

- **0** – Não se aplica (ex.: nota de ajuste ou complementar)
- **1** – Cliente presente na loja (venda presencial)
- **2** – Venda feita pela internet
- **3** – Venda feita por telefone
- **4** – Entrega em domicílio (apenas para NFC-e)
- **5** – Venda presencial fora da loja (ex.: em feiras ou eventos)
- **9** – Venda sem a presença do cliente, mas que não se encaixa nas opções 2 ou 3

**- Código de Regime Tributário:**informa para qual regime tributário será destinado, tendo como opções:

- **Simples Nacional**
- **Simples Nacional – Excesso de sublimite de receita bruta**(Quando a empresa ultrapassa o limite de receita permitida para recolher ICMS/ISS pelo Simples, mas permanece no regime).

**- Tipo:**define a finalidade da nota fiscal, indicando se a operação é de entrada ou saída de mercadoria, produto ou serviço.

**- Faturada:**indica se a Natureza de Operação será **faturada**:

- **Sim**: os **impostos serão calculados** normalmente.
- **Não**: os impostos **não serão calculados**, e a operação será marcada como **Ativada** (sem faturamento fiscal).

**-** **Consumidor Final:** informa se a operação é destinada ao **consumidor final**:

- **Sim**: a mercadoria ou serviço será **consumido pelo destinatário**, sem revenda.
- **Não**: o destinatário poderá usar a mercadoria em **revenda ou produção**.

⚠️ Além disso, estarão disponíveis outras guias, como I**CMS, IPI, PIS, COFINS e Retenções.**
Preencha cada uma delas **com atenção**, conforme as exigências da operação e, se possível, com o auxílio do seu **contador** ou de alguém com **conhecimento fiscal.**

**💡 Em caso de dúvidas sobre a criação de Natureza de Operação, [clique aqui](https://ajuda.sankhya.com.br/como-cadastrar-uma-nova-natureza-de-opera%C3%A7%C3%A3o-na-magis5) para acessar o manual completo com as orientações detalhadas.**

Após preencher todas as informações, clique no botão **"Salvar"**, localizado no **lado direito da página**, para concluir o processo.

![Captura de tela 2026-02-25 111014](https://ajuda.sankhya.com.br/hc/article_attachments/44010918268055)

Após concluir o cadastro da Natureza de Operação destinada à **Bonificação/Amostra**, é necessário defini-la como **“Padrão Bonificação/Amostra**”. Para isso, acesse a tela Naturezas de Operações, localize a operação recém-criada, **clique nos três pontos** ao lado da operação e selecione a opção **“Padrão Bonificação/Amostra”**.

![Captura de tela 2026-02-25 113000](https://ajuda.sankhya.com.br/hc/article_attachments/44010897908631)

Dessa forma, a natureza cadastrada ficará configurada como padrão para esse tipo de operação.

⚠️ **Atenção:** Caso não seja definida a operação ao "**padrão de bonificação"**, o sistema continuará utilizando o padrão de venda vigente.

Se a operação de **bonificação/amostra for configurada** após a criação de algum pedido, ela será aplicada apenas às vendas faturadas a partir desse momento, sem alterar pedidos ou operações já realizados anteriormente.

Para concluir o processo e garantir que os pedidos do tipo **Amostra** sejam faturados corretamente, é necessário também realizar a configuração do Faturador. Para isso, acesse **"Configurações"**, selecione a opção **"Integrações**" e, em seguida, clique em **"ERPs & Faturador"**.

![Captura de tela 2026-02-25 130055](https://ajuda.sankhya.com.br/hc/article_attachments/44010905373207)

Na tela, selecione o faturador responsável pelo faturamento dos pedidos Tik Tok e clique em **"Editar".**

![Captura de tela 2026-02-25 130245](https://ajuda.sankhya.com.br/hc/article_attachments/44010890061719)

Em "**Dados adicionais"**, você pode definir qual preço será utilizado na emissão das Notas Fiscais dos pedidos **Amostra TikTok**. Basta selecionar a opção desejada:

- **Preço de Custo**
- **Preço de Venda**

![Captura de tela 2026-02-25 130746](https://ajuda.sankhya.com.br/hc/article_attachments/44010910601239)

Após selecionar a opção desejada, clique em **"Salvar"**, localizado no canto superior da tela.

![Captura de tela 2026-02-25 132109](https://ajuda.sankhya.com.br/hc/article_attachments/44010905677207)
