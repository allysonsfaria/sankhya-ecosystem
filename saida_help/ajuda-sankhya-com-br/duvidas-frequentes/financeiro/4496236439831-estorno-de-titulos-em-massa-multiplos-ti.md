---
id: "4496236439831"
titulo: "Estorno de títulos em massa (múltiplos títulos)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4496236439831-Estorno-de-t%C3%ADtulos-em-massa-m%C3%BAltiplos-t%C3%ADtulos"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-07-22T15:19:03Z"
rotulos: ["Configuração", "Estorno", "Movimentação Financeira", "Atualização", "Financeiro", "#VALIDADOFER", "#CAUSARAIZ", "#O.S1597131", "Estorno simultâneo de múltiplos títulos", "Disponível apenas no layout HTML5", "Seleção de títulos confirmação e resumo do estorno"]
---

# Estorno de títulos em massa (múltiplos títulos)

**IMPLEMENTAÇÃO:**

A partir de implementação realizada na **versão 4.9b7**, o sistema permite o estorno simultâneo de múltiplos títulos, agilizando a correção de baixas realizadas indevidamente.

![Imagem 1: "Estorno de Títulos em massa" somente funciona no layout HTML5 (novo).](https://ajuda.sankhya.com.br/hc/article_attachments/16316029848983)  "Estorno de Títulos em massa" somente funciona no layout HTML5 (novo).

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16315982149655) SOLUÇÃO:**

Ao acessar a Movimentação Financeira, quando selecionar mais de um título (que estejam baixados) e clicar no botão **"Estornar"**, será aberta a janela **"Estorno de múltiplos títulos"**. Para confirmação, são exibidas algumas informações dos títulos selecionados: **"Estorno de múltiplos títulos"** com as informações de "Receita/Despesa", "Nro Único", "Nro Nota", "Vlr Baixa", "Data Baixa", "Origem", "Conciliado" e "Dh. Conciliação":

[GIF animado: Imagem 3: Ao acessar a Movimentação Financeira, quando selecionar mais de um título (que estejam baixados) e clicar no botão…](https://ajuda.sankhya.com.br/hc/article_attachments/4496200870167)

**Importante:** quando houver dentre os títulos apresentados, registros já conciliados na movimentação bancária, títulos que podem ser usados para recomposição e/ou títulos provenientes de antecipação de baixa, será apresentada a mensagem: **"Um ou mais títulos, dentre os selecionados, requerem sua atenção. Como deseja proceder?"** com as marcações abaixo:

(1)** Conciliados:** se estiver habilitada, irá estornar todos os títulos, inclusive os conciliados. Se estiver desmarcada, estornará apenas os não conciliados.

(1)** Recomposição:** caso essa marcação esteja ligada, o estorno tentará recompor o título original que foi dividido em duas ou mais parcelas no momento da baixa.

(1)** Antecipação:** se marcada, serão estornados os títulos provenientes de antecipação de baixa. Se desmarcada, esses títulos serão ignorados no estorno.

Quando você confirmar o estorno dos títulos apresentados na janela acima, será apresentada uma etapa de resumo com as abas **"Não Estornados"** e **"Estornados com sucesso"**, considerando que, na aba Não Estornados serão listados os títulos que não puderam ser estornados e sua justificativa e, na aba Estornados com sucesso, teremos os títulos que foram estornados:

[GIF animado: Imagem 4: Quando você confirmar o estorno dos títulos apresentados na janela acima, será apresentada uma etapa de resumo com as…](https://ajuda.sankhya.com.br/hc/article_attachments/4496244135063)

**Observação:** a aba Estornados com sucesso apenas será exibida caso não hajam títulos com impedimentos ao estorno e, consequentemente, a aba Não Estornados será ocultada e vice-versa.
