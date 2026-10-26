---
id: "360045111033"
titulo: "Configuração Arquivo de Retorno"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111033-Configura%C3%A7%C3%A3o-Arquivo-de-Retorno"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-08-07T18:00:41Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Layout", "Configuração Arquivo de Retorno", "br.com.sankhya.configuracao.arquivo.retorno", "Configuração Arquivo de Retorno manual", "Financeiro", "Arquivo de Retorno", "Define layout para dados de pagamento", "Importação exportação e ocorrências", "Informações essenciais e marcadores", "EDI Bancário"]
---

# Configuração Arquivo de Retorno

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312389272599) Módulo: Financeiro > EDI Bancário
```

---

Esta tela permite que você configure o layout do arquivo de retorno na comunicação com [Bancos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598894-Bancos) a ser importado para o sistema. O Banco encaminha para a empresa um Arquivo de Retorno, contendo os dados de pagamentos e pendências das Contas a Receber.

[Preenchimentos Iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111033-Configura%C3%A7%C3%A3o-Arquivo-de-Retorno#preenchimentosiniciais)                                                   [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111033-Configura%C3%A7%C3%A3o-Arquivo-de-Retorno#botooutrasopes...)

[Parametrizações de Ocorrências do Retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111033-Configura%C3%A7%C3%A3o-Arquivo-de-Retorno#parametrizaesdeocorrnciasdoretorno)             [Validação do Retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111033-Configura%C3%A7%C3%A3o-Arquivo-de-Retorno#validaodoretorno)

![Imagem 2: Parametrizações de Ocorrências do Retorno Validação do Retorno](https://ajuda.sankhya.com.br/hc/article_attachments/4406595110807)

## Preenchimentos Iniciais

Para cadastrar, alterar ou excluir Arquivos de Retorno utiliza-se o Painel de Controle da árvore hierárquica.

Informe o **"Código"** do arquivo.

No campo **"Título"** aponte o nome do arquivo.

A marcação **"Ativo"** identificará se o registro encontra-se ou não ativo.

Ao acionar a marcação **"Detalhe"**, será indicado se o registro é ou não um registro de Detalhe.

Quando efetuar a marcação **"SQL para Número Único"** será permitido o uso de um comando **"SQL"** para localização de um ou mais registros do financeiro. Este SELECT deve ser configurado da seguinte forma:

```
SELECT TGFFIN.NUFIN

FROM TGFFIN, TSIEMP

WHERE TGFFIN.ORIGEM = 'E'

AND TGFFIN.RECDESP = 1

AND TGFFIN.SERIENOTA = :SERIENOTA

AND TGFFIN.NUMNOTA = :NUMNOTA

AND TSIEMP.CODEMP = TGFFIN.CODEMP

AND TSIEMP.CGC = :CGC
```

O exemplo acima mostra um comando SQL que retorna uma ou mais linhas com o campo TGFFIN.NUFIN e recebe os seguintes parâmetros: **:SERIENOTA**, **:NUMNOTA** e **:CGC**.

Observe que os parâmetros são identificados pelo caractere **':'** (dois pontos) e seu tipo definido pelos sufixos **TXT\_** (para parâmetros texto) e **INT\_** (para parâmetros inteiros). Estes parâmetros devem ser configurados como campos do layout.

O campo **"Stored Procedure Chamada"** será disponibilizado para a criação e associação de uma stored procedure (rotina programada no Banco de Dados) para cada tipo de registro definido no layout. Esta rotina permite que sejam definidas as atualizações que deverão ser realizadas provenientes desta importação.

Os campos do cabeçalho serão exibidos de acordo com a seleção dos registros na árvore hierárquica. O campo **"Stored Procedure Chamada"**, só será apresentado para o arquivo pai.

Para maiores informações referente à marcação **"Conciliação Extrato Bancário"** acesse a rotina [Conciliação Extrato Bancário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606214-Concilia%C3%A7%C3%A3o-Extrato-Banc%C3%A1rio).

![Imagem 3: Para maiores informações referente à marcação "Conciliação Extrato Bancário" acesse a rotina Conciliação Extrato…](https://ajuda.sankhya.com.br/hc/article_attachments/4406595114263)

**Observação:** o campo **"Taxa Administrativa"** em destaque na imagem acima, tem a finalidade de definir como será considerada a taxa administrativa na baixa dos títulos. Ela estará visível na tela se um ou ambos parâmetros **"Somar (e zerar) taxa ao valor da baixa no ret.banc - SOMATXVLRBAIXA"** e **"Subtrai taxa ao valor da baixa no retorno bancário - SUBTXVLRBAIXA"** estiverem ligados. Após a configuração destes, o referido campo poderá ser definido entre as seguintes opções:

- **Considerar configuração global:** Está opção é a default (padrão). Quando não for configurada, valerá a configuração da forma que estão os parâmetros na base de dados, ou seja, determina que a rotina terá o comportamento atual.
- **Nada a fazer:** O sistema ignora a configuração do parâmetro e não utiliza em nada a taxa administrativa, ou seja, nem a soma e nem a subtrai no momento da baixa, de modo que serão respeitados os valores advindos do arquivo de retorno. Qualquer configuração relacionada à isto será ignorada.
- **Somar ao valor recebido:** O sistema irá ignorar os parâmetros e irá somar o valor da taxa ao valor recebido, informando o resultado no valor da baixa.
- **Subtrair do valor recebido:** O sistema irá ignorar os parâmetros e irá subtrair o valor da taxa ao valor recebido, informando o resultado no valor do desconto do título.

A parte inferior desta tela se destina-se a realização do cadastro dos campos juntamente às suas respectivas descrições:

![Imagem 4: A parte inferior desta tela se destina-se a realização do cadastro dos campos juntamente às suas respectivas descrições:](https://ajuda.sankhya.com.br/hc/article_attachments/4406595117079)

No caso da Configuração do Arquivo de Retorno não se deve incluir dentro do layout todos os campos disponíveis no manual do banco, como é feito no [Arquivo de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025392953-Configura%C3%A7%C3%A3o-Arquivo-de-Remessa). Para assegurar uma gestão financeira, fiscal e contábil eficaz, deve-se incluir apenas os campos abaixo, com suas respectivas posições:

- Identificador;
- Banco;
- Agência;
- Carteira;
- Nosso Número;
- Nufin;
- Valor Título;
- Valor Juros;
- Valor Descontos;
- Valor Abatimentos;
- Valor Baixa;
- Data Baixa;
- Data Crédito;
- Taxa Admin;
- Ocorrência;
- Conta;
- Dígito da Conta.

**Nota:** o identificador Dígito da Conta atende aos padrões do banco Itaú para número de conta e, também diferencia pelo dígito, as contas que eventualmente tenham números iguais. Esse campo é concatenado com o campo Conta.

Lembrando que, os campos Valor Juros e Valor Descontos são de preenchimento obrigatório. 

![Imagem 5: Os layouts de banco que não incluem campos específicos, como, Valor Juros e Valor Descontos , poderão ter posições…](https://ajuda.sankhya.com.br/hc/article_attachments/26191674643735) Os layouts de banco que não incluem campos específicos, como, Valor Juros e Valor Descontos, poderão ter posições zeradas no layout atual do arquivo.

**Observação:** se a conta do titulo não tiver uma conta configurada para baixa de retorno (cadastro de [Conta](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas), aba [EDI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#abaintercmbioeletrnicodedadosedi), campo **"Conta p/ baixa"**), o sistema fará a baixa com a conta configurada no arquivo, e caso localize mais de um cadastro com mesmo banco e conta, utilizará o cadastro com menor código.  

Além das variáveis convencionais listadas acima, tem-se também as variáveis abaixo que podem ser utilizadas na **"Configuração de Ocorrências"**, conforme máscara, que vem logo após o nome da variável.

```
DATABAIXA

DATABAIXADDMMYYYY

DATABAIXAYYYYMMDD

DATABAIXAYYMMDD

DATACREDITO

DATACREDITODDMMYYYY

DATACREDITOYYYYMMDD

DATACREDITOYYMMDD

DATAVENCIMENTO

DATAVENCIMENTODDMMYYYY

DATAVENCIMENTOYYYYMMDD

DATAVENCIMENTOYYMMDD
```

Salientando que YY - corresponde a data para ano (dois dígitos)/ MM - data para mês (dois dígitos)/ DD data dia (dois dígitos). As variáveis **"DATABAIXA"**, **"DATACREDITO"** e **"DATAVENCIMENTO"** apresentarão as datas com máscara no formato **"DDMMYY"**.

Ao clicar no botão **"Novo"** a tela passa para o modo Formulário permitindo a configuração do campo do layout:

![Imagem 6: Ao clicar no botão "Novo" a tela passa para o modo Formulário permitindo a configuração do campo do layout:](https://ajuda.sankhya.com.br/hc/article_attachments/4406588101271)

Informe no campo **"Sequência"** o código sequencial dos campos que irão compor o registro que está sendo configurado.

No campo **"Início"** você deverá inserir a Posição Inicial do campo.

Aponte no campo **"Fim"** a Posição Final do campo.

A marcação "Identificador" deverá ser habilitada para o campo que será utilizado para identificar o Registro de Detalhe, dentro do Arquivo de Retorno.

Deverá ser informado no campo **"Conteúdo p/ Identificação"** o conteúdo do campo identificador do registro de detalhe.

**Nota:** quando uma remessa de cobrança Pix for gerada, os títulos que compõem a remessa poderão ser identificados por meio do **"Nufin"**, **"NossoNumero"** ou **"TXID"** para que, dessa forma, os títulos Pix sejam devidamente processados por meio do arquivo de retorno.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111033-Configura%C3%A7%C3%A3o-Arquivo-de-Retorno#top)

## Botão Outras Opções...

O botão Outras Opções... conta com duas funcionalidades, **"Importar Layout"** e **"Exportar Layout"**; ambas tem por objetivo facilitar a configuração de layouts no sistema, uma vez que layouts já existentes em outras bases poderão ser importados e reutilizados, tem-se a geração de economia de tempo e trabalho na confecção destes arquivos.

![Imagem 7: O botão Outras Opções... conta com duas funcionalidades, "Importar Layout" e "Exportar Layout" ; ambas tem por objetivo…](https://ajuda.sankhya.com.br/hc/article_attachments/4406595133847)

Ao acionar a opção Importar Layout, será aberto um pop-up para upload do arquivo desejado. De forma contrária, a opção Exportar Layout disponibiliza o layout fora do sistema para ser utilizado conforme a necessidade da empresa. É importante citar que os arquivos que poderão ser importados ou exportados, devem ser do formato **".xml"**.

**Importante:**  o layout poderá ser importado em uma base, desde que esta base suporte a estrutura hierárquica deste layout. Portanto, é essencial se atentar para a configuração realizada no parâmetro **"Máscara para Intercâmbio Eletrônico de Dados (EDI) - MASCEDI"**. Por exemplo, se em uma base para a qual será feita a importação, a máscara definida no referido parâmetro é **"99\.99\.99;0"**, não será possível importar um layout que possua **"4"** (quatro) níveis hierárquicos.

**Observação:** utilizando as funcionalidades Importar Layout e Exportar Layout; os campos **"Inserir quando não existir o registro"** e **"Alterar"** localizados na Configuração de Ocorrências de Retorno (descrita no tópico abaixo) não serão importados/exportados, visto que os mesmos possuem configurações relativas à várias empresas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111033-Configura%C3%A7%C3%A3o-Arquivo-de-Retorno#top)

## Parametrizações de Ocorrências do Retorno

Na tela Configuração Arquivo de Retorno bancário, clicando no Botão Outras Opções... tem-se a opção **"Configurações de Ocorrências..."**.

![Imagem 8: Na tela Configuração Arquivo de Retorno bancário, clicando no Botão Outras Opções... tem-se a opção "Configurações de…](https://ajuda.sankhya.com.br/hc/article_attachments/4406588129175)

**Importante:** neste processo, as Ocorrências deverão ser cadastradas. Antes de configurá-las, faz-se necessário selecionar o campo **"Ocorrência"**. Se o usuário clicar sobre outro campo e configurar as ocorrências, neste outro campo, o processamento do retorno bancário não funcionará.

Vejamos abaixo o pop-up de **"Configuração de Ocorrências de Retorno"**:

![Imagem 9: Vejamos abaixo o pop-up de "Configuração de Ocorrências de Retorno" :](https://ajuda.sankhya.com.br/hc/article_attachments/4406588132503)

Insira o **"Cód. Ocorrência"** informado no manual do banco, para identificar a operação.

No campo **"Descrição"** informe o nome da ocorrência.

Caso seja efetuada a marcação **"Reportar(Exibe mensagem p/ cada linha)"** fará com que o sistema mostre o processamento ao usuário quando passar pela ocorrência em questão.

A marcação **"Interromper"** quando realizada, interrompe o processo ao passar pela ocorrência.

Referente à opção **"Gravar QR Code Pix"**, esta indicará ao sistema que deverá gravar no campo **"PIX Copia e Cola"** da aba [Lançamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874#abalanamento) da [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira), no título identificado por meio do seu TXID, o conteúdo especificado nas posições definidas para a variável QRCODE (presente também no arquivo de retorno). 

**Observação:** você pode optar por gravar esse código e não enviá-lo ao cliente, porém não será possível enviá-lo ao cliente sem que este seja gravado no sistema.

Ao acionar a marcação **"Baixar"**, será baixado o(s) título(s) após o processamento.

A marcação **"Baixar Parcial"** é utilizada para realizar a baixa de um título com valor menor e deixar o restante como pendência.

Quando a marcação **"Enviar E-mail Pix"** for marcada, o documento de cobrança do PIX será enviado para a fila de envios de e-mail ao cliente de acordo com o modelo de e-mail que você definir na tela [Modelo de E-mail](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110133) e informá-lo no campo **"Modelo corpo e-mail"** da seção **"Configurações para Envio de E-mail Pix"**.

**Observação:** se você optar por habilitar essa marcação, lembre-se que a marcação Gravar QR Code Pix também deve ser acionada.

Além de que, quando você realizar a habilitação da marcação Enviar E-mail Pix, a seção  Configurações para Envio de E-mail Pix será exibida para que, assim, você realize o preenchimento dos campos Modelo corpo e-mail e **"Rel. Formatado Pix"**.

Posteriormente, você pode realizar a identificação do remetente da mensagem da seguinte maneira:

1. Verifique a **"Conta STMP"** cadastrada na tela Modelo de E-mail, vinculado ao campo Modelo corpo e-mail desta tela;
2. Na ausência desta, observe a Conta STMP da empresa do título;
3. Caso esta também não seja informada, confira a conta presente na tela [Servidor STMP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593494).

Assim, observe a forma como os destinatários das mensagens serão definidos:

1. O e-mail inserido no campo **"Email"** da aba [Endereço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abaendereo) do [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros) será considerado  o principal;
2. Todos os contatos que estiverem com a marcação **"Recebe boleto/Pix p/ email"** da sub-aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#sub-abageral), aba [Contatos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abacontatos) do Cadastro de Parceiros habilitada, serão colocados em cópia no envio;
3. Caso não haja e-mail informado para o parceiro, o sistema tornará o primeiro contato encontrado como o principal, e os demais serão definidos como cópia.

**Importante:** se não for possível identificar o remetente e/ou destinatário considerando as condições acima, o registro na fila de e-mails não será gerado.

Tratando-se da marcação **"Alterar"** o seu acionamento comporta as seguintes funcionalidades:

1. Exibirá a seção **"Configurações do Alterar"** que possibilita a modificação de algumas informações do título no processamento do retorno. As informações a serem alteradas são o Tipo de Título, Centro de Resultado, Natureza, Conta Bancária e Banco.
2. Por meio das ocorrências do tipo Alterar, será possível acrescentar os valores de despesas com cartórios. Para isso, basta que o usuário que esta configurando a mesma, selecione o layout bancário que deseja criar a ocorrência para ajuste da Despesa com Cartório e efetue a inclusão do campo.

Em seguida, selecione o campo no qual são mapeadas as ocorrências e acione no botão [Outras opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111033-Configura%C3%A7%C3%A3o-Arquivo-de-Retorno#h_01EC5VZ5BGC9MPJ9PRFSZJZPMJ) a opção **"Configurações de Ocorrências"**. Deste modo, será exibida a tela **"Configurações de Ocorrências de Retorno"**.

Logo após, será necessário criar a nova ocorrência do tipo Alterar e adicionar o campo que deseja ser ajustado quando a ocorrência cadastrada existir no arquivo de remessa quando for processado.

**Observação:** o nome deste campo deve ser igual ao nome do campo configurado no layout bancário, e por sua vez igual a coluna do banco de dados que se deseja fazer o ajuste. Caso sejam vários campos, basta colocá-los separados por **";"**. Como por exemplo DESPCART;NUFIN;DIGSAFRA.

No processo de cobrança registrada depois que o título foi enviado para protesto, há situações em que o banco devolve o título de cobrança pelo tempo de vencimento do mesmo. Quando isto é feito, o arquivo de retorno vem com a instrução para retirar a responsabilidade de cobrança pelo banco, retornando à responsabilidade para a empresa (cada banco tem uma ocorrência diferente). Para tanto, na seção Configurações do Alterar além do preenchimento dos campos Conta Bancária e Banco; utiliza-se a opção **"Remover título do monitoramento de cobrança"** para indicar que o título deverá ser retirado do monitoramento de cobrança.

![Imagem 10: No processo de cobrança registrada depois que o título foi enviado para protesto, há situações em que o banco devolve o…](https://ajuda.sankhya.com.br/hc/article_attachments/4406595163287)

A marcação **"Conciliar"** quando efetuada, irá conciliar os títulos baixados depois do processamento.

Quando acionar a marcação **"Registrar Nosso nº"** será gerado o nosso número no(s) título(s), gravando na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira).

Efetuando-se a marcação **"Registrar Log"** serão registradas todas as movimentações que são feitas no processamento do retorno, na tabela.

A marcação **"Inserir quando não existir o registro"** é utilizada quando estamos processando um arquivo de retorno e neste possui um título que não está cadastrado no sistema. Então, podemos habilitar esta marcação e, ao processar o arquivo, será cadastrado automaticamente o título no financeiro.

Acionando a marcação **"Motivo de Rejeição"**, processando um Retorno que tenha ocorrência de Entrada Rejeitada e esteja utilizando esta configuração, o sistema apresentará os Motivos de Rejeição cadastrados e os gravará no campo Observação da tabela de **"Log"** de ocorrências bancárias (TSIOBCLOG).

**Cadastro de Motivo de Rejeição de Entradas de Retorno Bancário:**

Dentro do pop-up **"Configuração da Ocorrência de Retorno"**, tem-se a opção para cadastrar os **"Motivos de Rejeição"** para ocorrência de entradas rejeitadas, nas configurações de retorno bancário. Para isto, basta acionar o botão Motivos de Rejeição, onde será aberta uma janela para informar-se o Código e a Descrição da Rejeição.

[GIF animado: Imagem 11: Dentro do pop-up "Configuração da Ocorrência de Retorno" , tem-se a opção para cadastrar os "Motivos de Rejeição" para…](https://ajuda.sankhya.com.br/hc/article_attachments/4406588163735)

Novamente na tela de Configuração Arquivo de Retorno, na grade de campos do arquivo, é necessário cadastrar-se uma ou mais das seguintes variáveis de erro (quantas forem necessárias):

Erro1, Erro2, Erro3, Erro4 etc, informando as respectivas posições, para que o sistema localize os motivos de rejeição no arquivo e grave corretamente a observação no log de processamento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111033-Configura%C3%A7%C3%A3o-Arquivo-de-Retorno#top)

## Validação do Retorno

Após validar o Arquivo de Remessa e receber o Arquivo de Retorno, deve-se processar este último no sistema e posteriormente validar se foram feitas as atualizações conforme as configurações de **"Ocorrências"**, efetuadas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111033-Configura%C3%A7%C3%A3o-Arquivo-de-Retorno#top)
