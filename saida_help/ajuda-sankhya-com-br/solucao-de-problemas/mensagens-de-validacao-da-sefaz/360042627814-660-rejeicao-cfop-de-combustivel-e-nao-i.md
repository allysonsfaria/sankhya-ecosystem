---
id: "360042627814"
titulo: "660 Rejeição: CFOP de Combustível e não informado grupo de combustível.(NT2017/002)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042627814-660-Rejei%C3%A7%C3%A3o-CFOP-de-Combust%C3%ADvel-e-n%C3%A3o-informado-grupo-de-combust%C3%ADvel-NT2017-002"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:08:01Z"
rotulos: ["ERRONF", "Produtos", "Configuração", "NF-e", "Impostos", "CFOP", "Combustível", "660", "CFOP de Combustível", "Preencher grupo de combustível", "Falta de informação no grupo de combustível", "CFOP de Combustível e não informado grupo de combustível", "660 Rejeição:", "Rejeição 660"]
---

# 660 Rejeição: CFOP de Combustível e não informado grupo de combustível.(NT2017/002)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16505745016471) MENSAGEM:**

660 Rejeição: CFOP de Combustível e não informado grupo de combustível.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16505745023639) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Configurações » Avançado » Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/16505745029911) Acesse: Configurações » Avançado » Preferências

Pesquise pelo parâmetro: **"COMBUSTIVEL- Distribuidor de combustível?"** e deixe ligado.

![Imagem 4: Acesse: Configurações » Cadastros » Produtos » Produtos](https://ajuda.sankhya.com.br/hc/article_attachments/16505745046679) Acesse: Configurações » Cadastros » Produtos » Produtos

Com o parâmetro acima ligado, no cadastro de produtos, será ativada uma aba com o nome **"COMBUSTÍVEL"**.

Preencha os campos:

- **"Código ANP"**
- **"Autorização CODIF"**
- **"Descrição ANP"**

![Imagem 5: "Descrição ANP"](https://ajuda.sankhya.com.br/hc/article_attachments/14600985994647)

Busque orientações com o contador para o correto preenchimento dos campos acima.

![Imagem 6: Após os ajustes, redigite os itens nota ou fature novamente o pedido.](https://ajuda.sankhya.com.br/hc/article_attachments/16505716205847) Após os ajustes, redigite os itens nota ou fature novamente o pedido.

No XML, o grupo de Combustível, será gerado da seguinte forma:

<!-- Grupo de Combustível -->
     <comb>
          <cProdANP>210101001</cProdANP>
               <descANP>GÁS COMBUSTÍVEL</descANP>
          <UFCons>ES</UFCons>
    </comb>

Caso a nota não seja de movimentação de combustível, revise o cadastro da TOP, no que se refere a CFOP que incidiu na nota e fazer o devido ajuste.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16505745069975) CAUSA:**

Quando for emitida uma NF-e e for informado CFOP para operações com Combustível e não for informado o Grupo de Combustível (tag: comb), haverá rejeição.

**![Imagem 8: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/16505716228503) OBSERVAÇÕES:**

**(1)** ([NT2017/002](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Yy9URkJxo5s=)) - Nota Técnica:

**(1)** Lista de CFOPs, suportadas para movimentação de Combustível:

1651,1652,1653,1658,1659,1660,1661,1662,1663,1664,2651,2652,2652,2653,2658,2659,2660,2661,2662,2663,2664,3651,3652,3653,5651,5652,5653,5654,5655,5656,5657,5658,5659,5660,5661,5662,5663,5664,5665,5666,5667,6651,6652,6653,6654,6655,6656,6657,6658,6659,6660,6661,6662,6663,6664,6665,6666,6667,7651,7654,7667
