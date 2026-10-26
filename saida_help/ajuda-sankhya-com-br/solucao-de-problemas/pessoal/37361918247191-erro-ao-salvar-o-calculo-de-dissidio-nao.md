---
id: "37361918247191"
titulo: "Erro ao Salvar o Cálculo de Dissídio: Não Foi Possível Confirmar a Folha de Pagamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37361918247191-Erro-ao-Salvar-o-C%C3%A1lculo-de-Diss%C3%ADdio-N%C3%A3o-Foi-Poss%C3%ADvel-Confirmar-a-Folha-de-Pagamento"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:22:15Z"
rotulos: ["Configuração", "Eventos", "Financeiro", "Folha de Pagamento", "ORA-20101", "Erro", "Cálculo de Dissídio", "Erro ao Salvar o Cálculo de Dissídio", "Plano Odontológico", "convênio médico e odontológico", "não devem receber reajuste por dissídio", "Tem seus valores recalculados"]
---

# Erro ao Salvar o Cálculo de Dissídio: Não Foi Possível Confirmar a Folha de Pagamento

**MENSAGEM:**

Falha ao gravar folha. ORA-20101: Dependente 1 não cadastrado.
ORA-06512: em "SANKHYA.TRG\_INC\_TFPVPS", line 16
ORA-04088: erro durante a execução do gatilho 'SANKHYA.TRG\_INC\_TFPVPS'

![Imagem 1: Falha ao gravar folha. ORA-20101: Dependente 1 não cadastrado. ORA-06512: em "SANKHYA.TRG_INC_TFPVPS", line 16…](https://ajuda.sankhya.com.br/hc/article_attachments/37361852680855)

##### SITUAÇÃO:

Ao realizar o cálculo e tentar salvar a folha de dissídio, o sistema impede a gravação da folha e apresenta a mensagem de erro acima, relacionada à ausência de dependente cadastrado e à execução de um gatilho no banco de dados.

##### SOLUÇÃO:

Para corrigir o problema, siga os passos abaixo:

**(1)** Acesse a tela **''Pessoal+''** (Pessoal+ » Rotinas Folha » Acessos Pessoal Mais).

**(2)** Localize o evento **''Plano Odontológico''** utlizado na folha.

**(3)** Na aba **''Avançado''**, desmarque a opção **''Tem seus valores recalculados''**.

![Imagem 2: (3) Na aba ''Avançado'' , desmarque a opção ''Tem seus valores recalculados'' .](https://ajuda.sankhya.com.br/hc/article_attachments/37450097240855)

**(4)** Salve o evento.

**(5)** Recalcule a folha de dissídio.

**(6)** Salve novamente a folha.

##### Por que eventos de convênio médico e odontológico não devem ser reajustados no dissídio?

##### O dissídio coletivo tem como finalidade reajustar verbas de natureza salarial, como salário base, horas extras, adicionais e outras verbas que compõem a remuneração do colaborador. Já os eventos de convênio médico e odontológico possuem natureza indenizatória ou de desconto, não sendo considerados verbas salariais. Por esse motivo, não devem ser impactados pelo reajuste do dissídio, nem configurados para recálculo nesse processo.

#####

##### CAUSA:

O erro ocorre porque o evento de plano odontológico estava **interferindo no salvamento da folha**, gerando **duplicidade de linhas de desconto** durante o cálculo do dissídio.

Esse comportamento acontece devido à configuração do evento para recalcular valores no dissídio, o que não se aplica a eventos de natureza indenizatória ou de desconto, como convênios odontológicos.
