---
id: "360042758794"
titulo: "Código Município do Destinatário: difere da UF do Destinatário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042758794-C%C3%B3digo-Munic%C3%ADpio-do-Destinat%C3%A1rio-difere-da-UF-do-Destinat%C3%A1rio"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:01Z"
rotulos: ["ERRONF", "Configuração", "Parceiro", "NF-e", "Cidades", "SEFAZ", "275", "Rejeição", "Corrija na NF-e", "Código município rejeitado", "Verifique endereço do parceiro"]
---

# Código Município do Destinatário: difere da UF do Destinatário

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16514655357591) **MENSAGEM:**

[275 - Rejeição]: Código Município do Destinatário: difere da UF do Destinatário.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16514618856983) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse a tela " Parceiros " (Configurações » Cadastros):](https://ajuda.sankhya.com.br/hc/article_attachments/16514618859159) Acesse a tela "**[Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)"** (Configurações » Cadastros):

- Localize os parceiros envolvidos na NF-e rejeitada ( Parceiro/ Parceiro Transportadora)
- Na aba **"Endereços"**, localize o Cód.Cidade dos mesmos.

![Imagem 4: Acessar a tela " Cidades " (Configurações » Cadastros » Endereços):](https://ajuda.sankhya.com.br/hc/article_attachments/16514655364887) Acessar a tela **"[Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913)"**  (Configurações » Cadastros » Endereços):

- Localize a cidade identificada no Item 1
- Verifique o conteúdo do campo **"Mun. domicílio fiscal"**:

![Imagem 5: Verifique o conteúdo do campo "Mun. domicílio fiscal" :](https://ajuda.sankhya.com.br/hc/article_attachments/14640668218391)

![Imagem 6: Acesse o site do IBGE: https://cidades.ibge.gov.br/](https://ajuda.sankhya.com.br/hc/article_attachments/16514618864663) Acesse o site do IBGE: <https://cidades.ibge.gov.br/>

- Em 'Pesquisar' digite o nome da cidade
- Ao abrir o conteúdo referente a mesma localize a informação "Código do Município"

![Imagem 7: Na tela Cidades (Configurações » Cadastros » Endereços) corrija o campo "Mun. domicílio fiscal" para a informação…](https://ajuda.sankhya.com.br/hc/article_attachments/16514618866071) Na tela Cidades (Configurações » Cadastros » Endereços) corrija o campo **"Mun. domicílio fiscal"** para a informação localizada no item anterior.

![Imagem 8: Abra a nota na "Central de Vendas" , redigite os dados do cabeçalho e gere um novo lote. Se a rejeição persistir…](https://ajuda.sankhya.com.br/hc/article_attachments/16514618868887) Abra a nota na **"Central de Vendas"**, redigite os dados do cabeçalho e gere um novo lote. Se a rejeição persistir inutilize/exclua a respectiva NF-e e refaça o lançamento.

**![Imagem 9: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16514655371287) OBSERVAÇÃO:**

Caso não consiga essa informação no site do IBGE, solicite ao seu Contador.

**![Imagem 10: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16514655373207) CAUSA:**

Quando emitida uma NF-e para destinatário localizado no Brasil (com UF diferente de EX - Exterior) e os dois primeiros dígitos do código do município for diferente do Código da UF correspondente a Sigla da UF informada nos dados do endereço do destinatário, será apresentada a rejeição.
