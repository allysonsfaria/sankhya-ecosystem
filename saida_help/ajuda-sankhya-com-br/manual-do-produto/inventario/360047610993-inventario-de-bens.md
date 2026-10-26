---
id: "360047610993"
titulo: "Inventário de Bens"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360047610993-Invent%C3%A1rio-de-Bens"
trilha: "Manual do Produto > Suprimentos e Estoque > Inventário"
atualizado_em: "2026-07-29T14:49:57Z"
rotulos: ["Configuração", "Relatórios", "Inventário", "Importação", "Estoque", "br.com.sankhya.mgeinvent.inventarioBem", "Inventário de Bens: Funcionalidades e Processo"]
---

# Inventário de Bens

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312644513047) Módulo: Inventário > Avançado
```

---

Esta tela tem o recurso que possibilita inventariar bens, podendo-se utilizar a contagem destes via coletor de dados e, posteriormente, realizar a importação dos dados inventariados para o sistema ou proceder com a contagem manual diretamente através deste. Desta forma, o ajuste corrigirá os departamentos e garantirá a possibilidade de visualizar os relatórios dos bens que possuíram alguma divergência.

| [Aba Cópia](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047610993-Invent%C3%A1rio-de-Bens#abacopia) |  | [Aba Contagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047610993-Invent%C3%A1rio-de-Bens#abacontagem) |
| --- | --- | --- |
| [Aba Resultado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047610993-Invent%C3%A1rio-de-Bens#abaresultado) |  |  |

Tem-se nesta tela dois acessos especiais que deverão ser liberados no [Controle de Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854) (Módulos > Inventário > Avançado > Inventários de Bens). O primeiro trata-se da caixa de seleção **"Ver Cópia"**, cuja funcionalidade é permitir que você visualize a aba [Cópia](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047610993#abacopia) da tela Inventário de Bens e, o segundo acesso **"Ver Resultado"**, permitirá a visualização da aba [Resultado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047610993#abaresultado) na tela referenciada.

![Imagem 2: Tem-se nesta tela dois acessos especiais que deverão ser liberados no Controle de Acessos ( Módulos > Inventário >…](https://ajuda.sankhya.com.br/hc/article_attachments/8759249028119)

Para realizar o cadastro de um novo inventário, deve-se acionar o botão ![Imagem 3: Para realizar o cadastro de um novo inventário, deve-se acionar o botão "Cadastrar Inventário de Bens" na parte…](https://ajuda.sankhya.com.br/hc/article_attachments/8759160637719) **"Cadastrar Inventário de Bens"** na parte superior desta tela.

No painel principal, tem-se o campo **"Data Inventário"** e este será preenchido automaticamente com a data atual e ficará bloqueado para edição.

No campo **"Empresa"** deve-se inserir a empresa selecionada para realizar o inventário. Nesta sequência, aciona-se o botão ![Imagem 4: No campo "Empresa" deve-se inserir a empresa selecionada para realizar o inventário. Nesta sequência, aciona-se o botão…](https://ajuda.sankhya.com.br/guide-media/01H3J6B4CB0CY0VBCETJQMAFWJ) **"Salvar"**, fazendo com que seja gerada a cópia do estoque de bens, independente se você possui o acesso especial Ver Cópia habilitado.

Nas **"Configurações da Tela"**, representada pelo ícone ![Imagem 5: Nas "Configurações da Tela" , representada pelo ícone tem-se as opções de marcação de "Exibe departamento na contagem"…](https://ajuda.sankhya.com.br/hc/article_attachments/8759167577367) tem-se as opções de marcação de **"Exibe departamento na contagem"** e **"Limpar departamento depois de inserir uma contagem"**.

## Aba Cópia

![Imagem 6: Aba Cópia](https://ajuda.sankhya.com.br/hc/article_attachments/8759288274711)

Nesta aba, tem-se o botão **"Atualizar Cópia"**, responsável por refazer a cópia de estoque dos bens. Este botão tem o objetivo de atualizar a cópia de estoque para os casos em que já tenham algum tipo de movimentação nos bens após a criação do inventário.

**Nota:** a atualização da cópia apenas será permitida para a data atual.

Sendo assim, caso você tente realizar a atualização da cópia de um inventário referente à uma data anterior da atual, o sistema emitirá a seguinte mensagem:

**"Não é possível atualizar uma cópia retroativa".**

Ainda dentro desta aba, o botão ![Imagem 7: Ainda dentro desta aba, o botão "Exportar grade para PDF" apresentará as opções de exportação e visualização das…](https://ajuda.sankhya.com.br/hc/article_attachments/8759165855511) **"Exportar grade para PDF"** apresentará as opções de exportação e visualização das informações da tela. Pode-se **"Exportar para PDF"**, **"Exportar para planilha"** ou **"Exportar para cubo"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047610993-Invent%C3%A1rio-de-Bens#top)

## Aba Contagem

![Imagem 8: Aba Contagem](https://ajuda.sankhya.com.br/hc/article_attachments/8759344287255)

Através desta aba, realiza-se o registro da contagem dos bens. Tem-se no menu superior da aba os campos **"Departamento"** e **"Código Bem"**.

Em relação ao Departamento, deve-se inserir o departamento da empresa a ser realizada a contagem de bens.

No campo Código Bem informa-se o código do bem encontrado durante a contagem física.

Desta forma, após preencher os dois campos acima informados, aciona-se o botão **"Inserir"** para registrar a contagem.

**Observação:** caso exista o Código do Bem informado no sistema, o registro será apresentado nesta grade. Por outro lado, informando-se um Código do Bem inválido, ou seja, que não esteja cadastrado no sistema, será apresentada a seguinte mensagem:

**"Não encontrado no sistema um bem com o código: X".**

**Nota:** por meio do parâmetro **"Qtd dígitos máscara geração automática de BENS - QTDDIGGERBEM"**, o usuário poderá informar quantos dígitos o Código do Bem precisará para que seja gerado.

O botão ![Imagem 9: O botão "Excluir" localizado nesta aba será responsável por deletar o registro selecionado.](https://ajuda.sankhya.com.br/hc/article_attachments/8759173080599) **"Excluir"** localizado nesta aba será responsável por deletar o registro selecionado.

Tem-se ainda nesta aba o botão ![Imagem 10: Tem-se ainda nesta aba o botão "Outras Opções" , de forma que, selecionando-o, será disponibilizada a funcionalidade de…](https://ajuda.sankhya.com.br/hc/article_attachments/8759173705879) **"Outras Opções"**, de forma que, selecionando-o, será disponibilizada a funcionalidade de **"Importar Dados Coletor"**, que permite que você importe um arquivo **.txt**. Ao clicar nesta opção, será apresentado o seguinte pop-up:

![Imagem 11: Tem-se ainda nesta aba o botão "Outras Opções" , de forma que, selecionando-o, será disponibilizada a funcionalidade de…](https://ajuda.sankhya.com.br/hc/article_attachments/8759345988631)

No campo **"Layout"** seleciona-se o layout a ser utilizado, sendo que este, deverá ser configurado na tela [Layout de Processamento de Arquivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607054), botão **"Outras Opções"**, opção **"Criar arquivo a partir de um modelo"**.

Insere-se no **"Arquivo"** o arquivo **.txt** encontrado em seu computador.

Acionando o botão **"Processar Arquivo"** será realizada a importação da contagem do arquivo.

Sendo assim, após realizar a confirmação, será apresentado no **"Painel Resultado"** um resumo do processamento do arquivo contendo os bens que foram inseridos na contagem, bem como os bens que não foram encontrados no sistema.

**Nota:** os códigos dos bens inseridos na contagem não serão apresentados no Painel Resultado, de outra forma, os bens não encontrados no sistema têm seus códigos apresentados nesta caixa de texto.

**Observação:** caso o arquivo importado tenha mais de uma data de contagem, será apresentado no painel acima mencionado uma lista com as datas encontradas no arquivo para que seja selecionada qual a data deseja-se realizar a importação e assim, realizar o reprocessamento do arquivo para importar os registros das datas escolhidas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047610993-Invent%C3%A1rio-de-Bens#top)

## Aba Resultado

Após finalizar a contagem dos bens, basta acessar esta aba para que sejam analisados os resultados.

![Imagem 12: Após finalizar a contagem dos bens, basta acessar esta aba para que sejam analisados os resultados.](https://ajuda.sankhya.com.br/hc/article_attachments/8759346685079)

Tem-se o **"Painel de Filtros"** ao lado esquerdo desta aba, apresentando todos os bens envolvidos no inventário, tendo este como funcionalidade a possibilidade de criar filtros personalizados ou utilizar os filtros rápidos.

No Painel de Resultados será demonstrado os bens que foram encontrados, bem como a totalização da situação destes bens no inventário, sendo que estes registros serão classificados em quatro cores:

- Os registros demonstrados na cor **verde** tratam-se de bens encontrados na cópia e na contagem, e que estão inseridos no departamento correto.
- Os bens posicionados com a cor **vermelha** são os encontrados apenas na cópia, sendo que estes registros serão incluídos na nota de ajuste para que seja realizada a baixa.
- Os bens encontrados na cor **laranja**, são os localiza dos na cópia e na contagem, porém, o departamento encontra-se divergente.
- Os bens que não foram localizados no sistema serão inseridos na cor **preta**.

**Nota:** na rotina de ajuste, o departamento será acertado no sistema. Desta forma, para que seja utilizada esta rotina, primeiramente deve-se criar um Modelo de Nota na tela **"Comercial > Consulta > Modelo de Notas e Pedidos"**, com o [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), campo **"Atualização do Bem = Baixa/Venda"**.

Posteriormente à realização do cadastro do Modelo de Nota, este deve ser inserido na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Estoque/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaestoquepreo), campo **"Modelo Ajuste de Baixa de Bem"**.

No menu desta aba, tem-se que o botão **"Ajustar"** será acionado para executar a rotina que cria uma nota para realizar a baixa nos bens não encontrados na contagem, assim como para ajustar os bens que encontrarem-se com seus departamentos divergentes.

Após acionar o botão acima mencionado, será exibido um pop-up para que seja marcado se deverá ser gerada a nota de baixa dos bens e/ou ajustar o departamento dos bens:

![Imagem 13: Após acionar o botão acima mencionado, será exibido um pop-up para que seja marcado se deverá ser gerada a nota de…](https://ajuda.sankhya.com.br/hc/article_attachments/8759348615191)

Selecionando as opções desejadas, basta acionar o botão Ajustar para que a rotina seja executada.

Nesta sequência, após acionar o botão acima, será apresentado um novo pop-up informando o Número Único da nota de baixa e, de igual modo, a quantidade de bens que foram baixados e tiveram seus departamentos ajustados.

**Observação:** esta rotina de Inventário de Bens não observará os bens locados ou que estejam em poder de terceiros.

**Importante:** o Inventário de Bens não será gerado nos registros e arquivos de Inventário Fiscal, como exemplo: [Registro de Inventário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117653-Registro-de-Invent%C3%A1rio), SPED Bloco H, entre outros.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047610993-Invent%C3%A1rio-de-Bens#top)
