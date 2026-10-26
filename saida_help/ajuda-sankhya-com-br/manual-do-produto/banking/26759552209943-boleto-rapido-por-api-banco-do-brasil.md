---
id: "26759552209943"
titulo: "Boleto Rápido por API Banco do Brasil"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26759552209943-Boleto-R%C3%A1pido-por-API-Banco-do-Brasil"
trilha: "Manual do Produto > Financeiro e Patrimônio > Sankhya Fintech > Banking"
atualizado_em: "2026-08-10T19:05:27Z"
rotulos: ["Configuração", "Boleto", "Financeiro", "Boleto Híbrido", "Banco do Brasil", "Boleto Simples", "API", "Credenciamento de conta", "Configuração de cobrança", "Modalidade do serviço"]
---

# Boleto Rápido por API Banco do Brasil

O [**Boleto rápido AP**I](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559) é uma solução do **Sankhya Fintech** que visa aumentar a eficiência operacional e a produtividade das empresas por meio da automação no processo de emissão e gestão de boletos bancários. Ao eliminar a necessidade de arquivos de remessa e retorno, essa solução simplifica e automatiza as operações financeiras de forma significativa.

Confira abaixo como configurar uma conta do banco **do Brasil** no Boleto rápido.

| Credenciamento banco do Brasil |
| --- |
| [Configurações iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/26759552209943-Boleto-R%C3%A1pido-por-API-Banco-do-Brasil#Configura%C3%A7%C3%B5esiniciais) |
| [Configurações de ações automáticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/26759552209943-Boleto-R%C3%A1pido-por-API-Banco-do-Brasil#Configura%C3%A7%C3%B5esdea%C3%A7%C3%B5esautom%C3%A1ticas) |

---

![Imagem 1: Caso não tenha gerado suas credenciais, acesse o link Como obter as credenciais do banco do Brasil para instruções…](https://ajuda.sankhya.com.br/hc/article_attachments/26759751668503) Caso não tenha gerado suas credenciais, acesse o link [Como obter as credenciais do banco do Brasil](https://ajuda.sankhya.com.br/hc/pt-br/articles/21042285386391) para instruções detalhadas sobre como criar suas credenciais de acesso.

---

## Configurações iniciais

Acesse o [**Assistente de Melhores Prática**](https://ajuda.sankhya.com.br/hc/pt-br/articles/26322304673943-Assistente-de-Melhores-Pr%C3%A1ticas)[**s**](https://ajuda.sankhya.com.br/hc/pt-br/articles/26322304673943-Assistente-de-Melhores-Pr%C3%A1ticas) e, em Configurações serviços Fintech › Boleto Rápido, na etapa "Selecionar conta", selecione a conta a ser credenciada. Clique em Avançar para iniciar a jornada de credenciamento. 

![Assistente de Melhores Práticas – Boleto Rápido, etapa Selecionar a conta para credenciar, com a lista de contas…](https://ajuda.sankhya.com.br/hc/article_attachments/42431720409367)

O credenciamento do Boleto Rápido é composto por três etapas:

### ![Imagem 3: Modalidade do serviço](https://ajuda.sankhya.com.br/hc/article_attachments/42309650842007) Modalidade do serviço

Para escolher a Modalidade do serviço, selecione o **"Boleto simples"** ou o **"Boleto híbrido"**, que é o boleto tradicional, acrescido de um QRCode para pagamento por PIX.

**Importante:** para aderir ao Boleto híbrido é preciso abrir uma chave pix junto à instituição bancária e preparar o seu atual modelo de boleto para receber o QR Code.

![Assistente de Melhores Práticas – Boleto Rápido, etapa Selecionar tipo de serviço, com as opções Boleto Simples e…](https://ajuda.sankhya.com.br/hc/article_attachments/42431744522519)

### ![Imagem 5: Configuração de cobrança](https://ajuda.sankhya.com.br/hc/article_attachments/42309644872471) Configuração de cobrança

Defina as regras de permanência do boleto após o vencimento, negativação ou protesto e insira as configurações de juros e multa. 

#### Configurar ações após o vencimento do título:

- Nessa etapa, o campo **Permanência após o vencimento** indica se o boleto permanecerá ativo no banco após o vencimento: se a opção **Seguir com a permanência padrão do convênio** for selecionada, a validade dos boletos respeitará o prazo acordado com a instituição bancária no momento da contratação dos serviços de emissão de boletos; já, escolhendo a opção **Configurar manualmente a permanência após o vencimento**, o prazo deverá ser inserido no campo **Dias de permanência após o vencimento**.
- ![Assistente de Melhores Práticas – Boleto Rápido, etapa Vencimento do Título, com as opções de permanência, negativação…](https://ajuda.sankhya.com.br/hc/article_attachments/42459470379543)
- Na seção **"Negativação"**, especifique se o boleto será negativado após o vencimento. Caso opte pela negativação, informe o número de dias corridos após o vencimento no campo **"Dias para negativação"** para que a negativação ocorra automaticamente. No campo **"Órgão Negativador"**, escolha entre as opções **"Serasa"** ou **"Quod"**.
- No campo **"Dias para protesto"**, defina se o boleto será protestado após o vencimento. Em caso afirmativo, especifique o número de dias para protesto: de 3 a 5 dias para dias úteis, ou 6 a 29, 35, 40 ou 45 dias para considerar dias corridos.

**Nota:** para as contas do Banco do Brasil não é possível negativar e protestar o título ao mesmo tempo.

#### Configurar juros:

- ![Assistente de Melhores Práticas – Boleto Rápido, etapa Juros, com as opções de tipo de juros para o Banco do Brasil.](https://ajuda.sankhya.com.br/hc/article_attachments/42459454376599)
- **Dispensar a cobrança de juros:** ao selecionar essa opção não será atribuído juros no boleto.
- **Definir uma taxa diária (em porcentagem):** ao informar essa opção, no registro do boleto será considerado um percentual para cobrança de juros.
- **Definir um valor (R$) fixo por dia:** com essa opção indicada, será enviado no registro do boleto um valor fixo (em reais) por dia de atraso para cobrança de juros.

Com a opção Definir uma taxa diária (em porcentagem) ativada, o campo **"Valor percentual"** será habilitado. Nele, informe o valor ou o percentual de juros. Por exemplo, caso seja informado 1%, será cobrado uma taxa de juros de 1% (em relação ao valor do título) ao dia.

Ao selecionar a opção Definir um valor (R$) fixo por dia, o campo **"Valor em reais"** será habilitado. Nele, informe o valor em reais que será cobrado por dia. Por exemplo, caso seja informado R$1,00, será cobrado uma taxa de juros de um real por dia, independente do valor do título.

#### Configurar multa:

![Assistente de Melhores Práticas – Boleto Rápido, etapa Multa, com as opções de tipo de multa para o Banco do Brasil.](https://ajuda.sankhya.com.br/hc/article_attachments/42459470390679)

Configure também os **"Tipos de Multa"**, conforme as alternativas a seguir:

- **Dispensar a cobrança de multa:** ao selecionar essa opção não será atribuído multa no boleto.
- **Definir um percentual em relação ao valor do título:** nessa opção, ao registrar o boleto será definido uma porcentagem de multa sobre o valor do título.
- **Definir um valor (R$) fixo:** indicando essa opção, será definido um valor fixo para cobrança de multa.

Com a opção Definir uma taxa mensal (em porcentagem) selecionada, o campo Valor percentual será habilitado. Nele, informe o valor ou o percentual de juros. Por exemplo, caso seja informado 10%, será cobrado um valor relativo a 10% do valor do título como taxa de multa.

Com a opção Definir um valor (R$) fixo por dia definida, o campo Valor em reais será habilitado. Nele, informe o valor em reais que será cobrado por dia. Por exemplo, caso seja informado R$10,00, será cobrado uma taxa de multa de dez reais, independente do valor do título.

Defina no campo **"Data da Multa"** a partir de qual data será cobrada a multa, dentre as seguintes alternativas:

- **Usar data de vencimento:** ao selecionar essa opção, será considerada a data de vencimento para cobrança de multa.
- **Configurar quantidade de dias:** com essa opção, será possível configurar uma quantidade de dias considerando a data de vencimento como base para cobrança de multa. Por exemplo, caso seja informado 5 dias no campo, será usada a data de Vencimento + 5, ou seja, a multa será cobrada 5 dias a partir da data do vencimento.

Se for selecionada a opção Configurar quantidade de dias, o campo **"Dias para multa"**, deverá ser preenchido com um valor maior que zero e que não seja negativo.

**Observação:** é obrigatório preenchimento de todos os campos que forem habilitados. 

Ao concluir o credenciamento, os tópicos configurados corretamente serão marcados como finalizados, permitindo o avanço para a próxima etapa.

### ![Imagem 9: Credenciamento de conta](https://ajuda.sankhya.com.br/hc/article_attachments/42309650843415) Credenciamento de conta

Forneça os dados da conta, como convênio, carteira e modalidade, além das credenciais geradas no portal Developers da instituição bancária correspondente.

![Assistente de Melhores Práticas – Boleto Rápido, etapa Dados da conta, com os campos de agência, conta, CNPJ, convênio,…](https://ajuda.sankhya.com.br/hc/article_attachments/42431720411287)

No campo **"Carteira"** informe o número da carteira do convênio de cobrança.

Preencha o campo **"Variação"** com o número da variação da carteira do convênio de cobrança. Pode-se informar um valor com até 3 dígitos.

Informe no campo **"Convênio"** o número do convênio estabelecido com o Banco.

É importante configurar um número de Convênio distinto para cada conta bancária. Caso seja informado um número de Convênio já utilizado em outra conta configurada com a API do Banco, será apresentada a mensagem:

**"O Convênio informado [xxxx] já está sendo usado para outra conta bancária."**

Por meio do campo **"Modalidade"**, será identificada a característica dos boletos dentro das modalidades de cobrança existentes no Banco. Este campo poderá ser definido com uma das seguintes alternativas:

- **Simples:** para a cobrança de duplicatas, notas promissórias, recibos e outros documentos;
- **Vinculada:** para a cobrança de duplicatas entregues ao Banco em garantia de operação de crédito ou como mecanismo de auto liquidez.

**Nota:** segundo as regras de negócio do Banco do Brasil, para a conta do tipo Vinculada, os boletos são dados como garantia ao banco e, por isso, não será permitido realizar alterações e cancelamento via API após sua emissão. Para estes processos, o banco direciona que sejam feitos diretamente pelo Internet Banking.

Com as credenciais geradas em mãos, informe o **"Client ID"** e **"Client Secret".**

**![Assistente de Melhores Práticas – Boleto Rápido, etapa Credenciais (via API), com os campos ClientID e Client Secret.](https://ajuda.sankhya.com.br/hc/article_attachments/42431720412183)t"**.  

Clique em **"Instalar"** para concluir a configuração e validação dos dados informados. Caso seja concluída com sucesso, o sistema exibirá uma mensagem confirmando a conclusão.

![Assistente de Melhores Práticas – Boleto Rápido, etapa Informações para finalização, com o resumo dos dados da conta e…](https://ajuda.sankhya.com.br/hc/article_attachments/42431720413079)

 Caso seja encontrado algum dado incorreto, será apresentada a mensagem:

**"As credenciais inseridas apresentaram erro no teste de integração. Por favor, tente novamente."**

Nesse caso, corrija as informações inseridas e realize uma nova tentativa. 

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/26759552209943-Boleto-R%C3%A1pido-por-API-Banco-do-Brasil#top)

---

## Configurações de ações automáticas

Na etapa Ações Automáticas do Assistente de Melhores Práticas, poderão ser realizadas as seguintes configurações abaixo:

![Assistente de Melhores Práticas – Boleto Rápido, etapa Ações Automáticas, com os campos de baixa automática,…](https://ajuda.sankhya.com.br/hc/article_attachments/42431744525079)

### Baixa automática

Defina a **"Baixa automática"** conforme as alternativas: 

- Não realizar;
- Realizar na data de pagamento;
- Realizar na data do crédito em conta.

Caso a opção seja diferente de Não realizar, a baixa automática será feita via API.

Pode-se verificar se o boleto foi baixado e conciliado automaticamente por meio dos campos:

- **Histórico**: localizado na aba [Lançamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Lan%C3%A7amento) da tela [Movimentação financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela) para versões menores que 4.23;
- **Baixa por API:** deverá ser ativado por meio da opção de configurações de formulário para versões 4.24 ou maiores.

Quando um boleto for baixado automaticamente, o campo receberá a seguinte descrição:

**"Baixado automaticamente pela API do Banco."**

Caso falte alguma configuração que impeça a API de realizar a baixa automática, aparecerá no Histórico do título na Movimentação Financeira:

**"Não foi possível realizar a baixa automática. Verifique triggers e processos de baixa."**

Já o campo Baixa por API trará o tipo de erro que impediu a realização da baixa.

### Lançamento baixa boleto

O campo **"Lançamento baixa boleto"** refere-se ao tipo de lançamento bancário. Se esse campo estiver vazio na tela Conta, o código de lançamento bancário a ser utilizado será aquele especificado no campo **"Lançamento bancário receitas"**, na aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades), das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa).

### TOP baixa boleto

No campo **"TOP Baixa boleto"** informe uma TOP de lançamento ao título. Lembre-se que, esse campo deve ser preenchido para que a baixa automática seja efetuada.

### Conciliação automática

O campo **"Conciliação automática"** pode ser configurado apenas quando o campo Baixa Automática não estiver com a opção **"Não realizar"** selecionada. Nele, defina a forma da Conciliação Automática, conforme as opções: 

- Não realizar;
- Realizar na data de pagamento;
- Realizar na data do crédito em conta.

### Tela Contas> aba Boleto/Duplicata

No campo **"Modelo Cobrança"** busque e selecione:

- O modelo de boleto cadastrado na tela [Modelos de Nota Fiscal/Duplicatas/Boletos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913-Modelos-de-Nota-Fiscal-Duplicatas-Boleto-s-).
- Informe a **"Impressora"** que será utilizada para impressão do boleto.
- Determine o **"Tipo Impressora"** para emissão do documento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/26759552209943-Boleto-R%C3%A1pido-por-API-Banco-do-Brasil#top)
