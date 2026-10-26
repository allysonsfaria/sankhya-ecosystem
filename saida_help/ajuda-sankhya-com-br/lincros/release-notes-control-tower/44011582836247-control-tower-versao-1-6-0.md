---
id: "44011582836247"
titulo: "[Control Tower] - Versão 1.6.0"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011582836247--Control-Tower-Vers%C3%A3o-1-6-0"
trilha: "Lincros > Control Tower > Release Notes - Control Tower"
atualizado_em: "2026-10-05T19:06:41Z"
rotulos: ["sync_hc", "lincros", "sync_hash_df4519ad0e08", "lincros_13438105"]
---

# [Control Tower] - Versão 1.6.0

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/44011577078423)

**Melhorias**:

- Foi criado o conceito de componentes de **Sub-Paradas**. Para maiores detalhes [clique aqui.](https://lincros.movidesk.com/kb/pt-br/article/102113/sub-paradas?preview=true&revisionId=279280)
- Novo relatório: "**Processos**"

  - Na aba relatórios, disponibilizado novo relatório: “Processos”. Esse relatório contempla as informações do antigo relatório de “Tempo de Pátio” e possui ainda mais informações. Também é exportado com informações do banco de dados, o que garante que as informações estarão exatamente como são visualizadas na tela de monitoramento. Ainda dentro dessa demanda, também incluímos uma validação que impede a exportação dos relatórios de “Viagens” e “Processos” sem utilização de nenhum filtro.
- Verificar se antena já está cadastrada na base ao salvar uma placa

  - Na obtenção de uma posição dos veículos, antes de cadastra-lo, agora aplicação verifica se já existe pelo número da antena. Antes em determinadas situações duplicava o veiculo.

## Correções Importantes:

- Ajustamos a forma em que o sistema determinava a **Data de Saída do Raio**;

  - Quando a aplicação recebe um faturamento estando a rota ainda não iniciada, a **data de conclusão do carregamento** é a **data de emissão do faturamento**, não mais a data de importação do mesmo.
- Agora o **Painel do Aeroporto** está listando as LOADs;
- Ao importar LOADs de uma planilha, o mapa sinótico de determinadas LOADs não eram listadas corretamente. Essa situação foi corrigida.

Correções:

- Corrigimos vários pequenos bug

![Imagem 2: Corrigimos vários pequenos bug](https://ajuda.sankhya.com.br/hc/article_attachments/44011600976919)
