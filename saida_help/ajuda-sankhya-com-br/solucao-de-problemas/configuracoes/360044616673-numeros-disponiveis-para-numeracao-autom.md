---
id: "360044616673"
titulo: "Números disponíveis para numeração automática acabaram"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616673-N%C3%BAmeros-dispon%C3%ADveis-para-numera%C3%A7%C3%A3o-autom%C3%A1tica-acabaram"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:53:41Z"
rotulos: ["#RevisadoGui", "CORE_E02249", "Configuração", "NF-e", "TOP", "ORA-06512", "Como Resolver Erro de Numeração Automática Esgotada", "Erro", "Documentos Eletrônicos"]
---

# Números disponíveis para numeração automática acabaram

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18603094930199) MENSAGEM:**

[CORE\_E02249] Números disponíveis para numeração automática acabaram!
ORA-06512: em "SANKHYA.STP\_NUMERAR\_NOTA2", line 104
ORA-06512: em line 1.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18603094932375) CAUSA:**

Ocorre quando uma TOP configurada para numerar o Pedido/Nota, teve a numeração esgotada. Devendo então aumentar o valor no cadastro da TOP.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18603094935447) SOLUÇÃO:**

Acesse a tela Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

Botão: Outras Opções...>>Controle de Numeração

Campo: Último número do talão: [Aumentar o valor neste campo]

Acesse a respectiva TOP (Tipo de Operação) do Pedido/Nota, e ao acessar a tela de 'Controle de Numeração', encontre a linha referente ao lançamento (Empresa/Serie/Mod.Doc. Fiscal) e faça o ajuste indicado acima.

Salve o registro alterado na TOP e posteriormente confirme o Pedido/Nota novamente.
