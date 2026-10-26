---
id: "360044597814"
titulo: "Produtos e Serviços na Negociação Pré-Venda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597814-Produtos-e-Servi%C3%A7os-na-Negocia%C3%A7%C3%A3o-Pr%C3%A9-Venda"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:46:43Z"
rotulos: ["Produtos", "Configuração", "Relatórios Formatados", "Parceiro", "Produtos e Serviços na Negociação Pré-Venda manual", "Gerenciando Produtos e Serviços na Pré-Venda", "Venda Mais"]
---

# Produtos e Serviços na Negociação Pré-Venda

Para oferecer os recursos necessários para informar os produtos e serviços na negociação da pré-venda, de forma que a tabela de preço ao fim da negociação seja gerada, o parâmetro **"Usa produtos na negociação Pré-venda? - USAPRODNEGOC"** foi criado.

Assim, na aba **"Produto e Serviços"** da tela [Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113213-Negocia%C3%A7%C3%A3o), e na tela [Modelo de Projetos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604434-Modelo-de-Projetos), os campos **"Pedido Modelo"** e **"Exige Prod. na Negociação"** serão apresentados nas abas [Informações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604434-Modelo-de-Projetos#abainforma%C3%A7%C3%B5es) e [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604434-Modelo-de-Projetos#sub-abageral), respectivamente.
Além de que, o Modelo de Projeto será vinculado ao **"Modelo de Notas e Pedidos"** por meio do parâmetro **"Metodologia p/ Pré-Venda - SERVMETPRE"**.

Desse modo, defina no campo Pedido Modelo, o modelo de nota a ser utilizado na metodologia pré-venda.

![Imagem 1: Desse modo, defina no campo Pedido Modelo , o modelo de nota a ser utilizado na metodologia pré-venda.](https://ajuda.sankhya.com.br/hc/article_attachments/4414485361815)

Na Pré-Venda, você pode definir a partir de qual etapa será obrigatório ter produtos cadastrados; de forma que, não será possível prosseguir para uma próxima etapa se a etapa atual estiver com a marcação **"Exige Prod. na Negociação"** habilitada, e não existirem produtos cadastrados.

**Nota:** quando uma pré-venda for realizada no Sankhya-Om com um parceiro que não possui integração com o [Checkout](https://ajuda.sankhya.com.br/hc/pt-br/articles/360056765053-Processos-de-vendas-no-Sankhya-Checkout#inser%C3%A7%C3%A3odecpfnacompra), esse parceiro será identificado na finalização da venda executada no Checkout. Assim, as etapas da metodologia serão definidas.

**Observação:** não se deve marcar a referida opção para primeira etapa, pois não terá nenhum produto ou serviço cadastrado.

```
    ![Imagem 2: Observação: não se deve marcar a referida opção para primeira etapa, pois não terá nenhum produto ou serviço cadastrado.](https://ajuda.sankhya.com.br/hc/article_attachments/42310625059351) Para a próxima etapa de execução, é necessário que você possua produtos
          cadastrados.
```

Quando inserido o primeiro item em **"Produtos/Serviços"** é criado um cabeçalho de nota/pedido conforme o modelo de notas vinculado ao modelo de projeto, assim, a cada item inserido é criado um item na nota/pedido.

Ao criar a nota o sistema utilizará a empresa do vendedor vinculado ao usuário logado, ou seja, se o vendedor for "0" o sistema pega a empresa inserida no modelo de notas e pedidos.

Ao fechar a negociação, é criada uma tabela de preço e inseridos todos os produtos e serviços na aba Produto/Serviço da tela Negociação.![Imagem 3: Ao fechar a negociação, é criada uma tabela de preço e inseridos todos os produtos e serviços na aba Produto/Serviço da…](https://sankhyasd.zendesk.com/hc/article_attachments/360055963254/embim854.jpg)

Assim, quando um Modelo de Notas e Pedidos for cadastrado, é criado um cabeçalho e cada produto e serviço inserido na aba Produtos/Serviços é inserido na nota. 

---

### Impressão da Proposta

Primeiramente, é necessário informar o modelo do relatório criado na tela [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados) no parâmetro **"Modelo de relatrio proposta Produtos/Servios Pr-ve -** **MODRELPRODNEG"**.

Assim, após cadastrar um relatório com um modelo IReport na tela Relatórios Formatados, e inseri-lo também no parâmetro Modelo de relatrio proposta Produtos/Servios Pr-ve -  MODRELPRODNEG.

Então, clique no botão ![Imagem 4: Então, clique no botão "Imprimir Proposta" na aba Geral da tela Negociação o sistema irá buscar o modelo IReport…](https://ajuda.sankhya.com.br/hc/article_attachments/11437960317463) **"Imprimir Proposta"** na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113213-Negocia%C3%A7%C3%A3o#abageral) da tela Negociação o sistema irá buscar o modelo IReport inserido na tela Relatórios Formatados.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597814-Produtos-e-Servi%C3%A7os-na-Negocia%C3%A7%C3%A3o-Pr%C3%A9-Venda#top)
