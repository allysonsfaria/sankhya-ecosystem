---
id: "360044600794"
titulo: "Múltiplas Partilhas/Anexos para Empresas do Simples Nacional"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600794-M%C3%BAltiplas-Partilhas-Anexos-para-Empresas-do-Simples-Nacional"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:50:39Z"
rotulos: ["Configuração", "NF-e", "Alíquota de ISS", "Simples Nacional", "ICMS", "Impostos", "Múltiplas Partilhas para Empresas do Simples Nacional manual", "Configuração de Partilhas no Simples Nacional"]
---

# Múltiplas Partilhas/Anexos para Empresas do Simples Nacional

Caso a empresa esteja encaixada em mais de uma Partilha/Anexo de Serviços, pois esta possui várias atividades de prestação de serviços, as quais se enquadram em mais de um anexo da [Lei Complementar 123/2006](http://www.planalto.gov.br/ccivil_03/leis/LCP/Lcp123.htm), no Sankhya Om será possível cadastrar mais de uma partilha/anexo para empresas optantes do Simples Nacional, para os casos em que o lançamento efetuado possua produtos/serviços que se enquadrem em partilhas/anexos diferentes.

**Importante:** o comportamento mencionado abaixo, é válido apenas para o cálculo de [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Al%C3%ADquotas-de-ISS) e/ou [ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS).

São necessárias as seguintes configurações:

Primeiramente na tela [Partilha/Anexo do Simples Nacional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601574-Partilha-Anexo-do-Simples-Nacional), configure devidamente as Partilhas/Anexos:

![Imagem 1: Primeiramente na tela Partilha/Anexo do Simples Nacional , configure devidamente as Partilhas/Anexos:](https://ajuda.sankhya.com.br/hc/article_attachments/4410457510679)

Feito isso, no [Cadastro de Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913), aba [Naturezas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas#abanaturezas), se a empresa possuir uma ou mais partilhas/anexos, marque e/ou preencha corretamente os campos **"Optante pelo SIMPLES"**, **"Cód. Regime Tribut."** e **"Tipo de Partilha/Anexo SN"**.

![Imagem 2: Feito isso, no Cadastro de Empresas , aba Naturezas , se a empresa possuir uma ou mais partilhas/anexos, marque e/ou…](https://ajuda.sankhya.com.br/hc/article_attachments/4410457573655)

Depois, no [Cadastro de Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o) ambas as abas [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o#abaimpostos) e [Configurações por Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o#abaconfiguraesporempresa); possuem o campo Tipo de Partilha/Anexo, que deve ser definido corretamente de acordo com o serviço e empresa em questão, respectivamente:

[GIF animado: Imagem 3: Depois, no Cadastro de Serviços ambas as abas Impostos e Configurações por Empresa ; possuem o campo Tipo de…](https://ajuda.sankhya.com.br/hc/article_attachments/4410457653271)

**Importante:** você deve configurar os Serviços, se a empresa trabalhar com tal aspecto.

Nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba [SIMPLES Nacional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abasimplesnacional), poderão ser cadastrados os vários Tipos de Partilhas/Anexos com datas de vigências diferenciadas. Para cada tipo cadastrado, tem-se sua correspondente vigência, de modo que, o sistema irá considerar aquela mais atual para cada Tipo de Partilha/Anexo.

![Imagem 4: Nas Preferências da Empresa , aba SIMPLES Nacional , poderão ser cadastrados os vários Tipos de Partilhas/Anexos com…](https://ajuda.sankhya.com.br/hc/article_attachments/4410457680919)

Na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), ao realizar a emissão da NF-e, o sistema verifica se a empresa é Optante pelo Simples Nacional e caso afirmativo, efetua as seguintes análises:

1. Se houver um lançamento na tela de [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abageral), de origem estrangeira (campo **"Origem do produto"** selecionado com a opção **"1 - Estrangeira, Importação direta, exceto a indicada no código 6"** ou **"6 - Estrangeira, Importação direta, sem similar nacional, constante em lista de Resolução CAMEX"**) ou de fabricação própria (campo **"Usado como"** definido como **"Venda (Fabricação Própria)"**), será feita a busca nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), do Tipo de Partilha/Anexo vigente igual a Indústria para se calcular o ICMS e IPI;
2. Para demais Produtos, o sistema irá buscar o Tipo de Partilha/Anexo vigente igual a Comércio para calcular o ICMS e IPI;
3. Para [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o), o sistema irá buscar o Tipo de Partilha/Anexo informado na aba [Configurações por Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o#abaconfiguraesporempresa); não encontrando ou se estiver em branco, irá buscar na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o#abaimpostos). Se estes dois campos estiverem em branco, o sistema irá tratar o Simples Nacional aplicando a regra já existente.
4. Caso a empresa não seja Optante pelo Simples Nacional, serão consideradas as regras fiscais para empresas débito/crédito.

![Imagem 5: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16647150405527) Acesse também:

[Anexos e Faixas do Simples Nacional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107273-Anexos-e-Faixas-do-Simples-Nacional)
