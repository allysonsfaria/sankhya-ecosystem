---
id: "360044600254"
titulo: "Contingências do CT-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600254-Conting%C3%AAncias-do-CT-e"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Documentos Fiscais Eletrônicos > CT-e e CT-e OS"
atualizado_em: "2026-09-15T16:58:13Z"
rotulos: ["CT-e", "EPEC", "SEFAZ", "Transporte", "Contingência", "Contingências", "Contingências do CT-e manual", "Contingências do CT-e: Estratégias e Procedimentos", "Documentos Eletrônicos", "SVC"]
---

# Contingências do CT-e

O CT-e possui algumas formas de envio por contingência, que podem ser utilizadas conforme a necessidade da empresa. São elas:

- SVC - SEFAZ Virtual de Contingência;
- EPEC - Envio Prévio de Emissão em Contingência;
- FSDA - Formulário de Segurança Documento Auxiliar.

Abaixo, você pode conferir as particularidades envolvidas em cada uma dessas contingências nos links:

[SVC](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600254-Conting%C3%AAncias-do-CT-e#svc-sefazvirtualdecontingncia)                                                                [EPEC](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600254-Conting%C3%AAncias-do-CT-e#epec-envioprviodeemissoemcontingncia)                                                     [FSDA](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600254-Conting%C3%AAncias-do-CT-e#fsda-formulriodeseguranadocumentoauxiliar)

[Manutenção de Contingência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600254-Conting%C3%AAncias-do-CT-e#manutenodecontingncia)

### SVC - SEFAZ Virtual de Contingência

Essa contingência é uma alternativa de emissão do CT-e com transmissão do documento para o Sistema de Contingência Virtual (SVC). Ao utilizar essa modalidade de contingência, o DACTE pode ser impresso em papel comum e não será necessário realizar a transmissão do CT-e para a SEFAZ de origem quando os problemas técnicos que anteriormente impediram a transmissão, forem solucionados.

O objetivo da SVC é permitir que os contribuintes obtenham a autorização de emissão do CT-e em um ambiente de autorização alternativo, que pode ser utilizado sempre que o ambiente da sua circunscrição estiver indisponível, ou se for apresentando um elevado tempo de resposta, de forma que não haverá a necessidade de alteração da série do CT-e.

O SVC é dependente da ativação da SEFAZ de origem, ou seja, só irá entrar em operação quando a SEFAZ de origem estiver com problemas técnicos que impossibilitem a recepção do CT-e.

Para que o sistema possa emitir o CT-e nesse ambiente de autorização, é preciso configurar nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba [CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abact-e), a forma de envio/transmissão do lote do CT-e. Com isso, no caso da SEFAZ de origem estar com problemas da recepção dos documentos, o sistema poderá automaticamente optar pelo meio de envio através da SVC.

Quando o CT-e for lançado por esse tipo de emissão, o campo **"Tipo de emissão do CT-e"**, será preenchido com a descrição **"Autorização pela SVC-XX"**, em que **"XX"** pode ser **"SP"** ou **"RS"**, que são as únicas unidades federativas que possuem a SVC.

![Imagem 1: Quando o CT-e for lançado por esse tipo de emissão, o campo "Tipo de emissão do CT-e" , será preenchido com a descrição…](https://ajuda.sankhya.com.br/hc/article_attachments/1500009621481)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600254-Conting%C3%AAncias-do-CT-e#top)

### EPEC - Envio Prévio de Emissão em Contingência

Essa contingência, permite que a empresa emita uma solicitação de registro de evento de CT-e, anterior a autorização do documento propriamente dita com um layout contendo o mínimo de informações.

Esse evento deve ser enviado à SEFAZ Virtual de Contingência (SVC) que atende a UF do emissor do documento, onde, dado que o EPEC foi autorizado, a empresa poderá prestar o serviço imprimindo o DACTE em modelo de Contingência em papel comum. Quando o sistema for retomado, o emitente deve enviar o CT-e normal para sua SEFAZ autorizadora.

Para realização do envio do CT-e como EPEC, realize a marcação do documento como EPEC através do botão **"CT-e"**, opção [Marcar conhecimentos como EPEC](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596894-Aprova%C3%A7%C3%A3o-do-CT-e#marcarconhecimentoscomoepec), em seguida acione a opção [Enviar conhecimentos como EPEC](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596894-Aprova%C3%A7%C3%A3o-do-CT-e#enviarconhecimentoscomoepec). O envio do CT-e como EPEC também pode ocorrer de forma automática, desde que as configurações nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abact-e) estejam corretamente efetuadas.

Quando o CT-e for emitido por esse tipo de contingência, o campo **"Tipo de emissão do CT-e"**, ficará preenchido como **"EPEC pela SVC"**. Além disso, o campo **"Status CT-e"**, será apresentado com a descrição **"Enviada EPEC"**.

![Imagem 2: Quando o CT-e for emitido por esse tipo de contingência, o campo "Tipo de emissão do CT-e" , ficará preenchido como…](https://ajuda.sankhya.com.br/hc/article_attachments/1500010040941)

Assim, uma mensagem será enviada à SEFAZ para justificar o envio do CT-e como EPEC. Sendo esta:

**"Contingência em EPEC em decorrência de problemas técnicos."**

**Observação:** todo EPEC emitido pela empresa transportadora, deve ser autorizado assim que o serviço da SEFAZ de origem retornar seus serviços ao normal, possuindo o máximo de 7 (sete) dias para fazê-lo; caso contrário, a empresa ficará bloqueada para emissão de outros EPEC's.

Após a geração do lote do CT-e ser enviado como EPEC no ambiente de origem autorizado, o campo **"Tipo de emissão do CT-e"** continua preenchido como **"EPEC pela SVC"** e o campo **"Status CT-e"** será alterado para **"Aprovada"**.

**Importante:** podem ocorrer casos em que a SEFAZ estadual e a SVC estarão indisponíveis, de modo que o sistema fará a tentativa de envio do CT-e através do EPEC, mas ainda assim podem ocorrer erros nessa emissão. Com esse comportamento, após determinado tempo, não será mais possível enviar o CT-e no ambiente normal de autorização estadual, pois não será possível alterar o tipo de emissão do CT-e. O sistema está apto para realizar a emissão do CT-e mesmo nessas situações, com base nas seguintes considerações:

- No momento em que um CT-e for enviado como EPEC e a receita retornar a seguinte rejeição:

**"639 - Rejeição: Existe EPEC emitido há mais de 7 dias (168h) sem a emissão do CT-e no ambiente normal de autorização"**

- O sistema automaticamente irá preencher o campo **"Status CT-e"** com os dizeres **"Aguardando Correção"** e irá limpar o conteúdo dos campos **"Tipo de Emissão CT-e"**, **"Nro. Aleatório"** e **"Chave CT-e"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600254-Conting%C3%AAncias-do-CT-e#top)

### FSDA - Formulário de Segurança Documento Auxiliar

Esse procedimento de contingência, será adotado pelos emissores que adquirirem o Formulário de Segurança para impressão de Documento Auxiliar – FSDA.

Esse meio de contingência pode ser utilizado quando a empresa transportadora identificar a existência de qualquer fator que prejudique ou impossibilite a transmissão do CT-e e/ou a obtenção da autorização de uso da SEFAZ. Nesse caso, a empresa pode acionar a Contingência com FSDA, seguindo os passos:

- Faça a geração de um arquivo XML do CT-e com o campo **"tpEmis"** alterado para **"5"**.
- Realize a impressão do DACTE em no mínimo duas vias do FSDA, constando no corpo a expressão, **"DACTE em Contingência – impresso em decorrência de problemas técnicos"**. As vias devem ter a seguinte destinação:

I - Uma das vias permitirá o trânsito dos veículos do prestador do serviço de transporte e deverá ser mantida arquivada pelo destinatário no prazo estabelecido pela legislação tributária para a guarda de documentos fiscais.

II - Outra via, deve ser mantida arquivada pelo emitente no prazo estabelecido pela legislação tributária para a guarda dos documentos fiscais.

III - Sendo o tomador diverso do destinatário, deve existir uma terceira via, que será remetida a este para efeito de registros contábeis e fiscais, pois apenas essa via do FSDA dará direito ao crédito.

O emissor deve transmitir o CT-e imediatamente após a resolução dos problemas técnicos que impediram a transmissão do CT-e inicialmente, observando o prazo limite de 7 (sete) dias a partir da emissão do documento. Além disso, o emissor deverá tratar os CT-e's transmitidos por ocasião da ocorrência dos problemas técnicos, que estão pendentes de retorno.

Para que seja emitido um CT-e em contingência FSDA, primeiramente, você deve selecionar o CT-e, marcá-lo como **"FSDA"** e por fim, realizar a impressão do mesmo em um papel específico.

Quando um CT-e for emitido como FSDA, o campo **"Tipo de emissão do CT-e"**, será apresentado como **"Contingência FSDA"**.

Quando o serviço da SEFAZ de origem voltar ao normal, faça a geração do lote do CT-e visando a autorização do mesmo. Mesmo após esse procedimento, o campo **"Tipo de emissão do CT-e"** continuará preenchido com a descrição **"Contingência FSDA"**, porém o campo **"Status CT-e"** será alterado para **"Aprovada"**.

Dessa forma, quando a SEFAZ retornar ao normal, ao imprimir o CT-e como FSDA. Sendo que, o sistema pode enviar à SEFAZ uma justificativa registrada na tela [Manutenção de Contingência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612534-Manuten%C3%A7%C3%A3o-de-Conting%C3%AAncias-NF-e), caso não haja nenhuma, o texto abaixo será enviado:

**"Contingência em FSDA em decorrência de problemas técnicos."**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600254-Conting%C3%AAncias-do-CT-e#top)

### Manutenção de Contingência

Na tela [Manutenção de Contingência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612534-Manuten%C3%A7%C3%A3o-de-Conting%C3%AAncias-NF-e), é possível justificar a emissão do CT-e em contingência. Por meio dela, você pode definir qual a data e hora de início e fim da entrada em contingência, além de definir a justificativa e vincular quais são os CT-e's que terão a justificativa definida para a emissão em contingência.

![Imagem 3: Na tela Manutenção de Contingência , é possível justificar a emissão do CT-e em contingência. Por meio dela, você pode…](https://ajuda.sankhya.com.br/hc/article_attachments/1500010017641)

Para que seja possível inserir uma justificativa para emissão do CT-e, preencha os seguintes campos:

O campo **"Nro. Contingência"** apresenta o número de cadastro da contingência. Ele pode ser gerado automaticamente, ou informado de forma manual. Essa definição é feita no botão ![Imagem 4: O campo "Nro. Contingência" apresenta o número de cadastro da contingência. Ele pode ser gerado automaticamente, ou…](https://ajuda.sankhya.com.br/hc/article_attachments/16343673846167) **"Configuração da tela"** localizado no canto direito da tela.

Informe a **"Empresa"** responsável pela emissão do CT-e em contingência. E selecione a opção **"CT-e"**, no campo **"Tipo de documento"**.

Em seguida, informe no campo **"Emissão CT-e"** qual o meio de envio em contingência do CT-e. Para essa configuração, o campo **"Tipo Contingência"** deve ser definido com a opção **"Manual"**.

---

**Aba Geral**

No campo **"Dh Abertura"** dessa aba, informe a data e hora da entrada em contingência.

O campo **"Dh Fechamento"** é preenchido com a data e hora em que o ambiente da SEFAZ de origem retornou a normalidade, após os problemas terem sido solucionados.

Informe a **"Justificativa"** da emissão dos CT-e's em contingência.

---

**Aba Notas**

Nessa aba, realize a inserção dos Conhecimentos de Transporte que serão emitidos em contingência.

![Imagem 5: Nessa aba, realize a inserção dos Conhecimentos de Transporte que serão emitidos em contingência.](https://ajuda.sankhya.com.br/hc/article_attachments/1500009754422)

Quando você selecionar o botão ![Imagem 6: Quando você selecionar o botão para a inclusão de notas , informe o campo "Nro. Único Nota" dessa forma, os demais…](https://ajuda.sankhya.com.br/hc/article_attachments/16202400619159) para a inclusão de notas, informe o campo **"Nro. Único Nota"** dessa forma, os demais campos serão preenchidos automaticamente.

**Observação:** a tela de manutenção de contingência é preenchida automaticamente para os casos onde o CT-e é emitido em contingência FSDA ou EPEC.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600254-Conting%C3%AAncias-do-CT-e#top)
