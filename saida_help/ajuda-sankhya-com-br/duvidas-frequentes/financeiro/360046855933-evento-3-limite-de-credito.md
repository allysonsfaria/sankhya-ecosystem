---
id: "360046855933"
titulo: "Evento 3 - Limite de Crédito"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360046855933-Evento-3-Limite-de-Cr%C3%A9dito"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-09-24T14:57:37Z"
rotulos: ["Configuração", "Parceiro", "Crédito", "TOP", "Preferências", "Financeiro", "Validação limite crédito (VALLIMCRED)", "Configurações para vendas e liberação", "Limite crédito matriz (LIMCREDMATRIZ)"]
---

# Evento 3 - Limite de Crédito

**(1)** Para este evento, tem-se as seguintes configurações:

![Imagem 1: O parâmetro "Valida limite de crédito? - VALLIMCRED " deve estar devidamente configurado:](https://ajuda.sankhya.com.br/hc/article_attachments/19034099763735) O parâmetro "Valida limite de crédito? - **VALLIMCRED**" deve estar devidamente configurado:

- Tela 'Preferências' (Configurações » Avançado):

![Imagem 2: Tela 'Preferências' ( Configurações » Avançado):](https://ajuda.sankhya.com.br/hc/article_attachments/19034084138263)

**Determina-se neste parâmetro se serão ou não validados os limites de crédito dos parceiros; optando-se por validar, define-se também como será essa validação; o parâmetro tem as seguintes opções:**

- **Não valida:** não validará o limite de crédito;
- **Valida todo a receber:** validará o limite de crédito. Na solicitação de liberação do evento para o valor solicitado será considerado financeiros "Reais" existentes e o financeiro do lançamento em curso ("Real" ou "Provisão"), sendo que essa validação ignora provisões existentes;
- **Valida a receb. e prov. no mês:** irá validar o limite de crédito. Na solicitação de liberação do evento para o valor solicitado será considerado financeiros Reais e Provisão com data de negociação (TGFFIN.DTNEG) dentro do mês corrente + o valor do lançamento em curso (Real ou Provisão);
- **Valida TUDO p/TOP c/Financeiro:** validará o limite de crédito. Na solicitação de liberação do evento para o valor solicitado serão considerados financeiros Reais existentes mais o financeiro do lançamento em curso (somente em lançamento que atualiza financeiro Real). Para o lançamento que provisiona financeiro, o sistema permite confirmar quando o parceiro não tem financeiros Reais existentes que ultrapassem o limite de crédito;
- **Valida TUDO p/TOP c/Financeiro com provisão:** irá validar o limite de crédito. Na solicitação de liberação do evento para o valor solicitado serão considerados todos os financeiros pendentes, Reais e Provisões, inclusive o financeiro do lançamento em curso (Real ou Provisão).

**Nota:** caso o parâmetro Valida limite de crédito? - VALLIMCRED esteja configurado com a opção "Valida TUDO p/TOP c/Financeiro" e a TOP da nota atualizar o financeiro, o sistema exigirá a liberação de limites. Caso a TOP da nota não atualize financeiro, não será exigida a liberação de limites.

![Imagem 3: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/20804191046423)  **IMPORTANTE:**

Na configuração deste evento, caso o parâmetro **"Valida Limite de crédito pela matriz? - LIMCREDMATRIZ"** estiver habilitado, e o parceiro matriz configurado não possuir limite de crédito, a liberação do evento não será solicitada. 

![Imagem 4: No cadastro de 'Parceiros', no campo " Limite de crédito " presente na aba 'Crédito', define-se um valor:](https://ajuda.sankhya.com.br/hc/article_attachments/19034111489047) No cadastro de 'Parceiros', no campo "**Limite de crédito**" presente na aba 'Crédito', define-se um valor:

- Tela 'Parceiros' (Configurações » Cadastros):

![Imagem 5: Tela 'Parceiros' (Configurações » Cadastros) :](https://ajuda.sankhya.com.br/hc/article_attachments/19034094829975)

**Exemplo:** ao lançar uma Nota (mais precisamente no ato da confirmação do Pedido/Nota), se a soma dos débitos do Parceiro forem superiores ao Limite de Crédito definido para o Cliente, será aberto o pop-up de solicitação de liberação. Porém, uma vez que a liberação já tenha sido realizada e o pedido confirmado, a liberação de limites não será solicitada novamente mesmo que haja alteração nos produtos do pedido.

**![Imagem 6: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/20804191064215) OBSERVAÇÕES:**

1. Na configuração deste evento, tem-se que caso o parâmetro**"Valida Limite de crédito pela matriz? - LIMCREDMATRIZ"** estiver habilitado, e o parceiro matriz configurado não possuir limite de crédito, a liberação do evento não será solicitada.
2. Já o parâmetro **"Validar limite de crédito com valor zero? - VALLIMCREDZERO"**, quando ligado, permite que o sistema valide limites de crédito para parceiros com limite configurado como zero.
3. Os parâmetros indicados a seguir também influenciam na rotina para usar o evento 03 , se atentar nas configurações dos mesmo quando se trata de vendas com cartão de crédito e debito: **VALLIMCRETPV (Consumir limite de crédito por Tipo de Negociação**) **VALLIMCRETIT (Não consumir limite de crédito por Tipo Título?**). Se estiverem com a opção **NENHUM** selecionado , mesmo que seja uma venda de cartão de DEBITO (Á VISTA) o sistema ira solicitar a liberação do evento.

Ressalta-se que os parâmetros influenciarão conforme a opção configurada:

**(1)** Parâmetro VALLIMCRETIT

- **Nenhum:**o sistema retorna todos os títulos, independentemente do [Tipo de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494).
- **Apenas crédito:**o sistema não considera os títulos configurados com o Subtipo**"Cartão de Crédito"**, na tela Tipo de Título, e que sejam de origem de estoque ([Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras)/[Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)).
- **Apenas débito:**o sistema desconsidera os títulos financeiros configurados com o Subtipo**"Cartão de Débito"**, na tela Tipo de Título, e que sejam de origem de estoque (Central de Compras/Vendas).
- **Ambos:**o sistema desconsidera os títulos financeiros configurado com o Subtipo Cartão de Crédito ou Cartão de Débito, e que sejam de origem de estoque (Central de Compras/Vendas).

**(1)** Parâmetro VALLIMCRETPV

- **Nenhum:** o sistema retorna todos os títulos, independentemente do [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#top) para consumir o limite de crédito.
- **Apenas crédito:**o sistema desconsidera do consumo do limite de crédito os títulos cujo **"Subtipo"** na tela Tipo de Negociação seja **"Cartão de Crédito"**.
- **Apenas débito:**o sistema desconsidera do consumo do limite de crédito os títulos cujo Subtipo na tela Tipo de Negociação seja**"Cartão de Débito"**.
- **Ambos:**o sistema desconsidera do consumo do limite de crédito os títulos cujo Subtipo na tela Tipo de Negociação seja Cartão de Crédito ou Cartão de Débito
