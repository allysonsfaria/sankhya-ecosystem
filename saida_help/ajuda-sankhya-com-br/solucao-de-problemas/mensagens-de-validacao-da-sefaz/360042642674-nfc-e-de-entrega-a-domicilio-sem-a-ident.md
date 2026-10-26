---
id: "360042642674"
titulo: "NFC-e de entrega a domicílio sem a identificação do destinatário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042642674-NFC-e-de-entrega-a-domic%C3%ADlio-sem-a-identifica%C3%A7%C3%A3o-do-destinat%C3%A1rio"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:25Z"
rotulos: ["ERRONF", "Configuração", "Parceiro", "XML", "SEFAZ", "TOP", "NFC-e", "787", "Rejeição 787: NFC-e Entrega Domicílio Sem Destinatário"]
---

# NFC-e de entrega a domicílio sem a identificação do destinatário

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16444062467095) MENSAGEM:**

[787-Rejeição]: NFC-e de entrega a domicílio sem a identificação do destinatário.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16444037822999) SOLUÇÃO:**

Sempre que houver entrega em domicílio, é obrigatório informar os dados do destinatário da NFC-e.

![Imagem 3: Acesse " Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/article_attachments/16444062471447) Acesse "**[Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)**

(Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)

- Aba: "**NF-e/NFC-e"**
- Indicador de Presença para NF-e/NFC-e: = **4-NFC-e com entrega em domicilio**

Quando a TOP estiver configurada com a opção 4, o parceiro da nota deverá ser devidamente registrado com os dados do endereço para que seja preenchido no XML da NFC-e o endereço de entrega.

Ou seja, não deverá ser utilizado um parceiro 'genérico', e sim um parceiro 'real', com os dados de endereço devidamente configurados.

![Imagem 4: Após os ajustes, gere lote da NFC-e novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16444037825559) Após os ajustes, gere lote da NFC-e novamente.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16444037827479) CAUSA:**

Quando for emitida uma NFC-e com o indicador de presença do comprador como "4 - NFC-e em operação com entrega a domicílio" e não for informado os dados do destinatário, será retornado a rejeição.

**![Imagem 6: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16444062478615) OBSERVAÇÃO:**

[Manual de Orientação do Contribuinte](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=9hd38oni4Nc=)
