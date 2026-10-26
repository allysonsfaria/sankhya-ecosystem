---
id: "360044596974"
titulo: "Atualização de Estoque Mínimo e Máximo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596974-Atualiza%C3%A7%C3%A3o-de-Estoque-M%C3%ADnimo-e-M%C3%A1ximo"
trilha: "Manual do Produto > Suprimentos e Estoque > Compras e Estoque"
atualizado_em: "2026-09-15T12:46:39Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "Relatórios", "UTILIZACONTROLE", "UTILIZALOCAL", "Estoque Mínimo", "Análise de Giro", "Atualização", "Controle", "Local", "Atualização de Estoque Mínimo e Máximo", "Controle Adicional", "br.com.sankhya.com.mov.atualizacaoestoqueminmax", "Atualização de Estoque Mínimo e Máximo manual", "Estoque", "Estoque Máximo", "Comercial"]
---

# Atualização de Estoque Mínimo e Máximo

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42311758669079) Módulo: Comercial > Rotinas
```

---

Esta tela é utilizada para a atualização dos estoques mínimos e máximos dos produtos. O estoque mínimo gera a necessidade de compra e o estoque máximo limita a quantidade a ser adquirida para o produto.

Esta rotina possui filtros laterais, grade com itens do estoque, formulário de alteração, botões para salvar/rejeitar as modificações, campo para busca rápida na grade (busca pelo código do produto ou pela descrição) e botões de navegação.

![Imagem 2: Esta rotina possui filtros laterais, grade com itens do estoque, formulário de alteração, botões para salvar/rejeitar…](https://ajuda.sankhya.com.br/hc/article_attachments/21680091116055)

É possível alterar os estoques mínimos e máximos dos itens, tanto com a tela em modo grade, quanto em modo formulário de alteração, apresentada através do duplo clique sobre a linha do produto:

![Imagem 3: É possível alterar os estoques mínimos e máximos dos itens, tanto com a tela em modo grade, quanto em modo formulário…](https://ajuda.sankhya.com.br/hc/article_attachments/21680237354647)

Os botões **"Confirmar"** e **"Rejeitar"** ficam habilitados somente quando existe alguma alteração pendente a ser salva.

**Nota:** as alterações só são de fato salvas no banco de dados, após clicar no botão Confirmar. Ao rejeitar as alterações, nenhuma informação é modificada.

Ainda é possível inserir um novo item no estoque (tabela TGFEST); ao clicar no botão  **"Cadastrar Estoque"** da barra de controle da grade, o novo item é inserido com estoque zero.

Ao inserir um item, os campos **"Estoque"**, **"Reservado"**, **"Cód. De Barras"** e a marcação **"Ativo"** não serão passíveis de alteração e, por isso, apresentam-se desabilitados.

**Importante:** não existe estoque mínimo e estoque máximo de terceiros, somente próprio. Sendo assim, o campo CODPARC (PK da TGFEST) não é visível e é inserido como 0 (por default).

### Observações importantes com relação ao campo LOCAL e CONTROLE

O campo **"Local"**, se visível no formulário de alteração e grade, fica desabilitado para produtos cuja marcação **"Usa local"** localizado no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Medidas e estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abamedidaseestoque), sub-aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#sub-abaestoque) esteja desabilitada.

![Imagem 4: O campo "Local" , se visível no formulário de alteração e grade, fica desabilitado para produtos cuja marcação "Usa…](https://ajuda.sankhya.com.br/hc/article_attachments/22401151674007)

**Observação:** por padrão, o produto inserido receberá local 0, mesmo se este não utilizar local.

Já o campo **"Controle"**, se visível no formulário de alteração e grade, poderá mudar dependendo do Tipo do Controle especificado para aquele produto. O texto de apresentação da coluna/campo, também poderá mudar conforme o título do controle especificado para o produto.

![Imagem 5: Já o campo "Controle" , se visível no formulário de alteração e grade, poderá mudar dependendo do Tipo do Controle…](https://ajuda.sankhya.com.br/hc/article_attachments/22401415104279)

![Imagem 6: Para mais informações sobre controle adicional de estoque, acesse o Cadastro de Produtos .](https://ajuda.sankhya.com.br/hc/article_attachments/23367927629847) Para mais informações sobre controle adicional de estoque, acesse o [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-).

### Parâmetros que influenciam nesta rotina

**Utiliza a coluna Local para controlar o estoque - UTILIZALOCAL:** quando habilitado, deixará o campo Local no formulário de alteração e a coluna Local na grade visíveis na tela.

**Utiliza a coluna Controle para controlar o estoque - UTILIZACONTROLE:** habilitará o campo e a coluna Controle. Deixa o campo Controle (no formulário de alteração) e a coluna Controle (na grade) visíveis na tela.

### Outras Telas ou funcionalidades afetadas

Os campos **"Estoque Mínimo"** e **"Estoque Máximo"** são utilizados para relatórios de [Análise de Giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106673), gerando uma necessidade de compra ao atingir o estoque mínimo e restringindo. Os parâmetros UTILIZALOCAL e UTILIZACONTROLE afetam outras telas do sistema, mas que não influenciam diretamente nesta rotina.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596974-Atualiza%C3%A7%C3%A3o-de-Estoque-M%C3%ADnimo-e-M%C3%A1ximo#top)
