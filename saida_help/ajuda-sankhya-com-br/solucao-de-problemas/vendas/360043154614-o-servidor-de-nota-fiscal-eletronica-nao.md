---
id: "360043154614"
titulo: "O servidor de nota fiscal eletrônica não está ativo "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043154614-O-servidor-de-nota-fiscal-eletr%C3%B4nica-n%C3%A3o-est%C3%A1-ativo"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:03:54Z"
rotulos: ["ERRONF", "Configuração", "Fast Service", "NF-e", "Servidor", "Mensagem: Servidor de NF-e inativo", "Recomendado para usuário com conhecimento em T.I", "Verifique e inicie o serviço \"sannfe-service\" no servidor", "Erro", "Documentos Eletrônicos"]
---

# O servidor de nota fiscal eletrônica não está ativo 

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16134463147031) MENSAGEM:**

O servidor de nota fiscal eletrônica não está ativo.

**![Imagem 2: SOLUÇÃO](https://ajuda.sankhya.com.br/hc/article_attachments/16134499959959) SOLUÇÃO**

![Imagem 3: Verifique o IP de instalação do servidor de nota fiscal eletrônica:](https://ajuda.sankhya.com.br/hc/article_attachments/16134463148567) Verifique o IP de instalação do servidor de nota fiscal eletrônica:

**Mitra:**

**(2)** Acesse o sistema pelo usuário SUP e/ou usuário com acesso a rotina abaixo:

**(2)** Avançado » Preferências » Todas as Preferências » CHAVE **"IPSERVNFE"**

**(2)** Botão Direito na Tela » Expandir nível 3 » Visualize o IP configurado.

**Fast Service:**

**(2)** Acesse o FAST pelo usuário SUP, busque pelo caminho Utilitários » **DBEExplorer** e execute o comando SELECT \* FROM TSIPAR WHERE CHAVE='IPSERVNFE'

**(2)** O IP será apresentado com um duplo clique na coluna 'Texto'.

![Imagem 4: Localizado o IP acima, acesse a máquina correspondente ao mesmo para iniciar o Servidor de Nota Fiscal Eletrônica.](https://ajuda.sankhya.com.br/hc/article_attachments/16134463150103) Localizado o IP acima, acesse a máquina correspondente ao mesmo para iniciar o Servidor de Nota Fiscal Eletrônica.

![Imagem 5: Caso trate-se de um servidor de nota fiscal eletrônica Windows :](https://ajuda.sankhya.com.br/hc/article_attachments/16134463150743) Caso trate-se de um servidor de nota fiscal eletrônica **Windows**:

**(2)** No Menu Iniciar da máquina buscar por **"services.msc"**:

**(2)** Aberto o services, busque do lado direito pelo serviço **"sannfe-service"**, conforme abaixo:

![Imagem 6: (2) Aberto o services, busque do lado direito pelo serviço "sannfe-service" , conforme abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/14632966755479)

**(2)** Possivelmente a coluna STATUS estará em branco e do lado direito estará habilitado a opção **"Inicia o serviço"**. Clique em Iniciar e aguarde que a inicialização seja concluída.

**(2)** Atualize o services (botão atualizar na barra de ferramentas) e verifique se o STATUS passou a ser apresentado com a informação "Em execução".

**(2)** Em caso positivo, teste uma nova emissão.

![Imagem 7: Caso trate-se de um servidor de nota fiscal eletrônica Linux :](https://ajuda.sankhya.com.br/hc/article_attachments/16134499965591) Caso trate-se de um servidor de nota fiscal eletrônica **Linux**:

**(2)** Através do aplicativo putty, acesse o IP do servidor de nota fiscal eletrônica pelo usuário mgeweb

**(2)** Localize a pasta do sannfe (normalmente na pasta home/mgeweb) e execute o comando: **./sannfe-service start**

**![Imagem 8: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17803876062743) IMPORTANTE:**

**(2)** Recomenda-se que o procedimento acima seja realizado por um usuário da empresa com conhecimento na infra/T.I.

**(2)** A princípio essa situação pode ocorrer apenas para sistema da Linha DELPH (Mitra), visto que para a Linha W esse serviço não precisa estar iniciado.
