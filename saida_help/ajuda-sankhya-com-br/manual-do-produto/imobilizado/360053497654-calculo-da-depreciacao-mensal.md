---
id: "360053497654"
titulo: "Cálculo da Depreciação Mensal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360053497654-C%C3%A1lculo-da-Deprecia%C3%A7%C3%A3o-Mensal"
trilha: "Manual do Produto > Financeiro e Patrimônio > Imobilizado"
atualizado_em: "2026-08-21T13:19:17Z"
rotulos: ["Produtos", "Configuração", "Contábil", "Fiscal", "CALCDEPMESANO", "Imobilizado", "Depreciação", "br.com.sankhya.mgeimob.calculodepreciacaomensal", "CALDEPVLRMESBX", "CALDEPCR", "DEPPRORATA", "AJUDEPDEVBEM", "Configurações e parâmetros", "Cálculo mensal depreciação", "Movimentos: Depreciação Baixa Devolução"]
---

# Cálculo da Depreciação Mensal

```
 Módulo: Imobilizado > Rotinas             Versão disponível: A partir da 4.3
```

---

Através desta tela, você calcula as depreciações para todos os bens disponíveis. O cálculo deverá ser realizado mensalmente, assim, ao abrir a tela, o Sankhya Om já irá sugerir a próxima referência esperada para o cálculo.

![Imagem 1: Através desta tela, você calcula as depreciações para todos os bens disponíveis. O cálculo deverá ser realizado…](https://ajuda.sankhya.com.br/hc/article_attachments/360091462173)

A marcação **"Fiscal/Contábil Tradicional"** buscará as informações para o cálculo do cadastro do imobilizado na sub aba **"Taxa Fiscal/Contábil Tradicional"** ([Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), aba [Bens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#ababens), sub-aba [Bens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-ababens)).

Quando a marcação **"p/ Ajuste Lei 11.638"** estiver habilitada, fará com que o sistema busque as informações para o cálculo do cadastro do imobilizado na sub-aba **"Taxa p/ Ajuste Lei 11.638"** (Cadastro de Produtos, aba Bens, sub-aba Bens).

**Observação:** no cálculo são gerados 4 tipos de movimento:

- A - Depreciação;
- C - Baixa;
- D - Devolução de Venda;
- 1 - Devolução de Compra.

**Importante:** com a marcação acima habilitada, o sistema não fará a Depreciação pró-rata mesmo se o parâmetro **"Depreciação pro rata de imobilizado? - DEPPRORATA"** estiver ligado.

Caso exista depreciação calculada para o mês posterior à **"Referência"** informada, será exibida uma mensagem avisando que já foi calculada depreciação para a referência posterior:

[GIF animado: Imagem 2: Caso exista depreciação calculada para o mês posterior à "Referência" informada, será exibida uma mensagem avisando que…](https://ajuda.sankhya.com.br/hc/article_attachments/360091463753)

Caso tente calcular uma depreciação futura e exista mês sem calcular, será exibida uma mensagem informando o último mês que possui cálculo da depreciação fiscal:

[GIF animado: Imagem 3: Caso tente calcular uma depreciação futura e exista mês sem calcular, será exibida uma mensagem informando o último mês…](https://ajuda.sankhya.com.br/hc/article_attachments/360091462893)

Se você selecionar um período anterior ou igual a um que já possua cálculo de depreciação, antes de realizar o cálculo e exclusão dos registros, o sistema emitirá um aviso informando que as depreciação feitas para o período e após ele serão excluídas:

[GIF animado: Imagem 4: Se você selecionar um período anterior ou igual a um que já possua cálculo de depreciação, antes de realizar o cálculo…](https://ajuda.sankhya.com.br/hc/article_attachments/360089315374)

Habilitando a opção **“Utilizar residual no cálculo do último mês de depreciação”**, o valor residual do bem, restante no último mês de depreciação, será somado à parcela de depreciação correspondente ao período.

Deve-se observar algumas validações a respeito dessa rotina, ressaltando-se que estas serão aplicadas para os dois modelos de depreciação, a normal e a de ajuste:

- Se os campos **Data Inicial** e **Data Final** da sub-aba [Bens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-ababens), da aba [Bens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#ababens), de cadastro de [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos) não estiverem preenchidos, não será possível calcular a quantidade de meses de depreciação total e assim aplicar a regra de cálculo para determinar a depreciação do saldo residual;
- Se o campo Data Final estiver preenchido e este for igual à referência de depreciação, então o saldo residual será depreciado;
- Caso o campo Data Inicial esteja vazio, mas o campo **“Data da compra”** da sub-aba **"Geral"**, da aba Bens, do cadastro de Produtos, tenha sido informado, o sistema utilizará esta data como base para aplicar a funcionalidade;
- Considerando um bem já depreciado anteriormente a uma taxa anual fixa, então a quantidade de meses restante será calculada com base nessa informação;
- Se apenas o campo Data Final não estiver preenchido, mas o campo Data Inicial estiver, o sistema calcula a quantidade de meses em que o bem será depreciado visando identificar se haverá valor residual no último mês de depreciação. Isso será feito aplicando a fórmula:

```
 Quantidade de meses = (100% / taxa anual) * 12 meses 
```

- Caso não seja possível definir a Data final para os bens depreciados a taxas diferentes durante o ano, essa funcionalidade não será aplicada.

Por fim, temos alguns parâmetros que influenciarão nesta rotina:

Com o parâmetro **"Considera só mes/ano para cálculo da depreciação - CALCDEPMESANO"** desligado, só serão selecionados bens com início de depreciação ou baixa até o dia 15 do mês de Referência.

**Nota:** Se o início da depreciação do bem ocorrer após o dia 15, no referido mês não haverá depreciação; se a baixa ocorrer após o dia 15, só será considerado no mês seguinte.

O parâmetro **"Calcula depreciação no valor do mês p/ bem baixado - CALDEPVLRMESBX"** faz com que, na referência da baixa do bem, seja calculada a depreciação para o mês selecionado.

Em relação ao parâmetro **"Calcula depreciação de centro de resultado? - CALDEPCR"**, este irá gravar no movimento o departamento e Centro de Resultado na Referência.

O parâmetro **"Depreciação pro rata de imobilizado? - DEPPRORATA"** faz com que a taxa seja calculada pró-rata na primeira depreciação do bem, de acordo com a data de início da depreciação e na baixa, de acordo com a data da baixa.

**Observação:** O cálculo pró-rata no início apenas ocorrerá se o parâmetro de chave CALCDEPMESANO estiver ligado.

O parâmetro **"Ajustar depreciação na devolução de venda de bem - AJUDEPDEVBEM"** quando habilitado, fará o ajuste da depreciação na Devolução de Venda do bem.

---

## Perguntas frequentes

### Por que dois bens baixados no mesmo dia podem depreciar com número de dias diferentes?

O sistema usa o mês em que cada bem começou a depreciar para calcular a base de dias — não a data da baixa. Como um bem pode ter começado em um mês de 30 dias e outro em um mês de 31, a divisão fica diferente mesmo com a baixa na mesma data.

Isso é esperado, não é erro. Controlado pelo parâmetro DEPPRORATDIAMES.

Exemplo: bem A começou a depreciar em março (31 dias), bem B em junho (30 dias). Baixados no mesmo dia, cada um usa a base do seu mês de início.
