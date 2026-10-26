---
id: "37724511439255"
titulo: "Como realizar o controle de cheques emitidos e não compensados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37724511439255-Como-realizar-o-controle-de-cheques-emitidos-e-n%C3%A3o-compensados"
trilha: "Universidade Sankhya > Jornada de Pagamentos"
atualizado_em: "2026-07-22T14:09:07Z"
rotulos: ["Configuração", "Contas", "Movimentação Financeira", "Financeiro"]
---

# Como realizar o controle de cheques emitidos e não compensados

| Categoria |
| --- |
| [Porque controlar os cheques emitidos é importante?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37724511439255-Como-realizar-o-controle-de-cheques-emitidos-e-n%C3%A3o-compensados#h_01KF3JX4ZQZ9EMSE82YFGGJ2AH) |
| [Quais problemas esse recurso resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37724511439255-Como-realizar-o-controle-de-cheques-emitidos-e-n%C3%A3o-compensados#h_01KF3JWVESM5Z6EF5ZZ9FB17JP) |
| [Quais os riscos de não as utilizar?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37724511439255-Como-realizar-o-controle-de-cheques-emitidos-e-n%C3%A3o-compensados#h_01KF3JWP6Z7YC1J40WJBPWG20B) |
| [Vídeo de demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37724511439255-Como-realizar-o-controle-de-cheques-emitidos-e-n%C3%A3o-compensados#h_01KF3JWHF2XBP4MMHS7SVJPCZ6) |
| [Cenário prático e passo a passo para realizar a atividade no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37724511439255-Como-realizar-o-controle-de-cheques-emitidos-e-n%C3%A3o-compensados#h_01KF3JWAH5Y3XBMCZY36QJGHZ3) |
| [Hora de colocar a mão na massa! Realize as movimentações necessárias](https://ajuda.sankhya.com.br/hc/pt-br/articles/37724511439255-Como-realizar-o-controle-de-cheques-emitidos-e-n%C3%A3o-compensados#h_01KF3JVTD1NV2KN0VTVCHBFA6E) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37724511439255-Como-realizar-o-controle-de-cheques-emitidos-e-n%C3%A3o-compensados#h_01KF3JTT796Y7QVSKB0DGGA7TK) |

## Controle de cheques emitidos e não compensados

#### Porque controlar os cheques emitidos é importante?

Esse controle permite acompanhar cheques que já foram emitidos, mas ainda não foram compensados, garantindo que o saldo bancário reflita apenas os valores realmente disponíveis. Isso evita decisões financeiras equivocadas por considerar valores comprometidos como saldo livre, além de melhorar a precisão na conciliação e no planejamento do caixa.

#### Quais problemas esse recurso resolve?

- **Evita pagamentos duplicados:** Impede que um título já pago por cheque seja quitado novamente.
- **Melhora a conciliação bancária:** Alinha os registros do sistema com o extrato real.
- **Reduz riscos operacionais e fraudes:** Facilita a identificação de extravios ou uso indevido de cheques.

#### Quais os riscos de não as utilizar?

Sem esse controle, a empresa pode tomar decisões com base em um saldo irreal, o que gera risco de inadimplência, falhas na conciliação bancária e exposição a fraudes ou extravios não identificados. Isso compromete a confiabilidade das informações financeiras e a segurança operacional.

##### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1052441790)

#### Cenário prático e passo a passo para realizar a atividade no sistema

**Contexto:** O **analista financeiro** da **Axis**, realizou o pagamento de uma despesa por meio de cheque. Como o cheque foi entregue ao fornecedor, o compromisso já foi assumido e, por isso, é necessário registrar a baixa do título no sistema. No entanto, como o valor ainda não saiu da conta corrente o banco só debita o valor quando o cheque for compensado, essa baixa será feita em uma conta de controle chamada **Cheque Fornecedor**.

**Tarefa:** No sistema, registre a baixa do título na conta Cheque Fornecedor. Após a compensação do cheque, transfira o valor para a conta corrente. Por fim, verifique o impacto no saldo bancário e confirme se as informações estão corretas na conciliação financeira.

#### Hora de colocar a mão na massa! Realize as movimentações necessárias

1. **Consultar o título financeiro associado ao cheque:**

- Acesse a tela **Movimentação Financeira**
  Menu: Financeiro » Rotinas » Movimentação Financeira
- Filtre por um título de despesa que foi associado a um cheque impresso anteriormente.
- Para validar se o título está de acordo, verifique as informações registradas na aba **Cobrança,** confira os campos: **Nosso número** e **Código de barras.**

2. **Consultar e acompanhar o cheque:**

- Acesse a tela **Histórico de Cheques**
  Menu: Financeiro » Consultas » Histórico de Cheques
- Utilize os filtros para localizar os títulos pagos com cheque.
- Informe no campo **Banda CMC7 ou nº do cheque** o código de barras conferido no título anteriormente.
- Clique no botão **Aplicar** para filtrar os resultados.
- Na seção **Relação de Cheques**, o campo **Status** estará exibindo **"Registrado"** e em **Histórico do cheque nº,** haverá  um evento do tipo **“Recebimento/Emissão”.**

3. **Baixar o título:**

- Acesse a tela **Movimentação Financeira**
  Menu: Financeiro » Rotinas » Movimentação Financeira
- Selecione o título consultado na primeira etapa, em que houve a impressão do cheque.
- Clique em **Baixar título**.
- Na tela de preenchimento de dados para baixa, preencha o campo **Conta** com a conta **“CHEQUE FORNECEDOR”.**
- Clique em **Baixar título.**

4. **Consultar o cheque baixado:**

- Retorne a tela **Histórico de Cheques** e clique em **Aplicar**.
- Na seção **Relação de Cheques**, o campo **Status** está exibindo **“Aguardando depósito”** e em **Histórico do cheque nº**, haverá  um evento do tipo **“Baixa”**.

5. **Registro da compensação (transferência do título financeiro de uma conta a outra):**

- Acesse a tela **Transferência de títulos**
  Menu: Financeiro » Rotinas »Transferência de títulos
- No campo **Filtrar os títulos:** Selecionar a opção **Pendentes**.
- Selecione as opções **Despesas** e **Baixados.**
- No campo Conta bancária: selecione a conta **“Cheque fornecedor”.**
- Em seguida clique no botão **Aplicar**.
- Selecione o cheque e clique no botão “**Selecionar Títulos”.** O título então apresentará na seção de **Títulos Selecionados.**
- Clique no botão **“Confirmar”.**
- Um pop-up de **Conta Bancária deve ser informada** será exibido, onde será necessário preencher os seguintes campos obrigatórios:

**Conta Destino:** Conta da compensação, informe a conta corrente utilizada na emissão do cheque.

**Tipo de Título:** Informe **“Cheque”**

**TOP de Transferência:** Informe a Top **Transferência de Títulos**

**Lançamento Origem:** Transferência de Pagamento.

**Lançamento Destino:** Transferência de Pagamento.

**Histórico:** Transferência de cheque.

- Em seguida clique em **OK**.

6. **Consulta da operação executada:**
   Acesse a tela **Conciliação bancária.**
   Menu: Financeiro » Rotinas »Conciliação Bancária

- Utilize os **Filtros rápidos** para buscar a operação realizada marcando:
- **Pendentes**
- **Receitas**
- **Despesas**
- **Conta:** Informe a conta **“Cheque Fornecedor”**
- Clique em **Aplicar**
- Serão apresentados dois registros, a despesa (que foi baixada no ato de entrega do cheque) e a receita (criada para realizar a compensação com a despesa uma vez que o título foi transferido.)
- Mude o filtro da conta para a **conta corrente** que houve a transferência.
- Clique em **Aplicar**
- Ao aplicar o filtro da **conta corrente**, será exibido o **título de despesa**, refletindo a transferência da despesa para a conta.

#### Correção e Repetição

- Certifique-se de que todos os campos obrigatórios foram preenchidos corretamente, incluindo os dados do cheque, a conta bancária e os parâmetros de impressão.
- Lembre-se de que a baixa deve ser feita na conta “Cheque Fornecedor”.
- Após a transferência, na tela de conciliação, deve haver um registro de despesa na conta corrente e uma despesa e receita de mesmo valor na conta “Cheque Fornecedor”. Isso garante o devido controle da operação.
- Caso o processo não tenha sido concluído conforme esperado, revise as informações e refaça o procedimento, garantindo que os registros estejam alinhados e atualizados.
