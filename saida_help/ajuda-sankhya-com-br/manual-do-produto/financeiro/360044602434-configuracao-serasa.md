---
id: "360044602434"
titulo: "Configuração Serasa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602434-Configura%C3%A7%C3%A3o-Serasa"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:38:06Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Integração", "Serasa", "Preferências", "Financeiro", "Configuração Serasa", "br.com.sankhya.mge.configuracao.consulta.serasa", "Configuração Serasa manual", "Integração Serasa: configuração inicial usuário e senha", "Ambientes: homologação e produção parâmetros URL", "Consultas: monitoramento análises de crédito relatórios detalhados"]
---

# Configuração Serasa

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312261689879) Módulo: Financeiro > Preferências
```

---

![Imagem 2: A partir do dia 14 de novembro de 2024 , a integração com o Serasa será descontinuada e esta tela não receberá mais…](https://ajuda.sankhya.com.br/hc/article_attachments/24825435643671) A partir do dia **14 de novembro de 2024**, a integração com o Serasa será descontinuada e esta tela não receberá mais manutenções ou melhorias.

---

**Importante:** essa tela será apresentada para uso, se a empresa possuir o opcional **"30720 - CONSULTA SERASA /W"** ou **"20503 - JIVA-CONSULTA SERASA /W"**.

A tela Configuração Serasa é participante da [Integração Consulta SERASA EXPERIAN](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110113-Integra%C3%A7%C3%A3o-Consulta-SERASA-EXPERIAN); através dela, você poderá realizar as configurações iniciais que possibilitaram a consulta ao [Serasa Experian](https://www.serasaexperian.com.br/). Nela, tem-se as marcações que definem quais consultas serão efetuadas, o Usuário e sua respectiva Senha, e se tal consulta será realizada em Ambiente de Homologação.

A marcação **"Homologação"** quando realizada, determina que a consulta será realizada em ambiente de Homologação; consequentemente, ao ser desmarcada, tem-se a realização da consulta em ambiente de Produção.

**Observação:** os campos **"Usuário"** e **"Senha"**, são utilizados apenas para consultas integradas e portanto, são diferentes dos dados de login empregado no acesso ao site do Serasa; logo a empresa que optar por utilizar a Integração Consulta SERASA EXPERIAN, deverá entrar em contato com o Serasa e solicitar o Usuário e Senha de login de integração e inserir, respectivamente nestes campos.

![Imagem 3: Observação: os campos "Usuário" e "Senha" , são utilizados apenas para consultas integradas e portanto, são diferentes…](https://ajuda.sankhya.com.br/hc/article_attachments/4413552731671)

A tela Configuração Serasa possui precedência sobre a configuração realizada na tela [Análise de Risco Serasa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115753-An%C3%A1lise-de-Risco). As configurações aqui presentes podem ser realizadas pelo usuário SUP ou pelo próprio Usuário, mas é importante que o acesso com o usuário seja feito apenas na primeira vez para as devidas configurações, pois essa tela determina os acessos que o usuário terá permissão na tela Análise de Risco Serasa.

**Importante:** vale ressaltar que, atualmente, não há implementação nativa que copie as configurações do SUP para o usuário logado ao abrir a tela Configuração Serasa porém, caso não haja nenhuma configuração nessa tela para o usuário logado, ao realizar a consulta na Análise de Risco Serasa, serão usadas as configurações do SUP de forma automática. Em outras palavras, é possível criar qualquer usuário sem nem dar acesso à tela Configuração Serasa e também será possível realizar a consulta na tela Análise de Risco Serasa utilizando-se das configurações do SUP.

Após efetuar as devidas configurações, recomendamos que o Usuário não tenha mais acesso à tela Configuração Serasa, pois a partir desse momento a configuração desse usuário será por meio da tela Análise de Risco Serasa. Considere o seguinte exemplo:

Um usuário "X" logado no sistema, possui acesso à tela Configuração Serasa e marca as opções que ele poderá consultar, e desmarca aquelas que se enquadram na situação contrária. As opções que não forem assinaladas, não serão visíveis à este usuário quando o mesmo acessar a tela Análise de Risco Serasa.

**Observação:**

Configure os novos endereços de endpoints do Serasa, por meio dos seguintes parâmetros:

- Para o Ambiente de Produção, informe no parâmetro **"URL de produção para requisição do serasa - URLPRODSERASA"** o endereço **sitenet43-2.serasa.com.br**
- Já para o Ambiente de Homologação, informe no parâmetro **"URL de homologação para requisição do serasa - URLHOMOSERASA"** o endereço **mqlinuxext-2.serasa.com.br**

Desse modo, ao acessar a tela Análise de Risco Serasa e realizar uma pesquisa por **"Parceiro"**, **"Prospect"** ou **"CNPJ/CPF"**, o Serasa retornará os dados da consulta conforme os parâmetros configurados.

Ressaltamos ainda, que se o campo **"Texto"** dos dois parâmetros não estiverem preenchidos, o sistema utilizará o endereço atual do Serasa.

---

Essa tela é dividida em três seções, sendo a primeira delas de nome **Acesso**, composta pelas informações citadas no início desta documentação.

**Seção Relato Analítico**

Essa seção, corresponde às buscas feitas a um CNPJ, em que apresentará consultas mais detalhadas que visam auxiliar as decisões de análise e liberação de crédito. Assim, teremos as seguintes marcações:

- Classificação do Risco de Crédito - Empresas;
- Risco de Crédito do Setor;
- Anotações e Consultas SPC;
- Quadro Social e Administração;
- Novo Quadro Social mais completo;
- Participações;
- Serasa Score com Positivo;
- Endereços e Telefones Adicionais;
- SPC Sócios e Administradores;
- Faturamento estimado com positivo;
- Gasto Estimado;
- Índice Relacionamento Mercado;
- Limite de Crédito PJ;
- Collection Scoring PJ;
- Situação Fiscal;
- Alerta de Identidade PJ;
- Modelo NRI1 Apres. Alerta de Ident. PJ;
- Modelo NRI2 Apres. Alerta de Ident. PJ;
- Modelo NRI3 Apres. Alerta de Ident. PJ;
- Comportamento de Pagamento do Setor;
- Registro de Consultas Detalhado;
- Alerta Cadastral da Empresa;
- Alerta Cadastral dos Sócios e Administradores;
- Vendas com Cartão;
- Anotações e Consultas SPC Sócios;
- Serasa Score Atacadista;
- Índice Relacionamento Mercado e Setor;
- Anotações e Consultas SPC de Sócios e Administradores;
- Mosaic Business;
- Score Sócios;
- Serasa Score Empresa;
- Indicador de Riskscoring;
- Indicador de Alertascoring;
- Perfil Financeiro;
- Indicador de fatura Riskscoring no gestor;
- Verificação de títulos;
- Indicador de Recuperação de Crédito;
- Renda Estimada Sócios e Administradores PF;
- Faturamento Presumido;
- Comportamento de Pagamento de Empresas;
- Relatório avançado PJ.

Quando a marcação Relatório avançado PJ estiver ligada, o sistema enviará as tags conforme exposto abaixo. Observe:

- Na tag CDOPÇÃO, o texto **"RPME"** será enviado na posição 05 do arquivo;
- Na tag MODELO, o envio do texto **"HPJ8"** ocorrerá na posição 131;
- Na tag RISKSCORING, envia-se o arquivo com o caractere **"E"** na posição 46;
- Na tag IND.LIMITE PJ, o arquivo enviará o caractere **"H"** na posição 392.

Além disso, se a referida marcação estiver selecionada, as marcações Indicador de Riskscoring e Limite de Crédito PJ também devem ser habilitadas.

Destacamos ainda que, caso você não realize nenhuma das marcações citadas acima,  apenas as informações básicas serão exibidas no retorno da consulta, incluindo o Quadro Social e Administração, porém para que este seja trazido, é preciso selecionar a marcação correspondente a ele.

**Importante:** no envio do arquivo, as marcações Quadro Social e Administração e Participações terão a posição 43, conforme determinadas condições. Observe:

- Quando ambas as marcações Quadro Social e Administração e Participações estiverem desmarcadas, o envio destas no arquivo será **"0"**, visto que, não gera quadro social e não gera participações;
- Ao acionar a marcação Quadro Social e Administração, e desmarcar Participações, o envio se dará com **"1"**, uma vez que, gera quadro social, porém não gera participações;
- Quando as marcações Quadro Social e Administração e Participações forem acionadas, o envio ocorrerá com **"2"**, em que irá gerar quadro social e participações;
- Porém, quando a marcação Quadro social e Administração não for acionado e a marcação Participações habilitada, o envio será realizado com **"3"**, ou seja, não gera quadro social, mas gera participações.

**Observação:** com a marcação Alerta de Identidade PJ habilitada, caso seja apresentada a mensagem **"RTMIUSUARIO NAO AUTORIZADO PARA NRI3"**, será necessário entrar em contato com o Serasa para verificar se você possui os devidos acessos para consultar a feature de Alerta de identidade PJ.

**Observação:** não é possível ativar simultaneamente as marcações **"Alerta de Identidade PJ"** e **"Indicador de Alertascoring"**. Caso você as selecione, será apresentada a mensagem:

**"Não é permitido escolher Indicador de Alertascoring junto com Alerta de identidade PJ."**

**Observação:** para que as marcações **"Modelo NRI1 Apres. Alerta de Ident. PJ"**, **"Modelo NRI2 Apres. Alerta de Ident. PJ"**, **"Modelo NRI3 Apres. Alerta de Ident. PJ"** sejam apresentadas na tela, marque a opção Alerta de Identidade PJ.

---

**Seção Monitore Gerencie Carteira**

Nesta seção, você poderá incluir um Parceiro ou Prospect no serviço de monitoramento de clientes do Serasa.

Ao efetuar a marcação **"Monitore Gerencie Carteira"**, serão apresentados os campos abaixo para definição do monitoramento:

Selecione a **"Quantidade de Dias de Monitoramento"** do seu Parceiro, de acordo as opções:

- Acompanhamento por 30 dias;
- Acompanhamento por 60 dias;
- Acompanhamento por 90 dias;
- Acompanhamento por 120 dias;
- Acompanhamento por 180 dias;
- Acompanhamento por período indeterminado.

Informe o **"Perfil do cliente"** e o **"Grupo de e-mail(opcional)"** previamente cadastrados no site do Serasa.

Após configurar o monitoramento, ao realizar uma consulta na tela [Análise de Risco Serasa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115753), a marcação Monitore Gerencie Carteira será exibida no pop-up **"Preferências"**. Sendo que, ao mantê-la habilitada, o CNPJ do Parceiro consultado será inserido no serviço de monitoramento. Ao desabilitar a referida marcação, não será possível gerar o arquivo de envio para monitoramento.

Após esse processo, o retorno do Serasa será apresentado na tela, com umas das seguintes mensagens:

**"Bloco #L08010200INCLUSAO NO MONITORE EFETUADA COM SUCESSO"**

**"Bloco #L08010210DOCUMENTO JA ESTA SENDO MONITORADO"**

Esta mensagem também será exibida no quadro Monitore Gerencie Carteira da Grade principal na tela Análise de Risco Serasa.

---

**Seção Bureau - Sintético**

Aqui, você poderá realizar consultas relacionadas ao CPF conforme o layout definido pelo manual do Serasa. Sendo assim, observe a seguir, as opções disponíveis para as análises de crédito:

- Resumo de Grafia;
- Registro de Consultas;
- Participação Societária;
- Resumo de Anotações Negativas;
- Pendências de Pagamentos;
- Dívida Vencida;
- Cheque Sem Fundo;
- Cheque Sustado;
- Protestos;
- Ações Judiciais;
- Falência;
- Dados de referências (Pessoais e/ou Bancárias);
- Documentos Roubados, Furtados e/ou Extraviados;
- Detalhes de outras grafias;
- Resumo de cadastro sintético;
- histórico de scoring base individual;
- Compromissos – Previsão de Pagamento;
- Cadastro de Compromissos Previstos;
- Quantidade de ocorrências;
- Alerta de Óbito;
- Alerta em negócios;
- Alerta de Identidade;
- Limite de Credito;
- Anotações SPC;
- Consultas ao SPC;
- Anotações e Consultas ao SPC;
- Confirmação de Dados Cadastrais;
- IRM –Ind Relac. Mercado;
- Gasto Estimado;
- Score Serasa;
- Score Serasa com SPC;
- Renda Pró;
- Renda Pró – consulta isolada;
- Risco de Crédito do Perfil;
- Recomenda Crédito;
- Capacidade Mensal de Pagamento;
- Capacidade Mensal de Pagamento – consulta isolada;
- Comprometimento Mensal Estimado;
- Comprometimento Mensal Estimado – consulta isolada;
- Consulta Isolada Vendas com Cartão PJ;
- Ind. de recuperação de Crédito - COLLEC. SCORING;
- Ind. de recuperação de Crédito - COLLEC. SCORING – cons. Isolada;
- Indicador Relacionamento Mercado e Setor – PF;
- Score positivo PF;
- Score positivo PF (PME);
- Renda Estimada;
- Tendencia de uso de Cartão de Crédito;
- Pontualidade de Pagamentos;
- Capacidade de Pagamento;
- Comprometimento de Renda;
- Indicador de Atraso;
- Tendencia de uso de Crédito e Financiamentos;
- Pontualidade de Pagamento de Cartão de Crédito;
- Ponderação de Dividas e Pagamentos;
- Comportamento de uso de Cheque Especial + AD Depositante;
- Hábitos de Pagamentos PF.

**Observação:** quando o parâmetro **"Salvar arquivo de envio e retorno do Serasa ? - SALVARARQSERASA"** estiver ligado, o sistema irá começar a salvar o arquivo enviado e o arquivo de retorno do Serasa no diretório informado no parâmetro **"Diretório onde será salvo o arquivo de envio e retorno do Serasa - REPOARQSERASA"**. Sendo que, este parâmetro não funciona com o repositório de arquivos. Este funcionará somente quando for utilizado o diretório do servidor, como, por exemplo /home/mgeweb/Serasa/.

**Nota:** você poderá utilizar o serviço de consulta do Serasa por meio de **"Ações Agendadas"**. Além disso, para utilizar essa integração é necessário que haja um registro na tabela TSICFG para o usuário zero, pois é com base nas configurações desse usuário, que as informações serão enviadas para o Serasa. Assim, você poderá utilizar a seguinte consulta para encontrar os dados na tabela: select \* from TSICFG t where CHAVE = 'configuracao.serasa.job'. Caso julgue necessário acesse o artigo [Ações Agendadas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110653).
