---
id: "4411588603159"
titulo: "Dashboard auxiliar do BLOCO K"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4411588603159-Dashboard-auxiliar-do-BLOCO-K"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Escriturações e Declarações   > EFD ICMS/IPI"
atualizado_em: "2026-09-30T11:16:21Z"
rotulos: ["Configuração", "Relatórios", "Fiscal", "EFD", "Estoque", "br.com.sankhya.mgeliv.nuDsb.auxiblocok", "BLOCO K", "k200", "k230", "k210", "k250", "k280", "EFD ICMS/IPI", "Filtros e Atualização", "Controle Bloco K", "Detalhes dos Registros"]
---

# Dashboard auxiliar do BLOCO K

| ``` ![Imagem 1: Módulo: Configurações>Controle de Acesso Remoto Versão disponível: A partir da 4.11](https://ajuda.sankhya.com.br/hc/article_attachments/42313173992471)Módulo: Configurações>Controle de Acesso Remoto ![Imagem 2: Módulo: Configurações>Controle de Acesso Remoto Versão disponível: A partir da 4.11](https://ajuda.sankhya.com.br/hc/article_attachments/42313157862935)Versão disponível: A partir da 4.11 ``` |
| --- |

---

Por meio desta tela, você pode realizar a conferência de forma detalhada das informações pertinentes a geração do Bloco K da EFD ICMS/IPI, por exemplo, a quantidade de produtos e insumos utilizados na produção, quais produtos foram produzidos, entre outras.

Inicialmente, é necessário informar no Painel de Filtros a **"Empresa"** e o **"Período"** dos registros que deseja visualizar. A **"Data inventário"** deve ser preenchida apenas para o registro K200 - Estoque Escriturado.

![Imagem 3: Inicialmente, é necessário informar no Painel de Filtros a "Empresa" e o "Período" dos registros que deseja visualizar.…](https://ajuda.sankhya.com.br/hc/article_attachments/4411589574167)

Ainda no Painel de Filtros, você pode definir qual o **"Status Ordem de Produção"** que serão exibidos os registros, conforme as seguintes marcações:

- Todas;
- OP Iniciadas e Concluídas no Período de Apuração;
- OP Iniciadas e não Concluídas no Período de Apuração;
- OP Iniciadas em Período Anterior e Concluídas no Período de Apuração;
- OP Iniciadas em Período Anterior e não Concluídas no Período de Apuração.

Com os filtros configurados, acione o botão **"Atualizar"**, assim, ao clicar em cada registro serão apresentadas as informações pertinentes a ele. Trataremos a seguir, sobre cada um:

[K200 - Estoque Escriturado](https://ajuda.sankhya.com.br/hc/pt-br/articles/4411588603159-Dashboard-auxiliar-do-BLOCO-K#K200-EstoqueEscriturado)

[K230 - Produção Própria - Itens Produzidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4411588603159-Dashboard-auxiliar-do-BLOCO-K#K230-Produ%C3%A7%C3%A3oPr%C3%B3pria-ItensProduzidos)

[K210 - Desmontagem de mercadoria - Item de Origem](https://ajuda.sankhya.com.br/hc/pt-br/articles/4411588603159-Dashboard-auxiliar-do-BLOCO-K#K210-Desmontagemdemercadoria-ItemdeOrigem)

[K250 - Industrialização efetuada por terceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/4411588603159-Dashboard-auxiliar-do-BLOCO-K#K250-Industrializa%C3%A7%C3%A3oefetuadaporterceiros)

[K280 - Correção de Apontamento - Estoque Escriturado](https://ajuda.sankhya.com.br/hc/pt-br/articles/4411588603159-Dashboard-auxiliar-do-BLOCO-K#K280-Corre%C3%A7%C3%A3odeApontamento-EstoqueEscriturado)

---

#### K200 - Estoque Escriturado

O registro K200- Estoque Escriturado apresenta o saldo em estoque de cada produto no último dia do período de apuração do Bloco K. Clicando em uma linha, serão apresentados no painel inferior os detalhes do registro K200 - Estoque escriturado - Detalhado por Posse.

[GIF animado: Imagem 4: O registro K200- Estoque Escriturado apresenta o saldo em estoque de cada produto no último dia do período de apuração…](https://ajuda.sankhya.com.br/hc/article_attachments/4411692795543)

Lembrando que este registro será gerado após a execução da Cópia e Contagem de estoque (Processo de inventário). Para isso, é necessário ligar o parâmetro **"GERAK200CTE"**, que habilitará na tela [EFD - Fiscal ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263), aba [Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263#abaconfigura%C3%A7%C3%B5es), o campo **"Data da contagem p/ K200"** onde você deverá informar a data da contagem. Caso o parâmetro esteja desligado, será considerado o estoque que consta no último dia da geração do SPED Fiscal da referência em questão. 

![Imagem 5: Lembrando que este registro será gerado após a execução da Cópia e Contagem de estoque (Processo de inventário). Para…](https://ajuda.sankhya.com.br/hc/article_attachments/4411604222103)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4411588603159-Dashboard-auxiliar-do-BLOCO-K#comosfiltros)

#### K230 - Produção Própria - Itens Produzidos

No painel superior serão apresentadas as informações do registro K230 - Produção Própria - Itens produzidos, isto é, os dados da produção acabada de um produto em processo e finalizado. Ao clicar sobre um registro, no painel inferior serão exibidos os detalhes do registro K235 - Produção Própria -Insumos consumidos referentes ao consumo do insumo (MP).

![Imagem 6: No painel superior serão apresentadas as informações do registro K230 - Produção Própria - Itens produzidos , isto é,…](https://ajuda.sankhya.com.br/hc/article_attachments/4411682198551)

**(1)** Ao clicar duas vezes sobre um registro o sistema irá direcioná-lo a tela Ordens de Produção - Nova, onde você poderá verificar as informações pertinentes ao registro indicado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4411588603159-Dashboard-auxiliar-do-BLOCO-K#comosfiltros)

#### K210 - Desmontagem de mercadoria - Item de Origem

Neste painel, temos os detalhes referentes ao registro K210 - Desmontagem de mercadorias - Item de origem, que tem o objetivo de escriturar a desmontagem de mercadorias dos tipos, por exemplo, matéria-prima, embalagem, entre outras. Ao clicar sobre um registro, no painel inferior serão apresentadas as informações relacionadas ao registro K215 - Desmontagem de mercadorias - Item de destino, que possui a finalidade de escriturar a desmontagem (com ou sem ordem de serviço) de mercadorias.

![Imagem 7: Neste painel, temos os detalhes referentes ao registro K210 - Desmontagem de mercadorias - Item de origem , que tem o…](https://ajuda.sankhya.com.br/hc/article_attachments/4411688261015)

**(1)** Ao clicar duas vezes sobre um registro o sistema irá direcioná-lo a tela Ordens de Produção - Nova, onde você poderá verificar as informações pertinentes ao registro indicado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4411588603159-Dashboard-auxiliar-do-BLOCO-K#comosfiltros)

#### K250 - Industrialização efetuada por terceiros

No painel superior serão exibidas as informações do registro K250 - Industrialização efetuada por terceiros - itens produzidos, isto é, os produtos que foram industrializados por terceiros e sua respectiva quantidade. Ao clicar sobre um registro, no painel inferior temos os dados detalhados do registro K255 - Industrialização efetuada por terceiros - itens consumidos.

![Imagem 8: No painel superior serão exibidas as informações do registro K250 - Industrialização efetuada por terceiros - itens…](https://ajuda.sankhya.com.br/hc/article_attachments/4411688304791)

**(1)** Ao clicar duas vezes sobre um registro o sistema irá direcioná-lo a tela Ordens de Produção - Nova, onde você poderá verificar as informações pertinentes ao registro indicado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4411588603159-Dashboard-auxiliar-do-BLOCO-K#comosfiltros)

#### K280 - Correção de Apontamento - Estoque Escriturado

Neste painel, temos os detalhes do registro K280 - Correção de Estoque Escriturado, que tem o objetivo de escriturar a correção de apontamento do Registro K200.

![Imagem 9: Clicando duas vezes sobre um registro o sistema irá direcioná-lo a Central de Vendas , exibindo a nota que foi…](https://ajuda.sankhya.com.br/hc/article_attachments/4411688455703)
**(1)** Clicando duas vezes sobre um registro o sistema irá direcioná-lo a [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414), exibindo a nota que foi realizado o ajuste.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4411588603159-Dashboard-auxiliar-do-BLOCO-K#comosfiltros)
