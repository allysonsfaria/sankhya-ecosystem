---
id: "4407648211735"
titulo: "Código da bandeira de operadora de cartão de crédito e/ou débito inexistente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4407648211735-C%C3%B3digo-da-bandeira-de-operadora-de-cart%C3%A3o-de-cr%C3%A9dito-e-ou-d%C3%A9bito-inexistente"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T15:22:05Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "XML", "SEFAZ", "NFC-e", "#validadoPenelope", "rejeição 443", "Código da bandeira de operadora", "UFSENVTBAND", "HABFISCALPOSTIT", "Tag tBand obrigatória para cartões", "Configuração de título e POS", "Rejeição 443: Bandeira inexistente"]
---

# Código da bandeira de operadora de cartão de crédito e/ou débito inexistente

**![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/15965844088471) MENSAGEM:**

Rejeição-443: Código da bandeira de operadora de cartão de crédito e/ou débito inexistente

**![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/15965876247575) SOLUÇÃO:**

Para os Estados que exigirem a geração da tag: <tBand> sempre que o tipo de pagamento informado no tipo de título **(Tipo de pgto para NFC-e / NF-e / CF-e)** for: 03 - Cartão de Crédito ou 04 - Cartão de Débito, foi criado o parâmetro "**UFSENVTBAND** **- UFs a gerar tag tBand em XML (UF,UF)"** que deverá receber a UF de tal exigência.

**Exemplo:**

![Imagem 3: Exemplo:](https://ajuda.sankhya.com.br/hc/article_attachments/12744280132503)

Havendo mais de uma UF, informe separando-as por vírgula. **Exemplo:** GO,MG

![Imagem 4: Havendo mais de uma UF, informe separando-as por vírgula. Exemplo: GO,MG](https://ajuda.sankhya.com.br/hc/article_attachments/12744280674967)

**Exemplo com erro:**

![Imagem 5: Exemplo com erro:](https://ajuda.sankhya.com.br/hc/article_attachments/4407648705303)

**Exemplo do XML após o preenchimento do parâmetro:**

![Imagem 6: Exemplo do XML após o preenchimento do parâmetro:](https://ajuda.sankhya.com.br/hc/article_attachments/4407648696983)

Parâmetro criado e disponibilizado a partir dos releases: 4.7b752, 4.8b436 e 4.9b32.

**![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/15965876249239) CAUSA:**

Erro apresentado pela ausência da tag: <tBand> em operações com tipo de pagamento: Cartão de Crédito ou Cartão de Débito.

**Importante:** ao atualizar para a correção da rejeição citada acima, se atentar a configuração do tipo de título, o campo **"Forma Pagamento TEF"** para as vendas em cartões de crédito/débito,

![Imagem 8: Importante: ao atualizar para a correção da rejeição citada acima, se atentar a configuração do tipo de título, o campo…](https://ajuda.sankhya.com.br/hc/article_attachments/15695539341975)

**![Atenção](https://ajuda.sankhya.com.br/hc/article_attachments/15965844094103) OBSERVAÇÃO:**

A configuração do campo descrito acima é influenciada pelo parâmetro: **"HABFISCALPOSTIT" - Permite informar Fiscal quando o título for POS",** habilitando o mesmo, irá gerar a Tag  tBand preenchida, mesmo que a opção "**Utiliza POS"** do tipo de título esteja marcada.

![Imagem 10: A configuração do campo descrito acima é influenciada pelo parâmetro: "HABFISCALPOSTIT" - Permite informar Fiscal…](https://ajuda.sankhya.com.br/hc/article_attachments/12744449138455)
