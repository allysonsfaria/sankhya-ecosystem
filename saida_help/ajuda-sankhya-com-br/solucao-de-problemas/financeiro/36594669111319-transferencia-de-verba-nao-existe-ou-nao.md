---
id: "36594669111319"
titulo: "Transferência de Verba não existe ou não pode ser usado aqui"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36594669111319-Transfer%C3%AAncia-de-Verba-n%C3%A3o-existe-ou-n%C3%A3o-pode-ser-usado-aqui"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:22:43Z"
rotulos: ["NUFIN", "Movimentação Financeira", "Centro de Resultado", "Financeiro", "Planejamento Orçamentário", "Transferência", "CORE_E01315", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "TGMTVO", "Transferência Orçamentária", "TGMTRA"]
---

# Transferência de Verba não existe ou não pode ser usado aqui

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/36594669106839) **MENSAGEM:**

[CORE\_E01315] Transferência de Verba não existe ou não pode ser usado aqui.

**SITUAÇÃO:**

A **Transferência Orçamentária** é responsável por registrar todas as transferências realizadas diretamente por ela.

Sempre que uma transferência é feita, seja entre naturezas, Centros de Resultado (CR) ou metas, o sistema grava essas informações na tabela **TGMTVO.**

Essas movimentações podem ser **filtradas**, **consultadas** ou **estornadas** posteriormente.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/36594669107223)SOLUÇÃO:**

#### Transferências provenientes de Solicitações (Aprovação)

##### **(1)** Filtre os registros na tela [''Transferência Orçamentária''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360048880094-Transfer%C3%AAncia-Or%C3%A7ament%C3%A1ria) (Metas e Orçamentos » Transferência Orçamentária):

- ##### Se a transferência não aparecer e o erro for exibido, significa que o lançamento gerou um NUFIN vinculado a uma Solicitação de Liberação de Transferência.
- ##### Esse tipo de movimentação não é registrado como uma Transferência Orçamentária direta, portanto não é gravado na tabela TGMTVO.
- O sistema registra a movimentação na tabela **TGMTRA**, utilizada exclusivamente para solicitações do tipo **atencipação**, **suplementação** ou **transferência**.

Transferências originadas de **solicitações de aprovação** sempre são registradas na **TGMTRA**, não na **TGMTVO**, por isso **não aparecem** como transferência padrão na tela “Transferência Orçamentária”.

#### Como identificar a diferença entre os tipos de transferência

A distinção pode ser feita tanto analisando diretamente as tabelas quanto pela própria interface do sistema.

**(1)** Acesse a tela [**''Planejamento Orçamentário''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio).

**(2)** Abra a opção **''Ver movimentações do Orçamento/Meta”**.

Na tela exibida:

- Movimentações feitas pela **Transferência Orçamentária direta** aparecem na coluna **“Transf. de saldo”**.
- Movimentações feitas por **Solicitações (Aprovação)** aparecem na coluna **“Transferência”**.

Isso permite identificar claramente de onde cada movimentação se originou.

#### Como visualizar a origem da transferêcia pela interface

Para identificar a origem da transferência diretamente pela interface:

**(1)**Acesse a tela [**''Planejamento de Metas/Orçamentos''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609814-Planejamento-de-Metas-Or%C3%A7amentos) (Metas e Orçamentos » Planejamento de Metas/Orçamentos).

**(2)** Na aba **''Planejamento''** selecione a **''Natureza/CR/Projeto** desejado.

**(3)** Em seguida, clique em **''Outras Opções''** (ícone de três pontos) e selecione a opção **“Ver movimentações do Orçamento/Meta”**.

![Imagem 3: (3) Em seguida, clique em ''Outras Opções'' (ícone de três pontos) e selecione a opção “Ver movimentações do…](https://ajuda.sankhya.com.br/hc/article_attachments/36594742198551)![Imagem 4: (3) Em seguida, clique em ''Outras Opções'' (ícone de três pontos) e selecione a opção “Ver movimentações do…](https://ajuda.sankhya.com.br/hc/article_attachments/36594742198935)

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/36594742199447)CAUSA:**

O erro ocorre porque o lançamento filtrado na tela ''Transferência Orçamentária'' não foi gerado por uma transferência direta.

Em vez disso, o sistema criou um **NUFIN** vinculado a uma **solicitação de liberação de transferência**, e esse tipo de movimentação é registrado na tabela **TGMTRA**, não na **TGMTVO**.

Transferências provenientes de **solicitações** (Antecipação, Suplementação ou Transferência) ficam armazenadas na TGMTRA, portanto **não aparecem como transferências de saldo** na tela "Transferência Orçamentária", causando a inconsistência ao tentar localizá-las.
