---
id: "360044613214"
titulo: "Mapa de Separação Manual"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613214-Mapa-de-Separa%C3%A7%C3%A3o-Manual"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-07-29T14:14:24Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Impressão", "WMS", "Estoque", "Separação", "Mapa de Separação Manual", "VALESTMAPSEPWMS", "br.com.sankhya.wms.mapaseparacaomanual", "Mapa de Separação Manual manual", "Empresa ordem de carga.", "Validações pendências estoque", "Todos pedidos ou específicos"]
---

# Mapa de Separação Manual

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311560809495) Módulo: WMS > Rotinas 
```

---

Esta rotina possibilitará a Separação Manual dos Produtos enviados ao WMS.

![Imagem 2: Esta rotina possibilitará a Separação Manual dos Produtos enviados ao WMS .](https://ajuda.sankhya.com.br/hc/article_attachments/360085280534)

Para impressão do Mapa de Separação de todos os Pedidos de uma Ordem de Carga, bastará informar a **"Empresa"** e a **"Ordem de Carga"**, deixando vazios os campos **"Área de conferência"** e **"Pedido"**. Ao clicar em **"Gerar Mapa"**, o sistema questionará se você deseja realizar a separação para todos os pedidos ou por ordem de carga:

![Imagem 3: Para impressão do Mapa de Separação de todos os Pedidos de uma Ordem de Carga , bastará informar a "Empresa" e a "Ordem…](https://ajuda.sankhya.com.br/hc/article_attachments/360085280694)

Clicando em **"Todos os pedidos"** o sistema mostrará todas as separações que são por Pedido para aquela Ordem de Carga e, no WMS, todas elas passarão para a situação **''Em processo de separação''**; assim, será necessário visualizar o mapa somente uma vez para obter-se o Mapa de Separação completo desta Ordem de Carga (OC).

Para filtrar o Mapa de Separação daquelas separações que foram geradas sem Área de Conferência (produtos não paletizados), deixe vazio o filtro para Área de Conferência e informe apenas a Empresa e a Ordem de Carga. Ao clicar em Gerar Mapa, o sistema perguntará se você deseja fazer a separação para todos os pedidos ou por ordem de carga e, neste momento, optando por Ordem de Carga, serão apresentadas todas as separações geradas para estas áreas e, no WMS, elas ficarão com o status **''Em processo de separação''**.

Para filtrar o Mapa de Separação por Pedido, informe em Área de Conferência a área para a qual você deseja imprimir o mapa de separação e, deverá informar também a Empresa, a Ordem de Carga e o Número do Pedido (NUMNOTA). Assim, ao clicar em Gerar Mapa, o sistema não apresentará nenhuma mensagem ao final e irá imprimir, automaticamente, o mapa de separação apenas para o Pedido e a Área de Conferência informada. Isto ocorrerá quando você desejar gerar um Mapa de Separação específico.

**Importante:** quando os mapas de separação são visualizados no Sankhya Om, a Expedição passa para o status **"Em Processo de Separação"** e, a partir de então, a Separação só poderá ser concluída pelo Sankhya Om. Contudo, após a conclusão da geração do mapa de separação, a Conferência poderá ser feita tanto manualmente quanto pelo Coletor de Dados.

Consulte documentação completa dos processos de separação e outras rotinas do WMS no Help On line do Módulo MGE WMS ou Manual do WMS disponível na área restrita do site Sankhya.

#### Parâmetros que influenciam nesta rotina

Caso seja necessário concluir a geração do mapa de separação desconsiderando as restrições de um determinado endereço que possua uma tarefa de reabastecimento corretivo pendente, temos o parâmetro **"Valida estoque na geração do mapa de separacao WMS - VALESTMAPSEPWMS"** que, por padrão, é apresentado ativado, o que significa que a validação de alguma pendência nos endereços de origem será mantida, a menos que o parâmetro seja desativado. Em outras palavras, para que a validação de pendência em algum endereço de origem não seja feita, realize a desativação do parâmetro; desativando o mesmo, a mensagem abaixo deixará de ser apresentada:

**"Há uma tarefa do tipo "Armazenagem" para o produto "X" com destino ao endereço "YY". Finalize-a antes de gerar o mapa de separação".**
