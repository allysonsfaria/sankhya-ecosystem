---
id: "360044603834"
titulo: "Ordem de Serviço"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603834-Ordem-de-Servi%C3%A7o"
trilha: "Manual do Produto > Contratos e Serviços > Contratos e Serviços"
atualizado_em: "2026-07-29T14:03:14Z"
rotulos: ["Produtos", "AJUDA DO SKW", "Configuração", "Parceiro", "Contratos e Serviços", "Ordem de Serviço", "Serviços", "Contato", "Compromissos", "Executante", "Responsável", "Consulta de OS", "OS", "Lançamento de OS", "Executadas", "Ordem de Serviço manual", "Atendimento", "br.com.sankhya.os.mov.OrdemServico", "Como Inserir Produtos e Serviços a um Executante", "Gestão de Atendimento"]
---

# Ordem de Serviço

| ``` ![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42311191431831) Módulo: Contratos e Serviços > Ordem de Serviço ``` |
| --- |

---

O módulo de Contratos e Serviços é uma solução para auxiliar a equipe de prestação de serviço que necessita de uma eficiente ferramenta de comunicação, gestão de atendimento e suporte.

Sua principal característica é a de dinamizar o processo de atendimento, com distribuição inteligente de carga das diferentes solicitações e, consequentemente, com expressivo ganho de escala.

A Ordem de Serviço (OS) é o principal recurso deste módulo. É por meio dela que se obtém indicadores para a análise de resultados. Os indicadores oferecidos pelo lançamento de uma OS, variam de acordo com a necessidade das empresas e, é justamente por isso, que o sistema tem flexibilidade na forma de lançamento.

Utilize a OS para descrever os problemas e soluções referentes a diversos assuntos, por exemplo, uma customização a ser criada.

**Importante:** o sistema fará uma validação no momento de salvar um item da OS, considerando o Executante, a Data/Hora Inicial e Final e o Parceiro iguais. Então, se já existir uma OS lançada nesse mesmo horário, será barrado e não permitirá salvar o item dessa OS. 

Abaixo, trataremos sobre as funcionalidades desta rotina:

[Componentes da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603834-Ordem-de-Servi%C3%A7o#componentesdatelaordemdeservi%C3%A7o)

[Modos de Visualização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603834-Ordem-de-Servi%C3%A7o#modosdevisualiza%C3%A7%C3%A3o)

[Serviços por Executante](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603834-Ordem-de-Servi%C3%A7o#servi%C3%A7osporexecutante)

![Imagem 2: Serviços por Executante](https://ajuda.sankhya.com.br/hc/article_attachments/360085884414)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603834-Ordem-de-Servi%C3%A7o#top)

## Componentes da tela

Conheça os componentes da tela, no video abaixo:

[Vídeo: tutorial do artigo](https://www.loom.com/embed/a62167c3aa2941bd9aae409c2e2dee5d)

**Informações adicionais**

Para que seja encaminhada a Ordem de Serviço por e-mail, realize as seguintes configurações:

**1.** Configure o Servidor SMTP no [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874), aba [SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874#abasmtp), ou;

**2.** Na tela [Contas SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603194-Contas-SMTP) deverá existir um Servidor SMTP configurado, ou ainda;

**Nota:** poderá ser apresentado alguns erros caso seja realizado o cadastro de um Servidor Gmail, visto que, em algumas ocasiões o serviço ou porta é bloqueado.

**3.** Na tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834), em relação ao parâmetro **"Servidor (SMTP): - EMAILSERVSMTP"**, ao inserir um servidor no campo **"Texto"**, existirá um problema onde, ao informar um Servidor SMTP válido, o mesmo entrará em uma parte do código que não passará usuário e senha do servidor.

Assim, para utilizar este parâmetro, é necessário que o servidor aceite a requisição sem autenticação.

| ``` ![Imagem 3: Dica: Para saber mais informações sobre o botão "Opções para Assinatura Digital da Sub-OS" acesse a documentação…](https://ajuda.sankhya.com.br/hc/article_attachments/42311191435799) Dica: Para saber mais informações sobre o botão ![Imagem 4: Dica: Para saber mais informações sobre o botão "Opções para Assinatura Digital da Sub-OS" acesse a documentação…](https://ajuda.sankhya.com.br/hc/article_attachments/42311178781207) "Opções para Assinatura Digital da Sub-OS"  acesse a documentação Assinatura Digital. ``` |
| --- |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603834-Ordem-de-Servi%C3%A7o#top)

## Modos de Visualização

Algumas telas apresentam dois estados de visualização, o primeiro chamado de **"Modo de Edição"** e o segundo **"Modo Planilha"**, que podem ser alternados através do botão ![Imagem 5: Algumas telas apresentam dois estados de visualização, o primeiro chamado de "Modo de Edição" e o segundo "Modo…](https://ajuda.sankhya.com.br/hc/article_attachments/360084939553) **"Alternar Layout"**.

**Nota:** tendo em vista que as informações de valores financeiros em mensagens de atraso deverão ser vistas apenas pela equipe do financeiro, utilize o parâmetro **"Mostra valor em atraso na Ordem de Serviço? - MOSTRAVLRATRASO"** para ocultar esta informação.

---

**Configurando o Modo Planilha**

Ao alternar a tela para o Modo grid, será apresentado o botão **"Configura a Visualização do Grid"** ![Imagem 6: Ao alternar a tela para o Modo grid , será apresentado o botão "Configura a Visualização do Grid" , ao acioná-lo, fará…](https://ajuda.sankhya.com.br/hc/article_attachments/360083774254), ao acioná-lo, fará com que pop-up **"Configurações da tela"** seja aberto para configurar a apresentação dos campos na tela.

[GIF animado: Imagem 7: Ao alternar a tela para o Modo grid , será apresentado o botão "Configura a Visualização do Grid" , ao acioná-lo, fará…](https://ajuda.sankhya.com.br/hc/article_attachments/4422442763543)

Os **"Disponíveis"** são todos os campos que existem na tela de agenda no Modo Planilha. Para efetuar a configuração dos campos, selecione o campo desejado e clique no botão **"Adiciona o campo"** para que o sistema carregue o campo na parte dos **"Escolhidos"**, em seguida, clique no botão **"Salvar"**.

[GIF animado: Imagem 8: Os "Disponíveis" são todos os campos que existem na tela de agenda no Modo Planilha . Para efetuar a configuração dos…](https://ajuda.sankhya.com.br/hc/article_attachments/4422436511639)

Além disto, é possível redimensionar o tamanho dos campos que foram escolhidos. Para isso, selecione o campo a ser redimensionado e, no campo **"Nova Largura"**, informe o valor desejado. Este valor não pode ser inferior ao campo **"Largura Mínima"**. Após fazer todos os redimensionamentos dos campos, clique no botão Salvar ou Salvar e aplicar.

![Imagem 9: Além disto, é possível redimensionar o tamanho dos campos que foram escolhidos. Para isso, selecione o campo a ser…](https://ajuda.sankhya.com.br/hc/article_attachments/4422445306647)

**Observação:** caso você clique no botão Salvar, ao fechar a tela, será necessário clicar no botão Aplicar da tela para que as alterações sejam feitas.

---

**Ordenação dos campos no modo planilha**

Em todas as telas onde há o modo planilha, podemos fazer a ordenação crescente e decrescente. Para isto, basta clicar no título da coluna que deseja fazer a ordenação. Para saber qual coluna está ordenada, o sistema marca a coluna com uma seta, informando se é crescente ou decrescente:

[GIF animado: Imagem 10: Em todas as telas onde há o modo planilha, podemos fazer a ordenação crescente e decrescente. Para isto, basta clicar…](https://ajuda.sankhya.com.br/hc/article_attachments/360087186013)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603834-Ordem-de-Servi%C3%A7o#top)

## Serviços por Executante

Para inserir um **"Produto"** e um **"Serviço"** a um **"Executante"** acesse a tela **"Serviços por Executante"**.

![Imagem 11: Para inserir um " Produto " e um " Serviço " a um " Executante " acesse a tela "Serviços por Executante" .](https://ajuda.sankhya.com.br/hc/article_attachments/4422446076183)

| ```  ![Imagem 12: Dica: Acesse o artigo Serviços por Executante , para conhecer as funcionalidades desta tela.](https://ajuda.sankhya.com.br/hc/article_attachments/42311191435799) Dica: Acesse o artigo Serviços por Executante, para conhecer as funcionalidades desta  tela. ``` |
| --- |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603834-Ordem-de-Servi%C3%A7o#top)

![acesse](https://ajuda.sankhya.com.br/hc/article_attachments/16077864648727) Acesse também:

[Lançamento de OS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS)

[Pendências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604254-Pend%C3%AAncias)
