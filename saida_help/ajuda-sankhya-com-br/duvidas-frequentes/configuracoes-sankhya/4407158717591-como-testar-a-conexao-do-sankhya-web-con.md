---
id: "4407158717591"
titulo: "Como testar a conexão do Sankhya Web Connection com a balança?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4407158717591-Como-testar-a-conex%C3%A3o-do-Sankhya-Web-Connection-com-a-balan%C3%A7a"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-08-31T19:28:10Z"
rotulos: ["Configuração", "Integração", "Balança", "Teste", "#validadoSilvio", "Teste de Conexão com a Balança", "Artigo atualizado KCS", "Produção - KCS", "WebConnection"]
---

# Como testar a conexão do Sankhya Web Connection com a balança?

A integração com balanças por meio do **WebConnection** permite a leitura automática dos dados de pesagem que a balança encaminha diretamente para o sistema, conforme imagem abaixo:

![Imagem 1: A integração com balanças por meio do WebConnection permite a leitura automática dos dados de pesagem que a balança…](https://ajuda.sankhya.com.br/hc/article_attachments/39890264454423)

Com a configuração realizada dentro do **WebConnection**, aba Integração Balança, é possível verificar através do botão **"Testar (obter peso)"**, dessa forma é apresentado o pop-up com a leitura realizada.

**Importante:**

Há alguns cenários onde pode ser apresentado erros durante o teste, conforme imagem abaixo:

![Imagem 2: Há alguns cenários onde pode ser apresentado erros durante o teste, conforme imagem abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/39890276004631)

Desta forma, temos uma outra validação:

Para validar se o **"Sankhya Web Connection"** está comunicando corretamente com a balança via porta serial, siga estes passos adicionais:

**(1)**  Na estação configurada, abra um navegador e cole o link: [**https://monitoramento-d8326.web.app/wc.html**](https://monitoramento-d8326.web.app/wc.html)

**(2)** Se as configurações estiverem corretas, aparecerá a mensagem: **"Mensagem recebida WC:**

**{"comando":"GET\_PESO","peso":"0.00"}"**. No parâmetro de peso, trará o peso que o **WebConnection** está recebendo da balança.

![Imagem 3: {"comando":"GET_PESO","peso":"0.00"}" . No parâmetro de peso, trará o peso que o WebConnection está recebendo da…](https://ajuda.sankhya.com.br/hc/article_attachments/39890264455831)

**(3)** Se aparecer **"peso":"-1"**, verifique as configurações da balança **(Porta COM, Frequência de Transmissão, Databits, Stopbits e Paridade)** no **"Web Connection"**.

**Observação:** É necessário validar as configurações de comunicação da balança, como **Porta COM, Frequência de Transmissão (baud rate), Data Bits, Stop Bits e Paridade**, conforme especificações do manual da balança, disponibilizado pelo fabricante ou pelo próprio cliente.

Para que a balança se comunique corretamente com o **WebConnection**, é imprescindível que esteja configurada com o protocolo de transmissão contínua (envio automático e constante de dados). Essa configuração também pode ser confirmada no manual do equipamento.
