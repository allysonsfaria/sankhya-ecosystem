---
id: "360044617453"
titulo: "EFD-REINF - Empresa não está sendo apresentada na rotina de Geração da Obrigação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617453-EFD-REINF-Empresa-n%C3%A3o-est%C3%A1-sendo-apresentada-na-rotina-de-Gera%C3%A7%C3%A3o-da-Obriga%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:52:55Z"
rotulos: ["Configuração", "Empresa", "Fiscal", "EFD", "Preferências", "Empresa matriz configurada", "Campos EFD-Reinf preenchidos", "Administração Pública direta"]
---

# EFD-REINF - Empresa não está sendo apresentada na rotina de Geração da Obrigação

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17004220431895) SOLUÇÃO:**

Considere o comportamento da aplicação conforme abaixo:

![Imagem 2: Considere o comportamento da aplicação conforme abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/17004190222999) A Empresa deve estar configurada como empresa matriz, ou seja, Empresas que possuem o campo **"Empresa Matriz (EFD)"** (Caminho de acesso: Comercial » Preferências » Empresa, aba: Propriedades) em branco ou configurado com o código da própria empresa;

**Nota:** empresas que possuem o campo configurado com código de outra empresa, para o sistema figuram como empresas filiais e terão seus movimentos gerados junto aos movimentos da matriz. Por este motivo, não serão apresentadas no botão de pesquisa na tela do REINF.

![Imagem 3: Considere o comportamento da aplicação conforme abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/17004190224535) Também são apresentadas empresas configuradas como Administração Pública direta, ou seja,   empresas que possuem o campo **"Empresa de Adm. Publica Direta?"** (Caminho de acesso: Comercial » Preferências » Empresa, aba: EFD-Reinf) marcado;

![Imagem 4: Considere o comportamento da aplicação conforme abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/17004220441111) Além destas duas premissas existe a necessidade de se configurar os seguintes campos:

Acesse: Comercial » Preferências » Empresa, aba: EFD-Reinf:

- **"Ambiente EFD-Reinf"**:  selecione uma das opções disponíveis
- **"Classificação Tributária - EFD-Reinf"**: selecione uma das opções disponíveis
- **"Data Validade Inicial Reinf":** obrigatório Preencher

**![Imagem 5: "Data Validade Inicial Reinf": obrigatório Preencher](https://ajuda.sankhya.com.br/hc/article_attachments/17004190231191) CAUSA:**

Ocorre quando uma das opções informadas acima não estão devidamente configuradas.
