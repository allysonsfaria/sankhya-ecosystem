---
id: "4409862149655"
titulo: "Melhores práticas para contabilização de compensação financeira"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4409862149655-Melhores-pr%C3%A1ticas-para-contabiliza%C3%A7%C3%A3o-de-compensa%C3%A7%C3%A3o-financeira"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:21:23Z"
rotulos: ["Configuração", "Movimentação Financeira", "TOP", "Contabilização", "Financeiro", "Conta bancária sem conta contábil em compensação", "Não gera movimento bancário (TGFMBC)", "Exceção para financeiros compensados nas regras TOP", "Erro"]
---

# Melhores práticas para contabilização de compensação financeira

Alguns clientes configuram a contabilização de suas TOP’s de baixa para buscar a conta contábil do cadastro da conta bancária, porém, quando se trata de um financeiro baixado através da rotina de 'Compensação Financeira', se deparam com o seguinte erro no momento da contabilização:

"**Baixa. A conta bancaria está sem conta contábil".**

Quando um financeiro é baixado por meio de um movimento de compensação, o mesmo não gera movimento bancário, ou seja: não vai para a TGFMBC.

Isso é comprovado quando observa-se um financeiro baixado nesta circunstância e verifica-se o campo '**Conta baixa'**na movimentação financeira. Este campo não terá conta informada, a partir deste ponto surge um dos questionamentos mais comuns nos nossos atendimentos fiscais/contábeis:

#### Como configurar a TOP para contabilização?

Crie uma tratativa nas regras de contabilização das TOPs utilizadas na rotina de compensação financeira de modo a informar uma exceção para os financeiros que fazem parte de uma compensação, conforme exemplo a seguir.

**Caso de uso:**

O acerto 1301 foi originado através da compensação dos seguintes financeiros:

- Receita: Número único: 577325=1000,00
- Despesa: Número único: 561976=1500,00

Ao efetuar o acerto foram informadas as TOP’s de recebimento e de pagamento respectivamente:

- **Foram baixados os financeiros:**
- Receita: R$1000,00
- Despesa: R$1000,00 ( Nro Único 584873): Esse financeiro foi criado no momento da compensação já baixado para ser a contrapartida da receita.
- **Observação**: O valor remanescente de 500,00 referente a despesa ficou em aberto no financeiro 561976 para ser baixado posteriormente.

#### Configurações recomendadas:

Veja neste exemplo como será feita a regra de contabilização da despesa (a mesma regra vale para a receita, sendo recomendado configurar de forma semelhante):

- TOP utilizada para a despesa (Pagamento):

- D- Valor do desdobramento:

Formula.VLRDESDOB

- C- Valor da baixa **caso o financeiro NÃO seja de compensação -**Neste caso, conforme na figura ilustrativa, pode-se buscar a conta da conta bancária normalmente:

IF(Formula.NUCOMPENS = 0, Formula.VLRBAIXA, 0)

- C-Valor da baixa caso o financeiro **seja de compensação -**Neste caso, não se pode buscar a conta da conta bancária, o ideal é que se use uma conta fixa ou que se busque de outro cadastro que não envolva o movimento bancário.:

IF(Formula.NUCOMPENS <> 0, Formula.VLRBAIXA, 0)

**![Imagem 1: Observações:](https://ajuda.sankhya.com.br/hc/article_attachments/16094766733079)Observações:**

Este é um exemplo simples de como essa exceção pode ser configurada dentro das regras de contabilização. Caso necessite de algo mais complexo e elaborado, um consultor de sua Franquia/Filial deverá ser acionado para parametrizações/validações.
