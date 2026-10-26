---
id: "39375098378903"
titulo: "Por que itens aparecem com preço zerado em requisições configuradas para usar custo?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39375098378903-Por-que-itens-aparecem-com-pre%C3%A7o-zerado-em-requisi%C3%A7%C3%B5es-configuradas-para-usar-custo"
trilha: "Melhores Práticas > Compras e Estoque"
atualizado_em: "2026-08-25T03:28:25Z"
rotulos: ["Produtos", "Custos", "Configuração", "Requisições", "TOP", "Artigo criado KCS", "CVE - KCS"]
---

# Por que itens aparecem com preço zerado em requisições configuradas para usar custo?

### Por que o preço aparece zerado ao incluir itens em uma requisição?

Em requisições, o preço do item não é digitado, ele é calculado automaticamente a partir do custo do produto, conforme a configuração da Tipo de Operação (TOP) usada. Se esse cálculo não encontra um custo válido, o preço fica zerado.

**Como o sistema calcula esse preço**

### Como o sistema calcula esse preço

O cálculo depende do campo **Usar como Preço** (USARPRECOCUSTO), configurado em Comercial > Cadastros > Tipos de Operação. Somente as opções abaixo buscam o custo do produto (as demais, como "Preço de Venda" ou "Preço em Moeda", não são afetadas por este problema):

- Último Custo Médio Com ICMS (M)
- Último Custo Gerencial (L)
- Último Custo Variável (V)
- Último Custo de Reposição (R)
- Último Custo de Entrada Com ICMS (E)
- Último Custo Médio Gerencial (G)
- Último Custo Médio Sem ICMS (Z)
- Último Custo de Entrada Sem ICMS (S)

### Principais causas do custo zerado

- **Produto sem custo calculado para o tipo selecionado**: não existe, ainda, um custo registrado no tipo definido na TOP (ex.: se a TOP usa "R", mas o produto nunca teve entrada que gerasse Custo de Reposição).
- **Custo por empresa não configurado**: com o parâmetro **CUSTOPOREMP** ligado, o custo precisa existir especificamente para a empresa em que a requisição está sendo lançada, um custo cadastrado só em outra empresa não é considerado.

> **Atenção com itens bonificados**: nesses casos, um preço zero pode ser intencional (desconto de bonificação de 100% sobre o custo), e não um erro de cálculo. Não confunda com as causas acima.

### Como verificar o custo do produto

**(1)** Acesse Comercial > Consultas > Variação de Custos de Produtos.

**(2)** Localize o produto e confira se existe custo registrado no tipo usado pela TOP.

**(3)** Se **CUSTOPOREMP** estiver ligado, confirme que o custo está registrado para a empresa da requisição especificamente.

### Como resolver o problema

Para corrigir a situação de custo zerado, execute as seguintes ações:

**(1)** Garanta que o produto tenha custo calculado (via nota de entrada, transferência ou implantação de saldo) antes de lançar a requisição.

**(2)** Com Custo por Empresa ativo, atualize o custo na empresa correta.

**(3)** Revise, na TOP usada, se a opção escolhida em "Usar como Preço" é a mais adequada ao processo.

**Importante**: o preço é calculado no momento em que o item é incluído na requisição. Se o custo do produto for atualizado depois, o item já incluído **não** é recalculado automaticamente, é preciso excluir e incluir o item novamente.
