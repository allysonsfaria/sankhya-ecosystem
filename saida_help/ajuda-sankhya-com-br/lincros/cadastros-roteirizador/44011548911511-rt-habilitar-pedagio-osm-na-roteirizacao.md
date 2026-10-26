---
id: "44011548911511"
titulo: "[RT] - Habilitar pedágio OSM na Roteirização"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011548911511--RT-Habilitar-ped%C3%A1gio-OSM-na-Roteiriza%C3%A7%C3%A3o"
trilha: "Lincros > Roteirizador > Cadastros - Roteirizador"
atualizado_em: "2026-10-05T19:05:31Z"
rotulos: ["sync_hc", "lincros", "lincros_13438213", "sync_hash_229e165f39ef"]
---

# [RT] - Habilitar pedágio OSM na Roteirização

**1 - Problema relatado pelo cliente:**
O cliente solicitou a ativação do parâmetro de integração com o OpenStreetMap (OSM) para que os pedágios mapeados nessa plataforma sejam considerados no cálculo de custos durante a roteirização de todas as suas unidades de depósito. Sem essa configuração, a roteirização ainda ocorre normalmente, mas sem a inclusão automática dos valores de pedágio do OSM na estimativa de custos.

## 2 - Passo a passo para resolver o problema:

1. ## Verificar a solicitação do cliente:

   - Confirmar se o cliente deseja a habilitar o parâmetro que utiliza os pedágios cadastrados no OSM para todos os depósitos.
   - Esclarecer as diferenças entre o cadastro manual e a integração automática com OSM.
2. ## Habilitar o parâmetro:

   - ## Acessar o sistema para habilitação do parâmetro (Processo efetuado pelo time de suporte):

     - Entrar no menu: **Roteirizador > Cadastros > Depósitos > Parâmetros de Geolocalização (ADMIN)**.
     - Localizar o parâmetro **"Usar pedágio do OSM"** e ativá-lo.
     - Salvar as alterações para garantir que a funcionalidade seja aplicada.
3. ## Vincular a classificação de veículo aos tipos de veículo:

   - Para a correta utilização dos pedágios é necessário que os tipos de veículo sejam vinculados a **"Classificação do Veículo (Utilizar para base de cálculo em pedágios)"**, para a manutenção desse cadastro o acesso é: Cadastros> Tipos de Veículo.
     As classificações disponíveis são:

     - **Sem classificação** (valor do pedágio: R$0,00)
     - ## Carro
     - ## Caminhão
     - ## Moto
4. ## Validar a Configuração:

   - Iniciar uma nova sessão de roteirização para testar a funcionalidade ativada.
   - Confirmar que os pedágios estão sendo exibidos corretamente na rota e incluídos no custo total.
5. ## Comunicar a Solução ao Cliente:

   - Informar ao cliente que a funcionalidade foi ativada e está pronta para uso.
   - Compartilhar o artigo explicativo sobre o uso dos pedágios do OSM.
