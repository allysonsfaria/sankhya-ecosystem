---
id: "360044294413"
titulo: "É possível alterar um Processo Produtivo sem Versionar?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044294413-%C3%89-poss%C3%ADvel-alterar-um-Processo-Produtivo-sem-Versionar"
trilha: "Dúvidas Frequentes > Produção"
atualizado_em: "2026-07-22T15:58:57Z"
rotulos: ["Produtos", "Configuração", "Processo Produtivo", "Produção", "Permitido: Alterar produtos sem OP vinculada", "Versionamento obrigatório: Alterações após OP", "Bloqueio: Alteração de informações gerais após OP", "Operação de Produção"]
---

# É possível alterar um Processo Produtivo sem Versionar?

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17294205555607) SITUAÇÃO:**

ROTINA: **Produção » Cadastros » Processo Produtivo -**Botão: **"Versionar"**

A partir da versão 3.19 (SankhyaW) foi criado a rotina de versionamento, na qual um processo produtivo caso já tenha OP (Operação de Produção) lançada utilizando só pode ser alterado se criar uma nova versão. 
Porém, é permitido realizar alterações nos produtos PA's e MP's dentro do processo produtivo mesmo que ele esteja exigindo versionamento.

Segue abaixo as situações em que essa alteração é possível: 

**(1)** **Caso¹:** Processo Produtivo criado, publicado e sem lançamento de OP. 
Pode-se alterar qualquer informação dentro do Processo. 

**(1)** **Caso²:** Processo Produtivo criado e com OP lançada. 
Após fazer o lançamento de uma OP não será mais possível alterar as informações gerais do cadastro do processo produtivo, como Planta de Manufatura, definição de terceiro, Repositório Inicial, alterações de configuração de lote do PA, etc.

Porém, ainda será possível fazer alterações em todos os outros produtos que não tem OP vinculada, como alterar quantidades, inserir produtos, excluir produtos, inserir PA, sub-produtos, etc.

Ou seja, o bloqueio de edição dos produtos está vinculado ao lançamento

Detalhes sobre a opção 'Versionar', acesse o Help do SankhyaW da Rotina.
