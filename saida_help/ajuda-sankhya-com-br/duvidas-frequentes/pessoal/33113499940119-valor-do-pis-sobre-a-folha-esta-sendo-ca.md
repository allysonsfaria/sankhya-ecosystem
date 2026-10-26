---
id: "33113499940119"
titulo: "Valor do PIS sobre a folha está sendo calculado em duplicidade no resumo da folha. O que fazer?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33113499940119-Valor-do-PIS-sobre-a-folha-est%C3%A1-sendo-calculado-em-duplicidade-no-resumo-da-folha-O-que-fazer"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:26:55Z"
rotulos: ["Configuração", "Relatórios", "PIS", "Impostos", "Folha", "soma duplicada da base", "duplicidade", "cálculo do PIS", "Valor do PIS sobre a folha", "calculado em duplicidade", "no resumo da folha", "Erro"]
---

# Valor do PIS sobre a folha está sendo calculado em duplicidade no resumo da folha. O que fazer?

**SITUAÇÃO**

Ao emitir o resumo da folha, é identificado que o valor do PIS sobre a folha está sendo calculado em duplicidade.

**SOLUÇÃO**

**(1)** Verifique qual dos eventos **"Base PIS PASEP Mensal"** é o **evento padrão do sistema Sankhya**, que deverá ser mantido em uso.

**(2)** No evento que será mantido, remova a identificação **"20 - Base PIS PASEP"** dos demais eventos para evitar conflitos e duplicidades.

**(3)** Desative o evento de base que não será utilizado, garantindo que apenas um evento esteja ativo com essa função.

**(4)** Feito os ajustes, emita um novo resumo da folha de pagamento para validar a correção e confirmar que a base de cálculo do PIS está sendo considerada corretamente.

**Exemplo:**

- Base de cálculo do PIS: R$ 10.016,89
- Valor devido PIS sobre Folha (1%): R$ 100,16

[**Saiba mais sobre a rotina PIS sobre a folha de pagamento!**](https://ajuda.sankhya.com.br/hc/pt-br/articles/28240000315543-PIS-sobre-a-folha-de-pagamento)

**CAUSA**

A duplicidade na base de cálculo do PIS sobre a folha ocorre devido à presença simultânea de dois eventos **Base PIS PASEP Mensal** ativos, ambos com a mesma identificação ''**20 - Base PIS PASEP''**. Além disso, esses eventos estão vinculados aos mesmos eventos de cálculo, o que resulta na **soma duplicada da base** durante a geração do resumo da folha.
