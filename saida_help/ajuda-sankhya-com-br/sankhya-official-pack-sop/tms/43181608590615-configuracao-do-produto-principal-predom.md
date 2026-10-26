---
id: "43181608590615"
titulo: "Configuração do Produto Principal (Predominante) da Viagem"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43181608590615-Configura%C3%A7%C3%A3o-do-Produto-Principal-Predominante-da-Viagem"
trilha: "Sankhya Official Pack - SOP > TMS"
atualizado_em: "2026-09-08T11:23:33Z"
rotulos: ["Restringir por Pedido", "Configuração do Produto Principal", "Grupo de Produtos do TMS", "campo Produto Principal na Viagem", "Produto Principal da Viagem"]
---

# Configuração do Produto Principal (Predominante) da Viagem

O campo **Produto Principal** da Viagem identifica qual mercadoria representa a carga transportada. Esse dado não é só informativo: ele alimenta diretamente o **MDF-e** — tipo de carga, descrição do produto, EAN e NCM são copiados do Produto Principal para o manifesto. Se o campo ficar em branco, o MDF-e sai sem essas informações. Este guia mostra como configurar o ambiente para que a lista de produtos oferecida na Viagem venha correta — nem vazia, nem cheia de opções que não fazem sentido para o transporte. 

| **Por que configurar isso:** sem a configuração correta, a busca de Produto Principal na tela Viagem pode não devolver nenhum resultado, ou devolver todos os produtos do cadastro geral (peças, insumos, itens que nunca deveriam aparecer ali). A configuração descrita abaixo é o que garante que apenas os produtos de fato transportados apareçam na lista. |
| --- |

### Pré-Requisitos

Antes de configurar o Produto Principal, certifique-se de que: 

**(1)** O módulo de Transporte de Cargas (TMS) está habilitado. 

**(2)** Existe (ou será criado) um Grupo de Produtos exclusivo para as mercadorias transportadas pela operação logística.

**(3)** O usuário tem acesso ao Cadastro de Produtos, para vincular os produtos ao grupo. 

**(4)** O usuário tem acesso à tela Configurações do TMS, aba Geral. 

**(5)** Os Pedidos de Frete usados na operação já existem (necessário apenas se for usar a restrição opcional por Pedido, passo 4).

**(6)** Permissão de acesso à tela Viagem, para validar o resultado. 

### Como a lista de produtos da Viagem é montada

O campo **Produto Principal** da Viagem não lista todo o cadastro de produtos da empresa. A busca aplica um filtro em duas camadas: 

- **Camada 1 — Grupo de Produtos Predominantes (sempre aplicada):** só entram na lista os produtos cujo **Grupo** (Cadastro de Produtos) é igual ao grupo configurado em Configurações do TMS.
- **Camada 2 — Produtos Permitidos do Pedido (condicional):** se a Viagem tiver um Pedido informado **e** esse Pedido tiver produtos cadastrados na aba Produtos Permitidos, a lista se restringe ainda mais, só aos produtos daquele Pedido.

O exemplo a seguir percorre a configuração ponta a ponta: o grupo **LOGISTICA (9800000)** reúne os produtos **663 – CARGA CONTEINER**, **677 – CARGA GERAL** e **213 – MATERIAL DE HIGIENE**; o Pedido **3 – CARREFOUR BARUERI** restringe a esses mesmos três na aba Produtos Permitidos; e a Viagem 4, vinculada a esse Pedido, oferece exatamente esses três produtos — resultando na escolha do produto **213 – MATERIAL DE HIGIENE** como Produto Principal. 

#### Passo 1 — Criar o Grupo de Produtos do TMS

No Cadastro de Grupo de Produtos, crie (ou reaproveite) um grupo dedicado às mercadorias transportadas pela operação logística — por exemplo, **9800000 – LOGISTICA**. Este grupo é o elo entre o Cadastro de Produtos e a Configuração do TMS: só ele decide quais produtos são candidatos a "Produto Principal" numa Viagem. 

| **Evidência pendente:** não há print do Cadastro de Grupo de Produtos isolado nesta documentação. O vínculo do grupo 9800000/LOGISTICA aparece de forma indireta no print do passo 2 (campo "Grupo" do Cadastro de Produtos). Recomenda-se complementar com um print da tela de Grupo de Produtos quando disponível. |
| --- |

#### Passo 2 — Vincular os Produtos ao Grupo

No **Cadastro de Produtos**, aba **Geral**, preencha o campo **Grupo** (obrigatório) com o grupo criado no passo 1. Repita para cada produto que deve poder ser escolhido como Produto Principal de uma Viagem. No exemplo, os produtos 663 (CARGA CONTEINER), 677 (CARGA GERAL) e 213 (MATERIAL DE HIGIENE) foram vinculados ao grupo 9800000/LOGISTICA. 

**(1)** **Abrir o produto** — localize o produto no Cadastro de Produtos (no exemplo, 663 – CARGA CONTEINER). **Cadastros > Produtos** **2**

**(2)** **Ir para a aba Geral** — o campo Grupo está na seção principal da aba, marcado com asterisco (obrigatório). 

**(3)** **Informar o Grupo** — digite ou pesquise o código do grupo (9800000/LOGISTICA) e salve. 

![Imagem 1: (3) Informar o Grupo — digite ou pesquise o código do grupo (9800000/LOGISTICA) e salve.](https://ajuda.sankhya.com.br/hc/article_attachments/43181665907735)

Cadastro de Produtos — produto 663 CARGA CONTEINER, aba Geral. O campo Grupo (obrigatório) vincula o produto ao grupo 9800000/LOGISTICA. 

| **ATENÇÃO:** o campo Grupo é obrigatório para todo produto (não é exclusivo do TMS). Use um grupo dedicado à operação logística para não misturar produtos de transporte com peças, insumos ou outros itens do cadastro geral. |
| --- |

#### Passo 3 — Informar o Grupo nas Configurações do TMS

Na tela **Configurações do TMS**, aba **Geral**, preencha o campo **Grupo de Produtos Predominantes** com o mesmo grupo vinculado aos produtos no passo 2. Este é o passo mais crítico da configuração: é ele que "liga" o filtro da tela Viagem ao grupo correto. 

(1)** Abrir Configurações do TMS** — acesse a tela e selecione a aba Geral. 

**(2)** **Preencher o Grupo de Produtos Predominantes** — informe o código do grupo (no exemplo, 9800000/LOGISTICA). 

**(3)** **Salvar** — a partir daqui, a tela Viagem passa a oferecer apenas produtos deste grupo. 

![Imagem 2: (3) Salvar — a partir daqui, a tela Viagem passa a oferecer apenas produtos deste grupo.](https://ajuda.sankhya.com.br/hc/article_attachments/43181668790935)

Configurações do TMS — aba Geral. O campo Grupo de Produtos Predominantes define qual grupo de produtos alimenta a busca de Produto Principal na Viagem. 

| **Crítico:** se este campo ficar em branco, a busca de Produto Principal na tela Viagem retorna **vazia** — nenhum produto aparece para escolha, mesmo que existam produtos corretamente vinculados a grupos. Esta é a causa mais comum do problema "não acho nenhum produto para escolher" na Viagem. |
| --- |

#### Passo 4 (opcional) — Restringir por Pedido, na aba Produtos Permitidos

No **Pedido** de Frete, aba **Produtos Permitidos**, é possível cadastrar quais produtos são válidos para aquele pedido específico. Esse passo é **opcional**: só existe efeito se a aba tiver pelo menos um produto cadastrado. 

**(1)** **Abrir o Pedido** — no exemplo, Pedido 3 – CARREFOUR BARUERI. **Cadastros > Pedidos > aba Produtos Permitidos**

**(2)** **Adicionar produtos** — no campo Produto, a busca já vem filtrada pelo grupo configurado no passo 3 (só aparecem produtos daquele grupo — no exemplo, os 3 resultados 663, 677 e 213). 

**(3)** **Salvar a lista** — a partir daqui, Viagens vinculadas a este Pedido só oferecerão estes produtos como Produto Principal. 

![Imagem 3: (3) Salvar a lista — a partir daqui, Viagens vinculadas a este Pedido só oferecerão estes produtos como Produto…](https://ajuda.sankhya.com.br/hc/article_attachments/43181665909143)

Pedido 3 – CARREFOUR BARUERI, aba Produtos Permitidos. O popup de busca do campo Produto já vem filtrado pelo grupo LOGISTICA — apenas 663, 677 e 213 aparecem. 

| **Opcional, não obrigatório:** deixar a aba Produtos Permitidos vazia **não** bloqueia nada — nesse caso, a Viagem oferece todos os produtos do grupo configurado no passo 3. A restrição por Pedido só entra em ação quando a aba já tem pelo menos um produto cadastrado. Use este passo apenas quando quiser reduzir as opções para um subconjunto específico daquele pedido. |
| --- |

### Resultado — o campo Produto Principal na Viagem

Com os três passos anteriores concluídos, a Viagem já oferece a lista correta. No exemplo, a Viagem 4 (Rota 8 – SAO PAULO X RECIFE, Nro Pedido/Operação 3 – CARREFOUR BARUERI, Empresa 4 – FILIAL GOIANIA SMARTIN PLUS, Veículo 3 – SNK2O27) tem o campo **Produto Principal** preenchido com **213 – MATERIAL DE HIGIENE** — um dos três produtos do grupo LOGISTICA, e também um dos três produtos permitidos no Pedido 3. 

![Imagem 4: Com os três passos anteriores concluídos, a Viagem já oferece a lista correta. No exemplo, a Viagem 4 (Rota 8 – SAO…](https://ajuda.sankhya.com.br/hc/article_attachments/43181665909271)

Viagem 4 — campo Produto Principal preenchido com 213/MATERIAL DE HIGIENE, resultado da configuração do grupo LOGISTICA e da restrição do Pedido 3. 

| **Por que isso importa no MDF-e:** ao gravar a Viagem, o sistema localiza a Ordem de Carga vinculada (se houver mais de uma, prevalece a de maior peso total) e copia, do produto escolhido como Produto Principal, o tipo de carga, a descrição, o EAN (referência) e o NCM para os manifestos (MDF-e) daquela viagem que ainda estejam pendentes de transmissão. Produto Principal em branco significa MDF-e sem essas informações. |
| --- |

###

### Diagnóstico rápido

| **Sintoma** | **Causa provável** | **O que verificar** |
| --- | --- | --- |
| A lista de Produto Principal vem **vazia** na Viagem. | O campo Grupo de Produtos Predominantes está em branco nas Configurações do TMS. | Abra Configurações do TMS > aba Geral e preencha o Grupo de Produtos Predominantes (passo 3). |
| Aparecem **produtos demais** (itens que não fazem sentido para transporte). | Produtos de outras áreas foram vinculados ao mesmo grupo configurado, ou o Pedido não tem restrição própria. | Revise o Cadastro de Produtos (campo Grupo) e, se necessário, cadastre a lista na aba Produtos Permitidos do Pedido (passo 4). |
| **Some um produto** que eu esperava encontrar. | O produto não está vinculado ao grupo configurado, ou o Pedido da Viagem tem uma lista de Produtos Permitidos que não inclui esse produto. | Confira o campo Grupo do produto (passo 2) e a aba Produtos Permitidos do Pedido usado na Viagem (passo 4). |

| **Atenção — diferença de comportamento entre telas:** quando o Grupo de Produtos Predominantes está em branco, a tela **Viagem** não trata esse caso e a busca de Produto Principal retorna vazia. Já a tela **Ordens de Carregamento** trata o grupo em branco como "sem restrição" e lista todos os produtos do cadastro. Ou seja: com a configuração em branco, uma tela mostra tudo e a outra não mostra nada. Isso não é um comportamento a corrigir por aqui — é uma inconsistência conhecida entre as duas telas, e o motivo prático de conferir sempre o passo 3 antes de reportar "bug" na Viagem. |
| --- |

### Checklist de Verificação

- Grupo de Produtos exclusivo para a operação logística criado (ex.: 9800000 – LOGISTICA).
- Todos os produtos transportados têm o campo Grupo preenchido com esse grupo, no Cadastro de Produtos.
- O campo Grupo de Produtos Predominantes, em Configurações do TMS > Geral, está preenchido com o mesmo grupo — nunca em branco.
- Se a operação exige restringir por Pedido, a aba Produtos Permitidos foi preenchida com os produtos válidos daquele Pedido.
- Uma Viagem de teste vinculada a um Pedido confirma que o campo Produto Principal lista somente os produtos esperados.

### Perguntas Frequentes

- **Preenchi o Grupo no produto, mas ele não aparece na Viagem. Por quê?**

Confirme se o mesmo grupo está preenchido no campo Grupo de Produtos Predominantes, em Configurações do TMS > Geral. A Viagem só busca produtos cujo grupo está registrado nessa configuração — sem ela preenchida, nenhum produto aparece. 

- **É obrigatório preencher a aba Produtos Permitidos do Pedido?**

Não. É uma restrição opcional. Se a aba estiver vazia, a Viagem oferece todos os produtos do grupo configurado. Só use essa aba quando quiser reduzir as opções a um subconjunto específico do Pedido. 

- **Um produto some da lista de Produto Principal só em algumas Viagens. É normal?**

Sim, se a Viagem estiver vinculada a um Pedido que tem restrição na aba Produtos Permitidos. Nesse caso, só os produtos daquela lista aparecem para aquela Viagem, mesmo que o produto pertença ao grupo configurado. 

- **Posso usar o mesmo grupo de produtos para outras finalidades além do TMS?**

O campo Grupo, no Cadastro de Produtos, é de uso geral. Mas o grupo informado em Configurações do TMS deve reunir especificamente os produtos que representam cargas transportadas — evite reaproveitar um grupo genérico que também contenha itens de outras áreas. 

- **Se eu não informar o Produto Principal na Viagem, o que acontece?**

O MDF-e daquela viagem é emitido sem tipo de carga, descrição, EAN e NCM copiados do produto — informações que normalmente vêm automaticamente dessa configuração. 

- **Por que na Viagem a lista vem vazia e em Ordens de Carregamento aparece tudo, com a mesma configuração em branco?**

É uma diferença de comportamento entre as duas telas: Ordens de Carregamento trata grupo em branco como "sem restrição" (lista tudo); a Viagem não tem esse tratamento (lista nada). A solução prática é a mesma nos dois casos — preencher o Grupo de Produtos Predominantes em Configurações do TMS. 

### Telas Relacionadas

**Cadastro de Grupo de Produtos:** define o grupo usado como filtro do Produto Principal. 

**Cadastro de Produtos:** vincula cada produto ao grupo, no campo Grupo da aba Geral. 

**Configurações do TMS:** registra o grupo no campo Grupo de Produtos Predominantes. 

**Pedido de Frete (aba Produtos Permitidos):** restringe opcionalmente os produtos válidos por Pedido. 

**Viagem:** exibe o campo Produto Principal já filtrado pelas regras acima. 

**MDF-e:** recebe tipo de carga, descrição, EAN e NCM copiados do Produto Principal da viagem.
