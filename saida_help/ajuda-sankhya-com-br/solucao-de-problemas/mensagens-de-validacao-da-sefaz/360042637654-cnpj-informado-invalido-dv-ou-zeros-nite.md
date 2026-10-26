---
id: "360042637654"
titulo: "CNPJ informado inválido (DV ou zeros) - [nItem: X]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042637654-CNPJ-informado-inv%C3%A1lido-DV-ou-zeros-nItem-X"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:51Z"
rotulos: ["ERRONF", "#RevisadoBraga", "Produtos", "Configuração", "Fiscal", "NF-e", "Portal de Vendas", "XML", "489", "[489-Rejeição]: CNPJ informado inválido", "Escala \"N\" CNPJ faltante", "Preencher CNPJ", "Erro"]
---

# CNPJ informado inválido (DV ou zeros) - [nItem: X]

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16444044050583) MENSAGEM:**

[489-Rejeição]: CNPJ informado inválido (DV ou zeros) - [nItem: X]

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16444044052119) SOLUÇÃO:**

Para correção siga os passos abaixo:

![Imagem 3: Acesse o " Portal de Vendas " e selecione a nota que está apresentando a Rejeição.](https://ajuda.sankhya.com.br/hc/article_attachments/16444068698519) Acesse o "**[Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654)"** e selecione a nota que está apresentando a Rejeição.

Botão: "**NF-e" »** "**Gerar XML da NF-e em arquivo para conferência"**.

Salve o arquivo na extensão \*.xml em um diretório do computador e abra o arquivo em 'Bloco de Notas' (Recomendamos o aplicativo '[Notepad++](https://notepad-plus-plus.org/)'). Desta forma, é possível identificar qual produto está com a rejeição indicada.

No XML estará indicado o seguinte trecho e a tag <CNPJFab> preenchida de forma incorreta.

<indEscala>N</indEscala>
**<CNPJFab>00000000000000</CNPJFab>**

![Imagem 4: Existe 2(duas) formas de corrigir.](https://ajuda.sankhya.com.br/hc/article_attachments/16444044055319) Existe 2(duas) formas de corrigir.

**(1)** 2.1- Na "**[Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414)"**, acesse a grade de itens e verifique 2 campos ("**Indicador de Escala Relevante"** e "**CNPJ do Fabricante da Mercadoria"**)

![Imagem 5: (1) 2.1- Na " Central de Vendas " , acesse a grade de itens e verifique 2 campos (" Indicador de Escala Relevante" e "…](https://ajuda.sankhya.com.br/hc/article_attachments/360060881273)

Preencha o CNPJ do Fabricante da Mercadoria, caso o Indicador de Escala Relevante esteja com a opção **'Produzido em Escala NAO Relevante('N')'**.

Salve a alteração feita nos itens da nota e gere o Lote novamente da NF-e.

**(1)** 2.2- Acesse o cadastro de Produtos e efetue os ajustes necessários, preenchendo adequadamente o CNPJ do Fabricante. Campos: "**Indicador de Escala Relevante"** e **"CNPJ do Fabricante da Mercadoria"**

![Imagem 6: (1) 2.2- Acesse o cadastro de Produtos e efetue os ajustes necessários, preenchendo adequadamente o CNPJ do Fabricante.…](https://ajuda.sankhya.com.br/hc/article_attachments/360059967674)

Salve a alteração feita nos cadastros dos produtos, fature novamente a Nota e, em seguida, gere Lote da NF-e.

**![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16444044058391) OBSERVAÇÃO:**

**Indicador de Escala Relevante**

O Indicador de Escala Relevante é um novo campo na NFe, introduzido a partir da versao NF-e **4.0**, nele indica-se bens e mercadorias que podem não se submeter ao regime de Substituição Tributária.

Ele foi instituído de acordo com o [Convênio ICMS 52/2017](https://www.confaz.fazenda.gov.br/legislacao/convenios/2017/CV052_17):

**Como o Indicador de Escala Relevante é usado na NFe**

O contribuinte deve indicar no campo indEscala da nota fiscal uma das opções:

S – Produzido em Escala Relevante;

N – Produzido em Escala NÃO Relevante.

Quando uma nota fiscal com um produto em escala não relevante é emitida, é obrigatório informar o CNPJ do fabricante no campo CNPJFab.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16444068703767) CAUSA:**

Ocorre quando o campo Indicador de Escala Relevante for configurado com a opção "**Produzido em Escala NÃO Relevante**" e o campo "**CNPJ do Fabricante da Mercadoria"** não estiver preenchido. O sistema irá gerar no xml as tag's <indEscala>N<indEscala> e <CNPJFab>00000000000000</CNPJFab> (com zeros), resultando na rejeição.
