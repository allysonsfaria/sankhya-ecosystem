---
id: "40220880300951"
titulo: "Cotação de Frete - TMS Transportador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40220880300951-Cota%C3%A7%C3%A3o-de-Frete-TMS-Transportador"
trilha: "Sankhya Official Pack - SOP > TMS"
atualizado_em: "2026-07-22T13:27:28Z"
rotulos: ["Configuração", "Cotação", "Email", "Transporte", "TMS", "Cotação de Frete", "Configurações TMS", "Cálculo do frete", "Esqueleto Oracle", "Esqueleto SQL Server", "Procedure customizada", "Pedido de Transporte"]
---

# Cotação de Frete - TMS Transportador

A tela ''**Cotação de Frete''** (Logística » TMS » Rotinas » Cotação Frete) permite simular rapidamente o valor de um frete entre dois pontos (origem e destino), gerar automaticamente um pedido de transporte e enviar a cotação por e-mail para o cliente, tudo sem sair da tela.

É indicada para equipes comerciais e operacionais que precisam responder cotações com agilidade, reaproveitando dados de um pedido modelo já cadastrado e a regra de cálculo de frete específica da empresa.

### Principais funcionalidades da tela

- **Calcular o valor** de um frete informando origem, destino, peso, volume e valor da mercadoria.
- **Gerar Pedido** de transporte automaticamente com base na cotação simulada.
- **Enviar Email** com o resumo da cotação para o cliente, usando um modelo de mensagem pré-cadastrado.
- **Consultar o histórico** de pedidos gerados pela tela e abrir cada um deles com um duplo clique.

###

### Pré-requisitos

Para garantir o funcionamento completo da tela, realize previamente três configurações essenciais. Essa etapa é normalmente executada pelo consultor de implantação ou pela equipe de TI.

#### 1. Configure o pedido modelo e os e-mails

**(1)** Acesse a tela **''Configurações TMS''** (Logística » TMS » Configurações TMS) e preencha os seguintes campos:

| Campo (na tela de configuração) | O que informar | Quando é usado |
| --- | --- | --- |
| **''Nro Pedido Modelo''** | Número de um Pedido de Transporte já existente, que servirá como “molde”. Deve possuir pelo menos um roteiro cadastrado. | Botão **Gerar Pedido** |
| **''Modelo de Assunto do Email''** | Texto que será utilizado como assunto do e-mail enviado ao cliente. | Botão **Enviar Email** |
| **''Modelo de Email''** | Texto do corpo do e-mail. Pode conter variáveis (placeholders), que serão substituídas automaticamente pelos dados da cotação no momento do envio. | Botão **Enviar Email** |

| Caso o campo “Nro Pedido Modelo” não esteja preenchido, o sistema exibirá a seguinte mensagem ao clicar em **“Gerar Pedido”**: **"Para gerar o pedido, é necessário configurar previamente o 'Nro Pedido Modelo' na tela de configuração do TMS."** |
| --- |

#### Variáveis disponíveis para uso no Modelo de E-mail

Utilize as variáveis abaixo para que sejam substituídas automaticamente no momento da montagem do e-mail:

| Variável | Substituída por |
| --- | --- |
| **${nl}** | Quebra de linha |
| **{PARCEIRO\_ORIGEM}** | Razão social do parceiro de origem |
| **{PARCEIRO\_DESTINO}** | Razão social do parceiro de destino |
| **{CIDADE\_ORIGEM}** | Nome da cidade de origem |
| **{CIDADE\_DESTINO}** | Nome da cidade de destino |
| **{VALOR\_MERCADORIA}** | Valor da mercadoria informado na tela |
| **{PESO}** | Peso em Kg informado na tela |
| **{M3}** | Metros cúbicos informados na tela |
| **{VALOR\_FRETE}** | Valor do frete calculado |

#### Exemplo de Modelo de Email:

```
Olá,${nl}${nl}
Segue cotação de frete:${nl}
Origem: {PARCEIRO_ORIGEM} - {CIDADE_ORIGEM}${nl}
Destino: {PARCEIRO_DESTINO} - {CIDADE_DESTINO}${nl}
Peso: {PESO} kg | Volume: {M3} m³${nl}
Valor da Mercadoria: R$ {VALOR_MERCADORIA}${nl}
Valor do Frete: R$ {VALOR_FRETE}${nl}${nl}
Atenciosamente.
```

#### 2. Customize a regra de cálculo do frete

Implemente a rotina de banco de dados **STP\_CALCULA\_VLRFRETE\_TMS** conforme a regra de negócio do cliente. Para mais detalhes, consulte a seção **“Personalização do cálculo do frete”**.

#### 3. Conceder acesso à tela

Acesse o **Controle de Acesso** e libere o recurso **br.com.sankhya.soplogistica.mov.cotacao.frete** para os perfis ou usuários que utilizarão a tela.

### Visão geral da tela

A tela está dividida em duas áreas principais:

- **Área de cotação (parte superior):** preencha os dados da cotação e utilize os botões de ação disponíveis.
- **Histórico (parte inferior):** visualize, em formato de grade, os pedidos de transporte já gerados pela tela.

#### Campos da área de cotação

| **Campo** | **Descrição** | **Obrigatório?** |
| --- | --- | --- |
| **Parceiro Origem** | Parceiro (cliente, transportadora, etc.) onde a carga será coletada. | Pelo menos um entre **Parceiro Origem** ou **Cidade Origem**. |
| **Cidade** | Cidade onde a carga será coletada. Caso o Parceiro Origem esteja preenchido | Pelo menos um entre **Parceiro** |
| **Origem** | e a cidade não, o sistema usa a cidade cadastrada no parceiro. | **Origem** ou **Cidade Origem**. |
| **Parceiro Destino** | Parceiro de destino da carga. | Pelo menos um entre **Parceiro Destino** ou **Cidade Destino**. |
| **Cidade Destino** | Cidade de destino da carga. | Pelo menos um entre **Parceiro Destino** ou **Cidade Destino**. |
| **Valor Mercadoria** | Valor total da mercadoria que será transportada. Influencia o cálculo quando a regra prevê ad valorem. | Não, mas recomendado. |
| **Peso em Kg** | Peso total da carga em quilogramas. | Não, mas recomendado. |
| **Metros Cúbicos** | Volume total da carga em m³. | Não, mas recomendado. |
| **Valor do Frete** | Resultado do cálculo. Pode ser preenchido manualmente caso a empresa queira sobrepor o valor. | Sim, para usar **Gerar Pedido**. |

#### Botões de ação disponíveis

| **Botão** | **O que faz** |
| --- | --- |
| **Calcular** | Aciona a regra de cálculo de frete cadastrada e preenche o campo **Valor do Frete**. |
| **Gerar Pedido** | Cria um Pedido de Transporte (com roteiro) baseado no pedido modelo configurado, ajustando parceiros, cidades, peso, m³ e valor do frete. |
| **Enviar Email** | Abre uma janela com assunto e corpo de e-mail pré-preenchidos para revisão e envio. |

#### Histórico da tela

- Visualize os pedidos de transporte gerados pela tela.
- Utilize o filtro personalizado para localizar pedidos específicos.
- Clique em “Aplicar” para atualizar os resultados conforme o filtro definido.
- Dê duplo clique em um pedido para abrir a tela de Pedido de Transporte, já posicionada no registro selecionado.

### Procedimento

#### Como simular o valor de um frete

##### **(1)** Acesse a tela ''Cotação Frete'' (Logística » TMS » Rotinas » Cotação Frete).

##### **(2)** Informe a origem da carga nos campos ''Parceiro Origem'' ou ''Cidade Origem'' (ou ambos).

##### **(3)** Informe o destino nos campos ''Parceiro Destino'' ou ''Cidade Destino'' (ou ambos).

##### **(4)** Preencha os campos ''Valor Mercadoria'', ''Peso em Kg'' e ''Metros Cúbicos'' com os dados da carga.

##### **(5)** Clique em Calcular.

##### **(6)** Verifique o campo “Valor do Frete”, que será preenchido conforme a regra de cálculo configurada.

| **ATENÇÃO**: Se sua empresa ainda não personalizou a regra de cálculo ( STP\_CALCULA\_VLRFRETE\_TMS ), o sistema sempre retornará R$ 0,00. Isso não é um erro — é o comportamento padrão até que a regra seja customizada. Veja Personalização do cálculo do frete. |
| --- |

#### Como gerar um pedido a partir da cotação

**(1)** Confirme que o campo **Valor do Frete** está preenchido (calculado ou digitado).

**(2)** Confirme que origem e destino estão preenchidos.

**(3)** Clique em ''Gerar Pedido''.

**(4)** O sistema cria um novo pedido a partir do **Nro Pedido Modelo** configurado na tela de configurações TMS, ajustando:

- Parceiros e cidades de origem e destino;
- Peso e quantidade (m³) com os valores da tela;
- Valor do frete da empresa com o valor calculado.

**(5)** Uma mensagem é exibida: "Pedido NNNN gerado com sucesso."

**(6)** O pedido aparece automaticamente no grid **Histórico**.

| **DICA:** Para abrir o pedido recém-criado e revisar/complementar dados, dê um duplo clique sobre ele no grid **Histórico**. |
| --- |

#### Como enviar a cotação por e-mail

**(1)** Após calcular o frete, clique em **Enviar Email**.

**(2)** O sistema abre a janela **Enviar Email** com os campos:

- **Destinatário:** informe o e-mail (ou e-mails) do destinatário separados por vírgula.
- **Assunto:** vem preenchido com o **Modelo de Assunto do Email** configurado.
- **Conteúdo:** vem preenchido com o **Modelo de Email** configurado, com as variáveis já substituídas pelos dados da cotação.

**(3)** Revise o conteúdo e ajuste o que for necessário.

**(4)** Clique em **Enviar**.

**(5)** Mensagem exibida: "Email marcado para ser enviado com sucesso".

| **IMPORTANTE:** O envio do e-mail é feito de forma **assíncrona** pela rotina de fila de mensagens do sistema. Isso significa que o e-mail não é enviado no exato momento do clique — ele entra em uma fila e é processado pela rotina padrão. Se a fila estiver parada ou o servidor de e-mail (SMTP) mal configurado, o envio não ocorre. |
| --- |

####

#### Como consultar o histórico

**(1)** Role até a área **Histórico** no rodapé da tela.

**(2)** Use o **filtro personalizado** para informar critérios (período, parceiro, etc.).

**(3)** Clique em **Aplicar** para atualizar a lista.

**(4)** Para abrir um pedido, **dê um duplo clique** sobre ele.

### Personalização do cálculo do frete

#### Assinatura obrigatória da rotina

A assinatura **deve ser preservada exatamente como abaixo**. Qualquer mudança na quantidade, ordem ou tipo dos parâmetros faz com que a tela falhe ao calcular.

| **#** | **Parâmetro** | **Sentido** | **Descrição** |
| --- | --- | --- | --- |
| 1 | P\_CODPARCORIG | Entrada | Código do parceiro de origem ( TGFPAR.CODPARC ). Pode vir nulo. |
| 2 | P\_CODPARCDEST | Entrada | Código do parceiro de destino ( TGFPAR.CODPARC ). Pode vir nulo. |
| 3 | P\_CODCIDORIG | Entrada | Código da cidade de origem ( TSICID.CODCID ). Pode vir nulo. |
| 4 | P\_CODCIDDEST | Entrada | Código da cidade de destino ( TSICID.CODCID ). Pode vir nulo. |
| 5 | P\_VLRMERCADORIA | Entrada | Valor da mercadoria. |
| 6 | P\_PESO | Entrada | Peso em Kg. |
| 7 | P\_M3 | Entrada | Volume em metros cúbicos. |
| 8 | P\_VLRFRETE | **Saída** | Valor do frete calculado. **Sempre devolver um número** — nunca nulo. |

**Esqueleto Oracle**

```
CREATE OR REPLACE PROCEDURE STP_CALCULA_VLRFRETE_TMS ( P_CODPARCORIG NUMBER,
P_CODPARCDEST NUMBER, P_CODCIDORIG NUMBER, P_CODCIDDEST NUMBER, P_VLRMERCADORIA NUMBER, P_PESO    NUMBER,
P_M3	NUMBER,
P_VLRFRETE OUT NUMBER
)
AS BEGIN
P_VLRFRETE := 0;

-- Implementar regra de cálculo da empresa aqui.
-- Exemplo (pseudo): consultar uma tabela própria de frete pela
-- combinação de cidades e aplicar fator por kg + ad valorem.

EXCEPTION
WHEN NO_DATA_FOUND THEN
P_VLRFRETE := 0;
END;
/
```

**Esqueleto SQL Server**

```
CREATE OR ALTER PROCEDURE STP_CALCULA_VLRFRETE_TMS @P_CODPARCORIG	NUMERIC(18, 0),
@P_CODPARCDEST	NUMERIC(18, 0),
@P_CODCIDORIG	NUMERIC(18, 0),
@P_CODCIDDEST	NUMERIC(18, 0),
@P_VLRMERCADORIA NUMERIC(18, 4),
@P_PESO	NUMERIC(18, 4),
@P_M3	NUMERIC(18, 4), @P_VLRFRETE	NUMERIC(18, 4) OUTPUT
AS BEGIN
SET @P_VLRFRETE = 0;

-- Implementar regra de cálculo da empresa aqui.
END GO
```

### Boas práticas de customização

- ##### Trate parâmetros nulos. Origem ou destino podem chegar com apenas o parceiro ou apenas a cidade.
- ##### Sempre retorne um número em P\_VLRFRETE . Use como padrão quando nenhuma regra se aplicar.
- ##### Nunca altere a assinatura (ordem, nome, tipo ou quantidade dos parâmetros).
- ##### Não execute COMMIT ou ROLLBACK dentro da procedure — a transação é controlada pela aplicação.
- ##### Não use DBMS\_OUTPUT ou prints — a aplicação espera apenas o retorno numérico limpo.
- ##### Trate exceções esperadas (como NO\_DATA\_FOUND ) e devolva 0 em vez de propagar erro.

### Como instalar a procedure customizada

**(1)** Conecte-se ao banco do cliente com um usuário do schema da Sankhya.

**(2)** Execute o script (CREATE OR REPLACE no Oracle, CREATE OR ALTER no SQL Server).

**(3)** Confirme se foi criada: ```sql -- Oracle SELECT TEXT FROM USER\_SOURCE WHERE NAME = 'STP\_CALCULA\_VLRFRETE\_TMS' ORDER BY LINE;-- SQL Server SELECT OBJECT\_DEFINITION(OBJECT\_ID('STP\_CALCULA\_VLRFRETE\_TMS'));

**(4)** Teste a procedure direto no banco antes de validar pela tela:sql -- Oracle DECLARE V\_VLR NUMBER; BEGIN STP\_CALCULA\_VLRFRETE\_TMS(12, 22, 2, 15, 1500, 100, 1, V\_VLR); DBMS\_OUTPUT.PUT\_LINE('Frete: ' || V\_VLR); END; / ```

**(5)** Acesse a tela ''Cotação de Frete'' (Logística » TMS » Rotinas » Cotação Frete) e clique em Calcular com os mesmos parâmetros para conferir o resultado.

### Mensagens e erros comuns

| **Mensagem** | **Quando aparece** | **O que fazer** |
| --- | --- | --- |
| "Selecione o Parceiro ou Cidade de Origem." | Ao clicar em **Calcular** ou **Gerar Pedido** sem origem informada. | Preencha **Parceiro Origem** ou **Cidade Origem**. |
| "Selecione o Parceiro ou Cidade de Destino." | Ao clicar em **Calcular** ou **Gerar Pedido** sem destino informado. | Preencha **Parceiro Destino** ou **Cidade Destino**. |
| "Informe o Valor do Frete." | Ao clicar em **Gerar Pedido** com o campo **Valor do Frete** vazio. | Clique antes em **Calcular** ou digite manualmente o valor do frete. |
| "Para gerar o pedido antes é necessário configurar o 'Nro Pedido Modelo' na tela de configuração do TMS." | Ao clicar em **Gerar Pedido** sem o pedido modelo configurado. | Acesse **Configurações TMS** e preencha o campo **Nro Pedido Modelo** com o número de um Pedido de Transporte existente. |
| "Selecione um pedido antes." | Ao tentar abrir um pedido no grid **Histórico** sem nenhum selecionado. | Clique em uma linha do grid antes de tentar abrir. |
| "Pedido NNNN gerado com sucesso." | Após criar pedido com sucesso. | Apenas confirmação. O pedido já aparece no grid  **Histórico**. |
| "Email marcado para ser enviado com sucesso" | Após confirmar o envio na janela **Enviar Email**. | A mensagem ficou na fila de envio. O envio efetivo ocorrerá pela rotina de fila padrão. |

####

### Perguntas Frequentes (FAQ)

- ##### Por que o Valor do Frete sempre vem zerado?

A rotina de cálculo (**STP\_CALCULA\_VLRFRETE\_TMS**) é entregue vazia propositalmente, pois cada cliente deve personalizá-la conforme sua regra de cálculo. Solicite ao consultor responsável pela implantação que realize a customização da procedure de acordo com a tabela de frete da empresa.

- **Posso digitar o valor do frete manualmente?**

Sim. O campo “Valor do Frete” permite digitação manual. Utilize essa opção para sobrepor o valor calculado em situações específicas ou para gerar o pedido sem executar o cálculo automático.

- **O e-mail é enviado na hora?**

Não. O sistema adiciona a mensagem à fila de envio (**FILA\_MSG**). O envio é realizado pela rotina padrão de filas da plataforma, conforme a frequência configurada no servidor. Caso o e-mail demore para ser entregue, verifique com a equipe de TI o status da fila e as configurações do servidor SMTP.

- **Posso configurar mais de um pedido modelo?**

Não. A configuração “Nro Pedido Modelo” permite informar apenas um pedido. Selecione um modelo que represente adequadamente o cenário mais comum de cotações da empresa.

- **Como o pedido modelo é usado?**

Ao clicar em “Gerar Pedido”, o sistema clona o pedido modelo (**cabeçalho e primeiro roteiro**) e ajusta automaticamente os seguintes dados:

- **Parceiros e cidades** de origem e destino;
- **Peso** e **quantidade (m³)**;
- **Valor do frete da empresa**.

Os demais campos como **TOP, natureza, condições e observações**, são mantidos conforme o pedido modelo e podem ser revisados após a geração.

- **Posso enviar para mais de um destinatário no e-mail?**

Sim. No campo **“Destinatário”**, informe os e-mails separados por vírgula. O sistema criará uma mensagem na fila para cada destinatário informado.
