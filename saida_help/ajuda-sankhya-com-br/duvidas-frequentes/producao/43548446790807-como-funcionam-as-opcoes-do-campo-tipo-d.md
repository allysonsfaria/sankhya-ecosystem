---
id: "43548446790807"
titulo: "Como funcionam as opções do campo \"Tipo do PI\" nas Configurações do PI da tela \"Composição de Produto\"?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43548446790807-Como-funcionam-as-op%C3%A7%C3%B5es-do-campo-Tipo-do-PI-nas-Configura%C3%A7%C3%B5es-do-PI-da-tela-Composi%C3%A7%C3%A3o-de-Produto"
trilha: "Dúvidas Frequentes > Produção"
atualizado_em: "2026-09-25T12:00:35Z"
rotulos: ["Artigo criado KCS", "Produção - KCS"]
---

# Como funcionam as opções do campo "Tipo do PI" nas Configurações do PI da tela "Composição de Produto"?

Entenda como funciona o valor padrão do campo **"Tipo do PI"** ao compor produtos intermediários no processo produtivo.

Ao cadastrar um produto intermediário (PI) na tela **"Composição de Produto"** (Produção » Cadastros » Composição do Produto), o campo **"Tipo do PI"** define como o sistema irá buscar ou produzir o PI necessário para a fabricação do produto acabado (PA). Este campo é fundamental para determinar se o PI será retirado do estoque existente ou se será gerada uma sub-ordem de produção automaticamente.

O valor padrão (default) do campo **"Tipo do PI"** ao incluir um novo PI na composição é **"Estoque"**. Ou seja, ao adicionar um PI, o sistema assume que o produto intermediário será consumido diretamente do estoque, sem a necessidade de gerar uma sub-ordem de produção para ele. Caso a operação da empresa exija que o PI seja produzido sob demanda, é necessário alterar manualmente o campo para **"Sub-ordem"** no momento do cadastro.

![Imagem 1: O valor padrão (default) do campo "Tipo do PI" ao incluir um novo PI na composição é "Estoque" . Ou seja, ao adicionar…](https://ajuda.sankhya.com.br/hc/article_attachments/43684610337047)

### Como funciona o campo "Tipo do PI"

Entenda as opções disponíveis e o comportamento padrão do campo.

O campo **"Tipo do PI"** possui duas opções principais:

- **"Estoque"**: o PI será consumido do estoque disponível. Não será gerada sub-ordem de produção para este item, mesmo em lançamentos manuais ou no cálculo de demanda indireta do MRP.
- **"Sub-ordem"**: o sistema irá gerar automaticamente uma ordem de produção para o PI, conforme a necessidade do PA. Neste caso, é possível configurar ainda o tipo de sub-ordem (sempre iniciar uma nova, iniciar quando não existir em aberto, sempre usar uma em aberto, etc).

![Imagem 2: "Sub-ordem" : o sistema irá gerar automaticamente uma ordem de produção para o PI, conforme a necessidade do PA. Neste…](https://ajuda.sankhya.com.br/hc/article_attachments/43684627100055)

### Boas práticas para configuração do "Tipo do PI"

Recomendações para garantir o correto funcionamento do processo produtivo.

Sempre avalie o fluxo de produção da empresa antes de definir o **"Tipo do PI"**. Utilize o padrão **"Estoque"** para PIs que são produzidos independentes e mantidos em estoque, otimizando o processo e evitando a geração desnecessária de ordens de produção. Para PIs críticos, de produção sob demanda ou que impactam diretamente a qualidade do PA, prefira a opção **"Sub-ordem"** e configure corretamente as dependências e regras de sincronização.

Lembre-se: a escolha correta do **"Tipo do PI"** impacta diretamente no planejamento, controle de estoque e eficiência do processo produtivo.
