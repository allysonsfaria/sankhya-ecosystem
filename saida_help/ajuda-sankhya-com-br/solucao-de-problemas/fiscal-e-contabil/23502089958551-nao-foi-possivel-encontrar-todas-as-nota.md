---
id: "23502089958551"
titulo: "Não foi possível encontrar todas as notas referenciadas no XML do documento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/23502089958551-N%C3%A3o-foi-poss%C3%ADvel-encontrar-todas-as-notas-referenciadas-no-XML-do-documento"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:48:15Z"
rotulos: ["Configuração", "NF-e", "XML", "Importação", "TOP", "Não foi possivel encontrar todas as notas referenciadas no XML do documento.", "CORE_E03151"]
---

# Não foi possível encontrar todas as notas referenciadas no XML do documento

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/23502089924119) MENSAGEM:**

[CORE\_E03151] Não foi possível encontrar todas as notas referenciadas no XML do documento.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/23502068636183) SOLUÇÃO:**

Através da marcação **"Desconsidera Nfe de orig. referenciada? (Importação de XML)",** na tela **Tipos de Operação TOP** (Comercial > Arquivo > Cadastros / Financeiro > Arquivos > Cadastros), quando habilitada, é possível importar o XML das devoluções de vendas sem que haja a NF-e de referência no sistema.

**Observação:**

Com a marcação acima efetuada, o sistema irá preencher a TOP ao importar o XML de Devolução de Venda. Além dessa marcação, é necessário que exista na tela **"Preferências da Empresa"** (Comercial » Preferências » Empresa), aba **"Modelo de Importação de XML",** o modelo de nota/pedido cadastrado na tela **"Modelo de Notas e Pedidos",** para respectiva TOP.

Vale ressaltar que, quando essa TOP é utilizada não se pode ser utilizar juntamente a marcação **"Permitir vinculo Manual para NFe Devolução para NFe Venda"** que, ao ser efetuada, determina se o Portal de Importação permitirá o vínculo manualmente das referências entre as NFe de Devolução e NFe de Venda. 

![Imagem 3: Vale ressaltar que, quando essa TOP é utilizada não se pode ser utilizar juntamente a marcação "Permitir vinculo Manual…](https://ajuda.sankhya.com.br/hc/article_attachments/23502089945239)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/23502068631831) CAUSA:**

Ao importar uma NFe de emissão própria, no portal de importação XML, o sistema apresenta a mensagem acima, não permitindo a importação.
