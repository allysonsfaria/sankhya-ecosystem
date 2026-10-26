---
id: "360052605413"
titulo: "O log de processamento de retorno está cheio, pois existem registros de processamentos realizados á mais de 90 dias"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360052605413-O-log-de-processamento-de-retorno-est%C3%A1-cheio-pois-existem-registros-de-processamentos-realizados-%C3%A1-mais-de-90-dias"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T15:29:40Z"
rotulos: ["Configuração", "Relatórios", "Ocorrências", "Financeiro", "O.S 1091553", "#ValidadoGuilhermelíder", "LOGTABOPER", "Lentidão possível", "Limpeza recomendada", "Log de retorno cheio"]
---

# O log de processamento de retorno está cheio, pois existem registros de processamentos realizados á mais de 90 dias

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/15935758440983) MENSAGEM:**

O log de processamento de retorno está cheio, pois existem registros de processamentos realizados á mais de 90 dias.
Isso pode causar lentidão no processamento e é altamente recomendável que você realize uma limpeza.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/15935734357655) SOLUÇÃO:**

1. A mensagem acima trata-se de um aviso. Caso opte por **"Remover os arquivos mais antigos"**, o que é altamente recomendável : Os registros que serão eliminados automaticamente por esta rotina, são dados de log gerados ao processar os arquivos de retorno, estes são apresentados num pop-up na tela ao término da execução, mostrando quais registros foram processados ou não.
2. Acontece que, tais registros, a longo prazo, não são necessários para análise, porém ocupam um espaço significativo no banco de dados.
3. Então com esta opção, poderá ser feita a limpeza automática de tais registros, para não afetar o espaço na base de dados, bem como o desempenho desta rotina. Sendo que a eliminação destes dados não constitui em risco de perda de informações necessárias para as consultas dos títulos financeiros.
