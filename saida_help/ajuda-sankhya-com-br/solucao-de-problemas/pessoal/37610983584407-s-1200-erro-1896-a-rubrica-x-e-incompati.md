---
id: "37610983584407"
titulo: "S-1200 | Erro 1896 - A Rubrica ‘X’ é incompatível com a categoria ‘X’ do trabalhador."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37610983584407-S-1200-Erro-1896-A-Rubrica-X-%C3%A9-incompat%C3%ADvel-com-a-categoria-X-do-trabalhador"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-08-18T19:55:24Z"
rotulos: ["Impostos", "Folha", "S-1200", "eSocial", "Configuração Funcionários", "Erro", "Pagamento de PLR", "Rubrica possui incidência de IRRF", "A Rubrica ‘X’ é incompatível", "Diretor não empregado", "Central de Projetos"]
---

# S-1200 | Erro 1896 - A Rubrica ‘X’ é incompatível com a categoria ‘X’ do trabalhador.

**MENSAGEM**:

**Erro 1896 - A Rubrica ‘X’ é incompatível com a categoria 901 do trabalhador.**

Ação Sugerida: Rubricas de incidência de IRRF iguais a [14, 34, 54, 94, 9024, 9034, 9054, 9834] só são aceitas para categorias do grupo de Empregado [1XX].

Elemento: /eSocial/evtRemun/dmDev[2]/infoPerApur/ideEstabLot/remunPerApur/itensRemun[2]/codRubr

**SITUAÇÃO:**

Ao enviar S-1200 dos funcionários que possuem pagamento de PLR é apresentado a mensagem de erro acima.

**SOLUÇÃO:**

Quando o pagamento for destinado a **diretor não empregado (categoria 722)**, é necessário utilizar **uma rubrica diferente**, com **incidência de IRRF compatível** com essa categoria.

As rubricas de **PLR**, que possuem **CodIncIRRF 14 – PLR**, são aceitas somente para trabalhadores do **grupo de empregados (1XX)**. Por esse motivo, ao utilizar esse tipo de rubrica para contribuintes individuais, o eSocial rejeita o envio da informação.

Nesses casos, ajuste o cadastro da rubrica e, após a correção, **reenvie o evento S-1200** ao eSocial.

![Imagem 1: Nesses casos, ajuste o cadastro da rubrica e, após a correção, reenvie o evento S-1200 ao eSocial.](https://ajuda.sankhya.com.br/hc/article_attachments/37647172687767)

**CAUSA:**

O erro ocorre porque a **rubrica utilizada possui incidência de IRRF permitida apenas para trabalhadores do grupo Empregados (1XX)**, conforme as regras do leiaute do eSocial.

De acordo com o leiaute, **eventos de PLR não podem ser informados para categorias que não pertencem ao grupo de empregados**, motivo pelo qual o eSocial rejeita o envio da informação para a categoria informada.
