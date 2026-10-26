---
id: "44011273683607"
titulo: "Erro \"Identificador do componente não encontrado em Componentes [null]\" ao Importar Tabela no Sistema"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011273683607-Erro-Identificador-do-componente-n%C3%A3o-encontrado-em-Componentes-null-ao-Importar-Tabela-no-Sistema"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:00:41Z"
rotulos: ["sync_hc", "lincros", "lincros_13438797", "sync_hash_d0aa5915113b"]
---

# Erro "Identificador do componente não encontrado em Componentes [null]" ao Importar Tabela no Sistema

## Erro "Identificador do componente não encontrado em Componentes [null]" ao Importar Tabela no Sistema

**1 - Problema Relatado pelo Cliente:**
O cliente informou que ao importar um arquivo Excel para atualizar a tabela de fretes, o log de Excel, retornou o erro "Identificador do componente não encontrado em Componentes [null]"

![Imagem 1: 1 - Problema Relatado pelo Cliente: O cliente informou que ao importar um arquivo Excel para atualizar a tabela de…](https://ajuda.sankhya.com.br/hc/article_attachments/44011289156375)

**2 - Passo a Passo para Resolver o Problema:**

1. **Identificar as Linhas com Erro na Planilha**

   - Abra o arquivo Excel que está sendo importado.
   - Navegue até a aba "Componentes por pessoas" que fica logo no rodapé do arquivo Excel.
   - Olhe para a linha 7, nas colunas A, B e C ficam salvos as pessoas que fazem parte do componente, o erro "Identificador do componente não encontrado em Componentes [null]" indica que foi adicionado um componente de frete mas não foi adicionado uma pessoa para fazer desse componente. Exemplo:
   - ![Imagem 2: Olhe para a linha 7, nas colunas A, B e C ficam salvos as pessoas que fazem parte do componente, o erro "Identificador…](https://ajuda.sankhya.com.br/hc/article_attachments/44011289272343)
   - Ou caso o componente foi adicionado de forma indevida, apenas remova-o da planilha.
2. **Adicionar as pessoas que vão fazer parte do componente**

   - **Com a planilha aberta na aba "Componente por pessoas" conforme comentado acima, na coluna A adicione o identificador do componente que indica qual vai ser o componente que essa pessoa vai ser adicionado, na coluna B adicione o nome desse componente e na coluna C adicione o CPF e ou o CNPJ dessa pessoa. Exemplo:**
   - ![Imagem 3: Com a planilha aberta na aba "Componente por pessoas" conforme comentado acima, na coluna A adicione o identificador do…](https://ajuda.sankhya.com.br/hc/article_attachments/44011320238743)
   - **Após essas alterações, salve a planilha Excel.**
3. **Reimportar a Planilha**

   - Após a inclusão das pessoas e salvar a tabela de frete, volte para a tela de tabelas de fretes através do caminho: Cadastros gerais > Transportadoras > Negociações > Tabelas de frete e clique em "importar" e selecione o arquivo em sua máquina e o importe, com isso, volte para a tela de log de excel pela tela: Operacional > Importação > Excel > Log e acompanhe a importação.
   - Caso o erro persista, verifique se o Excel de fato está salvo com as últimas alterações e caso ainda assim continuar, entre em contato com o time de suporte.
