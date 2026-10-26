---
id: "44013102009239"
titulo: "[TMS] - Erro de Importação de EDI DOCCOB: Fatura Já Aceita, Conferida ou Paga"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013102009239--TMS-Erro-de-Importa%C3%A7%C3%A3o-de-EDI-DOCCOB-Fatura-J%C3%A1-Aceita-Conferida-ou-Paga"
trilha: "Lincros > TMS > Financeiro - TMS"
atualizado_em: "2026-10-05T19:48:15Z"
rotulos: ["sync_hc", "lincros", "lincros_13432943", "sync_hash_35e7c8d649d2"]
---

# [TMS] - Erro de Importação de EDI DOCCOB: Fatura Já Aceita, Conferida ou Paga

**1 - Problema Relatado pelo Cliente:**
O cliente informou que um arquivo EDI DOCCOB não está sendo importado corretamente pelo sistema. A mensagem de erro apresentada pelo TMS no momento da importação do DOCCOB foi: **"Fatura 'X' já foi aceita, conferida ou paga."**

![Imagem 1: 1 - Problema Relatado pelo Cliente: O cliente informou que um arquivo EDI DOCCOB não está sendo importado corretamente…](https://ajuda.sankhya.com.br/hc/article_attachments/44013110873239)

## 2 - Passo a Passo para Resolver o Problema:

Quando essa mensagem de erro é exibida durante a importação de um DOCCOB, isso indica que o sistema identificou que a fatura informada já existe criada no sistema com o mesmo número e série que constam no DOCCOB, e já passou por alguma das seguintes etapas: **aceitação**, **conferência** ou **pagamento**. Isso impede que ela seja processada novamente.

Veja como analisar e resolver a situação:

1. ## Verifique a fatura no módulo de Faturas do TMS:

   - Acesse o módulo de Faturas. Financeiro > Faturas
   - Localize a fatura com o número informado na mensagem de erro, e se preciso, informe a série ou transportadora para facilitar a busca.
   - Confirme se a situação da fatura está como **Aceita**, **Conferida** ou **Paga**.
   - ![Imagem 2: Confirme se a situação da fatura está como Aceita , Conferida ou Paga .](https://ajuda.sankhya.com.br/hc/article_attachments/44013102421783)
2. ## Valide as informações contidas no arquivo EDI:

   - Abra o arquivo DOCCOB com um editor de texto e valide se na linha 352, posição 18 a 28, o número da fatura informado é o mesmo que o número pesquisado no sistema. E valide se na linha 352, posição 15 a 18, a séria da fatura é a mesma que a séria da fatura pesquisada no sistema.
   - No exemplo abaixo deste caso, o nome do arquivo DOCCOB que deu esse erro de importação era "EDI 23573.TXT" e não coincidia com a fatura mencionada dentro dele, a fatura 23572. Isso pode gerar confusão durante o envio e análise.
3. ## Entenda o cenário com a transportadora:

   - Se a fatura do DOCCOB é a mesma que já existe no sistema com uma das situações mencionadas, é preciso entender o motivo de tentar importar novamente o mesmo DOCCOB.
   - Importante confirmar com a transportadora se de fato é esta fatura que ela queria criar no TMS através do DOCCOB, e se o envio do arquivo está correto ou se houve algum engano no nome ou conteúdo do arquivo.
   - ![Imagem 3: Importante confirmar com a transportadora se de fato é esta fatura que ela queria criar no TMS através do DOCCOB, e se…](https://ajuda.sankhya.com.br/hc/article_attachments/44013102550807)
4. ## Reabra a fatura se realmente for necessário:

   - A transportadora pode querer enviar novamente o DOCCOB da mesma fatura para corrigir/ajustar alguma informação da fatura, como o Valor Faturado, ou informações de Desconto, por exemplo.
   - Para que o DOCCOB possa ser importado novamente, reabra a fatura já existente no TMS, através do botão "Reabrir" na tela de pesquisa de Faturas, ou dentro do registro da fatura.
   - Se o botão Reabrir não estiver aparecendo para você, pode ser que a fatura já tenha sido integrada com o seu ERP, ou que você não tenha permissão configurada para isso. Portanto, é importante seguir com a abertura de um chamado com o Suporte da Lincros para uma análise mais detalhada da situação.
   - Se uma fatura já estiver com o status de "integrada com sucesso" (ícone verde na coluna "integração" da tela de pesquisa de Faturas), é necessário verificar com o seu gestor se é possível estornar/reverter a integração desta fatura para que o botão "Reabrir" reapareça, e para que a fatura fique novamente em um status que permita importar novamente o seu DOCCOB.

**3 - Resumo do Artigo:**
Ao importar um EDI DOCCOB com mensagem de erro informando que a fatura já foi aceita, conferida ou paga, é necessário verificar se a fatura já foi processada no sistema e revisar o conteúdo do DOCCOB para se certificar se realmente se trata da mesma fatura ou se a transportadora se enganou ao gerar o DOCCOB repetindo o número e série de uma fatura já existente. Se realmente for necessário, basta reabrir a fatura (caso não esteja com o status de "paga")
