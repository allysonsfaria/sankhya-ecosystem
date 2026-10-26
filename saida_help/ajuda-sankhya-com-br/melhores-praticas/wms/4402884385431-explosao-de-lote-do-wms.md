---
id: "4402884385431"
titulo: "Explosão de lote do WMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4402884385431-Explos%C3%A3o-de-lote-do-WMS"
trilha: "Melhores Práticas > WMS"
atualizado_em: "2026-07-22T15:24:11Z"
rotulos: ["Configuração", "WMS", "Lote", "Estoque", "Preferências", "#validadoRonald", "Explosão de lote: Busca mercadoria validade", "Parâmetros: \"LOTAUTCENT\" \"LOTEDTVAL\"", "Separação: Configurações WMS; evitar conflitos"]
---

# Explosão de lote do WMS

O termo explosão de lote é muito utilizado no WMS, sendo o mesmo aquele que realizará a busca de uma determinada mercadoria que trabalhe com controle e data de validade. No sistema, atualmente, temos 3 formas para realizar o processo no WMS, que são elas:

**(1)** Onde no pedido pode ser informado o lote ou realizada a explosão de lote, deverá ser informado o item, tendo os parâmetros **"LOTAUTCENT" e "LOTEDTVAL"** habilitados.

**(1)** Habilitado o parâmetro **"LOTEENVIOWMS"** em um pedido, onde haja um produto com lote armazenado no WMS, este item não deverá ter seu campo **"CONTROLE (LOTE)"** preenchido. Devendo, assim, o pedido  ser confirmado e no envio para o WMS o sistema irá explodir o item no Pedido gravando os lotes encontrados, buscando o de menor validade e assim por diante, até atender a quantidade do pedido.

**(1)** Na tela **Comercial » Preferências » Empresa Aba 'WMS'** a marcação **"Utiliza explosão de lote na separação"** estando preenchida desta forma irá ser enviado ao WMS e as tarefas de separação irão ser preenchidas no campo controle com #EXPLODLOTE. No ato da separação no coletor, é permitido que o separador selecione o produto independente do seu lote. Desta forma, não fica condicionado a um lote específico, podendo ser pego o lote que o separador melhor encontrar em seu processo.

**![Imagem 1: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16342785203735) OBSERVAÇÃO:**

Ao realizar estas marcações, certifique que não está com o parâmetro **"LOTEENVIOWMS"** Habilitado e a marcação na tela **'Utiliza explosão de lote na separação'.** Com as duas marcações o sistema irá realizar divergências nas tarefas e causará inconsistência, não realizando a separação de maneira correta.
