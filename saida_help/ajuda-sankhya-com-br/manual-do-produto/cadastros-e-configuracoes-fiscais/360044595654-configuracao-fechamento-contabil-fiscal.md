---
id: "360044595654"
titulo: "Configuração Fechamento Contábil/Fiscal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595654-Configura%C3%A7%C3%A3o-Fechamento-Cont%C3%A1bil-Fiscal"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Cadastros e Configurações Fiscais"
atualizado_em: "2026-09-15T14:03:02Z"
rotulos: ["AJUDA DO SKW", "manual", "br.com.sankhya.mgeliv.cad.configparabloqctb", "Configuração Fechamento Contábil/Fiscal manual", "br.com.sankhya.mgecontab.configuracoesbloqueiocontabil", "Configuração", "Fiscal", "Movimentação Financeira", "Contabilidade", "Estoque", "Bloqueio retroativo de movimentações contábeis", "Liberação de bloqueios por usuário", "Configuração de fechamento contábil"]
---

# Configuração Fechamento Contábil/Fiscal

| ```  Módulo: Livros Fiscais > Contabilidade ``` |
| --- |

---

Esta rotina realiza o bloqueio das movimentações em datas retroativas, certificando-se que, após uma data específica (configurada pelo usuário), os dados relativos às movimentações que afetam a parte contábil e fiscal não serão modificados, ou seja, o fechamento impossibilitará o lançamento, exclusão e/ou edição de documentos em datas passadas, preservando assim, a integridade das informações.

| [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595654-Configura%C3%A7%C3%A3o-Fechamento-Cont%C3%A1bil-Fiscal#painelprincipal) |  | [Aba Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595654-Configura%C3%A7%C3%A3o-Fechamento-Cont%C3%A1bil-Fiscal#abaconfiguraes) |
| --- | --- | --- |
| [Aba Bloqueios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595654-Configura%C3%A7%C3%A3o-Fechamento-Cont%C3%A1bil-Fiscal#ababloqueios) |  |  |

![Imagem 1: Aba Bloqueios](https://ajuda.sankhya.com.br/hc/article_attachments/4413863536919)

## Painel Principal

![Imagem 2: Painel Principal](https://ajuda.sankhya.com.br/hc/article_attachments/4413863716759)

Neste Painel, localizado na parte superior da tela, o usuário deverá definir o **"Código Empresa"** a ser trabalhada no fechamento e, também, a **"Descrição"** do evento.

**Nota:** serão consideradas no campo Código Empresa apenas as [Empresas da Contabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608114-Empresa).

Sendo assim, definidos os dados da Empresa, todas as demais [Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595654-Configura%C3%A7%C3%A3o-Fechamento-Cont%C3%A1bil-Fiscal#abaconfiguraes) e [Bloqueios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595654-Configura%C3%A7%C3%A3o-Fechamento-Cont%C3%A1bil-Fiscal#ababloqueios) serão realizados considerando as informações apontadas neste Painel Principal.

A marcação **"Ativa"**funciona como uma **chave mestra de habilitação** do conjunto de regras.

Ela serve como um **filtro obrigatório** que valida e direciona o processamento do sistema em duas situações principais:

- **Para o Job de Bloqueio:** O processo automático de bloqueio (IncluirBloqueioFechamentoCtbJob) **só é executado** para os cabeçalhos de regras que estiverem explicitamente marcados como **ATIVA = Sim**.
- **Para a Liberação Manual:** Ao registrar uma liberação de bloqueio, o sistema **valida** se o cabeçalho da regra que está sendo liberada está **ATIVO**.

No botão ![Imagem 3: No botão "Outras Opções..." desta tela, teremos a o botão "Bloquear Movimentos de Períodos Passados" , que ao…](https://ajuda.sankhya.com.br/hc/article_attachments/16284734659095) **"Outras Opções..."** desta tela, teremos a o botão **"Bloquear Movimentos de Períodos Passados"**, que ao selecioná-lo será exibido um pop de mesmo nome:

![Imagem 4: No botão "Outras Opções..." desta tela, teremos a o botão "Bloquear Movimentos de Períodos Passados" , que ao…](https://ajuda.sankhya.com.br/hc/article_attachments/4413848099607)

Neste pop-up você informará o período em que deseja realizar o bloqueio. Após selecionar o botão **"Bloquear"**, o sistema irá bloquear os movimentos do período que foi informado no pop-up exibindo a mensagem que o bloqueio dos movimentos foi efetuada para o acesso de qualquer usuário.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595654-Configura%C3%A7%C3%A3o-Fechamento-Cont%C3%A1bil-Fiscal#top)

## Aba Configurações

![Imagem 5: Aba Configurações](https://ajuda.sankhya.com.br/hc/article_attachments/4413863799191)

Nesta aba, o usuário terá a opção de configurar 4 tipos de bloqueios, sendo que estes foram divididos por processos, para que os mesmos ocorram de maneira independente e, se necessário, em datas distintas, considerando os processos internos e particularidades dos fechamentos de cada empresa.

Têm-se as seguintes movimentações nesta aba:

- Movimentações Estoque/Custo;
- Movimentações Financeiras;
- Movimentações Contábeis;
- Movimentações Fiscais.

**Observação:** cada movimento disponibilizará ao usuário campos com listas de opções, sendo estas:

- Dia específico do mês subsequente;
- Primeiro dia do mês subsequente;
- Último dia do mês;
- Quinzenal;
- 48 Horas.

**Nota:** apenas as opções **"Dia específico"** e **"Dia específico do mês subsequente"** habilitarão os campos para informar o **"Dia do Fechamento"** no lado direito da tela.

![Imagem 6: Uma vez definidas as configurações, o sistema somente realizará os bloqueios para movimentações futuras, ou seja, para…](https://ajuda.sankhya.com.br/hc/article_attachments/16284734660503) Uma vez definidas as configurações, o sistema somente realizará os bloqueios para movimentações futuras, ou seja, para as datas posteriores à rotina.

Por fim, bastará acionar o botão ![Imagem 7: Por fim, bastará acionar o botão "Bloquear movimentos" para concluir o processo de configuração.](https://ajuda.sankhya.com.br/hc/article_attachments/16284810983191) **"Bloquear movimentos"** para concluir o processo de configuração.

**Observação:** após clicar no botão acima, o sistema apresentará a seguinte mensagem:

**"Deseja continuar com bloqueio do fechamento contábil? Caso confirme, será gerado um bloqueio para todos os movimentos que foram configurados, sendo possível alterações a registros de data anterior apenas com liberação".**

Ao confirmar o bloqueio, informa-se ao usuário que os movimentos foram bloqueados com sucesso.

![Imagem 8: Ao preencher as datas para fechamento das movimentações financeira (receita, despesa e bancário), o sistema irá…](https://ajuda.sankhya.com.br/hc/article_attachments/16284734660503) Ao preencher as datas para fechamento das movimentações financeira (receita, despesa e bancário), o sistema irá bloquear o lançamento de documentos na tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874), no período que estiver fechado. Após o fechamento do período contábil/fiscal, o lançamento de documentos apenas será permitido se a data da ação for maior que as datas determinadas na seção Movimentações Financeiras.

A inclusão automática de bloqueio, deve ser realizada de forma que as datas escolhidas de **“Fechamento Mov. Contábil”** e **“Fechamento Mov. Livro Fiscais”** sejam iguais ou superiores às datas escolhidas de fechamento das movimentações anteriores.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595654-Configura%C3%A7%C3%A3o-Fechamento-Cont%C3%A1bil-Fiscal#top)

## Aba Bloqueios

Nesta aba pode-se configurar as regras de bloqueio de acordo com o período de referência. Além disto, na aba em questão serão configuradas as exceções, ou seja, as permissões de liberação para o desbloqueio do sistema.

![Imagem 9: Nesta aba pode-se configurar as regras de bloqueio de acordo com o período de referência. Além disto, na aba em questão…](https://ajuda.sankhya.com.br/hc/article_attachments/4413856797463)

![Imagem 10: Ao realizar a configuração do fechamento contábil, para que sejam bloqueadas as inserções, alterações, deletes e baixas…](https://ajuda.sankhya.com.br/hc/article_attachments/16284734660503) Ao realizar a configuração do fechamento contábil, para que sejam bloqueadas as inserções, alterações, deletes e baixas financeiras no período configurado no fechamento, é necessário que o parâmetro **"Utiliza Fechamento Contábil? - UTILZFECHACTB"** esteja habilitado.

**Observação:** se o usuário bloquear movimentos de períodos passados nessa aba e tentar faturar parcialmente um pedido emitido no período bloqueado no [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) por meio do botão ![Imagem 11: Observação: se o usuário bloquear movimentos de períodos passados nessa aba e tentar faturar parcialmente um pedido…](https://ajuda.sankhya.com.br/hc/article_attachments/23633451905175) [Faturar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604014-Portal-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#faturar), o sistema permitirá o faturamento desde que existam produtos a serem faturados e que a data do faturamento esteja fora do período bloqueado. 

**Sub-aba Geral**

Esta sub-aba será alimentada automaticamente após acionar o botão **"Bloquear movimentos"** localizado na aba [Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595654-Configura%C3%A7%C3%A3o-Fechamento-Cont%C3%A1bil-Fiscal#abaconfiguraes).

Resumidamente, após as configurações serem realizadas e o bloqueio criado, apresenta-se nesta sub-aba, as datas escolhidas pelo usuário para cada tipo de movimento, de forma que, o sistema irá realizar o bloqueio de movimentações dos períodos cadastrados.

Ao realizar a marcação do campo **"Referência Fixa"**, o sistema irá bloquear todos os movimentos já realizados. Além de que, ao marcá-lo, as informações ficarão preservadas, evitando assim que um determinado usuário possa excluí-las ou editá-las.

**Nota:** para solicitar a liberação de notas que foram bloqueadas nesta tela, você poderá acessar a tela [Liberação de Bloqueio Contábil](https://ajuda.sankhya.com.br/hc/pt-br/articles/360048409753?flash_digest=41e1461a7a28596e6054cd5f7087650645e92779).

**Sub-aba Liberações**

![Imagem 12: Sub-aba Liberações](https://ajuda.sankhya.com.br/hc/article_attachments/4413863870999)

Nesta sub-aba, realiza-se a solicitação de liberação dos eventos já bloqueados.

Será necessário inserir o **"Cód. Usuário Liberador"** para que o mesmo realize ou não a liberação do bloqueio na tela [Liberação de Limites](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites).

Neste contexto, liberando ou negando a solicitação, o campo **"Status Liberação"** será modificado.

**Observação:** sempre que uma solicitação for realizada, o liberador poderá receber um e-mail ou SMS, de acordo com a configuração realizada para o evento no [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios), botão [Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#outrasop%C3%A7%C3%B5es), opção **"Limites para liberação"**.

Selecione o **"Tipo de Movimento"** para o qual deseja bloquear as movimentações dentre as opções abaixo: 

- Movimentações Estoque;
- Movimentações Calculo de Custo - Nota;
- Movimentações Calculo de Custo - Produto;
- Movimentações Calculo de Custo - Serviço;
- Movimentações Financeiras;
- Movimentações Bancárias;
- Movimentações Contábeis;
- Movimentações Fiscais - Livro ICMS/IPI;
- Movimentações Fiscais - Livro ISS;
- Movimentações Fiscais - Ajuste Apuração.

Indique o **"Tipo de ação"** que será realizada no Tipo de Movimento selecionado, conforme as seguintes opções:

- Alteração;
- Deleção;
- Inclusão;
- Rotina de Geração.

O campo **"Rotina de Geração"** será habilitado para os Tipos de Movimento abaixo, podendo recalcular custos e gerar os impostos definidos:

- Movimentações Calculo de Custo - Produto;
- Movimentações Calculo de Custo - Serviço;
- Movimentações Fiscais - Livro ICMS/IPI;
- Movimentações Fiscais - Livro ISS.

Nos campos **"Dh. Inicio Liberação"** e **"Dh. Fim Liberação"**, informe o período da autorização para realizar alterações em qualquer outro período fechado.

Exemplo:

| **Período Fechado:** Mês 08 | **Alteração:** Mês 09 |
| --- | --- |

| **Licença:** Para que a liberação seja efetivada, preencha nos campos citados acima a data do mês e o horário que realizará a alteração e não a do mês em que o período está fechado. |
| --- |

**Botão Itens Liberação**

Você pode desbloquear um ou mais movimentos, por meio do botão **"Itens Liberação"**. Para isso, acione o botão e filtre pelo movimento desejado, através dos campos **"Código do Parceiro"**, **"Data de movimento"**, **"Número único"**, **"Número Documento"** e **"Tipo de Movimentação"**. Depois, clique no botão **"Buscar"** para que os registros sejam exibidos.

Feito isso, selecione o movimento desejado e clique em **"Gravar"**. Desse modo, o item indicado será liberado do bloqueio.

[GIF animado: Imagem 13: Feito isso, selecione o movimento desejado e clique em "Gravar" . Desse modo, o item indicado será liberado do bloqueio.](https://ajuda.sankhya.com.br/hc/article_attachments/4413856533527)

**Observação:** caso a referência a ser lançada para a movimentação financeira retroativa na tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira) esteja bloqueada, porém, esta não seja visível, deve-se realizar as etapas abaixo:

**(1)** Nessa tela, na aba [Bloqueios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595654-Configura%C3%A7%C3%A3o-Fechamento-Cont%C3%A1bil-Fiscal#ababloqueios), verifique se há uma linha com a referência a ser desbloqueada;

**(1)** Se não houver, clique na opção **"Bloquear Movimentos de Períodos Passados"** do botão ![Imagem 14: (1) Se não houver, clique na opção "Bloquear Movimentos de Períodos Passados" do botão "Outras Opções" e informe a…](https://ajuda.sankhya.com.br/hc/article_attachments/16284734659095)**"Outras Opções"** e informe a referência requerida e bloqueie-a. Em seguida, atualize a tela;
**(1)** Na aba Itens Liberação da tela [Liberação de Bloqueio Contábil](https://ajuda.sankhya.com.br/hc/pt-br/articles/360048409753-Libera%C3%A7%C3%A3o-de-Bloqueio-Cont%C3%A1bil) informe os dados da liberação e realize a solicitação na tela [Liberação de Limites](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites). Por fim, inclua a movimentação retroativa, uma vez que a referência foi liberada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595654-Configura%C3%A7%C3%A3o-Fechamento-Cont%C3%A1bil-Fiscal#top)
