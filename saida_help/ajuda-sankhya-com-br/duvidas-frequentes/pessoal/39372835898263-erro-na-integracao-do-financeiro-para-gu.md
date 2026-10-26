---
id: "39372835898263"
titulo: "Erro na integração do financeiro para guia FGTS término de contrato - Base maior que o cálculo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39372835898263-Erro-na-integra%C3%A7%C3%A3o-do-financeiro-para-guia-FGTS-t%C3%A9rmino-de-contrato-Base-maior-que-o-c%C3%A1lculo"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:29:18Z"
rotulos: ["Integração", "Financeiro", "Rescisão", "13º Salário", "FGTS", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Erro na integração do financeiro para guia FGTS término de contrato - Base maior que o cálculo

**MENSAGEM**

A base de FGTS apresentada na integração com o financeiro está com valor maior do que o calculado na tela de cálculos da rescisão e na guia extraída do FGTS Digital.

**SITUAÇÃO**

Ao gerar a **"Guia de Recolhimento Rescisório do FGTS"** referente ao término de contrato, os valores apresentados na tela de cálculos da rescisão estão corretos e correspondem aos valores da guia extraída do FGTS Digital. Porém, ao realizar a integração com o financeiro, a base de FGTS aparece com valor superior ao esperado, gerando divergência nos valores a serem provisionados.

**SOLUÇÃO**

**(1)** Verifique se o funcionário possui uma folha de **13º Salário** calculada na mesma referência da rescisão.

Para isso, acesse a tela **Gerenciador de Folhas** (Pessoal+ » Rotinas Folha » Gerenciador de Folhas) e consulte se existe uma folha de **13º Salário** calculada para a mesma competência da rescisão. Caso exista, valide se essa folha está correta, pois ela pode impactar o cálculo da rescisão.

**(2)** Confirme se há eventos de **"13º Salário - 2ª Parcela"** ou **"Diferença de 13º Salário"** na rescisão. Esses valores são somados na base da **"Guia de Recolhimento Rescisório do FGTS"**, o que pode gerar a diferença observada.

**(3)** Valide os valores apresentados no **"Demonstrativo de Recolhimento FGTS Rescisório"**, especialmente o **"Campo 26 - Mês Rescisão"** e o **"Campo 31 - FGTS do Mês da Rescisão"**. Esses campos devem refletir corretamente a soma das bases de FGTS do mês da rescisão e do 13º salário, quando aplicável.

**(1)** **Ponto de atenção:** caso o funcionário já tenha recebido a **1ª parcela do 13º salário** ou tenha realizado a **antecipação do 13º salário**, e o valor pago seja superior ao valor devido na rescisão, o sistema deverá calcular o evento **DESC. 1ª PARC. 13º BASE FGTS MENSAL** como desconto na folha rescisória.

Esse desconto é necessário para ajustar a base de cálculo do FGTS da rescisão, garantindo que o valor do FGTS seja apurado corretamente e evitando recolhimentos indevidos.

**CAUSA**

A divergência ocorre porque o funcionário possui **"13º Salário"** calculado na mesma referência da rescisão. A **"Guia de Recolhimento Rescisório do FGTS"** soma automaticamente a base de FGTS da rescisão com a base de FGTS do 13º salário, resultando em um valor maior na integração com o financeiro. Este comportamento está correto conforme a legislação trabalhista, que determina o recolhimento do FGTS sobre ambas as verbas quando pagas no mesmo período.
