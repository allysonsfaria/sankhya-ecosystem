---
id: "36226748822551"
titulo: "Unable to load library 'XXXX': Não foi possível encontrar o módulo especificado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36226748822551-Unable-to-load-library-XXXX-N%C3%A3o-foi-poss%C3%ADvel-encontrar-o-m%C3%B3dulo-especificado"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:23:23Z"
rotulos: ["Configuração", "Fiscal", "Web Connection", "SAT", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "Módulo especificado", "Cadastro de Equipamentos Fiscais", "Módulo Fiscal", "SAT em operação"]
---

# Unable to load library 'XXXX': Não foi possível encontrar o módulo especificado

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/36226752840599) **MENSAGEM:**

Unable to load library 'XXXX'. Não foi possível encontrar o módulo especificado

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/36226748814743)SOLUÇÃO:**

**(1)** Na tela inicial do [''**Web Connection''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection), verifique qual versão ela se encontra instalada. Caso esteja utilizando a versão 64 bits, esta deve ser **desinstalada**.

**(2)** Certifique-se de baixar e instalar a **versão 32 bits** do **Web Connection externo**.

- O sistema deve operar sempre com o **Web Connection externo** (externo). Portanto, **desconsidere** o modo **Web Connection embarcado (interno)**.

**(3)** Após instalar o Web Connection 32 bits, reinicie o computador.

**(4)** Em seguida, clique e execute o **Web Connection externo (32 bits).**

**(5)** No sistema, acesse a tela [**''Cadastro de Equipamentos Fiscais - ECF/SAT/MFE''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110533-Cadastro-de-Equipamentos-Fiscais-ECF-SAT-MFE) (Comercial » Arquivo » Cadastros » Cadastro de Equipamentos Fiscais - ECF/SAT/MFE ) e realize o teste do módulo fiscal. O mesmo deverá retornar a mensagem **“SAT em operação”** confirmando o funcionamento correto.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/36226748815383)CAUSA:**

O erro ocorre quando o **Web Connection** instalado **não é compatível com o módulo fiscal (SAT/MFE)**.
