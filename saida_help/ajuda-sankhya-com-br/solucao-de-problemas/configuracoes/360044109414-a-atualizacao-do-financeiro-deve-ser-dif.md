---
id: "360044109414"
titulo: "A atualização do financeiro deve ser diferente entre a top de origem e a top de destino"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044109414-A-atualiza%C3%A7%C3%A3o-do-financeiro-deve-ser-diferente-entre-a-top-de-origem-e-a-top-de-destino"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:55:04Z"
rotulos: ["Configuração", "Movimentação Financeira", "Atualização", "TOP", "Financeiro", "CORE_E04611", "Tipos de Operação (TOP)", "Atualização do Financeiro"]
---

# A atualização do financeiro deve ser diferente entre a top de origem e a top de destino

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16636785370391) MENSAGEM:**

[CORE\_E04611]:  A atualização do financeiro deve ser diferente entre a top de origem e a top de destino.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16636785377303) SOLUÇÃO:**

![Imagem 3: Identifique os 'Tipos de Operação' envolvidos nesse processo: TOP de Origem e TOP de Destino.](https://ajuda.sankhya.com.br/hc/article_attachments/16636746974103) Identifique os 'Tipos de Operação' envolvidos nesse processo: TOP de Origem  e TOP de Destino.

**Exemplo:** Emissão de uma devolução de compra.

- TOP de Origem: COMPRA
- TOP de Destino: DEVOLUÇÃO DE COMPRA

![Imagem 4: Acesse a tela "Tipos de Operação-TOP" (Caminho de acesso: Comercial » Arquivo » Cadastros) e verifique a configuração…](https://ajuda.sankhya.com.br/hc/article_attachments/16636746976791) Acesse a tela **"Tipos de Operação-TOP"** (Caminho de acesso: Comercial » Arquivo » Cadastros) e verifique a configuração do campo **"Financeiro"** de ambas.

![Imagem 5: Acesse a tela "Tipos de Operação-TOP" (Caminho de acesso: Comercial » Arquivo » Cadastros) e verifique a configuração…](https://ajuda.sankhya.com.br/hc/article_attachments/14836861233559)

![Imagem 6: A atualização de financeiro não deverá ser a mesma para TOP Origem e TOP Destino. Reveja o processo utilizado e…](https://ajuda.sankhya.com.br/hc/article_attachments/16636746978327) A atualização de financeiro não deverá ser a mesma para TOP Origem e TOP Destino. Reveja o processo utilizado e sintonize com o usuário que acompanhou a implantação do sistema para alinhar a parametrização adequada ao cenário da empresa.

De forma geral para o exemplo do item 1:

- TOP de Origem: COMPRA »**Financeiro** = despesa
- TOP de Destino: DEVOLUÇÃO DE COMPRA »**Financeiro** = receita

Entenda que **se a sua compra gerou uma despesa**, **a devolução dessa compra gerou uma receita**. Não é possível prever um processo em que ambas as TOP'S irão gerar Receita, por exemplo.

![Imagem 7: Realizados os ajustes, refaça o faturamento. Lembre-se que se o lançamento referente a TOP, que teve alteração de…](https://ajuda.sankhya.com.br/hc/article_attachments/16636746984471) Realizados os ajustes, refaça o faturamento. Lembre-se que se o lançamento referente a TOP, que teve alteração de informações, deve ser feito novamente do zero.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16636785391383)CAUSA:**

Mensagem apresentada ao realizar faturamento ou devolução através do sistema, quando o campo Financeiro da TOP de Origem for igual a TOP de Destino.
