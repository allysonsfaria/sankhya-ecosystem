---
id: "42427405773719"
titulo: "Deleções, cancelamentos e inativações na integração Sankhya"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427405773719-Dele%C3%A7%C3%B5es-cancelamentos-e-inativa%C3%A7%C3%B5es-na-integra%C3%A7%C3%A3o-Sankhya"
trilha: "PLOOMES: Automação de propostas  > Geral"
atualizado_em: "2026-08-10T18:02:33Z"
rotulos: ["sync_hc", "ploomes", "ploomes_14328156", "sync_hash_aa6183ffb9a0"]
---

# Deleções, cancelamentos e inativações na integração Sankhya

## 1) Sobre o deleções, cancelamentos e inativações na integração Sankhya

A funcionalidade de **refletir deleções, cancelamentos e inativações** na integração Sankhya permite manter a consistência e integridade dos dados entre o Ploomes e o Sankhya quando registros são deletados, cancelados ou desativados em um dos sistemas.

Na prática, essa funcionalidade atua em três frentes:

- **Deleções do Sankhya refletidas no Ploomes:** quando um documento (Orçamento, Pedido de Venda ou Nota de Venda) tem seu CabecalhoNota deletado ou cancelado no Sankhya, a integração pode refletir essa ação deletando automaticamente o registro correspondente no Ploomes. Esse comportamento depende da ativação de gatilhos na configuração da integração.
- **Despareamento automático por ações no Ploomes:** quando um registro integrado é deletado ou desativado no Ploomes, a integração realiza automaticamente o despareamento do cadastro, liberando o ID correspondente no Sankhya para ser integrado a outros registros. Nenhuma ação é executada no Sankhya.
- **Tratamento automático de registros órfãos:** quando uma edição no Ploomes tenta ser exportada para o Sankhya, mas o registro correspondente não existe mais no ERP, a integração trata esse cenário automaticamente com despareamento ou deleção, conforme o tipo de entidade e a configuração dos gatilhos.

**Deleção vs. Despareamento:** a deleção remove o registro do Ploomes. O despareamento apenas desfaz o vínculo entre os cadastros na integração (remove o vínculo De-Para da integração), sem excluir nenhum dado do Ploomes ou do Sankhya.

---

## 2) Pré-requisitos

- Possuir a **integração Sankhya V3** ativa na conta Ploomes.
- Configurar os **gatilhos de importação de deleção/cancelamento** de Propostas e Vendas.
- Ter o **parâmetro LOGTABOPER habilitado no Sankhya** (necessário para utilizar os gatilhos de deleção na via Sankhya → Ploomes).

---

## 3) Configurando os gatilhos de deleção (Sankhya → Ploomes)

Os gatilhos de deleção permitem que deleções e cancelamentos realizados no Sankhya sejam refletidos automaticamente como deleções no Ploomes. Essa configuração é feita diretamente na tela de configuração da integração Sankhya.

## 3.1) Acessando os gatilhos de deleção

Acesse a tela de configuração da integração Sankhya no Ploomes. Os gatilhos de deleção estarão disponíveis na seção de configurações da via **Sankhya → Ploomes**.

![Imagem 1: Acesse a tela de configuração da integração Sankhya no Ploomes. Os gatilhos de deleção estarão disponíveis na seção de…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2223582198/221ff05da644214c93a660767709/IntegracaoSankhya-GatilhoDelecao-Orcamento.png?expires=1786536000&signature=759f29ae53a4ca364c9d887093ef9f0d58c2fc57baa8574acade251cf5ab0a4b&req=diIlFcx2n4BWUfMW3nq%2BgZu0Dnc9IY%2Bi5aURYl%2FdcwBcnh8ZhrBGpiOQNKnO%0A6r6HIJjZbVWzIIRK0iKV1aI%2Bxnk%3D%0A)

Exemplo do gatilho de importação de deleção de Orçamentos do Sankhya no Ploomes ativo.

Os gatilhos disponíveis são:

- **Refletir deleção para Orçamento**
- **Refletir deleção/cancelamento para Pedido de Venda**
- **Refletir cancelamento para Nota de Venda**

## 3.2) Ativando ou desativando os gatilhos

Cada gatilho pode ser ativado ou desativado de forma independente. Isso significa que você pode, por exemplo, ativar a deleção apenas para Pedidos de Venda sem afetar Orçamentos ou Notas de Venda.

Para ativar um gatilho, basta habilitá-lo na tela de configuração.

![Imagem 2: Para ativar um gatilho, basta habilitá-lo na tela de configuração.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2231651757/c1e71636b78ba41826beeedacdf0/IntegracaoSankhya-GatilhoDelecao-PedidoDeVenda.png?expires=1786536000&signature=07a0fd3f76654f90476a6d313d9677655c8277427cdaef4f8ba5d6912c16ff0a&req=diIkF897nIZaXvMW3nq%2BgTLa3LyZuBSd5rusdtJyZmAgPrkAEOUN0VrCzACE%0Ad4hzLJw3Dg5vmmQQralm8Osx%2BZM%3D%0A)

**Importante:** ao ativar ou reativar a integração Sankhya pela primeira vez (ou ao migrar de uma versão anterior), todos os gatilhos de deleção serão exibidos como **desativados por padrão**. Caso esteja reativando uma integração que já possuía os gatilhos configurados anteriormente, as configurações da última integração ativa serão preservadas.

## 3.3) Requisito do parâmetro LOGTABOPER

Para que os gatilhos de deleção funcionem, o parâmetro **LOGTABOPER** deve estar habilitado no Sankhya. Esse parâmetro permite que a integração consulte o log de alterações de tabelas no Sankhya para identificar eventos de deleção e cancelamento.

- **Se o parâmetro estiver desabilitado ao tentar ativar um gatilho:** o Ploomes exibirá um modal de erro informando que não é possível ativar o gatilho sem que o LOGTABOPER esteja habilitado no Sankhya.

![Imagem 3: Se o parâmetro estiver desabilitado ao tentar ativar um gatilho: o Ploomes exibirá um modal de erro informando que não…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2223592648/1eccf223393e5a0ca9626c9b80e5/IntegracaoSankhya-ToasterErro-LOGTABOPER.png?expires=1786536000&signature=9d454ba968e424a38d0a5de4be2a48af6ce8effea431354a884c1f8e76540504&req=diIlFcx3n4dbUfMW3nq%2BgQUZrkQ39scUBndefPd6%2BHFshg0BYcZZR%2BDBkxAx%0AL8%2FIHgbDbdvv2zQKQTNkasFCzWw%3D%0A)

- **Se o parâmetro for desabilitado após a ativação dos gatilhos:** o pooling da integração retornará erro a cada tentativa de consulta, e nenhuma ação de deleção será realizada no Ploomes até que o parâmetro seja habilitado novamente.

---

## 4) Utilizando o deleções, cancelamentos e inativações na integração Sankhya

## 4.1) Deleções refletidas do Sankhya para o Ploomes

Com os gatilhos de deleção/cancelamento de CabecalhoNota ativados, a integração monitora automaticamente os eventos de deleção e cancelamento no Sankhya por meio de consultas periódicas (pooling).

**Como funciona:**

1. Um documento (Orçamento, Pedido de Venda ou Nota de Venda) é deletado ou cancelado no Sankhya.
2. A integração captura o evento de deleção/cancelamento na próxima consulta ao Sankhya.
3. O registro correspondente no Ploomes é identificado e **deletado automaticamente**.
4. Um registro de histórico é criado na integração com o status **"Cadastro removido no Sankhya"**.

**Observação:** tanto a deleção quanto o cancelamento de um documento no Sankhya são interpretados da mesma forma pela integração e resultam na deleção do registro no Ploomes.

**Tratamento de erros:**

- **Falha de conexão com o Sankhya ou indisponibilidade:** a integração continuará tentando a cada 5 minutos, ampliando a janela de consulta até o momento do último sucesso de conexão.
- **Falha na deleção no Ploomes:** a integração realizará até 5 tentativas automáticas. Se todas falharem, a deleção será descartada e um registro de erro será criado no histórico da integração.

## 4.2) Despareamento automático por ações no Ploomes

Quando um registro integrado ao Sankhya é deletado ou desativado no Ploomes, a integração realiza automaticamente o **despareamento** do cadastro.

Esse comportamento é automático e não depende de configuração — ele é habilitado para todas as regras de negócio ativas da integração.

**Entidades contempladas e suas ações:**

| Entidade Integrada no Ploomes | Ação no Ploomes | Resultado na integração |
| --- | --- | --- |
| Empresa (PJ) | Deleção | Despareamento |
| Pessoa (PF) | Deleção | Despareamento |
| Produto | Deleção | Despareamento |
| Grupo de Produto | Deleção | Despareamento |
| Usuário | Desativação | Despareamento |
| Proposta | Deleção | Despareamento |
| Venda | Deleção | Despareamento |

**Como funciona:**

1. Um registro integrado ao Sankhya é deletado ou desativado no Ploomes.
2. A integração detecta a ação por meio de webhooks.
3. O vínculo (pareamento) entre o registro do Ploomes e o registro do Sankhya é removido da integração.
4. **Nenhuma ação é executada no Sankhya** — o registro correspondente no ERP permanece intacto.
5. Um registro de histórico é criado com as informações do despareamento.
6. Os campos mapeados com as chaves primárias do Sankhya (como CODPARC, CODPROD, CODVEND, NUNOTA, entre outros) **não são alterados**.

**Observação:** o despareamento é uma ação silenciosa. Não há notificações enviadas ao usuário. O registro da ação pode ser consultado na tela de logs da integração Sankhya.

## 4.3) Tratamento automático de registros órfãos na exportação

Quando você edita no Ploomes um registro integrado ao Sankhya e a tentativa de exportação falha porque o registro correspondente **não existe mais no Sankhya**, a integração trata automaticamente esse cenário. Esse comportamento é padrão e não depende de configuração.

**Para Empresas e Pessoas:**

- A integração realiza o **despareamento automático** do cadastro.
- Nenhuma ação é executada no Sankhya.
- Um registro de histórico é criado informando o despareamento por inexistência do par no Sankhya.

**Para Propostas e Vendas:**

O comportamento depende da configuração dos gatilhos de deleção:

- **Se o gatilho de importação de deleção estiver ativo:** a integração criará uma ação de **deleção** do registro no Ploomes. Um registro de histórico será criado com as informações da falha de exportação e da deleção subsequente.
- **Se o gatilho de importação de deleção não estiver ativo:** a integração realizará o **despareamento automático** do cadastro, seguindo o mesmo comportamento descrito para Empresas e Pessoas.

Em ambos os casos, nenhuma ação é executada no Sankhya e os campos mapeados com chaves primárias do Sankhya não são alterados.

---

## 5) Limitações

- **Deleções são irreversíveis:** não é possível reverter deleções realizadas pela integração no Ploomes.
- **Despareamentos são irreversíveis:** não é possível desfazer os despareamentos realizados pela integração.
- **Dependência do parâmetro LOGTABOPER:** os gatilhos de deleção na via Sankhya → Ploomes só funcionam com o parâmetro LOGTABOPER habilitado no Sankhya. Se ele for desabilitado, o pooling retornará erro até que o parâmetro seja reabilitado.
- **Cobertura limitada aos eventos do serviço de log do Sankhya:** somente eventos de deleção/cancelamento capturados pelo serviço de log de alterações de tabelas do Sankhya serão considerados pela integração.
- **Campos mapeados não são alterados:** as ações de despareamento ou deleção não modificam os campos mapeados com as chaves primárias do Sankhya (CODVEND, CODPARC, CODCTT, CODPROD, CODGRU ou NUNOTA).

---

## 6) F.A.Q.

**Posso ativar o gatilho de deleção apenas para um tipo de documento?**

Sim. Cada gatilho (Orçamento, Pedido de Venda e Nota de Venda) pode ser ativado ou desativado de forma independente.

**O que acontece se o parâmetro LOGTABOPER for desabilitado no Sankhya após eu ativar os gatilhos?**

O pooling da integração passará a retornar erro a cada tentativa de consulta. Nenhuma deleção será executada no Ploomes até que o parâmetro seja habilitado novamente no Sankhya.

**O despareamento automático altera ou exclui dados no Sankhya?**

Não. O despareamento apenas remove o vínculo entre os registros na Lookup da integração. Nenhuma ação é executada no Sankhya e nenhum dado é modificado no ERP.

**Como posso consultar as deleções e despareamentos realizados pela integração?** Todas as ações são registradas e podem ser consultadas na tela de logs da integração Sankhya no Ploomes.

**Posso desfazer uma deleção ou despareamento feito pela integração?**

Não. Tanto as deleções quanto os despareamentos realizados pela integração são irreversíveis.

**O despareamento automático precisa ser configurado?**

Não. O despareamento por ações no Ploomes e o tratamento de registros órfãos são comportamentos automáticos da integração Sankhya V3. Eles são habilitados automaticamente para todas as Rules ativas.

**O que acontece quando edito no Ploomes um registro cujo par foi deletado no Sankhya?**

A integração detecta que o registro correspondente não existe mais no Sankhya e age automaticamente. Para Empresas e Pessoas, realiza o despareamento. Para Propostas e Vendas, realiza a deleção no Ploomes (se o gatilho estiver ativo) ou o despareamento (se o gatilho estiver inativo).

**Ao reativar a integração, os gatilhos de deleção estarão ativos?**

Depende. Se a integração anterior já possuía os gatilhos configurados e você optar por reaproveitar a configuração, os gatilhos serão restaurados conforme a última configuração ativa. Caso contrário, todos os gatilhos serão exibidos como desativados por padrão.

**A integração envia notificações quando uma deleção ou despareamento ocorre?** Não. Essas ações são silenciosas. O registro da ação fica disponível apenas na tela de logs da integração.

---

## 7) Glossário

- **Despareamento:** remoção do vínculo entre um registro do Ploomes e seu registro correspondente no Sankhya dentro da integração. Não exclui dados de nenhum dos sistemas.
- **Pareamento:** vínculo que relaciona um registro do Ploomes a um registro do Sankhya na integração, permitindo a sincronização de dados entre eles.
- **Gatilho de deleção:** configuração que, quando ativada, permite que a integração reflita no Ploomes as deleções ou cancelamentos ocorridos no Sankhya.
- **Pooling:** processo periódico de consulta que a integração realiza no Sankhya para verificar se ocorreram novos eventos (como deleções ou cancelamentos).
- **LOGTABOPER:** parâmetro do Sankhya que habilita o registro de log de alterações em tabelas. Deve estar ativo para que a integração consiga capturar eventos de deleção e cancelamento.
- **Regra de negócio da integração:** regra da integração que define o comportamento de sincronização para um tipo específico de entidade (ex: Orçamento, Pedido de Venda, Empresa, etc.).
- **Registro órfão:** registro pareado na integração cujo correspondente foi deletado em um dos sistemas, deixando o vínculo sem par válido.
- **NUNOTA:** chave primária que identifica um documento (nota) no Sankhya.
- **CODPARC / CODCTT / CODPROD / CODGRU / CODVEND:** chaves primárias do Sankhya que identificam, respectivamente, Parceiro, Contato, Produto, Grupo de Produto e Vendedor.
- **Webhook:** mecanismo que envia automaticamente uma notificação quando uma ação específica ocorre em um sistema (neste contexto, usado pelo Ploomes para detectar deleções e desativações).
