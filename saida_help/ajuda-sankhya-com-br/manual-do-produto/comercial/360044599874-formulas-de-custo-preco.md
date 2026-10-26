---
id: "360044599874"
titulo: "Fórmulas de Custo/Preço"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599874-F%C3%B3rmulas-de-Custo-Pre%C3%A7o"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:22:28Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "AVALFCUSERRZERO", "Fórmulas de Custo/Preço", "br.com.sankhya.formulas.custo.preco", "Fórmulas de Custo/Preço manual", "Fórmulas", "Custo", "Preço", "Estoque", "Precificação Custos", "Comercial"]
---

# Fórmulas de Custo/Preço

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311799194519) Módulo: Comercial > Avançado > Fórmulas 
```

---

Nesta tela estão as ferramentas para a criação de fórmulas automáticas de precificação dos produtos e para a gestão e acompanhamento dos custos destes. A criação destas fórmulas consiste, basicamente, na construção de expressões aritméticas que automatizam o exaustivo trabalho de análise e cálculo para formação dos custos de cada produto. Este é um recurso particularmente produtivo para empresas que comercializam grande quantidade de itens distintos.

Para facilitar sua navegação nas funcionalidades dessa tela, acesse os links abaixo:

[Criação De Fórmulas De Custo/Preço No Sankhya Om](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599874-F%C3%B3rmulas-de-Custo-Pre%C3%A7o#cria%C3%A7%C3%A3odef%C3%B3rmulasdecusto/pre%C3%A7onosankhyaom)

[Construtor de Expressões](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599874-F%C3%B3rmulas-de-Custo-Pre%C3%A7o#construtordeexpress%C3%B5es)

[Fórmulas para o Cálculo do Custo do DIFAL/FCP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599874-F%C3%B3rmulas-de-Custo-Pre%C3%A7o#f%C3%B3rmulasparaoc%C3%A1lculodocustododifal/fcp)

[Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599874-F%C3%B3rmulas-de-Custo-Pre%C3%A7o#par%C3%A2metrosqueinfluenciamestarotina)

![Imagem 2: Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/article_attachments/360077372074)

Abaixo, demonstraremos alguns dos benefícios que as Fórmulas de Custo/Preço proporcionam:

- A automatização do processo elimina o risco de erros e diminui drasticamente o tempo da operação;
- Os preços e os custos podem ser reajustados em conjunto (todos os produtos do estoque), em subconjuntos (por grupo de produto, por lote, por tipo, etc.) ou ainda, individualmente;
- Podem-se criar fórmulas para análise de vários tipos de custo, que são atualizados simultaneamente e podem ser analisados e comparados individualmente.

**Observação:** As Fórmulas de Custo/Preço podem atualizar vários tipos de custo da empresa, possibilitando múltiplas análises.

### Criação De Fórmulas De Custo/Preço No Sankhya Om

A criação de Fórmulas de Custo/Preço no Sankhya Om consiste na elaboração de uma expressão aritmética que simule cada um dos passos da formação de preço de um produto; assim, você pode criar e registrar inúmeras fórmulas.

As abas desta tela apresentam duas partes distintas, uma para **"Fórmula"** e outra para **"Descrição da Fórmula"**, que servirá para descrever a expressão matemática da fórmula.

Desta forma, inicialmente, preencha os seguintes campos:

O campo **"Código"** é de preenchimento manual e obrigatório.

Informe no campo **"Descrição da Fórmula"** uma descrição para identificação da fórmula.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599874-F%C3%B3rmulas-de-Custo-Pre%C3%A7o#top)

### Construtor de Expressões

![Imagem 3: Construtor de Expressões](https://ajuda.sankhya.com.br/hc/article_attachments/360078505433)

Por meio do botão em destaque, temos o componente [Construtor de Expressões](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109213-Construtor-de-Express%C3%B5es).

Para obter detalhes do funcionamento deste componente, acesse o link acima.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599874-F%C3%B3rmulas-de-Custo-Pre%C3%A7o#top)

### Fórmulas para o Cálculo do Custo do DIFAL/FCP

Trouxemos abaixo, as fórmulas responsáveis pelo cálculo de custo e preço, específicas para permitir o custeio dos produtos, considerando os impostos do DIFAL/FCP:

**VLRDIFALDEST** - Deverá buscar o valor total do ICMS do DIFAL do destinatário da nota fiscal;

**VLRICMSDIFALREM** - Buscará o valor total do ICMS do DIFAL do remetente da nota fiscal;

**VLRICMSFCP** - Irá pesquisar o valor total do ICMS do FCP da nota fiscal;

**VLRFCPINT** - Executa a busca pelo valor total do ICMS do FCP Interno da nota fiscal.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599874-F%C3%B3rmulas-de-Custo-Pre%C3%A7o#top)

### Parâmetros que influenciam esta rotina

O parâmetro **"Avaliar fórmula de custo com erro como zero? - AVALFCUSERRZERO"** por padrão, é apresentado ligado; quando o mesmo for desabilitado, será feita a verificação pelo sistema de algum erro matemático nas fórmulas cadastradas no momento de sua utilização; caso algum erro seja encontrado, será apresentada uma mensagem informando sobre sua identificação. Por exemplo:

**"Erro na avaliação da fórmula 2 - "Divisão por 0"".**

**Nota:** Se o parâmetro for mantido ligado, este comportamento acima mencionado não ocorrerá, ou seja, nenhuma mensagem será apresentada caso a fórmula possua alguma imprecisão matemática.

O parâmetro **"Usar fórmula da empresa? - CUSTOFORMEMP"** definirá o local onde o sistema buscará a Fórmula Custo/Preço para atualização de custos. Quando ligado, será utilizada a fórmula informada na aba [Estoque/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abaestoquepreo) das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), permitindo uma atualização diferente para cada Empresa, de acordo com as fórmulas informadas. Quando desligado, o sistema buscará a fórmula informada na aba [Formação de Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abaformaodecustopreo) do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-).

No parâmetro **"TOP para aceitar Qtd igual a zero - TOPQTDZERO"**, informe o código da TOP que aceitará o lançamento de itens com quantidade zero, quando a nota for utilizada apenas para recalcular o custo dos produtos.

**Observação:** Quando a quantidade negociada da nota for igual a zero, para as TOP’s indicadas no parâmetro de chave TOPQTDZERO, o sistema carregará as variáveis AntCusComICM, AntCusSemICM, AntCusVar, AntCusRep, AntCusGer, da Fórmula de Custo/Preço com o custo anterior.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599874-F%C3%B3rmulas-de-Custo-Pre%C3%A7o#top)
