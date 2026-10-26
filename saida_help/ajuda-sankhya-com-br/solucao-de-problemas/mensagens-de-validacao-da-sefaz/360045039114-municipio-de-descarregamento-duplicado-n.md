---
id: "360045039114"
titulo: "Município de descarregamento duplicado no mdf-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045039114-Munic%C3%ADpio-de-descarregamento-duplicado-no-mdf-e"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T15:33:19Z"
rotulos: ["ERROMDFE", "MDF-e", "Parceiro", "Cidades", "SEFAZ", "680", "Rejeição 680: Município de Descarregamento Duplicado", "Erro"]
---

# Município de descarregamento duplicado no mdf-e

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16454948683415) MENSAGEM:**

[680 - Rejeição]: Município de descarregamento duplicado no mdf-e.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16454948685591) SOLUÇÃO:**

Em nosso sistema, os grupos de município de descarga serão formados conforme 'Código IBGE' informado para a 'Cidade' dos parceiros destinatários referentes a cada documento.

![Imagem 3: Dessa forma, quando a rejeição mencionada ocorrer, recomenda-se validar o Cód.Cidade inserido na aba 'Endereços' de…](https://ajuda.sankhya.com.br/hc/article_attachments/16454932206871) Dessa forma, quando a rejeição mencionada ocorrer, recomenda-se validar o Cód.Cidade inserido na aba 'Endereços' de cada parceiro. Avaliando principalmente se existem cadastros duplicados para uma mesma cidade, onde existirão códigos IBGE distintos.

Exemplo:

<infDoc>
<infMunDescarga>
<cMunDescarga>**2100873**</cMunDescarga>
<xMunDescarga>**Araguanã**</xMunDescarga>
<infCTe>
<chCTe>56789101112131415161718192021222324252627282</chCTe>
</infCTe>
</infMunDescarga>

<infMunDescarga>
<cMunDescarga>**2188873**</cMunDescarga>
<xMunDescarga>**Araguana**</xMunDescarga>
<infCTe>
<chCTe>56789101112131415161718192021222324252627111</chCTe>
</infCTe>
</infMunDescarga>
</infDoc>

Note que para o Município 'Araguanã' existem dois cadastros, com 'Mun.domicílio fiscal' distintos.

![Imagem 4: Realize os devidos ajustes, referenciando a cidade correta através da tela 'Parceiros', aba endereços. Após ajustes,…](https://ajuda.sankhya.com.br/hc/article_attachments/16454932209431) Realize os devidos ajustes, referenciando a cidade correta através da tela 'Parceiros', aba endereços.
Após ajustes, gere um novo lote do respectivo MDF-e;

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16454948691223) CAUSA:**

Quando for emitido um MDF-e e no grupo de documentos existirem dois ou mais grupos de Municípios de Descarga que referencie o mesmo município, será retornado a rejeição.
