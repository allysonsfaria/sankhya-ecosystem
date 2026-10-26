---
id: "44012749496599"
titulo: "[TMS] - Nota fiscal com Transportadora Incorreta"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012749496599--TMS-Nota-fiscal-com-Transportadora-Incorreta"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T19:37:47Z"
rotulos: ["sync_hc", "lincros", "lincros_13433273", "sync_hash_949eab3ba3ef"]
---

# [TMS] - Nota fiscal com Transportadora Incorreta

## 1 - Problema Relatado pelo Cliente

O cliente relatou que a nota fiscal foi enviada pela transportadora 'Padrão01', mesmo essa não atendendo a cidade de Porto Alegre/RS. O cliente solicitou uma verificação sobre o motivo dessa escolha, pois a transportadora não deveria ser selecionada para esse destino visto que, essa transportadora não atende esse destino.

## 2 - Passo a Passo para Resolver o Problema

1. **Verificar os Detalhes da Nota Fiscal:**

   - Acesse a nota fiscal no sistema em: Documentos Eeletronicos>NF-es
   - Verifique as informações de destino registradas na pré-nota fiscal associada a essa nota.
2. **Identificar o Destino Registrado na Pré-Nota Fiscal:**

   - Confirme se o destino registrado na pré-nota fiscal, é de fato é o destino da nota fiscal.

     - Caso o destino esteja incorreto/divergente da nota, esse é o motivo pelo qual a transportadora foi selecionada.
3. **Analisar a Seleção da Transportadora:**

   - Verifique qual transportadora foi selecionada para o envio da nota fiscal e quais rotas estavam disponíveis no momento da escolha.
   - Assim, podemos identificar que a transportadora selecionada, de fato atendia a rota que havia sido inserida na pré-nota porém, houve uma alteração na nota fiscal onde foi alterado o destino/rota, e agora, a transportadora que antes havia sido selecionada na pré-nota não atende a essa nova rota inserida na nota fiscal.
4. **Corrigir o Destino na Pré-Nota Fiscal:**

   - Caso o destino esteja incorreto, corrija o campo de destino para o destino correto em: Operacional>Documentos de Despacho>Pré-notas fiscais, acesse a pré-nota desejada e altere o campo de destino:

     ![Imagem 1: Caso o destino esteja incorreto, corrija o campo de destino para o destino correto em: Operacional>Documentos de…](https://ajuda.sankhya.com.br/hc/article_attachments/44012754241687)
5. **Recalcular a Nota Fiscal:**

   - Após a correção, recalcule o valor do frete da nota fiscal com as informações atualizadas.
   - Certifique-se de que a transportadora correta seja selecionada para o envio de acordo com o novo destino.
6. **Verificar se o Problema foi Resolvido:**

   - Verifique se o erro foi corrigido, e se a transportadora correta foi selecionada para o destino correto.
