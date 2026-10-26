---
id: "37729700382743"
titulo: "Como realizar a autorização de pagamentos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37729700382743-Como-realizar-a-autoriza%C3%A7%C3%A3o-de-pagamentos"
trilha: "Universidade Sankhya > Jornada de Pagamentos"
atualizado_em: "2026-07-22T14:08:59Z"
rotulos: ["Configuração", "Movimentação Financeira", "TOP", "Financeiro", "Autorização de Pagamentos"]
---

# Como realizar a autorização de pagamentos

| Categoria |
| --- |
| [O que é o processo de autorização de pagamentos?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37729700382743-Como-realizar-a-autoriza%C3%A7%C3%A3o-de-pagamentos#h_01KF3X7EQ84PPJ502RA78P55NP) |
| [Quais problemas essa prática resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37729700382743-Como-realizar-a-autoriza%C3%A7%C3%A3o-de-pagamentos#h_01KF3X6Z3XTYW2FTT39H5286HY) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37729700382743-Como-realizar-a-autoriza%C3%A7%C3%A3o-de-pagamentos#h_01KF3X6TK0TD4V5SYTMA2FPE6D) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37729700382743-Como-realizar-a-autoriza%C3%A7%C3%A3o-de-pagamentos#h_01KF3X6NJ3DJDKAJV498KW273S) |
| [Agora é a sua vez! Siga o passo a passo e aproveite o máximo do ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37729700382743-Como-realizar-a-autoriza%C3%A7%C3%A3o-de-pagamentos#h_01KF3X65H1KPWDFPNMZYGPB96N) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37729700382743-Como-realizar-a-autoriza%C3%A7%C3%A3o-de-pagamentos#h_01KF3X5PJEP1BAG5KPHYMMNKRN) |

## Autorização de pagamentos

#### O que é o processo de autorização de pagamentos?

Autorização de Pagamentos é o processo que exige aprovação prévia para pagamentos acima de um valor limite configurado.
Garante que apenas usuários autorizados possam liberar valores elevados, protegendo o fluxo de caixa e prevenindo pagamentos indevidos, erros operacionais e fraudes.

#### Quais problemas essa prática resolve?

- **Pagamentos indevidos:** impede que valores sejam pagos sem validação.
- **Fraudes e erros operacionais:** bloqueia liberações não autorizadas.
- **Quebra de políticas internas:** assegura que pagamentos sigam regras da empresa.
- **Falta de rastreabilidade:** gera registros claros para auditoria e controle financeiro.

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1056364770)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** Durante a rotina de pagamentos da **Axis**, chegou o vencimento da fatura mensal do fornecedor de embalagens. O valor da fatura ultrapassa o limite configurado para liberação automática no sistema. Para seguir o processo interno de aprovação, é necessário solicitar a autorização de um gestor financeiro antes de concluir a baixa do título.

**Tarefa:** Acesse a tela de **Movimentação Financeira**, localize um título de despesa pendente com valor acima do limite configurado anteriormente e solicite a autorização de pagamento. Realize a aprovação utilizando o usuário liberador configurado, após a liberação, realize a baixa do título normalmente, garantindo que o pagamento seja registrado de forma correta no controle financeiro.

#### Agora é a sua vez! Siga o passo a passo e aproveite o máximo do ERP Sankhya

1. **Simulação da baixa do pagamento**

- Acesse a tela **Movimentação Financeira**.
  Menu: Financeiro » Rotinas » Movimentação Financeira

**Nos filtros, marque as opções:**

- **Real + Provisão:** Real - (Clique em Aplicar)
- **Receitas + Despesas:** Despesas - (Clique em Aplicar)
- **Pendentes + Baixados:** Pendentes - (Clique em Aplicar)
- Selecione um título com valor de desdobramento superior a **R$ 500,00**, essa informação pode ser verificada na coluna **Vlr. Desdobramento.**
- Clique na opção **Baixar** e observe que o sistema solicita a autorização.
- Clique em **Sim** para definir o liberador.
- Preencha o campo **Liberador** com o usuário configurado anteriormente como liberador e clique em **Concluir**.

2. **Autorização do pagamento**

- Acesse a tela de **Autorização de Pagamentos**.
  Menu: Financeiro » Avançado » Autorização de Pagamentos

**Preencha os seguintes campos:**

- Usuário (usuário liberador)
- Senha
- No campo **Status**, marque a opção “Pendente” e clique em **Aplicar**.
- Atente-se, pois o sistema tentará a liberação de todos os títulos apresentados na grade, é preciso utilizar os botões **“Remove Selecionados”** e **“Remove Não Selecionados”** para manter na tela apenas o título financeiro que será liberado.
- Escolha o título financeiro pendente de autorização no qual houve a tentativa de baixa anteriormente, e clique em  **Autoriza**.
- Preencha o campo **Valor liberado** e em **Observação liberador**, digite **"Autorizado conforme política financeira."**
- Confirme clicando em **OK**.

3. **Baixa após aprovação**

- Retorne à tela de **Movimentação Financeira**.
- Selecione o título que estava pendente de liberação.
- Clique em **Baixar** para concluir o pagamento.

**Ponto de Atenção: Autorização de Pagamentos**

- Durante a realização desta aula, foi necessário configurar um valor mínimo para a autorização de pagamentos na TOP de pagamento, com o objetivo de simular corretamente o processo proposto. No entanto, é importante destacar que essa configuração impacta diretamente outros fluxos financeiros que serão abordados em aulas posteriores.
- Por isso, ao finalizar esta aula, o aluno deve retornar à tela de configuração da TOP utilizada e remover o valor preenchido no campo “**Valor mínimo para Autorização de Pagamento**”. Essa ação é essencial para evitar bloqueios indevidos ou comportamentos inesperados nas próximas etapas do treinamento.

**Fique atento a esse ajuste para garantir a continuidade adequada dos próximos conteúdos e o correto funcionamento do sistema.**

#### Correção e Repetição

- Verifique se o título correto foi selecionado para liberação.
- Após a autorização, a baixa deve ocorrer devidamente na tela Movimentação Financeira.
- Caso não consiga baixar o título, retorne a tela de Autorização de Pagamentos e confirme que foi devidamente liberado.
