---
id: "38000455453207"
titulo: "O que é PIS, COFINS e CSLL retidos? É possível reter somente na primeira parcela?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38000455453207-O-que-%C3%A9-PIS-COFINS-e-CSLL-retidos-%C3%89-poss%C3%ADvel-reter-somente-na-primeira-parcela"
trilha: "Universidade Sankhya > Jornada Fiscal "
atualizado_em: "2026-07-22T14:02:48Z"
rotulos: ["Configuração", "COFINS", "PIS", "CSLL", "Impostos", "Financeiro", "Artigo atualizado KCS", "Fiscal/Contábil - KCS", "Retenção na Fonte"]
---

# O que é PIS, COFINS e CSLL retidos? É possível reter somente na primeira parcela?

### O que é PIS, COFINS e CSLL retidos?

PIS, COFINS e CSLL retidos correspondem à retenção na fonte dessas contribuições sobre determinados serviços prestados. A empresa contratante retém 4,65% do valor bruto da nota (0,65% de PIS, 3% de COFINS e 1% de CSLL) e recolhe o valor à Receita Federal. Empresas do Simples Nacional, pessoas físicas e algumas atividades específicas podem ser dispensadas dessa retenção. O valor retido pode ser compensado pela empresa prestadora em obrigações fiscais futuras.

### Como configurar retenção de PIS, COFINS e CSLL na primeira parcela?

Quando há serviços tomados com retenções de **"PIS"**, **"COFINS"** e **"CSLL"**, o sistema realiza o cálculo dessas retenções no momento da baixa do título.

Por padrão, quando um título é parcelado e há múltiplas baixas parciais, o sistema rateia as retenções proporcionalmente entre todas as parcelas.

Atualmente, o sistema não possui tratativa nativa para concentrar a retenção apenas na primeira parcela, mas existe uma solução paliativa utilizando a opção **"Destaca Imposto na Baixa"** em conjunto com o **"Valor Mínimo"** no Cadastro de Impostos.

### Solução de contorno para retenção na primeira parcela

Para que as retenções sejam concentradas na primeira baixa, siga os passos abaixo:

**(1)** Acesse a tela **"Impostos"** (Comercial >> Configuração >> Cadastros >> Impostos).
**(2)** Localize os impostos de **"PIS"**, **"COFINS"** e **"CSLL"** que deseja configurar.
**(3)** No campo **"Destaque do Imposto"**, selecione a opção **"Destaca Imposto na Baixa"**.
**(4)** Configure o campo **"Valor Mínimo"** com um valor que seja inferior ao total de impostos calculado, mas superior ao valor das parcelas subsequentes.
**(5)** Salve as configurações.

### Exemplo prático de ajuste

Se uma nota fiscal possui R$ 1.000,00 de retenção total e será paga em 3 parcelas (ex: R$ 500,00, R$ 300,00 e R$ 200,00), configure o **"Valor Mínimo"** como R$ 250,00. Assim, apenas a primeira parcela terá a retenção aplicada. Caso o valor da primeira baixa seja inferior ao total dos impostos, o sistema impedirá a operação.

### Quais problemas empresariais são resolvidos pela configuração no ERP Sankhya?

- **Risco de cálculos incorretos:** Processos manuais geram erros na base de cálculo e alíquotas de retenção;
- **Desconformidade fiscal:** Alto risco de não conformidade legal, gerando multas e autuações;
- **Perda de controle:** Falta de controle e rastreabilidade sobre os valores retidos na fonte;
- **Dificuldade na compensação:** Problemas na apuração e compensação futura dos tributos retidos;
- **Ineficiência gerencial:** Gestão fiscal ineficiente devido à falta de dados automatizados.

###
