---
id: "44012581485463"
titulo: "[Routing] - Qualidade de endereço na importação de pedidos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012581485463--Routing-Qualidade-de-endere%C3%A7o-na-importa%C3%A7%C3%A3o-de-pedidos"
trilha: "Lincros > Roteirizador > Pedidos - Roteirizador"
atualizado_em: "2026-10-05T19:33:08Z"
rotulos: ["sync_hc", "lincros", "lincros_13433441", "sync_hash_cb9742024eda"]
---

# [Routing] - Qualidade de endereço na importação de pedidos

**Menu:**Importação > Pedidos

**Objetivo:**Facilitar a importação de endereços dos pedidos, garantindo uma geolocalização precisa e de qualidade para tornar a roteirização mais assertiva.

## Consideração:

- Acesso à importação de pedidos

## Processo de Importação de Pedidos

A importação de pedidos é essencial para a roteirização, pois as informações devem ser inseridas corretamente, seja manualmente (seguindo um layout padrão) ou automaticamente via API (JSON). Após a importação, os pedidos são utilizados na criação das rotas.

Para que a roteirização ocorra corretamente, cada pedido deve ter um endereço de entrega definido. Esse endereço pode ser o cadastrado no cliente ou um endereço secundário informado especificamente na importação do pedido. Caso um endereço seja enviado junto ao pedido, ele terá prioridade sobre o endereço do cadastro do cliente, garantindo maior flexibilidade na roteirização.

A seguir, apresentamos as diretrizes para garantir a qualidade dos endereços cadastrados.

## Dados Precisos de Endereço

A geolocalização define a posição correta dos pedidos na roteirização. Endereços incompletos ou mal formatados podem causar falhas na localização e comprometer a eficiência do processo. Para garantir uma geolocalização eficaz, os seguintes campos devem estar preenchidos corretamente:

**Endereço da Entrega:** Nome completo da via (Rua, Avenida, Rodovia, etc.), sem abreviações.

**Número da casa:** O número exato do imóvel.

**Bairro:**Nome completo, evitando variações ou abreviações.

**Município (Cidade):**Nome oficial da cidade.

**CEP:**O código postal completo e correto**.**

**UF:**A sigla do estado**.**

**Latitude e longitude:**Coordenadas precisas são fundamentais, especialmente para áreas de difícil acesso ou entregas em regiões densamente povoadas.

## Exemplo de endereço completo e preciso:

Rua das Acácias, 123

Bairro São Rafael

São Paulo - SP

CEP: 09321-030

Latitude: -23.640549

Longitude: -46.43953

![Interface gráfica do usuário, Aplicativo, MapaDescrição gerada automaticamente](https://ajuda.sankhya.com.br/hc/article_attachments/44012594955287)

## Indicador de Confiabilidade da Geolocalização

A confiabilidade da geolocalização pode ser verificada pela cor do ícone de Casinha/Alfinete exibido na tela de pedidos:

![Imagem 2: A confiabilidade da geolocalização pode ser verificada pela cor do ícone de Casinha/Alfinete exibido na tela de pedidos:](https://ajuda.sankhya.com.br/hc/article_attachments/44012590294679)

- Confiabilidade Alta;

  ![Imagem 3: Confiabilidade Alta;](https://ajuda.sankhya.com.br/hc/article_attachments/44012590395287)
- Confiabilidade Média;

  ![Imagem 4: Confiabilidade Média;](https://ajuda.sankhya.com.br/hc/article_attachments/44012567520023)
- Confiabilidade Baixa;

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
