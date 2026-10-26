---
id: "360045120393"
titulo: "Estoque / Endereçamento WMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120393-Estoque-Endere%C3%A7amento-WMS"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-09-19T23:07:07Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Consulta", "WMS", "Produto", "Parceiro", "Checkouts", "Endereçamento", "WMSUSAIDPALETE", "br.com.sankhya.wms.estoqueenderecamentowms", "Estoque/Endereçamento WMS manual", "Endereço", "Estoque", "Docas", "SEPAREACONFWMS", "Detalhes e filtros para gerenciar estoques", "Opções para filtrar e gerenciar endereços específicos", "Filtros detalhados para visualização por produto"]
---

# Estoque / Endereçamento WMS

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311600442775) Módulo: WMS > Consultas
```

---

Nesta tela são apresentados os estoques por endereços do WMS. Através dela, você terá informações por endereço, apresentando as entradas e saídas pendentes, estoques atual e disponível, filtrar endereços vazios, etc.

Neste artigo veremos os seguintes tópicos:

[Painel de Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120393-Estoque-Endere%C3%A7amento-WMS#paineldefiltros)                                                         [Seção Endereço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120393-Estoque-Endere%C3%A7amento-WMS#se%C3%A7%C3%A3oendere%C3%A7o)

[Seção Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120393-Estoque-Endere%C3%A7amento-WMS#se%C3%A7%C3%A3oproduto)        

![Imagem 2: Seção Produto](https://ajuda.sankhya.com.br/hc/article_attachments/4409830906007)

**Observação:** o objetivo da coluna **"Dt Val. Mín. Expedição"**, é informar qual a menor data de validade que um produto pode conter em estoque para que o sistema permita a sua expedição. Assim, na geração da onda de separação, será analisada a **"Data Atual"** mais os **"Dias para Expedição"** do [Cadastro do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113). Caso a data de validade ultrapasse esse cálculo, o sistema irá gerar a onda de separação. Dessa forma, essa data deverá ser um espelho da data que o sistema valida.

## Painel de Filtros

No lado direito da tela, note a existência de alguns filtros para configuração, e consequente apresentação dos produtos.

Inicialmente, temos o **"Assistente de Filtros"**, que permite a criação de filtros personalizados, que irão particularizar a busca dos produtos desejados.

Informe no campo **"Empresa"**, a empresa na qual os produtos desejados pertencem.

No filtro **"Parceiro"**, você pode informar qual parceiro deseja encontrar, uma vez que este também poderá possuir [Controle de Estoque de Terceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120393-Estoque-Endere%C3%A7amento-WMS#top)

## Seção Endereço

O campo **"Faixa de Endereços"**permite que você realize a busca dos produtos por uma determinada faixa de endereços. Estes podem ser ruas, docas etc.

Efetuando a marcação **"Desconsiderar Endereços Especiais"**, serão desconsiderados os endereços cadastrados na tela [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento) vinculados a endereços especiais da empresa nas **"Preferências da Empresa"**, aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abawms), os seguintes endereços:

- Cód. End. Sobra,
- Cód. End. Avaria,
- Cód. End. Perda,
- Cód. End. Divergência,
- Endereço Indefinido para movimentação e
- Endereço de Checkout Indefinido.

Se você efetuar a marcação **"Desconsiderar Docas"**, fará com que sejam desconsiderados endereços vinculados à docas cadastradas na tela [Docas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612974-Docas).

Com a marcação **"Desconsiderar Checkouts"**realizada, serão desconsiderados os endereços cadastrados na tela Endereço de Armazenamento, com a marcação **"Exclusivo p/ Conferencia"** efetuada. Através da configuração do parâmetro **"Separação por Área de Conferência no WMS? - SEPAREACONFWMS"**, esta marcação (Desconsiderar Checkouts) pode ser retirada da tela.

Quando a marcação **"Considerar Endereços Vazios"** estiver habilitada, será possível consultar no Estoque/Endereçamento os endereços que estão vazios.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120393-Estoque-Endere%C3%A7amento-WMS#top)

## Seção Produto

Selecione no campo **"Produto"** o produto ao qual você deseja visualizar.

Informe no campo **"Complemento"**, o complemento do produto que foi cadastrado para o mesmo.

Através do campo **"Referência"**, você filtra as informações pela referência do produto.

Você pode filtrar o produto desejado através de sua marca, informando a mesma no campo **"Marca"**.

No campo **"Referência do Fornecedor"**, informe a referência do fornecedor vinculada ao mesmo em seu cadastro.

Pelo campo **"Grupo de Produto"**, é feita a filtragem através do grupo de produtos do item que você deseja visualizar.

Informe no campo **"Período de Validade"**um período referente a data de validade dos produtos, que possuem esta informação cadastrada.

Caso o parâmetro **"Usa ID de palete no WMS? - WMSUSAIDPALETE"** esteja habilitado, será apresentado também o campo **"ID Palete"**, onde você pode realizar a filtragem através da ID do Palete.

Depois de criados e/ou preenchidos os filtros desejados, são apresentados na grade do lado superior direito da tela, os produtos que se enquadraram nestes filtros.

Os produtos apresentados na grade, quando possuem a data de validade menor que a data atual, sua linha é apresentada na coloração **"vermelha"**; quando a data de validade é menor que a data de validade mínima, a tonalidade da fonte na linha se torna **"laranja"**; se nenhum dos casos for válido, a linha se mantém na cor **"preta"**.

Ao selecionar um produto, na grade **"Resumo das movimentações pendentes para o produto"** será apresentada uma síntese das movimentações do produto.

- Selecionando uma linha sem produto, não serão exibidos registros na grade;
- Ao selecionar uma linha que tenha produto, mas que não possui movimentações, será apresentado o nome do produto, porém sem registros na grade;
- Se for selecionado um produto que possua movimentações, estas serão exibidas na grade.

**Observação:** os [filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120393-Estoque-Endere%C3%A7amento-WMS#paineldefiltros) definidos não têm impacto sobre esta grade. As movimentações do produto são carregadas independentemente dos filtros configurados. Os filtros aplicam-se somente a grade superior, onde são exibidos os endereços com estoque. Ao selecionar um produto na grade superior, as informações relacionadas às movimentações pendentes desse produto são automaticamente carregadas nesta grade.

**Nota:** no Sankhya Om, é necessário desligar o parâmetro **"Endereçar produtos em endereços com permissão vazia - WMSENDERPERMVAZ"** para que os produtos não sejam endereçados em endereços em que a lista de endereços não estejam informados.

O botão ![Imagem 3: O botão "Validades" será disponibilizado quando uma linha que possuir data de validade for selecionada. Ao acionar este…](https://ajuda.sankhya.com.br/hc/article_attachments/16844928502935)**"Validades"** será disponibilizado quando uma linha que possuir data de validade for selecionada. Ao acionar este botão, será apresentado um pop-up com os detalhes de data de validade do estoque:

[GIF animado: Imagem 4: O botão "Validades" será disponibilizado quando uma linha que possuir data de validade for selecionada. Ao acionar este…](https://ajuda.sankhya.com.br/hc/article_attachments/4409834741783)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120393-Estoque-Endere%C3%A7amento-WMS#top)
