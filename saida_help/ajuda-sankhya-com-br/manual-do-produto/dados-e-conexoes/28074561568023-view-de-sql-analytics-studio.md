---
id: "28074561568023"
titulo: "VIEW de SQL - Analytics Studio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28074561568023-VIEW-de-SQL-Analytics-Studio"
trilha: "Manual do Produto > Inteligência e Análise > Analytics AI > Dados e conexões"
atualizado_em: "2026-09-23T17:05:11Z"
rotulos: ["SQL", "Configuração", "Relatórios", "Componentes", "Analytics AI", "Analytics Studio", "VIEW de SQL", "VIEW de Cadastro", "VIEW de Análise de Dados", "Database"]
---

# VIEW de SQL - Analytics Studio

No [Analytics AI](https://ajuda.sankhya.com.br/hc/pt-br/articles/25640296222231), a **"VIEW de SQL"** é uma das três maneiras de carregar dados para os seus [Componentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio#Componentes). Essa funcionalidade permite que se crie uma consulta diretamente em SQL, utilizando as tabelas do seu database e a query resultante vai preencher os Componentes configurados.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=lGz2Gr3E2mo)

## Configurando a VIEW de SQL

Para configurar uma VIEW de SQL, siga os passos abaixo:

### ![Imagem 1: Área de Query](https://ajuda.sankhya.com.br/hc/article_attachments/42309657428119) Área de Query

É o espaço onde deverá escrever a sua consulta SQL. À medida que a query é montada, pode-se utilizar o dicionário de dados à direita da tela para visualizar todas as tabelas e colunas disponíveis, equivalentes às entidades criadas no database.

### ![Imagem 2: Suporte de filtros e variáveis de Input](https://ajuda.sankhya.com.br/hc/article_attachments/42309657428631) Suporte de filtros e variáveis de Input

A VIEW de SQL permite interação com os filtros e inputs que o usuário adiciona na interface. Essa funcionalidade possibilita uma experiência dinâmica de filtragem e busca, respeitando as interações dos usuários.

#### **(1)** Variáveis de filtro

Todo filtro configurado na tela pode ser acessado dentro da query SQL como uma variável. Esses filtros podem ser utilizados para que sua consulta seja filtrada de acordo com a seleção do usuário. O formato das variáveis de filtro é :ID\_NOMEDOCADASTRO.

Exemplo prático:

Suponha que queira que uma tabela filtre os dados de executivos selecionados pelo usuário, por um seletor. Se o usuário selecionar um executivo, sua query pode ser montada usando a variável de filtro :ID\_EXECUTIVO para filtrar os dados desse executivo em específico.

SELECT ID, DESCR, EMAIL FROM CAD\_1008

WHERE ID = :ID\_EXECUTIVO

Essa query retornaria apenas os dados do executivo que foi selecionado no seletor da interface, permitindo uma interação direta e flexível entre o usuário e os dados.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=HE763p0Fzkk)

#### **(1)** Variáveis de input

Da mesma maneira, pode-se interagir com inputs adicionados à interface. Os valores inseridos pelos usuários podem ser aproveitados nas suas queries e em outras ações relacionadas ao banco de dados. O formato da variável de input é :INPUT\_ID. Acesse a documentação do componente **"Input"** para entender melhor como ele é configurado.

Exemplo prático:

Vamos supor que deseja permitir que o usuário busque por nome de vendedor em uma lista. Ao adicionar um componente de input para o usuário digitar o nome do vendedor, esse valor pode ser usado na query SQL, aplicando a variável do input :INPUT\_72 da seguinte forma:

SELECT \* FROM CAD\_VENDEDOR

WHERE DESCR LIKE '%' :INPUT\_72  '%'

Aqui, o :INPUT\_72 é o ID do componente de input, e a query irá filtrar os resultados pelo nome inserido pelo usuário. No caso, se o usuário digitar "Maria", a query retornará todos os registros cujo nome contém "Maria".

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=hNv0S4g7BTU)

### ![Imagem 3: Mapeamento de colunas](https://ajuda.sankhya.com.br/guide-media/01HY3RKFT1NYRAS4YDHR5QPXNE) Mapeamento de colunas

Após executar sua query, tem-se a opção de marcar colunas específicas para se relacionarem com cadastros. Por exemplo, se sua consulta retorna dados de executivos, poderá marcar a coluna de ID do executivo para que o Analytics AI entenda que essa coluna corresponde a um cadastro de vendedor. Isso facilita futuras interações, como formulários de edição ou modais de detalhes, já que o sistema saberá qual filtro aplicar com base nessa marcação.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=VPFA1E5YwEA)

Com essas etapas, a sua VIEW de SQL estará configurada e pronta para popular os componentes desejados.
