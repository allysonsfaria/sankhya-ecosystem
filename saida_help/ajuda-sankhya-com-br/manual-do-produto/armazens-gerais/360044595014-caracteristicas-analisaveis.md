---
id: "360044595014"
titulo: "Características Analisáveis"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595014-Caracter%C3%ADsticas-Analis%C3%A1veis"
trilha: "Manual do Produto > Suprimentos e Estoque > Armazéns Gerais"
atualizado_em: "2026-07-29T15:06:27Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "WMS", "Características Analisáveis manual", "DESCLAUDOCASCAT", "br.com.sankhya.os.cad.caracteristicasAnalisaveis", "Cadastro", "Cadastro Características Laudo", "Laudo de Classificação"]
---

# Características Analisáveis

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42313204800663) Módulo: Armazéns Gerais > Cadastros
```

---

Nesta tela, cadastre as características a serem analisadas e descritas em um [Laudo de Classificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595074).

### Painel Principal

Ao acessa-lá, inicialmente, forneça as informações nos seguintes campos do Painel Principal:

![Imagem 2: Ao acessa-lá, inicialmente, forneça as informações nos seguintes campos do Painel Principal :](https://ajuda.sankhya.com.br/hc/article_attachments/20004011782039)

O campo **"Código"** pode ser alimentado de forma manual ou automática; essa definição é feita pelo botão ![Imagem 3: O campo "Código" pode ser alimentado de forma manual ou automática; essa definição é feita pelo botão "Configuração da…](https://ajuda.sankhya.com.br/hc/article_attachments/20003300773783) **"Configuração da tela"** na opção **"Numeração"**. Nesse campo informe a chave da característica, ou seja, essa numeração será responsável por identificá-la em todas as rotinas em que ela estiver presente.

Indique a definição da característica através do campo **"Descrição"**.

Por meio do campo **"Observação"**, insira qualquer informação adicional sobre a característica.

No campo **"Vinculado a"**, relacione uma classificação à outra, visto que há campos de classificação cujo resultado deve ser somado para ser considerado fora de padrão. Sendo assim, uma classificação poderá ser a soma de duas ou mais classificações originais.

Na confirmação de um laudo com valor diferente de zero e com a marcação **"Exige Liberação?"** habilitada, será incluída uma solicitação de liberação para o evento [38 - Características de Análises de Laudo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#38-caractersticasdeanlisesdelaudo) quando no campo Observação for inserido o nome da característica.

Ao optar pela liberação, será autorizada a confirmação da nota, se ela for negada, então será permitido a confirmação da nota e o sistema irá gerar uma **"Devolução do Produto"** com a mesma quantidade encontrada na **"Característica"** marcada.

Por meio do campo **"Ordem"** pode ser classificada a ordem para o cálculo do desconto de laudo. É importante ressaltar que quando o parâmetro **"Calcular Desconto de Laudo em Cascata? - DESCLAUDOCASCAT"** é habilitado, o sistema irá realizar o cálculo da Característica conforme o campo Ordem, de forma que o primeiro desconto será calculado com o peso líquido da nota; já o segundo desconto será realizado com base no resultado do cálculo anterior e assim por diante. Ao desativar o parâmetro, o cálculo será efetuado somente com o valor líquido da nota.

A marcação **"Análise de Terceiros/REPORT SUPPLIER"** representa uma característica, cuja análise é realizada por um parceiro terceiro.

No campo **"Qtd. Decimais"** defina a quantidade de casas decimais que a característica possui. Esse valor impacta tanto na quantidade mínima e máxima da característica no vínculo com um Padrão de Classificação (laudo), como também no resultado da característica em um apontamento de um laudo.

### Aba Usuários

Nesta aba, informe no campo **"Cód. Usuário"** o usuário que terá acesso à análise de uma característica específica.

![Imagem 4: Nesta aba, informe no campo "Cód. Usuário" o usuário que terá acesso à análise de uma característica específica.](https://ajuda.sankhya.com.br/hc/article_attachments/20005668945815)

#### Botão Edição Múltipla

O botão ![Edição](https://ajuda.sankhya.com.br/hc/article_attachments/15992376335511) **"Edição Múltipla"** permite a edição simultânea de vários registros a partir do modo grade. Ou seja, ao selecionar um conjunto de registros e clicar no botão, será possível editar os campos correspondentes de todos os registros de uma só vez. 

![Imagem 6: Para que esse botão seja apresentado, selecione mais de um registro.](https://ajuda.sankhya.com.br/hc/article_attachments/20005753912471) Para que esse botão seja apresentado, selecione mais de um registro.

![Imagem 7: Para que esse botão seja apresentado, selecione mais de um registro.](https://ajuda.sankhya.com.br/hc/article_attachments/20006143193623)

Considere o seguinte exemplo de uso desse botão:

Com as características em modo grade na tela Características Analisáveis selecione-as e, em seguida, clique no botão Edição Múltipla, assim os campos poderão ser editados simultaneamente para todas as selecionadas. 

![Imagem 8: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/20005845524503) Acesse também:

[Laudo de Classificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595074)
