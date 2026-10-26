---
id: "360044110134"
titulo: "Mensagem 'You have exceeded your request quota for this API'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110134-Mensagem-You-have-exceeded-your-request-quota-for-this-API"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:53:50Z"
rotulos: ["Maps", "OPS! OCORREU UM ERRO", "Configuração", "Requisições", "Preferências", "Limite Excedido na API do Google", "Erro", "Google Maps API"]
---

# Mensagem 'You have exceeded your request quota for this API'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16813329261847) MENSAGEM:**

'You have exceeded your request quota for this API'

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16813329264663) SOLUÇÃO:**

Verifique a configuração necessária para utilização da rotina:

![Imagem 3: Deve ser gerada 3 API Keys no link :](https://ajuda.sankhya.com.br/hc/article_attachments/16813329266199)  Deve ser gerada 3 API Keys no link :

<https://console.developers.google.com/apis/credentials>

(1)** Directions API** (https://console.developers.google.com/apis/library/directions-              backend.googleapis.com)

(1)**Geocoding API** (https://console.developers.google.com/apis/library/geocoding-backend.googleapis.com)

(1)**Maps JavaScript API** (https://console.developers.google.com/apis/library/maps-backend.googleapis.com)

![Imagem 4: No SankhyaW acesse:](https://ajuda.sankhya.com.br/hc/article_attachments/16813303597079) No **SankhyaW** acesse:

Configurações » Avançado » Preferências
Parâmetro: **"CHAVEGOOGLEMAP-Chave para mapas do sistema"**
Informe as chaves no parâmetro indicado acima.

Ao utilizar a rotina e se deparar com o erro que geralmente está presente no Log da aplicação 'You have exceeded your request quota for this API', significa que se está fazendo requisições demais e que a conta gratuita do GOOGLE não permite. Então é preciso adquirir o serviço do Google para funcionar.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16813329270295) CAUSA:**

Ocorre quando a requisição está ultrapassando o limite permitido pela conta gratuita, então é necessário que adquirir o serviço do Google.

**![Imagem 6: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16813303600279) OBSERVAÇÃO:**

Esta é uma lista de API's disponíveis para aquisição, porém somente as 3 primeiras são utilizadas pela aplicação Sankhya.

**Distance Matrix API**
**Geolocation API**
**Maps Elevation API**
Maps Embed API
Maps Static API
Places API for Web
Roads API
Street View Static API
