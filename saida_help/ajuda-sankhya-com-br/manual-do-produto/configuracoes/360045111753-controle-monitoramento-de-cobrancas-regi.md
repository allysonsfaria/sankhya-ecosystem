---
id: "360045111753"
titulo: "Controle/monitoramento de Cobranças Registradas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111753-Controle-monitoramento-de-Cobran%C3%A7as-Registradas"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:58:18Z"
rotulos: ["Configuração", "Monitoramento", "Movimentação Financeira", "Cobranças", "Registradas", "Controle/monitoramento de Cobranças Registradas manual", "AGTITRECGERCEDI", "Ocorrências", "Controle", "Financeiro", "Cobranças Registradas"]
---

# Controle/monitoramento de Cobranças Registradas

A [FEBRABAN - Federação Brasileira de Bancos](https://portal.febraban.org.br/), determinou o fim das cobranças sem registros, de modo a diminuir as fraudes entre os movimentos, visando garantir assim a segurança dos clientes das instituições financeiras.

Por esse motivo, temos no Sankhya-Om algumas configurações que tem o objetivo de melhorar a usabilidade do sistema quanto às cobranças da modalidade registrada, são elas:

Primeiramente, configure a tela [Ocorrências de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa). Depois, como as ocorrências de remessa são variáveis de acordo com a instrução que se deseja enviar ao banco, é necessário definir uma variável para buscar as ocorrências correspondentes ao tipo de instrução.

Dessa forma, na tela [Configuração Arquivo de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273-Configura%C3%A7%C3%A3o-Arquivo-de-Remessa), no layout de remessa no campo correspondente ao código de ocorrência, utilize a variável **"OCORRENCIA"** no conteúdo do campo, de modo que esta busque o código de ocorrência definido na configuração para cada tipo de instrução gerada.

[GIF animado: Imagem 1: Dessa forma, na tela Configuração Arquivo de Remessa , no layout de remessa no campo correspondente ao código de…](https://ajuda.sankhya.com.br/hc/article_attachments/4407252699287)

Para manter a consistência dos dados relacionados a alterações de uma determinada cobrança da modalidade registrada, na tela [Configuração Arquivo de Retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111033-Configura%C3%A7%C3%A3o-Arquivo-de-Retorno) tem-se no botão **"Outras Opções..."** a opção **"Configurações de Ocorrências..."**, que é responsável por unir as instruções de alterações enviadas ao banco com as instruções recebidas.

![Imagem 2: Para manter a consistência dos dados relacionados a alterações de uma determinada cobrança da modalidade registrada, na…](https://ajuda.sankhya.com.br/hc/article_attachments/4407245336343)

Em cada ocorrência configurada, é possível definir a ocorrência de remessa correspondente.

![Imagem 3: Em cada ocorrência configurada, é possível definir a ocorrência de remessa correspondente.](https://ajuda.sankhya.com.br/hc/article_attachments/4407252796823)

Realize esta configuração na seção **"Processamento de Ocorrências de Remessa"** por meio dos campos:

- **Cód. Ocorrência Remessa:** Nessa opção informe qual o código de ocorrência de remessa correspondente a esse código de ocorrência de retorno. O campo é aberto para digitação, pois o layout de retorno (configuração) não possui ligação com a conta onde as ocorrências de remessa foram definidas.
- **Atualização Ocorrência Remessa:** Nessa opção, escolha como o sistema irá marcar a ocorrência de remessa, **"Processada"** ou **"Rejeitada"** quando encontrar esta ocorrência no arquivo de retorno. A opção em branco é utilizada quando não se faz ligação entre as ocorrências de remessa e retorno.

Vejamos a seguir o comportamento do sistema:

**Financeiro**

Com base nas configurações descritas acima, as [Movimentações Financeiras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira) cuja Conta Bancária a elas relacionadas possuam ocorrência de remessas definidas, serão monitoradas pelo sistema. Este monitoramento passa a acontecer, a partir da transformação do título em uma cobrança, ou seja, quando este for inserido pela primeira vez em uma remessa.

As instruções de alteração de um título monitorado, são armazenadas no **"Registro de Alterações do Financeiro"** (tabela TGFRAF) com situação igual a **"A - A enviar"**.

![Imagem 4: As instruções de alteração de um título monitorado, são armazenadas no "Registro de Alterações do Financeiro" (tabela…](https://ajuda.sankhya.com.br/hc/article_attachments/8756894283927)

Títulos correspondentes às cobranças monitoradas, não podem ser deletados ou excluídos, pois estes ainda se encontram em carteira junto ao banco. Deste modo, em uma renegociação, o sistema utiliza o código de ocorrência de baixa para os títulos de origem e gera uma instrução referente à baixa do título no banco.

---

**Remessa**

Na utilização da rotina [Geração Arquivo de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606914-Gera%C3%A7%C3%A3o-Arquivo-de-Remessa), será possível observar além dos títulos que irão compor a remessa, as instruções de alterações de títulos, sendo que estes poderão ser visualizados por meio da grade principal da tela, com as seguintes colorações:

- As linhas **amarelas** correspondem a instruções de alterações de títulos;
- Já as linhas em **vermelho** correspondem a instruções de baixa de títulos.

É importante citar que, uma vez que as instruções de Alteração ou Baixa de Título são inseridas em um arquivo de remessa, sua situação é alterada para **"E - Enviada"**. Já as instruções de Entrada sempre ficarão com a situação **"A - A enviar"** pois elas podem ser enviadas novamente em outros arquivos de remessa, o que indica que elas já foram enviadas em algum momento e terá **"Nro da Remessa"** preenchido.

**Nota:** o processo de transmissão do arquivo ainda é manual, visto que é necessário entregar o arquivo gerado à instituição financeira (na maioria das vezes um upload no portal do banco).

**Importante:** o sistema ainda não está preparado para utilizar as funcionalidades descritas nesta documentação (Controle/monitoramento de Cobranças Registradas) em conjunto com o comportamento disponibilizado pela ativação do parâmetro **"Agrup. títulos receita na geração remessa EDI - AGTITRECGERCEDI"**.

---

**Processamento**

Por meio da rotina de [Processamento Arquivo de Retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115573-Processamento-do-Arquivo-de-Retorno) será identificado qual instrução de remessa a instrução de retorno processada no momento corresponde; este comportamento visa manter a consistência das instruções de remessa (instruções de alterações e baixa do título). Uma vez identificada, a instrução em questão tem sua situação atualizada como processada ou rejeitada.

Durante o Processamento do Arquivo de Retorno o sistema pode realizar alterações ou baixas em títulos pertencentes a conta monitorada e que já foram remetidos ao banco; como estas mudanças partiram do banco, não existe a necessidade de gerar uma instrução correspondente a essas ações para serem enviadas ao banco. Deste modo, qualquer alteração ou baixa em título que acontecer durante o Processamento do Arquivo de Retorno, nunca gera instruções a serem enviadas ao banco.

**Importante:** para que a rotina consiga efetuar a identificação entre instrução de remessa e retorno, é necessário realizar uma configuração prévia na tela [Configuração Arquivo de Retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111033-Configura%C3%A7%C3%A3o-Arquivo-de-Retorno), conforme descrito anteriormente.

---

**Histórico de Alterações**

Por meio da tela [Registro de Alteração Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606834-Registro-de-Altera%C3%A7%C3%A3o-Financeiro) tem-se a possibilidade de acompanhamento das instruções de um título (entrada, baixa e alteração).

Além de consultar as instruções que foram geradas para um determinado título, é possível executar a exclusão de uma instrução. A ação de exclusão, se torna necessária em possíveis erros de lançamento ou edições sobre um título cuja conta bancária possua monitoramento.

**Importante:** a exclusão de uma instrução deve ser executada com cautela, visto que não é possível gerar uma nova instrução a não ser a partir de uma edição no título. Visando auxiliar no controle destas ações, esta função pode ser habilitada ou desabilitada a partir dos [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos) à tela.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111753-Controle-monitoramento-de-Cobran%C3%A7as-Registradas#top)

![Imagem 5: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16241335182615) Acesse também:

[Ocorrências de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa)

[Registro de Alteração Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606834-Registro-de-Altera%C3%A7%C3%A3o-Financeiro)
