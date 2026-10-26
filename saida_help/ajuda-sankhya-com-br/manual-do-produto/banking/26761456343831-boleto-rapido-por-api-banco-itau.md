---
id: "26761456343831"
titulo: "Boleto Rápido por API banco Itaú"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26761456343831-Boleto-R%C3%A1pido-por-API-banco-Ita%C3%BA"
trilha: "Manual do Produto > Financeiro e Patrimônio > Sankhya Fintech > Banking"
atualizado_em: "2026-08-07T19:27:04Z"
rotulos: ["Configuração", "Boleto", "Financeiro", "API", "Banco Itáu", "API do Banco", "credenciais", "Boleto Rápido", "Itáu", "Itaú"]
---

# Boleto Rápido por API banco Itaú

O [Boleto rápido API](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559) é uma solução do **Sankhya Fintech** que visa aumentar a eficiência operacional e a produtividade das empresas por meio da automação no processo de emissão e gestão de boletos bancários. Ao eliminar a necessidade de arquivos de remessa e retorno, essa solução simplifica e automatiza as operações financeiras de forma significativa.

Confira abaixo como configurar uma conta do banco **Itaú** no Boleto rápido.

| Credenciamento Itaú |
| --- |
| [Configurações iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/26761456343831-Boleto-R%C3%A1pido-por-API-banco-Ita%C3%BA#Configura%C3%A7%C3%B5esiniciais) |
| [Configurações de ações automáticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/26761456343831-Boleto-R%C3%A1pido-por-API-banco-Ita%C3%BA#Configura%C3%A7%C3%B5esdea%C3%A7%C3%B5esautom%C3%A1ticas) |

---

![Imagem 1: Caso as credenciais ainda não tenham sido geradas, acesse o link Como obter as credenciais do boleto híbrido do banco…](https://ajuda.sankhya.com.br/hc/article_attachments/26761456315415) Caso as credenciais ainda não tenham sido geradas, acesse o link [Como obter as credenciais do boleto híbrido do banco Itaú](https://ajuda.sankhya.com.br/hc/pt-br/articles/21043102851223-Como-obter-credenciais-Boleto-H%C3%ADbrido-API-PIX-Banco-Ita%C3%BA) para obter as instruções de geração de credenciais de acesso.

---

## Configurações iniciais

Acesse o [**Assistente de Melhores Prática**](https://ajuda.sankhya.com.br/hc/pt-br/articles/26322304673943-Assistente-de-Melhores-Pr%C3%A1ticas)[**s**](https://ajuda.sankhya.com.br/hc/pt-br/articles/26322304673943-Assistente-de-Melhores-Pr%C3%A1ticas) e, em Configurações serviços Fintech › Boleto Rápido, na etapa "Selecionar conta", selecione a conta a ser credenciada. Clique em Avançar para iniciar a jornada de credenciamento. 

![Assistente de Melhores Práticas – Boleto Rápido, etapa Selecionar a conta para credenciar, com a lista de contas…](https://ajuda.sankhya.com.br/hc/article_attachments/42435205243287)

![Imagem 3: O cadastro da conta deverá respeitar as regras de inserção de informações:](https://ajuda.sankhya.com.br/hc/article_attachments/26761456315415) O cadastro da conta deverá respeitar as regras de inserção de informações:

- agência: sem dígito;
- conta: com dígito.

### ![Imagem 4: Modalidade do serviço](https://ajuda.sankhya.com.br/hc/article_attachments/42309680577943) Modalidade do serviço

Para escolher a Modalidade do serviço, selecione o **"Boleto simples"** ou o **"Boleto híbrido"**, que é o boleto tradicional, acrescido de um QRCode para pagamento por PIX.

**Importante:** para aderir ao Boleto híbrido é preciso preparar o seu atual modelo de boleto para receber o QR code.

![Assistente de Melhores Práticas – Boleto Rápido, etapa Selecionar tipo de serviço, com as opções Boleto Simples e…](https://ajuda.sankhya.com.br/hc/article_attachments/42435205244823)

### ![Imagem 6: Configuração de cobrança](https://ajuda.sankhya.com.br/hc/article_attachments/42309710709271) Configuração de cobrança

Defina as regras de permanência do boleto após o vencimento, negativação ou protesto e insira as configurações de juros e multa.

#### Configurar ações após o vencimento do título

- No campo **"Instrução de protesto"**, pode-se indicar se o título deve ou não ser protestado. Caso configure a opção **"Protestar",** no campo **"Dias para protesto"**, informe a quantidade de dias depois do vencimento do boleto para o protesto automático. No campo **"Contabilizar dia útil ou dias corridos"**, escolha entre a contabilização para dias úteis ou dias corridos.
- No campo **"Instrução de negativação"**, configure se o título deve ou não ser negativado. Se selecionada a opção **"Negativar",** do campo **"Dias para negativação"**, informe a quantidade de dias corridos depois do vencimento do boleto para a negativação automática.

**Nota:** o campo Dias para protesto deve receber valores entre 1 e 99 dias. O campo Dias para negativação deve receber valores entre 2 e 99 dias. 

**Nota:** para as contas do Banco Itaú não é possível negativar e protestar o título ao mesmo tempo.

**Observação:** atualmente não há retorno via API dos boletos que foram negativados ou protestados. Para acompanhar a execução, acesse o Bankline Itaú.

![Assistente de Melhores Práticas – Boleto Rápido, etapa Vencimento do Título, com as opções de permanência após o…](https://ajuda.sankhya.com.br/hc/article_attachments/42435177447447)

#### Configurar juros

- **Dispensar:** ao selecionar essa opção não será atribuído juros no boleto.
- **Definir um percentual diário (em porcentagem):** com essa opção configurada, será enviado no registro do boleto um percentual a ser cobrado por dia de atraso para cobrança de juros.
- **Definir um percentual mensal (em porcentagem):** por meio dessa opção, será enviado no registro do boleto um percentual mensal a ser cobrado por dia de atraso para cobrança de juros.
- **Definir um percentual anual (em porcentagem):** com essa opção indicada, será enviado no registro do boleto um percentual anual a ser cobrado por dia de atraso para cobrança de juros.
- **Definir um valor (R$) fixo por dia de atraso:** ao informar essa opção, no registro do boleto será considerado um valor fixo (em reais) diário por dia de atraso para a cobrança de juros.

Com a opção Definir uma taxa mensal (em porcentagem) selecione, o campo **"Valor percentual"** será habilitado. Nele, informe o valor ou o percentual de juros. Por exemplo, caso seja informado 1%, será cobrado uma taxa de juros de 1% ao mês em relação ao valor do título.

Com a opção Definir um valor (R$) fixo por dia definida, o campo **"Valor** **em reais"** será habilitado. Nele, informe o valor em reais que será cobrado por dia. Por exemplo, caso seja informado R$1,00, será cobrado uma taxa de juros de um real por dia, independente do valor do título.

Defina no campo **"Data dos Juros"** a partir de qual data será cobrado, através das seguintes alternativas:

- **Usar data de vencimento:** por meio desta, será considerada a data de vencimento para cobrança de multa.
- **Configurar quantidade de dias:** com essa opção, será possível configurar uma quantidade de dias considerando a data de vencimento como base. Por exemplo, caso seja informado 5 dias no campo, será usada a data de Vencimento + 5, ou seja, os juros serão cobrada 5 dias a partir da data do vencimento
- ![Assistente de Melhores Práticas – Boleto Rápido, etapa Juros, com as opções de dispensar cobrança, definir taxa diária…](https://ajuda.sankhya.com.br/hc/article_attachments/42435205246871)

#### Configurar multa

Configure também os **"Tipos de Multa"**, conforme as alternativas a seguir:

- **Dispensar a cobrança de multa:** ao selecionar essa opção não será atribuído multa no boleto.
- **Definir um percentual em relação ao valor do título:** nessa opção, ao registrar o boleto será definido uma porcentagem de multa sobre o valor do título.
- **Definir um valor (R$) fixo:** indicando essa opção, será definido um valor fixo para cobrança de multa.

Com a opção Definir uma taxa mensal (em porcentagem) selecionada, o campo Valor percentual será habilitado. Nele, informe o valor ou o percentual de juros. Por exemplo, caso seja informado 10%, será cobrado um valor relativo a 10% do valor do título como taxa de multa.

Com a opção Definir um valor (R$) fixo por dia definida, o campo Valor em reais será habilitado. Nele, informe o valor em reais que será cobrado por dia. Por exemplo, caso seja informado R$10,00, será cobrado uma taxa de multa de dez reais, independente do valor do título.

Defina no campo **"Data da Multa"** a partir de qual data será cobrada a multa, dentre as seguintes alternativas:

- **Usar data de vencimento:** ao selecionar essa opção, será considerada a data de vencimento para cobrança de multa.
- **Configurar quantidade de dias:** com essa opção, será possível configurar uma quantidade de dias considerando a data de vencimento como base para cobrança de multa. Por exemplo, caso seja informado 5 dias no campo, será usada a data de Vencimento + 5, ou seja, a multa será cobrada 5 dias a partir da data do vencimento.

Se for selecionada a opção Configurar quantidade de dias, o campo **"Dias para multa"**, deverá ser preenchido com um valor maior que zero e que não seja negativo.

**Observação:** é obrigatório preenchimento de todos os campos que forem habilitados. 

**Nota:** os campos **"Dias para juros"** e **"Dias para multa"** devem ser preenchidos com um valor maior que zero e que não seja negativo.

**Nota:** a instrução de juros e multa deverá resultar numa cobrança de juros e multa maior que R$ 0,01 ao dia. Ou seja, valores onde o cálculo de juros e multa resultam em um valor menor que R$ 0,01 são barrados pela API do Itaú e o boleto não é registrado.

![Assistente de Melhores Práticas – Boleto Rápido, etapa Multa, com as opções de dispensar, definir um percentual em…](https://ajuda.sankhya.com.br/hc/article_attachments/42435177449111)

Ao concluir o credenciamento, os tópicos configurados corretamente serão marcados como finalizados, permitindo o avanço para a próxima etapa.

### ![Imagem 10: Credenciamento de conta](https://ajuda.sankhya.com.br/hc/article_attachments/42309710710807) Credenciamento de conta

Forneça os dados da conta, como convênio, carteira e modalidade, além das credenciais geradas no portal Developers da instituição bancária correspondente.

![Assistente de Melhores Práticas – Boleto Rápido, etapa Dados da conta, com os campos de agência bancária, conta, CNPJ…](https://ajuda.sankhya.com.br/hc/article_attachments/42435177449751)

No campo **"Carteira"** informe o número da carteira da conta.

No campo **"CPF/CNPJ"** informe o número do CNPJ matriz da conta.

Após ter feito o processo de obtenção de credenciais pelo Bankline Itaú, clique em **"Sincronizar credenciais"** para habilitar o serviço. Com as credenciais sincronizadas, clique em **"Habilitar"** para concluir a configuração e validação dos dados informados. Caso seja concluída com sucesso, o sistema exibirá uma mensagem confirmando a conclusão.

Caso seja encontrado algum dado incorreto, será apresentada a mensagem:

**"As credenciais inseridas apresentaram erro no teste de integração. Por favor, tente novamente."**

Nesse caso, reveja as informações inseridas e realize uma nova tentativa.

**Observação:** para ativar o Boleto Rápido Itaú é necessário ter uma chave PIX cadastrada na conta e habilitá-la para o parceiro Sankhya Jiva Gestão de Negócios. O processo é válido tanto para a modalidade Simples, quanto para a Híbrida.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/26761456343831-Boleto-R%C3%A1pido-por-API-banco-Ita%C3%BA#top)

---

## Configurações de ações automáticas

Na etapa Ações Automáticas do Assistente de Melhores Práticas, poderão ser realizadas as seguintes configurações abaixo:

![Assistente de Melhores Práticas – Boleto Rápido, etapa Ações Automáticas, com os campos de baixa automática, lançamento…](https://ajuda.sankhya.com.br/hc/article_attachments/42435205249943)

### Baixa automática

Defina a **"Baixa automática"** conforme as alternativas: 

- Não realizar;
- Realizar na data de pagamento;
- Realizar na data do crédito em conta.

Caso a opção seja diferente de Não realizar, a baixa automática será feita via API.

Pode-se verificar se o boleto foi baixado e conciliado automaticamente por meio dos campos:

- **Histórico**: localizado na aba [Lançamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Lan%C3%A7amento) da tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela) para versões menores que 4.23;
- **Baixa por API:** deverá ser ativado por meio da opção de configurações de formulário para versões 4.24 ou maiores.

Quando um boleto for baixado automaticamente, o campo receberá a seguinte descrição:

**"Baixado automaticamente pela API do Banco."**

Caso falte alguma configuração que impeça a API de realizar a baixa automática, aparecerá no histórico do título na Movimentação Financeira:

**"Não foi possível realizar a baixa automática. Verifique triggers e processos de baixa."**

Já o campo **"Baixa por API"** trará o tipo de erro que impediu a realização da baixa.

### Lançamento baixa boleto

O campo **"Lançamento baixa boleto"** refere-se ao tipo de lançamento bancário. Se esse campo estiver vazio na tela Conta, o código de lançamento bancário a ser utilizado será aquele especificado no campo **"Lançamento bancário receitas"**, na aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades), das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa).

### TOP baixa boleto

No campo **"TOP Baixa boleto"** informe uma TOP de lançamento ao título. Lembre-se que, esse campo deve ser preenchido para que a baixa automática seja efetuada.

### Conciliação automática

O campo **"Conciliação automática"** pode ser configurado apenas quando o campo Baixa Automática não estiver com a opção **"Não realizar"** selecionada. Nele, defina a forma da Conciliação Automática, conforme as opções: 

- Não realizar;
- Realizar na data de pagamento;
- Realizar na data do crédito em conta.

**Nota:** a baixa e conciliação automáticas para contas do Banco Itaú só devem seguir a opção Realizar na data do crédito em conta caso o prazo de recebimento seja 0 ou 1 dia, visto que o banco não retorna via API a data de crédito em conta.

### Na tela "Contas", aba Boleto/Duplicata

Por meio do campo **"Modelo Cobrança"** busque e selecione o modelo de boleto cadastrado na tela [Modelos de Nota Fiscal/Duplicatas/Boletos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913-Modelos-de-Nota-Fiscal-Duplicatas-Boleto-s-).

Informe a **"Impressora"** que será utilizada para impressão do boleto.

Determine o **"Tipo Impressora"** para emissão do documento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/26761456343831-Boleto-R%C3%A1pido-por-API-banco-Ita%C3%BA#top)
