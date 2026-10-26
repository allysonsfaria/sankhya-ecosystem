---
id: "30709420233751"
titulo: "Boleto rápido por API - Sicoob"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30709420233751-Boleto-r%C3%A1pido-por-API-Sicoob"
trilha: "Manual do Produto > Financeiro e Patrimônio > Sankhya Fintech > Banking"
atualizado_em: "2026-08-07T19:41:21Z"
rotulos: ["Configuração", "Boleto", "Financeiro", "Boleto Rápido API", "Como obter credenciais", "API", "API do Banco", "Boleto Rápido", "Banco Sicoob", "Sicoob"]
---

# Boleto rápido por API - Sicoob

O [Boleto rápido API](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559) é uma solução do **Sankhya Fintech** que visa aumentar a eficiência operacional e a produtividade das empresas por meio da automação no processo de emissão e gestão de boletos bancários. Ao eliminar a necessidade de arquivos de remessa e retorno, essa solução simplifica e automatiza as operações financeiras de forma significativa.

Confira abaixo como credenciar uma conta do banco **Sicoob** no Boleto rápido.

| Credenciamento Sicoob |
| --- |
| [Configurações iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/30709420233751-Boleto-r%C3%A1pido-por-API-Sicoob#Configura%C3%A7%C3%B5esiniciais) |
| [Configurações de ações automáticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/30709420233751-Boleto-r%C3%A1pido-por-API-Sicoob#Configura%C3%A7%C3%B5esdea%C3%A7%C3%B5esautom%C3%A1ticas) |

---

![Imagem 1: Caso não tenha gerado suas credenciais, acesse o link Como obter as credenciais do banco Sicoob para obter instruções…](https://ajuda.sankhya.com.br/hc/article_attachments/30709420205719) Caso não tenha gerado suas credenciais, acesse o link [Como obter as credenciais do banco Sicoob](https://ajuda.sankhya.com.br/hc/pt-br/articles/30820232298007) para obter instruções detalhadas sobre como criar suas credenciais de acesso.

---

## Configurações iniciais

Acesse o [**Assistente de Melhores Prática**](https://ajuda.sankhya.com.br/hc/pt-br/articles/26322304673943-Assistente-de-Melhores-Pr%C3%A1ticas)[**s**](https://ajuda.sankhya.com.br/hc/pt-br/articles/26322304673943-Assistente-de-Melhores-Pr%C3%A1ticas) e, em Configurações serviços Fintech › Boleto Rápido, na etapa "Selecionar conta", selecione a conta a ser credenciada. Clique em Avançar para iniciar a jornada de credenciamento. 

![Assistente de Melhores Práticas – Boleto Rápido, etapa Selecionar a conta para credenciar, com a lista de contas…](https://ajuda.sankhya.com.br/hc/article_attachments/42439226691095)

O credenciamento do Boleto rápido é composto por três etapas:

### ![Imagem 3: Modalidade do serviço](https://ajuda.sankhya.com.br/hc/article_attachments/42309645322263) Modalidade do serviço

Para escolher a modalidade do serviço, selecione o **Boleto simples** ou o **Boleto híbrido**, que é o boleto tradicional, acrescido de um QR code para pagamento por PIX.

**Importante:** para aderir ao Boleto híbrido é preciso ter uma chave PIX aleatória junto à instituição bancária e preparar o seu atual modelo de boleto para receber o QR code. Em caso de dúvida, chame o gerente de relacionamento responsável por sua conta.

![Assistente de Melhores Práticas – Boleto Rápido, etapa Selecionar tipo de serviço, com as opções Boleto Simples e…](https://ajuda.sankhya.com.br/hc/article_attachments/42439194234135)

### ![Imagem 5: Configuração de cobrança](https://ajuda.sankhya.com.br/hc/article_attachments/42309645322903) Configuração de cobrança

####

#### **(1)** Configurar ações após o vencimento do título

Nesta etapa é possível definir regras para a permanência do boleto, negativação e protesto.

**(3)**Nessa opção, o campo **Permanência após o vencimento** indica se o boleto permanecerá ativo no banco após o vencimento: 

- se a opção **Seguir com a permanência padrão do convênio** for selecionada, a validade dos boletos respeitará o prazo acordado com a instituição bancária no momento da contratação dos serviços de emissão de boletos;
- já, escolhendo a opção **Configurar manualmente a permanência após o vencimento**, o prazo de permanência dos boletos após o vencimento deverá ser inserido no campo **Dias de permanência após o vencimento**.

**(3)**Na seção **Negativação**, especifique se o boleto será negativado após o vencimento. Caso opte pela negativação, informe o número de dias corridos após o vencimento no campo **Dias para negativação** para que a negativação ocorra automaticamente.

**(3)**Defina no campo **Dias para protesto** se o boleto será protestado após o vencimento. Se optar pelo protesto, informe o número de dias corridos após o vencimento para que o protesto ocorra automaticamente.

**Nota:** para as contas do Banco Sicoob não é possível negativar e protestar o título ao mesmo tempo.

![Assistente de Melhores Práticas – Boleto Rápido, etapa Vencimento do Título, com as opções de permanência, negativação…](https://ajuda.sankhya.com.br/hc/article_attachments/42439194235287)

#### **(1)** Configurar juros

**(3)**Determine os **Tipos de Juros** dentre as seguintes opções:

- **dispensar a cobrança de juros:** não será atribuído juros no boleto;
- **definir uma taxa diária (em porcentagem):** no registro do boleto será considerado um percentual diário para cobrança de juros. Com essa opção ativada, o campo **Valor percentual** será habilitado. Nele, informe o percentual de juros. Por exemplo, caso seja informado 1%, será cobrado uma taxa de juros de 1% ao mês em relação ao valor do título;
- **definir um valor fixo (R$) por dia de atraso:** no registro do boleto será considerado um valor diário em reais para cobrança de juros. Escolhendo essa opção, o campo **Valor em reais** será habilitado. Nele, preencha o valor dos juros. Por exemplo, caso seja informado R$ 1,00, será cobrado uma taxa de juros de R$ 1,00 ao dia.

**(3)**Defina no campo **Data dos juros** a partir de qual data serão cobrados os juros, dentre as seguintes alternativas:

- **usar data de vencimento:** a data de vencimento será considerada para cobrança de juros;
- **configurar quantidade de dias:** será possível configurar uma quantidade de dias considerando a data de vencimento como base para cobrança de juros. Por exemplo, caso seja informado um dia no campo, será usada a Data de Vencimento + 1, ou seja, os juros serão cobrados um dia a partir da data do vencimento.
- ![Assistente de Melhores Práticas – Boleto Rápido, etapa Juros, com as opções de dispensa, taxa diária percentual e valor…](https://ajuda.sankhya.com.br/hc/article_attachments/42439226695319)

#### **(1)** Configurar multa

**(3)**Configure também os **Tipos de Multa**, conforme as alternativas a seguir:

- **dispensar a cobrança de multa:** não será atribuído multa no boleto;
- **definir um percentual em relação ao valor do título:** ao registrar o boleto será definido uma porcentagem de multa sobre o valor do título. Ao selecionar essa a opção, o campo **Valor Percentual** será habilitado para informar o percentual de multa a ser aplicado. Por exemplo, se for definido 10%, a multa corresponderá a 10% do valor do título;
- **definir um valor fixo (R$):** no registro do boleto será considerado um valor fixo em reais para cobrança de multa. Com essa opção marcada, o campo **Valor em Reais** será habilitado para preencher um valor fixo de multa, independentemente do valor do título. Por exemplo, se for definido R$ 10,00, a multa aplicada será exatamente R$ 10,00, sem variação conforme o valor do boleto.

**(3)**Defina no campo **Data da Multa** a partir de qual data será cobrada a multa, dentre as seguintes alternativas:

- **usar data de vencimento:** a data de vencimento será considerada para cobrança de multa;
- **configurar quantidade de dias:** será possível configurar uma quantidade de dias considerando a data de vencimento como base para cobrança de multa. Por exemplo, caso seja informado um dia no campo, será usada a Data de Vencimento + 1, ou seja, a multa será cobrada um dia a partir da data do vencimento. Com essa opção marcada, o campo **Dias para multa** deverá ser preenchido com um valor que não seja negativo.
- ![Assistente de Melhores Práticas – Boleto Rápido, etapa Multa, com as opções de dispensa, percentual e valor fixo.](https://ajuda.sankhya.com.br/hc/article_attachments/42439194236695)

**Observação:** é obrigatório o preenchimento de todos os campos que forem habilitados. 

Ao concluir o credenciamento, os tópicos configurados corretamente serão marcados como finalizados, permitindo o avanço para a próxima etapa.

#### ![Imagem 9: Credenciamento de conta](https://ajuda.sankhya.com.br/hc/article_attachments/42309651231511) Credenciamento de conta

Nesta etapa forneça os dados da conta:

- agência bancária com dígito;
- conta-corrente com dígito;
- CNPJ da conta-corrente;
- código do beneficiário;
- último boleto emitido pela conta;
- chave PIX (exclusivo para boleto híbrido);
- ![Assistente de Melhores Práticas – Boleto Rápido, etapa Dados da conta, com os campos de agência, conta, CNPJ, último…](https://ajuda.sankhya.com.br/hc/article_attachments/42439194238103)
- credenciais: client\_id.
- ![Assistente de Melhores Práticas – Boleto Rápido, etapa Credenciais (via API), com o campo ClientID do Sicoob.](https://ajuda.sankhya.com.br/hc/article_attachments/42439194238871)

Inseridas todas as informações, clique no botão **Credenciar** para concluir a configuração e validação dos dados informados. Finalizada com sucesso, o sistema exibirá uma mensagem que confirmará a conclusão. Porém, caso seja encontrado algum dado incorreto, será apresentada a mensagem:

**"As credenciais inseridas apresentaram erro no teste de integração. Por favor, tente novamente."**

Nesse caso, reveja as informações inseridas e realize uma nova tentativa.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/30709420233751-Boleto-r%C3%A1pido-por-API-Sicoob#top)

---

## Configurações de ações automáticas

Na etapa Ações Automáticas do Assistente de Melhores Práticas, poderão ser realizadas as seguintes configurações abaixo:

### **(1)** Baixa automática

Determine se a **Baixa automática** será feita via API, conforme as alternativas: 

- não realizar;
- realizar na data de pagamento;
- realizar na data do crédito em conta.

Pode-se verificar se o boleto foi baixado e conciliado automaticamente por meio dos campos:

- **histórico**: localizado na aba [Lançamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Lan%C3%A7amento) da tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela) para versões menores que 4.23;
- **baixa por API:** deverá ser ativado por meio da opção de configurações de formulário para versões 4.24 ou maiores.

Quando um boleto for baixado automaticamente, o campo receberá a seguinte descrição:

**"Baixado automaticamente pela API do Banco."**

Caso falte alguma configuração que impeça a API de realizar a baixa automática, aparecerá no Histórico do título na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753):

**"Não foi possível realizar a baixa automática. Verifique triggers e processos de baixa."**

Já, o campo **Baixa por API** trará o tipo de erro que impediu a realização da baixa.

### **(1)** Lançamento baixa boleto

O campo **Lançamento baixa boleto** refere-se ao tipo de lançamento bancário. Se esse campo estiver vazio na tela [Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113), o código de lançamento bancário a ser utilizado será aquele especificado no campo **Lançamento bancário receitas**, na aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades) das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa).

### **(1)** TOP baixa boleto

No campo **TOP Baixa boleto** informe uma TOP de lançamento ao título. Lembre-se que, esse campo deve ser preenchido para que a baixa automática seja efetuada.

### **(1)** Conciliação automática

O campo **Conciliação automática** pode ser configurado apenas quando o campo **Baixa Automática** não estiver com a opção **Não realizar** selecionada. Nele, defina a forma da Conciliação automática, conforme as opções: 

- não realizar;
- realizar na data de pagamento;
- realizar na data do crédito em conta.

**Nota:** a baixa e conciliação automáticas para contas do Banco Sicoob só devem seguir a opção **Realizar na data do crédito em conta** caso o prazo de recebimento seja 0 ou 1 dia, visto que o banco não retorna via API a data de crédito em conta.

![Assistente de Melhores Práticas – Boleto Rápido, etapa Ações Automáticas, com os campos de baixa automática, lançamento…](https://ajuda.sankhya.com.br/hc/article_attachments/42439194242199)

### **(1)** Na tela "Contas", aba Boleto/Duplicata

Por meio do campo **Modelo Cobrança** busque e selecione o modelo de boleto cadastrado na tela [Modelos de Nota Fiscal/Duplicatas/Boletos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913-Modelos-de-Nota-Fiscal-Duplicatas-Boleto-s-).

Defina a impressora que será utilizada para emissão do documento.

### **(1)** Pontos de atenção na integração Sicoob

Ao utilizar o **Boleto Rápido Sicoob**, é importante considerar que o Sicoob **não** informa o canal de pagamento dos boletos, o que impossibilita a distinção entre pagamentos feitos via linha digitável e QR code.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/30709420233751-Boleto-r%C3%A1pido-por-API-Sicoob#top)
