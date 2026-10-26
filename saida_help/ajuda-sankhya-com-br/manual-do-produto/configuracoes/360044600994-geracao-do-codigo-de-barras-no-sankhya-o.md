---
id: "360044600994"
titulo: "Geração do Código de Barras no Sankhya Om"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600994-Gera%C3%A7%C3%A3o-do-C%C3%B3digo-de-Barras-no-Sankhya-Om"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:50:55Z"
rotulos: ["Produtos", "Configuração", "URL", "Estoque", "Código de Barras", "Chamada Direta", "Code128", "Ean13", "Ean8", "Geração do Código de Barras no Sankhya-W manual", "Geração de Código de Barras no Sankhya Om", "Sankhya Om"]
---

# Geração do Código de Barras no Sankhya Om

O Sankhya Om possui um serviço de geração de imagem do código de barras, em que, tem-se como parâmetro o tipo do Código de Barras e a resolução da imagem (DPI) correspondente ao Código de Barras. Esse serviço não dependerá de componentes de terceiros e/ou internet, suma vez que é gerado pelo próprio sistema.

![Imagem 1: As configurações mencionadas abaixo, devem ser realizadas com o acompanhamento direto de um Consultor Sankhya .](https://ajuda.sankhya.com.br/hc/article_attachments/16427058648087) As configurações mencionadas abaixo, devem ser realizadas com o acompanhamento direto de um Consultor Sankhya.

Existem duas maneiras de geração do Código de Barras, sendo elas, via [URL](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600994-Gera%C3%A7%C3%A3o-do-C%C3%B3digo-de-Barras-no-Sankhya-Om#url) ou [Chamada Direta](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600994-Gera%C3%A7%C3%A3o-do-C%C3%B3digo-de-Barras-no-Sankhya-Om#acessodiretopelosmtodos-.jar) dos métodos via jar. Observe:

## URL

Verifique abaixo, a URL utilizada para o serviço:

```
localhost:8080/mge/barcode.mge?cod=" + COD + "&dpi="+ DPI +"&tipo="+ TIPO
                         +"&impl=" + IMPL_COD + "&txt=" +TXT
```

Em que:

**COD** = Código informado para ser gerado o código de barras. Essa informação é obrigatória.

**DPI** = Resolução de imagem do Código de Barras. Essa funcionalidade considera três DIP's, sendo esses 120, 300 e 600. Caso não seja informado o DPI, será gerado o barcode com resolução 120, que é o valor padrão. Recomenda-se o valor de 300 DPI. Esta informação não é obrigatória.

**TIPO** = Esse é o formato que será gerado o barcode. Essa funcionalidade considera três formatos: Code128, Ean8 e Ean13. Se não informado, será gerado o barcode com o formato Code128, que é o valor padrão. Este não é um dado obrigatório.

**IMPL\_COD** = Este, possui uma flag em que, se for true, o TXT será gerado embaixo do barcode, caso seja diferente, admite valor false, gerando somente o barcode. Não sendo informado, o valor padrão é false. Essa também não é uma informação obrigatória.

**TXT** = Essa informação corresponde ao texto que será gerado embaixo do barcode. Caso seu valor seja null (nulo), e a flag **IMPL\_COD** seja true, a funcionalidade gera o TXT com o valor COD. Essa informação não é obrigatória.

Observe a seguir, alguns exemplos da geração por meio da URL:

**URL - Utilizando apenas o COD:** O processo gera somente o barcode, com 120 DPI (valor padrão) sem a numeração do COD embaixo do barcode:

![Imagem 2: URL - Utilizando apenas o COD: O processo gera somente o barcode, com 120 DPI (valor padrão) sem a numeração do COD…](https://ajuda.sankhya.com.br/hc/article_attachments/8930000759703)

**URL - Utilizando COD, DPI:** Possui a geração somente do barcode, com 300 DPI sem a numeração do COD embaixo do barcode:

![Imagem 3: URL - Utilizando COD, DPI: Possui a geração somente do barcode, com 300 DPI sem a numeração do COD embaixo do barcode:](https://ajuda.sankhya.com.br/hc/article_attachments/8930006548247)

**URL - Uso do COD, DPI, TIPO:** O processo gera somente o barcode, com 300 DPI e formato EAN13, sem a numeração do COD embaixo do barcode:

![Imagem 4: URL - Uso do COD, DPI, TIPO: O processo gera somente o barcode, com 300 DPI e formato EAN13, sem a numeração do COD…](https://ajuda.sankhya.com.br/hc/article_attachments/8929983197335)

**URL - Utilizando COD, DPI, TIPO, IMPL\_COD:** Será gerado o barcode, com 300 DPI e formato EAN13, com a numeração do COD; nessa situação o TXT não foi informado:

![Imagem 5: URL - Utilizando COD, DPI, TIPO, IMPL_COD: Será gerado o barcode, com 300 DPI e formato EAN13, com a numeração do COD;…](https://ajuda.sankhya.com.br/hc/article_attachments/8930048949911)

**URL - Fez-se o uso do COD, DPI, TIPO, IMPL\_COD, TXT:** Teremos aqui, a geração do barcode a partir do COD = 7891114003581, com 300 DPI e formato EAN13, com a mensagem do TXT; neste exemplo, utilizamos o termo "sankhya":

![Imagem 6: URL - Fez-se o uso do COD, DPI, TIPO, IMPL_COD, TXT: Teremos aqui, a geração do barcode a partir do COD =…](https://ajuda.sankhya.com.br/hc/article_attachments/8930077708951)

```
 Após a criação do modelo de etiqueta com a nova URL, realize a criação do modelo que
           será utilizado na tela de Modelo de etiquetas. Para execução de testes, é necessário alterar
           o endereço na URL, o endereço do servidor utilizado; a porta padrão é 8080.
```

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600994-Gera%C3%A7%C3%A3o-do-C%C3%B3digo-de-Barras-no-Sankhya-Om#top)

---

## Acesso direto pelos Métodos - .JAR

Outra forma de geração do barcode, é por meio do acesso direto dos métodos pelo iReport. Para o acesso direto dos métodos, é necessário possuir o sanutil.jar; caso não o tenha, siga as orientações abaixo:

1. No iReport, acesse Ferramentas > Opções:

|  | ![Imagem 7: 1. No iReport, acesse Ferramentas > Opções :](https://ajuda.sankhya.com.br/hc/article_attachments/42310737743767) |  |
| --- | --- | --- |

2. Em seguida, acesse a aba Classpath e caso não tenha, clique no botão Add JAR:

![Imagem 8: 2. Em seguida, acesse a aba Classpath e caso não tenha, clique no botão Add JAR :](https://ajuda.sankhya.com.br/hc/article_attachments/8930149994007)

#### Métodos Implementados

O Sankhya Om possui 9 métodos para a geração de barcode para formatos Code128, Ean8 e Ean13. Observe:

#### Code128

- buildCode128(String cod) - O metódo recebe o código para geração do barcode sem numeração;
- buildCode128(String cod, String texto) - O metódo recebe o código e o texto para o barcode ser gerado com numeração;
- buildCode128(String cod, String texto, int dpi) - O metódo recebe o código, o texto e o DPI; caso o texto seja nulo, o barcode será gerado sem numeração, se não for, será gerado com numeração.

#### Ean8

- buildEan8(String cod) - O metódo recebe o código para geração do barcode sem numeração;
- buildEan8(String cod, String texto) - O metódo recebe o código e o texto para ser gerado o barcode com numeração;
- buildEan8(String cod, String texto, int dpi) - O metódo recebe o código, o texto e o DPI, caso o texto seja nulo, o barcode não será gerado com numeração, se não for, será gerado com numeração.

#### Ean13

- buildEan13(String cod) - O metódo recebe o código para ser gerado o barcode sem numeração;
- buildEan13(String cod, String texto) - O metódo recebe o código e o texto para ser gerado o barcode com numeração;
- buildEan13(String cod, String texto, int dpi) - O metódo recebe o código, o texto e o DPI, caso o texto seja nulo, o barcode será gerado sem numeração, se não for, será gerado com numeração.

Observe alguns exemplos da geração por meio da Chamada Direta de Método:

**buildCode128("7891114003581")**

![Imagem 9: buildCode128("7891114003581")](https://ajuda.sankhya.com.br/hc/article_attachments/8930244720535)

---

**buildCodeEan8("65833254", "65833254")**

![Imagem 10: buildCodeEan8("65833254", "65833254")](https://ajuda.sankhya.com.br/hc/article_attachments/8930303376151)

---

**BuildCodeEan13("7891114114294", "7891114114294", 600)**

![Imagem 11: BuildCodeEan13("7891114114294", "7891114114294", 600)](https://ajuda.sankhya.com.br/hc/article_attachments/8930278582935)

```
 No iReport, o teste de chamada dos métodos acima descritos, é realizado acessando
           Propriedades > Image Expression; a chamada do método deve ser realizada no Image
           Expression.
```

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600994-Gera%C3%A7%C3%A3o-do-C%C3%B3digo-de-Barras-no-Sankhya-Om#top)

## Parâmetros que influenciam esta rotina

Por meio do parâmetro **"Formatação código de barras - FORMABARRASQTD"**, o sistema fará a leitura do código de barras do produto conforme você definir no campo **"Texto"**. Assim, confira o exemplo de formatação a seguir:

- Posição onde começa o código do produto - POSCODPROD=2;
- Número de campos do código do produto - TAMCODPROD=6;
- Posição onde começa a quantidade de produtos - POSQTD=8;
- Número de campos da quantidades de produtos - TAMQTD=5;
- Quantidade de decimais da quantidade de produtos - DECQTD=3.

Feito isso, será verificado se a marcação **"Cód.Barras com quantidade"** da tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), aba [Medidas e estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abamedidaseestoque), sub-aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-abaestoque) está selecionada.

Sendo assim, realizadas as configurações acima, o sistema localizará o produto e o código de barras, e o incluirá na tela de **"Lançamento por Código de Barras"**.

Ao ligar o parâmetro **"Cód.barras = Cód.Prod./Preço/Qtd, qdo iniciado c/2 - CODBARDECOMP2"**, o sistema irá ler o código de barras inserido originado da balança, gerado a partir do código de barras do produto + Preço + Peso, iniciado com o número 2.

### \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Regras para formato de código de barras para leitura de balança (Parâmetro CODBARDECOMP2)

Quando um produto é controlado por peso (balança), ele normalmente utiliza códigos de barras iniciados por **"2"**. O sistema interpreta qualquer código iniciado com esse dígito como um **código variável**, e não como um código fixo de cadastro.

Para evitar erros de validação e conflitos (como o erro `CORE_E03947`), siga estas diretrizes de cadastro:

- **Não cadastrar o código do fornecedor iniciado em 2 como EAN principal:** Esse código é gerado pela balança do fornecedor e varia conforme peso e preço, não sendo um identificador estável para o estoque.
- **Cadastrar o produto com um código interno fixo:** Utilize um código interno (SKU próprio) ou o EAN oficial do produto (normalmente iniciado por 7, 8, 0 ou 1).
- **Configuração de leitura:** O sistema ignora o código variável e foca nos dígitos centrais que correspondem ao código interno cadastrado. O padrão comum (que pode variar conforme a balança) é **2 PPPPP QQQQ C**:

  - **2**: Prefixo de balança.
  - **PPPPP**: Código interno do produto no seu sistema.
  - **QQQQ**: Quantidade ou peso gerado.
  - **C**: Dígito verificador.

**Exemplo Prático de Cadastro:** Para um produto "Queijo Minas" recebido com o código `2 12345 0500 8`:

1. **Código interno:** Cadastre como `12345`.
2. **EAN principal:** Deixe vazio ou preencha com o EAN real (fixo), se existir.
3. **Tipo de produto:** Marque como **Pesável** (utiliza balança no cadastro do produto).
4. **Parâmetro:** Certifique-se de que o parâmetro **CODBARDECOMP2** está ligado.

> **Atenção:** Se o parâmetro **FORMABARRASQTD** estiver configurado simultaneamente ao **CODBARDECOMP2**, deve-se garantir que as formatações não conflitem, ajustando as configurações de formação se necessário.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600994-Gera%C3%A7%C3%A3o-do-C%C3%B3digo-de-Barras-no-Sankhya-Om#top)
