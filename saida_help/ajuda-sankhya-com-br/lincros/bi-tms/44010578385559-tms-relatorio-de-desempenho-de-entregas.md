---
id: "44010578385559"
titulo: "[TMS] Relatório de Desempenho de Entregas: como funciona e por que os números podem divergir da transportadora"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010578385559--TMS-Relat%C3%B3rio-de-Desempenho-de-Entregas-como-funciona-e-por-que-os-n%C3%BAmeros-podem-divergir-da-transportadora"
trilha: "Lincros > TMS > BI - TMS"
atualizado_em: "2026-10-05T18:40:54Z"
rotulos: ["sync_hc", "lincros", "sync_hash_ada615c5f168", "lincros_15986458"]
---

# [TMS] Relatório de Desempenho de Entregas: como funciona e por que os números podem divergir da transportadora

Este artigo explica como o TMS Lincros monta os indicadores de posição e desempenho de entregas, o que significa cada situação exibida (no prazo, sem prazo, em atraso e entregue) e por que, em alguns casos, os números do sistema podem ser diferentes dos que a transportadora informa. O objetivo é ajudar você a interpretar corretamente o relatório e a manter os dados alinhados.

## Como o relatório é montado

O relatório de desempenho de entregas não é um cálculo independente. Ele reflete as informações que já estão registradas na plataforma. Dois dados sustentam todos os indicadores:

- **Previsão de entrega:** a data em que a entrega é esperada. É calculada pelo sistema a partir da data de coleta e da tabela de prazo de entrega cadastrada para a rota (origem, destino e transportadora).
- **Data de entrega realizada:** a data efetiva da entrega. Ela chega ao TMS por meio da ocorrência de entrega, enviada pela transportadora ou lançada na plataforma.

Comparando essas duas datas, o sistema classifica cada documento. Por isso vale uma regra simples: o TMS mostra o que foi informado nele. Ele não deduz uma entrega que não foi registrada, nem um prazo que não foi cadastrado.

## O que cada situação significa

- **No prazo:** a entrega foi realizada dentro da previsão, ou o documento ainda está em trânsito e a previsão não venceu.
- **Em atraso:** a previsão de entrega já venceu e o sistema ainda não recebeu a ocorrência de entrega para aquele documento.
- **Sem prazo:** o documento não tem uma previsão de entrega calculada, então o sistema não consegue classificá-lo como no prazo ou em atraso.

## Por que um documento aparece como "Sem prazo"

"Sem prazo" significa que a previsão de entrega ficou em branco. Isso acontece em três situações comuns:

1. **Não existe tabela de prazo cadastrada** para aquela combinação de transportadora, origem e destino. Sem a tabela, o sistema não tem base para calcular a data.
2. **A tabela de prazo foi cadastrada depois** de o documento já ter sido gerado. Nesse caso, a previsão precisa ser recalculada no documento. Apenas alterar a vigência da tabela não recalcula os documentos antigos: a tabela passa a valer automaticamente para os novos, mas os anteriores precisam do recálculo manual.
3. **O CEP de origem ou de destino está incompleto ou inconsistente**, o que impede o cálculo final da previsão.

**Como corrigir:** cadastre a tabela de prazo para as rotas necessárias e, em seguida, recalcule a previsão de entrega nos documentos afetados. O passo a passo do cadastro está em [Prazo de Entrega (Transportadora)](https://suporte.lincros.com/pt-BR/articles/13432718-tms-prazo-de-entrega-transportadora) e em [Previsão de entrega a partir da ordem de coleta](https://suporte.lincros.com/pt-BR/articles/13433369-tms-previsao-de-entrega-a-partir-da-ordem-de-coleta).

[screenshot: menu de cadastro de prazo de entrega]

## Por que um documento aparece "Em atraso" mesmo com a entrega já realizada

Quando a transportadora já entregou, mas o documento continua em atraso ou em trânsito no TMS, quase sempre a causa é a mesma: a ocorrência de entrega ainda não chegou ao sistema. A situação do documento só muda para entregue quando essa ocorrência é registrada.

Um detalhe do TMS ajuda a entender isso. Um pré-conhecimento pode agrupar várias notas fiscais. Ele só é considerado entregue quando **todas** as notas fiscais dele receberam a ocorrência de entrega. Se cinco de seis notas foram baixadas e uma ainda não, o pré-conhecimento inteiro permanece em trânsito. Isso ocorre porque a ocorrência é registrada por nota fiscal, e não por pré-conhecimento. A transportadora baixa a nota fiscal, e o pré-conhecimento é um agrupamento interno do TMS.

A ocorrência de entrega pode chegar ao TMS de algumas formas:

- Integração EDI com a transportadora.
- Integração via SSW, para transportadoras sem EDI.
- Portal da transportadora.
- Lançamento manual da ocorrência na própria plataforma, quando nenhuma das opções acima está disponível.

## Por que os números podem divergir do que a transportadora informa

É comum a transportadora apresentar, na planilha dela, um índice de desempenho diferente do que aparece no TMS. Por exemplo, a transportadora informa 98% de entregas no prazo e o sistema mostra um número bem menor. Isso não indica um erro da plataforma.

A explicação é direta. A transportadora enxerga o que aconteceu na ponta, na operação física. O TMS enxerga apenas o que foi registrado nele. Se as ocorrências de entrega não foram enviadas ao sistema, ou se os prazos não foram cadastrados, o TMS não tem como chegar ao mesmo número da transportadora.

Vale a analogia: o relatório expõe o processo, ele não cria a informação. Se uma etapa não foi concluída na origem, seja o cadastro do prazo ou o envio da ocorrência de entrega, nenhum relatório vai exibir essa etapa como concluída. Por isso, quando há divergência, o caminho é verificar o que ficou pendente de cadastro ou de envio, e não interpretar o resultado como falha do sistema.

## Como alinhar os números

1. Confirme se existe tabela de prazo cadastrada para todas as combinações de transportadora, origem e destino que você utiliza.
2. Recalcule a previsão de entrega nos documentos que foram gerados antes do cadastro ou do ajuste da tabela.
3. Garanta que a transportadora está enviando as ocorrências de entrega, por EDI, SSW ou portal. Quando não houver integração, registre a ocorrência manualmente na plataforma.
4. Abra novamente o relatório e valide os indicadores. Os documentos com prazo cadastrado e ocorrência recebida passarão a refletir a situação correta.

## Dúvidas frequentes

**Alterei a vigência da tabela de prazo e os documentos antigos continuam sem prazo. Por quê?**
A alteração de vigência não recalcula automaticamente os documentos que já existiam. Ela passa a valer para os novos. Para os anteriores, é preciso recalcular a previsão de entrega documento a documento.

**A transportadora confirma a entrega, mas o documento segue em trânsito. O que fazer?**
Verifique se a ocorrência de entrega chegou ao TMS. Se a transportadora tem integração, confirme o envio do arquivo. Se não tem, registre a ocorrência manualmente. Lembre também que, se o pré-conhecimento tem várias notas fiscais, todas precisam da ocorrência para o documento ser considerado entregue.

**Isso é um erro do sistema?**
Não. O relatório reflete os dados registrados na plataforma. Quando falta o cadastro do prazo ou o envio da ocorrência de entrega, o indicador aparece como sem prazo ou em atraso. Depois de completar essas informações, os números se ajustam.

---
