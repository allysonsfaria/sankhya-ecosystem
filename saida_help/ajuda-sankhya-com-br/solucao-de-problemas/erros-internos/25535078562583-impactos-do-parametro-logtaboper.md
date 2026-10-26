---
id: "25535078562583"
titulo: "Impactos do parâmetro LOGTABOPER"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25535078562583-Impactos-do-par%C3%A2metro-LOGTABOPER"
trilha: "Solução de Problemas > Erros Internos"
atualizado_em: "2026-07-22T14:45:27Z"
rotulos: ["Configuração", "Integração", "Preferências", "API", "LOGTABOPER", "SankhyaOm"]
---

# Impactos do parâmetro LOGTABOPER

Este parâmetro é utilizado para a integração com o SankhyaOM através da API. Ele possibilita a sincronização de aplicações terceiras com o SankhyaOM, entre elas, existe o serviço Consulta de Histórico de Entidades ([LOG de Tabelas](https://developer.sankhya.com.br/reference/get_logalteracoestabelas)) na API, que permite consultar inserções, edições ou exclusões em entidades específicas do sistema. Veja a lista de entidades [link](https://developer.sankhya.com.br/reference/entidades-para-log-de-altera%C3%A7%C3%A3o).

Para consumir este endpoint na a API Sankhya, ligue o parâmetro LOGTABOPER, na tela **"Preferências"** (Caminho: Configurações » Avançado » Preferências) do SankhyaOm:

### Atenção:

**A partir da versão 4.35, haverá uma migração do LOGTABOPER para o Micromódulo Instance Logs Monitor**, para saber mais utilize o artigo ["Log de Alterações para API: como ativar, desativar e acompanhar os registros de alteração"](https://ajuda.sankhya.com.br/hc/pt-br/articles/34538747408407).

![Imagem 1: A partir da versão 4.35, haverá uma migração do LOGTABOPER para o Micromódulo Instance Logs Monitor , para saber mais…](https://ajuda.sankhya.com.br/hc/article_attachments/25535056337047)

**Importante:** Ao ativar este parâmetro, serão criados gatilhos (triggers) no Banco de Dados. Durante o processo de ativação pode haver um bloqueio temporário das tabelas, o que pode impactar a performance do SankhyaOM. Para minimizar qualquer impacto negativo no desempenho do sistema, recomenda-se que a ativação do parâmetro seja realizada fora do horário de operação.
