---
id: "29913492823831"
titulo: "Cálculo da média do ST anterior na tela \"Ativar/Reprocessar ST Anterior pela Média das Entradas”"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/29913492823831-C%C3%A1lculo-da-m%C3%A9dia-do-ST-anterior-na-tela-Ativar-Reprocessar-ST-Anterior-pela-M%C3%A9dia-das-Entradas"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:36:44Z"
rotulos: ["Produtos", "Configuração", "Impostos", "Estoque", "Financeiro", "Cálculo da média do ST", "\"Ativar/Reprocessar ST Anterior pela Média das Entradas”"]
---

# Cálculo da média do ST anterior na tela "Ativar/Reprocessar ST Anterior pela Média das Entradas”

Compreenda os valores registrados nos campos QTDEST; BCSTRETTOTAL; VICMSSTRETTOTAL; BCSTRETUNIT; VICMSSTRETUNIT, na tabela TGFSTMM referente a tela **“Ativar/Reprocessar ST Anterior pela Média das Entradas”**

(1)** QTDEST**: se refere a contagem de estoque do produto que o cliente possui e seu valor pode ser identificado na tabela TGFCTE (ContagemEstoque). No exemplo abaixo são encontrados dois valores, sendo 51,00 e 0,17, tendo a somatória 51,17.

![Imagem 1: (1) QTDEST : se refere a contagem de estoque do produto que o cliente possui e seu valor pode ser identificado na…](https://ajuda.sankhya.com.br/hc/article_attachments/32037886413975)

(1)** BCSTRETOTAL**: calculo é realizado da seguinte forma:

- Será necessário encontrar primeiramente o valor de QTDEST identificado na tabela TGFCTE sendo 51,17;
- Neste exemplo é necessário pegar o **valor proporcional** referente a quantidade necessária para **abater o valor da contagem de estoque;**
- O valor a ser abatido do estoque é 51,17, e no exemplo foi necessário lançamento de 3 notas para bater esse estoque. Mas, como o valor das notas retornam 60 no campo QTDNEG, acaba passando o valor de 51,17. Assim, é necessário realizar o proporcional desse valor que no caso é 11,17.

![Imagem 2: O valor a ser abatido do estoque é 51,17, e no exemplo foi necessário lançamento de 3 notas para bater esse estoque.…](https://ajuda.sankhya.com.br/hc/article_attachments/32037886415127)

**Observação:** para chegar no valor 11,17 é necessário somar todos os valores de QTDNEG e identificar o valor necessário para abater nosso estoque realizado na contagem de estoque (QTDEST) sendo assim:

- 1° nota QTDNEG = 20 2° nota QTDNEG = 20 3° nota QTDNEG = 20 Sendo assim para abater o 51,17 do estoque é necessário somar as duas primeiras notas que é 40 e subtrair pelo valor referente ao estoque no caso 51,17, encontrando o valor de 11,17 \*\* Para encontrar o valor correto para assim calcular o BCSTRETOTAL, será necessário realizar o seguinte calculo: - (QTDNEG \* BASESUBSTIT) / PELO PROPORCIONAL PARA ABATER O VALOR DO ESTOQUE NO NOSSO CASO É 11,17 EX: (20 \* 744) / 11,17 = **|415,53| --> Valor proporcional da BASESUBSTIT**

Ao encontrar esse valor proporcional da BASESUBSTIT da nota que irá abater o restante do estoque será necessário realizar a soma de todos os valores encontrados na BASESUBSTIT e dividir pela QTDNEG

- **Exemplo:** ((781,20 \* 2) + 415,53) / 51,17 = **|38,65| --> Esse valor é o BCSTRETOTAL**

(1)** VICMSSTRETTOTAL**: para encontrar esse valor de média será necessário achar novamente o proporcional referente ao campo VLRICMS o seguinte cálculo:

- Para iniciar o cálculo, será necessário encontrar o valor proporcional do campo VLRICMS referente a nota que contribui para o abatimento do estoque, da seguinte maneira: (VLRICMS / QTDNEG) \* PROPORCIONAL (86,40 / 20) \* 11,17 = **|48,25| --> Valor proporcional do VLRICMS da nota**

![Imagem 3: Para iniciar o cálculo, será necessário encontrar o valor proporcional do campo VLRICMS referente a nota que contribui…](https://ajuda.sankhya.com.br/hc/article_attachments/32037886417047)

Após encontrar esse valor de VLRICMS proporcional será necessário apenas somar todos os valores do campo VLRICMS conforme abaixo:

**Exemplo:** (90,72 \* 2) + 48,25 = **|229,69| --> Valor do VICMSSTRETTOTAL**

(1)** BCSTREUNIT**: o calculo é realizado da seguinte forma:

- É feita a somatória de todos os valores encontrados na BASESUBSTIT seguindo o mesmo raciocínio de proporcional anteriormente, **exemplo**: ((781,20 \* 2) + 415,53) = **|1977,93| --> Esse é o valor de BCSTREUNIT**

(1)** VICMSSTRETUNIT**: a forma de cálculo utilizado para encontrar esse valor é a seguinte:

- Divida o valor retornado no campo VICMSSTRETTOTAL pela QTDEST conforme exemplo a seguir: VICMSSTRETTOTAL / QTDEST --- 229,69 / 51,17 = |4,488 ~= **4,49| --> Esse é o valor de VICMSSTRETUNIT**

Com isso temos todas as fórmulas de cálculo realizadas para encontrar os respectivos valores dos campos da tabela TGFSTMM.

![Imagem 4: Com isso temos todas as fórmulas de cálculo realizadas para encontrar os respectivos valores dos campos da tabela…](https://ajuda.sankhya.com.br/hc/article_attachments/32037886417687)
