---
id: "360043359253"
titulo: "Produto 'X' não pode ser usado com a TOP 'Y'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043359253-Produto-X-n%C3%A3o-pode-ser-usado-com-a-TOP-Y"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:05:35Z"
rotulos: ["#criadoRoger", "CORE_E02937", "Produtos", "Configuração", "TOP", "Ajustar restrições ou exceções no cadastro da TOP", "Produto não pode ser usado com a TOP especificada", "Verificar regras vinculadas ao usuário e produto", "Erro", "Comercial"]
---

# Produto 'X' não pode ser usado com a TOP 'Y'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16090286605847) MENSAGEM:**

[CORE\_E02937] Produto 'X' não pode ser usado com a TOP 'Y'.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16090286609815) SITUAÇÃO:**

Ao tentar confirmar um lançamento no sistema, a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16090286613911) SOLUÇÃO:**

![Imagem 4: TOP com restrições/exceções:](https://ajuda.sankhya.com.br/hc/article_attachments/16090286617111) TOP com restrições/exceções:

**(2)** Anote o **"Tipo de Operação (TOP)"** que está sendo utilizado e siga com as orientações abaixo.

**(2)** Acesse o cadastro de TOP’s (Caminho para acesso: Comercial » Arquivo » Cadastros).

**(2)** Acione o botão **"Outras Opções"** » **"Restrições/Exceções"**.

![Imagem 5: (2) Acione o botão "Outras Opções" » "Restrições/Exceções" .](https://ajuda.sankhya.com.br/hc/article_attachments/14475318518551)

**(2)** Para utilização dessa TOP com esse produto, ele deveria ser excluído de exceções.

**(2)** Caso a marcação fosse para **"Restrições"** (só pode ser usado com), o produto desejado deverá constar nessa lista.

![Imagem 6: Central de Certificações:](https://ajuda.sankhya.com.br/hc/article_attachments/16090270721815) Central de Certificações:

Caso a empresa utilize o módulo de **["Central de Certificações"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053-Central-de-Certifica%C3%A7%C3%B5es)**, realize as análises abaixo:

**(2)** Tela "**Usuários**" (Caminho para acesso: Configurações » Controle de Acesso).

**(2)** Selecione o usuário logado no sistema no momento que a validação ocorre.

**(2)** Busque a aba **"Validações"**.

**(2)** Caso exista alguma regra vinculada, prossiga com as verificações a seguir. Caso não exista, possivelmente essa não é a causa do seu problema/incidente.

**(2)** Localizada a regra acima, acesse a tela **"Central de Certificações"** (Caminho de acesso: Comercial » Avançado » Certificações), busque a regra vinculada e faça a análise de sua funcionalidade.

**(2)** Se essa regra estiver vinculada a restrições de TOP/Produto, sintonize internamente para compreender a necessidade dessa no processo da empresa e, assim, alterar os dados do seu lançamento ou desativar a regra.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16090286628759) CAUSA:**

Ocorre quando o lançamento esta utilizando Produto que tenha restrições e/ou validações em relação a TOP utilizada.
