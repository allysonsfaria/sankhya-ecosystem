---
id: "39376217235735"
titulo: "Como Remover a Validação de Estoque Empenhado em TOPs de Transferência"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39376217235735-Como-Remover-a-Valida%C3%A7%C3%A3o-de-Estoque-Empenhado-em-TOPs-de-Transfer%C3%AAncia"
trilha: "Melhores Práticas > Compras e Estoque"
atualizado_em: "2026-09-21T17:50:55Z"
rotulos: ["Configuração", "Agendamento", "TOP", "Estoque", "Transferência", "Artigo criado KCS", "CVE - KCS"]
---

# Como Remover a Validação de Estoque Empenhado em TOPs de Transferência

Ao realizar **"transferências entre empresas"**, o sistema considera o **"estoque empenhado"** por padrão, exigindo que os pedidos sejam marcados manualmente como **"Não pendente"**. Este processo gera retrabalho e pode ocasionar erros operacionais. Este artigo apresenta as alternativas disponíveis para otimizar esse processo.

### Entendendo a Validação de Estoque Empenhado

Quando uma **"TOP"** (Tipo de Operação) do tipo **"Transferência"** é utilizada, o sistema valida o estoque empenhado antes de permitir a movimentação. Isso significa que produtos com pedidos pendentes não podem ser transferidos automaticamente, exigindo intervenção manual para marcar cada pedido como não pendente.

### Solução para TOPs de Transferência

Para **"TOPs"** configuradas como **"Transferência"**, é possível habilitar a opção que considera o **"estoque real"** ao invés do estoque empenhado:

**(1)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

**(2)** Localize e abra a **"TOP"** de transferência que deseja configurar.

**(3)** Acesse a aba **"Estoque"**.

**(4)** Habilite a opção **"Considerar estoque real na baixa de estoque"**. Caso essa opção não esteja visível na aba Estoque, localize-a na Configuração da Tela, e inclua-o para que fique visível e possa efetuar a configuração desejada.

**(5)** Salve as alterações realizadas.

Com essa configuração ativada, o sistema não considerará o **"estoque empenhado"** durante o processo de transferência, utilizando apenas o estoque real disponível.

Exemplo:

 Imagine que um produto tem 10 unidades em **"Estoque"** (físico), mas o campo **"Disponível"** está em -5 (porque já foi vendido, mas ainda não saiu do estoque). Se a **TOP de Transferência** que você usar tiver a opção **"Considerar estoque real na baixa de estoque"** marcada, você conseguirá transferir até 10 unidades.

### Limitação para TOPs de Compra/Venda

Caso a operação de transferência seja realizada utilizando **"TOPs"** do tipo Compra/Venda, a configuração mencionada acima **não se aplica**. Esse tipo de movimento não permite a ativação da opção de considerar estoque real na baixa.

### Recomendações Importantes

Antes de implementar qualquer alteração, considere os seguintes pontos:

- **Avalie o impacto** da remoção da validação de estoque empenhado nos processos de controle de estoque da empresa.
- **Verifique se a "TOP"** utilizada é realmente do tipo Transferência
- **Teste a configuração** em ambiente de homologação antes de aplicar em Produção.
- **Documente as alterações** realizadas para facilitar futuras manutenções e auditorias.

Ao seguir estas orientações, o processo de Transferência entre empresas será mais ágil e eficiente, eliminando a necessidade de marcações manuais e reduzindo significativamente o tempo operacional.
