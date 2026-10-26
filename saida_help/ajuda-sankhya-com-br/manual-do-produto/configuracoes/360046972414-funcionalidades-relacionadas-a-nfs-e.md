---
id: "360046972414"
titulo: "Funcionalidades relacionadas à NFS-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T14:00:03Z"
rotulos: ["Configuração", "Portal de Vendas", "XML", "Nota Fiscal Eletrônica de Serviço - Prefeituras", "Prefeituras", "NFS-e", "Funcionalidades da NFS-e: Explorando as Opções"]
---

# Funcionalidades relacionadas à NFS-e

Nesta documentação você encontrará as funcionalidades relacionadas à NFS-e. Analisemos cada uma delas:

[Utilizando o botão NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e#utilizandoobotonfs-e)                    

[Botão Cancelar Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e#botocancelarnota)

[Substituição de NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e#substituiodenfs-e)

[Cancelamento de NFS-e - Prefeituras que não possuem o processo via webservices](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e#cancelamentodenfs-e-prefeiturasquenopossuemoprocessoviawebservices)

### Utilizando o botão NFS-e

Na parte superior do painel [Resultado da Seleção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025234554-Portal-de-Vendas-Atributos-da-Tela#grade-resultadodaseleo) no [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025234554-Portal-de-Vendas-Atributos-da-Tela), tem-se o botão **"NFS-e"** que apresenta as seguintes opções:

**Gerar Lote:** efetua o envio da NFS-e para a webservice. Mesmo processo do botão "Confirmar". O processo de geração de lote consiste no envio de NFS-e agrupadas em duas ou mais notas, limitando-as a 50 notas ou 500 kbytes, e será feito por esta opção.

**Observação:** esta opção não terá efeito se a NFS-e já tiver sido enviada.

- **Atenção (Reforma Tributária):** Ao tentar gerar o lote de uma nota que contenha múltiplos serviços, o sistema validará a carga tributária aproximada de todos eles. Caso exista divergência de percentuais entre os serviços da mesma nota, a geração do lote será bloqueada. Para seguir com o envio, será necessário igualar a configuração de Carga Média Tributária no cadastro dos Serviços envolvidos ou na aba Configurações do cadastro da Empresa.

**Buscar autorização:** utilizado no processo assíncrono, para identificar o status de processo de notas, que estão **"Aguardando Autorização"**. Quando ocorrer de na geração do lote, o servidor da NFS-e não responder, pode-se utilizar esta opção, para iniciar o processo de comunicação com o Web Service.

Assim, será verificado se a nota está autorizada na Prefeitura e caso esteja, o XML desta será vinculado à nota.

E caso no retorno desta consulta não exista um documento com o campo **"Identificação"** igual a **"numNota"** a busca pelo XML da NFS-e será suspenso e o documento continuará como não autorizado.

**Nota:** a consulta especificada acima, abrange somente a Prefeitura de Florianópolis.

**Observação:** na emissão de NFS-e pela integração com o E-notas, a busca de autorização das notas acontecerão de forma automática na confirmação do documento, sem que você precise fazer a busca da autorização manual.

**Buscar Autorização por Empresa/Data (Uberlândia):** através desta opção pode-se informar uma empresa e data, assim, o sistema buscará as notas emitidas na prefeitura de Uberlândia naquele dia e atualizará as informações no sistema para as notas que ainda não possuem informação de NFS-e. Isso será útil para quando a Nota for enviada pelo sistema e este por algum motivo não se conseguir buscar o resultado do processamento pelo **"Nro do protocolo de entrega"**, que é mais eficiente. O ideal nestes casos é pesquisar no site pelo **"Nro do RPS"** (numnota) e pegar a **"Data de emissão da Nota"**, e então usar esta data na opção de busca de autorização.

**Marcar lote como RPS:** o sistema apresenta a modalidade de contingência eletrônica para notas fiscais eletrônicas de serviço através do **RPS – "Recibo Provisório de Serviço"**. Constatando-se a impossibilidade do envio de uma **"Nota Fiscal Eletrônica de Serviço"**, deve-se marcá-la através desta opção.

**Marcar lote como RPS e imprimir:** além de realizar o procedimento descrito na opção anterior, acionando-se esta opção, será realizada a impressão da nota.

**Marcar como RPS e confirmar:** essa opção tem como funcionalidade, confirmar a(s) nota(s) e marcá-la(s) como **"Recibo Provisório de Serviços"**, eliminando a necessidade de confirmá-la(s) previamente para, em seguida, marcar como RPS.

**Desmarcar lote como RPS:** através desta opção o usuário novamente habilitará a nota fiscal de serviço para envio pela web service.

| ![Imagem 1: Desmarcar lote como RPS: através desta opção o usuário novamente habilitará a nota fiscal de serviço para envio pela…](https://ajuda.sankhya.com.br/hc/article_attachments/42311057659543) | Para cohecer as melhores práticas de como emitir uma NFS-e em contingência, acesse o artigo [Impressão de nota fiscal de serviço em contingência](https://ajuda.sankhya.com.br/hc/pt-br/articles/10928183956375). |
| --- | --- |

**Importante:** o parâmetro **"Qtd. máxima de notas em um lote NFS-e - NFSEMAXNOTALOTE"** determinará a quantidade de Notas em um Lote de NFS-e. O valor padrão é de 30 Notas.

**Cancelamento extemporâneo:** o cancelamento extemporâneo para NFS-e é solicitado diretamente na prefeitura do município quando há necessidade de cancelar a nota após o ISS ter sido pago/recolhido. A prefeitura então, retorna um número de protocolo do cancelamento, que deverá ser informado no pop-up apresentado através dessa opção para efetuar o cancelamento da nota no [Portal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654) ou [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414). Feito isso, a nota fiscal terá o status **"Cancelada"** e poderá ser pesquisada na tela [Notas Canceladas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107913). Além disso, essa opção só será apresentada quando a marcação **"Permite cancelamento extemporâneo?"** da aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abanfs-e), presente na tela Cidades for efetuada. 

**Gerar XML do RPS para NFS-e e Gerar XML para NFS-e:** ao selecionar uma ou mais notas e clicar nesta opção será realizado o download do arquivo XML.

**Nota:** para gerar o arquivo XML de notas canceladas, o **"Tipo de Movimento"** no Portal de Vendas deverá ser **"Canceladas"**.

**Enviar XML da NFS-e por e-mail:** ao selecionar uma nota com status **"Aprovada"** e acionar esta opção, o arquivo XML será enviado para o e-mail cadastrado no Cadastro de Parceiros, aba [NF-e/NFS-e/CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025232674-Parceiros#abanf-enfs-ect-e), campo **"Email específico p/ envio NFS-e"**.

**Observação:** pode-se inserir um ou mais e-mails neste campo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e#top)

### Substituição de NFS-e

Existem situações em que o emissor da NFS-e deseja cancelar a nota, porém não é mais possível devido ao esgotamento do tempo para fazê-lo ou mesmo à legislação municipal, tendo como opção, apenas realizar a Substituição da NFS-e.

**Observação:** nosso sistema permite que seja realizada a substituição de notas para as prefeituras que possuem esse serviço, quando as notas forem emitidas por API.

Será aprovada a NFS-e e substituída. No final, teremos duas notas, uma substituída e outra substituta pela integração. A nota substituída ficará com o status cancelada e, apenas a nota substituta ficará ativa.

Vejamos as configurações necessárias para utilização:

- **Cadastro de Cidades**

No cadastro de Cidades, aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025391813-Cidades#abageral), têm-se as seguintes configurações:

![Nfes22](https://ajuda.sankhya.com.br/hc/article_attachments/15589285825559)

**Tem substituição NFS-e:** Esta marcação define se a Cidade em questão possui substituição de NFS-e; ela é essencial para funcionamento desta funcionalidade.

**Quantidade de substituições permitidas:** Neste campo, informa-se a quantidade de substituições permitidas dentro do mês para as Empresas vinculadas à cidade em questão.

**Prazo para substituição de NFS-e:** Informa-se neste campo, o prazo em dias para que a Nota Fiscal de Serviço possa ser substituída.

- **Portal de Vendas**

Através do [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025232294-Portal-de-Vendas), botão NFS-e, tem-se a opção **"Substituir nota"**:

![Nfes23](https://ajuda.sankhya.com.br/hc/article_attachments/15589301901719)

Ao acionar esta opção, tem-se a execução da rotina de Substituição de NFS-e. Em seguida, o sistema realizará os seguintes procedimentos:

Na confirmação da NFS-e de substituição o sistema irá gravar na Observação da nota a seguinte mensagem:

**"Esta nota fiscal substitui a de Nr. xxxxxx."**

Em seguida, na confirmação/envio, serão geradas algumas informações no XML que identificam para o Sistema da Prefeitura que se trata de uma NFS-e Substituída. Vejamos abaixo:

![Nfes24](https://ajuda.sankhya.com.br/hc/article_attachments/15589301905303)

- **Livros Fiscais**

Na tela [Geração ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025395353-Gera%C3%A7%C3%A3o-ISS), ao realizar-se a geração do livro de ISS em um período em que ocorreram substituições de NFS-e, o sistema irá considerar internamente tais notas como "canceladas", apresentando ao fim da geração, a seguinte mensagem:

![Nfes25](https://ajuda.sankhya.com.br/hc/article_attachments/15589301907607)

Feita a geração do Livro do ISS, através da tela [Cadastro Livro ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025387833-Cadastro-Livro-ISS), é possível verificar a escrituração do ISS e verificar que as NFS-e's que foram substituídas possuem na aba **"Observação"** uma demonstração clara da operação ocorrida:

![Nfes26](https://ajuda.sankhya.com.br/hc/article_attachments/15589285832855)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e#top)

### Botão Cancelar Nota

Ao efetuar o cancelamento da NFS-e pela Central, informa-se um dos códigos a seguir quando solicitado:

- 1 - Erro na emissão;
- 2 - Serviço não prestado;
- 3 – Erro de assinatura;
- 4 – Duplicidade da nota;
- 5 – Erro de processamento.

**Nota:** as prefeituras que possuem códigos diferentes dos citados acima, podem consultar em seu tópico específico as devidas informações.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e#top)

### Cancelamento de NFS-e - Prefeituras que não possuem o processo via webservices

Para as prefeituras que não possuem o serviço de cancelamento via webservice realizado através do botão **"Cancelar nota"** (no qual é gerada uma comunicação do sistema com a prefeitura efetuando o cancelamento), o contribuinte deve solicitar diretamente no site da prefeitura. Após realizar o processo de cancelamento pelo site da prefeitura, pode-se cancelar a NFS-e no sistema.

![Imagem 7: Antes de solicitar o cancelamento da NFS-e no sistema, é fundamental que o cancelamento já tenha ocorrido no site da…](https://ajuda.sankhya.com.br/hc/article_attachments/16426532885271) Antes de solicitar o cancelamento da NFS-e no sistema, é fundamental que o cancelamento já tenha ocorrido no site da prefeitura.

Vejamos as configurações necessárias para o cancelamento:

- **Portal de Vendas**

Através do [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025232294-Portal-de-Vendas), botão **"Cancelar nota"**, tem-se a execução da rotina de Cancelamento da NFS-e:

![Nfes27](https://ajuda.sankhya.com.br/hc/article_attachments/15589301914903)

- **Cadastro de Cidades**

A NFS-e será cancelada de acordo com a configuração efetuada no Cadastro de Cidades, aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025391813-Cidades#abageral), campo **"Tipo de cancelamento para NFS-e"** que apresenta as seguintes opções:

![Nfes28](https://ajuda.sankhya.com.br/hc/article_attachments/15589301916055)

**Via Web Services:** Quando essa opção estiver cadastrada na cidade da empresa que esta solicitando o cancelamento, o sistema fará o atual processo de cancelamento, não ocorrendo nenhuma alteração.

**Via Web Services com valor limite de cancelamento:** Essa opção é indicada para a empresa prestadora do serviço, ao solicitar o cancelamento será verificado pelo sistema o valor informado no campo **"Valor Limite para Cancelamento NFS-e"**. Caso o valor (TGFCAB.VLRNOTA) da NFS-e não ultrapasse esse valor, o sistema terá o atual processo de cancelamento.

Caso o valor da nota fiscal ultrapasse o valor informado, será apresentado um pop-up para informar os dados do cancelamento da NFS-e efetuado na prefeitura:

![Nfes29](https://ajuda.sankhya.com.br/hc/article_attachments/15589301919895)

O campo **"Data Cancelamento na Prefeitura"** de preenchimento obrigatório aponta a data em que foi cancelada a NFS-e. Será gravada a informação no campo "Data Cancelamento Prefeitura" na tabela do cancelamento de notas (TGFCAN);

No campo **"Protocolo de Cancelamento"** indica-se as informações pertinentes ao protocolo de cancelamento, podendo conter letras/números. Será gravada a informação no campo "Protocolo de Cancelamento" na tabela do cancelamento de notas (TGFCAN);

Através do campo **"Motivo"** aponta-se a justifica pela qual está sendo realizado o cancelamento. Tem seu preenchimento obrigatório, seus dados serão ligados com a informação do campo acima com o texto "Cancelamento não ocorreu via web-services, realizado diretamente na prefeitura.". Será gravada a informação no campo "Motivo" na tabela do cancelamento de notas (TGFCAN);

**Via prefeitura com número de Protocolo:** Quando essa opção estiver cadastrada na cidade da empresa (Prestador do Serviço) em que estiver solicitando o cancelamento, será apresentado um pop-up para informar os dados do cancelamento da NFS-e efetuado na prefeitura:

![Nfes30](https://ajuda.sankhya.com.br/hc/article_attachments/15589301921943)

**Via prefeitura sem número de Protocolo:** Estando essa opção cadastrada na cidade da empresa prestadora do serviço que está solicitando o cancelamento, um pop-up para informar os dados do cancelamento da NFS-e efetuado na prefeitura será exibido:

![Nfes31](https://ajuda.sankhya.com.br/hc/article_attachments/15589301923479)

Após preencher as informações contidas nas opções apresentadas acima, ao clicar no botão **"Ok"**, o sistema realizará o processo de cancelamento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e#top)
