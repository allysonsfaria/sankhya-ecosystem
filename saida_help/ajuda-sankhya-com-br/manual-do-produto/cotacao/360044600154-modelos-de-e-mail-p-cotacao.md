---
id: "360044600154"
titulo: "Modelos de E-mail p/ Cotação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600154-Modelos-de-E-mail-p-Cota%C3%A7%C3%A3o"
trilha: "Manual do Produto > Comercial e Vendas > Vendas > Cotação"
atualizado_em: "2026-07-29T14:36:36Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Modelo", "Cotação", "Assunto", "Tipo de e-mail", "Parceiro", "Variáveis", "Cancelamento de produtos", "Novos produtos", "br.com.sankhya.swb.cotacao.cadastros.modeloemail", "Modelos de E-mail p/ Cotação manual", "Variáveis: Nome Razão Social Link Código do Produto.", "Configuração de e-mail: Novos produtos e Cancelamento.", "Texto e Assunto: Utilize variáveis para personalização.", "Documentos Eletrônicos"]
---

# Modelos de E-mail p/ Cotação

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42312233093527) Módulo: Cotação > Cadastros
```

---

A empresa decidindo utilizar o Portal de Cotação online, é necessário a configuração dos modelos de e-mail para envio ao contato do fornecedor.

![Imagem 2: A empresa decidindo utilizar o Portal de Cotação online, é necessário a configuração dos modelos de e-mail para envio…](https://ajuda.sankhya.com.br/hc/article_attachments/360083138533)

Através do campo **"Tipo de e-mail"** você definirá o modelo de e-mail que será configurado e, posteriormente, encaminhado dos fornecedores. A saber:

- **Novos produtos:** Este modelo será o assunto e o texto do e-mail que será enviado ao fornecedor, quando o comprador enviar os produtos requisitados para o fornecedor precificá-los no Portal de Cotação Online;
- **Cancelamento de produtos:** Este modelo será o assunto e o texto do e-mail que será direcionado ao fornecedor quando o comprador cancelar algum produto que já tenha sido enviado para o fornecedor. Para cada produto cancelado, será transmitido um e-mail ao fornecedor.

No campo **"Variáveis para e-mail"** serão apresentadas as variáveis que poderão ser utilizadas para construção do texto do e-mail; cada Tipo de e-mail apresenta um conjunto de variáveis possíveis de utilização. São elas:

#### Tipo de e-mail - Novos produtos

- Nome do parceiro;
- Razão social do parceiro;
- Nome do contato;
- Link de acesso ao portal de cotação;
- Nome Empresa;
- Número da cotação.

#### Tipo de e-mail - Cancelamento de produtos

- Nome do parceiro;
- Razão social do parceiro;
- Nome do contato;
- Link de acesso ao portal de cotação;
- Código do produto;
- Nome do Produto;
- Controle do produto;
- Nome Empresa;
- Número da cotação.

**Observação:** As variáveis Número da cotação e Nome Empresa poderão ser utilizadas tanto para a opção **"Novos produtos"** quanto para a opção **"Cancelamento de produtos"**.

O campo **"Assunto"** é destinado ao preenchimento da temática do e-mail; o motivo de seu envio.

**Nota:** Pode-se inserir as variáveis Número da cotação e Nome Empresa no campo Assunto, para que o vendedor possa localizar de forma ágil o e-mail identificando o número da cotação e a empresa solicitante pelo assunto do e-mail.

O espaço **"Texto para e-mail"** é empregado na formulação do texto do e-mail a ser enviado. Aqui, temos a liberdade de utilização das **"Variáveis para e-mail"** apresentadas acima.

**Observação:** A variável Nome Comprador só será preenchida se o código do responsável for maior que **"0"** e no [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios), aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abaidentificao), o campo **"Nome Completo"**,estiver preenchido.

#### Como utilizar as Variáveis para e-mail:

Suponhamos que você fez a escolha de configurar um modelo de e-mail do tipo **"Novos produtos"**. Definido o assunto, no espaço Texto para e-mail informe o seguinte texto:

```
Boa tarde João Almeida.

A empresa Áudio e Vídeo Produções, está efetuando cotações de produtos com seus fornecedores.

Para acessar o Portal Cotação e precificar os itens requisitados, clique aqui.
```

Os trechos em destaque são os resultados das variáveis escolhidas no campo **"Variáveis para e-mail"**; o fornecedor irá visualizar o e-mail desta forma. Este procedimento é feito digitando-se o texto desejado, e escolhendo as devidas variáveis. O texto apresentado acima, ao ser formulado na tela **"Modelos de E-mail p/ Cotação"**, será apresentado da seguinte forma:

```
Boa tarde ${nomecttcot.link}.

A empresa ${nomeempresa.link}, está efetuando cotações de produtos com seus fornecedores.

Para acessar o Portal Cotação e precificar os itens requisitados, ${linkcotacao.link}.
```

As variáveis em destaque se referem ao **"Nome do contato"**, **"Nome Empresa"** e **"Link de acesso ao portal de cotação"**, respectivamente.

**Observação:**A variável **"Link de acesso ao portal de cotação"** representa no e-mail enviado, o texto **"clique aqui"**, de modo que quando o contato clicar neste texto, será feito o direcionamento para a tela do Portal de Cotação.

---

![acesse](https://ajuda.sankhya.com.br/hc/article_attachments/16079182245655) Acesse também:

[Cotação - Configurações p/ envio de e-mail](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598074)
