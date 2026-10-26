---
id: "360044595074"
titulo: "Laudo de Classificação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595074-Laudo-de-Classifica%C3%A7%C3%A3o"
trilha: "Manual do Produto > Suprimentos e Estoque > Armazéns Gerais"
atualizado_em: "2026-07-29T15:06:33Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "WMS", "Liberação de Limites", "br.com.sankhya.armazem.cad.laudo.classificacao", "Laudo de Classificação manual", "Laudo Características Aprovação.", "Qualidade", "Armazéns Gerais"]
---

# Laudo de Classificação

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42313234236055) Módulo: Armazéns Gerais > Rotinas
```

---

O laudo é realizado para definir a classificação de qualidade em que o produto se enquadra, baseado em valores pré-definidos de acordo com cada característica analisável.

| Funcionalidades da tela | |
| --- | --- |
| [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595074-Laudo-de-Classifica%C3%A7%C3%A3o#painelprincipal) | [Aba Itens do Laudo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595074-Laudo-de-Classifica%C3%A7%C3%A3o#abaitensdolaudo) |
| [Botões da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595074-Laudo-de-Classifica%C3%A7%C3%A3o#bot%C3%B5esdatela) |  |

![Imagem 2: Botões da tela](https://ajuda.sankhya.com.br/hc/article_attachments/1500005359141)

### Painel Principal

No campo **"Empresa"** será apresentada a referida empresa a qual o laudo se refere.

**Nota:** pode-se limitar a visualização de determinadas empresas ao(s) usuário(s) de sua escolha. Para essa ação, é necessário criar uma regra na tela [Central de Certificações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053-Central-de-Certifica%C3%A7%C3%B5es) e, em seguida, vincular esta no cadastro do(s) usuário(s) desejado(s) por meio da aba [Validações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abavalidaes).

A **"Senha Portaria"** é a senha registrada na portaria para a movimentação. Uma vez preenchida, serão carregadas as informações do produto e padrão de classificação do contrato já vinculados anteriormente na portaria.

O campo **"Nº Laudo"** refere-se ao número do laudo gerado pelo sistema ao inserir o registro.

No campo **"Nota de Transporte"** serão apresentadas às NF's de transporte confirmadas e pendentes. 

**Observação:** caso a Nota de Transporte já tenha sido preenchida na tela [Controle de Portaria](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050373853), ao informar a senha, esse campo será alimentado pelo sistema.

O campo **"Veículo"** é destinado à informação do veículo da respectiva movimentação. Caso o transportador mude após a emissão da nota, o Veículo poderá ser alterado manualmente, mesmo com carta de correção. Lembrando que, esse Veículo deverá ser cadastrado previamente na tela [Veículos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109693). 

O **"Nº Único Nota"** trata-se do número único da nota a qual o laudo está relacionado. 

O **"Padrão de Classificação"** está relacionado ao produto que foi indicado no campo Cód. Produto.

O campo **"Cód. Produto"** está destinado ao produto que será classificado. Podendo ser preenchido de duas formas:

- **Manual:** Você informando o produto que será analisado;
- **Calculado:** Se a Nota de Transporte ou Senha Portaria for informada e o contrato estiver vinculado a um destes registros, o campo será preenchido com o produto do respectivo contrato.

**Nota:** caso o campo Nota de Transporte esteja preenchido, o campo Cód. Produto estará protegido contra edição e poderá ser habilitado se a informação da Nota de Transporte for retirada do Laudo.

No campo **"Status"** indique a situação do laudo, que poderá ser:

- **Aguardando Aprovação:** Status inicial do laudo ao inserir o registro.
- **Aprovado:** Quando o laudo é finalizado através do botão **"Aprovar Laudo"** e não tem entre suas características analisáveis, um resultado que esteja dentro de um intervalo de Padrão de Classificação com exigência de liberação.
- **Aprovado com ressalvas:** Diferente da opção anterior, nesse caso, há um resultado que esteja dentro de um intervalo de Padrão de Classificação que tenha a exigência de liberação. Assim, para ser aprovado pela rotina, primeiro o evento **"83 - Característica Analisável fora do intervalo de valores"** deve ser aprovado na rotina de [Liberação de Limites](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites).
- **Reprovado:** Quando o evento 83 é reprovado na tela de Liberação de Limites ou quando o laudo é reprovado através da opção **"Reprovar Laudo"** no botão **"Outras Opções"**.
- **Cancelado:** Nessa opção, o laudo é cancelado através da opção **"Cancelar"** localizada no botão Outras Opções.

No campo **"Cód. Usuário"** teremos o código do usuário que gerou o laudo.

A data e hora de criação do laudo serão apresentados no campo **"Dh. Alteração"**.

O registro da verificação de **"Transgenia"** deverá fazer parte das rotinas de classificação do produto e pode apresentar os resultados Positivo, Negativo, Declarado ou Participante.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595074-Laudo-de-Classifica%C3%A7%C3%A3o#top)

### Aba Itens do Laudo

![Imagem 3: Aba Itens do Laudo](https://ajuda.sankhya.com.br/hc/article_attachments/1500005275282)

Preencha o campo **"Cód. Característica"** com o código da característica analisável.

Informe no campo **"Resultado"** o resultado aferido na classificação do produto.

No campo **"Descontar"**, teremos o percentual de desconto a ser aplicado no Laudo, de acordo com a respectiva faixa de classificação da característica cadastrada na tela [Padrões de Classificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108593-Padr%C3%B5es-de-Classifica%C3%A7%C3%A3o), considerando que:   

- Se a marcação **"Usa Índices"** estiver habilitada, o cálculo do valor a Descontar será efetuado conforme a fórmula **Descontar = (Resultado - Vlr. Base p/ Cálculo por Índices) \* Índice**, respeitando os valores previamente cadastrados na tela Padrões de Classificação.
- Com a marcação **"Usa Intervalos"** efetuada, o cálculo do valor a Descontar irá levar em consideração o valor informado no campo **"% Descontar"** da sub aba Intervalo, aba Características Classificação da tela Padrões de Classificação.
- Caso as marcações Usa Intervalos e Usa Índices estejam desativadas, o valor do campo Descontar será **"0,00"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595074-Laudo-de-Classifica%C3%A7%C3%A3o#top)

### Botões da tela

#### Botão Aprovar Laudo

O botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/16028724680087) **"Aprovar laudo"** permite que você aprove o laudo após a conclusão de seu cadastro.

#### Botão Nota de Transporte

Na parte superior da tela, o botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/16028813341463) **"Nota de Transporte"** será apresentado quando o parâmetro **"Abrir pesagem a partir da nota de transporte - ABPESANOTRA"** estiver ligado e será habilitado ao inserir um novo Laudo ou ao filtrar um Laudo em que o campo Nota de Transporte esteja vazio e o status seja Aguardando Aprovação.

Ao acioná-lo, será aberto o pop-up de mesmo nome para que você possa lançar o Laudo a partir das informações da NF de Transporte:

![Imagem 6: Ao acioná-lo, será aberto o pop-up de mesmo nome para que você possa lançar o Laudo a partir das informações da NF de…](https://ajuda.sankhya.com.br/hc/article_attachments/5898485272343)

Defina no campo **"Pesquisar por"** a forma de pesquisa da nota, entre as opções; **"Chave NF-e"**, **"Veículo"**, **"Nro Nota"** e **"Nro Único"**. Conforme a seleção realizada neste campo, será habilitada para edição apenas a opção escolhida.

Ao pesquisar a Nota de Transporte por qualquer um dos campos citados acima, o sistema preencherá os demais campos com as informações da respectiva nota. Assim, você poderá **"Confirmar"** as informações e **"Lançar"** o laudo.

**Observação:** Ao realizar o lançamento para Laudos com status Aguardando aprovação, as informações de Empresa, Nota de Transporte e Veículo poderão ser editadas normalmente. 

#### Botão Outras Opções

Inicialmente, no botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/16028629683607) **"Outras Opções"**, é apresentada a opção **"Cancelar Laudo"**, que será utilizada para efetuar o cancelamento do registro, mas mantendo salvo o histórico. Essa ação pode ser feita, por exemplo, caso seja necessário interromper o processo de carga/descarga do caminhão por motivos diversos, o que não configura necessariamente que o laudo tenha sido reprovado por problemas de qualidade.

A opção **"Reprovar Laudo"** permite efetuar a reprovação do registro, mantendo o seu histórico.

**Nota:** o cancelamento ou reprovação de um laudo que possua [Pesagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595054) associada será realizado somente se esta estiver com status igual a **"Pesagem em Andamento"**. Caso o status seja diferente, ao tentar cancelar/reprovar o laudo, será apresentada a seguinte mensagem:

**"Este laudo está vinculado ao Ticket de Pesagem nº 189, que já tem documentos gerados. Portanto, esta ação não é permitida!"**

**Observação:** na tela **"Central de Armazéns"**, localizado no botão **"Outras Opções..."** teremos as opções **"Pesagem..."** e **"Laudo..."** que, quando você clicar nesta, o sistema exibirá as telas Laudo de Classificações e/ou [Pesagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595054). Sendo assim, quando o Romaneio for gerado nessas telas, automaticamente, ao atualizar a Central de Armazéns, o romaneio realizado será exibido.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595074-Laudo-de-Classifica%C3%A7%C3%A3o#top)
