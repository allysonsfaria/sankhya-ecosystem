---
id: "360045109433"
titulo: "Controle de qualidade dos produtos em processamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109433-Controle-de-qualidade-dos-produtos-em-processamento"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-29T14:54:03Z"
rotulos: ["Produtos", "AJUDA DO SKW", "Configuração", "Controle de Qualidade", "Produtos Acabados", "Controle de Qualidade dos PA's manual", "Estoque", "Produção", "br.com.sankhya.mgeprod.cad.TiposAmostra", "Configurações Iniciais", "Controle de Qualidade Integrado", "Execução do Ciclo", "Qualidade"]
---

# Controle de qualidade dos produtos em processamento

Este processo representa a execução do Controle de Qualidade dos Produtos Acabados (PA's) em processamento numa [Ordem de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119313-Ordens-de-Produ%C3%A7%C3%A3o). Este processo também é denominado por Controle de Qualidade Embarcado ao Processo Produtivo, pois, a execução do controle de qualidade é representada por atividades no roteiro de produção do Produto Acabado.

Neste artigo, iremos tratar dos seguintes tópicos:

[Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109433-Controle-de-qualidade-dos-produtos-em-processamento#configura%C3%A7%C3%B5es)                                                                            [Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109433-Controle-de-qualidade-dos-produtos-em-processamento#opera%C3%A7%C3%A3o)

## Configurações

Para o funcionamento deste processo é necessário realizar as configurações a seguir:

![Imagem 1: Defina o "Tipo de amostra" que será utilizado pelo Produto Acabado que você deseja executar o controle de qualidade.…](https://ajuda.sankhya.com.br/hc/article_attachments/16115991168791) Defina o **"Tipo de amostra"** que será utilizado pelo Produto Acabado que você deseja executar o controle de qualidade. Esse cadastro é realizado na tela [Tipos de Amostra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119013).

![Imagem 2: No Cadastro de Produtos você deve realizar os procedimentos abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16116009875095) No [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-) você deve realizar os procedimentos abaixo:

- Na aba [Medidas e estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abamedidaseestoque), sub-aba [Controle Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#sub-abacontroleadicional), selecione no campo **"Controlar por"**, a opção **"Número de lote"**.

![Imagem 3: Na aba Medidas e estoque , sub-aba Controle Adicional , selecione no campo "Controlar por" , a opção "Número de lote" .](https://ajuda.sankhya.com.br/hc/article_attachments/4416660555031)

- Informe o **"Tipo Amostra"** que será utilizado para o produto em questão, na aba [Tipos de Amostra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abatiposdeamostra):

![Imagem 4: Informe o " Tipo Amostra" que será utilizado para o produto em questão, na aba Tipos de Amostra :](https://ajuda.sankhya.com.br/hc/article_attachments/4416674282647)

![Imagem 5: Cadastre um Padrão de Classificação que será a representação sistêmica do ensaio (análise) ao qual o produto deve ser…](https://ajuda.sankhya.com.br/hc/article_attachments/16115991184407) Cadastre um [Padrão de Classificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108593) que será a representação sistêmica do ensaio (análise) ao qual o produto deve ser submetido durante o processo de Controle de Qualidade. Ao Padrão de Classificação, são relacionadas as características analisáveis que devem ser consideradas no ensaio, bem como o intervalo de aceitação de cada uma delas para o produto.

![Imagem 6: Cadastre um Padrão de Classificação que será a representação sistêmica do ensaio (análise) ao qual o produto deve ser…](https://ajuda.sankhya.com.br/hc/article_attachments/4416674680087)

![Imagem 7: Por fim, na tela Processo Produtivo , por meio do botão "Outras Opções..." , cadastre os "Ciclos de Controle de…](https://ajuda.sankhya.com.br/hc/article_attachments/16116009879831) Por fim, na tela [Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314), por meio do botão ![Imagem 8: Por fim, na tela Processo Produtivo , por meio do botão "Outras Opções..." , cadastre os "Ciclos de Controle de…](https://ajuda.sankhya.com.br/hc/article_attachments/16647483836951) **"Outras Opções..."**, cadastre os **"Ciclos de Controle de Qualidade"** necessários para serem executados durante uma Ordem de Produção do processo em questão.

![Imagem 9: Por fim, na tela Processo Produtivo , por meio do botão "Outras Opções..." , cadastre os "Ciclos de Controle de…](https://ajuda.sankhya.com.br/hc/article_attachments/8365302069143)

Neste pop-up, realize as seguintes configurações:

No campo **"Descrição"**, especifique uma descrição para identificar o ciclo em questão.

Na marcação **"Permite aprovar laudos com ressalvas"**, a aplicação permitirá que o executante do laudo o conclua aprovando-o, mesmo se uma das características estiver fora do intervalo de aceitação, ficando deste modo, com o resultado igual a **"Aprovado com Ressalva"**. A consequência de um laudo com ressalva é a instância de ciclo de controle de qualidade com o mesmo resultado.

---

Agora apresentaremos os procedimentos para configurar as atividades que fazem parte do Ciclo de Controle de Qualidade (detalhes sobre as configurações abaixo através do link [Configuração de Atividades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674)).

**1-** Anexe um evento de início de Controle de Qualidade na atividade que de fato irá inicializar o fluxo secundário referente ao controle de qualidade. Na atividade em questão, você deverá especificar qual o ciclo de controle que ela deve iniciar (Configuração de Atividades, aba [Controle de Qualidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674#abacontroledequalidade), campo "Ciclo controle de qualidade").

**2-** Caso a atividade em questão não possa ser finalizada sem que o setor de qualidade aponte resultado positivo (Aprovado ou Aprovado com Ressalva), deve-se então definir a atividade com "Validar ciclo de controle de qualidade".

**3-** Defina as atividades de **"Amostragem"** e **"Laudo"**. Cada ciclo deve possuir ao menos uma atividade de "Amostragem + Laudo" ou uma atividade de Amostragem mais uma atividade de Laudo. Esta definição é realizada na aba Controle de Qualidade da Configuração de Atividades no campo "Operação a ser realizada".

**4-** Determine a atividade de conclusão do Ciclo de Controle de Qualidade. A conclusão do ciclo é algo obrigatório, que considera todos os laudos gerados para todas as amostras para o produto/lote em questão, que foram processados na Ordem e deve sempre ser sinalizado na última atividade a ser realizada no fluxo secundário referente ao ciclo de qualidade (esta marcação se encontra na configuração da atividade, aba Controle de Qualidade).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109433-Controle-de-qualidade-dos-produtos-em-processamento#top)

## Operação

As atividades referentes a um Ciclo de Controle de Qualidade devem ser executadas, normalmente, conforme as demais atividades de um roteiro. Entretanto, as ações referente a qualidade estão localizadas na aba Controle de Qualidade (informações sobre esta aba, no link [Configuração de Atividades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674)).

Durante a execução de uma Ordem de Produção, a atividade que possuir o evento de início de ciclo anexado à ela, terá o botão **"Iniciar Ciclo"** habilitado. Deste modo, tem-se a capacidade de iniciar o fluxo secundário do roteiro referente ao Controle de Qualidade. Caso a atividade seja uma atividade de amostragem, o sistema obriga que as amostras do produto sejam registradas nesse momento.

#### Amostragem

Apenas as atividades configuradas com o tipo de operação igual a **"Amostragem"** ou **"Amostragem + Laudo"** possuem acesso às funcionalidades existente na grade de **"Amostras"**:

- **Gerar:** caso seja necessário, será possível ainda gerar novas amostras do PA a partir do botão **"Gerar Registro de Amostra"**.
- **Aprovar/Reprovar:** estes botões permitem a aprovação ou reprovação da amostra em questão. Diferente do processo de [Controle de Qualidade dos Materiais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596374), a Aprovação/Reprovação de uma amostra não gera uma requisição para baixa de estoque do produto, visto que o produto ainda não existe em estoque; o resultado da amostra, será uma pequena perda no resultado final da Ordem de Produção (quantidade final apontada inferior a quantidade de produto a ser fabricado pela ordem).

#### Laudo

Apenas as atividades configuradas com o tipo de operação igual a **"Laudo"** ou Amostragem + Laudo possuem acesso às funcionalidades existente na grade Laudo.

Na tela [Controle de Laudo de Amostras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611114), você deverá inserir um novo laudo por meio do botão ![Imagem 10: Na tela Controle de Laudo de Amostras , você deverá inserir um novo laudo por meio do botão "Novo" ; para isto, deve-se…](https://ajuda.sankhya.com.br/hc/article_attachments/16647483842583)**"Novo"**; para isto, deve-se especificar o padrão de classificação do laudo em questão, de forma a sinalizar ao sistema qual o ensaio (teste) que você deseja realizar neste momento. Automaticamente ao salvar o padrão de classificação, as características analisáveis do padrão são carregadas para que o usuário aponte seus respectivos resultados.

À medida em que são apontados os resultados das características, o sistema sinaliza com a cor **azul** para o que estiver dentro do aceitável e **vermelho** para o fora do aceitável.

Após a finalização do apontamento das diversas características, você deverá sinalizar a conclusão do laudo (através do botão ![Imagem 11: Após a finalização do apontamento das diversas características, você deverá sinalizar a conclusão do laudo (através do…](https://ajuda.sankhya.com.br/hc/article_attachments/16647496321303) **"Concluir Laudo"**). O sistema considera sempre o último laudo de cada amostra como uma forma de permitir o lançamento de diversos laudos, porém, o último anula os demais como forma de correção de análises erradas anteriores.

Caso o Ciclo de Controle de Qualidade **"Permita aprovar laudos com ressalva"** e o padrão de classificação utilizado **"Permite confirmar quando laudo for rejeitado"**, então ao concluir um laudo onde alguma das características analisáveis esteja fora do intervalo de aceitação, o sistema exibe uma mensagem questionando sobre a continuidade na aprovação do laudo mesmo assim (neste caso o resultado será Aprovado com Ressalva) ou então se o laudo será reprovado (o resultado será Reprovado).

Ao final de um Ciclo de Controle de Qualidade, representado pela passagem por uma atividade que **"Conclui Ciclo de Controle de Qualidade"**, serão consideradas todas as amostras para aquele produto/lote assim como os laudos das mesmas. Deste modo, finaliza aquela instância de ciclo em questão e gera um resultado para mesma considerando o resultado do último laudo de cada amostra:

- **Se todos os laudos aprovados:** O resultado da Instância de Ciclo de Controle de Qualidade será **"Aprovado"**;
- **Se algum laudo for aprovado com ressalva:** Neste caso, o resultado da Instância do Ciclo de Controle de Qualidade será **"Aprovado com Ressalva"**;
- **Se algum laudo for reprovado:** Então o resultado da Instância do Ciclo de Controle de Qualidade será **"Reprovado"**.

#### Gerência

Todo o processo de Controle de Qualidade dos PA's poderá ser acompanhado a partir da aba [Controle de Qualidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119313-Ordens-de-Produ%C3%A7%C3%A3o#abacontroledequalidade) da tela [Ordens de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119313-Ordens-de-Produ%C3%A7%C3%A3o).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109433-Controle-de-qualidade-dos-produtos-em-processamento#top)
