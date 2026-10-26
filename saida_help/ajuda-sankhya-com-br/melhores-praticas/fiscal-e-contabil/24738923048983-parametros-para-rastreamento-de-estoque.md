---
id: "24738923048983"
titulo: "Parâmetros para Rastreamento de Estoque/ST"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/24738923048983-Par%C3%A2metros-para-Rastreamento-de-Estoque-ST"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:46:32Z"
rotulos: ["Configuração", "Fiscal", "TOP", "Estoque", "ST", "Documentos Eletrônicos"]
---

# Parâmetros para Rastreamento de Estoque/ST

### Parâmetro para rastreamento de estoque/ST

Para configuração do Rastreamento de ST temos alguns parâmetros a serem observados referente à opção **"Rastrear Doc. Fiscais e Não Fiscais"**, são os seguintes:

(1)** DOCNFISCRASTST** - Documentos Não-Fiscais atualizam Rastreamento/ST:

Uma vez **ligado**, o sistema irá carregar para o rastreamento aquelas movimentações que não tem nenhuma finalidade fiscal.

Caso este esteja **desligado**, o sistema não irá considerar documentos não fiscais para o rastreamento de estoque mesmo com que o campo Rastreamento de Estoque esteja igual a Rastrear Doc. Fiscais e Não Fiscais;

(1)** TOPENTNFISRAST** - Lista de TOP Entrada no rastreamento de Doc. Não Fiscais:

Informe neste parâmetro as TOPs que atualizam o estoque de entrada e não atualizam o livro fiscal ou as TOPs que não atualizam estoque e atualizam o livro fiscal.

**(2)**Essa segunda opção geralmente é utilizada por empresas que importaram as notas de entrada do sistema antigo e tem esses lançamentos no Sankhya/W antes da entrada em produção;

(1)** TOPSAINFISRAST** -  Lista de TOP Saída no rastreamento de Doc. Não Fiscais:

Nesse parâmetro, devem ser informados as TOPs que atualizam o estoque de entrada e não atualizam o livro fiscal.

**![Imagem 1: Atenção:](https://ajuda.sankhya.com.br/hc/article_attachments/25451808708631) Atenção:**

Quanto aos parâmetros citados acima, se o sistema estiver configurado para rastrear documentos não fiscais e os parâmetros TOPENTNFISRAST e TOPSAINFISRAST estiverem vazios, todas as movimentações não fiscais de entrada e saída serão consideradas.

Agora, se optar pela utilização de apenas um dos dois parâmetros, deve-se colocar a opção **-1** no parâmetro que não for utilizado, caso contrário o sistema irá considerar todos os lançamentos não fiscais do parâmetro não utilizado.

(1)** TOPNFNEISRAST** - TOPs no Rastreamento no Fiscais/no Atual. Est.:

Se listada alguma TOP aqui, o sistema irá restringir o rastreamento a elas. Mas, caso não seja informada nenhuma TOP, o sistema irá rastrear todas as notas que atualizam estoque e que se encaixe nos seguintes movimentos: C - Compras, D - Devolução de Venda, T - Transferência ou Q - Requisição.

(1)** TOPENFNEISRAST** - esse parâmetro não existe de forma nativa no sistema:

Para esse parâmetro, a TOP não precisa atualizar nem estoque e nem livros, apenas se encaixar nos movimentos: C - Compras ou D - Devolução de Venda.

**Vale ressaltar que qualquer que seja o cenário, para que o Rastreamento funcione corretamente, as notas em questão devem possuir os dados referentes ao ST preenchidos em campos próprios.**
