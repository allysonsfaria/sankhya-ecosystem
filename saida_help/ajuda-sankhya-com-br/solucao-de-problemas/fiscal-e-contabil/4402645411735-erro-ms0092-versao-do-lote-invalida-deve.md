---
id: "4402645411735"
titulo: "Erro MS0092 - Versão do lote inválida. Deve ser utilizada a versão 1.05.01"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4402645411735-Erro-MS0092-Vers%C3%A3o-do-lote-inv%C3%A1lida-Deve-ser-utilizada-a-vers%C3%A3o-1-05-01"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:24:16Z"
rotulos: ["Configuração", "NF-e", "XML", "Atualização", "Ticket99769", "#autorizadoCláudia", "eSocial", "Atualize o sistema", "Erro MS0092 versão inválida", "Concorrência entre serviços", "Erro"]
---

# Erro MS0092 - Versão do lote inválida. Deve ser utilizada a versão 1.05.01

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16342171366807) MENSAGEM:**

[Erro MS0092] - Versão do lote inválida. Deve ser utilizada a versão 1.05.01.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16342186752279) SOLUÇÃO:**

Primeiramente pedimos a todos os clientes que estejam com a versão do sistema atualizada.
Versões mais recentes disponíveis no site: [http://downloads.sankhya.com.br/versoes-anteriores](https://ajuda.sankhya.com.br/hc/pt-br/articles/Downloads%20Sankhya%20)

- 4.8b271
- 4.7b640
- 4.6b755

Realize todas as configurações abaixo para correção do erro:

![Imagem 3: Ligue os parâmetros "ATVREINFSKW" e "DEBUGREINFSKW" (a ativação desses parâmetros é para o sistema deixar de usar o…](https://ajuda.sankhya.com.br/hc/article_attachments/16342171370519) Ligue os parâmetros **"ATVREINFSKW"** e **"DEBUGREINFSKW"** (a ativação desses parâmetros é para o sistema deixar de usar o San-Esocial e passar a usar o San-NFe para comunicar os dados do Reinf com a receita).

![Imagem 4: Acesse a tela Configurações » Avançado » Preferências e desligue o parâmetro "FPSANREINFEXE" .](https://ajuda.sankhya.com.br/hc/article_attachments/16342186756119) Acesse a tela Configurações » Avançado » Preferências e desligue o parâmetro **"FPSANREINFEXE"**.

![Imagem 5: Acesse a tela Configurações » Avançado » Preferências e desligue o parâmetro "FPSANREINFEXE" .](https://ajuda.sankhya.com.br/hc/article_attachments/15080452512535)

![Imagem 6: Em seguida, acesse o servidor no qual está instalado o San-Esocial, pare o serviço (com isto o san-eSocial deixará de…](https://ajuda.sankhya.com.br/hc/article_attachments/16342186762263) Em seguida, acesse o servidor no qual está instalado o San-Esocial, pare o serviço (com isto o san-eSocial deixará de olhar para os eventos do Reinf).

![Imagem 7: Reinicie o Sankhya-Om .](https://ajuda.sankhya.com.br/hc/article_attachments/16342171375511) Reinicie o **Sankhya-Om**.

![Imagem 8: Reinicie o Sankhya-Om .](https://ajuda.sankhya.com.br/hc/article_attachments/15080474977431)

![Imagem 9: O certificado digital deverá ser cadastrado na tela "Console NF-e" dentro do SankhyaOm , para que o sistema consiga…](https://ajuda.sankhya.com.br/hc/article_attachments/16342186768663) O certificado digital deverá ser cadastrado na tela **"Console NF-e"** dentro do **SankhyaOm**, para que o sistema consiga assinar os arquivos XML.

![Imagem 10: Na tela de geração do Reinf foi criado o campo 'Versão do layout" no qual ao cadastrar a referência 01/05/2021 deverá…](https://ajuda.sankhya.com.br/hc/article_attachments/16342171379351) Na tela de geração do Reinf foi criado o campo **'Versão do layout"** no qual ao cadastrar a referência 01/05/2021 deverá estar selecionado com a versão '1.05.01-Após Junho/2021'.

![Imagem 11: Depois de realizar as novas configurações, antes de gerar novamente o evento, efetue a limpeza do cachê do sistema e do…](https://ajuda.sankhya.com.br/hc/article_attachments/16342186774807) Depois de realizar as novas configurações, antes de gerar novamente o evento, efetue a limpeza do cachê do sistema e do navegador.

![Imagem 12: Vá até a aba do evento que está aguardando correção, clique em gerar e envie novamente para sistema conseguir comunicar…](https://ajuda.sankhya.com.br/hc/article_attachments/16342186775703) Vá até a aba do evento que está aguardando correção, clique em gerar e envie novamente para sistema conseguir comunicar os dados.

**![Imagem 13: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16342186778263) OBSERVAÇÃO:**

Lembrando que os parâmetros **"ATVREINFSKW"** e **"DEBUGREINFSKW"** devem estar habilitados.

**![Imagem 14: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16342186779799)CAUSA:**

Identificamos que o 'Erro MS0092' está sendo causando por concorrência entre o serviço do San-eSocial com o Reinf Embarcado.
