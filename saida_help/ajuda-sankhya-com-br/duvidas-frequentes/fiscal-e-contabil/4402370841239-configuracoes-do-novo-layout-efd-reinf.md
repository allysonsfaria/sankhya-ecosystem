---
id: "4402370841239"
titulo: "Configurações do novo Layout EFD-Reinf"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4402370841239-Configura%C3%A7%C3%B5es-do-novo-Layout-EFD-Reinf"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:24:18Z"
rotulos: ["Configuração", "Fiscal", "XML", "EFD", "Preferências", "#validadojenifer", "EFD-Reinf: Versão 1.05.01 enviar eventos", "Preferências logs reinicialização", "Certificado digital: Cadastro no Console NFe", "Documentos Eletrônicos"]
---

# Configurações do novo Layout EFD-Reinf

Recentemente nós tivemos uma atualização do EFD-Reinf  para o novo layout, porém, depois de atualizado para as versões do site que já contemplam este layout é necessário fazer algumas configurações:

Depois de  atualizar o sistema, siga os seguintes passos necessários:

![Imagem 1: Acesse a tela de "Preferências" em Configurações » Avançado » Preferências Ligue os parâmetros:](https://ajuda.sankhya.com.br/hc/article_attachments/16342025251735) Acesse a tela de **"Preferências"** em Configurações » Avançado » Preferências
Ligue os parâmetros:

**ATVREINFSKW**-Ativa o Reinf embarcardo?: ligado

**DEBUGREINFSKW**-Ativa os logs do Reinf embarcardo?: ligado

![Imagem 2: Acesse a tela de "Administração do Servidor" (Caminho de acesso: Configurações » Avançado » Administração do Servidor)…](https://ajuda.sankhya.com.br/hc/article_attachments/16342025254679) Acesse a tela de **"Administração do Servidor"** (Caminho de acesso:  Configurações » Avançado » Administração do Servidor), aba: **"Geral"**, opção: **"Reinicializar Sistema"**
Assim que ligar esses parâmetros será necessário reiniciar o **SankhyaOm**. Isso é preciso, pois nesta versão 1.05.01 o Reinf não usará mais o San-Esocial, somente o San-NFe.

![Imagem 3: Acesse a tela "Console NFe" em: Comercial » Configuração » Console NFe](https://ajuda.sankhya.com.br/hc/article_attachments/16342041827991) Acesse a tela **"Console NFe"** em: Comercial » Configuração » Console NFe

O certificado digital deverá ser cadastrado na tela Console NF-e dentro do **Sankhya Om**, para que o sistema consiga assinar os arquivos XML.

![Imagem 4: Acesse a tela "Reinf" em: Livros Fiscais » Conexão » Reinf » EFD - Reinf](https://ajuda.sankhya.com.br/hc/article_attachments/16342041829527) Acesse a tela **"Reinf"** em: Livros Fiscais » Conexão » Reinf » EFD - Reinf

Na tela de geração do Reinf foi criado o campo **"Versão do layout"** no qual ao cadastrar a referência 01/05/2021 deverá estar selecionado com a versão "1.05.01-Após Junho/2021"

![Imagem 5: Na tela de geração do Reinf foi criado o campo "Versão do layout" no qual ao cadastrar a referência 01/05/2021 deverá…](https://ajuda.sankhya.com.br/hc/article_attachments/4402389237143)

![Imagem 6: Vá até a aba do evento que está aguardando a correção, clique em gerar e envie novamente para o sistema conseguir…](https://ajuda.sankhya.com.br/hc/article_attachments/16342041832855) Vá até a aba do evento que está aguardando a correção, clique em gerar e envie novamente para o sistema conseguir comunicar os dados.
