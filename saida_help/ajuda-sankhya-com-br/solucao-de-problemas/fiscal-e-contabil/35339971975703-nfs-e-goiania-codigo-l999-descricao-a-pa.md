---
id: "35339971975703"
titulo: "NFS-e Goiânia Código: L999 Descrição: a partir de 10/2025, acesso pelo sistema Nota Control - portal do contribuinte"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35339971975703-NFS-e-Goi%C3%A2nia-C%C3%B3digo-L999-Descri%C3%A7%C3%A3o-a-partir-de-10-2025-acesso-pelo-sistema-Nota-Control-portal-do-contribuinte"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:25:18Z"
rotulos: ["Configuração", "Cidades", "Impostos", "TOP", "Prefeituras", "NFS-e", "VALIDASERIEGYN", "CNAE", "NFS-e Goiânia Código", "L999 Descrição", "a partir de 10/2025", "acesso pelo sistema Nota Control", "portal do contribuinte", "10/2025", "Controle de numeração", "Cód. Trib. Município NFS-e", "Tipo de serviço", "Cod. Trib. Município"]
---

# NFS-e Goiânia Código: L999 Descrição: a partir de 10/2025, acesso pelo sistema Nota Control - portal do contribuinte

**MENSAGEM:**

NFS-e Goiânia Código: L999 Descrição: a partir de 10/2025, acesso pelo sistema Nota Control - portal do contribuinte

**SOLUÇÃO:**

#### Pré-requisito para executar a solução:

Para **executar os passos da solução,** é preciso que **esteja na versão 4.35b215 ou superiores.**

Certo de que **está em uma das versões indicadas acima, siga os passos a seguir** para solucionar a mensagem de erro:

**(1)**  Acesse a tela **"Preferências"** (Configurações » Avançado » Preferências) e **desabilite o parâmetro** **"VALIDASERIEGYN"** (para permitir a série “1” ao invés de “UN”).

![Imagem 1: (1) Acesse a tela "Preferências" (Configurações » Avançado » Preferências) e desabilite o parâmetro "VALIDASERIEGYN"…](https://ajuda.sankhya.com.br/hc/article_attachments/35340022996887)

**(2)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP), clique no botão **"Outras opções"**, depois escolha **"Controle de numeração".**

![Imagem 2: (2) Acesse a tela "Tipos de Operação - TOP" (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP), clique no…](https://ajuda.sankhya.com.br/hc/article_attachments/35339971934103)

**(3)** Em seguida, na tela de "**Controle de numeração",** que será aberta, preencha os seguintes campos conforme orientações abaixo:

- **Empresa:** código da empresa que emitirá a nota
- **Serie:** 1
- **Mod. Doc. Fiscal:** 0
- **Último código:** 1

![Imagem 3: Último código: 1](https://ajuda.sankhya.com.br/hc/article_attachments/35340023007511)

**(4)** Depois, abra a tela **"Serviço"** (Configurações » Cadastros » Produtos » Serviço), vá até a aba **"Impostos"** e certifique-se de que o campo **"Cód. Trib. Município NFS-e"** esteja com a mesma numeração do código inserido no campo **"Tipo de serviço".**

**Importante:** o **número** inserido no **campo Cód. Trib. Município NFS-e não pode ter pontuação.**

![Imagem 4: Importante : o número inserido no campo Cód. Trib. Município NFS-e não pode ter pontuação.](https://ajuda.sankhya.com.br/hc/article_attachments/35339971942423)

**(5)**  Ainda na tela Serviço e na aba Impostos, garanta que o campo **"CNAE"** tenha exatamente **7 caracteres.**

**Importante:** caso o campo tenha **9 caracteres, limpe os dois últimos zeros** que estarão no final.

![Imagem 5: Importante: caso o campo tenha 9 caracteres, limpe os dois últimos zeros que estarão no final.](https://ajuda.sankhya.com.br/hc/article_attachments/35339971946007)

**(6)** Agora na tela Serviço e na aba **"Alíquotas de ISS",** certifique-se de que o campo **"Cod. Trib. Município"** esteja com a mesma numeração do código inserido no campo **"Tipo de serviço".**

**Importante:** o **número** inserido no **campo** Cod. Trib. Município **não pode ter pontuação.**

![Imagem 6: Importante: o número inserido no campo Cod. Trib. Município não pode ter pontuação.](https://ajuda.sankhya.com.br/hc/article_attachments/35339971957911)
