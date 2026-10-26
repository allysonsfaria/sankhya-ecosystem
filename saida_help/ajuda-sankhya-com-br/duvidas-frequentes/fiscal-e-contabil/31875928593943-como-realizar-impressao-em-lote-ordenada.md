---
id: "31875928593943"
titulo: "Como realizar impressão em lote ordenadas pelo número da nota?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31875928593943-Como-realizar-impress%C3%A3o-em-lote-ordenadas-pelo-n%C3%BAmero-da-nota"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:32:19Z"
rotulos: ["Configuração", "Impressão", "Parceiro", "NF-e", "DANFE", "impressão em lote", "ordenadas pelo número da nota"]
---

# Como realizar impressão em lote ordenadas pelo número da nota?

**(1)** Este artigo tem o objetivo de apoiar nas configurações necessárias para ordenar as notas por número de nota ao realizar impressões em lote nos portais (compra ou venda).

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31886567271319)SOLUÇÃO:**

![Imagem 2: Temos dois casos de exemplo, a primeira seria a configuração de ordenação ao selecionar várias notas não confirmadas ou…](https://ajuda.sankhya.com.br/hc/article_attachments/31875928578583) Temos dois casos de exemplo, a primeira seria a configuração de ordenação ao selecionar várias notas não confirmadas ou aprovadas e clicar no botão de impressora das portas.

Neste caso para que as notas sejam impressas conforme ordenação da grade, o parâmetro **"Imprimir DANFE e depois boletos? - IMPDANFEBOL"** deve estar desligado, pois quando está ligado tem prioridade sobre o parâmetro **"MULTSELORD - Respeitar a ordem da grade em selec. várias Notas?"**.

Já o parâmetro MULTSELORD, uma vez habilitado, fará com que as notas sejam impressas de acordo com sua ordenação/apresentação na grade.

**(2)Vejamos um exemplo:**

As notas de número 5487, 6587, 5481 e 44 não estavam ordenadas por número nota na grade e estavam sendo apresentadas conforme esta sequência informada. Ao solicitar a impressão das mesmas, com o parâmetro ativado, o sistema obedecerá a sequência que está na grade e a impressão ocorrerá na mesma ordem (5487, 6587, 5481 e 44).

Caso o parâmetro MULTSELORD esteja desligado, as notas serão impressas sempre obedecendo a sequência do número nota e não a sua apresentação na grade. Assim, ainda no exemplo citado, ao solicitar a impressão das notas 5487, 6587, 5481 e 44, as mesmas serão impressas obedecendo a numeração crescente das notas, ou seja, primeiro será impresso a nota de número 44, em seguida a 5481, a 5487 e por último a 6587, mesmo que as mesmas não estejam ordenadas pelo número da nota de forma crescente na seleção de notas na grade.

![Imagem 3: O segundo caso que temos é: ao selecionar notas em massa/lote e ir em "Outras opções > Confirmar" , o sistema confirma…](https://ajuda.sankhya.com.br/hc/article_attachments/31875928579095) O segundo caso que temos é: ao selecionar notas em massa/lote e ir em **"Outras opções > Confirmar"**, o sistema confirma e fatura todas as notas e imprime automaticamente, porém as impressões saem fisicamente todas desordenadas.

Neste caso, nativamente a ordem de impressão respeita a sequência de número único do lançamento, não verificando os parâmetros acima. Sendo necessário sempre ordenar os pedidos antes de selecionados para um faturamento em massa.

**(2)**Se por exemplo for ordenado os pedidos por transportadora antes do faturamento em massa, isso faz com que os números únicos fiquem divergentes, desordenando as impressões.  Então o orientado é que ao final dos filtros reordene por número único, dessa forma a ordem impressa é a mesma da ordem da grade, respeitando o número da nota.
