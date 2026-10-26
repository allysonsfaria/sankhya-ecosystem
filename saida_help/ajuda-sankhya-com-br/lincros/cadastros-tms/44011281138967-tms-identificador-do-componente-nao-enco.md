---
id: "44011281138967"
titulo: "[TMS] - Identificador do componente não encontrado em Componentes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011281138967--TMS-Identificador-do-componente-n%C3%A3o-encontrado-em-Componentes"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T18:59:48Z"
rotulos: ["sync_hc", "lincros", "lincros_13438896", "sync_hash_7e631e8c0fda"]
---

# [TMS] - Identificador do componente não encontrado em Componentes

**Menu:** Cadastros gerais > Transportadoras > Negociações > Tabelas de frete > Importar

**Objetivo:** Entender como corrigir a mensagem apresentada pelo sistema na importação de uma tabela de frete.

**Considerações:**

- Possuir uma planilha em Excel para importação da tabela de frete;

Durante a importação de uma tabela de frete no sistema, este faz uma série de validações onde caso encontre alguma divergência, apresentará um log que pode-se estar consultando acessando o menu Operacional > Importação > Excel > Log. Uma das mensagens que pode ocorrer durante a importação da tabela é a seguinte: Identificador do componente não encontrado em Componentes.

![Imagem 1: Durante a importação de uma tabela de frete no sistema, este faz uma série de validações onde caso encontre alguma…](https://ajuda.sankhya.com.br/hc/article_attachments/44011251998231)

Para corrigir essa mensagem deve-se verificar no Excel da tabela de frete que está sendo importada. No exemplo da imagem acima veja que o sistema passa o número 3 entre os colchetes (**[ ]**). Acessando a planilha Excel da tabela de frete, deve-se ir na aba "Componentes por pessoa" e aí procurar qual seria o componente correspondente deste "código" que nada mais é que o identificador do componente. No exemplo da imagem acima, o componente que apresentou a mensagem seria **3 - Paletização**.

![Imagem 2: Para corrigir essa mensagem deve-se verificar no Excel da tabela de frete que está sendo importada. No exemplo da…](https://ajuda.sankhya.com.br/hc/article_attachments/44011281457559)

Tendo identificado qual o componente, então no TMS deve-se acessar Cadastros gerais > Configurações da empresa > Componentes de frete, e aí buscar pelo componente em questão. Por fim, deverá habilitar o parâmetro **Restringir por pessoa,** e salvar.

![Imagem 3: Tendo identificado qual o componente, então no TMS deve-se acessar Cadastros gerais > Configurações da empresa >…](https://ajuda.sankhya.com.br/hc/article_attachments/44011250000535)

Feito isso então o sistema não mais apresentará essa mensagem ao importar a tabela de frete.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
