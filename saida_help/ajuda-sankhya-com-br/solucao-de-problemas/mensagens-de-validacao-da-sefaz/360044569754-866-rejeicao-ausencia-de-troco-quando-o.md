---
id: "360044569754"
titulo: "866 - Rejeição: Ausência de troco quando o valor dos pagamentos informados for maior que o total da nota.(NT2016/002)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044569754-866-Rejei%C3%A7%C3%A3o-Aus%C3%AAncia-de-troco-quando-o-valor-dos-pagamentos-informados-for-maior-que-o-total-da-nota-NT2016-002"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T15:51:39Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "Central de Vendas", "XML", "SEFAZ", "Impostos", "Rejeição 866", "Ausência de Troco", "NF-e/NFC-e"]
---

# 866 - Rejeição: Ausência de troco quando o valor dos pagamentos informados for maior que o total da nota.(NT2016/002)

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16581979403799) SITUAÇÃO:**

Ao realizar emissão de NF-e pela tela Central de Vendas no SankhyaW, acessando a opção (...)>>Ver Acompanhamento, é possível consultar o detalhe da Rejeição a seguir.

**![Imagem 2: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16581993765271) MENSAGEM:**

866-Rejeição: Ausência de troco quando o valor dos pagamentos informados for maior que o total da nota.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16581993766423) SOLUÇÃO:**

Para correção seguir os passos abaixo:

![Imagem 4: Comercial » Preferências » Empresa](https://ajuda.sankhya.com.br/hc/article_attachments/16581979408663) Comercial » Preferências » Empresa

Aba: NF-e/NFC-e

Campo: Desconsiderar valores de taxas financeiras na geração do XML

Mantendo o campo **desmarcado**, o comportamento do sistema não se altera, incluindo o valor de juros embutidos nas tags vDup e vPag, conforme xml abaixo. Com isso, esses valores ficam maiores que o conteúdo da tag vOrig.

![Imagem 5: Mantendo o campo desmarcado , o comportamento do sistema não se altera, incluindo o valor de juros embutidos nas tags…](https://ajuda.sankhya.com.br/hc/article_attachments/16581979410839)

Mantendo o campo **marcado,** as tags vDup e vPag contém apenas o valor da vOrig, sem considerar valores extras do financeiro, no campo valor de juros embutidos.

![Imagem 6: Após os ajustes na marcação, deverá excluir ou inutilizar a nota e faturar/gerar novamente e gerar Lote.](https://ajuda.sankhya.com.br/hc/article_attachments/16581979412247) Após os ajustes na marcação, deverá excluir ou inutilizar a nota e faturar/gerar novamente e gerar Lote.

![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16581993773207)**OBSERVAÇÃO:**

É possível ter a geração da tag <vtroco> apenas com utilização do TEF.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16581979414423) CAUSA:**

Quando for emitida uma NF-e (modelo 55) ou NFC-e (modelo 65) e o total do pagamento for maior que o total da NF, e não for informado o valor do troco.

**![Imagem 9: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16581993773207) OBSERVAÇÃO:**

1- (**NT2016/002**)

Nota Técnica:

<http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=uvfnqOj%20spg=>
