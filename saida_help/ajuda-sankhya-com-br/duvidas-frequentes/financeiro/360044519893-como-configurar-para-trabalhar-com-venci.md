---
id: "360044519893"
titulo: "Como configurar para trabalhar com Vencimento Fixo para Dia de Pagamento?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044519893-Como-configurar-para-trabalhar-com-Vencimento-Fixo-para-Dia-de-Pagamento"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-07-22T15:55:53Z"
rotulos: ["#criadoRoger", "Configuração", "Parceiro", "Crédito", "Preferências", "Financeiro", "Vencimento Fixo dia de Pagamento", "Configure prazo parceiro", "Configure prazo negociação"]
---

# Como configurar para trabalhar com Vencimento Fixo para Dia de Pagamento?

**(1)** Veja agora 2 principais opções de trabalhar com Vencimento Fixo.

#### **(2)**Cenário 1:

Desabilita o parâmetro **"TRANSFVENC"** em (Caminho de acesso: Configurações » Avançado » Preferências) e informe o **Dia Desejado** para ser dia Fixo de Vencimento no campo **"Dia para pagamento"** do cadastro de parceiro (Caminho de acesso: Configurações » Cadastros » Parceiros, aba: Credito).

Exemplo de Vencimento Fixo no **dia 12**, mesmo que o vencimento dê em um Feriado ou Final de Semana, se a parcela do Tipo de Negociação estiver com o campo Prazo: 1, o sistema somará apenas 1 na data base.

Vejamos os exemplos abaixo.

**Exemplo 1:**
**Prazo**: 1
**Dt Neg:** 09/02/2018
**Dt Base pro calculo de vencimento** 09/02/2018 + PRAZO (neste caso é 1) = 10/02/2018
Como dia 10 é **antes** do dia 12 (Dia para pagamento), o vencimento será 12/02/2018

**Exemplo 2:**
**Prazo:** 12
**Dt Neg:** 09/02/2018
**Dt Base pro calculo de vencimento** 09/02/2018 + PRAZO (neste caso é 12) = 21/02/2018
Como dia 21 é depois do dia 12 (Dia para pagamento), o vencimento será 12/03/2018

**Exemplo 3:**
**Prazo:** 1
**Dt Neg:** 15/02/2018
**Dt Base pro calculo de vencimento** 15/02/2018 + PRAZO (neste caso é 1) = 16/02/2018
Como dia 16 é depois do dia 12 (Dia para pagamento), o vencimento será 12/03/2018

Ou seja, se o cliente quiser dia 12 sempre mesmo sem dar prazo nenhum pro cliente, o prazo deve ficar 1. Se ele quiser dia 12 sempre mas sempre garantir que vai ficar pro próximo mês, informando 12 no prazo já faz isso acontecer.

#### **(2)** Cenário 2:

Outra forma de configurar seria o parâmetro TRANSFVENC (Caminho de acesso: Configurações » Avançado » Preferências) desligado.

Na parcela do Tipo de negociação (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de Negociação, aba: Parcelas) marque a opção **"Soma prazo de cliente"** e campo **"Prazo":** 1.

No cadastro do parceiro (Caminho de acesso: Configurações » Cadastros » Parceiros, aba: Credito) informe o **Dia  Desejado** para ser dia Fixo de Vencimento, no campo Dia para pagamento, e valor de prazo no campo **"Prazo médio pagamento"**.

Como essa configuração no tipo de negociação sempre fica com Prazo = 1 e a configuração completa do dia para pagamento fica apenas no parceiro, dando a possibilidade de se utilizar o mesmo tipo de negociação com parceiros diferentes e 'Dia para pagamento' diferentes.

**(1)** Mais detalhes, acesse o artigo: [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173), para verificar as considerações finais. Lembrando que as 2 (duas) opções relatadas são possíveis cenários e dependendo do processo de cada Empresa pode não atender em sua totalidade.

**![Imagem 1: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17005051588247) OBSERVAÇÃO:**

Para que o sistema valide a Seção Dias fixos para pagamento é necessário habilitar os parâmetros **"Utiliza regra de vencimento para dias fixos? - USARDIAFIXOVCT"** e **"Altera calculo de vencimento para dias fixos? - CALDIAFIXOVCT".**
