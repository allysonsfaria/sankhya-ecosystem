---
id: "360044596954"
titulo: "Controle de Qualidade na Saída"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596954-Controle-de-Qualidade-na-Sa%C3%ADda"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-10-14T18:52:00Z"
rotulos: ["Produtos", "AJUDA DO SKW", "Configuração", "Controle de Qualidade na Saída", "Controle de Qualidade na Saída manual", "TOP", "Estoque", "Configurações Iniciais", "Operação do Controle de Qualidade", "Laudo Técnico Obrigatório", "Qualidade"]
---

# Controle de Qualidade na Saída

Algumas empresas tem a obrigatoriedade de emitir um laudo técnico ao comercializar seus produtos como forma de comprovar a qualidade dos mesmos. Essa pode ser uma exigência de seus clientes, ou mesmo de algum órgão fiscalizador do segmento.

O laudo técnico é um processo de qualidade onde se coleta uma amostra do produto que está sendo comercializado e verificam-se diversas características obtendo o resultado de cada uma delas.

Tem-se o uso deste processo, em empresas que comercializam produtos químicos que serão utilizados por outras empresas na fabricação de outros produtos e precisam da comprovação de que algumas características do produto estão dentro dos limites aceitáveis, como as características de um teste físico-químico, onde são avaliadas densidade, odor, cor etc, e/ou microbiológico, onde efetua-se contagem de fungos e leveduras, contagem de coliformes etc.

#### Configurações

O processo de Controle de Qualidade na Saída é iniciado com a geração das amostras que serão utilizadas para analisar as características do produto em um laudo. Assim, para o funcionamento deste processo é necessário realizar as configurações a seguir:

**1 -** Efetue a ativação dos parâmetros **"Utiliza Status do Lote? - UTILSTATUSLOTE"** e **"Controle de Laudo de Amostras? - CONTRLAUDOAMOST"**;

**2 -** No [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-) você deve realizar os procedimentos abaixo:

- Na aba [Medidas e estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abamedidaseestoque), sub-aba [Controle Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#sub-abacontroleadicional), no campo **"Controlar por"** selecione a opção **"Número de lote".** (É necessário ativar o parâmetro **"Utiliza a coluna Controle para controlar o estoque - UTILIZACONTROLE"**);
- Também deverá ser realizada a marcação **"Usa Status de Lote",** aba Medidas e estoque, sub-aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaestoque);
- Na aba [Tipos de Amostra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119013), devem estar definidos quais os Tipos de Amostra serão utilizados para a geração dos respectivos registros de amostra;

**3 -** Com o produto configurado para a geração de amostras, é preciso ajustar o [Tipo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) [de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114), para gerar os registros de amostras que serão utilizados nos testes. Neste caso, assinale a opção **"Gerar amostras para laudo"** localizada na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral).

**Importante:** para o processo de Controle de Qualidade na Saída, o registro de amostra não poderá ser gerado manualmente; o que torna a configuração anterior obrigatória.

**4 -** Como o laudo técnico com as características do produto é um elemento obrigatório para sua comercialização, é necessário também no Tipo de Operação - TOP restringir a confirmação do documento sem que exista o laudo para cada item e que este esteja aprovado. Esta configuração é feita assinalando a opção **"Exige Laudo de análise"** presente na aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque).

**5 -** Por fim, é necessário configurar um padrão de classificação para representar o teste que será realizado no produto. Para isso, na tela [Padrões de Classificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108593) deve-se inserir um padrão para o Produto ou Grupo de Produto de acordo com a necessidade e em seguida incluir as características analisáveis que você deseja analisar, bem como o intervalo de aceitação (mínimo e máximo).

#### Operação

O processo de Controle de Qualidade na Saída é iniciado no documento que de fato dará saída do produto em estoque. Com isso, ao confirmar o documento cujo Tipo de Operação - TOP esteja configurado para gerar amostra, o sistema gera o registro de amostra para os itens que sejam controlados por Status do lote.

Ainda na confirmação do documento, caso a TOP esteja configurada para Exigir Laudo de análise, o sistema irá verificar se já existe laudo aprovado (ou aprovado com ressalva) para todos os itens do documento. Caso não exista laudo para um dos produtos, o evento de liberação [45 - Liberação para Laudo de matéria prima](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#45-liberaoparalaudodematriaprima) será solicitado. O motivo da geração do evento, é que podem existir exceções que permitam o documento ser confirmado sem a existência do laudo, como, por exemplo, um laudo antigo para o mesmo produto/lote.

Uma vez que o registro de amostra foi gerado pelo sistema, os usuários responsáveis pela qualidade podem executar suas tarefas. Dessa forma, é necessário acessar a tela [Registro de Amostras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611334) e coletar, verificar e aprovar a amostra.

Com a amostra aprovada e protocolada (usuário analista e hora da analise informados), será possível lançar um laudo para a amostra onde será apontado o resultado de cada uma das características analisáveis. Desse modo, acesse a tela [Controle de Laudo de Amostras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611114), filtre a amostra em questão para inserção de um novo laudo. Depois de incluir o laudo, as características estarão aguardando que o usuário aponte o resultado para posteriormente **"Concluir o Laudo"**.

Uma vez que o laudo está lançado e aprovado (ou aprovado com ressalva), o sistema permitirá confirmar o documento.

**Importante:** para realizar a impressão do laudo técnico, é necessária criação de um relatório personalizado.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596954-Controle-de-Qualidade-na-Sa%C3%ADda#top)
