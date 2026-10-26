---
id: "360043577734"
titulo: "Produto: XX Diferença na quantidade de bens digitados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043577734-Produto-XX-Diferen%C3%A7a-na-quantidade-de-bens-digitados"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-08-14T14:28:17Z"
rotulos: ["#criadoRoger", "CORE_E01832", "Produtos", "Configuração", "Imobilizado", "Atualização", "TOP", "Estoque", "Erro CORE_E01832", "Produto Imobilizado", "Correção de lançamento"]
---

# Produto: XX Diferença na quantidade de bens digitados

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16108280388759) MENSAGEM**:

[CORE\_E01832] Produto: XX Diferença na quantidade de bens digitados!

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16108284199575) SOLUÇÃO**:

Para correção, siga os passos abaixo:

![Imagem 3: Caso o lançamento seja de um produto Imobilizado, a TOP está configurado para Atualizar BEM , então neste caso deverá…](https://ajuda.sankhya.com.br/hc/article_attachments/16108284200471) Caso o lançamento seja de um produto Imobilizado, a TOP está configurado para  **Atualizar BEM**, então neste caso deverá lançar o código do Bem.

**(2)** Na grade Itens, selecione o item Imobilizado, clique no botão **"[...]Outras Opções"** » **"Bens"** e selecione a opção de acordo com o documento, pesquise pelo bem e selecione.

![Imagem 4: Caso o lançamento não seja de um produto Imobilizado, considere trocar a TOP do lançamento da nota ou ajustar a…](https://ajuda.sankhya.com.br/hc/article_attachments/16108280401303) Caso o lançamento não seja de um produto Imobilizado, considere trocar a TOP do lançamento da nota ou ajustar a configuração da TOP para não Atualizar BEM, acessando:

**(2)** Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

**(2)** Aba: **"Estoque"**,

**(2)**Campo "**Atualização do BEM":** Não Atualizar. Com esta opção marcada, não irá validar o BEM no ato do lançamento do documento. (Marcação histórica, após ajuste, deverá lançar o documento novamente.)

**![Imagem 5: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16108284209943) CAUSA**:

Ocorre quando o documento lançado possui itens do tipo Imobilizado e a TOP está configurado para atualizar bem e o bem não foi vinculado ao produto lançado ou a TOP não deveria atualizar bem e está configurado para atualizar.

Considere alinhar com a equipe interna para verificar o documentado lançado antes de fazer os ajustes informados acima.
