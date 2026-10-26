---
id: "5840766689559"
titulo: "Boleto rápido API"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559-Boleto-r%C3%A1pido-API"
trilha: "Manual do Produto > Financeiro e Patrimônio > Sankhya Fintech > Banking"
atualizado_em: "2026-10-09T19:16:48Z"
rotulos: ["Configuração", "Contas", "Boleto", "Financeiro", "COMPDEVACERTO", "Boleto Rápido API", "PERCMULTA", "Boleto Híbrido", "Banco do Brasil", "Boleto Simples", "Banco Itaú", "TAXADIAATRASO", "Banco Santander", "API", "Registro baixa alteração e retorno automático de boletos", "Emitir boletos via API", "Credenciamento configurações específicas por banco", "APIBDEBUG", "FILABOLETA", "Banco Sicoob", "Banco Sicredi", "Sankhya Fintech"]
---

# Boleto rápido API

| ```  Módulo: Financeiro > Consultas              Versão disponível: A partir da 4.20 ``` |
| --- |

---

O **Boleto rápido API** é uma solução do **Sankhya Fintech** que visa aumentar a eficiência operacional e a produtividade das empresas por meio da automação no processo de emissão e gestão de boletos bancários. Ao eliminar a necessidade de arquivos de remessa e retorno, essa solução simplifica e automatiza as operações financeiras de forma significativa.

**(1)** Principais funcionalidades:

- **registro de boletos:** emissão de boletos simples e híbridos (QR code para pagamento via PIX) de maneira rápida e eficiente, com todos os dados necessários para a cobrança;
- **reprocessamento de registros:** a partir da versão 4.29, é possível reenviar todos os boletos para uma nova tentativa de registro junto à instituição bancária. O botão **"Reprocessar registro"** está disponível na tela [Acompanhamento de Boletos - API](https://ajuda.sankhya.com.br/hc/pt-br/articles/7215349603223-Acompanhamento-de-Boletos-API);
- **cancelamento de boletos:** cancelamento de boletos por diversos motivos, como solicitação do cliente ou cancelamento da nota fiscal. O processo de cancelamento é detalhado no tópico [Cancelamento de um boleto](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559-Boleto-R%C3%A1pido-API#CancelamentodeumBoleto);
- **alterações de boletos:** permite ajustes nos dados do boleto, como vencimento, desconto e abatimento;
- **baixa e conciliação automática:** recebimento automático das informações de pagamento dos boletos, com baixa automática, facilitando o processo de conciliação bancária.

Atualmente, os bancos e modalidades ativas para o **Boleto rápido** são:

| **Banco** | **Modalidade** | **Versão** |
| --- | --- | --- |
| Banco do Brasil | Simples | 4.20 |
| Banco do Brasil | Híbrido | 4.22 |
| Banco Itaú | Simples | 4.23 |
| Banco Itaú | Híbrido | 4.23 |
| Banco Santander | Simples | 4.26 |
| Banco Santander | Híbrido | 4.26 |
| Banco Sicoob | Simples | 4.32 |
| Banco Sicoob | Híbrido | 4.32 |
| Banco Sicredi | Simples | 4.32 |
| Banco Sicredi | Híbrido | 4.32 |
| Banco Bradesco | Simples | 4.32 |
| Banco Bradesco | Híbrido | 4.35 |
| Banco Caixa Econômica Federal | Simples | 4.32 |
| Banco Safra | Simples | 4.32 |

![Imagem 1: Para entender como ocorre a cobrança do serviço Boleto rápido , acesse o artigo Detalhes de cobrança de serviço do…](https://ajuda.sankhya.com.br/hc/article_attachments/21042558210583) Para entender como ocorre a **cobrança do serviço Boleto rápido**, acesse o artigo [Detalhes de cobrança de serviço do boleto rápido](https://ajuda.sankhya.com.br/hc/pt-br/articles/14550240434839-Detalhes-de-cobran%C3%A7a-de-servi%C3%A7o-do-boleto-r%C3%A1pido).

| Configurações e processos para emissão de boletos |
| --- |
| [Habilitação e configuração do serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559-Boleto-r%C3%A1pido-API#Habilita%C3%A7%C3%A3oeconfigura%C3%A7%C3%A3odoservi%C3%A7o) |
| [Acompanhamento do serviço Boleto rápido](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559-Boleto-r%C3%A1pido-API#Acompanhamentodoservi%C3%A7oBoletoR%C3%A1pido) |
| [Boletos anteriores a ativação do serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559-Boleto-r%C3%A1pido-API#Boletosanterioresaativa%C3%A7%C3%A3odoservi%C3%A7o) |
| [Ocorrências de remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559-Boleto-r%C3%A1pido-API#Ocorr%C3%AAnciasdeRemessa) |
| [Alterações de dados do boleto](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559-Boleto-r%C3%A1pido-API#Altera%C3%A7%C3%B5esdedadosdoBoleto) |
| [Renegociação de títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559-Boleto-r%C3%A1pido-API#Renegocia%C3%A7%C3%A3odeT%C3%ADtulos) |
| [Compensação financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559-Boleto-r%C3%A1pido-API#Compensa%C3%A7%C3%A3oFinanceira) |
| [Cancelamento de um boleto](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559-Boleto-r%C3%A1pido-API#CancelamentodeumBoleto) |
| [Desabilitando o serviço Boleto rápido](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559-Boleto-r%C3%A1pido-API#Desabilitandooservi%C3%A7oBoletoR%C3%A1pido) |
| [Parâmetros que influenciam essa rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559-Boleto-r%C3%A1pido-API#par%C3%A2metrosqueinfluenciamessarotina) |

---

### Habilitação e configuração do serviço

O processo de credenciamento ao **Boleto Rápido** agora é condicionado à contratação prévia do serviço.

> ⚠️ **Atenção:** Atualmente, a API opera exclusivamente com contas vinculadas a CNPJ.

### 1. Pré-requisito: Contratação

Antes de iniciar a configuração técnica, o sistema verificará se o serviço está ativo. Caso você visualize a mensagem "Você ainda não contratou o PIX Imediato/Boleto Rápido":

![Imagem 2: Antes de iniciar a configuração técnica, o sistema verificará se o serviço está ativo. Caso você visualize a mensagem…](https://ajuda.sankhya.com.br/hc/article_attachments/38499218257943)

- Clique no botão **"Quero conhecer"** para ser direcionado ao Marketplace.
- Para detalhes sobre planos e valores, acesse o guia de [Contratação e cobrança dos serviços Fintech](https://ajuda.sankhya.com.br/hc/pt-br/articles/14550240434839-Contrata%C3%A7%C3%A3o-e-cobran%C3%A7a-dos-servi%C3%A7os-Fintech).

### 2. Fluxo de Credenciamento (Assistente de Melhores Práticas)

Com o serviço devidamente contratado, acesse a tela **Assistente de Melhores Práticas**, navegue até o menu **Configurações serviços Fintech**, selecione a opção **Boleto Rápido** e clique em **Iniciar**.

![Imagem 3: Com o serviço devidamente contratado, acesse a tela Assistente de Melhores Práticas , navegue até o menu Configurações…](https://ajuda.sankhya.com.br/hc/article_attachments/38499247663895)

O processo é dividido em 6 etapas:

1. **Seleção da Conta e Modalidade:** Selecione a conta bancária e defina o tipo de serviço: **Boleto Simples** ou **Boleto Híbrido** (que inclui QR Code para pagamento via PIX).

   ![Imagem 4: Seleção da Conta e Modalidade: Selecione a conta bancária e defina o tipo de serviço: Boleto Simples ou Boleto Híbrido…](https://ajuda.sankhya.com.br/hc/article_attachments/38499247664919)![Imagem 5: Seleção da Conta e Modalidade: Selecione a conta bancária e defina o tipo de serviço: Boleto Simples ou Boleto Híbrido…](https://ajuda.sankhya.com.br/hc/article_attachments/38499218263447)
2. **Dados da Conta Bancária:** Preencha as informações solicitadas.

   > ⚠️ **Importante:** Os dados variam conforme o banco. É crucial confirmar todas as informações com seu gerente bancário antes de preencher para evitar falhas na emissão.

![Imagem 6: ⚠️ Importante: Os dados variam conforme o banco. É crucial confirmar todas as informações com seu gerente bancário…](https://ajuda.sankhya.com.br/hc/article_attachments/38499218268311)

3. **Configuração de Cobrança:** Defina as regras de permanência do boleto após o vencimento, condições para negativação ou protesto, além de taxas de juros e multas.
4. **Ações Automáticas:** Configure os parâmetros para que os processos de baixa e conciliação ocorram de forma automática no ERP.

![Imagem 7: Ações Automáticas: Configure os parâmetros para que os processos de baixa e conciliação ocorram de forma automática no…](https://ajuda.sankhya.com.br/hc/article_attachments/38499218269335)

5. **Credenciais:** Insira o Client ID e o Client Secret gerados no portal de desenvolvedores do seu banco.

   - Consulte os links ao final deste artigo para guias específicos de cada banco.

![Imagem 8: Consulte os links ao final deste artigo para guias específicos de cada banco.](https://ajuda.sankhya.com.br/hc/article_attachments/38499247668375)

6. **Resumo de Configuração:** Revise todos os dados. Se estiverem corretos, clique em **"Instalar"**.

   - Ao concluir com êxito, a conta exibirá o status **CREDENCIADA**.

![Imagem 9: Ao concluir com êxito, a conta exibirá o status CREDENCIADA .](https://ajuda.sankhya.com.br/hc/article_attachments/38499247669527)![Imagem 10: Ao concluir com êxito, a conta exibirá o status CREDENCIADA .](https://ajuda.sankhya.com.br/hc/article_attachments/38499218275095)

---

### Informações Importantes

**1. Credenciamento via tela** [**‘Contas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas)**’:** Para clientes em versões que ainda não contemplam a implementação da nova jornada (PLG), recomendamos como alternativa o processo de credenciamento antigo: Na tela **Contas**, escolha a conta que será configurada como API. Em seguida, na aba [**Boleto(s)/Duplicatas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#ababoletosduplicatas), ative a marcação **Boleto Rápido** e selecione o serviço **API do Banco**. Clique no botão **Configurar Credenciais** para abrir o processo de credenciamento.

**2. Versões anteriores à 4.28:** Não será possível realizar atualizações de credenciamento ou novos credenciamentos em versões anteriores à **4.28**.

![Imagem 11: 2. Versões anteriores à 4.28: Não será possível realizar atualizações de credenciamento ou novos credenciamentos em…](https://ajuda.sankhya.com.br/hc/article_attachments/38499218275735)

#### Links para obtenção de Credenciais

- [Como obter as credenciais do Banco do Brasil](https://ajuda.sankhya.com.br/hc/pt-br/articles/21042285386391-Como-obter-as-credenciais-do-Banco-do-Brasil)
- [Como obter as credenciais do Banco Itaú](https://ajuda.sankhya.com.br/hc/pt-br/articles/21043102851223-Como-obter-as-credenciais-do-Banco-Ita%C3%BA)
- [Como obter as credenciais do Banco Santander](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069541531927-Como-obter-as-credenciais-do-banco-Santander)
- [Como obter as credenciais do Banco Sicoob](https://ajuda.sankhya.com.br/hc/pt-br/articles/30820232298007-Como-obter-as-credenciais-do-banco-Sicoob)
- [Como obter as credenciais do Banco Sicredi](https://ajuda.sankhya.com.br/hc/pt-br/articles/30801000122519-Como-obter-as-credenciais-do-banco-Sicredi)
- [Como obter as credenciais do Banco Bradesco](https://ajuda.sankhya.com.br/hc/pt-br/articles/36551875605911-Como-obter-credenciais-do-Banco-Bradesco)
- [Como obter as credenciais da Caixa Econômica](https://ajuda.sankhya.com.br/hc/pt-br/articles/32097122017431-Boleto-r%C3%A1pido-por-API-Caixa-Econ%C3%B4mica-Federal)
- [Como obter as credenciais do Banco Safra](https://ajuda.sankhya.com.br/hc/pt-br/articles/32712894425495-Boleto-r%C3%A1pido-por-API-Safra)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559-Boleto-r%C3%A1pido-API#top)

### Acompanhamento do serviço Boleto rápido

Com todas as configurações executadas, a conta estará apta para emitir boletos de cobrança por meio da API do banco, eliminando a necessidade de transferência de arquivos de remessa e retorno.

**Nota:** as operações do **Boleto rápido** são gerenciadas e gravadas sob o usuário **"0 - SUP"**, pois se tratam de ações automáticas no sistema.

![Imagem 12: Pode-se acompanhar o histórico e o monitoramento dos boletos por meio da tela Acompanhamento de Boletos - API .](https://ajuda.sankhya.com.br/hc/article_attachments/21042558210583) Pode-se acompanhar o histórico e o monitoramento dos boletos por meio da tela [Acompanhamento de Boletos - API](https://ajuda.sankhya.com.br/hc/pt-br/articles/7215349603223-Acompanhamento-de-Boletos-API).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559-Boleto-r%C3%A1pido-API#top)

### Boletos anteriores a ativação do serviço

A partir da **versão 4.33**, ao credenciar a conta, os boletos registrados via arquivo CNAB antes da ativação do serviço e que ainda estiverem abertos no banco serão automaticamente incorporados ao fluxo do **Boleto rápido**.

Para isso, o sistema identifica automaticamente todos os boletos pendentes com ocorrências de registro via CNAB e consulta a instituição bancária para validar seu status. Se o boleto ainda estiver ativo no banco, ele será atualizado para o status **"1 - Em aberto"** e seguirá o fluxo normal do serviço, permitindo alterações, cancelamentos e liquidações de forma automática pelo Boleto rápido.

Essa atualização torna o processo mais rápido e eficiente desde o momento da adesão, eliminando a troca manual de arquivos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559-Boleto-r%C3%A1pido-API#top)

### Ocorrências de remessa

Quando uma nova conta bancária for configurada para emissão de boletos com API do banco, as ocorrências de remessa e a conta bancária configurada serão inseridas automaticamente, além dos campos abaixo que serão monitorados pela API do banco:

- abatimento;
- abatimento cancelado;
- dt. vencimento;
- vlr desconto.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559-Boleto-r%C3%A1pido-API#top)

### Alterações de dados do boleto

Todas as alterações permitidas em boletos registrados são enviadas automaticamente ao banco pela API, sem necessidade de enviar arquivos de remessa ou renegociar o título.

A **API** monitora os seguintes campos para alterações:

- desconto;
- abatimento;
- cancelamento do abatimento;
- data de vencimento.

**Observações**

- **Desdobramento e juros/multa:** não é possível alterar o valor de desdobramento (na aba **Lançamento** da tela **Movimentação Financeira**) para boletos emitidos por contas bancárias integradas via **API**. Além disso, os valores de juros e multa inseridos diretamente no Sankhya, seja pela **Movimentação Financeira** ou pela tela **Cálculo de Juros e Multas** não são transmitidos. Se precisar ajustar esses valores, será necessário renegociar o título.
- **Prazos para alteração e cancelamento:**
  - **banco do Brasil:** após gerar o boleto, há um prazo de **30 minutos** para alterar a data de vencimento ou cancelar o boleto. Depois disso, as solicitações são enviadas ao banco;
  - **banco Itaú:** o prazo é de **24 horas** para realizar alterações ou cancelar. Após esse período, as solicitações também são enviadas ao banco;
  - **banco Santander:** não há tempo mínimo necessário para realizar alterações.

- **Restrições para alteração:**

  - no banco do Brasil, não é possível alterar a data de vencimento de boletos vencidos;
  - para todos os bancos, não é possível alterar títulos já pagos, liquidados ou baixados.

- **Informações de juros e multa:** os valores de juros e multa retornam no campo **"Vlr Juros"** da resposta da **API** e são preenchidos automaticamente na **Movimentação Financeira**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559-Boleto-r%C3%A1pido-API#top)

### Renegociação de títulos

Ao realizar a [Renegociação de títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393) de boletos registrados pela API do banco e confirmar a renegociação, os títulos originais são cancelados e novos são emitidos. Nesse processo, o sistema envia automaticamente duas instruções à **API** do banco:

1. cancelar os boletos antigos;
2. gerar novos títulos renegociados.

**Nota:** ao gerar um título, o envio automático para o banco ocorrerá exclusivamente no momento da geração do boleto, diretamente na tela de Renegociação de títulos.

**Observação:** a **Conta** usada na renegociação é definida pelo parâmetro **"Conta Padrão para Financeiro - CONTAPADRAOFIN"**. Se não houver conta informada neste parâmetro, será usada a conta do primeiro financeiro escolhido. Além disso, para renegociação de títulos com contas ativas na API, a marcação **"Manter nosso número para 1 título?"** não pode estar ativa. 

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559-Boleto-r%C3%A1pido-API#top)

### Compensação financeira

Esta rotina é realizada por meio da tela [Compensação financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115073-Compensa%C3%A7%C3%A3o-Financeira#top). Nela, você pode usar o valor total de uma receita para quitar uma despesa, o que resulta na baixa do título original. 

Quando a compensação total envolve boletos registrados pela **API** do banco, o sistema envia automaticamente uma instrução para **baixar ou cancelar** o boleto de cobrança.

**Observação:** se necessário, o documento de cobrança (boleto) atualizado deverá ser reimpresso na tela [Impressão de Boleto(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607094-Impress%C3%A3o-de-Boleto-s-).

Ao desfazer uma compensação total, o sistema cancela a operação e o título retorna ao status **Pendente** na tela **Movimentação Financeira**.

Para gerar um novo boleto após o cancelamento, é necessário seguir novamente o processo de registro do boleto, já que a baixa ou cancelamento anterior já foi registrado no banco.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559-Boleto-r%C3%A1pido-API#top)

### Cancelamento de um boleto

Você pode cancelar um boleto emitido por uma conta configurada com a API do banco das seguintes formas:

![Imagem 13: por meio da tela Movimentação Financeira , acione nos Filtros as marcações "Receita" , "Real" e "Pendente" , em…](https://ajuda.sankhya.com.br/hc/article_attachments/16116095969303) por meio da tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela), acione nos [Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#filtros) as marcações **"Receita"**, **"Real"** e **"Pendente"**, em seguida, selecione o registro desejado e acione o botão **"Excluir"**. Desse modo, será apresentado o aviso:

**"Você deseja realmente excluir o registro selecionado? Isso não pode ser desfeito."**

Confirme para realizar a exclusão do registro e do boleto vinculado a ele;

![Imagem 14: no Portal de Vendas , selecione a nota já confirmada e acione o botão "Cancelar Nota" . Ao confirmar a exclusão será…](https://ajuda.sankhya.com.br/hc/article_attachments/16116104455191) no [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601454-Portal-de-Vendas-Atributos-da-Tela), selecione a nota já confirmada e acione o botão **"Cancelar Nota"**. Ao confirmar a exclusão será apresentado um pop-up para ser informada a **"Justificativa"** do cancelamento. Feito isso, a nota será cancelada. 

Ainda existem outras situações em que o cancelamento do boleto ocorre automaticamente:

- alteração da conta bancária vinculada ao título;
- baixa do título financeiro;
- quando o campo Nosso Número for limpo;
- compensação integral dos títulos;
- renegociação dos títulos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559-Boleto-r%C3%A1pido-API#top)

### Desabilitando o serviço Boleto rápido

Para descredenciamento de uma ou mais contas credenciadas, basta selecionar a conta desejada na tela **'Assistente de Melhores Práticas' :: Configurações Fintech :: Boleto Rápido** e acessar a opção **"Descredenciar conta"**.

Essa ação descredencia a utilização da conta no serviço de Boleto Rápido, porém a cobrança pelo serviço continuará ocorrendo até que o contrato seja efetivamente cancelado. A credencial será inativada e o retorno dos boletos não serão feitos de forma automática.

Já para o cancelamento do contrato, um usuário com perfil gerencial — e diferente do usuário SUP — deve acessar a opção **"Cancelar contrato"**.

Essa ação desativa todas as contas credenciadas e realiza o cancelamento do serviço contratado junto à Sankhya Fintech.

> **Nota:** Para versões que não possuem acesso ao Assistente de Melhores Práticas, basta na tela **'Contas'** alterar a Conta configurada para outro tipo de emissão, como **"Boleto Avançado/Duplicatas"** ou **"Pix CNAB"**.

![Imagem 15: Nota: Para versões que não possuem acesso ao Assistente de Melhores Práticas, basta na tela 'Contas' alterar a Conta…](https://ajuda.sankhya.com.br/hc/article_attachments/40777775147287)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559-Boleto-r%C3%A1pido-API#top)

###

### Parâmetros que influenciam essa rotina

**Consumir API Bancos em modo Debug? - APIBDEBUG:** com este parâmetro ligado, os logs do Boleto rápido serão ligados para serem salvos no ServerLog.

**TOP de baixa para recebimentos - RCBTOPBAIXA:** se o campo TOP Baixa boleto estiver vazio na tela Contas, a TOP de baixa seguirá a configuração realizada neste parâmetro.

**Conta Padrão para Financeiro - CONTAPADRAOFIN:**na renegociação será utilizada a **"Conta"** informada neste parâmetro. Se não houver conta informada neste parâmetro, será usada a conta referente ao primeiro financeiro escolhido.

**Calcula valor liquido boleta? - VLRLIQBOL:** quando este parâmetro estiver ligado e uma conta for configurada para emitir os boletos via API do banco será enviado para o campo **"Valor Original"** o valor apresentado no campo **"Vlr. Líquido"**. Caso o parâmetro esteja desligado, o **"Vlr. Desdobramento"** será enviado para o campo Valor Original. 

**Controla boleto por fila? - FILABOLETA:** o serviço API não trabalha com a configuração de **"Fila de Boleto"**.

**Realizar compensação de devolução usando acerto - COMPDEVACERTO:** este parâmetro deve estar ligado para que a compensação financeira seja efetuada corretamente via API.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559-Boleto-r%C3%A1pido-API#top)
