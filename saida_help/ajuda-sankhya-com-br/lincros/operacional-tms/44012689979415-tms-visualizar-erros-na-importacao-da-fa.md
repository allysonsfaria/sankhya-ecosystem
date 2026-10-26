---
id: "44012689979415"
titulo: "[TMS] - Visualizar erros na Importação da Fatura (arquivo EDI)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012689979415--TMS-Visualizar-erros-na-Importa%C3%A7%C3%A3o-da-Fatura-arquivo-EDI"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T19:36:12Z"
rotulos: ["sync_hc", "lincros", "sync_hash_62f46dc91d24", "lincros_13433367"]
---

# [TMS] - Visualizar erros na Importação da Fatura (arquivo EDI)

**Menu**: Operacional > Importação > EDI > Log

**Objetivo**: Como verificar o motivo que a fatura não foi importada no sistema

**Considerações**:

- Possuir o arquivo 'EDI' para ser importado;

Na tela de Log de importação de EDI disponível através do menu: Operacional > Importação > EDI > Importação > Log,  pode ser verificado se o arquivo foi ou não importado (com erro ou com sucesso).

É possível verificar também a origem, se foi importada para dentro do sistema manualmente ou por e-mail por exemplo.

## Exemplo da tela do log de importação EDI

![Imagem 1: Exemplo da tela do log de importação EDI](https://ajuda.sankhya.com.br/hc/article_attachments/44012683520023)

1. Acessar o menu: Operacional > Importação > EDI > Importação > Log;

![Imagem 2: Acessar o menu: Operacional > Importação > EDI > Importação > Log;](https://ajuda.sankhya.com.br/hc/article_attachments/44012694915863)

2. Localizar o arquivo no qual foi importado;

3. Basta clicar sob o 'Código';

4. Em seguida, na aba "Conteúdo" onde mostra os registros detalhado do arquivo;

5. Notasse que há uma X vermelho indicando o registro com problema e ao clicar na seta ao lado esquerdo, vai trazer mais detalhes do problema;

6. Nesse caso, a fatura foi enviada antes do CT-e ser enviado para o sistema. E por conta disto, ele foi importado, porém, este CT-e que deveria estar nesta fatura, não vai agrupar por não se encontrar ainda no sistema.

![Imagem 3: 6. Nesse caso, a fatura foi enviada antes do CT-e ser enviado para o sistema. E por conta disto, ele foi importado,…](https://ajuda.sankhya.com.br/hc/article_attachments/44012675814423)

7. Já na aba seguinte, 'Erros', já pe apresentando os erros que ocorreram de uma forma simplificada;

![Imagem 4: 7. Já na aba seguinte, 'Erros', já pe apresentando os erros que ocorreram de uma forma simplificada;](https://ajuda.sankhya.com.br/hc/article_attachments/44012705885335)

 "Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
