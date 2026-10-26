---
id: "1500001961842"
titulo: "Data de vencimento da parcela não informada ou menor que Data de Emissão [Ocorr:1]-NT(2016/002)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500001961842-Data-de-vencimento-da-parcela-n%C3%A3o-informada-ou-menor-que-Data-de-Emiss%C3%A3o-Ocorr-1-NT-2016-002"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T15:25:51Z"
rotulos: ["NF-e", "SEFAZ", "Financeiro", "#formatadoroger", "900", "Data de vencimento inadequada", "Ajustar datas de vencimento", "Vencimento menor que Emissão", "Regra de validação", "Erro"]
---

# Data de vencimento da parcela não informada ou menor que Data de Emissão [Ocorr:1]-NT(2016/002)

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16287431639959) MENSAGEM**:

[900 - Rejeição]: Data de vencimento da parcela não informada ou menor que Data de Emissão [Ocorr:1].

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16287407062039) SOLUÇÃO:**

Para essa Regra de Validação não há exceções. Sempre que informado o grupo de Parcelas de cobrança, a data de vencimento da parcela deve ser preenchida com uma data maior que a data de emissão do documento.

(1)** Exemplo:**
Foi emitida uma NF-e com uma parcela de duplicata e a data de vencimento (**17**/06/2020) foi informada com a data menor que a data de emissão do documento  (**06**/07/2020). Nessas condições, a NF-e foi rejeitada pelo motivo 900.

![Imagem 3: Acesse: Portal de Vendas>>Central de Notas Acesse a NF-e e identifique a data de emissão da nota, depois verifique na…](https://ajuda.sankhya.com.br/hc/article_attachments/16287431651351) Acesse: Portal de Vendas>>Central de Notas
Acesse a NF-e e identifique a data de emissão da nota, depois verifique na aba: **"Financeiro"** a Data de Vencimento dos títulos. Caso esteja menor que a data de emissão do documento considere ajustar:

**(1)** Se as Parcelas do Tipo de Negociação estiverem configuradas com a opção de digitação (**Digitar somente Data ou Digita Data e valor**), será possível ajustar manualmente os vencimentos dos títulos, acessando a nota.

**(1)** Se as Parcelas do Tipo de Negociação estiverem configuradas com a opção de digitação (**Não Digita**), acesse a opção Refazer Financeiro da Nota em: Outras Opções>>Refazer Financeiro. Esta ação considerará os prazos estipulados pelas parcelas do tipo de negociação e efetuará o cálculo automático  dos vencimentos, considerando a base do prazo.

![Imagem 4: Após os ajustes, gere lote da NF-e novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16287431654679) Após os ajustes, gere lote da NF-e novamente.

**![Imagem 5: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16287431658135) OBSERVAÇÃO:**

altere o parâmetro **"USADTVINCOMPFIN"** para a opção **"Data Baixa".** Deste modo, no momento da compensação do crédito o título compensado (receita) ficará com a data de vencimento igual a data em que está sendo baixado.

![Imagem 6: altere o parâmetro "USADTVINCOMPFIN" para a opção "Data Baixa". Deste modo, no momento da compensação do crédito o…](https://ajuda.sankhya.com.br/hc/article_attachments/15022114935319)

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16287407087127) CAUSA:**

Quando for emitida uma NF-e (modelo 55) e informado o grupo de Parcelas de cobrança e a Data de vencimento da parcela não for informada ou for menor que a data de emissão do documento, haverá a rejeição pelo motivo.

**![Imagem 8: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16287431658135) OBSERVAÇÃO:**

**1-** (**NT2016/002**)

Nota Técnica:

<http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Y6Lj7G0uHwc=>
