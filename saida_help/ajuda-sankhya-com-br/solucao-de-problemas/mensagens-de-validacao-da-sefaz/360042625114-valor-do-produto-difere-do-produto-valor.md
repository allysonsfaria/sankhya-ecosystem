---
id: "360042625114"
titulo: "Valor do Produto difere do produto Valor Unitário de Comercialização e Quantidade Comercial. (NT2011/005)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042625114-Valor-do-Produto-difere-do-produto-Valor-Unit%C3%A1rio-de-Comercializa%C3%A7%C3%A3o-e-Quantidade-Comercial-NT2011-005"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:08:34Z"
rotulos: ["ERRONF", "Produtos", "Configuração", "NF-e", "SEFAZ", "629", "Valor Unitário", "Divergência no Valor do Produto e Valor Unitário", "Quantidade"]
---

# Valor do Produto difere do produto Valor Unitário de Comercialização e Quantidade Comercial. (NT2011/005)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16510257743767) MENSAGEM:**

[629 - Rejeição]: Valor do Produto difere do produto Valor Unitário de Comercialização e Quantidade Comercial.

**![Imagem 2: SOLUÇÃO: Para correção, siga os passos abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16510257752727) SOLUÇÃO:**
Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Configurações » Cadastros » Produtos » Produtos Aba: "Venda" Campo "Digitação na nota": 'Quant. e Valor…](https://ajuda.sankhya.com.br/hc/article_attachments/16510234634519) Acesse: Configurações » Cadastros » Produtos » Produtos
Aba: **"Venda"**
Campo **"Digitação na nota":** 'Quant. e Valor Unitário'

![Imagem 4: Acesse: Comercial » Rotinas » Central de Vendas Veja os itens da Nota e verifique qual produto está com a diferença…](https://ajuda.sankhya.com.br/hc/article_attachments/16510257761431) Acesse: Comercial » Rotinas » Central de Vendas
Veja os itens da Nota e verifique qual produto está com a diferença entre **'Quantidade' x 'Valor** **Unitário**'. Se atentar caso haja acréscimo/desconto.

Exemplo:

![Imagem 5: Exemplo:](https://ajuda.sankhya.com.br/hc/article_attachments/360060880673)

No exemplo acima nota-se o '**Vlr. Unitário'**  igual à R$ 9,99 (<vUnCom>9.9900</vUnCom>), com **quantidade**  igual à 2 (<qCom>2.0000</qCom>) e o **Vlr. Total** foi calculado em R$ 20,00 (<vProd>20.00</vProd>).
Contudo, o valor esperado dessa multiplicação seria **R$ 19,98** (9.9900 \* 2.0000).

![Imagem 6: Acesse: Configurações » Avançado » Preferências e ligue o parâmetro " DIVTOTQTDNFE- Divide VLRTOT do item pela QTDNEG…](https://ajuda.sankhya.com.br/hc/article_attachments/16510234643607) Acesse: Configurações » Avançado » Preferências e ligue o parâmetro "**DIVTOTQTDNFE- Divide VLRTOT do item pela QTDNEG no XML da NFE"**

A funcionalidade do parâmetro é dividir a tag <vProd> pela tag <qCom> até a quantidade de casas decimais cuja diferença fique dentro do limite aceitável pela SEFAZ. Isso vai evitar que a tag <vUnCom> tenha sempre 10 casas decimais fixas.

![Imagem 7: Após os ajustes redigite Empresa/Parceiro da Nota e gere lote novamente. Caso seja necessário inutilize a nota e fature…](https://ajuda.sankhya.com.br/hc/article_attachments/16510257769879) Após os ajustes redigite Empresa/Parceiro da Nota e gere lote novamente. Caso seja necessário inutilize a nota e fature novamente. Certifique os ajustes anteriormente feitos e gere lote.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16510234649367) CAUSA:**

A mensagem de erro é apresentada quando a Sefaz verifica as informações quanto a Valor Unitário X Quantidade X Valor total do item.
Ocorre em casos que tenha produtos/serviços com grandes quantidades e valores muito pequenos e/ou conversão de unidades.

O **SankhyaOM/JivaEVO** por padrão multiplica a Quant. pelo VlrLiqUnitario para ter o total do item, e o Sefaz faz o contrario em sua validação, divide o total do item que foi informado na tag <vProd> pela quantidade informada na tag <qCom>.

**![Imagem 9: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16510234651031) OBSERVAÇÃO:**

([NT2011/005](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=41lDzlbw3co=)) - Nota técnica
