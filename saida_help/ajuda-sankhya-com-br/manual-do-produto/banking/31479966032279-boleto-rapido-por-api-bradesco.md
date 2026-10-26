---
id: "31479966032279"
titulo: "Boleto rápido por API - Bradesco"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31479966032279-Boleto-r%C3%A1pido-por-API-Bradesco"
trilha: "Manual do Produto > Financeiro e Patrimônio > Sankhya Fintech > Banking"
atualizado_em: "2026-09-09T19:52:59Z"
rotulos: ["Configuração", "Boletos", "Financeiro", "Boleto Rápido API", "Como obter credenciais", "API", "API do Banco", "Boleto Rápido", "EDI automático", "Banco Bradesco", "Bradesco"]
---

# Boleto rápido por API - Bradesco

O [Boleto rápido API](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559) é uma solução do **Sankhya Fintech** que visa aumentar a eficiência operacional e a produtividade das empresas por meio da automação no processo de emissão e gestão de boletos bancários. Ao eliminar a necessidade de arquivos de remessa e retorno, essa solução simplifica e automatiza as operações financeiras de forma significativa.

Confira abaixo como credenciar uma conta do banco **Bradesco** no Boleto rápido.

| Credenciamento Bradesco |
| --- |
| [Configurações iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/31479966032279-Boleto-r%C3%A1pido-por-API-Bradesco#Configura%C3%A7%C3%B5esiniciais) |
| [Configurações de ações automáticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/31479966032279-Boleto-r%C3%A1pido-por-API-Bradesco#Configura%C3%A7%C3%B5esdea%C3%A7%C3%B5esautom%C3%A1ticas) |

---

## Configurações iniciais

Com o serviço devidamente contratado, acesse a tela Assistente de Melhores Práticas, navegue até o menu Configurações serviços Fintech, selecione a opção Boleto Rápido e clique em Iniciar.

### Seleção da Conta e Modalidade

Selecione a conta bancária e defina o tipo de serviço: Boleto Simples ou Boleto Híbrido (que inclui QR Code para pagamento via PIX).

![Imagem 1: Selecione a conta bancária e defina o tipo de serviço: Boleto Simples ou Boleto Híbrido (que inclui QR Code para…](https://ajuda.sankhya.com.br/hc/article_attachments/42092412747799)

### Dados da Conta Bancária

Preencha as informações solicitadas.

![Imagem 2: Preencha as informações solicitadas.](https://ajuda.sankhya.com.br/hc/article_attachments/42092412749207)

### Configuração de cobrança

![Imagem 3: Configuração de cobrança](https://ajuda.sankhya.com.br/hc/article_attachments/42092418634135)

####

#### **(1)** Configurar ações após o vencimento do título

Nesta etapa é possível definir regras para a permanência do boleto, negativação e protesto.

**(3)**Nessa opção, o campo **Permanência após o vencimento** indica se o boleto permanecerá ativo no banco após o vencimento: 

- se a opção**Seguir com a permanência padrão do convênio** for selecionada, a validade dos boletos respeitará o prazo acordado com a instituição bancária no momento da contratação dos serviços de emissão de boletos;
- já, escolhendo a opção**Configurar manualmente a permanência após o vencimento**, o prazo de permanência dos boletos após o vencimento deverá ser inserido no campo **Dias de permanência após o vencimento**.

**(3)**Na seção **Negativação**, especifique se o boleto será negativado após o vencimento. Caso opte pela negativação, informe o número de dias corridos após o vencimento no campo **Dias para negativação** para que a negativação ocorra automaticamente.

**(3)**Defina no campo **Dias para protesto** se o boleto será protestado após o vencimento. Se optar pelo protesto, informe o número de dias corridos após o vencimento para que o protesto ocorra automaticamente.

**Nota:** para as contas do Banco Bradesco não é possível negativar e protestar o título ao mesmo tempo.

#### **(1)** Configurar juros

![Imagem 4: (1) Configurar juros](https://ajuda.sankhya.com.br/hc/article_attachments/42092412751127)

**(3)**Determine os **Tipos de Juros**dentre as seguintes opções:

- **dispensar a cobrança de juros:** não será atribuído juros no boleto;
- **definir uma taxa diária (em porcentagem):** no registro do boleto será considerado um percentual diário para cobrança de juros. Com essa opção ativada, o campo **Valor percentual** será habilitado. Nele, informe o percentual de juros. Por exemplo, caso seja informado 1%, será cobrado uma taxa de juros de 1% ao mês em relação ao valor do título;
- **definir um valor fixo (R$) por dia de atraso:** no registro do boleto será considerado um valor diário em reais para cobrança de juros. Escolhendo essa opção, o campo **Valor em reais** será habilitado. Nele, preencha o valor dos juros. Por exemplo, caso seja informado R$ 1,00, será cobrado uma taxa de juros de R$ 1,00 ao dia.

**(3)**Defina no campo **Data dos juros**a partir de qual data serão cobrados os juros, dentre as seguintes alternativas:

- **usar data de vencimento:** a data de vencimento será considerada para cobrança de juros;
- **configurar quantidade de dias:** será possível configurar uma quantidade de dias considerando a data de vencimento como base para cobrança de juros. Por exemplo, caso seja informado um dia no campo, será usada a Data de Vencimento + 1, ou seja, os juros serão cobrados um dia a partir da data do vencimento.

#### **(1)** Configurar multa

![Imagem 5: (1) Configurar multa](https://ajuda.sankhya.com.br/hc/article_attachments/42092418634775)

**(3)**Configure também os**Tipos de Multa**, conforme as alternativas a seguir:

- **dispensar a cobrança de multa:** não será atribuído multa no boleto;
- **definir um percentual em relação ao valor do título:** ao registrar o boleto será definido uma porcentagem de multa sobre o valor do título. Ao selecionar essa a opção, o campo **Valor Percentual** será habilitado para informar o percentual de multa a ser aplicado. Por exemplo, se for definido 10%, a multa corresponderá a 10% do valor do título;
- **definir um valor fixo (R$):** no registro do boleto será considerado um valor fixo em reais para cobrança de multa. Com essa opção marcada, o campo **Valor em Reais** será habilitado para preencher um valor fixo de multa, independentemente do valor do título. Por exemplo, se for definido R$ 10,00, a multa aplicada será exatamente R$ 10,00, sem variação conforme o valor do boleto.

**(3)**Defina no campo **Data da Multa**a partir de qual data será cobrada a multa, dentre as seguintes alternativas:

- **usar data de vencimento:** a data de vencimento será considerada para cobrança de multa;
- **configurar quantidade de dias:** será possível configurar uma quantidade de dias considerando a data de vencimento como base para cobrança de multa. Por exemplo, caso seja informado um dia no campo, será usada a Data de Vencimento + 1, ou seja, a multa será cobrada um dia a partir da data do vencimento. Com essa opção marcada, o campo **Dias para multa** deverá ser preenchido com um valor que não seja negativo.

**Observação:** é obrigatório o preenchimento de todos os campos que forem habilitados. 

Ao concluir as configurações, os tópicos configurados corretamente serão marcados como finalizados, permitindo o avanço para a próxima etapa.

### Ações Automáticas

Configure os parâmetros para que os processos de baixa e conciliação ocorram de forma automática no ERP. O detalhamento completo dessas configurações está disponível no tópico Configurações de ações automáticas, mais abaixo neste artigo.

![Imagem 6: Configure os parâmetros para que os processos de baixa e conciliação ocorram de forma automática no ERP. O detalhamento…](https://ajuda.sankhya.com.br/hc/article_attachments/42092418635927)

---

### Credenciais

Baixe o certificado disponibilizado nesta etapa e acesse a documentação [Como obter credenciais do Banco Bradesc](https://ajuda.sankhya.com.br/hc/pt-br/articles/36551875605911)o para seguir o passo a passo, utilizando o certificado baixado quando solicitado. Com o Client ID e o Client Secret em mãos, insira-os nesta etapa e siga o credenciamento.

![Imagem 7: Baixe o certificado disponibilizado nesta etapa e acesse a documentação Como obter credenciais do Banco Bradesc o para…](https://ajuda.sankhya.com.br/hc/article_attachments/42092418636695)

### Resumo de Configuração

**Revise todos os dados. Se estiverem corretos, clique em "Instalar". Ao concluir com êxito, a conta exibirá o status CREDENCIADA.**

## Configurações de ações automáticas

Com o serviço API do Banco selecionado, poderão ser realizadas as configurações abaixo.

### **(1)** Baixa automática

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

**Nota:** a baixa e conciliação automáticas para contas do Banco Bradesco só devem seguir a opção **Realizar na data do crédito em conta** caso o prazo de recebimento seja 0 ou 1 dia, visto que o banco não retorna via API a data de crédito em conta.

###
