---
id: "43548293543831"
titulo: "Por que a OP de Desmonte baixa a matéria-prima ao invés de dar entrada no estoque?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43548293543831-Por-que-a-OP-de-Desmonte-baixa-a-mat%C3%A9ria-prima-ao-inv%C3%A9s-de-dar-entrada-no-estoque"
trilha: "Dúvidas Frequentes > Produção"
atualizado_em: "2026-09-22T15:49:44Z"
rotulos: ["Artigo criado KCS", "Produção - KCS"]
---

# Por que a OP de Desmonte baixa a matéria-prima ao invés de dar entrada no estoque?

Ao apontar a Ordem de Produção (OP) e gerar a nota de produção vinculada a uma TOP de Desmonte, o sistema deveria realizar a **entrada** da matéria-prima reaproveitada. Quando esse comportamento não ocorre e o sistema realiza uma **baixa** da MP (Matéria-Prima) ao invés da entrada, normalmente é porque duas configurações do processo não estão alinhadas ao fluxo de desmonte.

Para identificar e corrigir a causa, siga o passo a passo abaixo.

#### **(1)** Verifique a configuração da TOP de Desmonte:

1. Acesse a tela **Tipos de Operação – TOP (**Comercial » Arquivo » Cadastros » Tipos de Operação - TOP**)**.
2. Localize a TOP de Desmonte utilizada no processo.
3. Vá até a aba **Estoque**.
4. Confira o campo **"Atualiza estoque MP"** — ele precisa estar coerente com o comportamento esperado para o fluxo de desmonte **(Entrar).**

   ![Imagem 1: Confira o campo "Atualiza estoque MP" — ele precisa estar coerente com o comportamento esperado para o fluxo de…](https://ajuda.sankhya.com.br/hc/article_attachments/43600362855575)

#### **(2)** Verifique a configuração da matéria-prima na Composição do Produto:

1. Acesse a tela **Composição do Produto (**Produção » Cadastros » Composição do Produto**)**.
2. Selecione o produto e o processo produtivo de desmonte correspondente.
3. Vá até a aba **Matérias-Primas**.
4. Localize a matéria-prima que deveria retornar ao estoque.
5. Confira o campo **"Tipo de Uso do Material"** — ele deve estar configurado como **"Reaproveitamento em Desmonte"**.

   **Observação:** 
   **O sistema prioriza a configuração do campo "Tipo de Uso do Material" em relação à atualização de estoque da TOP, permitindo que materiais auxiliares efetivamente consumidos no processo de desmonte, como álcool isopropílico utilizado na limpeza de componentes eletrônicos, sejam corretamente baixados do estoque ao desmontar um Computador.**

   ![Imagem 2: Confira o campo "Tipo de Uso do Material" — ele deve estar configurado como "Reaproveitamento em Desmonte" .…](https://ajuda.sankhya.com.br/hc/article_attachments/43600362856727)

Esse campo é o que informa ao sistema que aquela MP (Matéria-Prima) deve ser reintegrada ao estoque (Entrar), e não tratada como consumo normal de produção (Baixar).

Com a TOP configurada corretamente e a MP (Matéria-Prima) marcada como **"Reaproveitamento em Desmonte"** na composição, o apontamento da OP e a geração da nota de produção devem realizar a entrada da matéria-prima no estoque, e não a baixa.

Se, após validar os dois pontos acima, o comportamento persistir, será necessário abertura de chamado com Service Desk.
