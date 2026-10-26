---
id: "4403969959831"
titulo: "Subprocesso Reutilizável"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4403969959831-Subprocesso-Reutiliz%C3%A1vel"
trilha: "Manual do Produto > Plataforma e Integrações > Flow"
atualizado_em: "2026-07-29T15:09:19Z"
rotulos: ["Configuração", "Fluxo de Trabalho", "Processos", "sankhyaflow", "subprocesso reutilizável", "Elimina recriação tornando o processo mais conciso e automatizado", "Inicia um processo a partir de outro pausando e retomando após conclusão", "Reutiliza processos existentes no SankhyaFlow como \"Compra de materiais", "Reutilização"]
---

# Subprocesso Reutilizável

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42313333136535) Versão disponível: a partir da 4.6
```

---

Esse é um recurso que permite iniciar um processo a partir de outro processo. O processo será pausado pelo subprocesso reutilizável e retomado quando ele for finalizado. Essa funcionalidade também permite a troca de informações entre os processos.

O modelador irá utilizar o subprocesso reutilizável quando estiver modelando um processo que necessite reutilizar um outro processo já disponível no SankhyaFlow, para que esse novo processo possa ser executado em sua completude.

Essa reutilização elimina a necessidade do modelador ter que construir novamente todo o processo, e torna a representação dele mais concisa.

Nesse artigo, você terá acesso aos seguintes tópicos:

---

1. [Caso de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403969959831-Subprocesso-Reutiliz%C3%A1vel#casodeuso)
2. [Configurando um Subprocesso](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403969959831-Subprocesso-Reutiliz%C3%A1vel#configurandoumsubprocesso)
3. [Resultados](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403969959831-Subprocesso-Reutiliz%C3%A1vel#resultados)
4. [Outras Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403969959831-Subprocesso-Reutiliz%C3%A1vel#outrasconfigura%C3%A7%C3%B5es)

---

#### Caso de Uso

A empresa Alpha Ltda é uma corretora de seguros que possui um processo interno chamado [Manutenção Corretiva de Equipamentos](https://drive.google.com/drive/folders/1gMKa6DsUgu_eSirFEvdHB__jJGpB9eGR), em que um colaborador solicita a manutenção, a equipe de manutenção analisa o equipamento, e dessa análise poderá surgir a necessidade de compra de uma peça nova para o reparo do equipamento. Após a compra da peça, o fluxo deve seguir para o técnico responsável realizar o conserto e, na sequência, segue para o solicitante avaliar o atendimento, conforme podemos observar na imagem abaixo:

![Imagem 2: A empresa Alpha Ltda é uma corretora de seguros que possui um processo interno chamado Manutenção Corretiva de…](https://ajuda.sankhya.com.br/hc/article_attachments/4403966350615)

| **Processo de Manutenção Corretiva de Equipamentos** |
| --- |

Como a empresa Alpha Ltda já possuía um processo de **"Compra de materiais"** modelado e em produção, o modelador definiu esse processo como sendo um subprocesso do processo de Manutenção, reutilizando todo o processo de compra de materiais.

Dessa forma, o processo de Manutenção será paralisado quando o fluxo chegar no subprocesso **"Solicitação de compra"** e será retomado quando esse subprocesso for finalizado com a confirmação do pedido de compra.

No processo de Manutenção, quando o técnico decidir solicitar peças para consertar o equipamento, esses dados preenchidos na tarefa **"Analisar equipamento"** serão preenchidos automaticamente em formulário, para representar a **"Solicitação de Materiais"** no subprocesso de Solicitação de compra, que está representado na imagem abaixo.

![Imagem 3: No processo de Manutenção , quando o técnico decidir solicitar peças para consertar o equipamento, esses dados…](https://ajuda.sankhya.com.br/hc/article_attachments/4403966515991)

| **Subprocesso "Solicitação de Compra"** |
| --- |

**Observação:** quando o subprocesso for concluído, o fluxo seguirá para o técnico consertar o equipamento. Nessa tarefa, iremos disponibilizar o número do pedido de compra para que ele possa consultar e localizar o produto junto à área responsável.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403969959831-Subprocesso-Reutiliz%C3%A1vel#top)

#### Configurando um Subprocesso

O primeiro passo para configurar o subprocesso reutilizável é inserir uma tarefa no processo e alterar para o tipo subprocesso reutilizável, conforme demonstramos abaixo:

[GIF animado: Imagem 4: O primeiro passo para configurar o subprocesso reutilizável é inserir uma tarefa no processo e alterar para o tipo…](https://ajuda.sankhya.com.br/hc/article_attachments/4403966595479)

| **Configuração do Subprocesso** |
| --- |

Na aba **"Dados de Entrada"** da configuração de subprocesso, o modelador pode definir scripts para obter dados de formulários do processo e registrá-los em formulários do subprocesso.

Dando continuidade na configuração do nosso caso de uso, iremos acessar a aba Dados de Entrada e definir o script que obtenha os dados preenchidos nos campos **"Peça"**, **"Quantidade"** e **"Observação"** da tarefa **"Analisar equipamento"** e, automaticamente, registre-os no formulário de Solicitação de compras do subprocesso, representando assim, os dados da inicialização. Observe abaixo a imagem com a configuração:

![Imagem 5: Dando continuidade na configuração do nosso caso de uso, iremos acessar a aba Dados de Entrada e definir o script que…](https://ajuda.sankhya.com.br/hc/article_attachments/4403966677271)

| **Script Dados de Entrada** |
| --- |

---

**Script completo da aba "Dados de Entrada"**

| ``` //Obtém linhas do formulário do processo mestre var buscarFormulario = getLinhasFormulario("AD_ADTWFSOLPROD"); for (var i = 0; i <buscarFormulario.length; i ++){ var produto = buscarFormulario[i].getCampo("CODPROD"); var quantidade = buscarFormulario[i].getCampo("QUANTIDADE"); var observacao = buscarFormulario[i].getCampo("OBSERVACAO"); //Registra dados no formulário do subprocesso var RegistraSolicSubProcesso = novaLinhaFormatadoSubProcesso("AD_SOLICITACAOCOMPRA");          RegistraSolicSubProcesso.setCampo("CODPROD", produto);          RegistraSolicSubProcesso.setCampo("QUANTIDADE", quantidade);          RegistraSolicSubProcesso.setCampo("OBSERVACAO", observacao);          RegistraSolicSubProcesso.save();} ``` |
| --- |

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403969959831-Subprocesso-Reutiliz%C3%A1vel#configurandoumsubprocesso) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403969959831-Subprocesso-Reutiliz%C3%A1vel#top)

---

Agora iremos configurar a aba **"Dados de Retorno"**. Esse recurso possibilita ao modelador definir scripts para obter dados de formulários do subprocesso e registrá-los em formulários do processo.

Em nosso exemplo, iremos obter os dados do pedido que estão armazenados no campo embarcado **"DETALHENOTIFICACAO"** do subprocesso **"Solicitação de compras"**.

Para isso, basta configurar o script na aba Dados de Retorno, conforme mostramos na imagem abaixo:

![Imagem 6: Para isso, basta configurar o script na aba Dados de Retorno , conforme mostramos na imagem abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/4403966827159)

| **Script Dados de Retorno** |
| --- |

---

**Script completo da aba "Dados de Retorno"**

| ``` //O método getCampoSubProcesso obtém o valor do campo 'DETALHENOTIFICACAO' que está no  subprocesso e contém o número do pedido, produto e status. var pedidos = getCampoSubProcesso("DETALHENOTIFICACAO"); var idInstanciaProcesso = getIdInstanceProcesso(); //Atualiza o campo 'NNOTA' do processo para que na tarefa 'Realizar manutenção'  o técnico possa visualizar os dados do pedido gerado.  var query = getQuery();     query.setParam("IDINSTANCIAPROCESSO", idInstanciaProcesso);     query.setParam("PEDIDOS", pedidos);    query.update("UPDATE AD_TWFSOLMANUTEQUIPAMENTOS SET NNOTA = {PEDIDOS} WHERE IDINSTPRN = {IDINSTANCIAPROCESSO}"); ``` |
| --- |

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403969959831-Subprocesso-Reutiliz%C3%A1vel#configurandoumsubprocesso) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403969959831-Subprocesso-Reutiliz%C3%A1vel#top)

#### Resultados

Realizadas as configurações, agora iremos exibir na Lista de Tarefas o comportamento do subprocesso no cenário em que o técnico necessite que a empresa compre peças para realizar a manutenção. Na inicialização, o solicitante informa o problema com o equipamento, no caso um computador, conforme imagem abaixo:

![Imagem 7: Realizadas as configurações, agora iremos exibir na Lista de Tarefas o comportamento do subprocesso no cenário em que o…](https://ajuda.sankhya.com.br/hc/article_attachments/4403967661079)

| **Solicitação de manutenção** |
| --- |

Em seguida, na solicitação 758139, o técnico realiza a análise do equipamento e solicita a peça para o conserto da máquina:

![Imagem 8: Em seguida, na solicitação 758139 , o técnico realiza a análise do equipamento e solicita a peça para o conserto da…](https://ajuda.sankhya.com.br/hc/article_attachments/4403967626007)

| **Análise da solicitação de manutenção** |
| --- |

Na sequência, o fluxo entra no subprocesso **"Solicitação de compras"**, com instância 758148 (solicitação), diretamente na tarefa Analisar solicitação de compra, em que será analisado se a Solicitação de compra será aprovada ou não:

![Imagem 9: Na sequência, o fluxo entra no subprocesso "Solicitação de compras" , com instância 758148 (solicitação) , diretamente…](https://ajuda.sankhya.com.br/hc/article_attachments/4403967568919)

| **Solicitação de peça para correção** |
| --- |

**Nota:** observe que na aba **"Solicitação de Compras"**, os campos preenchidos no processo (Peça, Quantidade e Observação) foram levados automaticamente para essa tarefa, através do script contido na aba Dados de Entrada na modelagem do processo de manutenção.

![Imagem 10: Nota: observe que na aba "Solicitação de Compras" , os campos preenchidos no processo ( Peça , Quantidade e Observação…](https://ajuda.sankhya.com.br/hc/article_attachments/4403967540503)

| **Análise da Solicitação de Compra** |
| --- |

Dando continuidade, o fluxo segue para a tarefa de cotação:

![Imagem 11: Dando continuidade, o fluxo segue para a tarefa de cotação:](https://ajuda.sankhya.com.br/hc/article_attachments/4403967491351)

| **Solicitação de peça para correção** |
| --- |

Após a cotação, o fluxo do subprocesso executa a tarefa de serviço de **"Geração de pedidos"** e a tarefa de notificação sobre os pedidos ao responsável pela solicitação. Assim, o processo retorna para a tarefa de Manutenção de equipamentos para o técnico realizar a manutenção do mesmo:

![Imagem 12: Após a cotação, o fluxo do subprocesso executa a tarefa de serviço de "Geração de pedidos" e a tarefa de notificação…](https://ajuda.sankhya.com.br/hc/article_attachments/4403967468823)

| **Tarefa "Realizar manutenção"** |
| --- |

Observe que, no campo **"Nro. Pedido(s) Gerado(s)"** contém os dados que obtivemos do campo **"DETALHENOTIFICACAO"** do subprocesso, através do script configurado na aba Dados de Retorno. O técnico poderá utilizá-los para obter informações no sistema ou com a área responsável sobre a compra realizada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403969959831-Subprocesso-Reutiliz%C3%A1vel#top)

#### Outras Configurações

---

**Métodos disponíveis para trocar dados entre formulários do processo e subprocesso**

Nas configurações de Dados de Entrada e Dados de Retorno, também podemos utilizar os métodos abaixo para trocar informações entre formulários do processo e subprocesso.

**Dados de Entrada:**

- **setCampoSubProcesso:** Permite inserir dados no Formulário Embarcado do subprocesso.
- **novaLinhaFormatadoSubProcesso:** Possibilita a inserção de uma nova linha no Formulário Formatado do subprocesso.
- **novaLinhaNativoSubProcesso:** Permite inserir um novo registro do Formulário Nativo do suprocesso.

**Dados de Retorno:**

- **getCampoSubProcesso:** Obtém dados do formulário embarcado do subprocesso.
- **getLinhasFormatadoSubProcesso:** Obtém dados do formulário formatado do subprocesso e o retorno é um array com as linhas preenchidas.
- **getLinhasNativoSubProcesso:** Obtém dados do formulário nativo do subprocesso e o retorno é um array com as linhas preenchidas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403969959831-Subprocesso-Reutiliz%C3%A1vel#top)
