---
id: "360043698013"
titulo: "Empresa 'X' não pode ser usada com a TOP 'Y'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043698013-Empresa-X-n%C3%A3o-pode-ser-usada-com-a-TOP-Y"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:02:39Z"
rotulos: ["#criadoRoger", "CORE_E02945", "Configuração", "Empresa", "TOP", "Restrição de uso", "Verifique e ajuste as exceções", "Restrições de TOP/Empresa", "Erro", "Restrições"]
---

# Empresa 'X' não pode ser usada com a TOP 'Y'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16161248756247) MENSAGEM:**

[CORE\_E02945] Empresa 'X' não pode ser usada com a TOP 'Y'.

**![Imagem 2: SOLUÇÃO](https://ajuda.sankhya.com.br/hc/article_attachments/16161248757015) SOLUÇÃO**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse a tela " Tipos de Operação - TOP " (Caminho de acesso: Comercial » Arquivo » Cadastros), a note o 'Tipo de…](https://ajuda.sankhya.com.br/hc/article_attachments/16161248758551) Acesse a tela **"[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)"** (Caminho de acesso: Comercial » Arquivo » Cadastros), anote o 'Tipo de Operação (TOP)' que está sendo utilizado e siga com as orientações abaixo.

- Acione o botão "**Outras Opções**" » "**Restrições/Exceções"**.

![Imagem 4: Acione o botão " Outras Opções " » " Restrições/Exceções" .](https://ajuda.sankhya.com.br/hc/article_attachments/14708804542231)

Verifique se existem regras vinculadas para 'EMPRESA':

![Imagem 5: Verifique se existem regras vinculadas para 'EMPRESA':](https://ajuda.sankhya.com.br/hc/article_attachments/14708805731095)

- No exemplo acima, a TOP não poderá ser usada com a Empresa 25.
- Para utilização dessa TOP com essa empresa, essa linha deverá ser excluída de exceções.
- Caso a marcação fosse para 'Restrições' (só pode ser usado com), a empresa desejada deverá constar nessa lista.

![Imagem 6: Acesse a tela " Central de Certificações " (Caminho de acesso: Comercial » Avançado » Certificações):](https://ajuda.sankhya.com.br/hc/article_attachments/16161248759191) Acesse a tela **"[Central de Certificações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053)"** (Caminho de acesso: Comercial » Avançado » Certificações):

Caso a empresa utilize o módulo de 'Central de Certificações', realize as análises abaixo:

- Tela **"[Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874)"**: (Caminho de acesso: Configurações » Controle de Acesso).
- Selecione o usuário logado no sistema no momento que a validação ocorre.
- Busque a aba "**Validações"**.

![Imagem 7: Busque a aba " Validações" .](https://ajuda.sankhya.com.br/hc/article_attachments/14708799881239)

- Caso exista alguma regra vinculada, prossiga com as verificações a seguir. Caso não exista, possivelmente essa não é a causa do seu problema/incidente.
- Localizada a regra acima, acesse a tela "[**Central de Certificações**"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053) (Comercial > Avançado > Certificações), busque a regra vinculada e faça a análise de sua funcionalidade.
- Se essa regra estiver vinculada a restrições de TOP/Empresa, sintonize internamente para compreender a necessidade dessa no processo da empresa e, assim, alterar os dados do seu lançamento ou desativar a regra.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16161248759703) CAUSA:**

Ocorre quando há restrições/exceções de uso da respectiva empresa com a TOP do lançamento, impedindo o lançamento.
