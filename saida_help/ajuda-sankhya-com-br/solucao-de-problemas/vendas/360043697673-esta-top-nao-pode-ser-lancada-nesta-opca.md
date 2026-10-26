---
id: "360043697673"
titulo: "Esta TOP não pode ser lançada nesta opção"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043697673-Esta-TOP-n%C3%A3o-pode-ser-lan%C3%A7ada-nesta-op%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:02:49Z"
rotulos: ["Configuração", "NF-e", "Movimentação Financeira", "SEFAZ", "TOP", "ORA-20101", "Erro ORA-20101 ao lançar TOP de Destino", "Verificar e configurar a TOP Denegada corretamente", "Incompatibilidade da TOP com o tipo de movimento da nota"]
---

# Esta TOP não pode ser lançada nesta opção

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16148826730007) MENSAGEM:**

ORA-20101: Esta TOP não pode ser lançada nesta opção.Nota de Nro Único: 
ORA-06512: em "SANKHYA.TRG\_UPD\_TGFCAB", line 945
ORA-04088: erro durante a execução do gatilho 'SANKHYA.TRG\_UPD\_TGFCAB'

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16148790664343) SITUAÇÃO:**

Ao tentar efetuar o lançamento, usando uma TOP de Destino, a seguinte mensagem é apresentada.

(1)** CASO:**

Mensagem pode ser apresentada ao **"Consultar Situação Atual da Nota"** de uma NF-e com Status **Denegada** na SEFAZ e diferente desse no sistema.

**![Imagem 3: SOLUÇÃO](https://ajuda.sankhya.com.br/hc/article_attachments/16148790668823) SOLUÇÃO**

![Imagem 4: Verifique no cadastro de " Tipos de Operação " se existe uma Top Denegada para o mesmo Tipo de Movimento da nota…](https://ajuda.sankhya.com.br/hc/article_attachments/16148790670999) Verifique no cadastro de **"**[**Tipos de Operação**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)**"** se existe uma **Top Denegada** para o mesmo Tipo de Movimento da nota analisada.

(1)** EXEMPLO:** Mensagem ocorrendo para uma nota de **Devolução de Venda**, dessa forma é necessário uma Top Denegada com o tipo de movimento Devolução de Venda.

![Imagem 5: Caso não exista, configure a mesma e/ou duplique uma atual (que tenha sido validada junto ao Consultor de sua…](https://ajuda.sankhya.com.br/hc/article_attachments/16148790675479) Caso não exista, configure a mesma e/ou duplique uma atual (que tenha sido validada junto ao Consultor de sua Franquia), alterando apenas o Tipo de Movimento.

![Imagem 6: Anote o código da Top Denegada criada e vincule a mesma na aba "NF-e/NFC-e" » Campo ' Tipo de Operação NF-e Denegada '…](https://ajuda.sankhya.com.br/hc/article_attachments/16148826754967) Anote o código da Top Denegada criada e vincule a mesma na aba **"NF-e/NFC-e"** » Campo '**Tipo de Operação NF-e Denegada**' da TOP utilizada no lançamento que originou a mensagem.

![Imagem 7: Realizado tais ajustes, refaça a Consulta situação atual da nota , dessa forma o Status deverá ser devidamente…](https://ajuda.sankhya.com.br/hc/article_attachments/16148790683287) Realizado tais ajustes, refaça a Consulta situação atual da nota, dessa forma o Status deverá ser devidamente atualizado para Denegada.

![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16148826766103) **CAUSA:**

Ocorre quando uma TOP de Destino não pode ser usado com o tipo de movimento adequado.

Observação: Essa validação pode ocorrer no portal de importação de xml,  a configuração do campo "Top para simulação de impostos" nas 'Preferências para importação de NF-e' influência diretamente na geração da nota de emissão própria. Caso a nota gerada não seja a configurada com a top  como emissão própria, analisar o campo 'Top para simulação de impostos'
