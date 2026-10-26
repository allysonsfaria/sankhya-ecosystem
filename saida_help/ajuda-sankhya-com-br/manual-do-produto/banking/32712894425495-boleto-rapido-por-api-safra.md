---
id: "32712894425495"
titulo: "Boleto rápido por API - Safra"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32712894425495-Boleto-r%C3%A1pido-por-API-Safra"
trilha: "Manual do Produto > Financeiro e Patrimônio > Sankhya Fintech > Banking"
atualizado_em: "2026-08-07T19:56:15Z"
rotulos: ["Configuração", "Boleto", "Financeiro", "Boleto Rápido API", "Boleto rápido", "Como obter credenciais", "API", "API do Banco", "EDI automático", "Banco Safra", "Sankhya Fintech", "Safra"]
---

# Boleto rápido por API - Safra

O [Boleto rápido API](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559) é uma solução do **Sankhya Fintech** que visa aumentar a eficiência operacional e a produtividade das empresas por meio da automação no processo de emissão e gestão de boletos bancários. Ao eliminar a necessidade de arquivos de remessa e retorno, essa solução simplifica e automatiza as operações financeiras de forma significativa.

Confira abaixo como credenciar uma conta do banco **Safra** no Boleto rápido.

| Credenciamento Safra |
| --- |
| [Configurações iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/32712894425495-Boleto-r%C3%A1pido-por-API-Safra#Configura%C3%A7%C3%B5esiniciais) |
| [Ativação do EDI automático](https://ajuda.sankhya.com.br/hc/pt-br/articles/32712894425495-Boleto-r%C3%A1pido-por-API-Safra#Ativa%C3%A7%C3%A3odoEDIautom%C3%A1tico) |
| [Configurações de ações automáticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/32712894425495-Boleto-r%C3%A1pido-por-API-Safra#Configura%C3%A7%C3%B5esdea%C3%A7%C3%B5esautom%C3%A1ticas) |

---

## Configurações iniciais

Acesse o Assistente de Melhores Práticas e, em Configurações serviços Fintech › Boleto Rápido, na etapa "Selecionar conta", selecione a conta a ser credenciada. Clique em Avançar para iniciar a jornada de credenciamento.

![Assistente de Melhores Práticas – Boleto Rápido, etapa Selecionar a conta para credenciar, com a lista de contas…](https://ajuda.sankhya.com.br/hc/article_attachments/42461262469015)

O credenciamento do Boleto rápido é composto por três etapas:

### ![Imagem 2: Modalidade do serviço](https://ajuda.sankhya.com.br/hc/article_attachments/42309651824023) Modalidade do serviço

Escolha a modalidade do serviço, selecionando a opção **Boleto simples**.

**Importante:** a modalidade Boleto híbrido não está disponível para o banco Safra.

![Assistente de Melhores Práticas – Boleto Rápido, etapa Selecionar tipo de serviço, com a opção Boleto Simples…](https://ajuda.sankhya.com.br/hc/article_attachments/42461278565143)

### ![Imagem 4: Configuração de cobrança](https://ajuda.sankhya.com.br/hc/article_attachments/42309645992599) Configuração de cobrança

####

#### **(1)** Configurar ações após o vencimento do título

Nesta etapa é possível definir regras para a permanência do boleto, negativação e protesto.

**(3)**Nessa opção, o campo **Permanência após o vencimento** indica se o boleto permanecerá ativo no banco após o vencimento: 

- se a opção**Seguir com a permanência padrão do convênio** for selecionada, a validade dos boletos respeitará o prazo acordado com a instituição bancária no momento da contratação dos serviços de emissão de boletos;
- já, escolhendo a opção**Configurar manualmente a permanência após o vencimento**, o prazo de permanência dos boletos após o vencimento deverá ser inserido no campo **Dias de permanência após o vencimento**.

**(3)**Na seção **Negativação**, especifique se o boleto será negativado após o vencimento. Caso opte pela negativação, informe o número de dias corridos após o vencimento no campo **Dias para negativação** para que a negativação ocorra automaticamente.

**(3)**Defina no campo **Dias para protesto** se o boleto será protestado após o vencimento. Se optar pelo protesto, informe o número de dias corridos após o vencimento para que o protesto ocorra automaticamente.

**Nota:** para as contas do Banco Safra não é possível negativar e protestar o título ao mesmo tempo.

![Assistente de Melhores Práticas – Boleto Rápido, etapa Vencimento do Título, com as opções de permanência, negativação…](https://ajuda.sankhya.com.br/hc/article_attachments/42461278567063)

#### **(1)** Configurar juros

**(3)**Determine os **Tipos de Juros**dentre as seguintes opções:

- **dispensar a cobrança de juros:** não será atribuído juros no boleto;
- **definir uma taxa diária (em porcentagem):** no registro do boleto será considerado um percentual diário para cobrança de juros. Com essa opção ativada, o campo **Valor percentual** será habilitado. Nele, informe o percentual de juros. Por exemplo, caso seja informado 1%, será cobrado uma taxa de juros de 1% ao dia;
- **definir um valor fixo (R$) por dia de atraso:** no registro do boleto será considerado um valor diário em reais para cobrança de juros. Escolhendo essa opção, o campo **Valor em reais** será habilitado. Nele, preencha o valor dos juros. Por exemplo, caso seja informado R$ 1,00, será cobrado uma taxa de juros de R$ 1,00 ao dia.

**(3)**Defina no campo **Data dos juros**a partir de qual data serão cobrados os juros, dentre as seguintes alternativas:

- **usar data de vencimento:** a data de vencimento será considerada para cobrança de juros;
- **configurar quantidade de dias:** será possível configurar uma quantidade de dias considerando a data de vencimento como base para cobrança de juros. Por exemplo, caso seja informado um dia no campo, será usada a Data de Vencimento + 1, ou seja, os juros serão cobrados um dia a partir da data do vencimento.

![Assistente de Melhores Práticas – Boleto Rápido, etapa Juros, com as opções de tipo de juros para o Banco Safra.](https://ajuda.sankhya.com.br/hc/article_attachments/42461278567575)

#### **(1)** Configurar multa

**(3)**Configure também os**Tipos de Multa**, conforme as alternativas a seguir:

- **dispensar a cobrança de multa:** não será atribuído multa no boleto;
- **definir um percentual em relação ao valor do título:** ao registrar o boleto será definido uma porcentagem de multa sobre o valor do título. Ao selecionar essa a opção, o campo **Valor Percentual** será habilitado para informar o percentual de multa a ser aplicado. Por exemplo, se for definido 10%, a multa corresponderá a 10% do valor do título;
- **definir um valor fixo (R$):** no registro do boleto será considerado um valor fixo em reais para cobrança de multa. Com essa opção marcada, o campo **Valor em Reais** será habilitado para preencher um valor fixo de multa, independentemente do valor do título. Por exemplo, se for definido R$ 10,00, a multa aplicada será exatamente R$ 10,00, sem variação conforme o valor do boleto.

**(3)**Defina no campo **Data da Multa**a partir de qual data será cobrada a multa, dentre as seguintes alternativas:

- **usar data de vencimento:** a data de vencimento será considerada para cobrança de multa;
- **configurar quantidade de dias:** será possível configurar uma quantidade de dias considerando a data de vencimento como base para cobrança de multa. Por exemplo, caso seja informado um dia no campo, será usada a Data de Vencimento + 1, ou seja, a multa será cobrada um dia a partir da data do vencimento. Com essa opção marcada, o campo **Dias para multa** deverá ser preenchido com um valor que não seja negativo.

**Observação:** é obrigatório o preenchimento de todos os campos que forem habilitados. 

![Assistente de Melhores Práticas – Boleto Rápido, etapa Multa, com as opções de tipo de multa para o Banco Safra.](https://ajuda.sankhya.com.br/hc/article_attachments/42461262474007)

Ao concluir as configurações, os tópicos configurados corretamente serão marcados como finalizados, permitindo o avanço para a próxima etapa.

---

## Ativação do EDI automático

Para ativar o serviço do Boleto rápido Safra, siga os passos abaixo.

### **(3)**Autorização para EDI automático

Nesta etapa, você vai preencher as informações necessárias para enviar a carta de autorização do EDI automático. Essa autorização é fundamental, pois, embora o Safra já ofereça integração por API, nem todas as operações são feitas automaticamente por esse canal.

A troca de arquivos CNAB com o banco será feita de forma automática pela Kobana, nossa parceira autorizada para esse tipo de serviço. Depois que as informações forem enviadas, você vai receber um e-mail da Kobana confirmando que a carta foi mandada para o banco.

**Importante:**

- você não precisa contratar a Kobana — a Sankhya Fintech já cuidou disso para você;
- você também não precisa configurar nada nem gerar arquivos manualmente;
- toda a comunicação com o banco será feita automaticamente pela Kobana.

Siga os passos abaixo para fazer a autorização:

**1.** preencha os dados para gerar a carta de autorização. Essa carta será enviada por e-mail ao banco e vai permitir que a Kobana faça a troca de arquivos com ele. Os e-mails informados também receberão uma cópia dessa carta, junto com uma apresentação sobre a Kobana;

Preencha os seguintes dados pessoais do responsável pela conta bancária, do gerente do banco e de quem está preenchendo a carta.

![Assistente de Melhores Práticas – Boleto Rápido, etapa Credenciais (via EDI), com os campos de dados do responsável…](https://ajuda.sankhya.com.br/hc/article_attachments/42461262475415)Clique em **Avançar**, e informe os dados da conta bancária:

- número da agência;
- conta-corrente com dígito;
- CNPJ da conta-corrente;
- carteira do convênio;
- número do último boleto emitido com essa conta.

**Importante:** você poderá ver o andamento da autorização do EDI Automático pela linha do tempo mostrada logo abaixo.

![Assistente de Melhores Práticas – Boleto Rápido, etapa Dados da conta, com os campos de agência, conta, CNPJ, carteira,…](https://ajuda.sankhya.com.br/hc/article_attachments/42461278569367)

**2.** fale com o gerente do seu banco. Depois de preencher os dados, entre em contato com o gerente do seu banco para reforçar a solicitação de ativação do serviço;

**3.** espere a confirmação do banco. Você vai receber um e-mail confirmando que o serviço foi ativado com sucesso. Só depois dessa confirmação será possível seguir para o próximo passo;

**4.** volte e finalize o credenciamento. Depois da confirmação, clique no botão **Habilitar** que aparece na tela para terminar o processo.

**Importante:** com a ativação do EDI, alguns bancos podem restringir o acesso manual aos arquivos de remessa e retorno no Internet Banking. Se você quiser continuar acessando esses arquivos, fale com o seu banco para saber se isso é possível.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/32712894425495-Boleto-r%C3%A1pido-por-API-Safra#top)

---

### ![Imagem 10: Credenciamento de conta](https://ajuda.sankhya.com.br/hc/article_attachments/42309645993495) Credenciamento de conta

Depois que o banco configurar o serviço, você vai receber um e-mail avisando que seu credenciamento poderá ser efetivado.

Acesse novamente a jornada de adesão, vá até o último passo e clique em **"Credenciar"** para finalizar o processo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/32712894425495-Boleto-r%C3%A1pido-por-API-Safra#top)

---

## Configurações de ações automáticas

Na etapa Ações Automáticas do Assistente de Melhores Práticas, poderão ser realizadas as seguintes configurações abaixo:

### ![Assistente de Melhores Práticas – Boleto Rápido, etapa Ações Automáticas, com os campos de baixa automática, lançamento…](https://ajuda.sankhya.com.br/hc/article_attachments/42461278570007)

(1)** Baixa automática**

Determine se a **Baixa automática** será feita via API, conforme as alternativas: 

- não realizar;
- realizar na data de pagamento;
- realizar na data do crédito em conta.

Pode-se verificar se o boleto foi baixado e conciliado automaticamente por meio dos campos:

- **histórico**: localizado na aba [Lançamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Lan%C3%A7amento) da tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela) para versões menores que 4.23;
- **baixa por API:** deverá ser ativado por meio da opção de configurações de formulário para versões 4.24 ou maiores.

Quando um boleto for baixado automaticamente, o campo receberá a seguinte descrição:

**"Baixado automaticamente pela API do Banco."**

Caso falte alguma configuração que impeça a API de realizar a baixa automática, aparecerá no Histórico do título na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753):

**"Não foi possível realizar a baixa automática. Verifique triggers e processos de baixa."**

Já, o campo **Baixa por API** trará o tipo de erro que impediu a realização da baixa.

### **(1)** Lançamento baixa boleto

O campo **Lançamento baixa boleto**refere-se ao tipo de lançamento bancário. Se esse campo estiver vazio na tela [Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113), o código de lançamento bancário a ser utilizado será aquele especificado no campo **Lançamento bancário receitas**, na aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades) das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa).

### **(1)** TOP baixa boleto

No campo **TOP Baixa boleto** informe uma TOP de lançamento ao título. Lembre-se que, esse campo deve ser preenchido para que a baixa automática seja efetuada.

### **(1)** Conciliação automática

O campo **Conciliação automática** pode ser configurado apenas quando o campo **Baixa Automática** não estiver com a opção **Não realizar** selecionada. Nele, defina a forma da Conciliação automática, conforme as opções: 

- não realizar;
- realizar na data de pagamento;
- realizar na data do crédito em conta.

**Nota:** a baixa e conciliação automáticas para contas do Banco Safra só devem seguir a opção **Realizar na data do crédito em conta** caso o prazo de recebimento seja 0 ou 1 dia, visto que o banco não retorna via API a data de crédito em conta.

### **(1)** Na tela "Contas", aba Boleto/Duplicata

Por meio do campo**Modelo Cobrança**busque e selecione o modelo de boleto cadastrado na tela [Modelos de Nota Fiscal/Duplicatas/Boletos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913-Modelos-de-Nota-Fiscal-Duplicatas-Boleto-s-).

Defina a impressora que será utilizada para emissão do documento.

### **(1)** Considerações sobre o funcionamento do boleto rápido Safra

Se você usa o Boleto bápido Safra, fique atento a alguns pontos importantes sobre o envio e retorno dos arquivos:

- **envio de remessa ao banco**: o sistema manda o arquivo para o Safra a cada 10 minutos;
- **tempo de resposta do banco**: o banco leva cerca de 4 horas para processar esse arquivo;
- **retorno com a resposta do banco**: a resposta do banco só aparece no próximo dia útil (D+1).
- **acompanhamento da operação**: você pode acompanhar tudo pela tela [Acompanhamento de Boletos - API](https://ajuda.sankhya.com.br/hc/pt-br/articles/7215349603223), lembrando que a resposta do banco só estará disponível no dia útil seguinte.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/32712894425495-Boleto-r%C3%A1pido-por-API-Safra#top)
