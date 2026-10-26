---
id: "360044110074"
titulo: "Não foi possível ler o caminho do BDE no registro do Windows"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110074-N%C3%A3o-foi-poss%C3%ADvel-ler-o-caminho-do-BDE-no-registro-do-Windows"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:53:56Z"
rotulos: ["Configuração", "Registro", "Erro de Leitura do Caminho do BDE no Registro do Windows", "Erro", "Windows", "Permissões"]
---

# Não foi possível ler o caminho do BDE no registro do Windows

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16948890809367) MENSAGEM:**

Não foi possível ler o caminho do BDE no registro do Windows
Chave KEY\_LOCAL\_MACHINE\SOFTWARE[\WOW6432NODE]\Borland\Database Engine

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16948890799895) SITUAÇÃO:**

Ao tentar acessar o MGE/MITRA, ocorre a mensagem:

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16948890820759) CAUSA:**

Ocorre quando os usuários não possuem permissões mínimas para gravar dados executados pelo BDE.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16948931761431) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 5: Com o usuário Administrador do Sistema Operacional Windows, pesquise pela palavra 'Executar' ou aperte o botão do…](https://ajuda.sankhya.com.br/hc/article_attachments/16948931766935) Com o usuário Administrador do Sistema Operacional Windows, pesquise pela palavra 'Executar' ou aperte o botão do teclado 'Windows + R'. Acesse: Executar [Abrira um pop-up]

![Imagem 6: Com o usuário Administrador do Sistema Operacional Windows, pesquise pela palavra 'Executar' ou aperte o botão do…](https://ajuda.sankhya.com.br/hc/article_attachments/360063053313)

Digite 'regedit' e clique em OK.

Navegue ate o caminho:

KEY\_LOCAL\_MACHINE\SOFTWARE\Borland\Database Engine [**Para Sistema 32 Bits**]

KEY\_LOCAL\_MACHINE\SOFTWARE\WOW6432Node\Borland\Database Engine [**Para sistema 64 Bits**]

**Exemplo:**

![Imagem 7: Exemplo:](https://ajuda.sankhya.com.br/hc/article_attachments/360062172514)

Em Nomes de Grupo ou de Usuário adicione Administradores, depois os Usuários que utilizarão o sistema e, em Permissões, marque todas as opções da coluna Permitir, aplique e clique em OK.

![Imagem 8: Em Nomes de Grupo ou de Usuário adicione Administradores, depois os Usuários que utilizarão o sistema e, em Permissões,…](https://ajuda.sankhya.com.br/hc/article_attachments/360063053333)

**![Imagem 9: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16948931778327) OBSERVAÇÃO:**

Este procedimento geralmente é executado pela Equipe de TI da Empresa, que possui permissões de **Administrador**.
