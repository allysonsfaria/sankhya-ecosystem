---
id: "6326421146007"
titulo: "Veja como gerar o C177 no EFD ICMS/IPI"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/6326421146007-Veja-como-gerar-o-C177-no-EFD-ICMS-IPI"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:16:41Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "CFOP", "EFD ICMS/IPI", "#validadoMurilo", "Configuração Inicial: Acesse \"Empresa\" e marque a opção para gerar o C177.", "Configurações Adicionais: Ajuste os campos de produto CFOP e preferências de incentivo na empresa.", "Cadastro de Incentivos: Configure incentivos na tela \"Cadastros Incentivos Fiscais/Financeiros\"."]
---

# Veja como gerar o C177 no EFD ICMS/IPI

REGISTRO C177: COMPLEMENTO DE ITEM - OUTRAS INFORMAÇÕES (código 01, 55) -
(VÁLIDO A PARTIR DE 01/01/2019)

Este registro deverá ser apresentado somente pelos contribuintes obrigados por legislação específica de cada UF, com o objetivo de agregar informações adicionais ao item, de acordo com tabela a ser publicada pela UF.

![Imagem 1: Este registro deverá ser apresentado somente pelos contribuintes obrigados por legislação específica de cada UF, com o…](https://ajuda.sankhya.com.br/hc/article_attachments/6325858193687)

**1° Passo**

Na tela **"Empresa"** (Caminho de acesso: Comercial » Preferências » Empresa), aba **"EFD - Escrituração Fiscal digital"**, sub aba **"Bloco e Registro"** configure e marque para gerar.

![Imagem 2: Na tela "Empresa" (Caminho de acesso: Comercial » Preferências » Empresa), aba "EFD - Escrituração Fiscal digital" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/16448419087383)

**2° Passo**

Foi criada uma nova tela, denominada **"Cadastros Incentivos Fiscais/Financeiros",** nela será possível configurar os diversos incentivos que por ventura a empresa tenha, atendendo a uma necessidade de geração de vários incentivos ao mesmo tempo.

![Imagem 3: Foi criada uma nova tela, denominada "Cadastros Incentivos Fiscais/Financeiros", nela será possível configurar os…](https://ajuda.sankhya.com.br/hc/article_attachments/16448414103575)

**3° Passo**

Tela **"Produtos"** (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos) configure os campos **"Cód. Apur. Inc. PRODEPE/FUNCRESCE"** e **"Indicador Esp. Inc. PRODEPE/FUNCRESCE"** com a opção  **'Com Incentivos';**

![Imagem 4: Tela "Produtos" (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos) configure os campos "Cód. Apur.…](https://ajuda.sankhya.com.br/hc/article_attachments/16448419090839)

**4° Passo**

Na tela  Empresa (Caminho de acesso: Comercial » Preferências » Empresa), aba **"Livros Fiscais"**, marque o campo **"Beneficiário de Incentivo PRODEPE/FUNCRESCE?"**;

![Imagem 5: Na tela Empresa (Caminho de acesso: Comercial » Preferências » Empresa) , aba "Livros Fiscais" , marque o campo…](https://ajuda.sankhya.com.br/hc/article_attachments/16448414106903)

**5° Passo**

No cadastro de CFOP (Caminho de acesso: Comercial » Arquivo » Cadastros » CFOP), marque o campo **"Tipo de Operação PRODEPE"** igual a **"Operação Incentivada"**.

\* Configure para o CFOP que usar no lançamento da nota.

![Imagem 6: * Configure para o CFOP que usar no lançamento da nota.](https://ajuda.sankhya.com.br/hc/article_attachments/16448414108311)

![Imagem 7: * Configure para o CFOP que usar no lançamento da nota.](https://ajuda.sankhya.com.br/hc/article_attachments/16448414109463)

**Importante:** O código que vai ser gerado no campo 2 do C177 é gerado através da tabela COD\_INF\_ITEM Código da informação adicional, de acordo com tabela a ser publicada pela SEFAZ, conforme tabela definida no item 5.6.

Ele será formado a partir da combinação da UF que a cidade no cadastro de empresa pertence, mais a configuração Indicador de Enquadramento (tela cadastro de incentivo) e também o Indicador de Sub-apuração ( tela cadastro de incentivo).
