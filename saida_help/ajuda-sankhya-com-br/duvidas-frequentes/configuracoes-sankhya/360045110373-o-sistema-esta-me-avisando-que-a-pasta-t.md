---
id: "360045110373"
titulo: "O sistema está me avisando que a pasta temporária é inválida"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110373-O-sistema-est%C3%A1-me-avisando-que-a-pasta-tempor%C3%A1ria-%C3%A9-inv%C3%A1lida"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-09-11T20:40:08Z"
rotulos: ["AJUDA DO SKW", "Configuração", "Relatórios", "Sankhya-W", "O sistema está me avisando que a pasta temporária é inválida manual", "Resolvendo Aviso de Pasta Temporária", "Erro", "Instalação"]
---

# O sistema está me avisando que a pasta temporária é inválida

#### Aviso de pasta temporária inválida:

#### Por que o Sankhya-W está me avisando de problemas com o diretório temporário?

Você está sendo avisado porque tal problema é crítico e pode comprometer o funcionamento de algumas rotinas do sistema, como geração e visualização de relatórios, inclusão de anexos, operações com imagens, entre outras.

Verifique se o Sankhya-W foi instalado conforme padrão definido nos manuais de ‘Instalação/Atualização do Sistema’. Isto ocorre principalmente por erros na configuração do sistema.

#### Como resolver?

- **Linux**

![Imagem 1: Verifique se o disco ou as partições estão cheias, através do comando: df-h](https://ajuda.sankhya.com.br/hc/article_attachments/19357514640279) Verifique se o disco ou as partições estão cheias, através do comando:  **df-h**

![Imagem 2: A instalação e todas as configurações do sistema devem ser feitas utilizando o usuário padrão definido: “ mgeweb ”.](https://ajuda.sankhya.com.br/hc/article_attachments/19357514651799) A instalação e todas as configurações do sistema devem ser feitas utilizando o usuário padrão definido: “mgeweb”.

•Verifique se o JBoss está instalado a partir do diretório “/home/mgeweb”

•Verifique se a incialização do JBoss foi feita com o usuário mgeweb.

- **Windows:**

Se a inicialização do sistema for Serviço, defina um usuário responsável pela inicialização do Serviço:

  1    Clique com o botão direito do mouse, selecione “Propriedades”

[GIF animado: Imagem 3: 1 Clique com o botão direito do mouse, selecione “ Propriedades ”](https://sankhyasd.zendesk.com/hc/article_attachments/360043290513/embim87.gif)

  2   Na aba “Logon”, selecione “Esta Conta”, defina a conta, a senha e redigite a senha novamente.

Esta conta é o usuário do Windows utilizado para logon.

[GIF animado: Imagem 4: Esta conta é o usuário do Windows utilizado para logon.](https://sankhyasd.zendesk.com/hc/article_attachments/360042445014/embim88.gif)
