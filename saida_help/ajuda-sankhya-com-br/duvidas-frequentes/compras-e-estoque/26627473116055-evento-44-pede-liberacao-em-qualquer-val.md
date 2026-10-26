---
id: "26627473116055"
titulo: "Evento 44 pede liberação em qualquer valor e não segue a Liberação em Cascata da TOP"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26627473116055-Evento-44-pede-libera%C3%A7%C3%A3o-em-qualquer-valor-e-n%C3%A3o-segue-a-Libera%C3%A7%C3%A3o-em-Cascata-da-TOP"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-10-14T17:20:35Z"
rotulos: ["Configuração", "TOP", "Financeiro", "Parâmetro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "não a configurada na aba da top \"Liberação por alçada\"", "sistema está validando a alçada do cadastro do usuário", "Artigo atualizado KCS", "CVE - KCS", "Alçada"]
---

# Evento 44 pede liberação em qualquer valor e não segue a Liberação em Cascata da TOP

**MENSAGEM**

A configuração de liberação de limites na **"TOP"** do pedido de compras (Comercial >> Arquivo >> Cadastros >> Tipos de Operação - TOP) não está solicitando liberação ao usuário configurado. Além disso, pedidos de compras com valor inferior ao limite estabelecido estão indevidamente solicitando liberação ou o sistema está validando a alçada do cadastro do usuário e não a configurada na aba **"Liberação em Cascata"** da TOP.

**SITUAÇÃO**

O cliente configurou a liberação de limites na **"TOP"** do pedido de compras para um usuário específico. No entanto, ao testar um pedido de compras, a liberação não foi acionada conforme esperado. O sistema está validando a alçada do cadastro do usuário e não a configurada na aba **"Liberação em Cascata"**.

**SOLUÇÃO**

Para resolver esta situação, compreenda o funcionamento da validação no **"Evento 44"** e o comportamento dos parâmetros:

**(1)** Entenda que no **"Evento 44"**, com a configuração realizada na **"TOP"**, a validação ocorre para todos os movimentos confirmados com essa TOP, seja o valor inferior ou superior ao valor configurado.

**(2)** Verifique que o sistema não valida com base no valor do movimento, mas sim na marcação configurada na **"TOP"**. A validação ocorre independentemente do valor, desde que a **"TOP"** esteja marcada para o evento.

**(3)** Considere que valores de movimento só são considerados quando há a utilização de **"Liberação em Cascata"**, que se trata de um processo de liberação, e não de uma validação do **"Evento 44"**.

**(4)** Para configurar liberação por valor específico, utilize o recurso de **"Liberação em Cascata"** na **"TOP"**, definindo os aprovadores e seus respectivos limites de valor.

**(5)** Verifique se cada aprovador da cascata possui, no cadastro de usuário, limite de liberação para o evento 44 que cubra o valor do movimento. A cascata define quem vai liberar, mas a alçada continua sendo validada pelo cadastro do usuário.

O parâmetro **"LIBCASCSMPDEF"** (Liberação em cascata sempre definir liberador) define o que acontece quando o valor do movimento fica fora da faixa do **último nível** da cascata configurada na **"TOP"**. Ele atua apenas em cenários específicos (por exemplo, níveis cadastrados com Ordem 0 ou solicitante que também é aprovador do último nível):

- Com o parâmetro **"LIBCASCSMPDEF"** ligado (padrão): o sistema mantém o usuário do último nível da cascata como liberador, mesmo com o valor fora da faixa.
- Com o parâmetro **"LIBCASCSMPDEF"** desligado: o sistema não define o liberador. O campo fica em branco (código 0 - SUP) para ser selecionado qual usuário vai liberar.

**CAUSA**

A causa do comportamento está relacionada ao funcionamento do **"Evento 44"**, que não realiza validação direta por valores, e ao fato de que a **"Liberação em Cascata"** da **"TOP"** apenas define quem vai liberar, conforme a faixa de valor. A alçada do aprovador continua sendo validada pelos limites do cadastro do usuário.
