---
id: "23005245015191"
titulo: "Geração do Grupo JA. Detalhamento Específico de Veículos novos na NF-e (veicProd)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/23005245015191-Gera%C3%A7%C3%A3o-do-Grupo-JA-Detalhamento-Espec%C3%ADfico-de-Ve%C3%ADculos-novos-na-NF-e-veicProd"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:42:38Z"
rotulos: ["Produtos", "Configuração", "Veículos", "NF-e", "RATEIOPORVEICU", "XML", "Estoque", "FILTRAVEICCTRL", "VINPRODVEINFE", "BLOQCADPLACADUP", "Configurações » Cadastros » Produtos » Produtos", "Configurações » Cadastros » Veículos", "Comercial » Arquivo » Cadastros » Tipos de Operação - TOP", "Comercial » Consulta » Portal de Vendas", "pesoB", "pesoL"]
---

# Geração do Grupo JA. Detalhamento Específico de Veículos novos na NF-e (veicProd)

Na emissão da Nota Fiscal Eletrônica (NF-e) para a venda de veículos novos, a correta geração das informações no grupo Detalhamento de Veículos Novos (veicProd) é crucial para cumprir as exigências fiscais e garantir a conformidade do processo. Este artigo aborda de forma detalhada os procedimentos necessários para configurar adequadamente as tags desse grupo, conhecido como Grupo JA.

Nesta operação, visando um controle mais adequado e a prevenção de falhas na emissão do documento, é essencial realizar não apenas o cadastro do produto a ser negociado na NF-e, mas também o registro detalhado dos veículos em estoque, incluindo todas as suas particularidades. Esse processo não apenas agiliza o faturamento, mas também garante a precisão e integridade das informações na nota fiscal emitida.

Esse processo não apenas agiliza o faturamento, mas também garante a precisão e integridade das informações na nota fiscal emitida.

**Hierarquia de Pesos na NF-e (Grupo veicProd)**

É possível informar o **Peso Bruto** e o **Peso Líquido** diretamente na tela de Cadastro de Veículos. Para a geração das tags `<pesoB>` e `<pesoL>` no XML, **os dados preenchidos no veículo têm prioridade máxima**.

O sistema sempre obedecerá a seguinte ordem no momento do faturamento:

1. **Cadastro do Veículo (Prioridade 1):** O sistema busca o peso aqui primeiro.
2. **Cadastro do Produto (Secundário):** Usado apenas se o cadastro do veículo não possuir o peso informado.
3. **Sem peso:** Se nenhum dos cadastros possuir a informação, a NF-e é gerada sem as tags de peso, não bloqueando o faturamento.

Acesse os links abaixo para realizar as configurações necessárias:

| Configurações e telas envolvidas | |
| --- | --- |
| [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/23005245015191-Gera%C3%A7%C3%A3o-do-Grupo-JA-Detalhamento-Espec%C3%ADfico-de-Ve%C3%ADculos-novos-na-NF-e-veicProd#CadastrodeProdutos) | [Cadastro de Veículos](https://ajuda.sankhya.com.br/hc/pt-br/articles/23005245015191-Gera%C3%A7%C3%A3o-do-Grupo-JA-Detalhamento-Espec%C3%ADfico-de-Ve%C3%ADculos-novos-na-NF-e-veicProd#CadastrodeVeiculos) |
| [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/23005245015191-Gera%C3%A7%C3%A3o-do-Grupo-JA-Detalhamento-Espec%C3%ADfico-de-Ve%C3%ADculos-novos-na-NF-e-veicProd#TiposdeOpera%C3%A7%C3%A3o) | [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/23005245015191-Gera%C3%A7%C3%A3o-do-Grupo-JA-Detalhamento-Espec%C3%ADfico-de-Ve%C3%ADculos-novos-na-NF-e-veicProd#CentraldeVendas) |
| [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/23005245015191-Gera%C3%A7%C3%A3o-do-Grupo-JA-Detalhamento-Espec%C3%ADfico-de-Ve%C3%ADculos-novos-na-NF-e-veicProd#PortaldeVendas) |  |

## Cadastro de Produtos

Na tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos), é recomendável a realização de um registro para cada modelo e versão, em vez de cada ano de fabricação/ano de modelo. Isso se deve ao fato de que o controle correspondente será conduzido no [Cadastro de Veículos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111533-Ve%C3%ADculos).

Ao cadastrar um produto, é crucial especificar o **"Peso bruto"** e o **"Peso líquido"** localizados na aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque), sub-aba [Medidas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abamedidas). Os valores inseridos nestes campos atuarão de forma secundária na geração das tags `<pesoL>` e `<pesoB>`.

Nesse caso, o sistema só utilizará os pesos do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos) caso o [Cadastro do Veículo](https://ajuda.sankhya.com.br/hc/pt-br/articles/32275684636695-Cadastro-de-Ve%C3%ADculos) (que tem prioridade) esteja com os campos de peso vazios.

![Imagem 1: Nesse caso, o sistema só utilizará os pesos do Cadastro de Produtos caso o Cadastro do Veículo (que tem prioridade)…](https://ajuda.sankhya.com.br/hc/article_attachments/23214539453975)

Além disso, na sub-aba [Controle Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abacontroleadicional) é necessário que a opção **"Livre"** seja selecionada no campo **"Controlar Por"**e, o campo **"Título"** preenchido com o título **"Chassis"**.

![Imagem 2: Além disso, na sub-aba Controle Adicional é necessário que a opção "Livre" seja selecionada no campo "Controlar Por" e,…](https://ajuda.sankhya.com.br/hc/article_attachments/23212026062999)

**Nota:** caso o sistema do Controle Adicional não suporte os 17 caracteres necessários para identificar o número do chassis, é necessário ajustar o número de caracteres nos campos das tabelas relacionados a esse Controle Adicional.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/23005245015191-Gera%C3%A7%C3%A3o-do-Grupo-JA-Detalhamento-Espec%C3%ADfico-de-Ve%C3%ADculos-novos-na-NF-e-veicProd#top)

## Cadastro de Veículos

Na tela Cadastro de Veículos serão registrados todos os veículos em estoque, com indicação da empresa, produto e número de chassis. Estes últimos servirão como a chave de ligação entre o item negociado no documento e o veículo cadastrado em estoque.

Ao configurar essa tela, pode-se organizar os campos de entrada de dados de forma lógica e intuitiva, além de personalizar as configurações conforme as necessidades específicas da empresa e do processo de gestão de estoque. Essa otimização facilitará o registro ágil e preciso de novos veículos, contribuindo para uma operação mais eficiente e livre de erros no controle de estoque.

Desse modo, configure as seguintes abas:

### Aba Propriedades

![Imagem 3: Aba Propriedades](https://ajuda.sankhya.com.br/hc/article_attachments/23033346460823)

Na negociação de veículos novos, uma vez que ainda não foram emplacados, o conteúdo dos campos **"Placa"** e **"Cidade Emplacamento"** devem ser preenchidos com zero, pois essas informações atualmente não estão previstas na geração do grupo **<veicProd>**. Para permitir que o sistema inclua veículos novos com a mesma indicação de Placa para diversos veículos é necessário desativar o parâmetro **"Bloquear cadastro de placas em duplicidade - BLOQCADPLACADUP"**.

No campo **"Parceiro ou Empresa"** informe a empresa a qual pertence o veículo em estoque.

Informe no campo **"Cor"** o código da cor do veículo segundo as regras de pré-cadastro do DENATRAN (v2.0), sendo elas:

- 1 - AMARELO;
- 2 - AZUL;
- 3 - BEGE;
- 4 - BRANCA;
- 5 - CINZA;
- 6 - DOURADA;
- 7 - GRENÁ;
- 8 - LARANJA;
- 9 - MARROM;
- 10 - PRATA;
- 11 - PRETA;
- 12 - ROSA;
- 13 - ROXA;
- 14 - VERDE;
- 15 - VERMELHA;
- 16 - FANTASIA.

No campo **"Número do Motor"** defina a numeração do motor e o ano de fabricação do veículo no campo **"Ano Fabricação"**. 

Informe o ano do modelo do veículo no campo **"Ano Modelo"**. 

No campo **"Cap/Pot/Cil"**, indique a cilindrada do veículo.

Preencha o número do **"Chassis"** do veículo e no campo **"RENAVAM"**, o valor zero, pois essa informação atualmente não está prevista na geração do grupo **<veicProd>**.

Informe também o **"Peso Bruto"** e o **"Peso Líquido"** do veículo (campos localizados abaixo do campo Peso Máximo na tela de [Cadastro de Veículos](https://ajuda.sankhya.com.br/hc/pt-br/articles/32275684636695-Cadastro-de-Ve%C3%ADculos)). Conforme a nova regra de prioridade do sistema, os valores preenchidos nestes dois campos serão a fonte principal de informação para gerar o peso do veículo na NF-e.

### Aba Informações Complementares

![Imagem 4: Aba Informações Complementares](https://ajuda.sankhya.com.br/hc/article_attachments/23053676025751)

Selecione no campo **"Aferição"** a opção **"Não Usa"**, pois essa informação atualmente não está prevista na geração do grupo <veicProd>.

Informe no campo **"Cap. Máx. de Tração"** a capacidade de tração do veículo e, no campo **"Capacidade Máxima de Lotação"**, a capacidade máxima permitida de passageiros sentados, inclusive o motorista. 

Determine o código da marca e modelo do veículo no campo **"Cód.Marca/Modelo"** conforme tabela RENAVAM.

Informe no campo **"Código da Cor (Tabela DENATRAN)"** o código da cor do veículo segundo as regras de pré-cadastro do DENATRAN (v2.0). 

Selecione a condição do veículo no campo **"Condição do Veículo"** conforme as opções:

- 1 - Acabado;
- 2 - Inacabado;
- 3 - Semiacabado.

No campo **"Condição do VIN"** informe se o veículo tem VIN (chassi) **"Remarcado"** ou **"Normal"**. 

Selecione no campo **"Cor Fabricante"** a cor de fabricação do veículo.

Através do campo **"Tipo de Veículo"**, informe o tipo do veículo conforme Tabela RENAVAM, sendo eles:

- 2 - CICLOMOTO;
- 3 - MOTONETA;
- 4 - MOTOCICLO;
- 5 - TRICICLO;
- 6 - AUTOMÓVEL;
- 7 - MICROÔNIBUS;
- 8 - ÔNIBUS;
- 10 - REBOQUE;
- 11 - SEMIRREBOQUE;
- 13 - CAMINHONETA;
- 14 - CAMINHÃO;
- 17 - C.TRATOR;
- 22 - ESP/ÔNIBUS;
- 23 - MISTO/CAM.

Determine a distância entre os eixos no campo **"Distância entre Eixos"** e, no campo **"Espécie de Veículo"** preencha a espécie do veículo conforme tabela RENAVAM, sendo elas:

- 1 - PASSAGEIRO;
- 2 - CARGA;
- 3 - MISTO;
- 4 - CORRIDA;
- 5 - TRAÇÃO;
- 6 - ESPECIAL.

Informe a **"Potência"** do veículo e, no campo **"Restrição"**, a restrição conforme as seguintes opções:

- 0 - Não há;
- 1 - Alienação Fiduciária;
- 2 - Arrendamento Mercantil;
- 3 - Reserva de Domínio;
- 4 - Penhor de Veículos;
- 9 - Outras.

Utilize o campo **"Serial"** para informar a série do veículo.

No campo **"Tipo de Combustível (Tabela RENAVAM)"** preencha o código conforme a tabela RENAVAM (v2.0), sendo eles:

- 1 - Álcool;
- 2 - Gasolina;
- 3 - Diesel;
- 16 - Álcool/Gasolina;
- 17 - Gasolina/Álcool/GNV;
- 18 - Gasolina/Elétrico.

Através do campo **"Tipo Pintura"** informe o tipo de pintura aplicada ao veículo. 

#### Código do Veículo no Cadastro de Produtos

![Imagem 5: Para que esta seção seja visualizada é necessário a ativação dos parâmetros "Vincular produto a um veículo p/ Geração…](https://ajuda.sankhya.com.br/hc/article_attachments/23055650103831) Para que esta seção seja visualizada é necessário a ativação dos parâmetros **"Vincular produto a um veículo p/ Geração da NFE - VINPRODVEINFE"** e **"Usar rateio por veículo? - RATEIOPORVEICU"**.

No campo **"Produto"**, o código do produto vinculado ao veículo deve corresponder ao produto a ser negociado durante a venda dele na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/23005245015191-Gera%C3%A7%C3%A3o-do-Grupo-JA-Detalhamento-Espec%C3%ADfico-de-Ve%C3%ADculos-novos-na-NF-e-veicProd#top)

## Tipos de Operação - TOP

Na tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), a TOP utilizada na negociação de veículos novos, além das configurações para geração da NF-e, requer que a marcação **"Gerar tag na NF e para Negociação de Veículos Novos"** da aba [NF-e/NFC-e/CF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce/cfe) esteja ativada.

![Imagem 6: Na tela Tipos de Operação - TOP , a TOP utilizada na negociação de veículos novos, além das configurações para geração…](https://ajuda.sankhya.com.br/hc/article_attachments/23058422367895)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/23005245015191-Gera%C3%A7%C3%A3o-do-Grupo-JA-Detalhamento-Espec%C3%ADfico-de-Ve%C3%ADculos-novos-na-NF-e-veicProd#top)

## Central de Vendas

Na tela [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), durante a negociação, utiliza-se a TOP configurada no passo anterior. Logo após, no campo **"Tipo de Operação Veículos Novos"** da [Grade Cabeçalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradecabealho), selecione entre as opções disponíveis a operação que está sendo realizada. 

![Imagem 7: Na tela Central de Vendas , durante a negociação, utiliza-se a TOP configurada no passo anterior. Logo após, no campo…](https://ajuda.sankhya.com.br/hc/article_attachments/23161552560535)

Na [Grade de Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens), registre o produto associado ao veículo novo e no campo **"Controle"**, insira o número do chassis correspondente ao veículo em negociação.

**Nota**: para identificar o veículo negociado com base no chassis informado é necessário ativar o parâmetro **"Filtrar veículos com Chassi igual ao Controle - FILTRAVEICCTRL"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/23005245015191-Gera%C3%A7%C3%A3o-do-Grupo-JA-Detalhamento-Espec%C3%ADfico-de-Ve%C3%ADculos-novos-na-NF-e-veicProd#top)

## Portal de Vendas

No [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas), após a realização das configurações e o lançamento do documento no formato sugerido, ao clicar no botão ![Imagem 8: No Portal de Vendas , após a realização das configurações e o lançamento do documento no formato sugerido, ao clicar no…](https://ajuda.sankhya.com.br/hc/article_attachments/23212999319831) **"NF-e"** e selecionar a opção **"Gerar XML da NFe em arquivo para conferência"**, o sistema irá gerar o XML da NF-e com o grupo **<veicProd>** completo.

![Imagem 9: No Portal de Vendas , após a realização das configurações e o lançamento do documento no formato sugerido, ao clicar no…](https://ajuda.sankhya.com.br/hc/article_attachments/23161812587159)

Em caso de dúvidas sobre o Grupo JA. Detalhamento Específico de Veículos novos consulte o [MOC 7.0 – Anexo I, Leiaute e Regras de Validação da NF-e e da NFC-e](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=J%20I%20v4eN00E=).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/23005245015191-Gera%C3%A7%C3%A3o-do-Grupo-JA-Detalhamento-Espec%C3%ADfico-de-Ve%C3%ADculos-novos-na-NF-e-veicProd#top)
