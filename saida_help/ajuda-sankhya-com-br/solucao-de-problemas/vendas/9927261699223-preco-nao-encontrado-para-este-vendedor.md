---
id: "9927261699223"
titulo: "Preço não encontrado para este Vendedor/Tipo de Negociação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9927261699223-Pre%C3%A7o-n%C3%A3o-encontrado-para-este-Vendedor-Tipo-de-Negocia%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:05:22Z"
rotulos: ["Produtos", "Configuração", "Vendedor", "TOP", "Preferências", "CORE_E03247", "TOP não recalcula preço ao duplicar pedido", "Preço não encontrado", "Marque 'Recalcular preço' e ajuste 'Atualiza preço'", "Erro"]
---

# Preço não encontrado para este Vendedor/Tipo de Negociação

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19572139532951) MENSAGEM:**

[CORE\_E03247] Preço não encontrado para este Vendedor/Tipo de Negociação.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19572139534743) SITUAÇÃO:**

Ao duplicar um pedido de venda a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19572139535255) CAUSA:**

Ocorre quando a TOP não está com o campo 'Recalcular preço prod. ao faturar' selecionado e o pedido é duplicado.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19572146758551) SOLUÇÃO:**

Acesse o parâmetro '**TIPTABPRECOS - Tabela de preço por',** na tela **Preferências** (Caminho de acesso à tela: Configurações » Avançado » Preferências), e observe se no campo 'Valor' está marcada a opção 'Tipo de Negoc./Vendedor'.

![Imagem 5: Acesse o parâmetro ' TIPTABPRECOS - Tabela de preço por', na tela Preferências (Caminho de acesso à tela: Configurações…](https://ajuda.sankhya.com.br/hc/article_attachments/19572139539479)

Caso deseje verificar todas as opções disponíveis para o parâmetro basta acessar o link abaixo:

[Parâmetro TIPTABPRECOS - Quais as opções disponíveis para definição do controle das tabelas de preço ? – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053496574-Par%C3%A2metro-TIPTABPRECOS-Quais-as-op%C3%A7%C3%B5es-dispon%C3%ADveis-para-defini%C3%A7%C3%A3o-do-controle-das-tabelas-de-pre%C3%A7o-)

Em seguida, acesse a tela da **TOP** em questão e marque o campo 'Recalcular preço prod. ao faturar' . Por fim, realize o teste marcando o campo 'Atualiza preço' no momento de duplicar.

![Imagem 6: Em seguida, acesse a tela da TOP em questão e marque o campo 'Recalcular preço prod. ao faturar' . Por fim, realize o…](https://ajuda.sankhya.com.br/hc/article_attachments/19572146761879)

Caso a TOP esteja com a marcação **"Recalcular preço prod. ao faturar"** assinalada, ao faturar um pedido, o sistema buscará o último preço do produto em vigor; se desmarcada, será utilizado o preço aplicado no pedido faturado.

Defina no campo **"Usar como Preço"** qual o valor a ser atribuído aos itens lançados na central; o preço utilizado para o produto, dentre as seguintes opções:

- Valor Líquido da origem;
- Último Custo Médio Gerencial;
- Preço em Moeda;
- Último Custo Médio Sem ICMS;
- Último Custo de Entrada Com ICMS;
- Último Custo Variável;
- Último Custo Gerencial;
- Último Custo de Reposição;
- Preço de Venda;
- Nenhum;
- Último Custo Médio Com ICMS;
- Último Custo de Entrada Sem ICMS;
- Média das notas de origem.
