---
id: "360045118913"
titulo: "Etapas de Produção"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118913-Etapas-de-Produ%C3%A7%C3%A3o"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:33:02Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "WMS", "Parceiro", "CONTRLAUDOAMOST", "TOP", "Estoque", "Produção", "Etapas de Produção", "Fórmula de Composição", "Fórmula de Produção", "INTEGRAWMSPROD", "Laudo de análise", "Local de Destino", "Local de Origem", "Pedente de confirmação", "Requisição", "TOP de entrada", "TOP de saída", "br.com.sankhya.etapasdeproducao", "Etapas de Produção manual", "Gerenciamento de Matérias Primas", "Formulação de Processos"]
---

# Etapas de Produção

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312116743703) Módulo: Comercial > Arquivo > Cadastros 
```

---

Nesta tela, cadastramos as etapas que irão compor os processos produtivos na empresa. Essas etapas organizarão a **"Fórmula de Produção"**. Trouxemos um exemplo:

Na confecção de uma camisa, temos uma etapa de corte, uma de costura, outra de embalagem. Cada etapa utilizará matérias primas específicas, o que possibilita ao gestor disponibilizar estas matérias à medida que forem sendo necessárias.

As TOP's aqui configuradas, gerarão notas para as Matérias Primas utilizadas na etapa. Estas TOP's marcarão a **"Entrada"** e a **"Saída"** do produto em cada Etapa de Produção e poderão atualizar ou não o estoque das MPs, de acordo com a definição que você realizar. Por exemplo:

Na confecção de camisas, onde as TOP's de Entrada e Saída foram configuradas para atualizar o estoque, dando baixa nas Matérias Primas e, posteriormente, entrada no Produto Acabado, da seguinte maneira:

- Para a etapa de corte, configuramos a **"TOP de Entrada"** para baixar o estoque da MP: tecido.
- Para a etapa costura, configuramos a **"TOP de Entrada"** para baixar o estoque das MP's: linhas e botões.
- Para a etapa embalagem, a **"TOP de Saída"** foi configurada para dar entrada ao produto acabado, no estoque.

[Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118913-Etapas-de-Produ%C3%A7%C3%A3o#abageral)                                                                  [Aba Observação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118913-Etapas-de-Produ%C3%A7%C3%A3o#abaobserva%C3%A7%C3%A3o)

[Aba Locais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118913-Etapas-de-Produ%C3%A7%C3%A3o#abalocais)

![Imagem 2: Aba Locais](https://ajuda.sankhya.com.br/hc/article_attachments/1500000330242)

## Aba Geral

O campo **"Cód. Centro de Resultado"** terá a informação utilizada quando o **"Tipo de Movimento"** de uma das TOP's informadas for **"Requisição"**.

As configurações complementares da etapa serão informadas no campo **"Tipo"**; aqui, você informada se a referida será realizada internamente ou por terceiros.

Se o tipo **"Laudo de análise"** estiver selecionado e a TOP de transferência exigir laudo, o sistema não permitirá transferir de etapa de produção sem lançar o laudo ou com laudo padrão zero.

Nos campos **"TOP de Entrada"** e **"TOP de Saída"** informamos as TOP's que gerarão notas com as MPs da etapa, para entrada ou saída das mesmas.

A marcação **"A nota fica pendente de confirmação"** deve ser selecionada caso você queira que a nota de entrada ou de saída não seja confirmada automaticamente.

**Nota:** Existem dois campos com esse nome, um para notas de entrada, outro para notas de saída e eles ficam sempre logo abaixo do campo da sua TOP (de Entrada ou de Saída).

Quando o campo **"TOP de produção"** estiver preenchido em uma etapa, ao fazer a transferência de etapas saindo desta etapa, a TOP da produção será alterada, automaticamente, para a TOP informada no campo TOP de produção.

Ao fazer movimentações com Matérias Primas na entrada ou saída de uma etapa, o sistema usará as Matérias Primas configuradas na tela [Fórmula de Composição do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025390173-F%C3%B3rmula-de-Composi%C3%A7%C3%A3o-do-Produto) para a etapa em questão. Quando o campo **"Etapa p/Seleção de MPs"** estiver preenchido, o sistema utilizará as Matérias Primas da etapa informada neste campo.

Os campos **"Origem Parceiro Entrada"** e **"Origem Parceiro Saída"** serão habilitados pelo parâmetro **"Utiliza planejamento Produção por Estoque mínimo? - USAPLAPROESTMIN"**.

Além disso, para o campo ficar habilitado, no cadastro de Etapas de Produção, a etapa tem que estar marcada como **"Etapa de Terceiros"** (Tipo = Terceiros), e o campo de sua respectiva TOP preenchido, assim, os campos de Origem Parceiro terão três opções com suas aplicações:

- O Local da Produção utilizará o Parceiro informado no Cadastro de **"Local"** do Produto Acabado;
- Local de Origem;
- Local de Destino.

Cada um destes locais terá a seguinte função:

- **Local da Produção:** Usará o parceiro informado no cadastro do Local do Produto Acabado.
- **Local de Origem:** Este utilizará o parceiro informado no cadastro do Local de Origem, que foi informado na Etapa.
- **Local de Destino:** Usará o parceiro informado no cadastro do Local de Destino, que foi informado na Etapa.

O campo **"Gerar Amostras"** será habilitado por meio do parâmetro **"Controle de laudo de amostra? - CONTRLAUDOAMOST"**. Conforme a opção escolhida neste campo, serão geradas amostras para os produtos (PA's) que usarem Status de Lote.

Com a marcação **"Verifica pendência no WMS na Saída da Etapa"** realizada, o sistema não permitirá sair da etapa de produção se existir alguma pendência (tarefa em andamento) no WMS. O campo é visível apenas se você possuir o opcional WMS e o parâmetro **"Utiliza Integração da Produção x WMS - INTEGRAWMSPROD"** estiver ligado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118913-Etapas-de-Produ%C3%A7%C3%A3o#top)

## Aba Observação

Esta aba contém um campo que será utilizado para relatar observações pertinentes à etapa que será cadastrada.

![Imagem 3: Esta aba contém um campo que será utilizado para relatar observações pertinentes à etapa que será cadastrada.](https://ajuda.sankhya.com.br/hc/article_attachments/1500000342801)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118913-Etapas-de-Produ%C3%A7%C3%A3o#top)

## Aba Locais

![Imagem 4: Aba Locais](https://ajuda.sankhya.com.br/hc/article_attachments/1500000330362)

Os campos **"Local Entrada Origem"**, **"Local Entrada Destino"**, **"Local Saída Origem"** e **"Local Saída Destino"** são utilizados para definição da origem e destino para TOP's de **"Entrada"** e **"Saída"**, quando o campo **"Tipo"** for marcado como **"Local"**.

Estes locais serão utilizados na transferência entre etapas; os locais não preenchidos serão solicitados no momento da transferência.

As marcações **"Usar Local Entrada Destino da Produção"**, **"Usar Local Entrada Origem da Produção"**, **"Usar Local Saída Destino da Produção"**, **"Usar Local Saída Origem da Produção"**, o sistema usará os locais informados na própria produção para o Produto Acabado (PA) e para as Matérias Primas (PA).

Lembre-se que o botão ![Imagem 5: Lembre-se que o botão "Edição múltipla" permite a edição simultânea de vários registros a partir do modo grade. Ou…](https://ajuda.sankhya.com.br/hc/article_attachments/16241420047767) **"Edição múltipla"** permite a edição simultânea de vários registros a partir do modo grade. Ou seja, ao selecionar um conjunto de registros e clicar no botão, será possível editar os campos correspondentes de todos os registros de uma só vez. 

Por exemplo, com as etapas de produção em modo grade na tela Etapas de Produção selecione-as e em seguida clique no botão Edição múltipla, assim os campos de todas as abas poderão ser editados simultaneamente para as etapas selecionadas. 

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118913-Etapas-de-Produ%C3%A7%C3%A3o#top)

##
