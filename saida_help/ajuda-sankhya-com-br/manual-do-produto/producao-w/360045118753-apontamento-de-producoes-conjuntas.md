---
id: "360045118753"
titulo: "Apontamento de Produções Conjuntas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118753-Apontamento-de-Produ%C3%A7%C3%B5es-Conjuntas"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-29T14:54:41Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "Rateio", "Matéria-Prima", "Ordem de Produção", "Produção", "br.com.sankhya.prod.apontamentoproducaoconjunta", "Apontamento de Produções Conjuntas manual", "Vários produtos de mesma matéria-prima", "Rateio de materiais entre Produções", "Incluir Confirmar Transferir Visualizar Novo"]
---

# Apontamento de Produções Conjuntas

```
 Módulo: Produção > Rotinas
```

---

Em muitas empresas de Produção Contínua, existe o fenômeno denominado de Produção Conjunta, que é o aparecimento de diversos produtos a partir da mesma matéria-prima, como é o caso do tratamento industrial contendo quase todos os produtos naturais na agroindústria. Trouxemos alguns exemplos:

- **Soja:** óleos, farelos;
- **Boi:** ossos, diferentes tipos de carnes;
- **Petróleo:** gasolina, querosene, emulsão asfáltica;
- **Frango:** peito, coxa, coração;
- **Leite cru:** leite padronizado, cremes.

Os produtos gerados a partir da Produção Conjunta, são normalmente nomeados de Co produtos, sendo que, esses produtos são sempre de fabricação principal da Indústria. Como os Co produtos consomem a mesma matéria-prima, existe a necessidade, muitas vezes, de se ratear o consumo das matérias-primas entre os PAs fabricados.

Esta tela tem o objetivo de permitir o rateio de um apontamento de materiais de uma Produção Conjunta.

![Imagem 1: Esta tela tem o objetivo de permitir o rateio de um apontamento de materiais de uma Produção Conjunta .](https://ajuda.sankhya.com.br/hc/article_attachments/4416790792855)

O processo se dá início com a inserção da OP a qual se deseja realizar o apontamento. Através do botão ![incluir](https://ajuda.sankhya.com.br/hc/article_attachments/15524672665239) **"Incluir OP"**, teremos a exibição do pop-up **"Incluir Ordem de Produção (OP)"** que permitirá a referida inserção:

![Imagem 3: O processo se dá início com a inserção da OP a qual se deseja realizar o apontamento. Através do botão "Incluir OP" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/4416790962839)

Ao definir a OP e concluir a sua inserção, caso exista mais de uma instância da atividade que esteja Em Andamento, a coluna **"Atividade"** será exibida para que seja indicada qual instância da atividade será incluída.

Ao finalizar a inclusão da OP/PA, serão adicionadas, automaticamente, as MPs conforme a Lista de MPs para o PA; se o material já existir entre as matérias-primas selecionadas, este não será incluído novamente, ou seja, não haverá duas MPs na grade.

> **Importante**: para casos em que o Operador de Produção **não pode visualizar as matérias primas devido ao sigilo** na composição do produto final, é possível configurar o sistema para inibir a visualização das MPs através da configuração "**Inibe acesso à matéria prima"** da aba **Segurança do cadastro de Usuários**.

![Imagem 4: Importante : para casos em que o Operador de Produção não pode visualizar as matérias primas devido ao sigilo na…](https://ajuda.sankhya.com.br/hc/article_attachments/4416784462743)

**Observação:** o parâmetro **"Permitir definir produto como MP de si próprio. - PRODMPPROP"** quando habilitado, possibilitará que um produto seja apontado como Matéria-prima de um apontamento, quando este produto for o próprio Produto Acabado do apontamento.

Ao lado superior esquerdo da tela, temos os botões ![mais](https://ajuda.sankhya.com.br/hc/article_attachments/15524743489687) **"Incluir MP"** e **"Remover MP"**, respectivamente. Através deles você realiza a inclusão/exclusão de matérias-primas que façam parte da lista de MPs da grade de OP/PA.

![Imagem 6: Ao lado superior esquerdo da tela, temos os botões "Incluir MP" e "Remover MP" , respectivamente. Através deles você…](https://ajuda.sankhya.com.br/hc/article_attachments/4416791314327)

Utilizando o botão ![Imagem 7: Utilizando o botão "Resultado" , você poderá visualizar o "Resultado do Rateio de Apontamento" para cada MP selecionada…](https://ajuda.sankhya.com.br/hc/article_attachments/15524743496983) **"Resultado"**, você poderá visualizar o **"Resultado do Rateio de Apontamento"** para cada MP selecionada na grade. Sendo que, o rateio é proporcional à quantidade produzida em cada Ordem de Produção, sendo calculado da seguinte maneira:

```
Índice = Qtd. Mistura * Qtd Apontada na OP/ ? (Qtd. Mistura * Qtd. Apontada na OP)
Qtd. Apontada = Qtd. Apontada da MP * Índice
? = Somatória
```

Após realizar todas as inclusões necessárias, por meio do botão ![Imagem 8: Após realizar todas as inclusões necessárias, por meio do botão "Confirmar" teremos a solicitação da inserção do rateio…](https://ajuda.sankhya.com.br/hc/article_attachments/15524781512087) **"Confirmar"** teremos a solicitação da inserção do rateio do apontamento. Para tanto, será apresentada a seguinte mensagem de confirmação deste procedimento:

**"Será inserido e confirmado um apontamento para cada OP/PA/Atividade. Deseja continuar?".**

Após a confirmação, será exibido o pop-up **"Apontamento confirmado!"** contendo as opções **"Transferência Parcial"**, **"Finalizar Atividades"**, **"Visualizar OP"** e **"Novo Apontamento"**, bem como, em seu rodapé, os números dos apontamentos que foram criados.

![Imagem 9: Após a confirmação, será exibido o pop-up "Apontamento confirmado!" contendo as opções " Transferência Parcial" , "…](https://ajuda.sankhya.com.br/hc/article_attachments/4416871010583)

Abaixo temos a descrição e funcionalidade de cada uma destas opções:

**Transferência Parcial**

Esta opção permite realizar a transferência parcial das OPs selecionadas, sendo que, a coluna **"Saldo a Transferir"** estará disponível para alteração.

![Imagem 10: Esta opção permite realizar a transferência parcial das OPs selecionadas, sendo que, a coluna " Saldo a Transferir"…](https://ajuda.sankhya.com.br/hc/article_attachments/4416871174423)

Ao confirmar a(s) transferência(s), todos os registros transferidos terão as colunas **"Quantidades Apontadas"**, **"Quantidade Transferidas"** e Saldo a Transferir atualizadas.

Quando o campo **"Quantidade base para apontamento"** da aba [Apontamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058460853-Configura%C3%A7%C3%A3o-de-Atividades-Nova#abaapontamento) estiver configurado com a opção **"Não sugere"**, a coluna **"Qtd. apontada"** do PA será exibida com o valor igual a zero, dessa forma, o apontamento só será confirmado após a alteração desse valor. Caso o referido campo esteja com a opção **"Qtd. apontada de PA"** selecionada, o apontamento poderá ser confirmado sem a necessidade de editar o valor apresentado na coluna. 

Caso nenhuma atividade se encontre configurada para executar a transferência, esta opção ficará desabilitada.

**Finalizar Atividades**

Através desta opção, você realiza o encerramento da atividade a qual foi realizado o apontamento.

![Imagem 11: Através desta opção, você realiza o encerramento d a atividade a qual foi realizado o apontamento .](https://ajuda.sankhya.com.br/hc/article_attachments/4416871127319)

**Visualizar OP**

Por meio desta opção, será aberta a tela [Ordens de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119313) posicionada na OP selecionada, possibilitando assim, a sua visualização.

![Imagem 12: Por meio desta opção, será aberta a tela Ordens de Produção posicionada na OP selecionada, possibilitando assim, a sua…](https://ajuda.sankhya.com.br/hc/article_attachments/4416854960023)

**Novo Apontamento**

Esta opção possibilita o lançamento de um novo apontamento, ou seja, retorna para a tela inicial.

**Nota:** na tela de [Lançamento de Ordem de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599554), podemos alterar a Qtd. de Co-produto; sendo este uma Produção Conjunta, surgirá um pop-up para a edição. Porém, na edição deste, irá constar a marcação **"Seq. Produção Conjunta e Reproporcionar qtd. entre Co-produções"**. Quando habilitada, as OPs de lançamento serão ajustadas de acordo com a quantidade de processamento (Un. padrão). Quando esta não for habilitada, somente a quantidade de processamento (Un. padrão) será alterada, sendo que, irá como sugestão para a quantidade da MP para esta tela e não será ajustado para as OPs do lançamento.

**Observação:** a Produção Conjunta deverá especificar o Nro da OP conjunta e todas as OPs que compõem a produção conjunta serão incluídas no apontamento. Quanto à Ordem de Produção, esta deverá especificar individualmente o Nro das OPs que compõem a OP conjunta no apontamento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118753-Apontamento-de-Produ%C3%A7%C3%B5es-Conjuntas#top)
