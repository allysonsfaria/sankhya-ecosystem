---
id: "360044601474"
titulo: "Integração NFS-e / NDD SankhyaOm / JivaOm"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601474-Integra%C3%A7%C3%A3o-NFS-e-NDD-SankhyaOm-JivaOm"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:51:30Z"
rotulos: ["Configuração", "Serviço", "Parceiro", "Conector NFS-e", "JobKey NDDigital", "NDD", "NFS-e Monitor", "Integração NFS-e / NDD Sankhya-W manual", "Integração", "Prefeituras", "NFS-e", "Integração com NDD para NFS-e: Simplificando Processos Municipais", "NDD Digital"]
---

# Integração NFS-e / NDD SankhyaOm / JivaOm

O objetivo desta integração é possibilitar no sistema a associação com o parceiro **"NDD Digital"** para automatização de integrações junto as Prefeituras para as demandas de Nota fiscal de Serviço Eletrônica. Desta forma, foi feita uma parceria com um especialista nesta solução, a NDD, que ficará responsável pela parte de envio, aprovação e retorno das informações necessárias para as NFS-e's, sendo que este hoje já possui uma grande gama de cidades atendidas com a solução de NFS-e.

O NFS-e Web Service da NDD é um serviço WEB, responsável pela comunicação entre o ERP e o sistema de processamento de Nota Fiscal de Serviço eletrônica, desenvolvido pela NDDigital. Através do NFS-e Web Service, é possível enviar RPS, cancelar NFS-e, consultar RPS e NFS-e.

Na prática, o SankhyaOm irá tratar a NDD como uma Prefeitura, enviando via XML/Webservices os dados para o Servidor NDD, onde será processada a informação, e a partir da NDD o envio para a Prefeitura especifica; deste modo, estes irão receber o retorno da Prefeitura, e nos transmitir estas informações retornadas da Prefeitura, sendo que em caso de erros, o mesmo irá ocorrer.

O sistema de integração também permite a utilização dos ambientes de Homologação e Produção, porém no caso do ambiente de homologação, existe a dependência da disponibilidade da prefeitura, que em alguns casos não existe.

Vejamos o fluxo funcional da integração NDD / NFS-e:

![Imagem 1: Vejamos o fluxo funcional da integração NDD / NFS-e:](https://ajuda.sankhya.com.br/hc/article_attachments/9219189284759)

**Premissas para utilização**

**1)** Entrar em contato com a área Comercial Sankhya, e verificar a disponibilidade da NFS-e para a cidade onde a empresa está localizada.

**2)** Preencher o formulário de cadastro encaminhado pelo Departamento Comercial Sankhya.

**3)** Realizar a abertura de uma OS com a solicitação de integração, anexando nesta o formulário.

**4)** Anexar o arquivo do Certificado Digital no modelo A1 e sua correspondente senha, através do formulário mencionado no item 2.

**5)** Solicitar/confirmar o credenciamento junto a Prefeitura da cidade da empresa, em que será utilizada a NFS-e. Importante: Se a empresa não for liberada para utilizar via Webeservices, esta não irá conseguir utilizar a emissão de NFS-e por esta modalidade.

**6)** Solicitar os acessos (usuário/senha) do portal da Prefeitura para utilização da NFS-e; na Ordem de Serviço que é aberta no item 3, deve-se mencionar os dados de acesso ao portal da Prefeitura.

**7)** Feito o cadastramento e tendo-se a liberação pela Sankhya e NDD, será liberado o Job ID (NDD), que deverá ser informado na tela **"Comercial > Preferências > Empresa"** (detalharemos esta configuração mais adiante).

**8)** Deve-se adquirir a licença para o produto **"30658- NDDigital - Nota fiscal de serviço eletrônica/W"**. Para Jiva, adquira a licença **"20487 - JIVA-NFS-e NDDIGITAL /W"**.

**Importante:** os dados da empresa informados no item 2, devem ser relacionados à empresa situada na cidade a ser integrada. Caso esta possua filiais que também serão integradas, deve-se preencher um formulário para cada cidade, e da mesma forma, abrir-se uma OS para cada filial.

**9)** Estar com as versões adequadas e necessárias para utilização da integração, que são:

- SankhyaOm - Versão 3.8 ou superior.
- JivaOm - Versão 3.8 ou superior.
- SanNFe - Versão 2.18b9 ou superior.

**10)** Baixar o manual de orientação da Prefeitura e efetuar a leitura do mesmo,  pois os dados de cada Município são distintos, assim como alíquota, código de tributação no município, Natureza do ISS,  Regime especial de Tributação (que geralmente variam). Deve-se atentar para estes detalhes/dados  que são configuráveis.

Para utilização desta integração, são necessárias algumas configurações no sistema. São elas:

**Comercial > Arquivo > Cadastros > Tipos de Operação - TOP**

Nesta tela, na aba Livro Fiscal, quando a empresa utilizar a integração com a NDD, se faz necessária a configuração do campo **"Cód. Natureza Oper. ISS (NFS-e)"**.

![Imagem 2: Nesta tela, na aba Livro Fiscal , quando a empresa utilizar a integração com a NDD, se faz necessária a configuração do…](https://ajuda.sankhya.com.br/hc/article_attachments/9219194709271)

Para o campo mencionado, tem-se a seguinte lista de opções:

| 1 - Tributação no Município;  2 – Tributação fora do Município;  3 – Isenção;  4 – Imune;  5 – Exigibilidade suspensa por decisão judicial;  6 – Exigibilidade suspensa por procedimento administrativo;  7 – Sem dedução;  8 – Com dedução / Materiais;  9 – Imune / Isenta de ISSQN;  10 – Devolução / Simples remessa;  11 – Intermediação;  12 – Prestação de serviço;  13 – Simples remessa;  14 – Anulada;  15 – Vencida;  16 – Tributada integralmente;  17 – Tributada integralmente com ISSRF;  18 – Tributada integralmente e sujeita a substituição tributária; | 19 – Tributada com redução da base de cálculo;  20 – Tributada com redução da base de cálculo com ISSRF;  21 – Tributada com redução de cálculo e sujeita a substituição tributária;  22 – Não tributada – ISS regime fixo;  23 – Não tributada – ISS regime estimativa;  24 – Não tributada – ISS construção civil recolhido antecipadamente;  25 – Não tributada – Ato cooperado;26 – Tributada no prestador;  27 – Tributada no tomador;  28 – Tributado Fixo;  29 – Isenta/Imune;  30 – Outro município;  A - Sem Dedução;  B - Com Dedução/Materiais;  C - Imune/Isenta de ISSQN;  D - Devolução/Simples Remessa;  J - Intemediação. |
| --- | --- |

As opções acima que se encontram sublinhadas, são opções inerentes ao sistema, e também são válidas para a NDD. Caso não se possua a integração com NDD, as opções apresentadas no campo **"Cód. Natureza Oper. ISS (NFS-e)"** serão apenas as alternativas sublinhadas.

A informação a ser definida neste campo, deve ser verificada no manual disponibilizado pela Prefeitura  e confirmada juntamente ao setor fiscal da Empresa, para se chegar a opção correta a ser utilizada.

**Comercial > Preferências > Empresa**

Na aba **"NFS-e"**, deve-se atentar para a configuração de alguns campos, que irão influenciar diretamente no sucesso ou fracasso da emissão na NFS-e via integração com a NDD. Primeiramente, tem-se o campo **"Regime esp. tributação ISS (NFS-e)"**:

![Imagem 3: Na aba "NFS-e" , deve-se atentar para a configuração de alguns campos, que irão influenciar diretamente no sucesso ou…](https://ajuda.sankhya.com.br/hc/article_attachments/9219203031575)

Este campo deve ser configurado, caso a Prefeitura possua esta informação a ser prestada na NFS-e. Vejamos abaixo as opções nativas disponíveis para definição neste campo, e suas opções equivalentes quando se utiliza a integração com  NDD:

| Nativo do Sistema | Com a NDD |
| --- | --- |
| 1 - Microempresa municipal  2 - Estimativa  3 - Sociedade de profissionais  4 - Cooperativa  5 - MEI (Simples Nacional)  6 - ME EPP  (Simples Nacional)  C - senta de ISS  E - Não Incidência no Município  F - Imune  G - Tributável Fixo  H - Tributável S.N.  K - Exigibilidd Susp.Dec.J/Proc.A  N - ão Tributável  T – Tributável | 1 - Microempresa Municipal;  2 – Estimativa;  3 – Sociedade de profissionais;  4 – Cooperativa;  5 – MEI – Simples Nacional;  6 – ME EPP – Simples Nacional;  7 – Isenta de ISS;  8 – Não incidência no município;  9 – Imune;  10 – Exigibilidade Susp.Dec J/Proc.A;  11 – Não tributável;  12 – Tributável;  13 – Tributável fixo;  14 – Tributável S.N; |

Foram criados os campos **"JobKey NDDigital"** e **"Conector NFS-e"**.

![Imagem 4: Foram criados os campos "JobKey NDDigital" e "Conector NFS-e" .](https://ajuda.sankhya.com.br/hc/article_attachments/9219639666967)

No campo **"JobKey NDDigital"** informa-se o código da empresa no servidor na NDD, identificando seu acesso.

Já no campo **"Conector NFS-e"** tem-se duas opções de escolha, a saber:

- **ND Digital:** Por esta opção, indica-se que a NFS-e será utilizada pela Integração da NDD.
- **Nativo do sistema:** Esta alternativa, define que a NFS-e será enviada diretamente pelo sistema Sankhya-Om, apenas no caso de existir a integração nativa desenvolvida pela Sankhya.

Para que seja possível enviar notas utilizando a integração NDD, a empresa deverá ter um JobKey cadastrado na NDDigital; para isso, é necessário preencher um formulário com os dados da Empresa e a ND Digital irá disponibilizar um código **"JobKey"**, onde serão trafegadas as requisições. Para cada empresa que irá utilizar a integração, deve-se possuir um JobKey.

**Observação:** é necessário verificar qual o código que a Prefeitura local utiliza, e se o utiliza, pois as faixas indicadas com os números (1 a 6), são para um determinado padrão de Prefeitura e as faixas compostas por letras, são para utilização de outro padrão.

**Importante:** caso a empresa tenha passado (e solucionado) por alguma questão comercial e contratual juntamente a NDD, os dois campos mencionados acima, devem ser modificados para **"em branco"** (sem nenhuma informação) e **"Nativo do Sistema"**, respectivamente.

**Configurar o SankhyaOm / SanNFe - Conexão**

Para utilização da integração com a NDD, é necessário incluir o certificado digital da empresa no SanNFe, através da tela **"Comercial > Configuração > Console NF-e"** no SankhyaOm.

Como já relatado inicialmente nas premissas para utilização, é necessário que o SankhyaOm esteja na versão 3.8 ou superior, e o SanNFe na versão 2.18b9 ou superior.

Uma outra característica de suma importância, é premissa de funcionamento, a existência de conexão com a internet para comunicação junto a Prefeitura; além disso, o endereço do IP referente ao servidor local de acessos da internet, deve ser informado no parâmetro **"IP do Servidor de Nota Fiscal Eletrônica - IPSERVNFE"** acessado através da tela **"Configurações > Avançado > Preferências"**.

#### Cadastros envolvidos para emissão de Notas de Serviço

**Comercial > Preferências > Empresa**

- **Aba NFS-e**

Ambiente NFS-e: Homologação / Produção (definir o ambiente);

Incentivador cultural: desmarcado;

Reg.Esp.Tributação ISS: Microempresa Municipal (de acordo com cada Empresa; informação vinda da contabilidade).

- **Aba CNAE Empresa**

Se a Empresa possuir mais de um CNAE, deve-se informar na aba CNAE os CNAE’s existentes.

**Configurações > Cadastros > Parceiros**

Deve-se preencher os dados cadastrais corretamente, bem como dados de endereço, CEP, CPF/CNPJ, Inscrição Municipal; são dados necessários de acordo com o cadastro na Prefeitura, e são validados no envio da nota fiscal.

**Configurações > Cadastros > Produtos > Serviço**

Define-se na aba Impostos, o campo **"Tem ISS"** com **"Tributado"**, preenche-se o **"Cód. de Trib. Município NFS-e"** (listagem adquirida junto a Prefeitura) e o **"CNAE"** da empresa.

Além disso, informa-se no campo **"Tipo de serviço"**, o código da atividade/Lista de serviços (lista LCP 116), referente ao serviço cadastrado.

Exemplo: "Tipo de Serviço": 1701 – "Assessoria ou consultoria de qualquer natureza..."

Exemplo: "Cód. de Trib. Município NFS-e": 639920000

#### Configurações > Cadastros > Endereços > Cidades

Informa-se no campo **"Mun. domicílio fiscal"**; código este fornecido pelo IBGE.

**Comercial > Arquivo > Cadastros > Alíquotas > Alíquotas ISS**

Configura-se a alíquota de ISS com o percentual informado pela Prefeitura e de acordo com a Lista de serviços.

**Comercial > Arquivo > Cadastros > Tipos de Operação - TOP**

Deve-se criar uma TOP específica para a emissão de NFS-e, e configurar nesta, os seguintes campos:

- **Aba Livro fiscal**

**Cód. Natureza Oper. ISS (NFS-e):** Exemplo: Tributado no município (verifica-se esta informação junto a contabilidade); se existirem operações onde possam ocorrer as tributações no município e outra Tributação fora do município (no caso de cidades distintas) é necessário que existam TOP's diferentes, visto que na TOP só se pode utilizar uma Natureza de operação.

**Modelo do documento:**  01 – Nota fiscal

- **Aba Impressão**

**NFS-e:** Normal

**Mod. Imp. NFS-e:** Se existir.

**Mod. Imp. RPS:** Se existir.

**NFS-e por Natureza:** Marca-se apenas se for necessário.

**Modelo do Documento:** 01 - Nota Fiscal

Configurar numeração das notas (se já foram realizadas emissões por outro sistema ou direto no site da Prefeitura, deve-se verificar o último número gerado, para que se mantenha a sequencia correta).

**Configurações > Cadastros > Impostos**

Os impostos federais retidos (PIS,COFINS,IR,CSLL) devem ser configurados nesta tela, seguindo as configurações de retenção já existentes no sistema.

**Portal de Vendas - Central de Vendas**

- Utiliza-se a Central de Vendas - Portal de Vendas para emissão das Notas fiscais de prestação de serviços e envio das notas para a Prefeitura posteriormente.
- Informa-se os dados necessários, Empresa, TOP, Parceiro, Tipo de Negociação, Serviço prestado (configurações citadas acima), valores etc.
- Utiliza-se a aba Serviços disponível na grade de itens, para informar os códigos dos respectivos serviços prestados.
- Depois de informados os dados desejados corretamente, valores, impostos, confirma-se a  nota.
- No Portal de Vendas, nos Resultados de Seleção, pode ser enviada uma nota ou várias mantendo-se pressionado o botão "Ctrl" no teclado, selecionando-se as notas desejadas e escolhendo-se no botão "NFS-e" a opção desejada.
- Em relação a cidade de execução do serviço, caso seja necessário informar esta diferente da cidade do parceiro, na Central de Vendas na aba Impostos da nota, consta um campo para informar o código da cidade onde ocorreu a execução do Serviço. O padrão é que este campo fique vazio, considerando a cidade do parceiro como local da execução.
- Após aprovação das notas, pode-se acessar o site de homologação da Prefeitura e efetuar a consulta das notas, e a conferência se esta consta corretamente conforme estava no Sankhya-Om, bem como a emissão/impressão da NFS-e pelo site da Prefeitura.

**Monitor NDD**

Para verificar a situação de uma nota fiscal enviada, pode-se acessar o site/monitor disponibilizado pela NDD; com este acesso, será possível consultar a situação, status ou ocorrência das notas em processamento ou já processadas. O usuário e senha, são os fornecidos pela NDD, na etapa de cadastro.

Abaixo tem-se o link para o NFS-e Monitor de **"Homologação"**:

http://nfsehl.e-datacenter.nddigital.com.br/NFSeMonitor/Default.aspx

Além deste, tem-se o link para o NFS-e Monitor de **"Produção"**:

http://nfse.e-datacenter.nddigital.com.br/NFSeMonitor/logon.aspx?sys=NFS&msgKey=

Vejamos a tela de acesso NFS-e Monitor da NDD:

![Imagem 5: Vejamos a tela de acesso NFS-e Monitor da NDD:](https://ajuda.sankhya.com.br/hc/article_attachments/9219693224087)

Vejamos na imagem abaixo, a tela onde são realizadas as consultas do NFS-e Monitor, onde tem-se na lateral esquerda da tela os filtros para realização das consultas, e na parte superior, as notas retornadas pela consulta realizada.

![Imagem 6: Vejamos na imagem abaixo, a tela onde são realizadas as consultas do NFS-e Monitor, onde tem-se na lateral esquerda da…](https://ajuda.sankhya.com.br/hc/article_attachments/9219695739671)

É de suma relevância efetuar o backup da base, e realiza-se as simulações em uma base de testes direcionada para o ambiente de Homologação antes de utilizar-se em Produção. Nunca se deve utilizar a base de Produção direcionada para o ambiente de Homologação da prefeitura e a base de testes direcionada para Produção.

**Consulta de erros no NFS-e Monitor**

Caso tenham ocorrido erros na emissão da NFS-e, pode-se também consultá-los através do NFS-e Monitor.

![Imagem 7: Caso tenham ocorrido erros na emissão da NFS-e, pode-se também consultá-los através do NFS-e Monitor.](https://ajuda.sankhya.com.br/hc/article_attachments/9219709773463)

Erros informados na coluna Status como **"Erro de negócio"** indicam que existe algum problema nos dados informados, por exemplo:

Erro do código de tributação:

Código de tributação no município inexistente > E35 - Código de tributação inexistente

CNAE Inexistente > NDD: E33 - Código CNAE inexistente

**Solução:** Deve-se verificar se foi informado no Cadastro de Serviços, o código de tributação referente a cidade de utilização.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601474-Integra%C3%A7%C3%A3o-NFS-e-NDD-SankhyaOm-JivaOm#voltaraotopo])
