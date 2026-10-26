---
id: "44010120200087"
titulo: "[TMS] - Problema na Cálculo de Prazos de Entrega para Notas Fiscais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010120200087--TMS-Problema-na-C%C3%A1lculo-de-Prazos-de-Entrega-para-Notas-Fiscais"
trilha: "Lincros > TMS > Entregas e Ocorrências - TMS"
atualizado_em: "2026-10-05T18:30:12Z"
rotulos: ["sync_hc", "lincros", "lincros_13432863", "sync_hash_8b155b3cf2d2"]
---

# [TMS] - Problema na Cálculo de Prazos de Entrega para Notas Fiscais

## 1 - Problema Relatado pelo Cliente

O cliente relatou que o sistema não está calculando os prazos de entrega das notas fiscais apesar de já constarem com o embarque e a tabela cadastrada. O cliente solicita que seja verificado o motivo desse erro e como solucioná-lo.

## 2 - Passo a Passo para Resolver o Problema

1. **Verificar o Embarque e o Pré-Conhecimento:**

   - Acesse o registro de embarque das notas fiscais em: Operacional>Cargas>Pré-conhecimentos, acesse o pré-conhecimento desejado e verifique se há um embarque no mesmo:

     - ![Imagem 1: Verifique se as informações de embarque, incluindo o destino, estão corretas e consistentes com o pré-conhecimento…](https://ajuda.sankhya.com.br/hc/article_attachments/44010098552343)

       Verifique se as informações de embarque, incluindo o destino, estão corretas e consistentes com o pré-conhecimento associado.

1. **Identificar a Divergência de Destino:**

   - Compare o destino registrado no embarque com o destino do pré-conhecimento.
   - Caso o destino no embarque seja diferente do destino no pré-conhecimento, isso pode estar impedindo o cálculo correto do prazo de entrega.
2. **Criar o Prazo para o Novo Destino:**

   - Se o destino do embarque for diferente e não houver um prazo de entrega cadastrado para esse destino específico, acesse o menu de cadastros de prazos de entrega.
   - Crie ou atualize o prazo de entrega para o destino correto.
3. **Recalcular o Embarque:**

   - Após a criação ou atualização do prazo de entrega, recalcule o embarque para garantir que o sistema agora considere o novo prazo e calcule corretamente os prazos das notas fiscais.
   - Operacional>Cargas>Embarques, procure pelo embarque desejado e clique em recalcular:

     ![Imagem 2: Operacional>Cargas>Embarques, procure pelo embarque desejado e clique em recalcular:](https://ajuda.sankhya.com.br/hc/article_attachments/44010129514135)
4. **Verificar se o Cálculo foi Corrigido:**

   - Após o recálculo, verifique se o sistema agora apresenta o prazo de entrega corretamente para as notas fiscais.

## 3 - Prazo alterado na tabela: notas já geradas e recálculo em lote

Ao alterar o prazo de entrega no cadastro da transportadora (por exemplo, de 1 para 2 dias para um destino), o sistema **não recalcula automaticamente** as notas e pré-conhecimentos que já haviam sido gerados. Eles mantêm a previsão calculada com o prazo anterior e, por isso, notas entregues dentro do novo prazo podem continuar aparecendo como atrasadas até que a previsão seja recalculada.

Para atualizar a previsão de várias notas de uma só vez, sem abrir documento por documento:

1. Acesse Operacional > Cargas > Pré-conhecimentos;
2. Filtre as notas fiscais do destino alterado (ou pelo período em que foram geradas);
3. Selecione os registros desejados;
4. Clique em **Recalcular**.

O sistema aplica o prazo atualizado da tabela do transportador aos registros selecionados. Alternativamente, o recálculo pode ser feito por embarque (Operacional > Cargas > Embarques > Recalcular) ou documento a documento.

**Importante:** não existe um recálculo geral que atualize todas as notas do sistema ao mesmo tempo; o recálculo é feito sobre a seleção realizada (pré-conhecimentos filtrados/selecionados, embarque ou documento).

Para mais detalhes sobre o recálculo de vários pré-conhecimentos, consulte o artigo [[TMS] - Como recalcular vários pré-conhecimentos de uma única vez](https://suporte.lincros.com/pt-BR/articles/13433318-tms-como-recalcular-varios-pre-conhecimentos-de-uma-unica-vez).
