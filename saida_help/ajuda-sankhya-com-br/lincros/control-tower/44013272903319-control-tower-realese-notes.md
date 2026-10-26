---
id: "44013272903319"
titulo: "[Control Tower]  - Realese Notes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013272903319--Control-Tower-Realese-Notes"
trilha: "Lincros > Control Tower"
atualizado_em: "2026-10-05T19:53:00Z"
rotulos: ["sync_hc", "lincros", "lincros_13432757", "sync_hash_5e0cf3d947b8"]
---

# [Control Tower]  - Realese Notes

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/44013306516247)

## Melhorias

- As alterações de placa são registradas no **Histórico de Placa**;
- Adicionado a informação de "**Data de saída do raio**" na tela de LOAD e no relatório Tempo de pátio;
- Melhorias na captura de posições da Autotrac;
- Mapa sinótico informa quando um veículo está sem sinal;
- Foi criado o conceito de **Sub-parada**. para maiores detalhes [clique aqui](https://lincros.movidesk.com/kb/pt-br/article/102113/sub-paradas?preview=true&revisionId=279291);
- Verificar se antena já está cadastrada na base ao salvar uma placa

  - Na obtenção de uma posição dos veículos, antes de cadastra-lo, agora aplicação verifica se já existe pelo número da antena. Antes em determinadas situações duplicava o veiculo.
- Exportação direta dos relatórios online;
- Novos relatórios:

  - "**Processos**"

    - Na aba relatórios, disponibilizado novo relatório: “Processos”. Esse relatório contempla as informações do antigo relatório de “Tempo de Pátio” e possui ainda mais informações. Também é exportado com informações do banco de dados, o que garante que as informações estarão exatamente como são visualizadas na tela de monitoramento. Ainda dentro dessa demanda, também incluímos uma validação que impede a exportação dos relatórios de “Viagens” e “Processos” sem utilização de nenhum filtro.
  - Viagens;

## Correções Importantes:

- Ajustamos a forma em que o sistema determinava a **Data de Saída do Raio**;

  - Quando a aplicação recebe um faturamento estando a rota ainda não iniciada, a **data de conclusão do carregamento** é a **data de emissão do faturamento**, não mais a data de importação do mesmo.
- Ajustado o Cadastro de Paradas
- Ajustes no envio de informações de Cutoff;

Correções

- Corrigimos vários pequenos bugs;

![Imagem 2: Corrigimos vários pequenos bugs;](https://ajuda.sankhya.com.br/hc/article_attachments/44013276204183)
