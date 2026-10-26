---
id: "360043132934"
titulo: "Natureza 'X' não pode ser usada com a TOP Y"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043132934-Natureza-X-n%C3%A3o-pode-ser-usada-com-a-TOP-Y"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:04:46Z"
rotulos: ["#criadoRoger", "CORE_E02931", "Configuração", "TOP", "Natureza", "Ajuste restrições/exceções no cadastro de TOP", "Cheque regras na Central de Certificações", "Natureza 'X' incompatível com TOP 'Y'", "Erro", "Comercial"]
---

# Natureza 'X' não pode ser usada com a TOP Y

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16135648334487) MENSAGEM:**

[CORE\_E02931] Natureza 'X' não pode ser usada com a TOP 'Y'.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16135628666519) CAUSA:**

Ocorre quando está utilizando Natureza que tenha restrições e/ou validações em relação a TOP utilizada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16135628658583) SOLUÇÃO:**

![Imagem 4: TOP com restrições/exceções:](https://ajuda.sankhya.com.br/hc/article_attachments/16135648339223) TOP com restrições/exceções:

Anote o 'Tipo de Operação (TOP)' que está sendo utilizado e siga com as orientações abaixo.

**(2)** Acesse o cadastro de **"[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"** (Caminho de acesso: Comercial » Arquivo » Cadastros).

**(2)** Acione o botão **"Outras Opções"** » **"Restrições/Exceções"**.

![Imagem 5: (2) Acione o botão "Outras Opções" » "Restrições/Exceções" .](https://ajuda.sankhya.com.br/hc/article_attachments/14655175863447)

**(2)** Verifique se existem regras vinculadas para **"Natureza"**:

![Imagem 6: (2) Verifique se existem regras vinculadas para "Natureza" :](https://ajuda.sankhya.com.br/hc/article_attachments/14655175859351)

**(2)** Para utilização dessa TOP com essa Natureza, essa linha deverá ser excluída de exceções.

**(2)** Caso a marcação fosse para Restrições (só pode ser usado com), a Natureza desejada deverá constar nessa lista.

![Imagem 7: Central de Certificações:](https://ajuda.sankhya.com.br/hc/article_attachments/16135648342807) Central de Certificações:

Caso a empresa utilize o módulo de **"[Central de Certificações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053-Central-de-Certifica%C3%A7%C3%B5es)"** é necessário realizar as análises abaixo:

**(2)** Tela **"Usuários"** (Caminho de acesso: Configurações » Controle de Acesso).

**(2)** Selecione o usuário logado no sistema no momento que a validação ocorre.

**(2)** Busque a aba **"Validações"**.

**(2)** Caso exista alguma regra vinculada, prossiga com as verificações a seguir. Caso não exista, possivelmente essa não é a causa do seu problema/incidente.

**(2)** Localizada a regra acima, acesse a tela Central de Certificações (Caminho de acesso: Comercial » Avançado » Certificações), busque a regra vinculada e faça a análise de sua funcionalidade.

**(2)** Se essa regra estiver vinculada à restrições de TOP/Natureza, sintonize internamente para compreender a necessidade dessa no processo da empresa e assim alterar os dados do seu lançamento ou desativar a regra.
