---
id: "360042865174"
titulo: "Todas as NF-e's emitidas estão gerando a tag <xMun> como se o parceiro fosse do exterior."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042865174-Todas-as-NF-e-s-emitidas-est%C3%A3o-gerando-a-tag-xMun-como-se-o-parceiro-fosse-do-exterior"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:05:51Z"
rotulos: ["DUVIDANF", "Configuração", "Fiscal", "Parceiro", "NF-e", "XML", "Preferências", "Ajuste \"CODPAISBRASIL\" para 55", "Corrigir município na nota fiscal", "Reemitir ou criar nova nota"]
---

# Todas as NF-e's emitidas estão gerando a tag <xMun> como se o parceiro fosse do exterior.

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16453302880151) SOLUÇÃO:**

Para correção deste erro, seguir os passos abaixo:

![Imagem 2: Acesse: " Preferências " (Caminho de acesso: Configurações » Avançado » Preferências )](https://ajuda.sankhya.com.br/hc/article_attachments/16453334521751) Acesse: "**[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)"**  (Caminho de acesso: Configurações » Avançado » Preferências)

Parâmetro: "**CODPAISBRASIL"** - Código do País Brasil

Alterar para : **55** , salvar.

**(2)** Exemplo **Antes** do ajuste:

<xBairro>VILA NOVA CONCEICAO</xBairro>
<cMun>3550308</cMun>
**<xMun>EXTERIOR</xMun>**
<UF>SP</UF>

**(2)** Exemplo **Depois** do Ajuste:

<xBairro>VILA NOVA CONCEICAO</xBairro>
<cMun>3550308</cMun>
**<xMun>São Paulo</xMun>**
<UF>SP</UF>

![Imagem 3: Acessar novamente a emissão da Nota, faturar novamente ou criar nova Nota e Gerar Lote.](https://ajuda.sankhya.com.br/hc/article_attachments/16453334529943) Acessar novamente a emissão da Nota, faturar novamente ou criar nova Nota e Gerar Lote.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16453302892183) CAUSA:**

Definição incorreta no parâmetro "**CODPAISBRASIL"**.
