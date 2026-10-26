---
id: "39379027883031"
titulo: "Como configurar a exibição e edição de colunas na aba \"Itens\" da Central de Vendas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39379027883031-Como-configurar-a-exibi%C3%A7%C3%A3o-e-edi%C3%A7%C3%A3o-de-colunas-na-aba-Itens-da-Central-de-Vendas"
trilha: "Melhores Práticas > Configurações"
atualizado_em: "2026-07-29T02:27:54Z"
rotulos: ["Produtos", "Configuração", "Fiscal", "Modo Edição", "Central de Vendas", "Artigo criado KCS", "CVE - KCS"]
---

# Como configurar a exibição e edição de colunas na aba "Itens" da Central de Vendas

Na **Central de Vendas**, você pode visualizar e editar os produtos ou serviços de um documento de duas maneiras no painel de Itens: no **Modo Grade** (em formato de tabela) ou no **Modo Formulário** (ficha detalhada de um único item).

Para visualizar ou editar informações específicas, o campo precisa estar habilitado no modo de visualização que você está utilizando. Veja como configurar cada um:

### Configurar colunas no Modo Grade

O Modo Grade é ideal para editar vários itens de forma rápida.

1. Abra um documento na **Central de Vendas**.
2. No painel de **Itens**, certifique-se de estar na visualização em grade.
3. Ao lado do botão de Incluir Item, temos uma opção com nome "**Configuração da Grade**"
4. Insira no painel "**Colunas Selecionadas**", os campos que deseja que fiquem visíveis no modo grade.
5. Clique em **Aplicar** ou **Salvar**. A tabela será atualizada imediatamente.

### Configurar campos no Modo Formulário

O Modo Formulário é útil para visualizar todos os detalhes de um único item em uma tela mais limpa.

1. Abra um documento na **Central de Vendas**.
2. Acesse a opção **Configurar Formulário** (disponível no menu superior do painel com ícone de engrenagem).
3. Insira no painel "**Colunas Selecionadas**", os campos que deseja que fiquem visíveis no modo grade.
4. Clique em **Aplicar** ou **Salvar**. O formulário agora exibirá os novos campos para preenchimento.

### Modo Grade e Formulário Juntos (Tela Dividida)

Esta opção é ideal para quem deseja a agilidade da grade junto com o detalhamento do formulário ao mesmo tempo.

1. Abra um documento na **Central de Vendas**.
2. A tela será dividida: uma área listará todos os itens (Grade) e a outra mostrará os detalhes do item selecionado (Formulário).
3. Atenção: Os campos exibidos em cada área respeitam as configurações feitas individualmente nos passos 1 e 2 acima.

### Parâmetros que afetam a pesquisa e exibição de Códigos/Referências

A forma como o sistema busca e exibe o código ou referências dos produtos na tela de Itens é controlada por dois parâmetros principais:

**CODPROREF:** (Código e/ou referência nos itens?): Quando configurado com a opção "Referência", ele habilita a opção de pesquisar os produtos no lançamento utilizando seus respectivas referencias. Diferente disso, será apresentado o campo "Código".

**MOSTRARQUALREF:** (Mostrar qual o tipo de referência): Sua ativação é obrigatória sempre que o parâmetro CODPROREF estiver definido como "Referência". É ele quem determina se a grade de itens exibirá apenas a Referência do Produto, apenas a Referência do Fornecedor, ou ambas.
