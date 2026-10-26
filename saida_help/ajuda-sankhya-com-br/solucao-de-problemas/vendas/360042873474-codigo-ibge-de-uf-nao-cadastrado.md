---
id: "360042873474"
titulo: "Código IBGE de UF não cadastrado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042873474-C%C3%B3digo-IBGE-de-UF-n%C3%A3o-cadastrado"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-08-04T14:07:03Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "NF-e", "CORE_E03959", "Cadastro", "Preencha corretamente", "Código IBGE faltando", "Verifique endereços"]
---

# Código IBGE de UF não cadastrado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16108775829783) MENSAGEM:**

Código IBGE de UF não cadastrado.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16108821450903) SITUAÇÃO:**

Ao tentar confirmar notas no sistema, é apresentada a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16108775832983) SOLUÇÃO:**

![Imagem 4: Identifique na aba "Endereço" e "Endereço de Entrega" de todos os parceiros envolvidos no lançamento (Parceiro,…](https://ajuda.sankhya.com.br/hc/article_attachments/16108775836439) Identifique na aba **"Endereço"** e **"Endereço de Entrega"** de todos os parceiros envolvidos no lançamento (Parceiro, Transportadora, Empresa) de qual Estado/UF os mesmos são.

![Imagem 5: Identifique na aba "Endereço" e "Endereço de Entrega" de todos os parceiros envolvidos no lançamento (Parceiro,…](https://ajuda.sankhya.com.br/hc/article_attachments/14534386020503)

![Imagem 6: Acesse a tela " Estados " (Caminho de acesso: Configurações » Cadastros » Endereços) , selecione o Estado dos parceiros…](https://ajuda.sankhya.com.br/hc/article_attachments/16108775840279) Acesse a tela **"[Estados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601294-Estados)"** (Caminho de acesso: Configurações » Cadastros » Endereços), selecione o Estado dos parceiros mencionados no item 1 e preencha corretamente o campo **"Código IBGE"'**:

| **CÓD.IBGE** | **UF** |
| --- | --- |
| 12 | AC |
| 27 | AL |
| 16 | AP |
| 13 | AM |
| 29 | BA |
| 23 | CE |
| 53 | DF |
| 32 | ES |
| 52 | GO |
| 21 | MA |
| 51 | MT |
| 50 | MS |
| 31 | MG |
| 15 | PA |
| 25 | PB |
| 41 | PR |
| 26 | PE |
| 22 | PI |
| 33 | RJ |
| 24 | RN |
| 43 | RS |
| 11 | RO |
| 14 | RR |
| 42 | SC |
| 35 | SP |
| 28 | SE |
| 17 | TO |
| 99 | EX |

Fonte: Tabela "Unidades\_da\_Federacao.txt" [[ http://sped.rfb.gov.br/arquivo/show/1949](http://sped.rfb.gov.br/arquivo/show/1949)]

![Imagem 7: Preenchido o campo conforme tabela acima, redigite o cabeçalho da nota e teste a confirmação dos dados.](https://ajuda.sankhya.com.br/hc/article_attachments/16108775844631) Preenchido o campo conforme tabela acima, redigite o cabeçalho da nota e teste a confirmação dos dados.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16108821477271) CAUSA:**

Mensagem apresentada ao realizar lançamentos com parceiros que não possuem o Código IBGE devidamente cadastrado para o seu Estado, no sistema.
