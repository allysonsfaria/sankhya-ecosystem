---
id: "17203158792855"
titulo: "Cálculo realizado para geração do F525 - EFD CONTRIBUIÇÕES"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/17203158792855-C%C3%A1lculo-realizado-para-gera%C3%A7%C3%A3o-do-F525-EFD-CONTRIBUI%C3%87%C3%95ES"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:53:35Z"
rotulos: ["Impostos", "CFOP", "Financeiro", "EFD Contribuições", "F525: Registro obrigatório", "Proporção receita auferida", "Detalhamento receitas no EFD", "F525"]
---

# Cálculo realizado para geração do F525 - EFD CONTRIBUIÇÕES

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17203128775703)SOLUÇÃO:**

**F525:** Registro obrigatório para a pessoa jurídica submetida ao regime de tributação com base no lucro presumido, optante pela apuração das contribuições sociais pelo regime de caixa.

O total das receitas relacionadas nos registros F525 deve corresponder ao total das receitas recebidas, relacionadas nos registros F500.

O valor que o sistema leva ao EFD, é o valor de desdobramento dos financeiros, que sofreram baixas no período de geração do txt, pois é o que representa a receita auferida no período, o sistema precisa aplicar sobre esse valor, as proporções que as notas que os originou tem.

Nesse ponto, o sistema analisa os valores contábeis das notas (Cadastro Livro ICMS/IPI) e quebrando a soma de todos esses valores presentes no livro, por CST X CFOP presentes na nota, e faz o seguinte cálculo:
 
Vamos imaginar uma nota, com seu total em R$ 8.071,99 e um financeiro de R$ 6.071,83 onde temos dois CST's 08 e 01 entre os itens da nota, e dois CFOP's 5902 e 5124, conforme imagem abaixo:

![Imagem 2: Nesse ponto, o sistema analisa os valores contábeis das notas (Cadastro Livro ICMS/IPI) e quebrando a soma de todos…](https://ajuda.sankhya.com.br/hc/article_attachments/17211440300951)

A soma de todos os valores contábeis da nota, presentes no livro (Cadastro Livro ICMS/IPI) = 2000,16 + 6071,83 = 8.071,99 (igual ao total da nota, pois a soma dos valores contábeis nos livros, devem bater com o total da nota sempre)
 
Em seguida, se faz necessário encontrar o valor da proporção de cada CST/CFOP sobre o total da nota:

- 2000,16 / 8071,99 = 0,247790 (índice da proporção)
- 6071,83 / 8071,99 = 0,752210 (índice da proporção)

Próximo passo do sistema, é aplicar sobre o valor do Desdobramento do financeiro R$ 6.071,83 que foi baixado no período, o índice de cada CFOP/CST para ser apresentado no F525:

- CST 08 = 6.071,83 \* 0,247790 = 1.504,59
- CST 01 = 6.071,83 \* 0,752210 = 4.567,29

E é dessa forma que o sistema leva para o txt do EFD, proporcionalizando o valor do desdobramento baixado no período, por CST/CFOP de acordo com total de cada um dessa relação, com o total de cada documento:

![Imagem 3: E é dessa forma que o sistema leva para o txt do EFD, proporcionalizando o valor do desdobramento baixado no período,…](https://ajuda.sankhya.com.br/hc/article_attachments/17208202856215)

Lembrando que a tributação efetiva da operação, será apresentada no F500, pois no F525 é apenas o detalhamento das receitas auferidas, e ao observarmos nesse exemplo, o F500 não tributou o CST 8, pois seria um erro isso, devido a ser uma operação com alíquota zero:
 
![Imagem 4: Lembrando que a tributação efetiva da operação, será apresentada no F500, pois no F525 é apenas o detalhamento das…](https://ajuda.sankhya.com.br/attachments/token/P9CE0enX4PuuZ9dQb2CgUbVF3/?name=image.png)
 
Veja que o campo 7, que é onde seria levado o valor de PIS, está zerado.
