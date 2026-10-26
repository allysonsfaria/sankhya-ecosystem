---
id: "8617472931351"
titulo: "Ordem de carga XXX usada na nota de Nro Unico: XXXX esta fechada e não pode ser alterada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/8617472931351-Ordem-de-carga-XXX-usada-na-nota-de-Nro-Unico-XXXX-esta-fechada-e-n%C3%A3o-pode-ser-alterada"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:11:53Z"
rotulos: ["Configuração", "NF-e", "TOP", "não apagar", "ORA-20101", "Alteração de Ordem de Carga Fechada", "Erro"]
---

# Ordem de carga XXX usada na nota de Nro Unico: XXXX esta fechada e não pode ser alterada

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16347550767767) MENSAGEM**:

ORA-20101: Ordem de carga XXX usada na nota de Nro Unico: XXXX esta fechada e não pode ser alterada.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16347550774167)CAUSA:**

Ao tentar emitir Nota Fiscal (Tipo de Movimento Devolução ou Complemento) e o parâmetro ALTOCFECFORMOC estiver desligado será retornado a Mensagem de Erro de Ordem de Carga Fechada, impedindo a emissão da nota.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16347568289047)SOLUÇÃO:**

A Ordem de Carga já está fechada e não é permitido gerar um novo lançamento de destino estando ela fechada. Mas é possível alterar uma Ordem de Carga ativando o parâmetro "**ALTOCFECFORMOC"**.

Quando habilitado, permite ao usuário alterar registros na tela de Formação de Carga. Quando a Ordem de Carga estiver fechada basta ativar o parâmetro e gerar a nota. Caso desabilite o parâmetro, o sistema não permite a mudança de nenhum dado referente a uma ordem de carga fechada.
