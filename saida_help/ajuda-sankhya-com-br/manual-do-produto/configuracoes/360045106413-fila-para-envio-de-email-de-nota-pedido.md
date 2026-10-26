---
id: "360045106413"
titulo: "Fila para envio de email de nota/pedido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106413-Fila-para-envio-de-email-de-nota-pedido"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-08-24T12:57:25Z"
rotulos: ["manual", "HTML", "Configuração", "Parceiro", "XML", "Nota", "Data de entrada", "email", "email de XML", "Fila para envio de email de nota/pedido", "Pedido", "br.com.sankhya.bim.filaenvioemailnotapedido", "Fila para envio de email de Nota/Pedido manual", "Financeiro", "Gerenciamento Eficiente de E-mails de Notas/Pedidos", "Erro"]
---

# Fila para envio de email de nota/pedido

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310867866391) Módulo: Configurações > Avançado > Envio de Mensagens
```

---

Esta tela apresentará os dados, de um pedido/nota, enviados por e-mail, em que você poderá visualizar se o e-mail de XML foi ou não enviado.

![Imagem 2: Esta tela apresentará os dados, de um pedido/nota, enviados por e-mail, em que você poderá visualizar se o e-mail de…](https://ajuda.sankhya.com.br/hc/article_attachments/360082960853)

Você também poderá utilizar os Filtros disponíveis na tela para encontrar o(s) e-mail(s) desejados, desse modo, teremos a seção **"Status"** em que pode-se filtrar os e-mails por:

- Pendente de envio;
- Em processo de envio;
- Erro de envio; e
- Enviadas.

Se você desejar filtrar todos os status basta marcar a opção **"Status"**.

Assim como por **"Período de Entrada"**, **"Email"**, **"Parceiro"**, **"Número Único Financeiro"**, **"Número Nota"** e **"Nosso Número"**.

Tem-se ainda que no topo da tela teremos os botões:

![Imagem 3: Navegação : Por meio desses botões, você poderá passar dentre os e-mails que foram filtrados na tela.](https://ajuda.sankhya.com.br/hc/article_attachments/16275091233815) **Navegação**: Por meio desses botões, você poderá passar dentre os e-mails que foram filtrados na tela.

![Imagem 4: Atualizar : Este atualizará as informações da tela.](https://ajuda.sankhya.com.br/hc/article_attachments/16275065029143) **Atualizar**: Este atualizará as informações da tela.

![Imagem 5: Exportar : Aqui pode-se exportar a grade para PDF, tem-se ainda as opções "Exportar para PDF" , "Exportar para…](https://ajuda.sankhya.com.br/hc/article_attachments/16647442041623) **Exportar**: Aqui pode-se exportar a grade para PDF, tem-se ainda as opções **"Exportar para PDF"**, **"Exportar para planilha"** e **"Exportar para cubo"**.

![Imagem 6: Agendar : No pop up exibido ao pressionar este botão, informe o tempo em minutos para que a tela faça uma atualização…](https://ajuda.sankhya.com.br/hc/article_attachments/16275091249943) **Agendar**: No pop up exibido ao pressionar este botão, informe o tempo em minutos para que a tela faça uma atualização automática de seus dados.

**Nota:** caso você informe zeros, a tela não será atualizada automaticamente.

![Imagem 7: Reenviar : Este irá reenviar os e-mails marcados na grade por meio da opção de seleção.](https://ajuda.sankhya.com.br/hc/article_attachments/16275091256599) **Reenviar**: Este irá reenviar os e-mails marcados na grade por meio da opção de seleção.

Ao selecionar o e-mail, será possível verificar no campo localizado logo abaixo o corpo da mensagem. Caso seja necessário, o usuário ainda poderá clicar no botão **"Ver mensagem em HTML"** para que a mesma seja apresentada neste formato. Ao lado é possível verificar o anexo do e-mail e para baixá-lo, basta clicar no botão **"Baixar anexo"** e salvá-lo no local de sua preferência.

![Imagem 8: Ao selecionar o e-mail, será possível verificar no campo localizado logo abaixo o corpo da mensagem. Caso seja…](https://ajuda.sankhya.com.br/hc/article_attachments/360082978933)

Os e-mails que tiveram sucesso de envio serão apresentados na grade na cor **verde**, os que estão pendentes de envio na cor **amarela** e os que tiveram algum erro de envio são apresentados na cor **vermelha**.

Além disso, no filtro Status existe uma legenda indicando a que se refere cada cor, sendo:

- **Pendentes de envio:** ![clip3016](https://ajuda.sankhya.com.br/hc/article_attachments/360060976874)Amarelo;
- **Erro de Envio:** ![clip3017](https://ajuda.sankhya.com.br/hc/article_attachments/360061907453)Vermelho;
- **Enviadas:** ![clip3018](https://ajuda.sankhya.com.br/hc/article_attachments/360060976894) Verde.

**Nota:** a medida que os e-mails vão sendo enviados, os arquivos de anexos vão sendo gerados e armazenados internamente no sistema. Estes arquivos são desnecessários a partir de um certo momento para o sistema e consomem um espaço significativo no disco. No parâmetro **"Dias p/ vencimento de arquivos temporários - DIASVENCTFILE"** informe o tempo que o arquivo ficará armazenado internamente. Após este período, ele será excluído para não ocupar espaço desnecessariamente.

#### Erro no Envio de E-mail

Quando o sistema não conseguir enviar uma mensagem do tipo e-mail, contendo documentos do tipo boleto e nota, uma mensagem de alerta será enviada ao usuário que comandou o envio.

Após 3 tentativas de envio de e-mail sem sucesso, o status do envio da mensagem é alterado para **"Erro: não enviado"**. Além disto, o sistema grava essa mensagem de erro no banco de dados e emite um alerta na tela para o usuário que tentou enviar a mensagem, estando este logado ou não, informando que a mensagem não foi enviada. Tem-se o exemplo:

**"A mensagem de e-mail para <EMAIL> com assunto <ASSUNTO> não pôde ser entregue, verifique"**

**Observação:** caso não esteja logado no sistema e sua mensagem não tenha sido enviada, quando ele logar a mensagem será exibida nas notificações do sistema.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106413-Fila-para-envio-de-email-de-nota-pedido#top)
