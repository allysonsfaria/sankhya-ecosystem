---
id: "360044596874"
titulo: "Outros Impostos com Base Mensal Considerando Raiz do CNPJ "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596874-Outros-Impostos-com-Base-Mensal-Considerando-Raiz-do-CNPJ"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:45:39Z"
rotulos: ["Configuração", "CNPJ", "Parceiro", "Matriz", "Filial", "LEI10833RECEB", "Outros Impostos com Base Mensal Considerando Raiz do CNPJ", "Retido", "Retroativo", "Outros Impostos com Base Mensal Considerando Raiz do CNPJ  manual", "Impostos", "Financeiro", "Configuração e Cálculo de Impostos de Base Mensal"]
---

# Outros Impostos com Base Mensal Considerando Raiz do CNPJ 

Em casos de lançamentos de compra e venda de serviços, para parceiros com a mesma raiz do CNPJ. 

O cálculo do imposto de Base Mensal pode ser feito no momento do faturamento da nota ou no momento da baixa.

Primeiramente, para utilizar esta funcionalidade é necessário verificar a configuração dos parâmetros abaixo:

- **Calcular Imposto c/Base Mensal na Nota? -  CALCMENSALNOTA:** se habilitado, os impostos com base mensal serão retidos na Nota, e o valor líquido do Título irá para o Financeiro. Se o parâmetro estiver desligado, mesmo que a TOP esteja configurada na aba [Outros Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaoutrosimpostos) para um imposto com **"Base Mensal"**, o cálculo não será feito na Nota. Esta situação do parâmetro desligado é importante quando a retenção dos Outros Impostos com Base Mensal for feita na baixa do financeiro, pois neste caso o financeiro deverá estar bruto.
- **Calc. Imp. de Base Mensal p/ Receitas no Financeiro - CALCMENSALREC:** quando ligado considerará para efeito de retenção de impostos de Base Mensal no financeiro os títulos de receita (o padrão serve apenas para despesas). É importante que o valor do financeiro esteja bruto.

Em seguida, acesse a tela [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834). Por ser um imposto de Base Mensal, deve-se acionar a marcação de **"Calcular com Base Mensal"**, informar um **"Vlr. Mínimo da Base Mensal"** e configurar o **"Parceiro"**, **"Top"**, **"Empresa"** que contemplarão o cálculo do imposto.

![Imagem 1: Em seguida, acesse a tela Impostos . Por ser um imposto de Base Mensal , deve-se acionar a marcação de "Calcular com…](https://ajuda.sankhya.com.br/hc/article_attachments/10444819890199)

**Importante:** com relação a top devem-se configurar todas as tops que farão o cálculo desde as tops de compra, venda e baixa do financeiro.

Após a configuração do imposto o sistema fará o acúmulo dos valores para verificar se o lançamento terá ou não o cálculo, isso serve tanto para a baixa quanto o cálculo para a nota.

**Exemplo de Cálculo para a Nota\Baixa para Venda (Prestador de serviço):**

1. Configurada a empresa 109,110 com a raiz do CNPJ: 26314062. O sistema sempre pegará os oito primeiros dígitos do CNPJ;
2. No imposto foi configurado o parceiro 12, Empresa 109 e top de venda 27;
3. O serviço 2 foi configurado;
4. O sistema foi configurado para o cálculo ser na nota:

- Parâmetro CALCMENSALNOTA = Sim
- Parâmetro CALCMENSALREC = Não

Nota de Venda excedeu os 5.000,00 e efetua o cálculo:

![Imagem 2: Nota de Venda excedeu os 5.000,00 e efetua o cálculo:](https://ajuda.sankhya.com.br/hc/article_attachments/8769339232919)

Configurado agora para efetuar o cálculo através da baixa do título:

- Parâmetro CALCMENSALNOTA = Não
- Parâmetro CALCMENSALREC = Sim

![Imagem 3: Parâmetro CALCMENSALREC = Sim](https://ajuda.sankhya.com.br/hc/article_attachments/8769392391319)

**Exemplo de Cálculo para a Nota\Baixa para Compra (Tomador de serviço):**

1. Configurado os parceiros 1090, 1108 com a raiz do CNPJ: 26314062. O sistema sempre pegará os oito primeiros dígitos do CNPJ;
2. No imposto foi configurado a empresa 1,  top de compra 25;
3. O serviço 2 foi configurado;
4. O sistema foi configurado para o cálculo ser na nota:

- Parâmetro CALCMENSALNOTA = Sim
- Parâmetro CALCMENSALREC = Não

![Imagem 4: Parâmetro CALCMENSALREC = Não](https://ajuda.sankhya.com.br/hc/article_attachments/8769417607319)

Configurado agora para efetuar o cálculo através da baixa do título:

- Parâmetro CALCMENSALNOTA = Não
- Parâmetro CALCMENSALREC = Sim

![Imagem 5: Parâmetro CALCMENSALREC = Sim](https://ajuda.sankhya.com.br/hc/article_attachments/8769461135767)

Existem operações em que a retenção dos impostos mensais ocorre de acordo com movimentações feitas entre prestadores e tomadores, em que os prestadores podem ter matriz e filiais e os tomadores também podem ter matriz e filiais. Para tratamento destes casos, se faz necessária a ativação do parâmetro **"Aplicação da Lei 10833 art. 31 inciso 4 no recebimento? - LEI10833RECEB"**.

Com este parâmetro ativado, os casos em que uma empresa presta serviço para parceiros matriz e filial ou empresas matriz e filial tomam serviço de um parceiro serão considerados. Conclusão, o sistema realiza a retenção de impostos com base mensal agrupando pela raiz do CNPJ, nas seguintes situações:

1. empresas matriz e filial prestam serviço a um parceiro;
2. uma empresa toma serviço de parceiros matriz e filial;
3. uma empresa presta serviço para parceiros matriz e filial;
4. empresas matriz e filial tomam serviço de um parceiro.

Contudo, as situações 3 e 4 irão existir, apenas se o parâmetro LEI10833RECEB estiver ativado.

Vejamos agora exemplos para os casos 3 e 4, respectivamente:

**Comportamento para o caso de uma empresa prestar o serviço para parceiros matriz e filial (situação 3):**

Quando houver outros impostos configurados com base mensal o irá considerar para alcance da base mensal as notas dos parceiros (vendas) que possuem a mesma raiz de CNPJ, por exemplo:

![Imagem 6: Quando houver outros impostos configurados com base mensal o irá considerar para alcance da base mensal as notas dos…](https://ajuda.sankhya.com.br/hc/article_attachments/9856044894999)

Considerando que a retenção se baseie no regime de competência (considerando a data de entrada e saída da(s) nota(s) dentro do mesmo mês que o usuário está lançando a nota atual), a retenção nesse caso ocorrerá na confirmação da segunda nota com a base de 6.000,00 considerando a primeira nota que é de outro parceiro, porém, com a mesma raiz de CNPJ.

**Comportamento para o caso em que as empresas matriz e filial,tomamo serviço de um parceiro (situação 4):**

Quando houver outros impostos configurados com base mensal o sistema deverá considerar para alcance da base mensal as notas emitidas para empresas (compras) que possuem a mesma raiz de CNPJ, por exemplo:

![Imagem 7: Quando houver outros impostos configurados com base mensal o sistema deverá considerar para alcance da base mensal as…](https://ajuda.sankhya.com.br/hc/article_attachments/9856160249623)

Considerando que a retenção se baseie no regime de competência (considerando a data de entrada e saída da(s) nota(s) dentro do mesmo mês que o usuário está lançando a nota atual), a retenção nesse caso ocorrerá na confirmação da segunda nota com a base de 6.000,00 considerando a primeira nota que é de outra empresa, porém, com a mesma raiz de CNPJ.

**Retenção de Outros Impostos Mensais em baixas retroativas:**

No momento da realização da baixa de um título, é apresentada ao lado do campo **"Outros Impostos Mensais"**, a marcação **"Retido"**; este campo possibilita que você defina se o imposto mensal será retido ou não. Esta opção, por padrão é apresentada habilitada, e para que ela seja exibida, é necessário que exista o cálculo de impostos mensais no título, e que a baixa seja realizada em uma data retroativa, fora do mês corrente. Por exemplo, se hoje é dia 10/01/2015, e deseja-se baixar um título com a data retroativa, de modo que não se retenha os outros impostos mensais (marcação não realizada), deve-se realizar a baixa em uma data fora e anterior ao mês de janeiro.

O botão **"Detalhes"** localizado à frente desta marcação, exibe as informações do imposto calculado.

![Imagem 8: O botão "Detalhes" localizado à frente desta marcação, exibe as informações do imposto calculado.](https://ajuda.sankhya.com.br/hc/article_attachments/8769518161175)
