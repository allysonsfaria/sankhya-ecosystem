---
id: "42427428299927"
titulo: "Importação em Produtos de cliente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427428299927-Importa%C3%A7%C3%A3o-em-Produtos-de-cliente"
trilha: "PLOOMES: Automação de propostas  > Produtos de Cliente"
atualizado_em: "2026-08-11T16:14:56Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5756355", "sync_hash_99c1f1b92947"]
---

# Importação em Produtos de cliente

A importação de produtos de cliente, assim como a de outras entidades, acontece através de uma planilha montada previamente com os dados desejados. O objetivo dessa funcionalidade é facilitar o cadastro e a atualização de vários registros massivamente.

## Requisitos e boas práticas

O Ploomes faz a leitura da sua planilha de maneira padronizada, por isso, certifique-se que o arquivo que será importado atende aos critérios à seguir:

- O arquivo deve estar no formato **.xlsx (Excel)**;
- A planilha deve conter **apenas uma aba**;
- Evite formatações, fórmulas ou caracteres especiais;
- Cada **coluna** corresponde a um campo já existente da sua conta;
- Cada **linha** corresponde a um produto de cliente;
- A primeira linha é lida como **cabeçalho**, utilize-a para indicar os campos que serão atualizados;
- Certifique-se de que colunas referentes a **campos obrigatórios** estejam preenchidas;
- Para mapear um **campo múltiplo** é necessário inserir uma coluna referente ao campo **para cada valor**.

Além dos critérios apresentados acima, os produtos de cliente indicados na planilha precisam estar vinculados a um produto e a um cliente. Caso nenhum desses itens estejam criados na base no momento da importação, a plataforma irá criá-los durante a importação, mas é necessário atribuir pelo menos uma dessas entidades aos produtos de cliente.

Teste a importação com uma planilha reduzida antes de importar grandes volumes para entender se terá os preenchimentos esperados.

## Como importar

## Passo 1: Acesse o módulo de Clientes

No menu lateral do Ploomes, clique em **Clientes**.

![Imagem 1: No menu lateral do Ploomes, clique em Clientes .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2591585484/d94a71ec3e7c1b849d9759142aa4/image.png?expires=1786536000&signature=ca2fd330d0f5ba57193b039732e61bc781dbc6fc1c0ead262c955bb07aab84b2&req=diUuF8x2mIVXXfMW3nq%2BgbxWn8xMTwnySnxfpFVTZu1L4ty69CwS6fiSJd3y%0ABYdJuXQGYyBzJrwIJAxS%2FDPMBuk%3D%0A)

## Passo 2: Altere o modo de visualização

Na tela de Clientes, clique em “**Quebrar por clientes**” e altere para “**Quebrar por produtos de cliente**”.

![Imagem 2: Na tela de Clientes, clique em “ Quebrar por clientes ” e altere para “ Quebrar por produtos de cliente ”.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2591586107/f6aa2a521b3f227fe16910ef33eb/image.png?expires=1786536000&signature=bf090e2c5caf43c77654f016c4e235ad12fd12b1b4765e336306d4d24e622865&req=diUuF8x2m4BfXvMW3nq%2BgWES0UoxfIsq0Nsb6awlHCurNCYGw9rqZ1OhCvph%0AzgdBan0fWT34FuZRFzfTPAPyWIg%3D%0A)

## Passo 3: Inicie a importação

Ainda na tela de Clientes, agora com a visualização segmentada por produtos de cliente, clique em “**Menu**” e depois em “**Importar produtos de cliente clientes pelo Excel**”.

![Imagem 3: Ainda na tela de Clientes, agora com a visualização segmentada por produtos de cliente, clique em “ Menu ” e depois em…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2591587393/13bac84e237e03b2e023d84ff70a/image.png?expires=1786536000&signature=4c989231858526f50158718d691cad364c8e0e78b6e42049cb18b05ef70e7f9d&req=diUuF8x2moJWWvMW3nq%2BgZEDuSeREeyfcrHQCS5w00YCCWxFZksni05tAi6r%0A5JV57Bf5QoOv8He3rjG8HM%2Femgo%3D%0A)

## Passo 4: Upload

Será aberta uma janela pop-up, dividida em três ou quatro etapas.

Nesta primeira tela, clique em “**Fazer upload da planilha**”, escolha o arquivo em seu computador e clique em “Próxima Etapa”.

[GIF animado: Imagem 4: Nesta primeira tela, clique em “ Fazer upload da planilha ”, escolha o arquivo em seu computador e clique em “Próxima…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2593448758/3de6897c3ccc4c5372536ed0cff3/import+customer+products+article.gif?expires=1786536000&signature=2c8e1e262867acdfc4e48d6f0ef397e0100affebda441beb1e88a27825fe29f1&req=diUuFc16lYZaUfMW3nq%2BgfV1LG%2F22jgfnEFoG7ijQksJ2BklECJM0BJ6bXC3%0A5HRIDyomGOqSG5pM0yKttSmGx88%3D%0A)

Caso a sua planilha contenha clientes que ainda não tenham sido cadastrados previamente, estes serão criados à partir da importação.

Neste caso, se houver uma coluna de responsável determinada para a entidade de Clientes, o nome precisa ser escrito exatamente como no Ploomes. Caso contrário, o cliente será cadastrado sem um responsável.

## Passo 5: Mapeamento

Nesta etapa, você deve informar ao Ploomes a qual campo do sistema cada coluna da planilha corresponde.

- Primeiro, selecione a **entidade do campo** a ser mapeado (Cliente, Produto, Produto de cliente e Grupo do produto);
- Em seguida, selecione o **campo** do sistema relacionado à coluna.

Para cada entidade sendo atualizada, é importante escolher ao menos um campo para impedir a criação de dois ou mais registros idênticos na base. Para tal, ative a opção “**Detectar duplicado por este campo**”.

Dessa forma, caso um registro com o mesmo valor do campo escolhido seja localizado, este será atualizado com as novas informações e a base ficará livre de duplicidades.

[GIF animado: Imagem 5: Dessa forma, caso um registro com o mesmo valor do campo escolhido seja localizado, este será atualizado com as novas…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2593469762/2dafc55f9b8adf7e2a16722ab0bd/map+customer+products+article.gif?expires=1786536000&signature=b66b061e63e11b785fa795b40c2e8cd7681537f2a4cf5b5a980c57af6607b29d&req=diUuFc14lIZZW%2FMW3nq%2BgbegJGFnnozCrfbOBFgN6F8uq5Zdb5pYh4kykhrc%0AkvDt%2FJeSS1dZvssH6hE%2Fg68g06o%3D%0A)

## Passo 6: Configurações

Se a sua conta possuir webhooks cadastrados, essa etapa estará presente na janela de importação.

Selecione a opção “**Não disparar webhooks durante a importação**” se desejado, caso contrário, mantenha a opção desmarcada e clique em “Próxima Etapa”.

Marcar essa opção impede que seja criada uma fila de webhooks, especialmente quando a planilha importada atualiza muitos registros no sistema, o que pode fazer com que essa fila cresça constantemente.

Caso essa etapa não esteja disponível, basta seguir para o próximo passo.

## Passo 7: Resumo

Nesta tela, o sistema exibirá alertas sobre possíveis erros que podem impedir a importação parcial ou completa de determinadas linhas.

Em caso de erros encontrados, uma tabela com as linhas cujos erros foram encontrados será exibida. Verifique as colunas para localizar em qual campo o erro ocorreu e leia os alertas destacados para entender os próximos passos a serem tomados:

- Alertas em amarelo indicam erros que impedem a importação apenas de um campo.
- Alertas em vermelho indicam erros que impedem a importação da linha inteira.

Ações disponíveis nessa tela:

- **Confirmar**: prossegue com a importação;
- **Etapa anterior**: retorna ao mapeamento;
- **Cancelar importação**: cancela todo o processo para correção do arquivo, se necessário.

## Passo 8: Processamento

Após passar por todas as etapas e confirmar a importação, a etapa de processamento será iniciada e será possível acompanhar o andamento do processo até a sua conclusão através da barra de andamento e de outras informações relevantes, atualizadas em tempo real:

- Linhas processadas (total de linhas processadas em relação ao arquivo);
- Linhas processadas com sucesso;
- Linhas processadas com erro;
- Entidades criadas;
- Entidades atualizadas.

A importação pode levar alguns minutos para iniciar, especialmente em **horários de pico**, devido ao limite de processos simultâneos. O tempo até a conclusão também pode ser afetado por esse motivo, variando à depender da quantidade de itens.

Caso a tela de importação seja minimizada, você pode abrir novamente clicando no **ícone de importação** no menu superior.

Após a conclusão, a barra de andamento ficará verde, indicando que a importação foi concluída.

Além disso, uma planilha de registros ficará disponível para download contendo os detalhes da importação. Esta planilha é especialmente indispensável se alguma linha tiver sido processada com erro, assim, será possível identificar exatamente qual linha foi afetada para que seja feita uma correção manual ou através de uma nova importação.

![Imagem 6: Além disso, uma planilha de registros ficará disponível para download contendo os detalhes da importação. Esta planilha…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2591609869/e5871fd939923aa4ec8a8bbb2082/image.png?expires=1786536000&signature=f0b5f7608501259b49d37514bad996bf7dccf7453a4829c34eb7a20b9dfc84e1&req=diUuF89%2BlIlZUPMW3nq%2BgY7XrljgThrgqXufpd3ZyszDcWo7XP4MmG%2BPbZOs%0AePIgfUZfaB06nMR2eMM7HdmmW%2Fw%3D%0A)

Caso necessário, durante a importação, é possível interromper o processo clicando em “Cancelar importação”. Neste caso, não será possível baixar a planilha de registros.

Se quiser saber mais sobre o módulo de Produtos de cliente, clique no botão abaixo:

[Conheça o Módulo de Produtos de Cliente](https://sankhya.zendesk.com/hc/pt-br/articles/42427449343639)

---

## Acesse a Universidade Ploomes para saber mais

A Ploomes disponibiliza uma plataforma de educação digital criada para capacitar seus clientes, oferecendo uma variedade de cursos, shorts, casos de uso e webinars.

Abaixo você confere uma sugestão de conteúdo disponível em nossa plataforma que se relaciona ao tema deste artigo.

[![Imagem 7: Abaixo você confere uma sugestão de conteúdo disponível em nossa plataforma que se relaciona ao tema deste artigo.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2049123152/853077256ba541dbb2c1c524eaff/Teste+01.png?expires=1786536000&signature=5773498e136f11c73f085d1f2b2d97c26242fe0b1343bad24d6ad4295c3e9b95&req=diAjH8h8noBaW%2FMW3nq%2BgRoAlL2equsjVSSkqBou65IX8DgzBB6tIhbtfBPN%0ARl6fDZo8V%2BYuBlrcPBHY4bo06RY%3D%0A)](https://universidade.ploomes.com/courses/boas-praticas-para-a-importacao-de-dados)
