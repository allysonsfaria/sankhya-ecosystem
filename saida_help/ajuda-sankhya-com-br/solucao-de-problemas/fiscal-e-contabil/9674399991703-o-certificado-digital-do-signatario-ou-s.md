---
id: "9674399991703"
titulo: "O certificado digital do signatário ou solicitante da informação encontra-se expirado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9674399991703-O-certificado-digital-do-signat%C3%A1rio-ou-solicitante-da-informa%C3%A7%C3%A3o-encontra-se-expirado"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:06:50Z"
rotulos: ["Configuração", "Eventos", "Fiscal", "NF-e", "SEFAZ", "MS00006", "Certificado digital expirado do signatário.", "Desligue parâmetro \"FPSANREINFEXE\" e reinicie o sistema.", "Verifique vencimento na tela \"Console NF-e\".", "Certificado Digital"]
---

# O certificado digital do signatário ou solicitante da informação encontra-se expirado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16778404464663) MENSAGEM:**

[Erro MS00006]: O certificado digital do signatário ou solicitante da informação encontra-se expirado.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16778412280471) SITUAÇÃO:**

Ao transmitir os eventos a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16778412283159) SOLUÇÃO:**

![Imagem 4: Verifique se o certificado digital está configurado com o novo vencimento na tela "Console NF-e" (Caminho de acesso à…](https://ajuda.sankhya.com.br/hc/article_attachments/16778404476311) Verifique se o certificado digital está configurado com o novo vencimento na tela **"Console NF-e"** (Caminho de acesso à tela: Comercial » Configuração » Console NFe), segue abaixo o manual da tela para mais informações.

**(1)** [Console NFe – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597734-Console-NFe)

![Imagem 5: Também acesse a tela "Preferências" (Caminho de acesso: Configurações » Avançado » Preferências), informe o parâmetro…](https://ajuda.sankhya.com.br/hc/article_attachments/16778404486039) Também acesse a tela **"Preferências"** (Caminho de acesso: Configurações » Avançado » Preferências), informe o parâmetro **"FPSANREINFEXE"** e observe se ele está ligado, caso esteja, desligue-o. Feito isso, envie novamente o fechamento REINF.

![Imagem 6: Também acesse a tela "Preferências" (Caminho de acesso: Configurações » Avançado » Preferências), informe o parâmetro…](https://ajuda.sankhya.com.br/hc/article_attachments/16778412298391)

![Imagem 7: Feito isso, reinicie o sistema através da tela " Administração do Servidor" (Caminho de acesso: Configurações »…](https://ajuda.sankhya.com.br/hc/article_attachments/16778404490391) Feito isso, reinicie o sistema através da tela **"Administração do Servidor"** (Caminho de acesso: Configurações » Avançado » Administração do Servidor)

![Imagem 8: Feito isso, reinicie o sistema através da tela " Administração do Servidor" (Caminho de acesso: Configurações »…](https://ajuda.sankhya.com.br/hc/article_attachments/16778404491415)

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16778412305943) CAUSA:**

Ocorre quando o certificado não está válido ou não foi inserido corretamente ou quando o parâmetro FPSANREINFEXE está ligado.
