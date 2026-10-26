---
id: "44013421491223"
titulo: "[TMS] - Erro na Importação de Região: Espaços Extras nos CNPJs"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013421491223--TMS-Erro-na-Importa%C3%A7%C3%A3o-de-Regi%C3%A3o-Espa%C3%A7os-Extras-nos-CNPJs"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:57:51Z"
rotulos: ["sync_hc", "lincros", "lincros_13432447", "sync_hash_251bad2279ca"]
---

# [TMS] - Erro na Importação de Região: Espaços Extras nos CNPJs

**1 - Problema Relatado pelo Cliente:**
O cliente relatou erro ao tentar importar a região da transportadora no sistema. A importação não foi concluída corretamente, e o cliente solicitou orientação para resolver o problema.

## 2 - Passo a Passo para Resolver o Problema:

1. ## Importe o arquivo e identifique o erro:

   - Realize a importação de arquivo Excel. Cadastros gerais > Transportadoras > Negociações > Regiões.
   - Clique em "Importar". Em seguida, uma nova aba será aberta, onde você deverá clicar em "Adicionar" para selecionar seu arquivo, e, posteriormente, em "Upload".
   - ![Imagem 1: Clique em "Importar". Em seguida, uma nova aba será aberta, onde você deverá clicar em "Adicionar" para selecionar seu…](https://ajuda.sankhya.com.br/hc/article_attachments/44013435028759)
   - Uma mensagem em verde será exibida, informando que você deve acompanhar o status da importação.
   - ![Imagem 2: Uma mensagem em verde será exibida, informando que você deve acompanhar o status da importação.](https://ajuda.sankhya.com.br/hc/article_attachments/44013460452887)
   - Selecione o Log da importação e acesse a aba "**Erros**", onde irá mostrar os erros da importação.
   - ![Imagem 3: Selecione o Log da importação e acesse a aba " Erros ", onde irá mostrar os erros da importação.](https://ajuda.sankhya.com.br/hc/article_attachments/44013435291287)
   - Observado o erro, você deve acessar o arquivo anexado, verifique se há inconsistências nos CNPJs, como espaços extras, caracteres inválidos ou dígitos adicionais.
2. ## Corrigir os dados da planilha:

   - No caso identificado, o erro foi causado por espaços extras no final dos CNPJs, exemplo: '00000000000000 '.
   - Para corrigir, selecione a coluna de CNPJs na planilha.
   - Utilize a função de remoção de espaços do editor de planilhas ou remova manualmente os espaços extras.
3. ## Salvar e tentar a importação novamente:

   - Após corrigir os dados, salve a planilha no formato adequado.
   - Tente importar a planilha novamente no sistema, seguindo os passos informados anteriormente.
4. ## Validar a importação:

   - Caso o erro persista, verifique se há outros campos com problemas semelhantes.
   - Se necessário, entre em contato com o suporte técnico para análise mais detalhada.
