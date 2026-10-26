---
id: "360044598334"
titulo: "Taxa de Boleto no Total da Nota"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598334-Taxa-de-Boleto-no-Total-da-Nota"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:47:23Z"
rotulos: ["Configuração", "Contas", "Parceiro", "Taxa de Boleto no Total da Nota", "Taxa de Boleto no Total da Nota manual", "Impostos", "Vendas", "Financeiro", "Inclusão de Taxa de Boleto no Total da Nota"]
---

# Taxa de Boleto no Total da Nota

Para que a taxa seja somada à nota e financeiro é necessário que:

- Os parâmetros **"Taxa de boleto no total da nota? - TAXBOLNOT"** e **"Taxa de boleto com tipo INCLUSO? - TAXBOLNOTTJ"** estejam ligados;
- Deve ser uma nota de Venda;
- Não pode ser nota de Complemento;
- O parceiro não pode ser isento de taxa mínima. Essa marcação se encontra na aba [Crédito](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abacrdito) da tela [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), campo **"Isento Taxa Boleto"**;
- A TOP não pode ser de impressora fiscal.
- Para que o cálculo seja gatilhado no rodapé da nota, os campos Banco, Conta Bancária e Tipo de Título devem estar preenchidos no financeiro. O sistema utiliza a Conta Bancária informada para buscar o valor configurado no campo "**Ou Cobrar taxa**" do cadastro de contas.
- O parâmetro **"Calcular taxa de boleto para o tipo de movimento - CALTXBLTPMV"** permite estender este procedimento para outros tipos de movimento. Configure-o utilizando a letra correspondente, **sempre separadas por ponto (.)**:

  - Somente Vendas: V
  - Somente Pedidos de Venda: P
  - Ambos (Pedido e Venda): P.V
  - **Nota:** Não utilize vírgula (,) ou ponto e vírgula (;) como separadores, pois o sistema desconsiderará a configuração.

**Observação:** não é possível realizar essa operação com taxa destacada na tela [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173).

Abaixo tem um exemplo de aplicação deste recurso:

Primeiramente ative o parâmetro Taxa de boleto no total da nota? - TAXBOLNOT.

Depois, na tela [Cadastros de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas) informe o valor da taxa que será cobrado para o envio do boleto no campo **"Ou Cobrar taxa"**. Neste exemplo, se o valor do título for menor que R$ 800,00, será cobrado do cliente uma taxa de R$ 250,00. Caso contrário, a taxa não será cobrada.

![Imagem 1: Depois, na tela Cadastros de Contas informe o valor da taxa que será cobrado para o envio do boleto no campo "Ou Cobrar…](https://ajuda.sankhya.com.br/hc/article_attachments/4409287953815)

Agora, realize na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414) o lançamento de uma nota de venda. No rodapé da nota, aba [Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414#abafinanceiro) informe o **"Banco"**, o **"Tipo de Título"** e a **"Conta Bancária"**.

![Imagem 2: Agora, realize na Central de Vendas o lançamento de uma nota de venda. No rodapé da nota, aba Financeiro informe o…](https://ajuda.sankhya.com.br/hc/article_attachments/4409290314647)

Dessa forma, o valor total da nota será atualizado. 

**Nota:** Se os dados financeiros forem inseridos após a nota já estar preenchida e o valor não atualizar automaticamente, é necessário refazer o financeiro (excluir e gerar as parcelas novamente) para que o gatilho de cálculo da taxa seja acionado.

**Observação:** neste exemplo, obteve-se a somatória do total da nota com a taxa gerada. Para isso, é necessário que o parâmetro **"Taxa de boleto com tipo INCLUSO?-TAXBOLNOTTJ"** esteja ligado. Caso contrário, o valor da taxa será informado, mas não será somado com o total da nota. É importante ressaltar ainda que, esse exemplo é básico e não estamos considerando outros tipos de gastos que poderiam ser cobrados como impostos, juros, entre outros. Deste modo, consideramos somente o valor do produto.

**Observação sobre o Valor Mínimo**: > No **Cadastro de Contas**, o campo "**Valor Mínimo para Taxa**" define o teto para a cobrança. A taxa só será aplicada se o valor do título for menor que o valor mínimo estipulado. Se você deseja que a taxa seja cobrada em qualquer situação, certifique-se de que o valor do título não ultrapasse o limite configurado neste campo.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598334-Taxa-de-Boleto-no-Total-da-Nota#top)
