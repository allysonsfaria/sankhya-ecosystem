---
id: "27896758680727"
titulo: "Como deduzir o INSS/IRRF em casos de (PF) quando e utilizado Tabela Progressiva?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27896758680727-Como-deduzir-o-INSS-IRRF-em-casos-de-PF-quando-e-utilizado-Tabela-Progressiva"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:39:08Z"
rotulos: ["Configuração", "Parceiro", "Movimentação Financeira", "Impostos", "TOP", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Tabela Progressiva"]
---

# Como deduzir o INSS/IRRF em casos de (PF) quando e utilizado Tabela Progressiva?

Existem situações em que se faz necessária a retenção de INSS/IRRF para pessoas físicas ou autônomos, em lançamentos como, por exemplo, de aluguéis ou transportes. Nesses casos, a verificação deve ser realizada com base na Tabela Progressiva.

Para um passo a passo detalhado e informações referentes aos campos, recomenda-se a consulta aos seguintes materiais:

- [Configurações para Retenção do IRPF/INSS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112873-Reten%C3%A7%C3%A3o-do-IRPF-INSS#configuraespararetenodoirpfinss-tabelaprogressiva-nacentraldecompras)
- [Retenção do IRPF/INSS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112873-Reten%C3%A7%C3%A3o-do-IRPF-INSS#retenodoirpfinss-tabelaprogressiva-nacentraldecompras)
- [Tabela de IRPF/INSS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108293-Tabela-de-IRPF-INSS)

No entanto, seguem abaixo as configurações básicas essenciais para que o processo seja executado corretamente:

- Na tela [**"Cadastro de Tipos de Operação - TOP"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114), para o Tipo de Movimento **"C-Compra"**, na aba [**"Impostos"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos), devem ser realizadas as seguintes marcações:

[GIF animado: Imagem 1: Na tela "Cadastro de Tipos de Operação - TOP" , para o Tipo de Movimento "C-Compra" , na aba "Impostos" , devem ser…](https://ajuda.sankhya.com.br/hc/article_attachments/27896788651287)

A seleção da opção **"Aplicar tabela de IRPF/INSS"**, quando realizada, determina que, nos lançamentos de Compra efetuados com esta TOP, para parceiros classificados como Pessoas Físicas, sejam aplicados os valores constantes na tabela de IRPF/INSS. Além disso, os campos **"Tem FUNRURAL/INSS"** e **"Tem IRF"** serão habilitados.

- Para que o sistema realize o cálculo da retenção de IRPF/INSS com base na tabela, é imprescindível o cadastro do Parceiro na aba **"**[**Parceiros sujeitos à tabela progressiva**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108293-Tabela-de-IRPF-INSS#abaparceirossujeitosatabelaprogressiva)**"**, disponível na tela [**"Tabela de IRPF/INSS"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108293-Tabela-de-IRPF-INSS).
- Ao selecionar a opção **"Usar serviço p/ cálculo com tabela de IRPF/INSS"** dentro da TOP, na aba **"Impostos"**, define-se o serviço que será utilizado para a realização do cálculo em conjunto com a tabela de IRPF/INSS.
- Na tela de [**"Serviços"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114), é necessário observar o campo **"% de valor de IR"**, localizado na aba **"Geral"**. Este campo não deve ser preenchido quando se utiliza a Tabela Progressiva e quando houver uma linha configurada com informações em **Outros Impostos**.

**Observações pertinentes:**

- Caso a TOP utilizada no lançamento esteja com a opção Aplicar Tabela de IRPF/INSS selecionada, porém Jurídica, o sistema efetuará os cálculos usuais de retenção de IRPF e INSS, conforme as alíquotas configuradas no Serviço ou em [**Outros Impostos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o#abaoutrosimpostos), não sendo aplicada a Tabela Progressiva.
- O cálculo do ISS permanecerá seguindo as regras vigentes, não sendo alterado pelo comportamento aqui descrito.
- A retenção, no caso de utilização da Tabela Progressiva, será apresentada exclusivamente na Movimentação Financeira.

![Imagem 2: A retenção, no caso de utilização da Tabela Progressiva, será apresentada exclusivamente na Movimentação Financeira.](https://ajuda.sankhya.com.br/hc/article_attachments/27959885697687)
