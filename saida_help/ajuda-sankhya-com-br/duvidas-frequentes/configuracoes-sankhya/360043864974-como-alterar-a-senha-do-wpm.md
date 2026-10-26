---
id: "360043864974"
titulo: "Como alterar a senha do WPM?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043864974-Como-alterar-a-senha-do-WPM"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-08-27T13:40:11Z"
rotulos: ["Produtos", "Configuração", "Segurança", "Atualização", "WPM", "Alteração de Senha no WPM"]
---

# Como alterar a senha do WPM?

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17128939724439) SITUAÇÃO:**

Quando a senha de acesso ao WPM é alterada e o cliente esqueceu esta senha, então é preciso excluir o arquivo 'wpm.session' para voltar a senha padrão.

- A senha padrão do WPM é **admin**. [Outras possibilidades : tecsis, 123456]
- Ao entrar no atualizador pela primeira vez com esta senha será solicitada a alteração de senha.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17128939727639) SOLUÇÃO:**

Caso essa informação se perca, ainda assim é possível alterar a senha do WPM como mostrado abaixo:

![Imagem 3: Acesse o servidor onde está instalado o WPM. Em Windows, acesse o sistema SankhyaOm, Administração do Servidor, aba…](https://ajuda.sankhya.com.br/hc/article_attachments/17128913753751) Acesse o servidor onde está instalado o WPM. Em Windows, acesse o sistema **SankhyaOm,** Administração do Servidor, aba **"Geral",** Diretório do Usuário e copie o link do diretório:

![Imagem 4: Acesse o servidor onde está instalado o WPM. Em Windows, acesse o sistema SankhyaOm, Administração do Servidor, aba…](https://ajuda.sankhya.com.br/hc/article_attachments/4403915344023)

Acesse pelo Executar (Botão Win + R):

![Imagem 5: Acesse pelo Executar (Botão Win + R):](https://ajuda.sankhya.com.br/hc/article_attachments/4403914730903)

![Imagem 6: Localize a pasta de instalação do WPM ( sankhyaw-wpm ). Existe o arquivo de nome ' wpm.session ' .](https://ajuda.sankhya.com.br/hc/article_attachments/17128939732119) Localize a pasta de instalação do WPM (sankhyaw-wpm). Existe o arquivo de nome '**wpm.session**' .

![Imagem 7: Localize a pasta de instalação do WPM ( sankhyaw-wpm ). Existe o arquivo de nome ' wpm.session ' .](https://ajuda.sankhya.com.br/hc/article_attachments/4403914770711)

![Imagem 8: Exclua definitivamente este arquivo. Como isso, o WPM voltará para a senha padrão ' admin '.](https://ajuda.sankhya.com.br/hc/article_attachments/17128939734679) Exclua definitivamente este arquivo. Como isso, o WPM voltará para a senha padrão '**admin**'.

![Imagem 9: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17128939738519) **OBSERVAÇÃO:**

Caso não encontre neste diretório, pesquise na pasta do usuário, executando o %userprofile%

Se Linux, procure /home/mgeweb/sankhyaw-wpm.

![Imagem 10: Acesse novamente o WPM com a senha padrão e será solicitada a alteração da senha no próximo acesso.](https://ajuda.sankhya.com.br/hc/article_attachments/17128939739671) Acesse novamente o WPM com a senha padrão e será solicitada a alteração da senha no próximo acesso.
