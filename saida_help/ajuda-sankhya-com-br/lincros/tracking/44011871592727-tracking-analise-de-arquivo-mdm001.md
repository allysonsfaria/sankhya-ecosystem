---
id: "44011871592727"
titulo: "[Tracking] Análise de arquivo MDM001"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011871592727--Tracking-An%C3%A1lise-de-arquivo-MDM001"
trilha: "Lincros > Tracking"
atualizado_em: "2026-10-05T19:13:53Z"
rotulos: ["sync_hc", "lincros", "lincros_13434690", "sync_hash_b35968c9785c"]
---

# [Tracking] Análise de arquivo MDM001

## Menu: Integrações > Upload > Modelo MDM001

**Objetivo:** Como analisar um arquivo MDM001 importado para o sistema.

## Considerações:

- Utilizar este tipo de importação em sua operação.

 Abaixo segue os procedimentos:

1º - Importar o arquivo MDM001.

2º - Verificar se todas as rotas da planilha subiram.

3º - Caso não, analise os logs para identificar os erros na integração em **Integrações> "Integração Conversor para importação de viagens manual."**Na imagem abaixo, o campo **Nº conta do fornecedor**é obrigatório e não estava presente nas linhas citadas no log de erros.

![Imagem 1: 3º - Caso não, analise os logs para identificar os erros na integração em Integrações> "Integração Conversor para…](https://ajuda.sankhya.com.br/hc/article_attachments/44011871835543)

 4º - Após verificar os logs e identificar os erros, abra novamente seu arquivo e corrija as linhas e/ou campos conforme verificado anteriormente. Na imagem a seguir o problema estava no CPF do motorista.

![Imagem 2: 4º - Após verificar os logs e identificar os erros, abra novamente seu arquivo e corrija as linhas e/ou campos conforme…](https://ajuda.sankhya.com.br/hc/article_attachments/44011885431575)

5º - Após analisar o arquivo e corrigir possíveis erros, deve-se importar o MDM001 e verificar os logs para checar se todos os problemas foram corrigidos.

  "Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
