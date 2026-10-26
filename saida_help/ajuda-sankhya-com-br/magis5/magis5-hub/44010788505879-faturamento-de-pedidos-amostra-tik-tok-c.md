---
id: "44010788505879"
titulo: "Faturamento de pedidos Amostra Tik Tok com ERP por API Aberta"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010788505879-Faturamento-de-pedidos-Amostra-Tik-Tok-com-ERP-por-API-Aberta"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T18:47:13Z"
rotulos: ["sync_hc", "magis5", "sync_hash_f3d8a90ce963", "magis5_204525010177"]
---

# Faturamento de pedidos Amostra Tik Tok com ERP por API Aberta

## Neste tópico vamos explicar como funciona o fluxo de pedidos amostra no Magis5 HUB utilizando o faturamento com ERP por API Aberta

---

⚠️ Para evitar que os pedidos de Amostra Tik Tok fiquem travados em **“Ag. logística”** no Magis5 HUB, **sem definição de transportadora**, é necessário habilitar no [Tik Tok Shop Seller Center](https://seller-br.tiktok.com/account/login), na aba “Envio”, a opção “**Utilizar Enviado pela Plataforma para encomendas sem cobrança?”.**

![image (47)-1](https://ajuda.sankhya.com.br/hc/article_attachments/44010781497111)

Essa configuração garante que os pedidos sejam importados corretamente para o Magis5 HUB e sigam normalmente o **fluxo de faturamento e expedição.**

### Configurando o faturamento de pedido Amostra

Para os pedidos de **Amostra Tik Tok Shop**, cujo faturamento é realizado diretamente com qualquer ERP por API aberta, os pedidos serão integrados ao **Magis5 HUB** e não permanecerão mais com o status **“Pendência”**. Eles seguirão normalmente o fluxo de **faturamento e expedição**, assim como os demais canais de venda.

⚠️ O faturamento é de responsabilidade integral do ERP do vendedor. Portanto, todas as configurações fiscais para a emissão de Notas Fiscais de pedidos de amostra devem ser devidamente ajustadas no ERP via API Aberta.

- Os pedidos de amostra entrarão com o status **“Ag. Separação”** no HUB. Continuaram em Ag.separação até que o ERP consumidor deve identificar que se trata de amostra e realizar seus fluxos operacionais internos e nos devolver a NF emitida.

**⚠️ Ação Necessária:**

Para que o seu sistema (ERP) identifique pedidos de **Amostra** automaticamente, é necessário que sua **equipe de desenvolvimento** realize um ajuste na leitura da nossa API.

**Instrução Técnica:** O ERP deve ser configurado para ler o **payload**do pedido.
Sempre que o campo `orderChannelType` contiver o valor `"sample_order"`, o sistema deverá classificar e tratar aquele pedido como Amostra.

**O Magis5 HUB:**

- Não interfere no faturamento.
- Não altera o fluxo financeiro.

Pedido segue fluxo operacional conforme regras do ERP.
