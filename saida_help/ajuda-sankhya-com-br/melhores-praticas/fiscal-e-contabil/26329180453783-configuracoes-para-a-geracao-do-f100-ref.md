---
id: "26329180453783"
titulo: "Configurações para a Geração do F100 referente a Juros, Multa, Desconto e Bonificação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26329180453783-Configura%C3%A7%C3%B5es-para-a-Gera%C3%A7%C3%A3o-do-F100-referente-a-Juros-Multa-Desconto-e-Bonifica%C3%A7%C3%A3o"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:42:33Z"
rotulos: ["Configuração", "Movimentação Financeira", "Impostos", "TOP", "Financeiro", "EFD Contribuições", "Configurações para a Geração do F100", "Juros Multa Desconto e Bonificação"]
---

# Configurações para a Geração do F100 referente a Juros, Multa, Desconto e Bonificação

O registro F100 da EFD-Contribuições é utilizado para detalhar as receitas específicas que não fazem parte da atividade principal da empresa, como receitas financeiras, juros, multas e descontos concedidos ou obtidos.

**1° Passo**

**Essa configuração deve ser feita na TOP de baixa**

Tela **"Tipos de Operação - TOP"**: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

- Aba Impostos: marque os campos **"Tem PIS"** e **"Tem COFINS"**

**Importante**: O financeiro deve estar baixado

**2° Passo**

**Tela "Empresa": Comercial » Preferências » Empresa**

- Aba **"EFD - Escrituração Fiscal Digital"**, sub Aba **"Geração F100"**
- **Observação:** aba **"Geração F100"** será habilitada para utilização somente quando  **"Tipo de Escrituração"** estiver **"EFD Contribuições"**.

![Imagem 1: Observação: aba "Geração F100" será habilitada para utilização somente quando "Tipo de Escrituração" estiver "EFD…](https://ajuda.sankhya.com.br/hc/article_attachments/26329180426647)

**Importante**: a aba Geração F100 permite configurar a geração do

F100 do EFD Contribuições referente juros, descontos e/ou multas recebidos e obtidos respectivamente, que foram destacados em campos próprios da movimentação financeira e que tiveram origem nas baixas de títulos.

Configure a aba Geração F100 de acordo com a necessidade.

**Aba "EFD": Escrituração Fiscal Digital > Sub-Aba Blocos e Registros**

- Marque o Bloco F
- Marque o registro F100

**3° Passo - Juros**

- Campo **"Tributa PIS/COFINS sobre Juros Recebidos de Receitas":** essa marcação deverá ser feita quando necessário tributar (calcular PIS e COFINS)  sobre os juros advindos de receitas;
- **Campo "Data da Operação Juros (Campo 05)":** somente será ativado se a opção Tributa PIS/COFINS sobre Juros Recebidos de Receitas estiver marcada.
- **Selecione uma das opções :**

![Imagem 2: Selecione uma das opções :](https://ajuda.sankhya.com.br/hc/article_attachments/26329180427543)

- **Data da Baixa:** se essa opção for escolhida, o campo 05 será preenchido com a data de baixa registrada na Movimentação Financeira.
- **Último dia do período da escrituração**: se essa opção for selecionada, ao gerar o arquivo, o campo 05 (Data da Operação) será preenchido com a data do último dia do período informado no campo **"Período"** da tela **"EFD-Contribuições"**. Por exemplo, se o período for de 01/04/2022 a 30/04/2022, a data gerada será 30/04/2022.

Configure também os demais campos pertinentes

- **"Cód. da Sit. Tribut. PIS/COFINS Juros"**
- **"Alíquota PIS"**
- **"Alíquota COFINS"**

![Imagem 3: "Alíquota COFINS"](https://ajuda.sankhya.com.br/hc/article_attachments/26329203974423)

**Importante:** após configurar essas opções, os valores serão ‘agrupados’, gerando um total por parceiro para todos os títulos de receita baixados no período de geração do EFD-Contribuições.

**4° Passo - Multa**

- Na aba Geração F100 faça as configurações conforme necessidade.

**Campo "Tributa PIS/COFINS sobre Receitas Obtidos de Multas?"**

Essa marcação deverá ser feita quando necessário tributar (calcular PIS e COFINS)  sobre os multas advindos de receitas.

**Campo "Data da Operação Multa (Campo 05)":** somente será ativado se a opção Tributa PIS/COFINS sobre Juros Recebidos de Receitas estiver marcada.

**Selecionar uma das opções :**

![Imagem 4: Selecionar uma das opções :](https://ajuda.sankhya.com.br/hc/article_attachments/26329180432663)

- **Data da Baixa: s**e essa opção for escolhida, o campo 05 será preenchido com a data de baixa registrada na Movimentação Financeira.
- **Último dia do período da escrituração**: Ao gerar o arquivo, o campo 05 (Data da Operação) será preenchido com a data do último dia do período informado no campo Período da tela EFD-Contribuições. **Ex:** Se o período for de 01/04/2022 a 30/04/2022, a data gerada será 30/04/2022.

Configure também os demais campos pertinentes

- Cód. da Sit. Tribut. PIS/COFINS Multa
- Alíquota PIS
- Alíquota COFINS

![Imagem 5: Alíquota COFINS](https://ajuda.sankhya.com.br/hc/article_attachments/26329180435223)

**5° Passo - Descontos**

- **Campo "Tributa PIS/COFINS sobre Descontos Obtidos de Despesas":** quando realizada esta marcação tem-se a tributação dos impostos PIS e COFINS sobre os descontos correspondentes às despesas.
- **Campo "Origem dos Descontos":** será habilitado quando a marcação Tributa PIS/COFINS sobre Descontos Obtidos de Despesas estiver efetuada.

As opções de Origem dos Descontos são:

![Imagem 6: As opções de Origem dos Descontos são:](https://ajuda.sankhya.com.br/hc/article_attachments/26329203977879)

- **Todos:** com essa opção o sistema irá considerar os descontos com origem Estoque, Financeiro e Pessoal na geração do F100.
- **Estoque e Financeiro:** selecionando essa opção, serão considerados apenas os descontos de origem Estoque e Financeiro na geração do F100.

**6° Passo - Bonificações**

- **Campo "Tributa PIS/COFINS sobre Aquisições em Bonificações":** com essa marcação, o Registro F100 será gerado com os valores de PIS/COFINS considerando as Aquisições Bonificadas, e/ou caso existam notas bonificadas com as CFOP's 1910 e/ou 2910.

**Nota:** se houver mais de uma Nota Fiscal de Bonificação, o sistema irá gerar apenas uma linha para o Registro F100 agrupando os documentos.

**Exemplo:** no exemplo, a geração foi configurada para gerar Juros obtidos na baixa de financeiro de receita com juros.

Título na movimentação Financeira

- Receita
- Baixado
- Juros auferidos

![Imagem 7: Juros auferidos](https://ajuda.sankhya.com.br/hc/article_attachments/26329180442263)

![Imagem 8: Juros auferidos](https://ajuda.sankhya.com.br/hc/article_attachments/26329203982359)

**No cadastro da TOP**

- Aba **"Impostos"** marque Tem PIS e Tem COFINS

![Imagem 9: Aba "Impostos" marque Tem PIS e Tem COFINS](https://ajuda.sankhya.com.br/hc/article_attachments/26329180446743)

Nas preferências da Empresa, aba EFD - Escrituração Fiscal Digital**,** tipo de Escrituração: EFD Contribuições

- Sub-Aba Geração F100: configurada os campos para geração do F100 para juros.

![Imagem 10: Sub-Aba Geração F100: configurada os campos para geração do F100 para juros.](https://ajuda.sankhya.com.br/hc/article_attachments/26329180448535)

**Dica Extra:**

**Não** depende das TOP´s estar configuradas para gerar livro;

**Não** depende de ter configuração de PIS e COFINS na natureza usada no financeiro.
