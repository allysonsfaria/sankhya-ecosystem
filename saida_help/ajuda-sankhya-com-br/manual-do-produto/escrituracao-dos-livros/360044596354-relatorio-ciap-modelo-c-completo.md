---
id: "360044596354"
titulo: "Relatório CIAP Modelo C (Completo)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596354-Relat%C3%B3rio-CIAP-Modelo-C-Completo"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Apuração e Livros Fiscais > Escrituração dos livros"
atualizado_em: "2026-10-13T16:46:18Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Relatórios", "Livros Fiscais", "Crédito", "br.com.sankhya.mgeliv.rel.relatoriociap", "Relatório CIAP Modelo C (Completo) manual", "ICMS", "Impostos", "Configure \"Empresa\" e \"Período\"; defina opções de impressão", "Inclui identificação do bem e valores de ICMS", "\"Quadro 2\" para base de crédito; \"Quadro 3\" para apuração do crédito"]
---

# Relatório CIAP Modelo C (Completo)

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312923008151) Módulo: Livros Fiscais > Relatórios
```

---

Tem-se nesta tela as configurações pertinentes a geração do relatório CIAP, no qual é feito o controle dos créditos de ICMS de Ativos Imobilizados que pertencem à empresa.

![Imagem 2: Este relatório contempla apenas os bens que forem configurados com fração mensal igual 48 meses.](https://ajuda.sankhya.com.br/hc/article_attachments/25856431210647) Este relatório contempla apenas os bens que forem configurados com fração mensal igual 48 meses. 

![Imagem 3: Este relatório contempla apenas os bens que forem configurados com fração mensal igual 48 meses.](https://ajuda.sankhya.com.br/hc/article_attachments/5409540130327)

Inicialmente, informa-se a **"Empresa"** e o **"Período"** pelos quais se deseja emitir (visualizar ou imprimir) o relatório CIAP.

#### Seção Impressão

A marcação **"Quadro 2"** quando habilitada, indica que será apresentado no relatório o Demonstrativo da Base do Crédito a ser Apropriado.

Ao acionar a marcação **"Quadro 3"**, tem-se no relatório o Demonstrativo da Apuração do Crédito a ser Efetivamente Apropriado.

Através da marcação **"Descrição Abreviada do Bem"** aponta-se que a coluna Descrição será representada pela descrição do bem de forma reduzida. Caso não esteja marcada, a coluna levará a descrição do produto.

O campo **"Página Inicial"** é responsável pela numeração da primeira página do relatório.

#### Seção Gravação dos Dados

O campo **"Última Página"** será preenchido automaticamente com o número da última página do relatório que foi gerado.

É necessário acionar o campo **"Gravar Página"** para que ocorra o preenchimento do campo Última Página.

#### Quadro 2 - Demonstrativo da Base do Crédito a ser Apropriado

Analisaremos agora as informações acerca das colunas contidas no quadro 2.

![Imagem 4: Analisaremos agora as informações acerca das colunas contidas no quadro 2.](https://ajuda.sankhya.com.br/hc/article_attachments/5409569253783)

**Colunas sob o título "Identificação do Bem"**

**Número ou Código:** O número ou código atribuído ao Bem a critério do contribuinte.

**Data:** A data da ocorrência de qualquer movimentação do Bem, tais como, aquisição, transferência, alienação ou baixa pelo curso do prazo de 4 (quatro) anos de utilização.

**Nota Fiscal:** O número do documento fiscal relativo à aquisição ou a outra ocorrência.

**Descrição Resumida:** A identificação do Bem de forma sucinta.

**Colunas sob o título "Valor do ICMS"**

**Entrada (Crédito passível de apropriação):** O valor do imposto passível de apropriação, relativo à aquisição acrescido quando for o caso do ICMS correspondente ao serviço de transporte e ao diferencial de alíquotas, vinculados à aquisição do bem.

**Saída, Baixa ou Perda (Dedução de crédito):** O valor correspondente ao imposto passível de apropriação, relativo à aquisição do bem anteriormente escriturado na coluna Entrada (Crédito passível de apropriação), quando ocorrer a alienação, a transferência, o perecimento, o extravio ou a deterioração do referido bem, ou ainda, quando houver completado o quadriênio de sua utilização.

**Saldo Acumulado (Base do crédito a ser apropriado):** O somatório da coluna Entrada (Crédito passível de apropriação), subtraindo-se desse o somatório da coluna Saída, Baixa ou Perda, cujo resultado no final do período de apuração servirá de base para o cálculo do crédito a ser apropriado.

#### Quadro 3 - Demonstrativo da Apuração do Crédito a ser Efetivamente Apropriado

Tem-se aqui as informações pertinentes as colunas apresentadas no quadro 3.

![Imagem 5: Tem-se aqui as informações pertinentes as colunas apresentadas no quadro 3.](https://ajuda.sankhya.com.br/hc/article_attachments/5409607289111)

**Tributadas e Exportação (1):** O valor das operações e prestações tributadas e de exportação escrituradas no mês.

**Total das Saídas (2):** O valor total das operações e prestações de saídas escrituradas pelo contribuinte no mês.

**Coeficiente de Creditamento (3 = 1 : 2):** O índice de participação das saídas, prestações tributadas e de exportação no total das saídas e prestações escrituradas no mês, encontrado mediante a divisão do valor das saídas, prestações tributadas e de exportação pelo valor total das saídas e prestações, considerando-se no mínimo 4 (quatro) casas decimais.

**Saldo Acumulado  (Base do Crédito a ser Apropriado) (4):** O valor da base do crédito a ser apropriado mensalmente, transcrito da coluna com o mesmo nome do Quadro Demonstrativo da Base do Crédito a ser Apropriado.

**Fração Mensal (5):** O quociente de 1/48 (um quarenta e oito avos).

**Crédito a ser Apropriado (6 = 3 x 4 x 5):** O valor do crédito a ser apropriado, encontrado mediante a multiplicação do coeficiente de creditamento pelo saldo acumulado e pela fração mensal, cujo resultado deve ser escriturado na forma prevista neste Regulamento.

### Parâmetros que influenciam nesta rotina

Ao ativar o parâmetro **“UFs que consideram devoluções de venda no CIAP - UFCONSDEVCIAP”**, o sistema identifica automaticamente quais estados devem considerar as devoluções de venda no cálculo do índice de crédito de ICMS no CIAP.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596354-Relat%C3%B3rio-CIAP-Modelo-C-Completo#top)
