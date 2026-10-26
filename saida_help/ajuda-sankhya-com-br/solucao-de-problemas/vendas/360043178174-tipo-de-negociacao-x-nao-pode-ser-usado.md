---
id: "360043178174"
titulo: "Tipo de Negociação 'X' não pode ser usado com a TOP 'Y'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043178174-Tipo-de-Negocia%C3%A7%C3%A3o-X-n%C3%A3o-pode-ser-usado-com-a-TOP-Y"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:03:10Z"
rotulos: ["#criadoRoger", "CORE_E02942", "Configuração", "Tipo de Negociação", "TOP", "Restrição entre Tipo de Negociação e TOP", "Verificar regras em \"Restrições/Exceções\" e \"Central de Certificações\"", "Ajustar ou desativar regras de validação", "Erro", "Comercial"]
---

# Tipo de Negociação 'X' não pode ser usado com a TOP 'Y'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16161626658455) MENSAGEM:**

[CORE\_E02942] Tipo de Negociação 'X' não pode ser usado com a TOP 'Y'.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16161626660247) SITUAÇÃO:**

Ao tentar realizar lançamentos no sistema, é apresentada a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16161626666519) SOLUÇÃO:**

![Imagem 4: TOP com restrições/exceções:](https://ajuda.sankhya.com.br/hc/article_attachments/16161612306711) TOP com restrições/exceções:

Anote o Tipo de Operação (TOP) que está sendo utilizado e siga com as orientações abaixo.

**(2)** Acesse o cadastro de **"[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"** (Comercial » Arquivo » Cadastros).

**(2)** Acione o botão "Outras Opções" » **"Restrições/Exceções"**.

**(2)** Verifique se existem regras vinculadas para **"Tipo de Negociação"**.

![Imagem 5: Central de Certificações:](https://ajuda.sankhya.com.br/hc/article_attachments/16161626669335) Central de Certificações:

Caso a empresa utilize o módulo de **"[Central de Certificações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053-Central-de-Certifica%C3%A7%C3%B5es)"**, realize as análises abaixo:

Acesse a tela "[**Usuários**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios)" (Configurações » Controle de Acesso) e selecione o usuário logado no sistema no momento que a validação ocorre.

**(2)** Verifique se existem informações na aba **"Validações"**.

**(2)** Caso exista alguma regra vinculada, prossiga com as verificações a seguir. Caso não exista, possivelmente essa não é a causa do seu problema/incidente.

**(2)** Localizada a regra acima, acesse a tela Central de Certificações (Caminho de acesso: Comercial » Avançado » Certificações), busque a regra vinculada e faça a análise de sua funcionalidade.

**(2)** Se essa regra estiver vinculada a restrições de TOP/Tipo de Negociação, sintonize internamente para compreender a necessidade dessa no processo da empresa e, assim, alterar os dados do seu lançamento ou desativar a regra.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16161612322327)CAUSA:**

Ocorre quando se esta utilizando Tipo de Negociação que tenha restrições e/ou validações em relação a TOP utilizada.
