---
id: "360042643294"
titulo: "Total do COFINS difere do somatório dos itens sujeitos ao ICMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042643294-Total-do-COFINS-difere-do-somat%C3%B3rio-dos-itens-sujeitos-ao-ICMS"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:23Z"
rotulos: ["ERRONF", "#RevisadoBernardo", "Configuração", "NF-e", "SEFAZ", "Alíquotas de COFINS", "Impostos", "603", "Divergência no Total de COFINS"]
---

# Total do COFINS difere do somatório dos itens sujeitos ao ICMS

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16443873590551) **MENSAGEM:**

[603 - Rejeição]: Total do COFINS difere do somatório dos itens sujeitos ao ICMS.

![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16443889846807) **SOLUÇÃO:**

Para correção siga os passos abaixo:

![Imagem 3: Acesse o " Cadastro de Produtos " :](https://ajuda.sankhya.com.br/hc/article_attachments/16443889847447) Acesse o "[**Cadastro de Produtos**"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113):

**(2)** Aba: "**Impostos**", campo "**Grupo COFINS"** = Verificar o valor informado neste campo.

![Imagem 4: Vá até o Cadastro de " Alíquotas de COFINS " e identifique através de um filtro por empresa, TOP, Parceiro e…](https://ajuda.sankhya.com.br/hc/article_attachments/16443889849879) Vá até o Cadastro de **"**[**Alíquotas** **de COFINS**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108813)" e identifique através de um filtro por empresa, TOP, Parceiro e Tipo(Saída/Entrada), se existe uma regra devidamente cadastrada para o mesmo GRUPO que está informado no cadastro do(s) produto(s).

![Imagem 5: Após os ajustes, fature novamente a nota ou redigite o item na nota e gere lote novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16443873593111) Após os ajustes, fature novamente a nota ou redigite o item na nota e gere lote novamente.

**![Imagem 6: OBSERVAÇÕES :](https://ajuda.sankhya.com.br/hc/article_attachments/16443873594519)OBSERVAÇÕES:**

**(2)** Procure orientações do contador, quanto ao % de 'Alíquota de COFINS' e o 'Cód. sit. tributária:';

**(2)** Recomenda-se sempre criar regras específicas para o respectivo tipo de movimento;

**(2)** O cálculo de PIS e COFINS é obrigatório para todas as movimentações de VENDA, mesmo que a incidência seja zero. Revisar a marcação de COFINS no Cadastro das Preferências da Empresa (Comercial » Preferências » Empresa) e no Cadastro de Tipos de Operação -TOP (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)

![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16443889852439) **CAUSA:**

Quando for emitida uma NF-e com o total do COFINS da NF-e diferente do somatório do valor do COFINS de cada item, será retornado a rejeição

**![Imagem 8: OBSERVAÇÕES :](https://ajuda.sankhya.com.br/hc/article_attachments/16443873594519)OBSERVAÇÕES:**

[Manual de Orientação do Contribuinte](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=9hd38oni4Nc=)
