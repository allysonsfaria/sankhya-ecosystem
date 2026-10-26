---
id: "25611476176663"
titulo: "Dedução de ICMS da base de PIS/COFINS em TOP do tipo de movimento Financeiro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25611476176663-Dedu%C3%A7%C3%A3o-de-ICMS-da-base-de-PIS-COFINS-em-TOP-do-tipo-de-movimento-Financeiro"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:45:11Z"
rotulos: ["Configuração", "ICMS", "Impostos", "TOP", "Financeiro", "Movimentação financeira", "Top do tipo movimentação financeira", "Dedução Pis/Cofins do valor do ICMS em CT-E Mov. Financeira", "Dedução de ICMS PIS/COFINS TOP tipo movimento Financeiro", "Ao acionar a marcação \"Deduzir valor do ICMS na BC do PIS e COFINS\"", "Artigo atualizado KCS", "PIS/COFINS", "Financeiro - KCS"]
---

# Dedução de ICMS da base de PIS/COFINS em TOP do tipo de movimento Financeiro

Dentro da TOP, na aba **"Impostos",** ao acionar a marcação **"Deduzir valor do ICMS na BC do PIS e COFINS"**, com o **Tipo de movimento** definido como **"I-Financeiro"**, o sistema procederá à dedução do valor de ICMS da base de cálculo do PIS e COFINS, no entanto, para que isso ocorra realize a seguinte configuração:

- A marcação **"Calcula PIS/COFINS por percentual das notas"**da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), desta tela e a **"Calcula PIS e Cofins na confirmação do financeiro"**das preferências da [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades), devem estar desmarcadas;
- O título deve conter valor de ICMS, se não o sistema considerará o valor do desdobramento do título para cálculo de PIS/COFINS;
- O cálculo é aplicado tanto para receitas e despesas quanto para títulos de origem financeira ou de estoque.

A marcação Deduzir valor do ICMS na BC do PIS e COFINS? só deverá ser selecionada na TOP, caso o campo Deduzir valor do ICMS na BC do PIS e COFINS? estiver indicado com a opção **"Configurado pela TOP"** na tela Preferências da Empresa, aba Propriedades.

A opção Deduzir valor do ICMS na BC do PIS e COFINS, não pode ser usada em conjunto com a opção Calcula PIS/COFINS por percentual das notas encontrada na aba Geral.

**Observação:**ao selecionar essa marcação e efetuar um novo lançamento de nota, o sistema irá subtrair da Base de Cálculo de PIS/COFINS o valor referente ao cálculo de ICMS.

Caso a marcação Calcula PIS/COFINS por percentual das notas da aba Geral, desta tela e a Calcula PIS e Cofins na confirmação do financeiro das preferências da Empresa, aba Propriedades estiverem marcadas e o Tipo de movimento igual a I-Financeiro o sistema realiza um cálculo proporcional considerando o valor de cada item da nota em relação ao valor total da mesma.

Em outras palavras, verifica-se a porcentagem que o valor de cada item representa em relação ao valor total da nota. Posteriormente, esse percentual será aplicado sobre o valor do título para proporcionar o ajuste correspondente.
