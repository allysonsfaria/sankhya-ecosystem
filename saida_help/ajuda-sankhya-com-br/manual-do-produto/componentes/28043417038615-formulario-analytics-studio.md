---
id: "28043417038615"
titulo: "Formulário - Analytics Studio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28043417038615-Formul%C3%A1rio-Analytics-Studio"
trilha: "Manual do Produto > Inteligência e Análise > Analytics AI > Componentes"
atualizado_em: "2026-09-23T17:16:45Z"
rotulos: ["Configuração", "Interface", "Analytics Studio", "Banco de Dados", "Formulário"]
---

# Formulário - Analytics Studio

No [Analytics Studio](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio), é possível criar formulários a partir das tabelas criadas no banco de dados. Esses formulários podem ser utilizados para adicionar ou editar registros e podem ser vinculados a diversos componentes da interface, como botões, tabelas ou listas, proporcionando interações dinâmicas e automatizadas.

![Imagem 1: No Analytics Studio , é possível criar formulários a partir das tabelas criadas no banco de dados. Esses formulários…](https://ajuda.sankhya.com.br/hc/article_attachments/28043417033751)

### Como criar um formulário

![Imagem 2: Acesse a seção de "Interações" do componente que deseja e crie um novo formulário.](https://ajuda.sankhya.com.br/hc/article_attachments/28043417035671) Acesse a seção de **"Interações"** do componente que deseja e crie um novo formulário.

![Imagem 3: Selecione o cadastro ao qual o formulário será vinculado. Isso definirá a fonte de dados que o formulário utilizará,…](https://ajuda.sankhya.com.br/hc/article_attachments/28043417036183) Selecione o cadastro ao qual o formulário será vinculado. Isso definirá a fonte de dados que o formulário utilizará, permitindo adicionar, editar ou visualizar registros associados a esse cadastro.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=wsR4GTrE2Og)

### IDs e Descrição

Toda tabela criada no Analytics Studio já recebe dois atributos nativos: 

- **ID:** pode ser autoincremental, numérico ou texto. Se o ID for autoincremental, ele será tratado como tal também no formulário, o que significa que o usuário não precisará interagir com ele, já que será gerado automaticamente. Se ele não for autoincremental, ele aparecerá no formulário para o usuário adicionar.
- **Descrição:** é um atributo nativo que aparece por padrão no formulário. Se o usuário desejar, pode renomear o campo **"Descrição"** ou, caso não queira utilizá-lo, pode marcar a descrição como autoincremental, o que a tornará praticamente ignorada no processo de inserção de dados.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=uu9vb9RbqFo)

### Campos FK (Foreign Keys)

Os campos FK oferecem várias opções de configuração que controlam como os dados relacionados serão manipulados.

- **Fixo:** utilizada quando um campo deve ter sempre o mesmo valor. Por exemplo: ao criar uma tarefa, o campo "status" pode ser automaticamente configurado como "pendente", eliminando a necessidade de seleção manual pelo usuário.
- **Seleção:** ideal para preencher campos com valores baseados no contexto da tela. Um exemplo seria ao clicar em uma negociação em uma lista: o formulário de **"Item de negociação"** pode ter o campo **"Negociação"** preenchido automaticamente com a negociação selecionada.
- **Busca:** permite que o usuário escolha valores de um drop-down, como preencher o campo "cidade" de um vendedor a partir de uma lista de cidades.
- **Busca e Adição:** além de selecionar um valor existente, o usuário pode adicionar um novo valor no momento do cadastro. Por exemplo, ao cadastrar um vendedor, se a cidade desejada não estiver na lista, o usuário pode adicionar a nova cidade na hora.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=U-1V2wvkHyM)

### Atributos comuns (Texto, Número, Data)

Para campos comuns como texto, número e data, há opções de configuração que controlam sua exibição e comportamento:

- **Editável:** o campo pode ser preenchido ou alterado pelo usuário.
- **Bloqueado:** o campo estará visível, mas não poderá ser editado.
- **Obrigatório:** o preenchimento do campo será obrigatório.
- **Oculto:** o campo não será exibido no formulário.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=bl2R3vmLzAU)

### Anexos

Para anexar arquivos, como fotos ou documentos, no formulário, use um atributo do tipo texto e marque a opção de **"Anexo"**. Por exemplo, ao cadastrar um vendedor, é possível criar um campo "foto" do tipo texto, marcar a opção “anexo” e, ao preencher o formulário, anexar uma foto do vendedor. A imagem (ex: foto\_do\_josé.jpg) será enviada para o Analytics AI Drive, e o link da imagem será armazenado no registro do vendedor.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=lStdK39_qAI)

### Máscaras

Campos do tipo texto e número podem ter máscaras aplicadas para garantir que o formato dos dados siga padrões predefinidos, como CPF, CNPJ, CEP, telefone ou tempo.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=-bEqufLUYr8)

### Atributos numéricos

Os atributos numéricos têm configurações específicas:

- **Prefixo e sufixo:** é possível adicionar caracteres antes (prefixo) ou depois (sufixo) do valor numérico.
- **Permitir valores iguais:** em situações onde valores únicos são necessários (como CNPJ), essa opção pode ser desmarcada para garantir que o valor não seja duplicado no banco de dados. Por exemplo, se não for permitido que dois registros possuam o mesmo CNPJ, o formulário irá validar isso automaticamente.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=LekBJrU6SV4)

### Reordenar colunas

A ordem dos campos no formulário pode ser ajustada de forma simples arrastando-os diretamente pela interface de configuração. Essa funcionalidade permite personalizar a disposição dos campos conforme a necessidade.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=LULO4XCRmU4)

### Configurações avançadas

- **Formulário Público:** é possível gerar um link público que permita o acesso ao formulário sem a necessidade de login.
- **Mensagem Pós-Submissão:** uma mensagem de confirmação pode ser configurada para ser exibida ao usuário após o envio do formulário.
- **Ação Pós-Adição/Edição:** essa opção permite que ações automáticas sejam realizadas após o envio do formulário. Por exemplo: ao criar um projeto, é possível configurar uma ação que crie automaticamente várias tarefas associadas.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=R5C2buTHnV4)

### Uso do formulário sem ações No-Code ou de Database

Ao utilizar o componente de formulário, não é necessário configurar ações no-code nem ações de banco de dados para a inserção ou edição de registros. O formulário já realiza essas operações automaticamente:

- **Adicionar Registros:** o formulário insere os dados diretamente na tabela associada, sem a necessidade de ações extras de banco de dados ou no-code.
- **Editar Registros:** da mesma forma, ao utilizar um formulário para editar registros, não é necessário configurar uma ação de "UPDATE" no banco de dados. O formulário já edita os registros automaticamente, sem precisar de nenhuma ação adicional.

### Interação com Views SQL

Para utilizar um formulário de edição numa View SQL, é importante mapear o campo de ID corretamente. O Analytics AI precisa identificar a qual cadastro o ID corresponde para que o formulário funcione corretamente. Por exemplo, em uma view de clientes, é necessário mapear a coluna de ID do cliente com o cadastro correspondente.

---

![Imagem 4: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/28131806203159) Acesse também:

[Analytics AI](https://ajuda.sankhya.com.br/hc/pt-br/articles/25640296222231-Analytics-AI)

[Analytics Studio](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio)
