---
id: "40877721221783"
titulo: "Configuração de Integração com a plataforma MULTICTE"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40877721221783-Configura%C3%A7%C3%A3o-de-Integra%C3%A7%C3%A3o-com-a-plataforma-MULTICTE"
trilha: "Sankhya Official Pack - SOP > TMS"
atualizado_em: "2026-07-22T13:27:08Z"
rotulos: ["MDF-e", "CT-e", "Configuração", "XML", "Importação", "Transporte", "MULTICTE", "Plataforma MULTICTE", "Documentos Multi-CTe", "Configuração de Integração", "Multi-Embarcador"]
---

# Configuração de Integração com a plataforma MULTICTE

Integração da viagem do TMS com a plataforma MULTICTE. Abaixo, seguem os detalhes das configurações necessárias.

**Ao instalar o addon, serão incluídas as seguintes ações agendadas:**

**(1)** **Importar Documentos Multi-CTe**: Para conectar no Multicte e baixar os xmls para a base.

**(2)** **Processar Documentos Multi-CTe**: Para processar o xml e gerar o documento no sankhya, sendo ct-e ou mdf-e.

![Imagem 1: (2) Processar Documentos Multi-CTe : Para processar o xml e gerar o documento no sankhya, sendo ct-e ou mdf-e.](https://ajuda.sankhya.com.br/hc/article_attachments/40877721201687)

#### Tela Configuração Multi CT-e

A tela **''Configuração Multi CT-e''** (Comercial → Rotinas → Configuração Multi CT-e) tem como objetivo de centralizar todas as configurações necessárias para realizar o download dos arquivos e importação para o Sankhya.

![Imagem 2: A tela ''Configuração Multi CT-e'' (Comercial → Rotinas → Configuração Multi CT-e ) tem como objetivo de centralizar…](https://ajuda.sankhya.com.br/hc/article_attachments/40877683567639)

No painel principal temos os campos:

(1)** Código**: Indica o código da configuração pois podem ter mais de uma.

(2)** Descrição**: Ajuda a identificar a configuração.

(3)** Ativo**: Utilizado para indicar se esta configuração esta ativa ou não, apenas as ativas serão consideradas para o processamento.

(4)** Tipo Integração**: A Multicte possui mais de uma api de integração, classificamos elas como **Multi-CT-e** e **Multi-Embarcador**, a diferença entre elas é a estrutura do XML da requisição:

- Para o tipo **Multi-CT-e** precisamos utilizar uma url para obter uma lista de protocolos através do soapaction: ObterProtocolos baseado em um período e depois utilizar o soapaction ObterXML para obter o xml baseado no protocolo obtido anteriormente.
- Depois a Multict-e criou uma nova api onde podemos obter de uma vez apenas os xml, através do soapaction: BuscarCTesPorPeriodo onde baixamos os arquivos baseado em um período.

Em ambos os casos a rotina salva a data da execução no campo **''Data Última Execução''** para que na próxima chamada utilize esta data como base para buscar apenas os registros gerados desde a última consulta.

#### Aba Geral

**URL CT-e**: Neste campo precisa ser incluído a url da api de acesso ao dados do cliente para baixar os CT-es, em alguns casos o cliente pode ter uma url diferente para cada empresa.

**URL MDF-e**: URL da api para baixar o MDF-e.

**Diretório p/ Importar XML CT-e/MDF-e**: Quando o tipo configurado for diretório, precisamos incluir neste campo o diretório do servidor ou do repositório de arquivos para que a rotina busque os xml de CT-e e MDF-e deste diretório ao invés de buscar direto no Multicte.

**Natureza**: Ao criar o CT-e no Sankhya será preenchido a Natureza conforme configurado neste campo.

**Centro de Resultado**: Ao criar o CT-e no Sankhya será preenchido o Centro de Resultado conforme configurado neste campo.

**Data Última Execução**: Data da última execução.

#### Aba Empresas

Nesta aba, são configuradas as empresas e seus respectivos tokens de acesso para a URL informada na aba **''Geral''**. Os CT-es importados serão incluído com esta empresa.

![Imagem 3: Nesta aba, são configuradas as empresas e seus respectivos tokens de acesso para a URL informada na aba ''Geral'' . Os…](https://ajuda.sankhya.com.br/hc/article_attachments/40877721204247)

#### Aba Mensagens Importador

Nesta aba são salvas as mensagens de falha geradas durante a importação e geração dos registros no Sankhya.

![Imagem 4: Nesta aba são salvas as mensagens de falha geradas durante a importação e geração dos registros no Sankhya.](https://ajuda.sankhya.com.br/hc/article_attachments/40886497849751)

#### Aba Observação

Nesta aba, configuramos como obter a placa do veículo, o CPF do motorista e o número da carga do cliente a partir do campo **''Observação do CT-e''**. Para isso, é necessário informar o texto que antecede e o que sucede cada informação desejada. Quando o texto terminar com espaço em branco, utilize o caractere \_ (underline), pois o Sankhya remove os espaços ao final do texto.

![Imagem 5: Nesta aba, configuramos como obter a placa do veículo, o CPF do motorista e o número da carga do cliente a partir do…](https://ajuda.sankhya.com.br/hc/article_attachments/40877683571863)

#### Aba Tipos de Operação

Nesta aba, é configurado o Tipo de Operação do Sankhya que será utilizado para cada tipo de serviço do CT-e:

- Normal;
- Redespacho Intermediário;
- Redespacho, Subcontratação;
- Serviço Vinculado ao Multimodal.

Também são configurados os Tipos de Operação para cada tipo de documento:

- CT-e Normal;
- CT-e de Anulação;
- CT-e Substituto;
- CT-e Normal com CST 60;
- CT-e Normal de Exportação (Art. 79);
- CT-e Normal entregue na mesma UF do carregamento;
- CT-e Normal iniciado em UF diferente da UF da empresa.

![Imagem 6: CT-e Normal iniciado em UF diferente da UF da empresa.](https://ajuda.sankhya.com.br/hc/article_attachments/40877721206807)

#### Tela de Documentos Multi CT-e

![Imagem 7: Tela de Documentos Multi CT-e](https://ajuda.sankhya.com.br/hc/article_attachments/40886447597207)

Quando a ação agendada realiza o download dos arquivos XML da MultiCTe, eles são salvo na tela **''Documentos Multi CT-e''** (Comercial → Rotinas → Documentos Multi CT-e) com o status **''Importado''**.

A outra ação agendada monitora todos os documentos com status ''Importado'' e realiza seu processamento. Quando o processamento é concluído com sucesso, o status é atualizado para **''Processado''** e o campo **''Nro Único CT-e''** é preenchido. Caso ocorra alguma falha, o status é alterado para **''Falha''**, sendo o motivo informado no campo **''Mensagem do Processamento''**. Os demais campos exibem informações extraídas do XML, facilitando consultas e análises.

Se a falha ocorrer por problemas de cadastro, por exemplo, após realizar os ajustes necessários, o usuário deverá acessar esta tela e alterar o campo status para ''Importado''. Dessa forma, a ação agendada processará novamente o registro, realizando uma nova tentativa de importação.

#### Tela Serviço

Durante o processo de importação do CT-e, a rotina precisa localizar os serviços com base nos componentes de serviço informados no XML. Para permitir que diferentes componentes sejam associados ao mesmo serviço, como por exemplo peso valor, frete peso e valor frete para o serviço 1 - Frete, foi criado o campo **''Nome Serviço MultiCT-e''** na tela de **''Serviço''** (Configuração > Cadastro > Produto > Serviço).

Dessa forma, é possível cadastrar mais de um componente de serviço presente no XML para um mesmo serviço do Sankhya, garantindo o correto vínculo durante a importação.

![Imagem 8: Dessa forma, é possível cadastrar mais de um componente de serviço presente no XML para um mesmo serviço do Sankhya,…](https://ajuda.sankhya.com.br/hc/article_attachments/40886447598999)
