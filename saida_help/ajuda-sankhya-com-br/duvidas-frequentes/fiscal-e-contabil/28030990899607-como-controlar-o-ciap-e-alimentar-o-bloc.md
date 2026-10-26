---
id: "28030990899607"
titulo: "Como controlar o CIAP e alimentar o Bloco G no EFD para novos clientes?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28030990899607-Como-controlar-o-CIAP-e-alimentar-o-Bloco-G-no-EFD-para-novos-clientes"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:38:50Z"
rotulos: ["Produtos", "Configuração", "Fiscal", "Impostos", "EFD", "Passos para resolver", "Razão do erro", "Detalhe do erro", "CIAP", "controlar o CIAP", "alimentar o Bloco G", "novos clientes"]
---

# Como controlar o CIAP e alimentar o Bloco G no EFD para novos clientes?

Esse tipo de dúvida pode ocorrer, principalmente, em situações de novas implantações, nas quais o cliente, que anteriormente realizava a apuração do CIAP em outro sistema, necessita agora inserir as informações do BEM no Sankhya para assegurar a continuidade adequada dessa apuração.

#### Procedimento

Normalmente, a apuração do CIAP e a alimentação do bloco G ocorrem de forma nativa quando a compra do BEM é registrada pelo portal de compras. Consequentemente, todos os dados são atualizados automaticamente no cadastro de produtos, na aba bens.

**(1)** Acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos) e, para os produtos nos quais se deseja apurar o CIAP, realize a inserção manual do bem, preenchendo todos os dados obrigatórios;

**(2)** Na aba **"Bens"**, sub-aba **"Bens"**, preencha corretamente a subaba **"CIAP"**.

**IMPORTANTE**: Os campos pertinentes a esta subaba somente serão habilitados caso o imobilizado (produto) esteja com a opção **"Atualizar CIAP"** marcada, na aba **Impostos** da tela Produtos.

- Informe as datas conforme o controle realizado;
- No campo **"Valor do ICMS"**, não deve ser inserido o valor remanescente a ser depreciado, mas sim o **VALOR TOTAL desde o início da aquisição do bem.** Somente dessa forma o sistema continuará gerando os valores conforme o esperado.
- O campo **"Tipo de movimentação do bem ou componente"** apresenta diversas opções, porém, para este caso de inserção manual dos dados, deve-se escolher a seguinte opção: **"SI - Saldo inicial de bens imobilizados"**

![Imagem 1: O campo "Tipo de movimentação do bem ou componente" apresenta diversas opções, porém, para este caso de inserção manual…](https://ajuda.sankhya.com.br/attachments/token/lfmQXC0BGZ3wtcNBiRNlVLBkE/?name=image.png)

##### IMPORTANTE: Quando o parâmetro "Utiliza TIPOENTCIAP para geração do SPED - TIPOENTCIAPSPED" estiver habilitado, durante a geração do SPED, o valor informado no campo Tipo de movimentação do bem ou componente será considerado no arquivo TXT gerado. Caso esteja desabilitado, será analisada a Data Inicial do Bem e a Data Atual, sendo calculada a diferença de meses entre as datas; será informado "IM" caso a diferença seja igual a "1", e "SI" caso seja diferente de "1".

**Para mais informações sobre o cadastro de Produtos e CIAP, consulte os seguintes materiais:**

- [Melhores Práticas - Configuração e Cálculo do CIAP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044580254-Melhores-Pr%C3%A1ticas-Configura%C3%A7%C3%A3o-e-C%C3%A1lculo-do-CIAP)

- [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#AbaCIAP)
