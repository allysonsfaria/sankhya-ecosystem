---
id: "44011061915671"
titulo: "&nbsp;Cálculo de Comissão do Marketplace por Categoria na Precificação Automática Mercado Livre"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011061915671--nbsp-C%C3%A1lculo-de-Comiss%C3%A3o-do-Marketplace-por-Categoria-na-Precifica%C3%A7%C3%A3o-Autom%C3%A1tica-Mercado-Livre"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T18:53:39Z"
rotulos: ["sync_hc", "magis5", "magis5_218698437402", "sync_hash_1136c8184975"]
---

# &nbsp;Cálculo de Comissão do Marketplace por Categoria na Precificação Automática Mercado Livre

## Neste guia, você entenderá o novo cálculo da comissão do marketplace por categoria de produto, utilizando a precificação automática para o Mercado Livre

---

Esta atualização aprimora o sistema de precificação automática do **Magis5**. Agora, o cálculo da comissão do marketplace pode considerar, além do tipo de anúncio **(como Clássico ou Premium)**, a **categoria específica** do produto.

Com isso, a precificação torna-se mais precisa, refletindo com maior fidelidade os custos da operação. Isso reduz a dependência de margens genéricas, contribui para a definição de preços mais competitivos e ajuda a preservar a rentabilidade das vendas..

### Realizando a configuração no Magis5

O comportamento do Magis5 varia conforme o status da configuração, para isso acesse a opção **"Configurações", "Integrações"** e por fim **"Marketplace"**

![Imagem 1: O comportamento do Magis5 varia conforme o status da configuração, para isso acesse a opção "Configurações",…](https://ajuda.sankhya.com.br/hc/article_attachments/44011035219735)

Edite o canal de venda em que deseje realizar a configuração e acesse a aba **"Margens e Custos"**e habilite a opção **"habilitar comissão por categoria"**

![Imagem 2: Edite o canal de venda em que deseje realizar a configuração e acesse a aba "Margens e Custos" e habilite a opção…](https://ajuda.sankhya.com.br/hc/article_attachments/44011035351063)

Ao **habilitar** a opção **"Habilitar comissão por categoria"**, o Magis5 passa a realizar uma busca inteligente da taxa de comissão, considerando a combinação entre o tipo de anúncio e a categoria do produto.
Dessa forma, a taxa específica para aquela combinação é identificada e utilizada no recálculo do preço de venda, aplicando a nova regra de comissão. 

Quando a opção está **desabilitada** (configuração padrão), o sistema mantém o funcionamento atual, calculando a comissão com base apenas na taxa vinculada ao tipo de anúncio, sem considerar a categoria do produto.

### Como funciona o recálculo

O recálculo do preço de venda ocorre automaticamente nos seguintes cenários:

- Quando um novo rascunho de anúncio é criado com uma categoria já definida.
- Quando uma categoria é adicionada ou alterada em um rascunho de anúncio existente.

Nesses momentos, o sistema realiza o recálculo da comissão e atualiza imediatamente o preço de venda do produto no rascunho.

![Imagem 3: Nesses momentos, o sistema realiza o recálculo da comissão e atualiza imediatamente o preço de venda do produto no…](https://ajuda.sankhya.com.br/hc/article_attachments/44011076379415)

**Alterações em outros campos do anúncio não acionam automaticamente o recálculo da comissão.**

### Composição do preço de venda

O preço final do produto é calculado considerando todos os componentes que influenciam sua formação:

**Preço de venda = Custo do produto + Custo de operação + Comissão do marketplace + Margem do produto + Regras de faixas de preço**

Com a funcionalidade de busca inteligente habilitada, o cálculo da comissão do marketplace passa a utilizar a taxa identificada pela combinação entre o tipo de anúncio e a categoria do produto, garantindo maior precisão na formação do preço de venda.

💡Caso o marketplace altere sua **árvore de categorias** e a categoria vinculada ao rascunho deixe de possuir uma regra de comissão válida, o cálculo da comissão poderá apresentar erro.

Para corrigir a situação, será necessário acessar as especificações do produto na Magis5, revisar a categoria vinculada, **realizar o mapeamento novamente para uma categoria válida e atualizada e salvar as alterações**.

Após a atualização da categoria, o sistema poderá realizar novamente o recálculo da comissão.

### Boas práticas

Para garantir que o cálculo de comissão seja realizado corretamente, mantenha as categorias dos produtos sempre atualizadas e revise os mapeamentos sempre que houver alterações na estrutura de categorias do marketplace.

A utilização da busca inteligente de taxa permite obter cálculos de comissão mais precisos, alinhados às regras atuais do marketplace e garantindo maior assertividade na formação do preço de venda.

- **Por que meu preço final sugerido aumentou ou diminuiu após ativar essa opção?**

Isso acontece porque o sistema passa a consultar a tabela de taxas específicas do marketplace para a categoria do produto, tornando o cálculo da comissão mais preciso.
Em muitos marketplaces, produtos de categorias diferentes possuem taxas de comissão distintas, mesmo quando utilizam o mesmo tipo de anúncio. Por exemplo, a comissão de um anúncio de **"Camiseta"** pode ser diferente da comissão de um anúncio de **"Micro-ondas"**, ainda que ambos sejam classificados como Anúncios Premium.

- **Essa alteração afeta meus anúncios que já estão publicados?**

**Não imediatamente.** O recálculo da comissão ocorre apenas nos momentos definidos pela funcionalidade: quando um novo rascunho de anúncio é criado com uma categoria definida ou quando a categoria de um rascunho existente é adicionada ou alterada.

- **Sou obrigado a utilizar essa funcionalidade?**

**Não**. A funcionalidade vem desabilitada por padrão. Caso prefira continuar utilizando uma taxa de comissão genérica vinculada apenas ao tipo de anúncio, basta manter a configuração desativada.
