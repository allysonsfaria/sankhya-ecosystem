---
id: "16612708990743"
titulo: "Nota (s) com frete incluso.<br>Não é possível vincular o CT-e com esta(s) nota(s)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/16612708990743-Nota-s-com-frete-incluso-br-N%C3%A3o-%C3%A9-poss%C3%ADvel-vincular-o-CT-e-com-esta-s-nota-s"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-09-18T14:22:37Z"
rotulos: ["CT-e", "Configuração", "NF-e", "Financeiro", "Gestão de Frete em Notas", "Erro", "Documentos Eletrônicos"]
---

# Nota (s) com frete incluso.<br>Não é possível vincular o CT-e com esta(s) nota(s)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16612708975127)  MENSAGEM:**

Nota (s) com frete incluso.<br>Não é possível vincular o CT-e com esta(s) nota(s).

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16612699884567) CAUSA:**

O erro ocorre pois a nota referenciada já se encontra aprovada no sistema e com o campo tipo frete definido como incluso.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16612693011607) SOLUÇÃO:**

Segue abaixo alguns parâmetros que influenciam na rotina:

![Imagem 4: O parâmetro "Recalcular Custos ao final de calc.de frete - RECALCCUSTOFRET" ao ser habilitado, calculará o custo de…](https://ajuda.sankhya.com.br/hc/article_attachments/16612699880343) O parâmetro **"Recalcular Custos ao final de calc.de frete - RECALCCUSTOFRET"** ao ser habilitado, calculará o custo de entrada da nota e o custo médio.
 
![Imagem 5: O parâmetro "Recalcular Custos ao final de calc.de frete - RECALCCUSTOFRET" ao ser habilitado, calculará o custo de…](https://ajuda.sankhya.com.br/hc/article_attachments/16618524469399) Caso o parâmetro **"Permite Frete Extra Nota em nota com Frete Incluso? - RATEXTNOTAFRINC"** se encontre ligado, o sistema permitirá o rateio do frete mesmo quando as notas já possuam o frete incluso.
 
![Imagem 6: O parâmetro "Recalcular Custos ao final de calc.de frete - RECALCCUSTOFRET" ao ser habilitado, calculará o custo de…](https://ajuda.sankhya.com.br/hc/article_attachments/16618486417559) Caso o parâmetro **"Aquisição de serviço de frete com frete incluso - AQSERVFRETINC"** esteja ativado, o cálculo de frete para melhor transportadora (de forma automática ou manual), desde que seja Incluso, será registrado no campo **"Vlr. frete calc."**.
