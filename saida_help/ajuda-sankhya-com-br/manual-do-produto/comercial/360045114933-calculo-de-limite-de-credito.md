---
id: "360045114933"
titulo: "Cálculo de Limite de Crédito"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114933-C%C3%A1lculo-de-Limite-de-Cr%C3%A9dito"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:32:41Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Parceiro", "Crédito", "Financeiro", "Cálculo de crédito", "Cálculo de Limite de Crédito", "Configurações de crédito", "Liberação de limite de crédito", "Limite", "Limite de crédito", "br.com.sankhya.mgecom.rot.calculolimitecredito", "Cálculo de Limite de Crédito manual", "Análise de Crédito", "Configuração e Cálculo", "Análise Automática", "Limite de Crédito"]
---

# Cálculo de Limite de Crédito

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312094606999) Módulo: Comercial > Rotinas > Análise de Crédito
```

---

Esta tela permite que seja definida as regras para a análise automática de crédito dos parceiros, incluindo a sugestão do limite de crédito a ser concedido por meio de uma fórmula configurável.

![Imagem 2: Esta tela permite que seja definida as regras para a análise automática de crédito dos parceiros , incluindo a sugestão…](https://ajuda.sankhya.com.br/hc/article_attachments/21979698054039)

Nesta tela, pode-se incluir informações do balanço ou balancete de seus clientes como: patrimônio líquido, direitos, obrigações, caixa, endividamento e outros. Além dos resultados de consulta, junto aos órgãos de proteção ao crédito e dados oriundos do próprio Financeiro e/ou Comercial como, volume médio de compras, histórico de pagamentos, atraso médio, perfil de parceiro e demais. Para compor um método de análise de crédito confiável, que norteie a decisão dos gestores de cobrança.

Pode-se estabelecer nesta tela, grupos de clientes que estarão sujeitos à análise de crédito de tipos diferenciados, como, por exemplo:

- Parceiros de um determinado segmento (comércio, indústria) que poderão ter uma análise de crédito baseada em uma análise de balanço, uma avaliação do SERASA, um histórico de compras, entre outros.
- Parceiros pessoa física, que poderão ser avaliados pela declaração de imposto de renda, propriedade de imóveis, carteira de trabalho, entre outros.
- Parceiros públicos (governos, prefeituras), que poderão ser avaliados pelo histórico de relacionamento, nível médio de atraso, entre outros.

Na tela [Configurações para Análise de Crédito](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115693-Configura%C3%A7%C3%B5es-para-An%C3%A1lise-de-Cr%C3%A9dito), deve-se montar as definições que serão utilizadas para realizar o cálculo da análise de crédito.

![Imagem 3: Na tela Configurações para Análise de Crédito , deve-se montar as definições que serão utilizadas para realizar o…](https://ajuda.sankhya.com.br/hc/article_attachments/21980067388951)

**Observação:** na tela Cálculo de Limite de Crédito, realizam-se os cálculos propriamente ditos.

O cálculo da análise de crédito é feito baseado em parâmetros configurados e, após o cálculo é possível atualizar automaticamente, no [Cadastro do Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros) os campos **"Limite de Crédito"** e **"Limite de Crédito Mensal"**; o processo de efetivação do limite calculado pode ser feito manualmente; esta possibilidade depende da marcação **"Efetiva Lim. Créd. Calc. automaticamente?"** que fica na aba [Crédito](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abacrdito) do Cadastro de Parceiros.

Após a Configuração da Análise de Crédito, deverá se configurar no Cadastro de Parceiros, aba Crédito, o campo **"Fórm. p/Cálculo Lim. Crédito"**.

Depois, na tela Cálculo de Limite de Crédito, deve-se criar um filtro para encontrar o(s) parceiro(s) e depois clicar em **"**Aplicar". Ao selecionar um parceiro, o sistema carregará as grades inferiores.

Caso existam informações do tipo **"Valor"** ou **"Lista"**, deve-se dar um duplo clique na linha e digitar o Valor ou selecionar a opção da Lista, e depois clicar no botão **"Confirmar Valor/Lista"** para salvar o que foi digitado/escolhido.

Após informar os parâmetros solicitados para o campo Valor e Lista e confirmá-los, pode-se clicar no botão ![Imagem 4: Após informar os parâmetros solicitados para o campo Valor e Lista e confirmá-los , pode-se clicar no botão "Calcular…](https://ajuda.sankhya.com.br/hc/article_attachments/21981225294743) **"Calcular p/ Todos"**.

Após feito o cálculo, se a marcação Efetiva Lim. Créd. Calc. automaticamente? do Cadastro de Parceiros estiver realizada, o sistema fará automaticamente a efetivação do crédito para o parceiro, fazendo a alteração nos campos Limite de Crédito e Limite de Crédito Mensal.

Se a marcação Efetiva Lim. Créd. Calc. automaticamente? não estiver selecionada, o sistema fará o cálculo e pode-se verificar os valores calculados na aba Limite Crédito Calculados, podendo informar um valor inferior ou superior nos campos: Limite de Crédito e Lim. Créd. Mensal. Após informado, é necessário clicar no botão **"Efetivar Limite"** para que o limite de crédito seja atualizado também na aba Crédito do Cadastro de Parceiros. Caso não seja informado os campos Limite de Crédito e Lim. Créd. Mensal, o sistema efetivará com os valores dos limites calculados através das fórmulas.

Sobre limite de crédito sugerido e limite de crédito efetivo, tem-se que o valor do crédito sugerido pela equação poderá ser acatado pelo gestor de crédito ou poderá haver mudança, baseada em critérios estabelecidos pelo gestor. Se desejar estabelecer um limite de crédito diferente do sugerido, tem-se de justificar sua opção no campo **"Observação"** e o sistema registrará todos os eventos como, limite sugerido, limite efetivo e justificativa para futuras consultas.

A historicidade dos limites de créditos sugeridos, concedidos, justificados e de todas as informações que compõem a formação do cálculo do crédito, permitirá fazer análises da evolução da situação de crédito do parceiro ao longo do tempo e fazer auditorias sobre os critérios de concessão de crédito adotados pela empresa.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114933-C%C3%A1lculo-de-Limite-de-Cr%C3%A9dito#top)
