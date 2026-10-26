---
id: "360044609554"
titulo: "Contagem de Estoque (Cód. barras)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609554-Contagem-de-Estoque-C%C3%B3d-barras"
trilha: "Manual do Produto > Suprimentos e Estoque > Inventário"
atualizado_em: "2026-07-29T14:48:54Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Inventário", "WMS", "Estoque", "Código de Barras", "Contagem de Estoque (Cód. barras)", "PEDEQTDEINVET", "TAMCODBARRA", "TDMINCONFBAR", "br.com.sankhya.invent.contagem.estoque.cod.barras", "Contagem de Estoque (Cód. barras) manual", "Inserção rápida produtos", "Salvar e confirmar contagem", "Leitura código barras"]
---

# Contagem de Estoque (Cód. barras)

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312566335511) Módulo: Inventário > Avançado
```

---

Através desta tela, você realiza a contagem do estoque por meio de um leitor de código de barras, como também por meio da digitação manual do código de barras dos produtos. Inicialmente, informe a data em que será efetuada a contagem do estoque e para qual empresa.

![Imagem 2: Através desta tela, você realiza a contagem do estoque por meio de um leitor de código de barras, como também por meio…](https://ajuda.sankhya.com.br/hc/article_attachments/6166201308055)

Em seguida, utilize o botão ![Imagem 3: Em seguida, utilize o botão "Prosseguir" para dar continuidade na contagem.](https://ajuda.sankhya.com.br/hc/article_attachments/6164829815575) **"Prosseguir"** para dar continuidade na contagem.

![Imagem 4: Em seguida, utilize o botão "Prosseguir" para dar continuidade na contagem.](https://ajuda.sankhya.com.br/hc/article_attachments/6164922454679)

Para inserção dos produtos na contagem, informe seu Código de Barras no campo **"[F8] Inserir produtos"** e pressione **"Enter"** ou o botão :

![Imagem 5: Para inserção dos produtos na contagem, informe seu Código de Barras no campo "(F8) Inserir produtos" e pressione…](https://ajuda.sankhya.com.br/hc/article_attachments/6165058387479)

Por meio do campo **"Defina o local da contagem"**, você indica o local onde os produtos estão depositados.

Clicando no link Saiba como inserir produtos rapidamente, teremos o pop-up **"Inserir/Remover produtos rapidamente"**, que apresenta as seguintes orientações para inclusão e remoção dos produtos da tela:

- **2\***12345678910

Quantidade de vezes que o código de barras deverá ser adicionado para mais de uma unidade do produto;

- **-**12345678910

Remove uma única unidade do produto correspondente ao código de barras;

- 2-12345678910

Quantidade de vezes que o código de barras deverá ser retirado para mais de uma unidade do produto;

**Observação:** o parâmetro **"Permite edição na contagem por Cód. Barras? - EDITACONTCODBAR"**, quando habilitado, permitirá a execução dos comportamentos elencados no link Saiba como inserir produtos rapidamente, como também a edição dos dados contidos nas colunas Quantidade, Unidade, Controle e Local.

**Nota:** os produtos de mesmo Código de Barras serão agrupados.

Temos través do botão ![Imagem 6: Temos través do botão "Detalhes" , as particularidades da contagem informadas na abertura da tela. Assim, você poderá…](https://ajuda.sankhya.com.br/hc/article_attachments/6165091303703) **"Detalhes"**, as particularidades da contagem informadas na abertura da tela. Assim, você poderá corrigir os dados incluir os mesmos, quando não for realizada na inserção inicial.

![Imagem 7: Temos través do botão "Detalhes" , as particularidades da contagem informadas na abertura da tela. Assim, você poderá…](https://ajuda.sankhya.com.br/hc/article_attachments/6165115409175)

Localizado na parte superior direita da tela, o botão ![Imagem 8: Localizado na parte superior direita da tela, o botão "Excluir (F9)" permitirá a eliminação dos produtos inseridos…](https://ajuda.sankhya.com.br/hc/article_attachments/6165116782615) **"Excluir [F9]"** permitirá a eliminação dos produtos inseridos incorretamente ou que não farão mais parte do processo de contagem de estoque. Ao final, você visualiza no rodapé da tela, os botões ![Imagem 9: Localizado na parte superior direita da tela, o botão "Excluir (F9)" permitirá a eliminação dos produtos inseridos…](https://ajuda.sankhya.com.br/hc/article_attachments/6165135715607) **"[F6] Cancelar"** e ![Imagem 10: Localizado na parte superior direita da tela, o botão "Excluir (F9)" permitirá a eliminação dos produtos inseridos…](https://ajuda.sankhya.com.br/hc/article_attachments/6165166883351) **"[F7] Confirmar"**, sendo eles, responsáveis pelo cancelamento e conclusão do processo em questão, sendo que, o cancelamento de uma contagem não poderá ser desfeito e a sua conclusão comportará os dados acerca de todo o processo efetuado.

![Imagem 11: Localizado na parte superior direita da tela, o botão "Excluir (F9)" permitirá a eliminação dos produtos inseridos…](https://ajuda.sankhya.com.br/hc/article_attachments/6165198530455)

**Observação:** através deste relatório, será possível visualizar apenas a unidade padrão do produto. Caso seja necessário realizar o agrupamento das unidades principal e alternativa em apenas uma linha por produto no relatório, você deve, primeiramente, executar no módulo MGE Inventário > Avançado, a rotina **"Consolidação na Unidade Principal"**, rotina esta, não existente no Sankhya Om.

 
![Imagem 12: Atenção, Implantador: o sistema utiliza a seguinte sequência para busca do código de barras no sistema:](https://ajuda.sankhya.com.br/hc/article_attachments/16251768704919) **Atenção, Implantador:** o sistema utiliza a seguinte sequência para busca do código de barras no sistema:

- Primeiramente, o sistema verifica se existe estoque com o código de barras e o local;
- Não encontrando, busca na tabela TGFVOA (aba [Unidades Alternativas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaunidadesalternativas) do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)), se existe no volume alternativo e utiliza os dados desta tabela;
- Se não encontrar, busca na tabela TGFBAR (aba [Código de Barras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abacdigodebarras) do Cadastro de Produtos), se existe no código de barras e utiliza os dados desta tabela;
- Caso não encontre, busca na tabela TGFPRO (aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abageral) do Cadastro de Produtos), se existe no produto e utiliza os dados desta tabela.

Se nenhuma das condições anteriores forem satisfeitas, será apresentada a seguinte mensagem: 

**"Código de Barras inexistente".**

Nessas tabelas, pode existir mais de um registro com o mesmo código de barras; sendo este o caso, o sistema irá utilizar o primeiro registro encontrado.

Depois de salvar o registro, o sistema limpará a grade e, os dados nela incluídos, poderão ser vistos na tela [Contagem de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609694) ou através de relatórios.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609554-Contagem-de-Estoque-C%C3%B3d-barras#top)
