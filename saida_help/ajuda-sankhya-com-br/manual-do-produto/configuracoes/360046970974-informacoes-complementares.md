---
id: "360046970974"
titulo: "Informações Complementares"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360046970974-Informa%C3%A7%C3%B5es-Complementares"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:59:59Z"
rotulos: ["Configuração", "XML", "Impostos", "TOP", "Nota Fiscal Eletrônica de Serviço - Prefeituras", "Prefeituras", "NFS-e", "Informações Complementares sobre NFS-e"]
---

# Informações Complementares

Nesta documentação você encontrará as informações complementares relacionadas à NFS-e. Vejamos sobre cada uma delas:

[Tabelas de armazenamento dos XML´s](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046970974-Informa%C3%A7%C3%B5es-Complementares#tabelasdearmazenamentodosxmls)                          [Lei da Transparência dos Tributos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046970974-Informa%C3%A7%C3%B5es-Complementares#leidatransparnciadostributos)   

[Observações a respeito de Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046970974-Informa%C3%A7%C3%B5es-Complementares#observaesarespeitodeimpostos)                              [Análise da descrição do Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046970974-Informa%C3%A7%C3%B5es-Complementares#anliseemrelaoadescriodoservio)

[Config. p/ envio da TAG <MunicipioIncidencia>](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046970974-Informa%C3%A7%C3%B5es-Complementares#configuraesparaenviodatagmunicipioincidencia) 

### Tabelas de armazenamento dos XML´s

A tabela do sistema onde ficam armazenados o XML's do RPS e da Nota aprovada é a TGFNFSE; seus respectivos campos são:

TGFNFSE.XMLRPS ?XML do RPS que será enviado;

TGFNFSE.XMLNFSE ? XML da NFSe já aprovada e devolvida pela Prefeitura.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046970974-Informa%C3%A7%C3%B5es-Complementares#top)

### Lei da Transparência dos Tributos

A lei da Transparência dos Tributos para NFS-e, possui uma particularidade, visto que no manual ABRASF (Associação Brasileira de Secretários e Dirigentes das Finanças dos Municípios das Capitais) não determina uma TAG específica para destacar os valores de impostos, nem como devem ser destacados na NFS-e. Dessa forma, observe abaixo as formas de geração da Lei da Transparência para NFS-e:

**1)** É possível que se apresentem estes valores, por meio de uma alteração no modelo de impressão, e compilação de alguns objetos via banco de dados; estas modificações deverão ser realizadas com o auxílio de um consultor Sankhya especializado.

**2)** Tem-se o parâmetro **"Aplicar a lei da transparência p/ NFS-e? - APLLEITRANSP"**, que quando habilitado leva a informação pertinente a Lei da Transparência na descrição do serviço no XML da nota. Para tanto, é necessário que as seguintes configurações sejam realizadas:

- O parâmetro "Fonte do cálculo da Carga Média Tributária - LEI12741FONTE" deverá estar devidamente configurado com a fonte do cálculo da Carga Média Tributária informada no campo "Texto" da tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834). A descrição da referida fonte será inserida ao final do detalhamento da Lei da Transparência no XML.
- Na tela de [Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553), aba Impostos, configure os campos **"% Carga Média Trib. Nacional", "% Carga Média Trib. Federal" e "% Carga Média Trib. Municipal"**. Sendo que, o campo % Carga Média Trib. Nacional não permitirá o seu preenchimento quando os outros dois campos estiverem configurados.
- Na tela [Grupo de Produtos/Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025238994-Grupos-de-Produtos-Servi%C3%A7os), os campos a serem preenchidos contém a mesma descrição e particularidade.

**Importante:** para as empresas que já utilizam a primeira forma de geração da Lei da Transparência, é necessário uma certa atenção ao habilitar o parâmetro Aplicar a lei da transparência p/ NFS-e? - APLLEITRANSP. Sendo que, de acordo com a forma de geração atual poderão ocorrer divergências entre as informações geradas. Além disso, será necessário ajustar o modelo de impressão para que no ato da impressão da nota, a Lei da Transparência seja destacada corretamente.

**3)** Para configurar a Lei da Transparência para prefeituras que usam o Json, além dos parâmetros mencionados nos itens 1 e 2, ative a marcação **"Enviar as inf. da Lei da Transparência na desc. de cada item"** e/ou **"Enviar inf. da Lei da Transparência com o total de impostos, na obs. da nota"** da aba  [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abanfs-e) nas Preferências da Empresa.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046970974-Informa%C3%A7%C3%B5es-Complementares#top)

### Observações a respeito de Impostos

**1-** Os impostos federais e a retenção do ISS não são demonstrados no "Valor Total" da Nota, apenas de forma informativa nos devidos campos e mantendo o "Valor da Nota" inalterado, ou seja, não são deduzidos do Valor Total.

**2-** O Valor da Nota que vai para a prefeitura é sempre igual ao valor dos serviços - desconto dos itens - desconto de serviços pé da nota. Se houverem "Retenções" na nota, elas NÃO serão deduzidas do Valor da Nota, isso vale também para ISS retido. Isso significa que o Valor da Nota na Prefeitura será diferente do "Valor Financeiro", nestes casos.

**3-** O "Valor dos Itens" que vai para a NFS-e é o "Valor Líquido", deduzindo inclusive o desconto de serviços do pé da Nota, rateados de acordo com o valor de cada serviço. O "Valor Unitário" será sempre o "Valor Liq." dividido pela "Quantidade", independente do que esteja na Nota. Quando há "Retenções", para melhor esclarecer os diferentes valores entre "Nota na Prefeitura" e "Nota no Sistema", adiciona-se ao campo de "Descrição" do serviço o texto:

**"Nota com retenção de impostos. Valor líquido (deduzindo as retenções) = R$ 999.99".**

**4-** Para todas as Prefeituras o sistema buscará informações sobre impostos, tanto da TGFDIN quanto da TGFIMN, ou seja, os impostos poderão ser calculados seguindo regras de TOP e/ou de "Outros Impostos", isso vale para todos os impostos, inclusive ISSQN.

Através do link [Cadastro de Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834) tem-se mais informações sobre os impostos abordados.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046970974-Informa%C3%A7%C3%B5es-Complementares#top)

### Análise da descrição do Serviço

O campo **"Descrição"** do serviço é composto da seguinte forma:

- Campo Observação Padrão (caso tenha sido informado);
- Campo Observação da Nota, campo TGFCAB.OBSERVACAO (caso tenha sido informado);
- Caso a Nota possua "Retenções", será adicionado o texto:

**"Nota com retenção de impostos. Valor líquido (deduzindo as retenções) = ###,##".**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046970974-Informa%C3%A7%C3%B5es-Complementares#top)

### Configurações para envio da TAG <MunicipioIncidencia>

Algumas prefeituras solicitam o envio da TAG **<MunicipioIncidencia>**; vejamos abaixo as condições para que seja enviada a informação correspondente ao município incidência:

**1-** Deve-se preencher o Código de Tributação do Município em algum dos seguintes cadastros:

- Cadastro do Serviços, [aba Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o#abaimpostos), campo **"Cód. Trib. Município NFS-e"**;
- Cadastro do Serviços, [aba Configurações por Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o#abaconfiguraesporempresa), campo **"Cód. Trib. Município NFS-e"**;
- [Cadastro da Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014), campo **"Cod. Trib. Município"**.

**2-** No Cadastro de Tipos de Operação - TOP, [aba Livro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal), o campo **"Cód. Natureza Oper. ISS (NFS-e)"** deve estar definido dentre as seguintes opções:

- Exigível;
- Exigibilidade Suspensa por Decisão Judicial;
- Exigibilidade Suspensa por Processo Administrativo.

**3-** Caso nas Preferências da Empresa, a [aba CNAE Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abacnaeempresa) não esteja configurada para a empresa de prestação, o sistema irá verificar:

- Se o ISS não for retido, o código do município de incidência será o mesmo código do município onde o Prestador do Serviço é estabelecido;
- Caso o ISS seja retido, o código do município de incidência será o mesmo código do município onde o Tomador do Serviço é estabelecido.

**4-** Caso nas Preferências da Empresa, a aba CNAE Empresa esteja configurada, o sistema irá verificar a definição feita no campo **"Local tributação (ISS Retido)"** caso o ISS for retido, e o campo **"Local tributação (ISS normal)"** se o ISS não for retido. Os campos citados acima possuem as seguintes opções:

- **Cidade do Prestador:** Neste caso, a cidade de prestação do serviço será a mesma cidade da empresa prestadora, independente do campo cidade da nota.
- **Cidade do Tomador:** A cidade de prestação do serviço será a mesma cidade do endereço do tomador, independente do campo cidade da nota.
- **Cidade de Prestação:** Nesta hipótese a cidade de prestação do serviço será a que estiver presente no campo Cidade da nota. Caso o referido campo não esteja informado, em caso de retenção do ISS, a cidade será a mesma do endereço do tomador; na situação em que o ISS não for retido, a cidade será a mesma do endereço do prestador.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046970974-Informa%C3%A7%C3%B5es-Complementares#top)
