---
id: "35787549433495"
titulo: "Advertência 1989 - Rubrica de desconto informada sem parcela prevista"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35787549433495-Advert%C3%AAncia-1989-Rubrica-de-desconto-informada-sem-parcela-prevista"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:21:03Z"
rotulos: ["Durante o envio dos eventos de remuneração \"S-1200\" \"S-2299\" ou \"S-2399", "foi informado desconto de empréstimo consignado para o trabalhador", "Advertência 1989", "Rubrica de desconto informada sem parcela prevista", "porém não há parcela registrada no Portal Emprega Brasil para a competência", "Artigo atualizado KCS", "Sankhya RH - KCS"]
---

# Advertência 1989 - Rubrica de desconto informada sem parcela prevista

| **Módulo:** Pessoal+ » Rotinas Folha » Central do eSocial |
| --- |

**SITUAÇÃO**

Ao tentar enviar os eventos de remuneração **"S-1200"**, **"S-2299"** ou **"S-2399"** para o eSocial, o sistema apresenta a advertência 1988. Ela indica que foi informado desconto de empréstimo consignado para o trabalhador, porém não há parcela registrada no Portal Emprega Brasil para a competência informada.

**SOLUÇÃO**

Para resolver a advertência 1988, siga os passos abaixo:

**(1)**  Exclua o cálculo da folha de pagamento do trabalhador.

**(2)**  Remova o lançamento do movimento referente ao desconto de empréstimo consignado (**"rubrica 9253"**).

**(3)**  Confirme se os dados do contrato de empréstimo consignado estão corretos (valor da parcela, código da instituição financeira e número do contrato).

**(4)**  Recalcule a folha do funcionário.

**(4)**  No **"Gerenciador de Folhas"** (Pessoal+ » Rotinas Folha » Gerenciador de Folhas), libere a folha para o eSocial.

**(5)**  Acesse a **"Central do eSocial"** (Pessoal+ » Rotinas Folha » Central do eSocial), gere novamente o evento de remuneração e efetue o envio.

**(6)**  Após o ajuste, o evento de remuneração deverá ser recepcionado com sucesso pelo eSocial, sem a advertência.

**CAUSA**

A advertência 1988 ocorre quando o empregador informa um desconto de empréstimo consignado (**"rubrica 9253"**), mas não há parcela correspondente registrada no Portal Emprega Brasil para a competência informada, ou quando ocorrem divergências nos valores e dados do contrato.
