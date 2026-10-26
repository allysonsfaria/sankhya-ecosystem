---
id: "44010145694615"
titulo: "[TMS] - Como atualizar o prazo de entrega quando o pré-conhecimento tem Cotação Spot confirmada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010145694615--TMS-Como-atualizar-o-prazo-de-entrega-quando-o-pr%C3%A9-conhecimento-tem-Cota%C3%A7%C3%A3o-Spot-confirmada"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T18:31:04Z"
rotulos: ["sync_hc", "lincros", "sync_hash_fc5f25a876ff", "lincros_17153884"]
---

# [TMS] - Como atualizar o prazo de entrega quando o pré-conhecimento tem Cotação Spot confirmada

**Menu**: Entregas e Ocorrências > Acompanhamento de entregas

**Objetivo**: Como ajustar o prazo de entrega de uma nota fiscal quando o pré-conhecimento vinculado possui uma Cotação Spot já confirmada.

## Por que a edição trava

Quando a nota fiscal possui uma cotação spot no status **Confirmada**, o sistema trava a edição de campos do pré-conhecimento, incluindo o prazo de entrega. Isso acontece porque a cotação foi criada com um valor de frete informado manualmente e, por segurança, o registro vinculado não pode ser modificado depois de confirmado — a edição só é permitida enquanto a cotação está com status **Aberta**.

Cancelar ou reabrir a cotação spot para contornar essa trava não é recomendado: isso impacta o recálculo do valor do frete já acordado com a transportadora.

## Caminho correto: lançar uma ocorrência de "Entrega Programada"

Em vez de editar o pré-conhecimento ou a cotação diretamente, ajuste o prazo de entrega lançando uma ocorrência:

1. Acesse **Entregas e Ocorrências > Acompanhamento de entregas**;
2. Localize a nota fiscal (é possível filtrar pelo número da NF);
3. Clique para expandir o registro e, na seção "Detalhes", use o botão **"Lançar ocorrências"**;
4. Registre uma ocorrência do tipo **"Entrega Programada"**, informando o novo prazo de entrega desejado.

Esse lançamento atualiza a previsão de entrega sem alterar o valor do frete nem mexer na cotação Spot vinculada.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
