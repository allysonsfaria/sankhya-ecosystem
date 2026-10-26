---
id: "360044581414"
titulo: "Procedimento de Cálculo em Rescisões por Regime de Caixa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044581414-Procedimento-de-C%C3%A1lculo-em-Rescis%C3%B5es-por-Regime-de-Caixa"
trilha: "Melhores Práticas > Pessoal+"
atualizado_em: "2026-07-29T13:14:57Z"
rotulos: ["#validado-pelaLorrana: Ass:Roger", "Configuração", "Impostos", "Financeiro", "Rescisão", "Cálculo de IRRF em Rescisões por Regime de Caixa", "IRRF", "Regime de Caixa"]
---

# Procedimento de Cálculo em Rescisões por Regime de Caixa

**Procedimento de Cálculo em Rescisões por Regime de Caixa**

IMPOSTO DE RENDA RETIDO NA FONTE

Imposto de Renda Retido na Fonte (IRRF) é uma obrigação tributária principal em que a pessoa jurídica ou equiparada, está obrigada a reter do beneficiário da renda, o imposto correspondente, nos termos estabelecidos pelo DECRETO Nº 3.000, DE 26 DE MARÇO DE 1999 e pela LEI Nº 7.713, DE 22 DE DEZEMBRO DE 1988, recolhido pelo Governo Brasileiro. Este artigo trata sobre os rendimentos do trabalho assalariado pagos por pessoas físicas ou jurídicas.
Geralmente o IR é calculado por fato Gerador (data de pagamento). O cálculo da Rescisão trata-se do último cálculo do colaborador na referência a ser efetivado. Portanto, para o cálculo do IR, faz-se necessário recompor as bases de IR das folhas que foram pagas dentro da referência da Rescisão, para chegarmos ao valor do desconto. A fórmula para encontrar a base de IR de uma folha é:

**Base IRRF = Base INSS – Valor Desconto INSS – Dependentes IR**

**CASO DE USO**

- Temos um caso de rescisão, realizada na referência **10/2018**, sendo paga dia **31/10.**
- Foi feito um adiantamento no mês **10/2018**, sendo pago dia **20/10.**
- Temos também a Folha Normal da referência 09/2018 que foi paga dia **05/10**.
- Funcionário tem **1 Dependente IR** = **R$ 189,59**

Nesse caso devemos recompor a base de IR dessas três folhas para encontrarmos a Base de Cálculo do IR, para depois chegarmos ao valor do evento 907 - IRRF – RESCISOES. Suponhamos:

**Base IRRF Folha Normal** = 1.300,41
**Dependente IR Folha Normal** = 189,59 \*
**Base IRRF Adiantamento** = 500,00 \*\*
**Base IRRF Rescisões** = 900,00
**Total da Base de Cálculo** = 2.890,00

\* A soma do valor do Dependente da Folha Normal tem que ser feita na Base de Cálculo do IR porque o Dependente é abatido na Base de Cálculo do IR da Rescisão. O valor do Dependente pode ser abatido apenas uma única vez conforme determinação SRF. Se a soma não for feita, o valor é abatido em duplicidade na recomposição de Bases do IR retornando o valor de desconto incorreto.

\*\* A Base IRRF Adiantamento só deve ser considerada na recomposição se o evento de “Desconto de Adiantamento” estiver configurado para as bases 1904 – BASE IRRF FOLHA NORMAL e 1907 – BASE IRRF RESCISÕES. Em Arquivos >> Eventos >> Bases de Cálculo >> IRRF – 1 – IRRF.

Conforme artigo 621 decreto 3000, todo adiantamento que não for pago integralmente no mês (exemplo regime caixa, em que a folha é paga no 5 dia útil), deve ter a retenção de IRRF imediatamente. Dessa forma os clientes que não usam esse recolhimento imediato, precisam rever suas configurações para correto recolhimento.
<http://www.planalto.gov.br/ccivil_03/decreto/D3000.htm>

**Adiantamentos de Rendimentos**

Art. 621. O adiantamento de rendimentos correspondentes a determinado mês não estará sujeito à retenção, desde que os rendimentos sejam integralmente pagos no próprio mês a que se referirem, momento em que serão efetuados o cálculo e a retenção do imposto sobre o total dos rendimentos pagos no mês.
§ 1º Se o adiantamento referir-se a rendimentos que não sejam integralmente pagos no próprio mês, o imposto será calculado de imediato sobre esse adiantamento, ressalvado o rendimento de que trata o art. 638.
§ 2º Para efeito de incidência do imposto, serão considerados adiantamentos quaisquer valores fornecidos ao beneficiário, pessoa física, mesmo a título de empréstimo, quando não haja previsão, cumulativa, de cobrança de encargos financeiros, forma e prazo de pagamento.

Com a Base de Cálculo recomposta, verifica-se a alíquota de acordo com a Tabela IRRF (É fundamental sempre verificar se houve alteração na tabela por parte da Receita Federal).

| **Base de cálculo (R$)** | **Alíquota (%)** | **Parcela a deduzir do IRPF (R$)** |
| --- | --- | --- |
| Até 1.903,98 | - | - |
| De 1.903,99 até 2.826,65 | 7,5 | 142,80 |
| De 2.826,66 até 3.751,05 | 15 | 354,80 |
| De 3.751,06 até 4.664,68 | 22,5 | 636,13 |
| Acima de 4.664,68 | 27,5 | 869,36 |

Fonte: <http://idg.receita.fazenda.gov.br/acesso-rapido/tributos/irpf-imposto-de-renda-pessoa-fisica>

Nesse caso, para a base de 2.890,00 se aplica a alíquota de 15%:

**IR** = 2.890,00 \* 15% = **433,50**

Aplicamos a dedução do IR conforme a Tabela:

**IR Deduzido** = 433,50 – 354,80 = **78,70**

Se houve desconto de IR na folha de pagamento ou no adiantamento, subtrai o valor já descontado para recolher somente a diferença. Se não houve o desconto, o valor do IR RESCISÕES será R$ 78,70. Suponhamos um desconto na Folha Normal 09/2018 no valor de R$ 20,00:

**IR Rescisões** = 78,70 – 20,00 = **58,70 \*\*\***

\*\*\* Esse é o valor do desconto de IR na Rescisão. Se houve desconto do Adiantamento, basta subtrair do valor de 58,70.

As informações desse caso de uso foram colocadas apenas para reproduzir uma situação e para demonstrar o procedimento de cálculo. Deve-se conferir as bases e o valor dos dependentes do caso real na aba “Bases de Cálculo”, na tela de cada tipo de folha (Normal, Adiantamento e Rescisão), para realizar a conferência.
