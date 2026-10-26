---
id: "15836926415511"
titulo: "O campo é obrigatório quando existir um registro filho 0220 com o campo código de barra preenchido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/15836926415511-O-campo-%C3%A9-obrigat%C3%B3rio-quando-existir-um-registro-filho-0220-com-o-campo-c%C3%B3digo-de-barra-preenchido"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:56:03Z"
rotulos: ["Produtos", "Configuração", "NF-e", "Impostos", "Campo obrigatório se registro 0220 tem código de barras.", "Verifique preenchimento de \"Referência\" e \"EAN/GTIN Produto\".", "Ajuste parâmetros para usar unidade padrão ou código de barras alternativa.", "Erro"]
---

# O campo é obrigatório quando existir um registro filho 0220 com o campo código de barra preenchido

(1)** MENSAGEM:**

O campo é obrigatório quando existir um registro filho 0220 com o campo código de barra preenchido.

(2)** CAUSA:**

Erro na geração do registro 0220 pela ausência do código de barras do produto.

(3)** SOLUÇÃO:**

Para validar a geração do código de barras/referência (campo 4) da unidade padrão no registro 0200 é necessário verificar as seguintes informações:
 
**Configurações > Cadastros > Produtos >**
• Aba Geral
Campo "Referência" deve estar preenchido;

![Imagem 1: • Aba Impostos Campo "EAN/GTIN Produto p/ NF-e" deve estar preenchido com uma das opções. Caso seja indicada a opção…](https://ajuda.sankhya.com.br/hc/article_attachments/15913972499863)
 
• Aba Impostos
Campo "EAN/GTIN Produto p/ NF-e" deve estar preenchido com uma das opções. 
Caso seja indicada a opção "Cód. Barras da Unidade Alternativa ou a Referência", o sistema irá validar se o preenchimento da referência na unidade padrão é diferente do código de barras vinculada na unidade alternativa.

![Imagem 2: Parâmetro: Usa Unidade padrao do produto no R.0200 - EFD- USAUNIPADR0200 Desligado (Default): não altera o…](https://ajuda.sankhya.com.br/hc/article_attachments/15914030893079)
 
**Parâmetro: Usa Unidade padrao do produto no R.0200 - EFD- USAUNIPADR0200**
**Desligado (Default):** não altera o comportamento que temos do sistema hoje.
**Ligado:** vai forçar a Unidade Padrão do produto no registro 0200.

![Imagem 3: Parâmetro: Usar cod. de barras de unidade alternativa no regi- LIVUSACODBARALT Ligado: Irá utilizar o código de barras…](https://ajuda.sankhya.com.br/hc/article_attachments/15914079409559)
 
**Parâmetro: Usar cod. de barras de unidade alternativa no regi- LIVUSACODBARALT**
**Ligado:** Irá utilizar o código de barras da unidade alternativa na geração do registro 0200.
**Desligado:** o sistema não irá considerar os dados da unidade alternativa na geração do registro 0200.
Vale reforçar que esse parâmetro só é acionado pelo sistema na geração, se o campo do GTIN na nota for igual ao código de barras da unidade alternativa. Do contrário, o sistema não verifica a configuração desse parâmetro.

![Imagem 4: Parâmetro: Usar cod. de barras de unidade alternativa no regi- LIVUSACODBARALT Ligado: Irá utilizar o código de barras…](https://ajuda.sankhya.com.br/hc/article_attachments/15914083173655)
