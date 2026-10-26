---
id: "4420402670359"
titulo: "Este cadastro se refere a uma devolução de emissão própria, mas o campo \"Buscar NF de origem p/ referenciar na NFe\" está desmarcado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4420402670359-Este-cadastro-se-refere-a-uma-devolu%C3%A7%C3%A3o-de-emiss%C3%A3o-pr%C3%B3pria-mas-o-campo-Buscar-NF-de-origem-p-referenciar-na-NFe-est%C3%A1-desmarcado"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T15:19:38Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "TOP", "#CausaRaiz", "CORE_E06108", "CORE_E06107", "Devolução de Emissão Própria", "Referência de NF-e", "Configuração de TOP", "devolução SEFAZ validação", "Erro", "Documentos Eletrônicos"]
---

# Este cadastro se refere a uma devolução de emissão própria, mas o campo "Buscar NF de origem p/ referenciar na NFe" está desmarcado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16283452331415) MENSAGEM:**

[CORE\_E06107] Este cadastro se refere a uma devolução de emissão própria. mas o campo "Buscar NF de origem p1 referenciar na NFe" está desmarcado. Se este campo ficar desmarcado, pode haver rejeição da nota, pois a SEFAZ exige esta informação

[CORE\_E06108] Este cadastro se refere a uma devolução de emissão própria, mas o campo "Buscar NF de origem p/ referenciar na NFe" está desmarcado. Se este campo ficar desmarcado, pode haver rejeição da nota, pois a SEFAZ exige esta informação.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16283452359447) CAUSA:**

Se todas as configurações acima forem realizadas e você tentar salvar a TOP de devolução na tela Tipos de Operação - TOP com a marcação Buscar NF-e de origem p/ referenciar na NFe desabilitada, será apresentada a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16283426316823) SOLUÇÃO:**

![Imagem 4: Na tela "Tipos de Operação - TOP" , localize a marcação "Buscar NF de origem p/ referenciar na NFe" e marque essa…](https://ajuda.sankhya.com.br/hc/article_attachments/16283452341271)  Na tela **"Tipos de Operação - TOP"**, localize a marcação **"Buscar NF de origem p/ referenciar na NFe"** e marque essa opção, conforme print abaixo:

![Imagem 5: Na tela "Tipos de Operação - TOP" , localize a marcação "Buscar NF de origem p/ referenciar na NFe" e marque essa…](https://ajuda.sankhya.com.br/hc/article_attachments/16283426326039)

**Observações:**

![Imagem 6: Essa validação ocorre quando o parâmetro "Valida NF de devolução sem documento referenciado - VALNFDEVDOCREF"…](https://ajuda.sankhya.com.br/hc/article_attachments/16283452341271) Essa validação ocorre quando o parâmetro **"Valida NF de devolução sem documento referenciado - VALNFDEVDOCREF"** encontra-se **ligado**;

![Imagem 7: Essa validação ocorre considerando:](https://ajuda.sankhya.com.br/hc/article_attachments/16283452352023) Essa validação ocorre considerando:

**(1)** Sendo esta TOP de Devolução de Compra ou Devolução Venda, a opção **"Normal"** do campo **"NF-e"** deve estar selecionada;

**(1)** Campo **"Modelo de Documento"**, com a opção **"55-Nota Fiscal Eletrônica"**;

Caso surjam exceções, em que seja necessário que essa referência não aconteça, o parâmetro acima sendo **desligado**, a validação deixará de acontecer, não mais exigindo essa marcação no cadastro da TOP.
