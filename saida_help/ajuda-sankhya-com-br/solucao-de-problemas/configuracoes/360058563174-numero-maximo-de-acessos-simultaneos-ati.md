---
id: "360058563174"
titulo: "Número máximo de acessos simultâneos atingido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360058563174-N%C3%BAmero-m%C3%A1ximo-de-acessos-simult%C3%A2neos-atingido"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:26:26Z"
rotulos: ["Configuração", "Empresa", "Usuários", "OS criaçao 772829", "testadoroger", "atualizadoroger", "CORE_E01435", "Controle de Acesso", "Erro de Número Máximo de Acessos Simultâneos Atingido", "Erro"]
---

# Número máximo de acessos simultâneos atingido

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16273328083223) MENSAGEM:**

[CORE\_E01435] Número máximo de acessos simultâneos atingido.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16273318627991) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse o cadastro de usuários em: Configurações » Controle de Acesso » Usuários Aba: "Identificação" Campo "Empresa" :…](https://ajuda.sankhya.com.br/hc/article_attachments/16273318630807) Acesse o cadastro de usuários em: Configurações » Controle de Acesso » Usuários
Aba: **"Identificação"**
Campo **"Empresa"**: verifique o código da empresa vinculado ao usuário

![Imagem 4: Acesse o cadastro de usuários em: Configurações » Controle de Acesso » Usuários Aba: "Identificação" Campo "Empresa" :…](https://ajuda.sankhya.com.br/hc/article_attachments/14660830848407)

![Imagem 5: Acesse a tela "Empresas" (Caminho de acesso: Configurações » Cadastros » Empresas ):](https://ajuda.sankhya.com.br/hc/article_attachments/16273318631959) Acesse a tela [**"Empresas"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas) (Caminho de acesso: Configurações » Cadastros » Empresas):

No campo **"Quantidade de usuários logados simultaneamente"**, realize a limitação do número de conexões **"por empresa"** no SankhyaOM.
Depois de configurado este campo, sendo feita a tentativa de acesso ao sistema com um número de usuários (conforme a empresa do usuário logado) que seja superior ao aqui estipulado, será apresentada a mensagem.

![Imagem 6: No campo "Quantidade de usuários logados simultaneamente" , realize a limitação do número de conexões "por empresa" no…](https://ajuda.sankhya.com.br/hc/article_attachments/14660950393623)

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16273318633751) CAUSA:**

Essa mensagem é resultante da Quantidade de Acessos Simultâneos configurada no Cadastro de Empresas (Configurações » Cadastros » Empresas), campo: Quantidade de usuários logados simultaneamente, de acordo com a empresa vinculada ao cadastro do usuário.
