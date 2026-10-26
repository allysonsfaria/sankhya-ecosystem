---
id: "7173166159511"
titulo: "Geração do registro E520 SPED FISCAL"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7173166159511-Gera%C3%A7%C3%A3o-do-registro-E520-SPED-FISCAL"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:14:52Z"
rotulos: ["Configuração", "Fiscal", "IPI", "Impostos", "EFD", "Estoque", "Configurações EFD IPI", "Documentos Entrada/Saída", "Modelos Documentos IPI"]
---

# Geração do registro E520 SPED FISCAL

Este registro deve ser preenchido para demonstração da apuração do IPI no período.

#### Configurações:

![Imagem 1: Tela: "Preferências da Empresa" (Comercial), aba "EFD - Escrituração Fiscal Digital", marque os seguintes Blocos e…](https://ajuda.sankhya.com.br/hc/article_attachments/16491100996759) Tela: **"Preferências da Empresa"** (Comercial), aba **"EFD - Escrituração Fiscal Digital",** marque os seguintes Blocos e Registros:

**E001**
**E500**
**E520**
**E990**

![Imagem 2: E001 E500 E520 E990](https://ajuda.sankhya.com.br/hc/article_attachments/15938850765335)

![Imagem 3: Tela: "Registro de Apuração do IPI:"](https://ajuda.sankhya.com.br/hc/article_attachments/16491124029719) Tela: **"Registro de Apuração do IPI:"**

Informe a empresa e período de geração do EFD em que o registro citado precisa ser gerado, e clique:

Abrir> Salvar> Visualizar

![Imagem 4: Abrir> Salvar> Visualizar](https://ajuda.sankhya.com.br/hc/article_attachments/15938869205527)

Basicamente seriam essas as configurações realizadas e necessárias para a geração do registro. Agora segue análise de algumas informações adicionais sobre os processos e validações do sistema:

**(1)** Se o documento for de "Entrada" nos livros fiscais (Tela Cadastro Livro ICMS/IPI), o sistema vai olhar para o campo **"Dt. do movimento"**, para selecionar os documentos que serão enviado ao E520, porém se for documento de "Saída" o sistema vai priorizar o campo "Dt. do documento".

**(1)** Os documentos devem estar com algum dos modelos de documento a seguir: 1, 4, 55, 65, 901;

**(1)** Nos livros fiscais (Tela Cadastro Livro ICMS/IPI) a origem dos documentos deve ser: Estoque ou Complemento

**(1)** No lançamento da nota, nos portais, na grade de itens do documento, os itens que tem valores a serem apresentados no E520 não podem estar com o campo CST IPI igual a: "(-1) Não sujeita ao IPI".
