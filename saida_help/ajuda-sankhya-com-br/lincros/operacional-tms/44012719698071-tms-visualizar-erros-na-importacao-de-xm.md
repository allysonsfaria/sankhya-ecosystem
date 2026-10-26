---
id: "44012719698071"
titulo: "[TMS] - Visualizar erros na Importação de XML de anulação de CT-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012719698071--TMS-Visualizar-erros-na-Importa%C3%A7%C3%A3o-de-XML-de-anula%C3%A7%C3%A3o-de-CT-e"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T19:36:16Z"
rotulos: ["sync_hc", "lincros", "lincros_13433363", "sync_hash_41f0a62abf90"]
---

# [TMS] - Visualizar erros na Importação de XML de anulação de CT-e

**Menu**: Operacional > Importação > CT-e > Importação

**Objetivo**: Entender por qual motivo ocorre erro durante a importação do arquivo XML

**Considerações**:

- Possuir um xml de CT-e em que o valor da tag <tpCTe> for igual a 2 (anulação);

Durante a importação do arquivo XML o sistema faz uma série de validações e, caso encontre alguma inconsistência, então apresentará um log em tela ao usuário com informações importantes referentes aquela operação.

Por exemplo, pode ser que no ato da importação do arquivo XML o sistema apresente a seguinte crítica: **ERROR: duplicate key value violates unique constraint "uk\_chave"**

![Imagem 1: Durante a importação do arquivo XML o sistema faz uma série de validações e, caso encontre alguma inconsistência, então…](https://ajuda.sankhya.com.br/hc/article_attachments/44012695409431)

O sistema apresenta essa mensagem, pois está tentando importar um XML que contém a tag '<tpCTe>' com o valor = '2', ou seja, de anulação, mas aquele CT-e em questão já se encontra em situação de anulado.

Para validar essa informação basta:
1. Copiar a chave presente na tag <chCte> dentro do XML;

2. Procurar por esta chave em Operacional > Importação > CT-e;

3. Validar se o CT-e daquela chave que foi copiada está com a situação igual Anulado.

![Imagem 2: 3. Validar se o CT-e daquela chave que foi copiada está com a situação igual Anulado.](https://ajuda.sankhya.com.br/hc/article_attachments/44012720043543)

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
