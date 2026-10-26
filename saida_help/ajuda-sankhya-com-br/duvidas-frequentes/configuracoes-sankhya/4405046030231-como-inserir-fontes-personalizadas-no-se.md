---
id: "4405046030231"
titulo: "Como inserir fontes personalizadas no servidor de aplicação Wildfly?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4405046030231-Como-inserir-fontes-personalizadas-no-servidor-de-aplica%C3%A7%C3%A3o-Wildfly"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T15:22:51Z"
rotulos: ["Configuração", "Relatórios", "IReport", "Wildfly", "Inserindo Fontes no Wildfly", "Fontes"]
---

# Como inserir fontes personalizadas no servidor de aplicação Wildfly?

O servidor de aplicação Wildfly contém o pacote de fontes nativas para sua utilização, mas em algum momento ou relatório específico é necessário realizar a inclusão de alguma fonte. Neste tutorial serão apresentadas as funcionalidades que ajudarão nesta inclusão.

![Imagem 1: Acesse o iReport para inclusão da fonte no seguinte caminho:](https://ajuda.sankhya.com.br/hc/article_attachments/16369725516695) Acesse o iReport para inclusão da fonte no seguinte caminho:

Ferramentas » Opções » Fonts » Install Font

![Imagem 2: Ferramentas » Opções » Fonts » Install Font](https://ajuda.sankhya.com.br/hc/article_attachments/4405039059863)

Em TrueType Font clique Browse e selecione a fonte desejada.

![Imagem 3: Em TrueType Font clique Browse e selecione a fonte desejada.](https://ajuda.sankhya.com.br/hc/article_attachments/4405045717527)

Clique em próximo > Family Name, defina o nome da fonte e marque a opção 'Embed this font in the PDF document'

![Imagem 4: Clique em próximo > Family Name, defina o nome da fonte e marque a opção 'Embed this font in the PDF document'](https://ajuda.sankhya.com.br/hc/article_attachments/4405045757335)

Finalize.

![Imagem 5: Gere o arquivo.jar da fonte, acesse novamente Ferramentas » Opções » Fonts e selecione a fonte importada no passo 2 e…](https://ajuda.sankhya.com.br/hc/article_attachments/16369756632983) Gere o arquivo.jar da fonte, acesse novamente Ferramentas » Opções » Fonts e selecione a fonte importada no passo 2 e clique em 'Export as extension':

![Imagem 6: Gere o arquivo.jar da fonte, acesse novamente Ferramentas » Opções » Fonts e selecione a fonte importada no passo 2 e…](https://ajuda.sankhya.com.br/hc/article_attachments/4405045777175)

Salve no formato nome\_da\_fonte.jar

![Imagem 7: Salve no formato nome_da_fonte.jar](https://ajuda.sankhya.com.br/hc/article_attachments/4405039221015)

![Imagem 8: Acesse a pasta de instalação do wildfly_producao, no seguinte caminho, de acordo com seu sistema operacional:](https://ajuda.sankhya.com.br/hc/article_attachments/16369725532055) Acesse a pasta de instalação do wildfly\_producao, no seguinte caminho, de acordo com seu sistema operacional:

/wildfly\_producao/modules/custom/net/sf/jaspereports/fonts/main/

e inclua o arquivo criado .jar

![Imagem 9: e inclua o arquivo criado .jar](https://ajuda.sankhya.com.br/hc/article_attachments/4405039266199)

Edite o arquivo modulo.xml conforme exemplo abaixo:

<?xml version="1.0" encoding="UTF-8"?>
<module xmlns="urn:jboss:module:1.1" name="custom.net.sf.jasperreports.fonts">
<resources>
<resource-root path="skw-ireport-pdf-fonts.jar"/>
<resource-root path="nome\_da\_fonte.jar"/>
</resources>
<dependencies>
</dependencies>
</module>

**![Imagem 10: OBSERVAÇÃO: altere de acordo com o nome criado na extensão .jar e repita o processo para outras bases (Teste ou Treina)](https://ajuda.sankhya.com.br/hc/article_attachments/16369725536151) OBSERVAÇÃO:** altere de acordo com o nome criado na extensão .jar e repita o processo para outras bases (Teste ou Treina)

Salve o arquivo.

![Imagem 11: Reinicie o Wildfly para carregar as alterações.](https://ajuda.sankhya.com.br/hc/article_attachments/16369725540247) Reinicie o Wildfly para carregar as alterações.

![Imagem 12: Faça as alterações no arquivo jrxml para a fonte criada e substitua o relatório dentro do Sankhya-W.](https://ajuda.sankhya.com.br/hc/article_attachments/16369756661399) Faça as alterações no arquivo jrxml para a fonte criada e substitua o relatório dentro do Sankhya-W.

Ireport:

![Imagem 13: Ireport:](https://ajuda.sankhya.com.br/hc/article_attachments/4405039371543)

**Sankhya-W**

![Imagem 14: Sankhya-W](https://ajuda.sankhya.com.br/hc/article_attachments/4405045957527)
