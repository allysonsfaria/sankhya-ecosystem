---
id: "7110390899735"
titulo: "O parceiro escolhido não possui um contato habilitado para responder cotações no portal, por isso só é permitido coleta manual"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7110390899735-O-parceiro-escolhido-n%C3%A3o-possui-um-contato-habilitado-para-responder-cota%C3%A7%C3%B5es-no-portal-por-isso-s%C3%B3-%C3%A9-permitido-coleta-manual"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T15:15:09Z"
rotulos: ["Configuração", "Cotação", "Parceiro", "Portal de Vendas", "COTC_E00044", "COTC_E00044-  Restrição na Coleta Automática de Cotações", "Erro"]
---

# O parceiro escolhido não possui um contato habilitado para responder cotações no portal, por isso só é permitido coleta manual

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16490734779287) MENSAGEM:**

[COTC\_E00044] O parceiro escolhido não possui um contato habilitado para responder cotações no portal, por isso só é permitido coleta manual.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16490734783127) CAUSA:**

Mensagem apresentada quando o fornecedor não possui um contato marcado para "Envia notificações de cotação?" e a coleta de preço foi definida como 'Online'.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16490734786839) SOLUÇÃO:**

Verifique na tela **"Cotação"** (Caminho de acesso: Cotação » Rotinas » Cotação)**,** as configurações abaixo:

(1)** Coleta de preço:** este campo representa a forma de coleta do preço do produto cotado; o mesmo pode possuir dois valores:

- **Online:** o fornecedor possuirá esta definição quando um contato ativo cadastrado do fornecedor possuir a marcação **"Envia notificações de cotação?"** realizada;
- **Manual:** o fornecedor possuirá esta marcação quando suas configurações forem opostas às citadas acima para o valor **"Online"**.

![Imagem 4: Manual: o fornecedor possuirá esta marcação quando suas configurações forem opostas às citadas acima para o valor…](https://ajuda.sankhya.com.br/hc/article_attachments/15938693805079)

O campo **"Coleta de preço"** não pode ser editado pelo comprador, porém, quando o comprador coletar manualmente o preço de um fornecedor que possui a coleta online, automaticamente o campo será modificado para **"Manual"**.

**Nota:** 

- Se a cotação possui um contato associado, e este possui permissão para receber a notificação da cotação, então o envio será realizado para este contato. Se este não possui permissão, então nenhum contato recebe o e-mail.
- Se não houver contato associado à cotação, então pegamos o 'contato padrão para cotação' do parceiro (Aba Geral >> Contato padrão para cotação), se este possui permissão para receber a notificação da cotação, então apenas ele recebe o e-mail com a cotação. Caso ele não possua permissão, então nenhum contato recebe o e-mail.
- Se não houver contato associado à cotação, e o parceiro não possui contato padrão para cotação, então pegamos o primeiro contato do parceiro configurado para receber e-mail de cotação.
