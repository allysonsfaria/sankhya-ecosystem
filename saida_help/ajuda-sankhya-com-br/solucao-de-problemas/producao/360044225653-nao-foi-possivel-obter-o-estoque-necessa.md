---
id: "360044225653"
titulo: "Não foi possível obter o estoque necessário da Matéria-prima 'X'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044225653-N%C3%A3o-foi-poss%C3%ADvel-obter-o-estoque-necess%C3%A1rio-da-Mat%C3%A9ria-prima-X"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-07-22T16:00:10Z"
rotulos: ["#PUBLIFER", "#revisadohugo", "PROD_E00075", "Configuração", "TOP", "Estoque", "Produção", "Verifique apontamentos e estoques", "Estoque insuficiente de matéria-prima", "Falta de estoque para produção", "Erro", "Artigo atualizado KCS", "Produção - KCS"]
---

# Não foi possível obter o estoque necessário da Matéria-prima 'X'

**MENSAGEM**

[PROD\_E00075]: Não foi possível obter o estoque necessário da matéria-prima 'X' ou **"Estoque insuficiente no local X para finalizar o apontamento"**.

**SITUAÇÃO**

Ao realizar apontamentos em **Operações de Produção (Produção » Rotinas » Operações de Produção)** ou em **Apontamento de Produção (Produção » Rotinas » Apontamento de Produção)**, o sistema solicita o estoque disponível para gerar a nota de produção e finalizar o processo.

**SOLUÇÃO**

Considere as validações de estoque necessário para consumo de matéria-prima no processo produtivo, avaliando os cenários abaixo:

**(1)**  **Verificação de atividades:** Identifique em quantas atividades as matérias-primas estão sendo apontadas. O ideal é que sejam apontadas em apenas uma atividade, para evitar duplicidade de baixa. Caso para determinada atividade o apontamento não seja necessário, realize os devidos ajustes na parametrização do processo produtivo, para não apontar MP.

**(2)** **Apontamentos parciais:** Realize os apontamentos parciais sempre na mesma atividade, evitando fracionar o consumo de matérias-primas em atividades diferentes.

**(3)** **Verificações de estoque:** Verifique se existe saldo suficiente para o **"Local"**, **"Controle"** e **"Empresa"** selecionados na respectiva operação. Caso a matéria-prima trabalhe com **"Controle por Lote"**, valide se o lote apontado ou à explodir se encontra dentro da validade ou trabalhar com 'Usa Status de Lote'(Controle de qualidade) e está conforme a movimentação da TOP.

**(4)**  **Validação do Processo Produtivo:** Com o processo e a versão utilizados na OP, acesse: **Processo Produtivo - NOVA » Roteiro » Atividade » aba Operações de Estoque,** verifique se todas as configurações estão corretas.

**(5)**   **Validação da Composição do Produto:** Com o Produto Acabado, Processo Produtivo e versão utilizados na OP, acesse: **Composição do Produto » Aba Matérias-Primas,** confirme se todas as configurações estão corretas.

**(6)**   **Parâmetro LOTAUTCENT:** Caso os materiais a serem consumidos utilizem controle por lote e o sistema realize a explosão, verifique o parâmetro: **“LOTAUTCENT – Controle automático por data de validade do lote?”,** na tela: **Configurações » Avançado » Preferências**

**(7)**   **Configurações de Estoque da TOP de Produção:** Valide os seguintes campos: **'Atualiza Estoque MP'**, **'Estoque MP de Terceiros'** e **'Status para Baixa no Estoque'.**

**(8)**   **Configurações de Estoque – Grupos de Produtos e Serviços:** Verifique o campo: **'Valida Estoque'.**

**Correção de fluxo:** Caso as matérias-primas já tenham sido apontadas incorretamente em mais de uma atividade gerando consumo duplicado, pode ser necessário cancelar a Ordem de Produção atual e criar uma nova, realizar um processo de Desmonte ou Ajuste de Estoque.

Caso seja necessário realize as devidas alterações nos cadastros mencionados, evitando a mensagem de estoque insuficiente.

**CAUSA**

A mensagem ocorre por falta de estoque físico disponível ou por parametrização de processo, composição ou configurações globais de estoque. Se as matérias-primas foram apontadas em mais de uma atividade, o sistema pode interpretar o consumo como duplicado para cada nota de produção, elevando o consumo e gerando a mensagem de estoque insuficiente.
