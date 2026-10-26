---
id: "360044085733"
titulo: "Parcela calculada pela fórmula não pode ter seu valor alterado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044085733-Parcela-calculada-pela-f%C3%B3rmula-n%C3%A3o-pode-ter-seu-valor-alterado"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-09-21T20:01:30Z"
rotulos: ["#PUBLIFER", "#revisadohugo", "CORE_E02785", "Configuração", "Fórmulas", "Movimentação Financeira", "Tipo de Negociação", "Financeiro", "Fórmula de Parcelas", "Erro"]
---

# Parcela calculada pela fórmula não pode ter seu valor alterado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16105902810135) MENSAGEM:**

[CORE\_E02785] Parcela calculada pela fórmula não pode ter seu valor alterado.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16105917709207) SOLUÇÃO:**

![Imagem 3: Verifique se o tipo de negociação utilizado possui fórmula vinculada:](https://ajuda.sankhya.com.br/hc/article_attachments/16105902816535) Verifique se o tipo de negociação utilizado possui fórmula vinculada:

Tela **"[Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o)**" (Caminho de acesso: Comercial » Arquivo » Cadastros), aba **"Parcelas"**, campo **"Fórmula"**.

![Imagem 4: Tela " Tipos de Negociação " (Caminho de acesso: Comercial » Arquivo » Cadastros) , aba "Parcelas" , campo "Fórmula" .](https://ajuda.sankhya.com.br/hc/article_attachments/14505980142615)

![Imagem 5: Para a situação reportada no item 1, não serão permitidas alterações no respectivo financeiro que façam com que as…](https://ajuda.sankhya.com.br/hc/article_attachments/16105902820247) Para a situação reportada no item 1, não serão permitidas alterações no respectivo financeiro que façam com que as parcelas não atendam aos requisitos da fórmula.

(1)** Importante:**

Caso essa situação ocorra na rotina **"[Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML)"** atente-se a opção **"Usar financeiro"** da aba **"Financeiro"**. Para tipo de negociação com fórmula, essa opção deverá ser igual **Usar financeiro do sistema**.

![Imagem 6: Caso essa situação ocorra na rotina " Portal de Importação de XML " atente-se a opção "Usar financeiro" da aba…](https://ajuda.sankhya.com.br/hc/article_attachments/14505981259031)

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16105917716759) CAUSA:**

Mensagem apresentada ao realizar alterações em financeiros que são gerados por fórmulas e tais alterações não atendem aos requisitos da respectiva fórmula.
