---
id: "360044616073"
titulo: "Parceiro 'X' não pode ser usado com a TOP 'Y'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616073-Parceiro-X-n%C3%A3o-pode-ser-usado-com-a-TOP-Y"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:54:27Z"
rotulos: ["#PUBLIFER", "CORE_E02944", "Configuração", "Parceiro", "TOP", "Restrição de Parceiro para Tipo de Operação Específico", "Erro", "Comercial"]
---

# Parceiro 'X' não pode ser usado com a TOP 'Y'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16636495070231) MENSAGEM:**

[CORE\_E02944]:  Parceiro 'X' não pode ser usado com a TOP 'Y'.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16636495073303) SOLUÇÃO:**

![Imagem 3: TOP com restrições/exceções:](https://ajuda.sankhya.com.br/hc/article_attachments/16636510285079) TOP com restrições/exceções:

Anote o 'Tipo de Operação (TOP)' que está sendo utilizado e siga com as orientações abaixo.

- Acesse a tela **"Tipos de Operação - TOP"** (Caminho de acesso: Comercial » Arquivo » Cadastros);
- Acione o botão 'Outras Opções' » 'Restrições/Exceções';

![Imagem 4: Acione o botão 'Outras Opções' » 'Restrições/Exceções';](https://ajuda.sankhya.com.br/hc/article_attachments/14837449252119)

Verifique se existem regras vinculadas para 'Parceiro':

![Imagem 5: Verifique se existem regras vinculadas para 'Parceiro':](https://ajuda.sankhya.com.br/hc/article_attachments/14837480228759)

- No exemplo acima, a TOP não poderá ser usada com o parceiro 18.
- Para utilização dessa TOP com esse parceiro, essa linha deverá ser excluída de exceções. Para tal, realize alinhamento interno e compreenda se essa exclusão é válida para o cenário atual da empresa.
- Caso a marcação fosse para 'Restrições' (só pode ser usado com), a empresa desejada deverá constar nessa lista.

![Imagem 6: Central de Certificações:](https://ajuda.sankhya.com.br/hc/article_attachments/16636495079319) Central de Certificações:

Caso a empresa utilize o módulo de 'Central de Certificações' realize as análises abaixo:

- Tela **"Usuários"** (Caminho de acesso: Configurações » Controle de Acesso);
- Selecione o usuário logado no sistema no momento que a validação ocorre;
- Busque a aba **"Validações"**.

![Imagem 7: Busque a aba "Validações" .](https://ajuda.sankhya.com.br/hc/article_attachments/14837501665303)

Caso exista alguma regra vinculada, prossiga com as verificações a seguir. Caso não exista, possivelmente essa não é a causa do seu problema/incidente.

- Localizada a regra acima, acesse a tela **"Central de Certificações"** (Caminho de acesso: Comercial » Avançado » Certificações), busque a regra vinculada e faça a análise de sua funcionalidade.
- Se essa regra estiver vinculada a restrições de TOP/Parceiro, sintonize internamente para compreender a necessidade dessa no processo da empresa e, assim, alterar os dados do seu lançamento ou desativar a regra.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16636495081239) CAUSA:**

Ocorre quando está sendo utilizado um Código 'Parceiro' que tenha restrições e/ou validações em relação a 'TOP' utilizada.
