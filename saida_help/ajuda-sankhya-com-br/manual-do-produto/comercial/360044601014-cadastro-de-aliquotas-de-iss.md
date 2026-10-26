---
id: "360044601014"
titulo: "Cadastro de Alíquotas de ISS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Cadastro-de-Al%C3%ADquotas-de-ISS"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-09-28T11:59:19Z"
rotulos: ["AJUDA DO SKW", "manual", "Alíquotas de ISS manual", "ISS", "Configuração", "Fiscal", "Alíquota de ISS", "Impostos", "Alíquotas de ISS", "br.com.sankhya.core.cad.aliquotasiss", "BUSCALIQSDEST", "VALISSZERONFSE", "USARETISSESP", "Prefeituras", "ISS e ISSQN", "Competência Municipal", "Configuração e Alíquotas"]
---

# Cadastro de Alíquotas de ISS

**Caminho de acesso:** Menu Principal › Comercial › Arquivo › Cadastros › Alíquotas · Menu Principal › Contratos e Serviços › Arquivos › Cadastros

**Neste artigo**

- [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Cadastro-de-Al%C3%ADquotas-de-ISS#oque)
- [Sobre o ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Cadastro-de-Al%C3%ADquotas-de-ISS#iss)
- [Antes de começar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Cadastro-de-Al%C3%ADquotas-de-ISS#antes)
- [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Cadastro-de-Al%C3%ADquotas-de-ISS#painel)
- [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Cadastro-de-Al%C3%ADquotas-de-ISS#geral)
- [Aba Tabela de Retenção por Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Cadastro-de-Al%C3%ADquotas-de-ISS#retencao)
- [Alíquota ISS para empresa optante pelo Simples](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Cadastro-de-Al%C3%ADquotas-de-ISS#simples)
- [Nacional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Cadastro-de-Al%C3%ADquotas-de-ISS#simples)

## O que é e para que serve

O **Cadastro de Alíquotas de ISS** registra as alíquotas do Imposto Sobre Serviço (ISS) por cidade, serviço e empresa, com o código de tributação, as deduções de base e as regras de retenção por Parceiro usadas no cálculo do imposto nas notas de serviço. Nas empresas optantes pelo Simples Nacional, a tela não é considerada por padrão: o sistema usa a Partilha/Anexo do Simples Nacional, a menos que a marcação **Considerar Alíquota de ISS por Serviço** esteja habilitada.

---

## Sobre o ISS

O ISS, ou ISSQN (Imposto Sobre Serviço de Qualquer Natureza), é de âmbito municipal: somente os municípios têm competência para instituí-lo (Art. 156, IV, da Constituição Federal). A única exceção é o Distrito Federal, unidade da federação que tem as mesmas atribuições dos Estados e dos municípios. O ISSQN tem como fato gerador a prestação (por empresa ou profissional autônomo) de serviços descritos na lista de serviços da Lei Complementar nº 116, de 31 de julho de 2003.

Como regra geral, o ISSQN é recolhido ao município em que se encontra o estabelecimento do prestador. O recolhimento só é feito ao município em que o serviço foi prestado (ver o artigo 3º da lei complementar citada) no caso de serviços caracterizados por sua realização no estabelecimento do cliente (tomador) — por exemplo, limpeza de imóveis, segurança, construção civil e fornecimento de mão de obra.

Os contribuintes do imposto são as empresas ou profissionais autônomos que prestam o serviço tributável, mas os municípios e o Distrito Federal podem atribuir às empresas ou pessoas que tomam os serviços a responsabilidade pelo recolhimento do imposto.

A alíquota varia de um município para outro. A União, por meio da lei complementar citada, fixou a alíquota máxima de 5% para todos os serviços. A alíquota mínima é de 2%, conforme o artigo 88 do Ato das Disposições Constitucionais Transitórias da Constituição Federal. A base de cálculo é o preço do serviço prestado.

A função do ISSQN é predominantemente fiscal. Mesmo sem alíquota uniforme, não se pode afirmar que se trata de um imposto seletivo. O ISS não incide sobre locação de bens móveis, conforme jurisprudência do Supremo Tribunal Federal (STF) (RE 116.121, Rel. Min. Marco Aurélio).

O ISS é devido ao município em que o serviço é efetivamente prestado, ainda que o estabelecimento prestador esteja situado em outro município (Roque Carrazza). A Primeira Seção do Superior Tribunal de Justiça (STJ), porém, pacificou o entendimento de que, para fins de incidência do ISS, importa o local em que foi concretizado o fato gerador, como critério de fixação de competência e exigibilidade do crédito tributário, ainda que se releve o teor do art. 12, alínea a, do Decreto-Lei nº 406/68 (AgRg no REsp 334188, DJ 23.06.2003 p. 245).

O ISS incide na operação de arrendamento mercantil de coisas móveis (Súmula 138 do STJ) e sobre o valor dos serviços de assistência médica, incluídos as refeições, os medicamentos e as diárias hospitalares (Súmula 274 do STJ).

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Cadastro-de-Al%C3%ADquotas-de-ISS#sumario)

---

## Antes de começar

Antes de configurar o cálculo do ISS, confira as configurações abaixo:

1. No [**Cadastro de Serviço**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o), aba [**Impostos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos), selecione no campo **Tem ISS** a opção correspondente ao tipo de tributação e preencha o campo **CNAE** (Classificação Nacional de Atividades Econômicas).
2. Nas [**Preferências da Empresa**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [**Propriedades**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades), configure o campo **ISS**, que define como se dá a tributação de ISS da empresa:
   - **Tributado**
   - **Isento**
   - **Não Tributado**
3. No [**Cadastro de Parceiros**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros), aba [**Fiscal**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal), defina a marcação **Retém ISS**. Ela determina qual alíquota é usada no cálculo: marcada, o sistema usa a alíquota da cidade do Parceiro e deduz o valor do imposto; desmarcada, usa a alíquota da cidade da empresa e não deduz. Só faz sentido reter o ISS se ele for calculado pela cidade do Parceiro, pois o Parceiro pagará menos na nota e recolherá o imposto devido. Na compra de serviços, só faz sentido reter se o cálculo for pela cidade da empresa.
4. Nos [**Tipos de Operação (TOP)**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [**Livro Fiscal**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal), configure três pontos:
   - Preencha o campo **Atualização livros de ISS** com uma das opções: **Não Atualiza**, para operações que não movimentam serviços; **Prestações**, para operações que movimentam serviços prestados; ou **Aquisições**, para operações que movimentam serviços tomados.
   - Configure o campo **Modelo Documento ISS** conforme o modelo usado nos documentos fiscais de serviços. O campo é habilitado quando o campo **Atualização livros de ISS** está com **Prestações** ou **Aquisições**.
   - No campo **Código CFPS**, informe o Código Fiscal de Prestações de Serviço (CFPS) da operação. Os códigos devem ser incluídos antes no [**Cadastro de CFOP**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600714-CFOP), com código acima de 8000.

**ℹ️ Nota**

Para que a alíquota da cidade da prestação do serviço seja usada no cálculo de ISS de uma nota de compra, informe essa cidade no campo **Cidade** da aba [**Impostos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#abaimpostos) do [Rodapé](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#graderodap) da nota, antes de informar o serviço no lançamento.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Cadastro-de-Al%C3%ADquotas-de-ISS#sumario)

---

## Painel Principal

- **Percentual de ISS** — aceita até 5 casas decimais na alíquota, para garantir precisão no cálculo em municípios específicos. Para isso, verifique se o parâmetro **Decimais p/ alíquota de ISS** (`DECALIQISS`) está habilitado na tela [**Preferências**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias).
- **Código Alíquota** — identifica qual alíquota é usada nos documentos fiscais.
- **Cidade** — a cidade em que o ISS incide.
- **Serviço** — o serviço sobre o qual o ISS incide.
- **Empresa** — a empresa a que o ISS se aplica.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Cadastro-de-Al%C3%ADquotas-de-ISS#sumario)

---

## Aba Geral

A aba **Geral** reúne o percentual, a tributação, o benefício municipal e as deduções de base do ISS.

### Alíquota e tributação

- **Percentual de ISS** — o percentual de ISS que será cobrado.
- **Cód. Tributação ISS** — o tipo de código de tributação de ISS, entre as opções:
  - **07 - Não Tributado**
  - **06 - Isento**
  - **00 - Tributado**
  - **01 - Tributado com ISS Retido**

**ℹ️ Nota**

No campo **Percentual de ISS**, o sistema considera 4 casas decimais após a vírgula para calcular o ISS de forma exata e conforme a legislação. Isso afeta diretamente o cálculo do imposto na Central de Compras e na Central de Vendas.

#### Não calcula

**O que faz**

Com a marcação **Não calcula** e o parâmetro **Buscar Alíquota se não houver destaque** (`BUSCALIQSDEST`) habilitados, a alíquota vai para o XML, mas sem valor do imposto informado para o item.

**Quando usar**

Use quando a alíquota precisa constar no XML sem que o imposto seja destacado no item.

**Como funciona**

A marcação só é salva quando o campo **Cód. Tributação ISS** está com **07 - Não Tributado** ou **06 - Isento**. Se outro valor for informado com a marcação e o parâmetro habilitados, o sistema exibe "Cód. Tributação ISS não pode ser do tipo tributado enquanto o campo 'Não Calcula' é igual a 'Sim'."

**ℹ️ Nota**

Na validação dos dados do campo, pode aparecer uma mensagem informando que a nota possui valor de ISS, mas que ele não foi informado na tabela de impostos. Nesse caso, habilite o parâmetro **Permitir valores zerados na NFS-e** (`VALISSZERONFSE`) e a mensagem deixa de ser exibida.

### Benefício municipal e dedução na base

A prefeitura de Uberlândia permite deduções na base do ISS em algumas situações. Para isso, a aba tem dois campos:

- **Perc. de dedução na base do ISS** — o percentual aplicado no valor do item para compor a base reduzida.
- **Tipo de dedução de base do ISS** — o tipo de dedução permitido pela prefeitura, entre **Por percentual**, **Sub-Empreito** e **Materiais**. É este campo que informa ao sistema que há dedução na base de ISS.

O manual da Prefeitura de Uberlândia permite emitir notas com dedução por percentual ou por valor. O Sankhya Om sempre calcula o imposto pelo percentual informado no campo **Perc. de dedução na base do ISS**. Com a opção **Por percentual**, o sistema gera o XML com o percentual informado; com as outras duas opções, calcula o valor a partir do percentual e gera o XML com esse valor.

**⚠️ Atenção**

O sistema busca primeiro as informações no [Cadastro de Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos). As informações deste cadastro só são usadas quando não há configuração de impostos. Se as duas formas estiverem configuradas, prevalece o Cadastro de Impostos.

#### Número de identificação do Benefício Municipal

**O que faz**

Registra o código numérico oficial, de até 14 posições, do benefício ou incentivo fiscal concedido pela prefeitura local.

**Quando usar**

Use quando a prefeitura concede benefício ou incentivo fiscal ao serviço. O preenchimento é necessário para atender ao Padrão Nacional da Declaração de Prestação de Serviço (DPS).

**Como funciona**

Com o campo preenchido, o sistema:

- Aplica as reduções na base de cálculo do imposto durante o faturamento, em conjunto com as regras de dedução.
- Gera automaticamente o grupo estrutural `beneficioMunicipal` no arquivo JSON de integração enviado ao eNotas/Nota Gateway.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Cadastro-de-Al%C3%ADquotas-de-ISS#sumario)

---

## Aba Tabela de Retenção por Parceiro

A aba só aparece quando o parâmetro **Utiliza retenção de ISS por Cidade/Empresa/Serviço** (`USARETISSESP`) está habilitado.

- **Parceiro** — o Parceiro que deve seguir a regra de retenção do ISS em relação ao município e ao tipo de serviço cadastrado.
- **Retém ISS** — permite definir, para um mesmo Parceiro, o modelo de retenção do ISS por município: em um município o serviço pode estar sujeito à retenção na fonte e em outro não. Com esta marcação feita aqui, o sistema desconsidera a marcação **Retém ISS** da aba [**Fiscal**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal) do [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros).
- **Edição múltipla** — edita vários registros ao mesmo tempo a partir do modo grade. Por exemplo: com as alíquotas em modo grade, selecione-as e clique em **Edição múltipla**; os campos passam a ser editados de uma vez para todas as alíquotas selecionadas.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Cadastro-de-Al%C3%ADquotas-de-ISS#sumario)

---

## Alíquota ISS para empresa optante pelo Simples Nacional

Quando a empresa é optante pelo Simples Nacional e a marcação **Considerar Alíquota de ISS por Serviço** está desmarcada, o sistema desconsidera a aba [**Alíquota de ISS**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss) do [Cadastro de Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o) e a tela Alíquotas de ISS. Com a marcação **Optante pelo SIMPLES** ativada na aba [**Naturezas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas#abanaturezas) do [Cadastro de Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas), o sistema passa a usar a Partilha/Anexo do Simples Nacional definida nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa). Ele busca a partilha vinculada e usa as informações preenchidas no cadastro da partilha, na tela [Partilha/Anexo do Simples Nacional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601574-Partilha-Anexo-do-Simples-Nacional). Confira a seguir as validações realizadas pelo sistema em cada cenário.

### Empresa optante pelo Simples Nacional

1. O sistema acessa as Preferências da Empresa, verifica a aba [**SIMPLES Nacional**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abasimplesnacional) e valida qual cadastro de Partilha/Anexo está vinculado à empresa.
2. Em seguida, busca esse cadastro na tela Partilha/Anexo do Simples Nacional e aplica o percentual do campo **%ISS** da Partilha em todas as notas que contêm ISS.

### Empresa não optante pelo Simples Nacional

O sistema realiza todas as validações padrão para cálculo ou retenção do imposto, conforme detalhado neste artigo.

### Empresa optante pelo Simples Nacional com alíquota de ISS por serviço

Disponível a partir da versão 4.36.

Com a marcação **Considerar Alíquota de ISS por Serviço** habilitada nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), o sistema deixa de aplicar o percentual do campo **%ISS** da Partilha/Anexo do Simples Nacional. Em vez dele, passa a usar a alíquota cadastrada nesta tela para cada serviço prestado.

Use esta configuração quando a empresa presta serviços com alíquotas de ISS diferentes entre si — por exemplo, um serviço tributado a 2% e outro a 5%. Nesse cenário, a alíquota única da Partilha não representa corretamente o imposto de cada serviço.

A marcação vem desmarcada por padrão. Desmarcada, vale o comportamento descrito em [Empresa optante pelo Simples Nacional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Cadastro-de-Al%C3%ADquotas-de-ISS#optante).

**ℹ️ Nota**

A alíquota usada no cálculo e no destaque do ISS é a mesma enviada ao Nota Gateway no campo `aliquotaIss` do arquivo JSON da NFS-e.
