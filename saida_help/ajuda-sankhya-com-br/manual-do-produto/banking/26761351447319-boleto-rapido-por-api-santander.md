---
id: "26761351447319"
titulo: "Boleto Rápido por API - Santander"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26761351447319-Boleto-R%C3%A1pido-por-API-Santander"
trilha: "Manual do Produto > Financeiro e Patrimônio > Sankhya Fintech > Banking"
atualizado_em: "2026-08-10T19:05:34Z"
rotulos: ["Configuração", "Movimentação Financeira", "Boleto", "Financeiro", "Boleto Híbrido", "Boleto Simples", "API", "Configuração de cobrança", "Modalidade do serviço", "Credenciamento de Conta ", "Chave PIX", "Santander"]
---

# Boleto Rápido por API - Santander

O [Boleto rápido API](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559) é uma solução do **Sankhya Fintech** que visa aumentar a eficiência operacional e a produtividade das empresas por meio da automação no processo de emissão e gestão de boletos bancários. Ao eliminar a necessidade de arquivos de remessa e retorno, essa solução simplifica e automatiza as operações financeiras de forma significativa.

Confira abaixo como configurar uma conta do banco **Santander** no Boleto rápido.

| Credenciamento Santander |
| --- |
| [Configurações iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/26761351447319-Boleto-R%C3%A1pido-por-API-Santander#Configura%C3%A7%C3%B5esiniciais) |
| [Configurações de ações automáticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/26761351447319-Boleto-R%C3%A1pido-por-API-Santander#Configura%C3%A7%C3%B5esdea%C3%A7%C3%B5esautom%C3%A1ticas) |

---

![Imagem 1: Caso não tenha gerado suas credenciais, acesse o link de Como obter as credenciais do banco Santander para saber como…](https://ajuda.sankhya.com.br/hc/article_attachments/26761815180823) Caso não tenha gerado suas credenciais, acesse o link de [Como obter as credenciais do banco Santander](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069541531927) para saber como poderá gerar as suas credenciais de acesso.

---

## Configurações iniciais

Acesse o [**Assistente de Melhores Prática**](https://ajuda.sankhya.com.br/hc/pt-br/articles/26322304673943-Assistente-de-Melhores-Pr%C3%A1ticas)[**s**](https://ajuda.sankhya.com.br/hc/pt-br/articles/26322304673943-Assistente-de-Melhores-Pr%C3%A1ticas) e, em Configurações serviços Fintech › Boleto Rápido, na etapa "Selecionar conta", selecione a conta a ser credenciada. Clique em Avançar para iniciar a jornada de credenciamento. 

![Assistente de Melhores Práticas – Boleto Rápido, etapa Selecionar a conta para credenciar, com a lista de contas…](https://ajuda.sankhya.com.br/hc/article_attachments/42433377601175)

O credenciamento do Boleto rápido é composto por três etapas:

### ![Imagem 3: Modalidade do serviço](https://ajuda.sankhya.com.br/hc/article_attachments/26762263269655) Modalidade do serviço

Para escolher a modalidade do serviço, selecione o **Boleto simples** ou o **Boleto híbrido**, que é o boleto tradicional, acrescido de um QR code para pagamento por PIX.

**Importante:** para aderir ao Boleto híbrido é preciso abrir uma chave PIX junto ao banco e preparar o seu atual modelo de boleto para receber o QR code.

![Assistente de Melhores Práticas – Boleto Rápido, etapa Selecionar tipo de serviço, com as opções Boleto Simples e…](https://ajuda.sankhya.com.br/hc/article_attachments/42433377602199)

### ![Imagem 5: Configuração de cobrança](https://ajuda.sankhya.com.br/hc/article_attachments/26762238096023) Configuração de cobrança

Defina as regras de permanência do boleto após o vencimento, negativação ou protesto e insira as configurações de juros e multa. 

#### Configurar ações após o vencimento do título

- Informe no campo **Permanência após o vencimento** se o boleto permanecerá ativo no banco após o vencimento. Caso escolha a opção **Seguir com a permanência padrão do convênio** o tempo de permanência será configurado conforme negociado com o banco.
- Na seção **Protesto**, informe se o boleto será protestado após o vencimento. Em caso de protesto, informe a quantidade de dias para protesto e se a contabilização será em dias úteis ou corridos.

**Nota:** para as contas do banco Santander não é possível negativar um título

![Assistente de Melhores Práticas – Boleto Rápido, etapa Vencimento do Título, com as opções de permanência após o…](https://ajuda.sankhya.com.br/hc/article_attachments/42433377603223).

#### Configurar juros

- **Dispensar a cobrança de juros:** ao selecionar essa opção não será atribuído juros no boleto.
- **Definir uma taxa mensal (em porcentagem):** ao informar essa opção, no registro do boleto será considerado um percentual para cobrança de juros.

Com a opção Definir uma taxa mensal (em porcentagem) ativada, o campo **Valor percentual** será habilitado. Nele, informe o valor ou o percentual de juros. Por exemplo, caso seja informado 1%, será cobrado uma taxa de juros de 1% ao mês em relação ao valor do título.

![Assistente de Melhores Práticas – Boleto Rápido, etapa Juros, com as opções de dispensar, definir taxa diária ou…](https://ajuda.sankhya.com.br/hc/article_attachments/42433377604119)

#### Configurar multa

Configure também os **Tipos de Multa**, conforme as alternativas a seguir:

- **Dispensar a cobrança de multa:** ao selecionar essa opção não será atribuído multa no boleto.
- **Definir um percentual em relação ao valor do título:** nessa opção, ao registrar o boleto será definido uma porcentagem de multa sobre o valor do título.

Com a opção Definir uma taxa mensal (em porcentagem) definida, o campo Valor percentual será habilitado. Nele, informe o valor ou o percentual de juros. Por exemplo, caso seja informado 10%, será cobrado um valor relativo a 10% do valor do título como taxa de multa.

Defina no campo **Data da Multa** a partir de qual data será cobrada a multa, dentre as seguintes alternativas:

- **Usar data de vencimento:** ao selecionar essa opção, será considerada a data de vencimento para cobrança de multa.
- **Configurar quantidade de dias:** com essa opção, será possível configurar uma quantidade de dias considerando a data de vencimento como base para cobrança de multa. Por exemplo, caso seja informado 1 dia no campo, será usada a Data de Vencimento + 1, ou seja, a multa será cobrada 1 dia a partir da data do vencimento.

Se for selecionada a opção Configurar quantidade de dias, o campo **Dias para multa**, deverá ser preenchido com um valor que não seja negativo.

![Assistente de Melhores Práticas – Boleto Rápido, etapa Multa, com as opções de dispensar, definir percentual em relação…](https://ajuda.sankhya.com.br/hc/article_attachments/42433349017111)

Ao concluir o credenciamento, os tópicos configurados corretamente serão marcados como finalizados, permitindo o avanço para a próxima etapa.

### ![Imagem 9: Credenciamento de conta](https://ajuda.sankhya.com.br/hc/article_attachments/30966697516183) Credenciamento de conta

Forneça os dados da conta, como convênio, carteira e modalidade, além das credenciais geradas no portal Developers da instituição bancária correspondente.

![Assistente de Melhores Práticas – Boleto Rápido, etapa Dados da conta, com os campos de agência, conta, CNPJ, convênio,…](https://ajuda.sankhya.com.br/hc/article_attachments/42433377606295)

Informe no campo **Convênio** o número do convênio estabelecido com o banco.

Caso esteja credenciando o **Boleto Híbrido**, no campo **Tipo de Chave PIX**, insira o tipo de chave que está aberta junto ao banco, como e-mail, telefone, CNPJ, celular ou chave aleatória, além de copiar e colar a chave para o campo **Chave PIX**.

Com as credenciais geradas, informe o **Client ID** e **Client Secret**.

![Assistente de Melhores Práticas – Boleto Rápido, etapa Credenciais (via API), com os campos ClientID e Client Secret.](https://ajuda.sankhya.com.br/hc/article_attachments/42433349021079) 

Inseridas todas as informações, clique no botão Credenciar para concluir a configuração e validação dos dados informados. Caso seja concluída com sucesso, o sistema exibirá uma mensagem que confirmará a conclusão. Porém, caso seja encontrado algum dado incorreto, será apresentada a mensagem:

**"As credenciais inseridas apresentaram erro no teste de integração. Por favor, tente novamente."**

Nesse caso, reveja as informações inseridas e realize uma nova tentativa.

**Observação:** para ativar o Boleto híbrido Santander é necessário ter uma chave PIX cadastrada na conta.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/26761351447319-Boleto-R%C3%A1pido-por-API-Santander#top)

---

## Configurações de ações automáticas

Na etapa Ações Automáticas do Assistente de Melhores Práticas, poderão ser realizadas as seguintes configurações abaixo:

![Assistente de Melhores Práticas – Boleto Rápido, etapa Ações Automáticas, com os campos de baixa automática,…](https://ajuda.sankhya.com.br/hc/article_attachments/42433349028503)

### Baixa automática

Defina a **Baixa automática** conforme as alternativas: 

- não realizar;
- realizar na data de pagamento;
- realizar na data do crédito em conta.

Caso a opção seja diferente de Não realizar, a baixa automática será feita via API.

Pode-se verificar se o boleto foi baixado e conciliado automaticamente por meio dos campos:

- **histórico**: localizado na aba [Lançamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Lan%C3%A7amento) da tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela) para versões menores que 4.23;
- **baixa por API:** deverá ser ativado por meio da opção de configurações de formulário para versões 4.24 ou maiores.

Quando um boleto for baixado automaticamente, o campo receberá a seguinte descrição:

**"Baixado automaticamente pela API do Banco."**

Caso falte alguma configuração que impeça a API de realizar a baixa automática, aparecerá no Histórico do título na Movimentação Financeira:

**"Não foi possível realizar a baixa automática. Verifique triggers e processos de baixa."**

Já, o campo Baixa por API trará o tipo de erro que impediu a realização da baixa.

### Lançamento baixa boleto

O campo **Lançamento baixa boleto** refere-se ao tipo de lançamento bancário. Se esse campo estiver vazio na tela Contas, o código de lançamento bancário a ser utilizado será aquele especificado no campo **Lançamento bancário receitas**, na aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades) das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa).

### TOP baixa boleto

No campo **TOP Baixa boleto** informe uma TOP de lançamento ao título. Lembre-se que, esse campo deve ser preenchido para que a baixa automática seja efetuada.

### Conciliação automática

O campo **Conciliação automática** pode ser configurado apenas quando o campo Baixa Automática não estiver com a opção **Não realizar** selecionada. Nele, defina a forma da Conciliação Automática, conforme as opções: 

- não realizar;
- realizar na data de pagamento;
- realizar na data do crédito em conta.

**Nota:** a baixa e conciliação automáticas para contas do Banco Santander só devem seguir a opção Realizar na data do crédito em conta caso o prazo de recebimento seja 0 ou 1 dia, visto que o banco não retorna via API a data de crédito em conta.

### Tela Contas> aba Boleto/Duplicata

No campo **"Modelo Cobrança"**  busque e selecione:

- O modelo de boleto cadastrado na tela [Modelos de Nota Fiscal/Duplicatas/Boletos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913-Modelos-de-Nota-Fiscal-Duplicatas-Boleto-s-).
- Informe a **"Impressora"** que será utilizada para impressão do boleto.
- Determine o **"Tipo Impressora"** para emissão do documento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/26761351447319-Boleto-R%C3%A1pido-por-API-Santander#top)
