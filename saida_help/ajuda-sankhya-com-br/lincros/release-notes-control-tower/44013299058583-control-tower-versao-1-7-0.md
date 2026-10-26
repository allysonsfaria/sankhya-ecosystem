---
id: "44013299058583"
titulo: "[Control Tower] - Versão 1.7.0"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013299058583--Control-Tower-Vers%C3%A3o-1-7-0"
trilha: "Lincros > Control Tower > Release Notes - Control Tower"
atualizado_em: "2026-10-05T19:53:06Z"
rotulos: ["sync_hc", "lincros", "lincros_13432753", "sync_hash_ae294e9e579d"]
---

# [Control Tower] - Versão 1.7.0

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/44013323857303)

Novidades:

 A partir da próxima versão (versão 1.8) os relatórios abaixo serão descontinuados do sistema:

- Aderência Detalhado (substituído pelo relatório de viagens);
- Histórico de temperaturas (relatório descontinuado);
- Pico de velocidade (substituído pelo relatório de anomalias);
- Coordenada das paradas (relatório descontinuado);
- PNP Consolidado (substituído pelo relatório de anomalias e viagens);
- Tempo de pátio (substituído pelo relatório de processos);
- Trânsito (relatório descontinuado);
- Coletas (substituído pelo relatório de viagens e processos);
- Posições (substituído pelo relatório de Veículos);
- Vendas diretas (substituído pelo relatório de viagens);
- Entregas (Viagens e Processos);
- Riscos (relatório descontinuado);
- PNP (substituído pelo relatório de anomalias);
- SSMA (substituído pelo relatório de viagens);
- Anomalias (substituído pelo novo relatório de anomalias);

Em substituição a estes, teremos 4 novos relatórios:

- Veículos
- Viagens
- Processos
- Anomalias

## Melhorias

- A partir da versão 1.5 contabilizamos os atrasos por meio da data e hora atuais;

  - Se a data e hora prevista for menor que a atual, o sistema irá informar que a posição do caminhão possa estar atrasada.

![Uma imagem contendo captura de telaDescrição gerada automaticamente](https://ajuda.sankhya.com.br/hc/article_attachments/44013299332375)

- Agora o sistema contabiliza a distância de deslocamento realizado no recebimento de uma posição;

![Imagem 3: Agora o sistema contabiliza a distância de deslocamento realizado no recebimento de uma posição;](https://ajuda.sankhya.com.br/hc/article_attachments/44013299440663)

           A informação deve ser exibida nos ícones conforme abaixo:

- - **Pré-viagem**: “Distância percorrida para carregamento (KM)” irá considerar a somatória da distância percorrida enquanto o veículo estiver em “Pré-viagem”;
  - **Em trânsito:** “Distância percorrida para descarga (KM)” irá considerar a somatória distância percorrida enquanto o veículo estiver em trânsito para descarga, começando a contabilizar após a conclusão da parada de carregamento;
  - **Término**: “-Distância total percorrida (KM)” irá considerar a somatória entre a distância percorrida “Em trânsito” e “Pré-viagem-”;

## Correções Importantes

- Corrigimos o painel de aeroporto, agora quando o caminhão estiver em processo de “**Pré-viagem**” a informação deve aparecer no painel da unidade de **carregamento** e quando estiver “**Em Trânsito**” deve aparecer no painel da unidade de **descarga**.
- Corrigimos vários pequenos bugs.

![Imagem 4: Corrigimos vários pequenos bugs.](https://ajuda.sankhya.com.br/hc/article_attachments/44013307097239)
