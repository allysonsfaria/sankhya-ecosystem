---
id: "360043178914"
titulo: "Local 'X' não pode ser usado com a TOP 'Y'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043178914-Local-X-n%C3%A3o-pode-ser-usado-com-a-TOP-Y"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:02:55Z"
rotulos: ["#PUBLIFER", "CORE_E02935", "Configuração", "TOP", "Local 'X' não compatível com TOP 'Y'", "Ajuste regras de TOP ou altere Local", "Verifique regras e validações vinculadas", "Erro", "Comercial", "Restrições"]
---

# Local 'X' não pode ser usado com a TOP 'Y'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16163103080855) MENSAGEM:**

[CORE\_E02935] Local 'X' não pode ser usado com a TOP 'Y'.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16163103085847) SITUAÇÃO:**

Ao tentar confirmar um lançamento no sistema, a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16163103090583) SOLUÇÃO:**

![Imagem 4: TOP com restrições/exceções:](https://ajuda.sankhya.com.br/hc/article_attachments/16163091126679) TOP com restrições/exceções:

**(2)** Anote o **"[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"** que está sendo utilizado e siga com as orientações abaixo.

**(2)** Acesse o cadastro de TOP’s (Caminho: Comercial » Arquivo » Cadastros).

**(2)** Acione o botão **"Outras Opções"** » **"Restrições/Exceções"**.

![Imagem 5: (2) Acione o botão "Outras Opções" » "Restrições/Exceções" .](https://ajuda.sankhya.com.br/hc/article_attachments/14706057152279)

**(2)** Verifique se existem regras vinculadas para **Local**, caso positivo, realize os ajustes, de forma que o local desejado seja incluído ou certifique se outro local deverá ser utilizado no lançamento.

![Imagem 6: (2) Verifique se existem regras vinculadas para Local , caso positivo, realize os ajustes, de forma que o local…](https://ajuda.sankhya.com.br/hc/article_attachments/14706040642455)

![Imagem 7: Central de Certificações:](https://ajuda.sankhya.com.br/hc/article_attachments/16163091138327) Central de Certificações:

Caso a empresa utilize o módulo de **"[Central de Certificações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053-Central-de-Certifica%C3%A7%C3%B5es)"**, realize as análises abaixo:

**(2)** Acesse a tela **"[Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios)"** (Caminho de acesso: Configurações » Controle de Acesso);

**(2)** Selecione o usuário logado no sistema no momento que a validação ocorre;

**(2)** Busque a aba **"Validações**".

![Imagem 8: (2) Busque a aba "Validações ".](https://ajuda.sankhya.com.br/hc/article_attachments/14706085719063)

**(2)** Caso exista alguma regra vinculada, prossiga com as verificações a seguir. Caso não exista, possivelmente essa não é a causa do seu problema/incidente.

**(2)** Localizada a regra acima, acesse a tela Central de Certificações (Caminho de acesso: Comercial » Avançado » Certificações), busque a regra vinculada e faça a análise de sua funcionalidade.

**(2)** Se essa regra estiver vinculada a restrições de TOP/Local, sintonize internamente para compreender a necessidade dessa no processo da empresa e, assim, alterar os dados do seu lançamento ou desativar a regra.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16163091141527) CAUSA:**

Ocorre quando o lançamento está utilizando Local que tenha restrições e/ou validações em relação a TOP utilizada.
