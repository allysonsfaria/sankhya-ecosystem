---
id: "360043362733"
titulo: "A atualização de estoque deve ser diferente entre a TOP de origem e a TOP de destino"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043362733-A-atualiza%C3%A7%C3%A3o-de-estoque-deve-ser-diferente-entre-a-TOP-de-origem-e-a-TOP-de-destino"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:05:25Z"
rotulos: ["Configuração", "Atualização", "TOP", "Estoque", "CORE_E04610", "Atualização de Estoque", "TOP de Destino", "TOP de Origem", "Erro"]
---

# A atualização de estoque deve ser diferente entre a TOP de origem e a TOP de destino

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16114468547735) MENSAGEM:**

[CORE\_E04610] A atualização de estoque deve ser diferente entre a TOP de origem e a TOP de destino.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16114452984471) SOLUÇÃO:**

![Imagem 3: Identifique os Tipos de Operação envolvidos nesse processo: TOP de Origem e TOP de Destino.](https://ajuda.sankhya.com.br/hc/article_attachments/16114468558487) Identifique os Tipos de Operação envolvidos nesse processo: TOP de Origem  e TOP de Destino.

**Exemplo:** Emissão de uma devolução de compra.

**(2)** TOP de Origem : COMPRA

**(2)** TOP de Destino: DEVOLUÇÃO DE COMPRA

![Imagem 4: Acesse a tela " Tipos de Operação-TOP " (Comercial » Arquivo » Cadastros) e verifique a configuração do campo…](https://ajuda.sankhya.com.br/hc/article_attachments/16114453009047) Acesse a tela **"[Tipos de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"** (Comercial » Arquivo » Cadastros) e verifique a configuração do campo **"Atualização do Estoque"** de ambas.

![Imagem 5: Acesse a tela " Tipos de Operação-TOP " (Comercial » Arquivo » Cadastros) e verifique a configuração do campo…](https://ajuda.sankhya.com.br/hc/article_attachments/14559560147095)

![Imagem 6: A atualização de estoque não deverá ser a mesma para TOP Origem e TOP Destino. Reveja o processo utilizado e sintonize…](https://ajuda.sankhya.com.br/hc/article_attachments/16114453017879) A atualização de estoque não deverá ser a mesma para TOP Origem e TOP Destino. Reveja o processo utilizado e sintonize com o usuário que acompanhou a implantação do sistema para alinhar a parametrização adequada ao cenário da empresa.

De forma geral para o exemplo do item 1:

**(2)** TOP de Origem: COMPRA » campo **"Atualização do estoque": ENTRAR**

**(2)** TOP de Destino: DEVOLUÇÃO DE COMPRA » campo **"Atualização do estoque": BAIXAR**

![Imagem 7: (2) TOP de Destino: DEVOLUÇÃO DE COMPRA » campo "Atualização do estoque": BAIXAR](https://ajuda.sankhya.com.br/hc/article_attachments/14559341843223)

Entenda que **se a sua compra gerou uma entrada de estoque**, **a devolução dessa compra gerou uma saída**. Não é possível prever um processo em que ambas as TOP'S irão gerar entrada, por exemplo.

![Imagem 8: Realizados os ajustes, refaça o faturamento. Lembre-se que se o lançamento referente a TOP que teve alteração de…](https://ajuda.sankhya.com.br/hc/article_attachments/16114453022743) Realizados os ajustes, refaça o faturamento. Lembre-se que se o lançamento referente a TOP que teve alteração de informações deve ser feito novamente do zero.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16114468599575) CAUSA:**

Mensagem apresentada ao realizar faturamento ou devolução através do sistema, quando o campo Atualização do estoque da TOP de Origem for igual a TOP de Destino.
