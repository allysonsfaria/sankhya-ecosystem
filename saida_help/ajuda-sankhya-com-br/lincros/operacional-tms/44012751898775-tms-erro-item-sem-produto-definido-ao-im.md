---
id: "44012751898775"
titulo: "[TMS] - Erro \"Item sem produto definido\" ao importar EDI de Ocorrência"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012751898775--TMS-Erro-Item-sem-produto-definido-ao-importar-EDI-de-Ocorr%C3%AAncia"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T19:38:09Z"
rotulos: ["sync_hc", "lincros", "lincros_13433259", "sync_hash_820c328b30b6"]
---

# [TMS] - Erro "Item sem produto definido" ao importar EDI de Ocorrência

**1 - Problema Relatado pelo Cliente:**
Ao receber arquivos EDI de ocorrências via e-mail, é exibida a seguinte mensagem de erro no sistema: **"Foi adicionado um item sem produto definido"**. Com isso, o EDI fica parado e não consegue ser vinculado à nota fiscal, impedindo o processamento da informação.

![Imagem 1: 1 - Problema Relatado pelo Cliente: Ao receber arquivos EDI de ocorrências via e-mail, é exibida a seguinte mensagem de…](https://ajuda.sankhya.com.br/hc/article_attachments/44012734665239)

## 2 - Passo a Passo para Resolver o Problema:

1. ## Entenda a origem do erro:

   - O erro ocorre porque o sistema está tentando importar um item da nota fiscal que não possui produto definido.
2. ## Verifique os parâmetros de configuração da empresa:

   - Acesse a tela de **Parâmetros da Empresa** (Cadastros gerais > Configurações da empresa > Parâmetros > Empresa) no sistema para verificar se o parâmetro que resolve o problema está ativo.
   - O parâmetro `importarItemNF` **deve estar configurado como `true`**.
   - Caso não esteja, entre em contato com o suporte Lincros para fazer a devida parametrização.
3. ## Teste novamente a importação:

   - Após ajustado os parâmetros, tente importar novamente o arquivo EDI com ocorrência.
   - Para importar, navegue por Operacional > Importação > EDI > Importação
   - Clique em "Adicionar" onde irá abrir uma tela para escolher o arquivo EDI. Salve e aguarde carregar.
   - Verifique se o erro persiste e se o EDI consegue ser vinculado corretamente à nota fiscal.
4. ## Se o problema persistir:

   - Certifique-se de que o conteúdo do arquivo EDI está correto e que as notas fiscais possuem itens válidos.
   - Caso necessário, entre em contato com o suporte técnico para uma verificação mais detalhada.
