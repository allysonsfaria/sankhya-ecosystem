---
id: "10652510565015"
titulo: "e-Social faz apuração do IRRF?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10652510565015-e-Social-faz-apura%C3%A7%C3%A3o-do-IRRF"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-22T15:02:58Z"
rotulos: ["Configuração", "Central de Vendas", "Impostos", "eSocial", "Base de Cálculo do IRRF", "Evento S-5002: Totalização", "Classificação e Tabela 21 do eSocial", "IRRF"]
---

# e-Social faz apuração do IRRF?

**(1)** Conforme MOS o esocial terá o evento S-5002 – Imposto de Renda Retido na Fonte que apenas faz a totalização da base de cálculo de cada trabalhador utilizando as informações de valores do evento de
pagamentos (S-1210) e também informações de valores dos eventos remuneratórios (S-1200, S-1202, S-1207, S2299 e S-2399) que tenham sido referenciados no evento de pagamentos, conforme as classificações utilizadas nas rubricas por tipo, conforme definido no campo {tpValor} do grupo [basesIrrf], correlacionado com a “Tabela 21 – Códigos de Incidência Tributária da Rubrica para o IRRF” do eSocial.

**(1)** O eSocial, diferentemente do que faz em relação à contribuição previdenciária, não efetua
cálculo do valor devido e apenas consolida o valor informado pelo declarante como efetivamente
retido a título de Imposto de Renda. Esse valor é apurado através das rubricas cujo {codIncIRRF} seja
igual a [31, 32, 33, 34, 35].

[20210903 Minuta NDE 01 - eSocial S-1\_0 - IR sobre Rendimentos do Trabalho (www.gov.br)](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/20210903-minuta-nde-01-esocial-s-1_0-ir-sobre-rendimentos-do-trabalho.pdf)

![Imagem 1: 20210903 Minuta NDE 01 - eSocial S-1_0 - IR sobre Rendimentos do Trabalho (www.gov.br)](https://ajuda.sankhya.com.br/attachments/token/XQgnFqOlmaWQnRDSvqDOfqSZG/?name=image.png)

**(1)** Sendo assim, se faz importante os eventos de ter sua classificação de IRRF feito corretamente de acordo com Tabela 21 – Códigos de Incidência Tributária da Rubrica para o IRRF” do esocial, para que haja o desconto correto no cálculo e, assim, tenha os seus valores de Base e Desconto de IRRF informados corretamente ao esocial.
