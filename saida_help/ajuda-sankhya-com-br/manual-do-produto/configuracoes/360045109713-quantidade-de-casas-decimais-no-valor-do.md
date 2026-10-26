---
id: "360045109713"
titulo: "Quantidade de Casas Decimais no Valor do Contrato "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109713-Quantidade-de-Casas-Decimais-no-Valor-do-Contrato"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:55:53Z"
rotulos: ["Produtos", "Configuração", "Contrato", "Quantidade de Casas Decimais no Valor do Contrato  manual", "Estoque", "Financeiro", "Configurando Casas Decimais nos Contratos"]
---

# Quantidade de Casas Decimais no Valor do Contrato 

Para que os [Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774) apresentem os valores na quantidade de casas decimais desejada, realize as seguintes configurações:

**1)** Na tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#top), aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abamedidaseestoque), preencha no campo **"Decimais para o valor"** o número de casas decimais que o sistema aceitará para a quantidade do produto.

![Imagem 1: 1) Na tela Cadastro de Produtos , aba Medidas e Estoque , preencha no campo "Decimais para o valor" o número de casas…](https://ajuda.sankhya.com.br/hc/article_attachments/6606970012823)

**2)** Informe também o campo **"Valor"**, localizado na tela Contratos, aba [Produtos/Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos#abaprodutosservios).

![Imagem 2: 2) Informe também o campo "Valor" , localizado na tela Contrato s, aba Produtos/Serviços .](https://ajuda.sankhya.com.br/hc/article_attachments/6607366283799)

---

#### Imagem 3: Regras ImportantesRegras Importantes

**(2)** Nas telas [Reajuste de Contratos Ativos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113573) e [Faturamento de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654) não serão consideradas as casas decimais em suas respectivas grades. No caso do Faturamento de Contratos, como na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414) é levada em consideração a quantidade de casas decimais para valor, na nota virá com a quantidade conforme configurado no campo **"Vlr. Unitário"**.

**(2)** No Banco de Dados Sql Server tem a limitação do campo para 4 casas decimais, por isso, pode ocorrer a mensagem que o campo não suporta mais do que isso. Trata-se de comportamento do BD.

**(2)** Se o produto\serviço estiver configurado com o campo **"Decimal para Valor"** igual a vazio (em branco) o sistema levará em consideração que se trata de duas casas decimais como padrão. Se o campo estiver igual à zero, então será considerado que para este produto\serviço não podem ser aplicadas casas decimais, tornando o valor como inteiro.

**(2)** O parâmetro **"Habilitar preço por faixa? - BILFAIXA"** se habilitado será apresentada a aba **"Preços por Faixa"**, na aba de Produtos\Serviços do cadastro de Contratos. Além disso, será considerada duas casas decimais como padrão.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109713-Quantidade-de-Casas-Decimais-no-Valor-do-Contrato#top)
