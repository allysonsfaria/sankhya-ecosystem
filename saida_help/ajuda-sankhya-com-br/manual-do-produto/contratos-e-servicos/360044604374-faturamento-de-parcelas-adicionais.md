---
id: "360044604374"
titulo: "Faturamento de Parcelas Adicionais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604374-Faturamento-de-Parcelas-Adicionais"
trilha: "Manual do Produto > Contratos e Serviços > Contratos e Serviços"
atualizado_em: "2026-07-29T14:03:39Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Contratos", "Faturamento", "Contrato", "Faturamento de Parcelas Adicionais", "PARCELASADIC", "br.com.sankhya.mgeos.faturamento.parc.adicionais", "Faturamento de Parcelas Adicionais  manual", "TOP", "Financeiro", "Faturamento de Parcelas Adicionais: Flexibilidade Contratual"]
---

# Faturamento de Parcelas Adicionais

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42311194352791) Módulo: Contratos e Serviços > Rotinas > Faturamento de Parcelas Adicionais
```

---

O comportamento desta tela é semelhante ao da tela de Faturamento de Contrato. Através dela você poderá faturar parcelas adicionais como 13º salário, parcelas semestrais e entre outras parcelas configuradas na tela de [Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774).

![Imagem 2: O comportamento desta tela é semelhante ao da tela de Faturamento de Contrato . Através dela você poderá faturar…](https://ajuda.sankhya.com.br/hc/article_attachments/9295473365911)

Como, por exemplo, uma empresa que presta serviços e cobra uma mensalidade no valor de R$ 200,00 não consegue cobrar 13º salário com o comportamento normal do faturamento de contratos. No entanto, utilizando o recurso de **"Parcela Adicional"**, o usuário poderá configurar no **"Contrato"** a cobrança dessa parcela.

![Imagem 3: Não é possível calcular o ISS de parcelas adicionais nessa tela.](https://ajuda.sankhya.com.br/hc/article_attachments/26638751472279) Não é possível calcular o ISS de parcelas adicionais nessa tela.

Os dados são configurados na aba [Parcela Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos#abaparcelaadicional) do **"Contrato"** a receber a cobrança e a parcela será cobrada de acordo com a periodicidade da cobrança. Esta aba é habilitada através do parâmetro **"Trabalha com parcelas adicionais em contratos? - PARCELASADIC"**.

![Imagem 4: Os dados são configurados na aba Parcela Adicional do " Contrato" a receber a cobrança e a parcela será cobrada de…](https://ajuda.sankhya.com.br/hc/article_attachments/9295647886487)

Cada cabeçalho apresentado na aba Parcela Adicional do **"Contrato"**, será referente a uma nota’ que deve ser emitida conforme as configurações do cabeçalho. Devem-se faturar apenas as parcelas que estejam marcadas como **"Ativo"** na aba Parcela Adicional.

Quando são geradas movimentações a partir destas parcelas adicionais, estas parcelas não poderão ser **"Excluídas"** devido à ligação das tabelas.

## Exemplo

Na tela realize os filtros necessários para a localização das parcelas que serão faturadas. Logo após, basta selecionar a parcela desejada e clicar no botão **"Faturar"**.

Neste exemplo os filtros realizados foram:

- Tipo de operação: 67
- Tipo de título: 1
- Tipo de negociação: 2
- Data para referência: 01/06/2011

Ao clicar em faturar, será apresentada a seguinte mensagem:

**"Gerar fatura para Parcelas Adicionais?"**

Deste modo, ao realizar a confirmação será apresentada uma mensagem informando a quantidade de faturas geradas.

## Nunca incluir confirmada

No cadastro do Tipo de Operação – TOP em sua aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), existe o campo **"Nunca incluir confirmada"** que influencia no faturamento de parcelas adicionais. Quando estiver habilitada, as notas precisaram ser confirmadas após o faturamento. Se desmarcada, serão geradas notas já confirmadas.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604374-Faturamento-de-Parcelas-Adicionais#top)
