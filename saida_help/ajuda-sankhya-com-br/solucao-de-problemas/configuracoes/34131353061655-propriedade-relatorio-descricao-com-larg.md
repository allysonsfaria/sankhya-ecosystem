---
id: "34131353061655"
titulo: "\"Propriedade 'Relatorio.DESCRICAO' com largura acima do limite: (XX > XX)\" ao salvar um Relatório Formatado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34131353061655--Propriedade-Relatorio-DESCRICAO-com-largura-acima-do-limite-XX-XX-ao-salvar-um-Relat%C3%B3rio-Formatado"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:27:39Z"
rotulos: ["Configuração", "Relatórios Formatados", "Erro", "Relatorio.DESCRICAO", "criar ou alterar um relatório formatado (JRXML)", "cuja descrição ultrapassa o número máximo de caracteres", "largura acima do limite: (XX > XX)", "Descrição", "Propriedade 'Relatorio.DESCRICAO' com largura acima do limite: (XX > XX)", "Tamanho de Campo", "JRXML"]
---

# "Propriedade 'Relatorio.DESCRICAO' com largura acima do limite: (XX > XX)" ao salvar um Relatório Formatado

**MENSAGEM**

Propriedade 'Relatorio.DESCRICAO' com largura acima do limite: (XX > XX)

**SITUAÇÃO**

O erro ocorre ao criar ou alterar um relatório formatado (**JRXML**) cuja descrição ultrapassa o número máximo de caracteres permitidos pelo sistema.

**SOLUÇÃO**

**(1)**  Ajuste a descrição do relatório para que tenha tamanho igual ou inferior ao limite informado na mensagem de erro.

**(2)**  Conte também os caracteres de espaços e pontuação, pois eles são considerados no total.

**CAUSA**

O campo **"Descrição"** do relatório possui um tamanho máximo definido pela aplicação. Ao inserir um texto com quantidade de caracteres superior a esse limite, o sistema bloqueia a operação e retorna a mensagem de erro.
