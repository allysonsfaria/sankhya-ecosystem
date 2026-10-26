---
id: "44012753656343"
titulo: "[TMS] - Erro na Importação de XML: ERROR: value too long for type character varying(7)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012753656343--TMS-Erro-na-Importa%C3%A7%C3%A3o-de-XML-ERROR-value-too-long-for-type-character-varying-7"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T19:37:44Z"
rotulos: ["sync_hc", "lincros", "sync_hash_57aa1a89083a", "lincros_13433276"]
---

# [TMS] - Erro na Importação de XML: ERROR: value too long for type character varying(7)

## 1 - Problema Relatado pelo Cliente:

O cliente reportou erro na importação de arquivos XML de notas fiscais no portal. Mesmo após excluir o número do pedido, o erro persiste. A mensagem de erro apresentada é: "**ERROR: value too long for type character varying(7)**", impedindo a importação dos documentos fiscais.

**2 - Passo a Passo para Resolver o Problema:**

1. **Identificar o erro na importação do XML:**

   - Verifique a mensagem de erro gerada no portal ao tentar importar o XML.
   - Caso a mensagem seja "**ERROR: value too long for type character varying(7)**", significa que um campo no XML excede o limite de caracteres permitidos. Neste caso o valor permitido é **7.**
2. **Localizar o campo com erro:**

   - No caso específico identificado, foi analisado e o erro ocorre no campo "Placa do Veículo" do XML, que é permitido apenas 7 caracteres.
   - Esse dado está sendo extraído dos "Dados Adicionais" da nota fiscal.
   - ![Imagem 1: A placa deve conter, no máximo, 7 caracteres exemplo: ABC1D23. Mas nos XMLs fornecidos, o valor ultrapassa esse limite.](https://ajuda.sankhya.com.br/hc/article_attachments/44012732242583)

     A placa deve conter, no máximo, 7 caracteres exemplo: ABC1D23. Mas nos XMLs fornecidos, o valor ultrapassa esse limite.

     ![Imagem 2: A placa deve conter, no máximo, 7 caracteres exemplo: ABC1D23. Mas nos XMLs fornecidos, o valor ultrapassa esse limite.](https://ajuda.sankhya.com.br/hc/article_attachments/44012763066135)
3. **Corrigir o campo no XML:**

   - Entrar em contato com o emissor do documento fiscal e pedir a alteração / troca do XML.
4. **Reimportar o XML no portal:**

   - Após corrigir o campo de placa no XML, tente realizar a importação novamente.
   - Caso o problema persista, verifique se há outros campos que podem estar ultrapassando limites de caracteres.
   - Se necessário, entre em contato com o suporte técnico para uma análise mais detalhada.
