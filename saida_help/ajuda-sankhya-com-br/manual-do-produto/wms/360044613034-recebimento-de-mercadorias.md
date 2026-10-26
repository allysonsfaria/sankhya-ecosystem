---
id: "360044613034"
titulo: "Recebimento de Mercadorias"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-07-29T14:14:03Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "WMS", "Parceiro", "WMSVALCODVOLUSU", "Recebimento", "Estoque", "CODRELRECONTA", "IMPMAPARECONTA", "Avaria", "Direfença", "Falta", "Item", "Recebimento de Mercadorias", "Recontar", "br.com.sankhya.recebimento", "Recebimento de Mercadorias manual", "Gerenciamento do Recebimento de Mercadorias no WMS", "WMSPRODNAOREC"]
---

# Recebimento de Mercadorias

```
 Módulo: WMS > Rotinas
```

---

Essa tela possibilita que o gestor do armazém administre o recebimento das mercadorias da empresa que está responsável; ela auxilia no gerenciamento dos itens que entram na posse da empresa, tornando possível a tomada de decisões, visando um melhor gerenciamento do armazém. Essa tela também está envolvida na rotina de [Armazenamento de Produtos Recebidos em Endereço Flutuante](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112233).

| [Painel Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#painelfiltros) |  | [Painel Situação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#painelsituao) |
| --- | --- | --- |
| [Grade Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#graderecebimento) |  | [Grade Itens da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#gradeitensdanota) |
| [Botões no topo da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#botesnotopodatela) |  | [Portal de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#portaldecompras) |
| [Parâmetros que influenciam essa rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#par%C3%A2metrosqueinfluenciamessarotina) |  |  |

![Imagem 1: Parâmetros que influenciam essa rotina](https://ajuda.sankhya.com.br/hc/article_attachments/36442456154263)

## Painel Filtros

No lado esquerdo da tela, além da possibilidade de criação de filtros personalizados para apresentação das informações, você pode preencher os seguintes campos para filtragem:

O campo **"Empresa"** deve ter seu preenchimento obrigatório com a Empresa a qual está sendo realizado o recebimento.

Você também poderá filtrar os recebimentos informando o parceiro pelo qual foi realizado o recebimento no campo **"Parceiro"**.

Informe no campo **"Transportadora"** o parceiro transportadora que efetuou o deslocamento da mercadoria.

Preencha o campo **"Data de Recebimento"** com um intervalo de datas em que foram realizados os recebimentos de mercadoria.

Indique no campo **"Nro. Recebimento"** o número do recebimento que você deseja filtrar.

Você também pode filtrar os recebimentos indicando no campo **"Num. Pedido"**, o número do pedido a ele vinculado.

Também podemos filtrar os recebimentos através das docas em que eles ocorreram, essa informação é inserida no campo **"Doca"**.

Além dos campos até aqui mencionados, é possível, com o uso do campo **"Produto"**, filtrar os produtos relacionados aos recebimentos.

![Imagem 2: Além dos campos até aqui mencionados, é possível, com o uso do campo "Produto" , filtrar os produtos relacionados aos…](https://ajuda.sankhya.com.br/hc/article_attachments/36442456155927)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#top)

## Painel Situação

Além dos filtros que citamos acima, você pode utilizar as marcações presentes no painel **"Situação"** para filtragem e consequente apresentação dos recebimentos. Do mesmo modo que os filtros, você efetua as marcações desejadas e clica no botão **"Aplicar"**, para que os recebimentos que se enquadram no que foi estabelecido sejam exibidos na tela.

![Imagem 3: Além dos filtros que citamos acima, você pode utilizar as marcações presentes no painel "Situação" para filtragem e…](https://ajuda.sankhya.com.br/hc/article_attachments/36442456157207)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#top)

## Grade Recebimento

Nessa grade são exibidos os recebimentos de acordo com os filtros informados. Na imagem abaixo, os recebimentos com situação igual a Concluído foram exibidos com a coloração **Azul**; os recebimentos com situação igual à Conferência com divergência e Problemas na confirmação da nota apresentados na coloração **Vermelha** e as demais situações exibidas com a cor **Preta**.

![Imagem 4: Nessa grade são exibidos os recebimentos de acordo com os filtros informados. Na imagem abaixo, os recebimentos com…](https://ajuda.sankhya.com.br/hc/article_attachments/36442462542103)

**Nota:** você pode definir as cores para cada situação de recebimento através do botão [Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#bot%C3%A3ooutrasop%C3%A7%C3%B5es...), opção **"Preferência de Cores"**.

Essa tela irá receber também as notas de Transferência (entrada) originadas do [Portal de Movimentações Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109593-Portal-de-Mov-Internas) (botão Outras Opções, Enviar para WMS (Recebimento)).

**Importante:** em consequência da inversão da atualização de estoque configurada na TOP (Entrar), a atualização de estoque no lançamento da nota de transferência sofre uma inversão, de modo que, teremos a atualização de uma Baixa no local de Destino e de uma Entrada no local de Origem.

**Observação:** o parâmetro **"Exigir cadastro de volume por usuário no WMS? - WMSVALCODVOLUSU"** por padrão, é apresentado ativado, sendo necessário que sejam cadastradas as unidades dos produtos nas configurações por usuário no WMS. Se o parâmetro for desativado, não será necessário efetuar o cadastro, sendo possível que a pessoa tenha acesso a qualquer unidade no WMS.

**Observação:** quando o parâmetro **"Validar estoque da doca no recebimento? - WMSVALESTDCAREC"** estiver habilitado, o sistema irá bloquear a quantidade que ainda estiver na doca aguardando para ser armazenada, pois é possível que um recebimento seja para atender a quantidade completa do picking. Assim, o que sobrar do recebimento deverá ser encaminhado para o endereço de pulmão. Lembre-se que é possível consultar a quantidade bloqueada na coluna **"Bloqueado no WMS"** do painel **"Detalhes de estoque"** (Tela [Consulta de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353)).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#top)

## Grade Itens da Nota

Nessa grade são apresentados os itens da nota correspondentes ao recebimento, de acordo com cada linha selecionada na grade recebimentos.

![Imagem 5: Nessa grade são apresentados os itens da nota correspondentes ao recebimento, de acordo com cada linha selecionada na…](https://ajuda.sankhya.com.br/hc/article_attachments/36442456160407)

O botão **"Confirmar"** dessa grade ficará habilitado caso as notas do recebimento não tenham sido automaticamente confirmadas e estejam com a coluna **"Situação"** igual à **"Problemas na confirmação da nota"**. No processo de conferência do recebimento, o sistema realiza a confirmação da nota de compras de forma automática, porém, se existir algum problema na conferência, o sistema não confirmará o documento e a linha na grade **"Itens da Nota"** terá a coloração **Vermelha**.

Como mencionamos, através do botão Confirmar você realiza a tentativa de confirmação da nota, caso ela se encontre na situação Problemas na confirmação da nota. Ao acionar o botão, se a nota ainda não estiver confirmada, através do botão [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#bot%C3%A3ooutrasop%C3%A7%C3%B5es...), opção **"Histórico de confirmação da nota"**, você pode verificar a causa da não confirmação do documento; essa opção apresenta um pop-up de mesmo nome, contendo o campo **"Mensagem"**, que exibe o detalhamento da obstrução de confirmação da nota, permitindo assim, sua efetiva correção.

**Observação:** quando o produto da nota possuir a opção **"Número do lote"** do campo **"Controlar por"** do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-abacontroleadicional) configurado, é preciso informar o número de lote do produto ao enviar para o Recebimento de Mercadorias.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#top)

## Botões no topo da tela

#### Botão "Tratar Divergência"

Ao acionar o botão **Tratar divergência**, é exibido o **modal**a seguir.

![Imagem 6: Ao acionar o botão Tratar divergência , é exibido o modal a seguir.](https://ajuda.sankhya.com.br/hc/article_attachments/36442456162711)

---

#### Botão Mais Opções

- Apenas na tela do design system, é possível controlar a visibilidade das opções existente no botão **Mais opções**, exceto o sub-menu Preferência de cores. Para isso basta acessar a [tela de acesso](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603234-Valida%C3%A7%C3%A3o-de-Configura%C3%A7%C3%B5es-do-WMS), procurar por Recebimento de Mercadorias, adicionar o usuários e realizar a configuração para cada uma das opções contidas neste botão.

![Imagem 7: Apenas na tela do design system, é possível controlar a visibilidade das opções existente no botão Mais opções , exceto…](https://chat.google.com/u/0/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AOo0EEWzf2ntav0POiuXbhaChwybY5OVkF1UIXUnVA95lAZlxt3Qrsh6t%2FwLus2LAHaj8YBsO5ab55YwnEjfGY0sFcGCIxkaEYKMMqv0jmzL%2F41V1Aep3UUZYpQ7rWKw1Iy0q6SaYVitQoO6ecIrDTNEnz1o7Gu0IDLYPKBz6kwY9dOEnyzAq1mJCjMlnhPEYRp5JgKSZWj%2FNS4JKUMreZfu9nf50qHpTrkOpBsK43qfxs12kBgrZw2%2FCG1phsSz%2FZJ%2B6jkZnJzyPvM05dZ2F5r9kFW3V5q6zQVWx7X2miZL4ytMoH3KUA15vWN7eZnqDNNF283GVkqO4fqckltVsw1JLqfiwRSL3ZcBifDM9GmU6w%2FNfoH8qHKVgJEsdVZ%2FL5NyKRrO3HsqOEupVCTv61FvnGyVMp5ky44SdHWKtr0vXzkRMMCsq3j5HolfK7wUwQiiLMyJQyqISaQt2Le3HiNWPvpPWI1RW7HVNtq4SWEcr86Ikyu%2Bi2FLpAhhIHpNCG4fatBPqRQd1phRIZdEHIdM9goDNURU2jYK7dcvz7BWt4g4fEFoEb7LynSrFxrOEAjlGNKtmzYD%2BmK1hYKwLDaRflkMzoge6nSQ7EqWTEsIpQMSoPcw&allow_caching=true&sz=w1919-h969-rw)

- Este botão disponibiliza as seguintes opções:

**Liberação da Doca**

A utilização dessa opção é apenas para os recebimentos que estejam na situação **"Armazenado"**; Ao ser liberada, a situação assume o status de **"Concluído"**. Caso seja solicitada a liberação da doca, mas o recebimento não esteja corretamente finalizado, será exibida uma mensagem informando que a doca não pode ser liberada.

| ``` Dica: Caso o parâmetro "Liberação Automática de doca de entrada no WMS - LIBAUTDOCENTWMS"  esteja ligado, após armazenar todos os produtos a doca de entrada será liberada automaticamente. ``` |
| --- |

**Cancelar Recebimento**

Essa opção só cancela os recebimentos que ainda não tenham iniciado o seu processo de armazenagem, ou seja, recebimentos que nenhum dos seus produtos tenham sido armazenados.

**Histórico de confirmação da nota**

Essa opção exibe um pop-up de mesmo nome contendo informações referentes às tentativas de confirmação da nota, caso ela não tenha sido confirmada automaticamente. O pop-up apresentará o Número do Recebimento, o Número Único da Nota, a Data da Confirmação, o Código e Nome do Usuário que realizou tal procedimento e a Mensagem que está sendo a causa da não confirmação da nota.

**Preferência de Cores**

Ao acionar essa opção, será aberto um pop-up de mesma nomenclatura, para que você possa personalizar as cores do texto e o fundo das linhas na grade de Recebimento, de acordo com a Situação de cada um, ou seja, linhas referentes a Recebimentos Enviado para armazenagem, podem receber uma cor, Concluídos outra coloração e assim sucessivamente. Essa personalização pode ser feita de forma individual, onde cada pessoa poderá realizar da forma que preferir.

**Observação:** a configuração de cores deve ser realizada somente em HTML5. Caso contrário, se você acessar a tela em flex com essa configuração, ao retornar para o novo layout, as cores manterão o seu estilo padrão.

![Imagem 8: Observação: a configuração de cores deve ser realizada somente em HTML5. Caso contrário, se você acessar a tela em flex…](https://chat.google.com/u/0/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AOo0EEVNHeLHWtd1up9elP6P%2FHRBc8FeGqgWOsrawW2CcpkU6M0VCHYNo5Y0X833v2ae7l%2BIpxJQsFALi6KRVXoZRHCbqkhAuSCmW5NsC8oCVB%2FXfPY9KBwkA5UsdTsoLWRcpyT2Mj9b1Tlqw%2BIUgTHL6QQ%2BHM8XpRmYrCarRr4lsgcjNsx3kMl3gXxGZe2RtdQzKA8Vplz0OIJl6xwMYb4M%2FwEWiCqgGeTY9xq69eGRkp3g2u1ZMOuXWbyknOciq4m6YYPTPyO%2BakyJr3PVAJG5PwvSyDWtt6d6nykijuNLhDzN2ZS%2BWEGvnXQtqlejto8ogHf%2FIQPManV0%2BB3S2vZl0IN%2FeyXlXFZF9j4omqKRZ8m9RfewYRgnlLzq1Oorm%2Bc3REyZpkuDYbBjjadlzF8ByQyv3PJJKtCb8BvPQRULLw%2F8zykW2jeuYpLZyMA%2FcXi57h5lWbxMr%2F3dHLnbtT3mBp%2BKpWXapLjYHi0aCd6Jorrk%2B%2BmVZTIPK%2FphNsNntjwnhJcmns7AXbHvxNsfH9AjBRUGZnNsA6%2Bs4HBCA9BfGQt%2BduJsLM%2BjXzFXm%2BewVUi045aXvRe9UI1c15EBJU5YUrqo56%2Bvb%2FItAqn%2BHUlwuA%2FR5To%3D&allow_caching=true&sz=w1919-h969-rw)

![Imagem 9: (voltar ao topo)](https://chat.google.com/u/0/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AOo0EEW17zc0eDnCs6%2FRjpbL5L9UODE0f2q6Mfqx%2F%2B67C7KnIr4oKgoWKxOVW%2FbnyXHz69lBQNyQ8XA9VLDah8oRQzLBt%2FVnonwRqNZWasVjmyGuA9wEVIBSYtQGFgc1FKnixldZE6UNTqKvxZRecqfdt6njAFE3o6PIFudZHXzhuCrQ60mM7RHf9bj5DD4myCCHm%2FcsZ1dFrb2wUGaalpPpFhLyCmrXStvchzcd2yZkXBbhL6woDmJYkASbqcn1Fvq0TLr8ZNsDYKrAv9yyKwGAz9DkYlAAx3oyFzt6vk%2BjK3E52FM%2FMlLTCP7zwFu4TfRdIFncSOCRLcKTc2xPRbBr%2BwyE0VasAlldpowX45HFp61gp0iUjSl%2Fuhi1PXxQ%2Fzc43%2FZEWoSxGqXbO5Dae2hvFlmrgAoFsf0oOvuoXioMorAcblSEktp50aPO1Ec6gmAlEw7jqwb6oCPpOK22WS3Et6NLhqbT%2FYsPfiIc2y9ZY80rmbY%2B77G4t7sskMpcuPw5MuFFYkdHfnBHw15z5zZmROjwOT9MUlz60sELi424%2FX7wYRqnd7TcwbnbHJLJyjwLpTv0B09aK5RuMNrvlqplqHuIrZuacXlnEfo1kObUBuRuVdf6&allow_caching=true&sz=w1919-h969-rw)[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#top)

---

#### Gerar Tarefas

O botão **"Gerar Tarefas"** será habilitado quando o recebimento for conferido com sucesso, sem nenhuma divergência ou nenhuma recontagem pendente. Essa opção é um atalho para a tela de [Tarefas de Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613334-Tarefas-de-Recebimento), onde são efetivamente geradas as tarefas de armazenagem para os produtos do recebimento. Podemos trabalhar somente com um recebimento por vez para essa opção.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#top)

---

#### Divergência

O botão **"Divergência"** será disponibilizado para os recebimentos que apresentarem alguma divergência durante a sua conferência. Quando você acioná-lo, será apresentado o pop-up **"Divergências na Conferência"**, mostrando as conferências que estão com alguma divergência. 

Através do pop-up de divergência do recebimento e por meio das colunas da primeira grade do pop-up, você poderá ainda visualizar as seguintes informações:

- Unidade padrão;
- Qtde Unidade de Compra;
- Unidade Compra;
- Qtde. Falta;
- Qtde. Sobra;
- Qtde. Shelflife C/ Avaria;
- Qtde. Shelflife S/ Avaria; entre outros.

![Imagem 10: Qtde. Shelflife S/ Avaria; entre outros.](https://chat.google.com/u/0/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AOo0EEUoGTXg%2FvZycDNhkisoOFDuaGafktPIbDRv6BuVkMomLHI7XN6W3hv4mqVLL6xlJ9lHMB4meSGhr3Lxqwyhcl18VHWW7ggvEmGjqJNd2mfBYyqERvf%2FADLqfocSeZLU5yV4bx3Biwv8bZNYqFhyQvxtJ%2BNahzA0hPTNzf5dinU2ivOK1J5oj2LwRW6wOBlinPBEptiWHk8f3WeLdf8QOF2%2Bzqt37rECOs82BVBl2eCQWLehQrdjExCdddYM4EGT2obJqxDj3ecq76FVYDRJm4%2F6Rzdw44NnmY%2B%2Bvv%2FMUJ9uhr7lwcsR67IxEmCvmTwG5orDz7f9E6479GNM3wenNbIAObTUFIqK3mOEqOFYcL%2FwBlOzyAl6zugG%2B5sSEh0xp3n1XhFf7UtNWgzlwhE0zLs8RTPMCWvJzCXNkeh%2F7TVP2VZiDisGoLMwmsmcnd1aXDf8Pek6awbIh1s%2FtpzPA7Mw5cN4lrwqIjcb7VmED3jHEfApY0NH0lemevIpL49rvlkRCrvhx%2B7L%2FxDQSLsLRUwJNlhFvfrDJz9yV007VlNM4uir%2FdlhHpn1Gmt6tHlrBy5EfqgpcPPItvF7KOiFOxYXseSq%2F3cEz34bYnzrILfNrkU%3D&allow_caching=true&sz=w1919-h969-rw)

Na parte superior do pop-up, estão localizados os botões para que o gestor do armazém escolha qual a melhor ação a ser tomada para cada divergência. As informações do recebimento com divergência são apresentadas nas grades. 

**Nota:** é necessário que o lote informado no momento da conferência seja o mesmo informado na Nota Fiscal e, assim, caso a quantidade seja menor ou menor do que a negociada na Nota Fiscal, o sistema apresentará a divergência ao processar o recebimento. 

Cada botão realiza uma ação diferente para a divergência. Abaixo, trouxemos sobre o comportamento de cada um:

| [Recontar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#recontar) |  | [Avaria](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#avariadevolveravaria) |
| --- | --- | --- |
| [Item](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#itemdevolveritem) |  | [Falta (Devolver Falta)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#faltadevolverfalta) |
| [Falta e Avaria](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#faltaeavariadevolverfaltaeavaria) |  | [Qtd. Div. Shelflife Min.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#Qtd.Div.ShelflifeMin.) |
| [Aceita Falta e Avaria](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#aceitafaltaeavaria) |  | [Diferença](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#diferenaaceitardiferena) |
| [Avaria](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#avariaaceitaravaria) |  | [Falta (Aceitar Falta)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#faltaaceitarfalta) |

**Recontar**

Esse botão é utilizado em casos que você deseja que o item seja recontado, para confirmar se realmente existem diferenças ou se ocorreu algum erro humano na contagem. O mesmo produto pode ser recontado quantas vezes o gestor do armazém desejar ou até que ele não tenha mais divergência com a quantidade informada na Nota Fiscal.

**Nota:** quando uma tratativa de recontagem for selecionada para uma divergência, é necessário realizar, primeiramente, a recontagem, pois o sistema apenas realizará as demais tratativas quando não houver mais nenhuma recontagem pendente para os produtos com divergência.

**Importante:** além da obrigatoriedade de efetuar a marcação **"Utiliza recebimento parcial?"** presente na aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abawms) das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa) e na aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abawms) do [Cadastro de Tipos de Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (essa marcação possui a mesma denominação em ambas as telas), para utilização da funcionalidade de Recebimento Parcial de produtos, você deve efetuar a baixa de dois arquivos que correspondem ao Modelo de Mapa de Recontagem; esta baixa é realizada no [Sankhya Place](http://place.sankhya.com.br/#/login); de posse desses arquivos, ambos devem ser salvos/configurados na tela [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados) de modo que seu **"Código"** deve ser inserido no parâmetro **"Código do modelo do mapa de recontagem. - CODRELRECONTA"**. Além disso, para posterior impressão do mapa de recontagem, no parâmetro **"Impressora padrão para o mapa de recontagem. - IMPMAPARECONTA"**, você deve informar o equipamento padrão responsável pela realização das impressões.

Ao selecionar o botão Recontar quando houver uma divergência no Registro de conferência, o sistema irá verificar se há tarefas para o recebimento em questão e, ao ![Imagem 11: Ao selecionar o botão Recontar quando houver uma divergência no Registro de conferência, o sistema irá verificar se há…](https://ajuda.sankhya.com.br/hc/article_attachments/16923727097623) **"Confirmar"** o registro, caso houver, o recebimento não será executado e o sistema exibirá a seguinte mensagem:

**"O recebimento não pode ser processado porque existe tarefas de armazenagem em execução e existe a solicitação de recontagem. Aguarde a(s) tarefa(s) ser executada(s) e realize o processamento novamente."**

Porém, caso a marcação **"Utiliza recebimento parcial"** da aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abawms) da tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) for desabilitada, a validação acima não ocorrerá.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#divergncia) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#top)

**Avaria** **(Devolver Avaria)**

Esse botão deve ser utilizado quando a conferência apresentar uma divergência de avaria, ou seja, quando for informada uma quantidade avariada no coletor no momento da conferência, assim, você pode devolver essa quantidade avariada. Ao passar o mouse sobre o botão, o sistema irá propor a devolução apenas da quantidade registrada como avaria na conferência para o item da seleção.

Dessa forma, ao selecionar este, haverá a geração de uma nota de devolução de compra com a quantidade avariada para devolução.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#divergncia) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#top)

**Item** **(Devolver Item)**

Quando você passar o mouse nesse botão, o sistema irá propor a devolução da quantidade total do item na nota. Desse modo, ao notar qualquer divergência, o gestor do armazém pode acionar o botão **"Item"**, gerando assim, uma nota de devolução de compra com a quantidade total daquele item selecionado.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#divergncia) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#top)

**Falta** **(Devolver Falta)**

O botão apresentará a proposta de uma devolução da quantidade dada como falta na conferência compatada à quantidade esperada na nota quando você passar o mouse nele.

Assim, quando houver uma conferência que apresentar divergência de falta, você pode realizar a devolução da quantidade faltante. Esse botão também irá gerar uma nota de devolução de compra com a quantidade apresentada com falta.

**Nota:** se na mesma conferência também for registrada uma quantidade avariada, caso o botão **"Falta"** seja acionado, o sistema entenderá que a quantidade informada como avariada será aceita e enviada para o endereço cadastrado para Avaria.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#divergncia) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#top)

**Falta e Avaria** **(Devolver Falta e Avaria)**

O sistema irá exibir a informação de proposta de devolução da quantidade dada como falta e avaria na conferência comparada à quantidade em falta quando você passar o mouse em cima do referido botão.

Dessa forma, nos casos em que a conferência apresente quantidade avariada e também quantidade faltante para um determinado produto, ao utilizar o botão **"Falta e Avaria"**, fará com que o sistema aceite a quantidade conferida e gere uma nota de devolução de compra com a quantidade avariada somada à quantidade que está em falta. 

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#divergncia) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#top)

**Aceita Falta e Avaria**

Através desse botão você poderá tratar divergências simultâneas no processo de recebimento de devoluções de venda, ou seja, ao realizar a conferência dos produtos, poderá aceitar uma falta parcial e uma avaria de um item simultaneamente, onde, ao concluir a tratativa, ela será enviada para a tela [Tarefa de Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613334-Tarefas-de-Recebimento) e os armazenamentos poderão ser realizados em seus devidos locais, podendo ser um endereço de perda, avaria e armazenamento dos produtos.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#divergncia) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#top)

**Qtd. Div.Shelflife Mín.**

Ao passar o mouse por este botão, o sistema irá propor a devolução da quantidade registrada com shelflife dentro do mínimo permitido no Cadastro de Produtos. Assim, você poderá devolver o produto que contém a divergência de shelflife com a quantidade mínima configurada no campo **"Shelflife mínimo"** da aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abawms) na tela [Cadastro do Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-). Assim, ao clicar no botão **"Qtd. Div. Shelflife Min."** o pop-up Divergência irá atualizar a coluna **"Qtde a Devolver"** com a mesma quantidade informada na coluna **"Qtde Divergente"** na grade superior. Caso você insira outra quantidade diferente daquela na coluna Qtde a Devolver, o sistema exibirá a seguinte mensagem:

**"Os dados do campo "Qtde a Devolver" é incompatível com a quantidade a devolver real, altere os dados para prosseguir."**

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#divergncia) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#top)

**Diferença** **(Aceitar Diferença)**

No pop-up de informações desse botão, o sistema irá propor a aceitação da diferença quando a conferência registrar uma quantidade superior ao esperado na nota e criar uma nota complementar de entrada e/ou aceitar itens com shleflife fora do prazo mínimo configurado.

Assim sendo, em uma conferência a quantidade conferida de um produto for maior que a quantidade desse produto na nota de compra, o botão **"Diferença"** possibilita a geração de uma nota complementar (outra nota de compra) com a quantidade que foi conferida a mais.

**Observação:** durante a execução da rotina de Recebimento de Mercadorias, caso ocorra uma ação de **"Aceite da diferença"**, na confirmação das atividades em que existiram divergências de sobra, se o produto estiver em múltiplas notas do mesmo recebimento, é possível selecionar qual dos pedidos será utilizado para geração das notas de ajuste.

Ao se deparar com essa situação, no pop-up **"Divergências na Conferência"**, a sobra será apresentada com a tratativa **"Recontar"** e, ao clicar no botão **"Aceitar Diferença"**, é exibida uma nova coluna na grade inferior do pop-up denominada **"Selecionada"** e um botão **"Selecionar"** acima desta grade.

Quando você definir o pedido desejado para geração do ajuste, acione o botão Selecionar; uma marcação na cor verde é apresentada na coluna **"Selecionado"**, o que indica que aquele pedido será utilizado como origem para geração da nota de ajuste.

**Nota:** caso em uma conferência de entrada haja sobra e avaria juntas, será possível tratar as duas através do botão Aceitar Diferença.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#divergncia) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#top)

**Avaria** **(Aceitar Avaria)**

Nas conferências feitas pelo coletor que apresentaram quantidades avariadas, por meio desse botão, o sistema irá receber a quantidade informada como avariada na conferência. No momento em que forem geradas as tarefas de armazenagem para os produtos, esses produtos avariados serão enviados para o endereço de avaria cadastrado para a empresa.

Na primeira grade do pop-up de divergência, são exibidas as informações dos produtos com divergência. Para definir qual a tratativa para cada item, o gestor do armazém deve selecionar as linhas que deseja e clicar na ação que melhor se adapta. Caso as divergências selecionadas não sejam compatíveis com a tratativa escolhida, será exibida uma mensagem de aviso alertando sobre o ocorrido.

Já a segunda grade contém as informações da Nota/Pedido ao qual o produto pertence. Podem ser exibidas uma ou mais notas, se o produto estiver em mais de uma nota que tenha sido conferida com divergência.

Quando for feita a opção por uma tratativa de devolução, é necessário que você informe no campo **"Qtde a devolver"**, a quantidade correspondente a devolução.

**Nota:** como nessa grade podem existir mais de uma nota para o produto, atente-se para informar a quantidade para a nota correta.

Com todas as tratativas devidamente escolhidas pelo gestor do armazém, para confirmar todo esse processo, basta clicar no botão **"Confirmar"**.

É possível ainda realizar a devolução de todos os produtos que foram enviados para a conferência. Realize esse procedimento através do botão **"Devolver Tudo"**, assim, será gerada uma nota de devolução de compra em que todos os produtos de todas as notas do recebimento serão devolvidos.

Ao realizar uma devolução de divergência ou qualquer outro tipo de devolução, o sistema irá utilizar a TOP informada no campo **"TOP p/ devolução de mercadorias"** nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893) aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abawms); se esse campo não estiver informado, o sistema verifica se na TOP de origem, ou seja, se na TOP de compra existe uma TOP de devolução de compra informada nos [Cadastros de Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral); caso afirmativo, essa TOP de devolução de compra será utilizada.

**Observação:** o sistema verifica, primeiramente, se houve o preenchimento do campo **"TOP p/ devolução de mercadorias"** nas Preferências da Empresa aba WMS; não estando preenchido, verifica a segunda possibilidade acima mencionada.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#divergncia) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#top)

**Falta (Aceitar Falta)**

![Imagem 12: Falta (Aceitar Falta)](https://ajuda.sankhya.com.br/hc/article_attachments/1500001892862)

Esse botão apenas será exibido quando o recebimento de mercadorias for decorrente de um pedido de devolução de venda. Dessa forma, será possível Aceitar a Falta de produtos quando ocorrer a divergência na conferência do recebimento.

Assim, ao Aceitar a Falta de produtos em um recebimento de devolução de venda, a diferença entre a quantidade na nota e a quantidade conferida será contabilizada no estoque do endereço de perda da empresa, sendo possível consultá-la através das telas [Estoque / Endereçamento WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120393) e [Consulta Estoque com Ocorrências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613094).

**Nota:** quando essa rotina ocorrer, não será permitido realizar a devolução tanto do item quanto da falta, apenas recontar e aceitar a perda.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#divergncia) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#top)

---

#### Ver Tarefas

Clicando no botão **"Ver Tarefas"**, será exibido o pop-up **"Detalhe Tarefas Recebimentos de Mercadorias"** onde serão apresentadas todas as tarefas que estão relacionadas ao recebimento que foi selecionado na grade de recebimento.

![Imagem 13: Clicando no botão "Ver Tarefas" , será exibido o pop-up "Detalhe Tarefas Recebimentos de Mercadorias" onde serão…](https://ajuda.sankhya.com.br/hc/article_attachments/360100788854)

**Observação:** dado que há tarefas de Armazenagem, Armazenagem Expressa ou Armazenagem Seletiva em aberto na doca do respectivo recebimento no coletor de dados para SKU/UMA's, e o parâmetro **"Movimentação por unitizador (UMA)? - WMSMOVUNIUMA"** estiver desativado, não será possível executar as tarefas, de forma que, o sistema exibirá a seguinte mensagem:

**"A tarefa não pode ser executada. Existe recontagem em aberto nesta doca para este SKU/UMA. Contate o conferente para finalizar e assim poder prosseguir o armazenamento."**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#top)

---

#### Ver Peso e M3

Acionando o botão **"Ver Peso e** **M3"**, será aberto um pop-up conforme exibido na imagem abaixo, onde podemos verificar os detalhes referentes ao Peso e M3 (metro cúbico) dos recebimentos.

![Imagem 14: Acionando o botão "Ver Peso e M3" , será aberto um pop-up conforme exibido na imagem abaixo, onde podemos verificar os…](https://chat.google.com/u/0/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AOo0EEXC%2BbKIYGpQ07cAwIk0KaLoZVAuAtQK%2BEeyREKxp0gQw2D2ek0fVf7QF5s6ysmOX30sCIjma4a%2BqerV82eyYjx3AeGPGOsltuSJqmKBNXjYTuJWKHVs%2FcvN%2BrWw%2Fz7HRDDh0gEIH0xKZ0FwrXNmg2cog9vPYr3G%2B4INHLoudSVF1Y%2B6KNXoJTrTtlWtDCvIq4z6uPHwYYAgKZ6J8z3aIIFU1TxCJ3n2fTjwMZWotPrAkPCSPxwBNroiXtCIJPb80rnDm%2B7FHKh%2FC5kinidhCsqVE%2BU5TUeK4CirQ2kygO3lTkAUEfBJrnGk2m0dbLysjqjEHYIA7ch6J1qknJinOyaVPttlPao8iC2KsEbTD1b2PeJ5P%2FyWXSkptYXfpRXgCeUBKFvIMojdCaePVZhiKGhRdimbTvWUAGPE8oZ9GiGNMGUE1Nde%2BJQzuHfp%2FIyIofynfK2GzIZZ2uDveRtWDXIxh3Y1UyeCgCsWCK%2FKbbOgmPpgqfqiqUOtf8aTGYLl%2FmnZJd4T2IN6fHEuHPKN2VjFtBMwXcC5adqXyjAkaRB4Srr2mDjLf8zslAfD%2Fd3zJt6e%2Fm0on%2BWo7tUkEuN783WL665u3P%2BiHSG02vYmywCIRzdI&allow_caching=true&sz=w1919-h969-rw)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#top)

---

#### Exportar grade para PDF

O botão **"Exportar grade para PDF"** disponibiliza as opções de **"Exportar para PDF"**, **"Exportar para Planilha"** e **"Exportar para Cubo"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#top)

---

#### Conferências

Esse botão será habilitado apenas quando existir uma conferência para o recebimento selecionado.

Ao acionar esse botão, será aberto o pop-up **"Detalhes Itens Conferências"**:

![Imagem 15: Ao acionar esse botão, será aberto o pop-up "Detalhes Itens Conferências" :](https://chat.google.com/u/0/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AOo0EEWShVDVdCACvPx%2F8Q0y2st5SZvNL83BwPsXgE6LdLrIY3xm2gT54wvJyPLR6loOXv2ukvq4W2oew2hiTfWZ0Rjzt3RrsoFXiQszx1JnP7ylPjq5YEyd%2FtWtEs6iGAWyjWx1fx62HjTKRlOXJKU3H0aRviDH89zvCZMPmF3wakvBa7dL1rxggVaOSKeqF0tRBr9AkrLlTO%2FfJkjULoRTEU2U0zb98XooJADY9ooA%2BWH%2BQkXeqSouPKPD7KuC7v9wYe4uuixg9VfFWKX7oa6jxCsMybpz3m6H85QkMSHJkJ%2BGcUdWNKGcvG3%2B4GmD7U2QxqefOsO8iT2shlcwdI6vobA3NSOidisty90ZlATvW3orwzNLsPtRjIBro%2F5ZaM246WxWX5emOjqdHG9%2F%2Ffxr4YQDRfvAYTH7hvQvj%2FA%2FJ5uQDwgqFfLuP6ask1AU03XoZbCc9KqPKa%2FeXR3Rj16vHiKOGbTAuYYP1HDsVca9lFUmirATS%2FcwF6xxLlCsC1AvtQTSfldkjMiSum2%2B61yY7eRORf3YSnVHqK4uFMWAw7iPvrxoA3Z83JERn8c0rE2DBBY5YThOuWz4YGEOsqXrXeVjW1R1Dgv%2Fe%2F7SnRf%2BtDvvZSjK&allow_caching=true&sz=w1919-h969-rw)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#top)

---

#### Atualização Automática

Através do botão **"Atualização Automática"** você poderá configurar o tempo em segundos para atualização da tela Recebimento de Mercadorias.

⚠️ Observação Importante: Este botão e sua funcionalidade de temporizador não estão disponíveis no novo layout da tela (Design System - DS).

![Imagem 16: ⚠️ Observação Importante: Este botão e sua funcionalidade de temporizador não estão disponíveis no novo layout da tela…](https://ajuda.sankhya.com.br/hc/article_attachments/4406664463639)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#top)

## Portal de Compras

A partir da utilização da tela Recebimento de Mercadorias, no Portal de Compras é possível realizar o cancelamento de uma nota de devolução que foi gerada pelo WMS. Quando for solicitado o cancelamento de uma nota de devolução gerada pelo WMS, será exibido um pop-up para confirmar o cancelamento da nota com a seguinte mensagem:

**"Esta nota foi gerada por uma devolução de compra no WMS. Ao cancelar/excluir esta devolução será gerado um novo recebimento no WMS, para receber os itens que tinham sido devolvidos."**

No pop-up você pode **"Confirmar"** ou **"Cancelar"** a operação; se a escolha for para confirmar o cancelamento, o sistema cancela a nota de devolução e cria um novo recebimento com os itens dessa nota de devolução. O recebimento é gerado utilizando a nota que deu origem a nota de devolução.

O Sankhya Om não possui suporte para realizar o cancelamento de mais de uma nota de devolução de compra gerada pelo WMS, ou seja, é necessário que você realize o cancelamento nota por nota; caso contrário, será exibida a seguinte mensagem:

**"Foram selecionadas mais de uma nota de Devolução de Compra gerada pelo WMS. Por favor cancele uma nota por vez!"**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#top)

## Parâmetros que influenciam essa rotina

Quando o parâmetro **"Permite continuidade na conferência do recebimento - PERMCONTCONFER"** estiver habilitado, será possível que você pause e retome posteriormente, a conferência de mercadorias pelo coletor do WMS.

**Observação:** ao confirmar a pausa da conferência, os dados registrados até o momento não serão perdidos. Para retomar a conferência, basta selecionar a funcionalidade de conferência no coletor e o sistema irá direcionar automaticamente para a doca de entrada cuja conferência está em pausa; em seguida, um pop-up será exibido para confirmar qual ação você deseja executar, este conterá a seguinte mensagem:

**"Existe uma conferência em andamento. O que deseja fazer?"**

Assim, você poderá executar as seguintes ações:

Ao clicar em **"Enviar"**, os dados anteriormente informados serão enviados para validação e, a partir desse momento não será mais possível retomar a conferência.

Clicando em **"Cancelar"**, o sistema irá te direcionar para a tela do menu principal do coletor e os dados da conferência pausada serão mantidos.

Por fim, clicando em **"Continuar"**, você irá retomar a conferência pausada, dando continuidade ao processo.

**Nota:** a continuidade da conferência pode ser feita pelo mesmo responsável pela pausa ou qualquer outra pessoa que esteja envolvida na conferência inicial.

Além disso, com o parâmetro **"Usar Detalhamento DtVal na Divergencia de Rec.? - DETDTVALDIVREC"** ligado, ao efetuar a conferência de entrada de um produto cujo controle é realizado por data de validade (shelflife) e este possuir mais de uma data, será verificada a quantidade do produto divergente, do qual, pode-se visualizar as duas validades para o mesmo produto no campo "**Dt val**" na tarefa de armazenagem.

Ao ativar o parâmetro **"Habilita tratamento especial para Produto Não Rece - WMSPRODNAOREC"**, o coletor mostrará a opção **"Registrar ausência de item"** durante a recontagem. Com essa opção, se um produto não for entregue e o usuário não tiver o código de barras para bipar, ele poderá marcar a ausência do item. Isso gerará uma divergência, permitindo que o produto seja devolvido na nota posteriormente.

Com o parâmetro **"Movimentação por unitizador (UMA)? - WMSMOVUNIUMA"** ligado, o coletor irá solicitar a doca no recebimento que possui uma recontagem pendente. Assim, informe a UMA em seu referido campo para realizar a recontagem. Porém, com este desabilitado, o coletor será direcionado diretamente para a tela de **"Recontagem"** do **"Registro de Conferência"**.

---

![Imagem 17: Informações adicionais referente ao uso do parâmetro WMSMOVUNIUMA na Movimentação pró-ativa:](https://ajuda.sankhya.com.br/hc/article_attachments/18337803091351) **Informações adicionais referente ao uso do parâmetro WMSMOVUNIUMA na Movimentação pró-ativa:**

**(1)** Com o parâmetro WMSMOVUNIUMA habilitado, ao realizar movimentações com UMA's o sistema irá validar se o produto movimentado está em um endereço e/ou UMA para, então, realizar a movimentação. Então, se o produto não for reconhecido, o sistema exibirá a mensagem:

**"Não foi possível encontrar um produto com o código de barras informado xxxxxx"**

Além disso, caso o item não pertença à UMA, o sistema o informará por meio da mensagem:

**"Produto inexistente para a UMA informada"**

**(1)** No coletor **"TotalCross"**, a cada produto movimentado, seja ele integral ou parcial, o coletor irá exibir uma mensagem o informando da efetivação da tarefa.

**(1)** A nomenclatura do campo **"Controle tipo lista"** da tela [Movimentação Pró-ativa](https://ajuda.sankhya.com.br/hc/pt-br/articles/9813125446295#Movimenta%C3%A7%C3%A3oPr%C3%B3Ativa) do Coletor TotalCross será definida conforme o inserido no campo **"Título"** do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113) (sub-aba [Controle adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113#sub-abacontroleadicional), aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113#abamedidaseestoque)). Caso o campo Título esteja sem informação, o nome padrão Controle tipo lista será exibido no TotalCross.

**(1)** Além disso, quando um item com, ou sem controle adicional for coletado, será possível visualizar se o endereço de destino possui controle de UMA. Assim, em caso positivo, deve-se informar a UMA de destino de forma que a movimentação seja feita da origem sem UMA para um endereço controlado por UMA. Porém, se o endereço não possuir esse controle, o campo **"Quantidade"** do TotalCross será preenchido com um valor conforme à tarefa, mas este pode ser alterado desde que não seja o valor 0 ou negativo.

**(1)** Ao realizar uma movimentação entre UMA's, é importante se atentar aos seguintes critérios caso o endereço esteja vazio:

**(2)** O item não pode ser movimentado para uma UMA já armazenada utilizada em outro endereço;

- - Se utilizado o botão ![Imagem 18: Se utilizado o botão "Confirmar" , a UMA a ser movimentada poderá ser destinada ao seu novo endereço;](https://ajuda.sankhya.com.br/hc/article_attachments/18370576621975) **"Confirmar"**, a UMA a ser movimentada poderá ser destinada ao seu novo endereço;
  - A quantidade máxima de UMA's previstas no endereço deve ser respeitada;
  - Ao realizar essa movimentação, há algumas restrições, como, por exemplo, se o produto pertence a um grupo de produtos, se a sua área de armazenamento é pré-determinada, se o endereço está bloqueado, entre outros.

**(2)** Porém, se o endereço de destino estiver parcialmente ocupado, tem-se que:

- - Se utilizado o botão ![Imagem 19: Se utilizado o botão Confirmar sem informar a "UMA de destino" , então a mesma UMA de origem pode ser destinada ao novo…](https://ajuda.sankhya.com.br/hc/article_attachments/18370576621975) Confirmar sem informar a **"UMA de destino"**, então a mesma UMA de origem pode ser destinada ao novo endereço;
  - A quantidade máxima de UMA's previstas no endereço deve ser respeitada;
  - Ao realizar essa movimentação, há algumas restrições, como, por exemplo, se o produto pertence a um grupo de produtos, se a sua área de armazenamento é pré-determinada, se o endereço está bloqueado, entre outros.

**(1)** Dado que a tarefa da movimentação tenha origem na coleta de itens com UMA's parciais, o campo **"Quantidade"** será preenchido com o valor conforme a Movimentação Pró-ativa. Será possível alterá-lo, mas lembre-se que este não poderá ser 0 ou valores negativos.

---

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#top)

![Imagem 20: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16922878725143) Acesse também:

[Conferência Parcial de Entrada no Recebimento de Mercadorias](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500013006861-WMS-Confer%C3%AAncia-Parcial-de-Entrada-no-Recebimento-de-Mercadorias-)

[Registro de Conferência no Recebimento de Mercadorias](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias)

[Divergências no Registro de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500012384422-WMS-Diverg%C3%AAncias-no-Registro-de-Confer%C3%AAncia)
