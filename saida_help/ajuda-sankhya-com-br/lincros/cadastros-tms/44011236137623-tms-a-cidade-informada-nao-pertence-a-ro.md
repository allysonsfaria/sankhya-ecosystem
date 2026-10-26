---
id: "44011236137623"
titulo: "[TMS] - A cidade informada não pertence à rota"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011236137623--TMS-A-cidade-informada-n%C3%A3o-pertence-%C3%A0-rota"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T18:58:54Z"
rotulos: ["sync_hc", "lincros", "lincros_13438940", "sync_hash_6d44b6c7ae05"]
---

# [TMS] - A cidade informada não pertence à rota

**Menu**: Cadastros gerais > Transportadoras > Negociações > Prazos de entrega > Transportadora

**Objetivo**: Entender como corrigir a crítica apresentada ao importar tabela  para atualização de prazos de entrega;

## Considerações:

- Possuir a região cadastrada;
- Possuir a necessidade de importar uma planilha para atualização de prazos de entrega;

Abaixo segue os procedimentos:

Ao importar uma planilha para atualização de prazos, por exemplo, caso o sistema encontre alguma divergência de informações, durante a validação do arquivo será gerado um log que você poderá consultar em Operacional > Importação > Excel > Log.

E é possível que na aba Erros encontre a seguinte mensagem:' A cidade informada não pertence à rota';

![Imagem 1: E é possível que na aba Erros encontre a seguinte mensagem:' A cidade informada não pertence à rota';](https://ajuda.sankhya.com.br/hc/article_attachments/44011261127831)

O que ocorre é que na planilha existe uma cidade informada em uma determinada rota/região, mas no sistema não consta essa informação. Neste caso, deve-se:

1. Verificar na planilha que está importando, qual o código da tabela de prazos de entrega referente a cidade que apresentou a crítica;

![Imagem 2: O que ocorre é que na planilha existe uma cidade informada em uma determinada rota/região, mas no sistema não consta…](https://ajuda.sankhya.com.br/hc/article_attachments/44011229096983)

2. Tendo copiado o código mencionado acima, então deve-se acessar  Cadastros gerais > Transportadoras > Negociações > Prazos de entrega > Transportadora e procurar pelo código que foi copiado;

![Imagem 3: 2. Tendo copiado o código mencionado acima, então deve-se acessar Cadastros gerais > Transportadoras > Negociações >…](https://ajuda.sankhya.com.br/hc/article_attachments/44011213959703)

3. Na aba **Cadastro** da tabela de prazo de entregas, deverá procurar pelo campo **Rota** e clicar no lápis;

![Imagem 4: 3. Na aba Cadastro da tabela de prazo de entregas, deverá procurar pelo campo Rota e clicar no lápis;](https://ajuda.sankhya.com.br/hc/article_attachments/44011261523991)

4. Feito isso, então chegamos a informação referente a qual região deveremos estar vinculando as cidades;

![Imagem 5: 4. Feito isso, então chegamos a informação referente a qual região deveremos estar vinculando as cidades;](https://ajuda.sankhya.com.br/hc/article_attachments/44011214173847)

5. Tendo descoberto qual a região em questão, então deve-se acessar Cadastros gerais > Transportadoras > Negociações > Regiões, buscar pela região encontrada no item acima, e aí incluir a cidade faltante na região, conforme imagem.

![Imagem 6: 5. Tendo descoberto qual a região em questão, então deve-se acessar Cadastros gerais > Transportadoras > Negociações >…](https://ajuda.sankhya.com.br/hc/article_attachments/44011277072151)

6. Feito os passos acima, então  ao importar a tabela o sistema não irá mais apresentará a crítica quando importar a planilha.

 "Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
