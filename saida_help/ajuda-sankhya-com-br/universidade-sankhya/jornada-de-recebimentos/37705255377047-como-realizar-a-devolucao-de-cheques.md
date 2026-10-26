---
id: "37705255377047"
titulo: "Como realizar a devolução de cheques"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37705255377047-Como-realizar-a-devolu%C3%A7%C3%A3o-de-cheques"
trilha: "Universidade Sankhya > Jornada de Recebimentos"
atualizado_em: "2026-07-22T14:09:25Z"
rotulos: ["Contas", "Parceiro", "Movimentação Financeira", "Financeiro"]
---

# Como realizar a devolução de cheques

| Categoria |
| --- |
| [Como funciona e qual a sua importância?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37705255377047-Como-realizar-a-devolu%C3%A7%C3%A3o-de-cheques#h_01KF1DKACFXTWYRPEVM199H8FY) |
| [Quais problemas essa prática resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37705255377047-Como-realizar-a-devolu%C3%A7%C3%A3o-de-cheques#h_01KF1DK4XY920CT8B8ZEN9J435) |
| [Quais os riscos de não a utilizar?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37705255377047-Como-realizar-a-devolu%C3%A7%C3%A3o-de-cheques#h_01KF1DJYQRX8ECRQBWF1QRMTF1) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37705255377047-Como-realizar-a-devolu%C3%A7%C3%A3o-de-cheques#h_01KF1DJQHPHBTS16Y8PP239E8S) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37705255377047-Como-realizar-a-devolu%C3%A7%C3%A3o-de-cheques#h_01KF1DJJM5M5SQ8SBRSDSVQBE4) |
| [Agora, efetue as movimentações no sistema conforme o contexto fornecido](https://ajuda.sankhya.com.br/hc/pt-br/articles/37705255377047-Como-realizar-a-devolu%C3%A7%C3%A3o-de-cheques#h_01KF1DJA18YYCTX9R9BHKX80PW) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37705255377047-Como-realizar-a-devolu%C3%A7%C3%A3o-de-cheques#h_01KF1DHSADE6R4X4QXY5JQKRW5) |

## Devolução de cheque

#### Como funciona e qual a sua importância?

O processo de devolução de cheque no Sankhya consiste em manter um controle detalhado de todos os cheques recebidos de clientes devolvidos pelo banco. Quando ocorre o registro da devolução, o sistema atualiza automaticamente o contas a receber, estornando a baixa do título caso ela já tenha sido feita. O setor de cobrança e financeiro podem tomar ações corretivas, como reapresentação do cheque, bloqueio de vendas a prazo, ajuste no limite de crédito do cliente ou outras medidas previstas na política da empresa no momento de registrar esse processo no sistema.

Este procedimento é crucial para garantir a precisão dos registros financeiros e a integridade do contas a receber. Ele protege a saúde financeira da empresa ao evitar discrepâncias nos relatórios e agiliza a tomada de decisões, como a reapresentação do cheque ou renegociação de pagamentos. Além disso, melhora o controle sobre clientes inadimplentes.

#### Quais problemas essa prática resolve?

- **Desorganização financeira:** atualiza e centraliza os registros de cheques devolvidos, eliminando inconsistências e garantindo maior controle sobre as contas a receber.
- **Falta de rastreabilidade:** mantém um histórico claro das devoluções, facilitando auditorias e análises futuras.
- **Falta de ações preventivas:** permite medidas rápidas, como bloqueio de vendas ou ajustes de crédito, reduzindo os riscos de inadimplência.
- **Ineficiência operacional:** automatiza o registro das devoluções, economizando tempo e minimizando erros manuais.

#### Quais os riscos de não a utilizar?

Sem um controle estruturado de devolução de cheques, a empresa corre o risco de manter registros financeiros desatualizados e inconsistentes. Isso dificulta a identificação de inadimplentes, compromete o planejamento financeiro e aumenta a possibilidade de decisões comerciais inadequadas. Além disso, a falta de rastreabilidade pode dificultar auditorias e análises, impactando a credibilidade da empresa. A ausência desse processo também limita a capacidade de agir rapidamente em casos de inadimplência, agravando os problemas de fluxo de caixa.

#### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1056364496)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** A **Axis** identificou que um cheque de um cliente foi devolvido pelo banco devido à insuficiência de fundos, essa devolução precisa ser registrada no Sankhya para atualizar os registros financeiros, aplicar medidas corretivas e manter a rastreabilidade das ações realizadas. 

**Tarefa**: Você deve localizar um título que foi baixado (pago) com cheque e realizar a devolução deste. Caso não possua títulos baixados com cheque, faça a baixa e depois simule a devolução.

#### Agora, efetue as movimentações no sistema conforme o contexto fornecido

1. **Baixar um título (receber com cheque)**

   - Acesse a tela **Movimentação Financeira**
     Menu: Financeiro » Rotinas » Movimentação Financeira
   - Utilize os filtros para localizar um título, filtre por: Receitas, Real, Pendentes.
   - Abra o título e verifique o campo **Tipo de Título** que deve estar com a opção “Cheque”.
   - Clique no botão **Baixar** e realize o processo de baixa do título.
2. **Seleção dos títulos para devolução:**

   - Acesse a tela **Devolução de Cheques**
     Menu: Financeiro » Rotinas » Devolução de Cheques
   - No filtro lateral, preencha:

     - **Nro. Cheque:** Essa informação pode ser localizada na tela Movimentação Financeira, aba **Cobrança**, campo **Nosso Número**.
     - **Tipo de Lançamento**: Receita
     - Clique em **Aplicar**.
     - Selecione o título que será devolvido.
3. **Processar a devolução:**

   - Clique em **Processar Devolução** para devolver todos os cheques associados à baixa.
   - Preencha os dados do pop-up aberto Devolução de cheques na etapa **Devolução**: 

     - Alínea: Ex: **Cheque sem fundos - 1ª apresentação**
     - Data:
     - Valor: Valor do cheque a ser devolvido.
     - Clique no botão **Próximo**
     - Preencha todos os campos obrigatórios para a compensação da devolução:
     - **TOP Baixa**
     - **Natureza**
     - **Lançamento Bancário**
     - **Tipo de Título**
     - **Conta**
     - **Empresa baixa**
     - **Histórico**
     - Clique no botão **Próximo**
     - Na próxima tela preencha os campos que serão utilizados para a **Pendência** que se trata do título do cliente que ficará em aberto já que o cheque foi devolvido:
     - **Tipo Operação**
     - **Data do Vencimento**
     - As seguintes opções não são obrigatórias, mas podem ser usadas conforme a necessidade da empresa:
     - **Alterar Tipo de Título no original? -** Altera o tipo de título no registro original e na despesa gerada pela devolução, ajustando para o tipo informado nesta tela.
     - **Passar o Nro Cheque p/o Nro Nota? -** Insere o número do cheque devolvido no campo "Número Nota" do título correspondente.
     - **Bloquear Crédito do Parceiro? -** Bloqueia vendas a prazo no cadastro do parceiro, registrando "Devolução de cheques" como motivo do bloqueio.
     - **Alterar Tipo de Título do(s) título(s) em aberto? -** Aplica o tipo de título aos títulos de despesa e receita gerados, útil para parceiros com tipos específicos de títulos.
     - **Permitir devolução para títulos de receitas com comissão a ser paga** **? -** Permite a devolução de cheques mesmo com comissões pendentes; caso desmarcada, bloqueia devoluções nessa situação.
     - Clique em **Concluir**.
     - Caso necessário, utilize o botão **"Devolução Individual"** para devolver cheques específicos.

#### Correção e Repetição

- Após a devolução, confira se:
- O título de receita foi baixado corretamente.
- Há uma despesa gerada no mesmo valor para compensação.
- Existe um novo título de receita em aberto, indicando que o cliente ainda precisa realizar o pagamento.
