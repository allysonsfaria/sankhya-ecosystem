---
id: "43675418901271"
titulo: "Reajuste Salarial Retroativo - Impossível gravar data de alteração posterior à competência de efeito com folha calculada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43675418901271-Reajuste-Salarial-Retroativo-Imposs%C3%ADvel-gravar-data-de-altera%C3%A7%C3%A3o-posterior-%C3%A0-compet%C3%AAncia-de-efeito-com-folha-calculada"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-09-29T14:33:44Z"
rotulos: ["Artigo criado KCS", "Sankhya RH - KCS"]
---

# Reajuste Salarial Retroativo - Impossível gravar data de alteração posterior à competência de efeito com folha calculada

**MENSAGEM**

Impossível gravar data de alteração posterior à competência de efeito com folha calculada.

**SITUAÇÃO**

Ao tentar lançar um reajuste salarial retroativo, por exemplo, com vigência em 01/10, o sistema impede o salvamento da alteração salarial quando já existe folha calculada para a competência de efeito ou para competências posteriores. Isso ocorre, por exemplo, quando a folha do mês seguinte já foi processada, mas o reajuste precisa ser aplicado com data-base anterior, devido à assinatura tardia da convenção coletiva.

**SOLUÇÃO**

Para realizar o reajuste salarial retroativo quando já existe folha calculada para a competência de efeito ou posteriores, siga o passo a passo abaixo:

**(1)** Acesse a tela **"Folha de Pagamento"** Pessoal+ » Rotinas Folha » Gerenciador de Folhas

**(2)** Exclua as folhas já calculadas para as competências a partir da data de vigência do reajuste.

**(3)** Realize o lançamento do reajuste salarial retroativo na tela **"Reajuste Salarial"** Pessoal+ » Rotinas Folha » Reajuste Salarial, informando a data-base correta.

**(4)** Recalcule as folhas das competências excluídas, garantindo que o novo salário seja considerado desde a data-base.

**(5)** Caso não seja possível excluir as folhas, por fechamento contábil ou outros motivos, realize o reajuste na competência atual e utilize um evento de movimento para lançar a diferença salarial retroativa manualmente na folha complementar (folha de dissídio).

**(6)** Após o ajuste, gere e envie novamente o evento **"S-2206"** ao eSocial, certificando-se de que a data de vigência informada seja a correta.

**Observação:** Para colaboradores admitidos no mês da data-base, verifique se o sistema está considerando corretamente o cálculo das diferenças na folha complementar. Caso necessário, ajuste manualmente os valores para garantir o correto pagamento das diferenças salariais.

##

⚠️ **Atenção ao eSocial:** Se a alteração for relacionada a dados que devem ser enviados ao eSocial (como alteração salarial que gera evento S-2206), certifique-se de que:

- A data de efeito seja **posterior à data de virada do eSocial** cadastrada na empresa
- Após registrar a alteração, acesse a **Central de Eventos do eSocial** (Pessoal+ » Rotinas Folha » Central do eSocial) para gerar e enviar os eventos correspondentes

⚠️ **Impacto Financeiro:** Ao excluir uma folha já calculada, verifique se não há pagamentos ou obrigações já processadas que possam ser afetadas pela exclusão.

⚠️ **Rescisões:** Este mesmo comportamento se aplica ao cálculo de rescisões. Se você tentar calcular uma rescisão em uma competência que já possui folha mensal calculada, será necessário excluir a folha mensal primeiro.

**CAUSA**

O sistema bloqueia o lançamento de alterações salariais retroativas quando já existem folhas calculadas para a competência de efeito ou posteriores, para evitar inconsistências nos cálculos e divergências de informações enviadas ao eSocial. Isso garante que o histórico salarial e os eventos enviados estejam alinhados com a folha processada, evitando retrabalho e possíveis advertências no eSocial.
