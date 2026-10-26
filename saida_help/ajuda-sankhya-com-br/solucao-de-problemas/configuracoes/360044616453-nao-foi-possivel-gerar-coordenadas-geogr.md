---
id: "360044616453"
titulo: "Não foi possível gerar coordenadas geográficas dos marcadores"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616453-N%C3%A3o-foi-poss%C3%ADvel-gerar-coordenadas-geogr%C3%A1ficas-dos-marcadores"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:54:01Z"
rotulos: ["Maps", "Configuração", "Preferências", "Problemas com Carregamento do Google Maps e Geração de Coordenadas", "Erro", "Google Maps", "API KEY"]
---

# Não foi possível gerar coordenadas geográficas dos marcadores

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18585782007319) MENSAGEM:**

Esta página não carregou o Google Maps corretamente" e "Não foi possível gerar coordenadas geográficas dos marcadores.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18585782013463) SITUAÇÃO:**

Ao tentar efetuar a formação de carga, é apresentada a mensagem.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18585813488279) CAUSA:**

Ocorre quando as configurações para usar Mapa não estão devidamente corretas.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18585782027415) SOLUÇÃO:**

![Imagem 5: A API KEY deve ser gerada no GOOGLE em:](https://ajuda.sankhya.com.br/hc/article_attachments/18585813506327) A API KEY deve ser gerada no GOOGLE em:

<https://console.developers.google.com/apis/credentials> e informada no parâmetro **CHAVEGOOGLEMAP** (Configurações » Avançado » Preferências).

![Imagem 6: Além disso, cada uma das 3 APIs devem ser ativadas:](https://ajuda.sankhya.com.br/hc/article_attachments/18585782042263) Além disso, cada uma das 3 APIs devem ser ativadas:

- Directions API (https://console.developers.google.com/apis/library/directions-backend.googleapis.com)
- Geocoding API (https://console.developers.google.com/apis/library/geocoding-backend.googleapis.com)
- Maps JavaScript API (https://console.developers.google.com/apis/library/maps-backend.googleapis.com)

**Observação:**

O serviço do Google maps, pode sofrer alteração por parte do Fornecedor do Serviço(Google), no que se refere a cobrança para utilização do serviço, consulte informações com o Google.
