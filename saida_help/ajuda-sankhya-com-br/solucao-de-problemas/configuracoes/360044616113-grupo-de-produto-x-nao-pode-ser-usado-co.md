---
id: "360044616113"
titulo: "Grupo de Produto 'X' não pode ser usado com a TOP 'Y'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616113-Grupo-de-Produto-X-n%C3%A3o-pode-ser-usado-com-a-TOP-Y"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:54:23Z"
rotulos: ["#PUBLIFER", "CORE_E02936", "Produtos", "Configuração", "TOP", "Restrições entre Grupo de Produto e Tipo de Operação (TOP)", "Erro", "Comercial"]
---

# Grupo de Produto 'X' não pode ser usado com a TOP 'Y'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16617328078487) MENSAGEM:**

[CORE\_E02936]  Grupo de Produto 'X' não pode ser usado com a TOP 'Y'.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16617365001623) SOLUÇÃO:**

![Imagem 3: TOP com restrições/exceções:](https://ajuda.sankhya.com.br/hc/article_attachments/16617328085143) TOP com restrições/exceções:

Anote o **"Tipo de Operação (TOP)"** que está sendo utilizado e siga com as orientações abaixo:

- Acesse a tela **"Tipos de Operação"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e selecione a TOP em questão, por exemplo '1407 - Compra - Matéria Prima';
- Clique no botão **'Outras Opções**' » '**Restrições/Exceções**'.

![Imagem 4: Clique no botão 'Outras Opções ' » ' Restrições/Exceções '.](https://ajuda.sankhya.com.br/hc/article_attachments/32694558199063)

- Verifique se existem regras vinculadas para '**GRUPO PROD.**

![Imagem 5: Verifique se existem regras vinculadas para ' GRUPO PROD.](https://ajuda.sankhya.com.br/hc/article_attachments/32694558205975)

- No exemplo acima, a TOP selecionada (1407 - Compra - Matéria Prima) não poderá ser usada com o grupo de produto '60000 - Produtos Intermediários'.
- Para utilização dessa TOP com esse grupo de produto, ele deveria ser **excluído de exceções**.
- Caso a marcação fosse para '**Restrições**' (só pode ser usado com), o grupo de produto desejado deveria constar nessa lista.

![Imagem 6: Central de Certificações:](https://ajuda.sankhya.com.br/hc/article_attachments/16617365005591) Central de Certificações:

Caso a empresa utilize o módulo de **"Central de Certificações"**, realize as análises abaixo:

- Acesse a tela "**Usuários**": (Caminho de acesso: Configurações » Controle de Acesso);
- Selecione o usuário logado no sistema, no momento que a validação ocorre;
- Busque a aba '**Validações**'.

![Imagem 7: Busque a aba ' Validações '.](https://ajuda.sankhya.com.br/hc/article_attachments/14874447888279)

- Caso exista alguma regra vinculada, prossiga com as verificações a seguir. Caso não exista, possivelmente essa não é a causa do seu problema/incidente.
- Localizada a regra acima, acesse a tela **"Central de Certificações**" (Caminho de acesso: Comercial » Avançado » Certificações), busque a regra vinculada e faça a análise de sua funcionalidade.
- Se essa regra estiver vinculada a restrições de TOP/Grupo de Produto, sintonize internamente para compreender a necessidade desse no processo da empresa e, assim alterar os dados do seu lançamento ou desativar a regra.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16617328090135) CAUSA:**

Ocorre quando o lançamento está utilizando 'Grupo de Produto' que tenha restrições e/ou validações em relação a 'TOP' utilizada.
