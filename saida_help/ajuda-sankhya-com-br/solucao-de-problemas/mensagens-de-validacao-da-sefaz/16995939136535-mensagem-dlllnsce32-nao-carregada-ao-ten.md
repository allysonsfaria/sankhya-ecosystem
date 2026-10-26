---
id: "16995939136535"
titulo: "Mensagem \"DlllnscE32 não carregada\" ao tentar cadastrar um parceiro no FAST ou Mitra"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/16995939136535-Mensagem-DlllnscE32-n%C3%A3o-carregada-ao-tentar-cadastrar-um-parceiro-no-FAST-ou-Mitra"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:54:03Z"
rotulos: ["Configuração", "Parceiro", "Fast Service", "Sintegra", "Falta DLL Sintegra", "Baixar DLL validação", "Copiar DLL para SysWOW64", "Erro"]
---

# Mensagem "DlllnscE32 não carregada" ao tentar cadastrar um parceiro no FAST ou Mitra

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16995928002199) **MENSAGEM:**

"DlllnscE32 não carregada".

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16995953391511)CAUSA:**

Falta da DLL de comunicação/validação de IE do Sintegra.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16995967853463)SOLUÇÃO:**

Acessar o site do Sintegra(<http://www.sintegra.gov.br/>) e conferir se o CNPJ e IE do parceiro estão válidos:

![Imagem 4: Acessar o site do Sintegra( http://www.sintegra.gov.br/ ) e conferir se o CNPJ e IE do parceiro estão válidos:](https://ajuda.sankhya.com.br/hc/article_attachments/16995654468759)

Validado os dados do parceiro, ainda no site do Sintegra, acesse o menu serviços e clique em download:

![Imagem 5: Validado os dados do parceiro, ainda no site do Sintegra, acesse o menu serviços e clique em download:](https://ajuda.sankhya.com.br/hc/article_attachments/19257992730903)

![Imagem 6: Validado os dados do parceiro, ainda no site do Sintegra, acesse o menu serviços e clique em download:](https://ajuda.sankhya.com.br/hc/article_attachments/19258031680791)

Localizar o tópico "Módulo para verificar a consistência das Inscrições Estaduais" e baixar a DLL de validação de Inscrições Estaduais:

![Imagem 7: Localizar o tópico "Módulo para verificar a consistência das Inscrições Estaduais" e baixar a DLL de validação de…](https://ajuda.sankhya.com.br/hc/article_attachments/19257992755863)

Faça o download, extraia e pegue apenas o arquivo "DllInscE32.dll". Feche o sistema(Mitra/Fast Service) e copie o arquivo para a pasta C:\Windows\SysWOW64 ou para a pasta de instalação do sistema.
 
Feito isto abra o sistema e tente realizar o cadastro novamente.
