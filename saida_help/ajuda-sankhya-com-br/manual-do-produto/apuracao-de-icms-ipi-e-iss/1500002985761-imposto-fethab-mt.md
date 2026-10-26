---
id: "1500002985761"
titulo: "Imposto FETHAB - MT"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500002985761-Imposto-FETHAB-MT"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Apuração e Livros Fiscais > Apuração de ICMS, IPI e ISS"
atualizado_em: "2026-09-15T14:21:16Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "Impostos", "fethab", "mato grosso", "Cadastrar UPF marcar \"Calcular FETHAB?\"", "Definir alíquota e unidade padrão", "Informar no XML e ajustar agrupamento por itens", "MT"]
---

# Imposto FETHAB - MT

O imposto FETHAB (Fundo Estadual de Transporte e Habitação) é calculado por produto e de acordo com a quantidade comercializada. O cálculo desse imposto é realizado tomando como referência o índice Unidade Padrão Fiscal (UPF) que, nesse caso, é determinado semestralmente pela UF do Mato Grosso.

Abaixo, trouxemos as configurações necessárias para que você consiga utilizar o FETHAB - MT em nosso sistema:

Na tela de cadastro de [Estados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601294-Estados), você deve informar **"Cód. Unidade Federativa"** bem como, preencher todos os campos da aba [Unidades Fiscais por UF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601294-Estados#abaunidadesfiscaisporuf):

[GIF animado: Imagem 1: Na tela de cadastro de Estados , você deve informar "Cód. Unidade Federativa" bem como, preencher todos os campos da…](https://ajuda.sankhya.com.br/hc/article_attachments/1500003207421)

**Importante:** para o cálculo do FETHAB, é necessário que se tenha uma UPF cadastrada e que ela esteja com a validade dentro do período correspondente à data de negociação na emissão da nota fiscal.

Após configurar as Unidades Fiscais por UF, acesse a tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades), efetue a marcação **"Calcular FETHAB?"** para definir que a empresa escolhida estará sujeita ao cálculo do FETHAB para determinados produtos e preencha o campo **"Mensagem FETHAB para Inform.Adicional NF-e"**com a mensagem que será exibida no rodapé da nota:

[GIF animado: Imagem 2: Após configurar as Unidades Fiscais por UF , acesse a tela Preferências da Empresa , aba Propriedades , efetue a…](https://ajuda.sankhya.com.br/hc/article_attachments/360104219133)

Agora, na tela de [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostos), você deve informar o valor de **"Alíquota FETHAB"** que será aplicado no cálculo desse imposto e definir qual a **"Unidade Padrão p/ FETHAB"** a ser utilizada como base para a conversão das alíquotas alternativas:

[GIF animado: Imagem 3: Agora, na tela de Cadastro de Produtos , na aba Impostos , você deve informar o valor de "Alíquota FETHAB" que será…](https://ajuda.sankhya.com.br/hc/article_attachments/1500003183422)

**Observação:** o percentual do FETHAB pode variar de acordo com o produto comercializado, portanto, siga as regras determinadas pela legislação da UF competente.

Ainda no Cadastro de Produtos, na aba [Unidades Alternativas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaunidadesalternativas), você deve determinar a **"Qtd Casas Decimais UPF"** para a unidade alternativa escolhida:

[GIF animado: Imagem 4: Ainda no Cadastro de Produtos , na aba Unidades Alternativas , você deve determinar a "Qtd Casas Decimais UPF" para a…](https://ajuda.sankhya.com.br/hc/article_attachments/360102050394)

Por fim, para disponibilizar as informações de FETHAB no XML da NF-e, é necessário que você acesse a tela Preferências da Empresa, botão [Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#botooutrasopes), clique na opção **"Complemento p/ Itens da Nota (Web))"**, pesquise por **"FETHAB"** e selecione os campos da aba **"Itens da Nota"**. Após isso, na aba [NF-e/NFC-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abanf-enfc-e), efetue a marcação **"Usar nome do campo no Complemento para Itens da Nota?"**:

[GIF animado: Imagem 5: Por fim, para disponibilizar as informações de FETHAB no XML da NF-e , é necessário que você acesse a tela Preferências…](https://ajuda.sankhya.com.br/hc/article_attachments/360102049614)

Finalizando as configurações acima, ao lançar uma nota na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), serão exibidas as informações de Alíquota FETHAB, Valor FETHAB e o Valor Total FETHAB nos itens.

**Observação:** se você não preencher o campo Mensagem FETHAB para Inform. Adicional NF-e e a marcação Calcular FETHAB? nas Preferências da Empresa, aba Propriedades, o imposto será enviado de forma automática com a seguinte mensagem:

**"O imposto FETHAB será recolhido pelo adquirente desta mercadoria na condição de contribuinte substituto. No valor:|VL|".**

**Importante:** caso seja necessária a retenção desse imposto, ela deve ser feita pelo Tipo de Negociação, através da fórmula VLRNOTA - VLRFETHAB.

Influenciando a rotina do FETHAB, encontra-se a marcação **“Agrupar produtos semelhantes na NF-e?”** encontrada na aba [NF-e/NFC-e/CF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce/cfe) da tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), caso ela esteja habilitada, existirão dois comportamentos:

- **Nota com itens semelhantes:**

Ao emitir uma nota com itens semelhantes para os quais haja incidência do cálculo do FETHAB, além de agrupar os itens, conforme comportamento atual dessa funcionalidade, o sistema irá somar o valor do FETHAB calculado nos itens para compor a tag InfAdProd.

- **Nota com itens diferentes:**

Neste caso, ao emitir uma nota com itens diferentes para os quais haja incidência do cálculo do FETHAB, além de não realizar o agrupamento dos itens, o sistema não irá somar o valor do FETHAB calculado nos itens, e levará para a tag InfAdProd o valor calculado individualmente para cada item.

No entanto, quando a marcação Agrupar produtos semelhantes na NF-e? estiver desabilitada, ao emitir uma nota com itens semelhantes para os quais haja incidência do cálculo do FETHAB, além de não realizar o agrupamento dos itens, o sistema não irá somar o valor do FETHAB calculado nos itens e, levará para a tag InfAdProd o valor calculado individualmente para cada item.

**Parâmetros que influenciam esta rotina**

**Exceção p/ cálculo do FETHAB por TOP e Parceiros - EXCFETHABTOPPAR**: quando este parâmetro for habilitado, a marcação **“Calcular FETHAB”** será apresentada na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos) da tela [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e na aba [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal) da tela [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros).

Este parâmetro é utilizado para definir o cálculo do FETHAB, determinando se este terá exceção por Tipo de Operação - TOP e no Cadastro de Parceiros.

**Observação:** o cálculo ocorrerá somente na operação em que, o botão estiver marcado na tela Cadastro de Parceiros, ou na tela [Preferência da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa) e estiver marcado na tela Tipo de Operação - TOP, cujo movimento seja Nota de Venda, e as configurações e exceções para o cálculo do FETHAB, acima mencionadas, estiverem realizadas.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500002985761-Imposto-FETHAB-MT#top)
