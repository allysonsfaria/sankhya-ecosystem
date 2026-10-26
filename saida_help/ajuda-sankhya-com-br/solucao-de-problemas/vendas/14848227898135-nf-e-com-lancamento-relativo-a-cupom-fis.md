---
id: "14848227898135"
titulo: "NF-e com lançamento relativo a Cupom Fiscal referencia uma NFC-e [nItem: [nItem:nnn]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14848227898135-NF-e-com-lan%C3%A7amento-relativo-a-Cupom-Fiscal-referencia-uma-NFC-e-nItem-nItem-nnn"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T14:57:52Z"
rotulos: ["NF-e", "SEFAZ", "CFOP", "NFC-e", "375", "NF-e rejeitada por referência a NFC-e", "CFOP 5.929 e 6.929 rejeitados em alguns estados", "Corrija CFOP ou use Cupom Fiscal", "Erro", "Documentos Eletrônicos"]
---

# NF-e com lançamento relativo a Cupom Fiscal referencia uma NFC-e [nItem: [nItem:nnn]

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16635918549655) MENSAGEM:**

375 - Rejeição: NF-e com lançamento relativo a Cupom Fiscal referencia uma NFC-e [nItem: [nItem:nnn]

Veja a regra de validação da SEFAZ:

![Imagem 2: Veja a regra de validação da SEFAZ:](https://ajuda.sankhya.com.br/hc/article_attachments/14847033268759)

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16635918551319) SOLUÇÃO:**

Verifique se o CFOP foi informado indevidamente. Como essa regra de validação é opcional, em muitos Estados essa rejeição não vai ocorrer. Se o CFOP foi informado indevidamente, identifique outro código para o CFOP que adeque-se a operação. Caso seja mantido o CFOP, informe em substituição a NFC-e referenciada um Cupom Fiscal

**(2)** (**NT2015/002**) - Nota Técnica

<http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=hDS5co/qWOc=>

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16635918553623) CAUSA:**

A SEFAZ de alguns estados rejeitam a emissão de notas fiscais com CFOP **5.929** e **6.929** referenciando NFC-e

| **Posição da SEFAZ** | **UF** |
| --- | --- |
| 0=Não | MT,PE,RJ,SC |
| 1=Aceita CFOP 5929 com NFC-e referenciada; | AC,AL,AP,AM,DF,ES,MA,MG,MS,  PA,PB,PR,PI,RN,RS,RO,SP,SE,TO |
| Não se posicionou | CE,GO |

Fonte: [Portal NFC-e](http://nfce.encat.org/), em Desenvolvedor opção Regra de validação

**![Imagem 5: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16635918554775) OBSERVAÇÃO:**

Pode sofrer alterações de acordo com determinação de cada Estado.
