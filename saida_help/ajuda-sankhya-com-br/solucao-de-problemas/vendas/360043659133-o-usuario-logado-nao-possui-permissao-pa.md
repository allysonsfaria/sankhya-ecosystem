---
id: "360043659133"
titulo: "O usuário logado não possui permissão para exportar o XML."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043659133-O-usu%C3%A1rio-logado-n%C3%A3o-possui-permiss%C3%A3o-para-exportar-o-XML"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-08-01T01:10:57Z"
rotulos: ["CT-e", "Configuração", "Segurança", "Portal de Vendas", "XML", "ECOM_E00023", "Ajuste permissões em \"Segurança\" do usuário", "Erro ocorre por falta de permissão específica", "Usuário sem permissão para exportar XML", "Erro", "Artigo atualizado KCS", "CVE - KCS"]
---

# O usuário logado não possui permissão para exportar o XML.

**Mensagem**

[ECOM\_E00023] O usuário logado não possui permissão para exportar o XML.

**Situação**

Ao tentar exportar um arquivo XML, como por exemplo ao gerar o XML do CT-e pelo **"Portal de Vendas"** (Comercial >> Consulta >> Portal de Vendas) ou realizar o download de arquivos XML de notas fiscais, o sistema apresenta a mensagem de erro informando que o usuário não possui permissão para realizar esta operação.

**Solução**

Para resolver o problema, configure as permissões necessárias no cadastro do usuário seguindo os passos abaixo:

**(1)** Acesse a tela **"Usuários"** (Configurações >> Controle de Acesso >> Usuários).

**(2)** Localize e selecione o usuário que está enfrentando o problema de exportação.

**(3)** Acesse a aba **"Segurança"** no cadastro do usuário.

**(4)** Localize o campo **"Permite exportar relatórios?"** e marque esta opção para ativar a permissão.

**(5)** Localize o campo **"Pode Imprimir/Reimprimir Nota nas Centrais"** e marque esta opção para ativar a permissão.
![Imagem 1: (1) Acesse a tela "Usuários" (Configurações >> Controle de Acesso >> Usuários). (2) Localize e selecione o usuário que…](https://ajuda.sankhya.com.br/hc/article_attachments/14661315046167)

**(6)** Clique no **"Botão Salvar"** para confirmar as alterações realizadas.

**(7)** Solicite ao usuário que saia do sistema e faça login novamente para que as novas permissões sejam aplicadas.

**(8)** Teste a funcionalidade tentando novamente exportar o XML para verificar se o problema foi resolvido.

**Observações importantes:**

- Esta configuração é feita por usuário, sendo necessário repetir o processo para cada usuário que necessitar desta permissão.
- A permissão **"Permite exportar relatórios?"** afeta não apenas a exportação de XML, mas também a exportação de relatórios em geral.
- Se o problema persistir após seguir estes passos, verifique se o usuário possui todas as outras permissões necessárias para acessar a funcionalidade específica, como permissões na tela de CT-e ou nas centrais de vendas.
- Quando utilizado via navegador Google Chrome, pode ser necessário também habilitar a opção de conteúdo não seguro nas configurações do navegador, alterando de "Bloqueado" para "Permitir".

**Causa**

O erro ocorre porque o usuário que está tentando realizar a operação de exportação de XML não possui as permissões necessárias configuradas no sistema. Especificamente, faltam as permissões de **"Permite exportar relatórios?"** e **"Pode Imprimir/Reimprimir Nota nas Centrais"** na aba de **"Segurança"** do cadastro do usuário.
