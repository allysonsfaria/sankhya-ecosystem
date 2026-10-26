---
id: "20147426739479"
titulo: "Não foi possível encontrar o Parceiro Remetente! Não há um parceiro ativo e com o CPF/CNPJ: 00000000000000"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/20147426739479-N%C3%A3o-foi-poss%C3%ADvel-encontrar-o-Parceiro-Remetente-N%C3%A3o-h%C3%A1-um-parceiro-ativo-e-com-o-CPF-CNPJ-00000000000000"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:51:16Z"
rotulos: ["Configuração", "Parceiro", "XML", "CORE_E07065", "Cadastro", "Parceiro Remetente Ausente", "CORE_E07067", "Erro"]
---

# Não foi possível encontrar o Parceiro Remetente! Não há um parceiro ativo e com o CPF/CNPJ: 00000000000000

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/20147426724631) **MENSAGEM:**

[CORE\_E07065] Não foi possível encontrar o Parceiro Remetente! Não há um parceiro ativo e com o CPF/CNPJ: 00000000000000.

[CORE\_E07067] Não foi possível encontrar o Parceiro Destinatário! Não há um parceiro ativo e com o CPF/CNPJ: 00000000000000

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/20147412432407)CAUSA:**

Atualmente o sistema olha para o primeiro cadastro com CNPJ = '00000000000000' existente na TGFPAR. Para verificar essa informação acesse a tela **"[Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)"** (Caminho: Configurações » Cadastros » Parceiros) e observe o campo **"CNPJ/CPF"**

![Imagem 3: Atualmente o sistema olha para o primeiro cadastro com CNPJ = '00000000000000' existente na TGFPAR. Para verificar essa…](https://ajuda.sankhya.com.br/hc/article_attachments/24024019995415)

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/20147426726423)SOLUÇÃO:**

Necessário manter apenas o parceiro com CNPJ = '00000000000000'  existente no XML com as demais informações, Razão Social, endereço.
