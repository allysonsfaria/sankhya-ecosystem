---
id: "360045109253"
titulo: "Importação de NF-e para lançamento de CT-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109253-Importa%C3%A7%C3%A3o-de-NF-e-para-lan%C3%A7amento-de-CT-e"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:55:33Z"
rotulos: ["CT-e", "Configuração", "Importação de NF-e para lançamento de CT-e manual", "NF-e", "Portal de Vendas", "Importação", "Importação Eficiente de NF-e para Lançamento de CT-e", "Documentos Eletrônicos"]
---

# Importação de NF-e para lançamento de CT-e

As informações a seguir têm por objetivo fornecer os dados necessários para configuração e utilização da funcionalidade de importação dos dados da NF-e para se lançar um CT-e. Sendo assim, estas informações são destinadas a empresas que são transportadoras (prestadoras do serviço de transporte).

A premissa para que o módulo possa ser utilizado, é a aquisição junto à equipe Comercial Sankhya do produto **"**CONHECIMENTO DE TRANSPORTE ELETRÔNICO /W".

Lembrando que a importação dos dados da NF-e para lançar um CT-e serve para agilizar significativamente a operação de lançamento do CT-e da transportadora. Assim, ela permite que grande parte dos dados do CT-e e das notas transportadas sejam inseridos rapidamente e posteriormente transmitidos para a SEFAZ.

[Configurações para Importação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109253-Importa%C3%A7%C3%A3o-de-NF-e-para-lan%C3%A7amento-de-CT-e#configuraesparaimportao)                [Import. dos dados da NF-e para lançar o CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109253-Importa%C3%A7%C3%A3o-de-NF-e-para-lan%C3%A7amento-de-CT-e#importaodosdadosdanf-eparalanaroct-e)

[Alteração do CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109253-Importa%C3%A7%C3%A3o-de-NF-e-para-lan%C3%A7amento-de-CT-e#alteraodoct-e)

## Configurações para Importação

Localizada no botão **"Outras Opções"** do [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601454-Portal-de-Vendas-Atributos-da-Tela), tem-se a opção [Preferências para importação de NF-e p/ CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604014-Portal-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#prefernciasparaimportaodenf-epct-e); é uma opção que será apresentada apenas quando o Tipo de Movimento selecionado, for **"Conhecimento de transporte"**.

#### Aba Cabeçalho

Nesta aba precisam ser informados os dados do cabeçalho do CT-e para que no momento da importação dos dados da NF-e todos os campos obrigatórios do cabeçalho do CT-e sejam preenchidos:

- **Tipo operação:** Informa-se o Tipo de Operação mais costumeiramente utilizado para o lançamento do CT-e.
- **Tipo de negociação:** Preenche-se a forma de pagamento normalmente empregada para o lançamento do CT-e.
- **Ambiente de consulta:** Esta opção é exclusivamente empregada para a importação de dados da nota através da consulta da mesma na SEFAZ; logicamente, caso esteja definida como "Homologação" a consulta será feita no ambiente de homologação, caso contrário será feita no ambiente de "Produção".
- **Tomador de serviço:** Quando se importam os dados da NF-e, o tomador de serviço já pode ser automaticamente definido através da modalidade de frete da nota. Se a modalidade for por conta do emitente, o tomador será o emitente da nota importada, se for por conta do destinatário, este será o tomador. Ainda existem situações que a nota não possui nenhuma dessas opções de modalidade; especificamente para quando essa situação ocorrer o tomador será definido nesse campo das preferências, sendo como remetente ou destinatário. E ainda existe a opção de informar na inclusão, que se marcada, o usuário precisa definir o tomador antes de concluir a importação dos dados da nota para lançar o CT-e.
- **Previsão de entrega:** Define-se aqui, se a previsão de entrega poderá ser igual a data atual ou informada na inclusão – antes de concluir a importação dos dados da nota.
- **Produto predominante:** Indica-se aqui qual o produto predominante da NF-e; pode ser o Primeiro item da NF-e, Fixo - neste caso digitado pelo usuário; ou Informar na Inclusão – antes de concluir a importação dos dados da nota.
- **Ao gerar CT-e:** Esta opção determina o que será ocorrer na conclusão da importação da nota. Definindo-se para realizar Nova Inclusão, ele conclui a importação e já prepara pra realizar outra; definindo-se por Posicionar no CT-e gerado, ao concluir a importação o CT-e gerado a partir da importação será posicionado na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025237294-Central-de-Vendas).
- **Cadastra destinatário na importação da NF-e?:** Realizando-se esta marcação, será possível realizar o cadastro de um destinatário rapidamente durante a importação de uma NF-e para lançamento de um CT-e. Mais detalhadamente, com a referida marcação realizada, durante a importação de uma NF-e pra lançar um CT-e, caso o destinatário da NF-e não esteja cadastrado como um parceiro no sistema, automaticamente será apresentado o pop-up [Cadastro simplificado de parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598454) para realização deste procedimento.

![clip6186](https://ajuda.sankhya.com.br/hc/article_attachments/360060987514/clip6186.png)

#### Aba Medidas

Nesta aba é preciso definir quais os valores padrões para unidade e o tipo de medida no lançamento do CT-e. Na NF-e existem as seguintes informações:

- Quantidade de volumes transportados;
- Peso Líquido (em kg);
- Peso Bruto (em kg).

Para cada valor dessas informações, o CT-e vai possuir uma unidade e um tipo de medida. Por isso é preciso informar:

- **Unidade:** M3, KG, TON, UNIDADE, LITROS, MMBTU, Não informar – Definindo-se por Não informar a unidade não será gerada no CT-e ao concluir a importação;
- **Tipo da medida:** Informa-se aqui um texto que identifique o tipo da medida. Por exemplo: suponhamos que a quantidade de volume e peso líquido da NF-e sejam 100 e 1000.00 respectivamente. Se for determinado:

Quantidade de volume:

Unidade: UNIDADE

Tipo da medida: CAIXA

Peso bruto:

Unidade: KG

Tipo da medida: PESO BRUTO

Ao importar os dados da NF-e serão geradas as informações no CT-e:

Código da Unidade de Medida: 03-UNIDADE

Tipo da Medida: CAIXA

Quantidade: 100

Código da Unidade de Medida: 01-KG

Tipo da Medida: PESO BRUTO

Quantidade: 1000

![clip6187](https://ajuda.sankhya.com.br/hc/article_attachments/360061915293/clip6187.png)

#### Aba Dados de Seguro

Nessa aba, informam-se os dados do Seguro de Transporte utilizados mais frequentemente na emissão do CT-e. É preciso informar:

- Seguradora: Nome da seguradora;
- Apólice: Número da apólice;
- Averbação: Número da averbação;
- Responsável: Quem será o responsável pelo seguro.

![clip6190](https://ajuda.sankhya.com.br/hc/article_attachments/360061915313/clip6190.png)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109253-Importa%C3%A7%C3%A3o-de-NF-e-para-lan%C3%A7amento-de-CT-e#top)

## Importação dos dados da NF-e para lançar o CT-e

Presente no botão **"Outras Opções"** localizado na aba Notas do Conhecimento de Transporte da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414), quando o Tipo de Movimento selecionado no [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601454) for **"Conhecimento de transporte"**, tem-se a opção Importação de NF-e p/ CT-e. Ao acioná-la, pode-se optar pelas seguintes formas de importação dos dados da NF-e. Vejamos:

**Importar XML da NF-e:**

Esta opção é utilizada para importar os dados da NF-e através de um arquivo XML. Quando essa opção for selecionada, abre-se uma janela para upload de um arquivo XML ou ZIP – contendo vários arquivos.

![clip6193](https://ajuda.sankhya.com.br/hc/article_attachments/360060987554/clip6193.png)

Ao selecionar o(s) arquivo(s) XML é feita uma validação do CNPJ/CPF do emitente, destinatário e transportadora da NF-e. Emitente e destinatário precisam estar cadastradas como parceiros, enquanto que a transportadora da nota precisa estar cadastrada como empresa. Caso algum CNPJ/CPF não seja encontrado nos devidos cadastrados as seguintes mensagens podem ser apresentadas:

Quando a Transportadora não é encontrada como empresa, o seguinte aviso é apresentado:

**"CNPJ/CPF: XXXXXXXXXXXXX do transportador não encontrado no cadastro de 'Empresas'. Será necessário informar a empresa manualmente."**

Caso o emitente/destinatário não sejam encontrados como parceiros, a seguinte mensagem de erro é apresentada:

**"CNPJ/CPF: XXXXXXXXXXXXX do emitente não encontrado no cadastro de 'Parceiro'"**

**"CNPJ/CPF: YYYYYYYYYYYYY do destinatário não encontrado no cadastro de 'Parceiro'"**

Com os dados de todos os envolvidos devidamente encontrados, as informações da importação serão preenchidas.

Caso na configuração das [Preferências para importação de NF-e p/ CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604014-Portal-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#prefernciasparaimportaodenf-epct-e) tenha-se definido alguma informação para ser incluída na inclusão do CT-e, deve-se fazê-lo neste momento, ou seja, antes de concluir a importação.

Para importar um novo arquivo XML basta clicar no botão de adição e selecionar o arquivo desejado. A partir da segunda inclusão de nota, o sistema também valida se o emitente e destinatário da nova nota são os mesmos que o da primeira nota; caso não seja, será emitida a seguinte mensagem:

**"As notas importadas devem possuir o mesmo emitente, destinatário."**

Caso a segunda nota possua uma transportadora diferente da transportadora da primeira nota importada, o seguinte aviso será apresentado:

**"A nota importada possui transportadora diferente."**

Se o XML a ser importado não possuir uma estrutura válida, o seguinte erro será apresentado:

**"XML mal formado ou inválido!"**

Se o XML a ser importado for do modelo de documento 65 (NFC-e) o seguinte erro será exibido:

**"Importação de NFC-e (documento modelo 65) não suportada!"**

Pode-se também optar por importar os dados das notas através das outras opções a serem citadas a seguir.

**Buscar nota do sistema:**

Esta opção é utilizada nos casos em que a empresa emitente da NF-e e a empresa transportadora emitente do CT-e se encontram na mesma base de dados. Esta opção quando acionada, é aberto um pop-up para pesquisa de notas para que seja feita a busca de qual nota deseja-se importar para lançar o CT-e:

![clip6196](https://ajuda.sankhya.com.br/hc/article_attachments/360060987574/clip6196.png)

A nota desejada pode ser importada clicando duas vezes nela. Assim que a nota desejada for selecionada, as mesmas validações existentes na importação do XML vão acontecer, exceto as que dizem respeito a validações específicas do arquivo XML. Somente notas fiscais de modelo **1**, **4**, **1B** ou **55** confirmadas podem ser usadas para lançar o CT-e. Para buscar mais nota é preciso clicar no botão de adição.

Assim que a nota desejada for selecionada ela será inserida com as devidas informações, como já mostrado na opção de importação do XML da NF-e.

**Consultar nota na SEFAZ:**

Esta opção é utilizada quando a empresa transportadora tem posse da chave de acesso da NF-e a ser transportada. Através dessa opção o usuário precisa digitar o CAPTCHA (um teste automatizado para diferenciação entre computadores e humanos e servem como uma ferramenta auxiliar para evitar spams ou mensagens disparadas por outros computadores ou robôs) e em seguida bipar, colar ou digitar a chave de acesso da nota. Em seguida será feita uma consulta da nota no portal da NF-e da mesma forma que se faz através do endereço:

[http://www.nfe.fazenda.gov.br/portal/consulta.aspx?tipoConsulta=completa&tip oConteudo=XbSeqxE8pl8=](http://www.nfe.fazenda.gov.br/portal/consulta.aspx?tipoConsulta=completa&tip%20oConteudo=XbSeqxE8pl8=)

![clip6197](https://ajuda.sankhya.com.br/hc/article_attachments/360061915333/clip6197.png)

Por esta opção, são feitas exatamente as mesmas validações já citadas para as outras opções de importar dados da nota, exceto as que dizem respeito a validações específicas do arquivo XML. Além das validações comuns de emitente, destinatário e transportadora, no caso dessa opção de consulta da nota na SEFAZ em específico, são feitas outras validações.

No momento da consulta, caso a NF-e esteja cancelada ou denegada, será apresentado ao usuário um aviso, sem importar os dados da nota:

**"NF-e cancelada ou denegada não pode ser importada."**

Além disso, caso a chave de acesso consultada seja inexistente, será também apresentado ao usuário tal informação:

![clip6204](https://ajuda.sankhya.com.br/hc/article_attachments/360060987594/clip6204.png)

Outra validação existente nessa opção de consulta da nota na SEFAZ é em relação ao CAPTCHA. Se em três minutos nenhuma consulta for realizada com o CAPTCHA a ser digitado, ele será expirado e outro será gerado:

![clip6199](https://ajuda.sankhya.com.br/hc/article_attachments/360061915353/clip6199.png)

Se o usuário digitar o CAPTCHA incorretamente, tal informação será apresentada para que ele digite um novo CAPTCHA:

![clip6201](https://ajuda.sankhya.com.br/hc/article_attachments/360060987614/clip6201.png)

Caso queira-se trocar a imagem do CAPTCHA apresentado, basta clicar-se no botão **"Atualizar CAPTCHA"**. Assim que a nota for consultada ela será inserida com os dados devidos, da mesma forma que acontece nas outras opções para importar dados da nota.

**Buscar nota recebida pelo e-mail/DF-e:**

Esta opção está diretamente relacionada a rotina [Configuração p/ leitura de XML no e-mail](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109533); depois que o sistema busca e localiza XML's dos documentos na Caixa de entrada do usuário de e-mail, estes uma vez baixados e salvos, podem ser importados através da opção Buscar nota recebida pelo e-mail. Para sua utilização, informa-se a Chave de acesso do XML, e solicita-se sua Consulta; caso o documento seja localizado, este será carregado na grade e poderá ser importado; caso contrário, será exibida a seguinte mensagem:

**"Xml não encontrado para a chave NF-e informada!"**

**Observação:** no processo de emissão do CT-e feito diretamente pela Central de Vendas, depois que o cabeçalho do CT-e é lançado, em seguida as informações de quais notas serão transportadas são definidas por meio da opção Importação de NF-e p/ CT-e, na conclusão de toda a importação, as informações de Seguro do Transporte já definidas nas Preferências para importação de NF-e p/ CT-e serão inseridas automaticamente na aba Seguros de Transporte.

**Nota:** ao realizar a importação do XML da NF-e, ou mesmo ao consultar os dados deste documento na SEFAZ, será possível importar/consultar as informações pertinentes aos itens da nota. Tem-se acesso à Descrição do Produto, Quantidade, Unidade, Valor Unitário e Valor.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109253-Importa%C3%A7%C3%A3o-de-NF-e-para-lan%C3%A7amento-de-CT-e#top)

## Alteração do CT-e

Uma vez estando-se posicionado no pop-up Importação de NF-e p/ CT-e, depois que todas as notas desejadas forem inseridas, pode-se ainda alterar as seguintes informações relativas ao CT-e:

- **Empresa:** poderá ser carregada a partir da importação, e editada;
- **Parceiro:** poderá ser carregado a partir da importação, e editado;
- **Previsão de entrega:** poderá ser carregada a partir das preferências de importação, e editada;
- **Produto predominante:** poderá ser carregado a partir da importação, e editado;
- **Série:** sempre será necessário informar antes de lançar o CT-e.

Além de poder alterar essas informações, pode-se também conferir os dados das notas inseridas na grade existente na parte inferior do pop-up.

Depois que todas as notas e informações forem conferidas e estiverem em conformidade, clica-se no botão **"Importar"**. Assim que ele importar, o CT-e será gerado contendo todas as informações obtidas através das Notas Fiscais. Conforme configuração realizada nas [Preferências para importação de NF-e p/ CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604014-Portal-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#prefernciasparaimportaodenf-epct-e) pode-se ter o CT-e apresentado assim que a importação for concluída, ou a solicitação da importação de novas notas para um novo CT-e.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109253-Importa%C3%A7%C3%A3o-de-NF-e-para-lan%C3%A7amento-de-CT-e#top)
