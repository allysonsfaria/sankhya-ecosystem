---
id: "14864479027991"
titulo: "'Vend. do lanç. de comissão' não pode ser combinado com outros vendedores"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14864479027991--Vend-do-lan%C3%A7-de-comiss%C3%A3o-n%C3%A3o-pode-ser-combinado-com-outros-vendedores"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T14:57:51Z"
rotulos: ["Configuração", "Parceiro", "Comissão", "Cálculo de Comissão", "COM_E00585", "Parâmetros Desabilitados", "Reativar e Descartar Cache", "Aviso de Comissão", "Erro"]
---

# 'Vend. do lanç. de comissão' não pode ser combinado com outros vendedores

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16621475124375) MENSAGEM:**

[COM\_E00585]: 'Vend. do lanç. de comissão' não pode ser combinado com outros vendedores!

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16621475137559)CAUSA:**

Ocorre porque em algum momento o parâmetro LANCAR COMISSAO MULTIPLA ter sido  habilitado e  a marcação CALCULAR COMISSAO MUTIPLA foi marcada na tela de **"Cálculo de comissão"** e, em seguida, o parâmetro foi **desabilitado**.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16621463307671)SOLUÇÃO:**

Na tela Comercial » Avançado » Cálculo de Comissão por Fórmula, ao marcar a opção para calcular para "Vendedor da nota" estava retornando o aviso 'Vendedor/Executante dos itens' não pode ser combinado com outros vendedores!
Porém consta somente uma marcação.

![Imagem 4: Na tela Comercial » Avançado » Cálculo de Comissão por Fórmula, ao marcar a opção para calcular para "Vendedor da nota"…](https://ajuda.sankhya.com.br/hc/article_attachments/14864406538007)

É provável que em algum momento o parâmetro **"LANCCOMMULT' Lançar Comissão p/Múltiplos Vendedores?"** foi ativado.

E ao tentar realizar a busca dos dados para calcular a comissão não estava sendo possível, sendo assim, ative novamente o parâmetro, desabilite a opção vendedor da comissão múltipla que estava retornando ativo, descarte o cache da administração do servidor e feche a tela calcular comissão por fórmula.

![Imagem 5: E ao tentar realizar a busca dos dados para calcular a comissão não estava sendo possível, sendo assim, ative novamente…](https://ajuda.sankhya.com.br/hc/article_attachments/14864472209943)

Após realizar este processo, abra novamente a tela e busque pela nota.
