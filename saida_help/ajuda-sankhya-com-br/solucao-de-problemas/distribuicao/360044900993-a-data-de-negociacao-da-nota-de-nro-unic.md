---
id: "360044900993"
titulo: "A data de negociação da nota de Nro Unico 'X' é anterior a data início da Ordem de Carga 'Y'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044900993-A-data-de-negocia%C3%A7%C3%A3o-da-nota-de-Nro-Unico-X-%C3%A9-anterior-a-data-in%C3%ADcio-da-Ordem-de-Carga-Y"
trilha: "Solução de Problemas > Distribuição"
atualizado_em: "2026-07-22T15:51:45Z"
rotulos: ["#PUBLIFER", "Configuração", "NF-e", "Preferências", "Financeiro", "Verificar Parâmetro", "Datas Inconsistentes", "Corrigir Preferências", "Erro"]
---

# A data de negociação da nota de Nro Unico 'X' é anterior a data início da Ordem de Carga 'Y'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16539171351703) MENSAGEM:**

A data de negociação da nota de Nro Unico 'X' é anterior a data início da Ordem de Carga 'Y'.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16539200778391) SOLUÇÃO:**

![Imagem 3: Certifique-se que as datas informadas na operação estão corretas. Em caso positivo, para permitir notas com data de…](https://ajuda.sankhya.com.br/hc/article_attachments/16539171364375) Certifique-se que as datas informadas na operação estão corretas. Em caso positivo, para permitir notas com data de negociação anterior a data de início da Ordem de Carga, **ligue** o parâmetro **DTNEGDTINICOC**:

- Tela **"Preferências"** (Caminho de acesso: Configurações » Avançado » Preferências):

![Imagem 4: Tela "Preferências" (Caminho de acesso: Configurações » Avançado » Preferências) :](https://ajuda.sankhya.com.br/hc/article_attachments/15439214451735)

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16539200786839) CAUSA:**

Mensagem apresentada quando existem notas com data de negociação anterior a data de início da Ordem de Carga e o parâmetro DTNEGDTINICOC está desligado.
