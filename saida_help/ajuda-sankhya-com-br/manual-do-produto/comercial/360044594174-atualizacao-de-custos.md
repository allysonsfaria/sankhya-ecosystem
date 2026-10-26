---
id: "360044594174"
titulo: "Atualização de Custos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594174-Atualiza%C3%A7%C3%A3o-de-Custos"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:19:26Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Custos", "Atualização de Custos", "br.com.sankhya.atualizacao.de.custo", "Atualização de Custos manual", "Configuração", "Atualização", "Estoque", "Comercial"]
---

# Atualização de Custos

```
 Módulo: Comercial > Rotinas
```

---

Nesta tela pode-se atualizar e visualizar todos os custos por Produto, verificando cada custo embutido para ele.

![Imagem 1: Nesta tela pode-se atualizar e visualizar todos os custos por Produto , verificando cada custo embutido para ele.](https://ajuda.sankhya.com.br/hc/article_attachments/21545149811223)

O campo **"Valor de venda fixo"** é utilizado para organizar um preço fixo em moeda. É para ser usado em empresas que trabalham com o preço em alguma moeda ou unidade mais estável como, por exemplo: dólar, euro, ouro, arroba de boi.

**Observação:** o campo **"Controle"** poderá mudar de nome dependendo da marcação no controle adicional de estoque do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-). Por exemplo: se o controle adicional de estoque estiver marcado como **"Parceiro"**, o campo deixará de se chamar Controle, passando a se chamar Parceiro.

**Nota:** quando criada uma regra na [Central de Certificações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053-Central-de-Certifica%C3%A7%C3%B5es), onde se define restrições por empresa e vincular esta regra criada a um usuário no [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios), aba [Validações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abavalidaes), fará com que, quando este usuário acessar a tela Atualização de Custos, ele consiga visualizar apenas as informações relacionadas à sua Empresa de Origem.

Para que os custos sejam atualizados de forma correta, verifique se:

- O custo é calculado na compra ou no menu [Recálculo de custos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594214-Rec%C3%A1lculo-de-Custos);
- A TOP está configurada para calcular custo;
- Se no Cadastro de Produtos os campos **"Fórmula de Custo/Preço"** e **"%Margem de Lucro"** estão devidamente preenchidos;
- A fórmula está corretamente configurada.

Nessa tela, pode-se atualizar os custos para produtos que possuem controle adicional por grade individual, por cada item de controle. Para tal ação, será necessário que o parâmetro **"Controla Custos por Controle ? - CUSTOPORCONT"** seja ligado e no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), o campo **"Controlar por"** e a opção **"Grade"** esteja selecionada.

Com a opção acima habilitada, determine o produto com esta configuração e note que o campo **"Grade"** será exibido para seleção do tipo de controle desejado. 

[GIF animado: Imagem 2: Com a opção acima habilitada, determine o produto com esta configuração e note que o campo "Grade" será exibido para…](https://ajuda.sankhya.com.br/hc/article_attachments/21545710528151)

Como exibido no gif acima, esse controle também poderá ser realizado por meio do botão **"Outras Opções..."**, opção **"Lançamento rápido p/ controle por grade"** caso deseje que seja realizado mais de um controle por vez do produto.

**Observação:** por meio desta opção será permitida apenas a inclusão do cadastro. As alterações e exclusões deverão ser realizadas individualmente.

### Parâmetros que afetam essa rotina

Através do parâmetro **"Decimais para custo - CUSTODEC"** é possível informar a quantidade de casas decimais que serão utilizadas nos campos dessa tela.

Se o parâmetro **"Controla Custos por Controle ? -** **CUSTOPORCONT"** estiver habilitado, o campo Controle aparecerá na tela.

Entretanto, caso na sub-aba [Controle Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abacontroleadicional) do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos) o controle adicional de estoque seja do tipo **"Série"** o campo não estará habilitado, mesmo que o parâmetro esteja ativado.

**Nota1:** ao ativar o parâmetro CUSTOPORCONT não é necessário informar a série, pois a mesma não interfere na atualização do custo para o produto.

**Nota2:** quando habilitado, **não é recomendado realizar transferências entre controles**, pois o controle é uma característica fixa do produto, e pode impactar o cálculo de custo.

Se o parâmetro **"Custo por empresa ? - CUSTOPOREMP"** estiver habilitado, o campo **"Empresa"** será exibido na tela.

Caso o parâmetro **"Controla Custos por Local ? - CUSTOPORLOC"** esteja habilitado, o campo **"Local"** aparece na tela.

Se o campo Controle estiver presente na tela, ele será determinado conforme o campo **"Tipo de controle de estoque"** da tela Cadastro de Produtos.

**Importante:** quando o Tipo de Operação da nota está configurada como **"Bonificação"**, o sistema faz apenas o recálculo do custo médio, portanto, apenas o campo **"CUSMED"** na TGFCUS será recalculado.

O processo acontecerá desta maneira devido à existência de alteração de estoque, no entanto, o **"CUSTOGERENCIAL"**, **"CUSTOREPOSICAO"** e **"CUSTOVARIAVEL"** na TGFCUS não será recalculado, sendo esse o comportamento atual do sistema.

"**Data para atualização de custo" — DTPATUCUST -** este parâmetro define qual campo de data da nota fiscal de entrada o sistema usa como referência ao registrar o custo na tela Atualização de Custos. As opções disponíveis são:

- **Negociação:** data em que o pedido de compra foi negociado.
- **Entrada/Saída:** data de entrada ou saída física da mercadoria na empresa.
- **Movimentação:** data de movimentação do lançamento no sistema.
- **Faturamento:** data de emissão da nota fiscal pelo fornecedor.

> ⚠️ **Importante** **— comportamento fixo do sistema:** Independentemente da opção configurada, o sistema **sempre utiliza a data de Entrada/Saída (DTENTSAI)** como base para o cálculo e registro do custo. Isso ocorre por exigências fiscais e contábeis e não pode ser alterado. 
>
> Na prática: mesmo que o parâmetro esteja configurado como "Negociação" ou "Movimentação", o custo registrado terá como referência a data de entrada/saída da nota. Caso essa data não esteja preenchida, o sistema utilizará a data de negociação como alternativa.
> Por este motivo, ao abrir a tela de Recálculo de Custos ou ao confirmar notas de compra, o sistema pode exibir um aviso orientando que o parâmetro seja ajustado para **"Entrada/Saída"**. Para não visualizar mais esse aviso, basta configurar o DTPATUCUST conforme indicado.

💡 **Atenção ao histórico:** alterar este parâmetro em ambiente com custos já lançados pode gerar inconsistências em recálculos de períodos anteriores. Em caso de dúvidas, consulte o suporte Sankhya antes de realizar a alteração em produção.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594174-Atualiza%C3%A7%C3%A3o-de-Custos#top)

![Imagem 3: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/21068165452695) Acesse também:

[Cálculo de Custos sem Fórmula de Precificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597894-C%C3%A1lculo-de-Custos-sem-F%C3%B3rmula-de-Precifica%C3%A7%C3%A3o)

[Como Atualizar Preço de Custo, Preço de Venda/Tabela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601494-Como-Atualizar-Pre%C3%A7o-de-Custo-Pre%C3%A7o-de-Venda-Tabela)
