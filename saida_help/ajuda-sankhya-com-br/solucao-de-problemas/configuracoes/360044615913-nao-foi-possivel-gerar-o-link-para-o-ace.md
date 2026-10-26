---
id: "360044615913"
titulo: "Não foi possível gerar o link para o acesso externo: o parâmetro 'Endereço para acesso externo ao WGE' não foi cadastrado no sistema"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044615913-N%C3%A3o-foi-poss%C3%ADvel-gerar-o-link-para-o-acesso-externo-o-par%C3%A2metro-Endere%C3%A7o-para-acesso-externo-ao-WGE-n%C3%A3o-foi-cadastrado-no-sistema"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:54:37Z"
rotulos: ["#PUBLIFER", "#Revisadoclaudio", "CORE_E03066", "Configuração", "Preferências", "Parâmetro", "Erro de Link para Acesso Externo ao WGE", "Erro", "WGE"]
---

# Não foi possível gerar o link para o acesso externo: o parâmetro 'Endereço para acesso externo ao WGE' não foi cadastrado no sistema

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16589648706455) MENSAGEM:**

[CORE\_E03066]: Não foi possível gerar o link para o acesso externo: o parâmetro 'Endereço para acesso externo ao WGE' não foi cadastrado no sistema.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16589634268695) CAUSA:**

Ao tentar executar rotinas no sistema que necessitam da URL de acesso e o parâmetro ENDACESSEXTWGE não estiver configurado, será apresentada a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16589634257687) SOLUÇÃO:**

![Imagem 4: Configure o parâmetro " ENDACESSEXTWGE" .](https://ajuda.sankhya.com.br/hc/article_attachments/16589634261783) Configure o parâmetro **"ENDACESSEXTWGE"**.

Acesse a tela **"Preferências"** (Caminho de acesso: Configurações » Avançado), busque pela chave **ENDACESSEXTWGE** e no campo **"Texto"**, informe o link (domínio) de acesso ao sistema.

- O parâmetro **"Endereço para acesso externo ao WGE", ENDACESSEXTWGE"**, é utilizado para determinar a URL externa de acesso ao sistema. A empresa deverá ter um link (domínio) que será apontado para o servidor do sistema, para que o sistema possa ser acessado pela internet.

![Imagem 5: O parâmetro "Endereço para acesso externo ao WGE", ENDACESSEXTWGE" , é utilizado para determinar a URL externa de…](https://ajuda.sankhya.com.br/hc/article_attachments/15298481916951)

![Imagem 6: Realizada essa configuração, teste uma nova execução do procedimento que estava sendo realizado.](https://ajuda.sankhya.com.br/hc/article_attachments/16589634263319) Realizada essa configuração, teste uma nova execução do procedimento que estava sendo realizado.
