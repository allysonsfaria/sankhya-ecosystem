---
id: "14198283222039"
titulo: "OC Fechada não permite alteração"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14198283222039-OC-Fechada-n%C3%A3o-permite-altera%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T14:59:23Z"
rotulos: ["Ordem de Carga", "Configuração", "COM_E00051", "Parâmetro", "Ative o parâmetro \"ALTOCFECFORMOC\" para permitir alterações", "OC fechada não pode ser alterada", "Parâmetro desativado impede alterações em OC fechada", "Erro", "Formação de carga"]
---

# OC Fechada não permite alteração

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16913805812503) MENSAGEM:**

[COM\_E00051]: OC Fechada não permite alteração.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16913790446487) SOLUÇÃO:**

![Imagem 3: Para utilizar uma ordem de carga fechada em novas notas/pedidos ou alterar um registro que possui uma ordem de carga…](https://ajuda.sankhya.com.br/hc/article_attachments/16913790452759) Para utilizar uma ordem de carga fechada em novas notas/pedidos ou alterar um registro que possui uma ordem de carga fechada vinculada, ative o parâmetro **"Permite alterar OC fechada na Formação de Carga? -** **ALTOCFECFORMOC".**

![Imagem 4: Quando habilitado, permite ao usuário alterar registros na tela de "Formação de Carga" . Quando a Ordem de Carga…](https://ajuda.sankhya.com.br/hc/article_attachments/16913805824279) Quando habilitado, permite ao usuário alterar registros na tela de **"Formação de Carga"**. Quando a Ordem de Carga estiver fechada, ative o parâmetro e gere a nota. Caso desabilite o parâmetro, o sistema não permite a mudança de nenhum dado referente a uma ordem de carga fechada.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16913790512407) CAUSA:**

Ocorre ao tentar alterar registros que possuem uma ordem de carga fechada vinculada ou tentar inserir uma ordem de carga fechada em um novo lançamento e o parâmetro **"Permite alterar OC fechada na Formação de Carga? -** **ALTOCFECFORMOC"** está desabilitado.
