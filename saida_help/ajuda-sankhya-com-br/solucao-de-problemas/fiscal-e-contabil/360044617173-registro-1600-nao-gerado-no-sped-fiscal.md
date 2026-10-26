---
id: "360044617173"
titulo: "Registro 1600 não gerado no SPED FISCAL"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617173-Registro-1600-n%C3%A3o-gerado-no-SPED-FISCAL"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:53:18Z"
rotulos: ["#revisadojunior", "Configuração", "SPED", "Movimentação Financeira", "EFD", "Estoque", "Financeiro", "Configure a tela \"Empresa\" para gerar Registro 1600.", "Ative a marcação \"Gerar registro 1600 pelo Resumo de Operações com Cartão\" se necessário.", "Verifique \"Tipos de Título\" e campos esperados."]
---

# Registro 1600 não gerado no SPED FISCAL

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16594936661271)SOLUÇÃO:**

![Imagem 2: Acesse a tela de "Tipos de Título" (Caminho de acesso: Financeiro » Arquivos » Cadastros » Tipos de Título).](https://ajuda.sankhya.com.br/hc/article_attachments/16594894338711) Acesse a tela de **"Tipos de Título"** (Caminho de acesso: Financeiro » Arquivos » Cadastros » Tipos de Título).

![Imagem 3: Localize os tipos de título utilizados nos lançamentos que não estão sendo enviados ao SPED.](https://ajuda.sankhya.com.br/hc/article_attachments/16594894341143) Localize os tipos de título utilizados nos lançamentos que não estão sendo enviados ao SPED.

![Imagem 4: Na aba "Fast Service" verifique o campo "Subtipo";](https://ajuda.sankhya.com.br/hc/article_attachments/16594894343575) Na aba **"Fast Service"** verifique o campo **"Subtipo";**

- Configuração esperada: cartão de Débito ou Cartão de Crédito;

![Imagem 5: Na aba "Geral", verifique o campo "Parc.Administradora" :](https://ajuda.sankhya.com.br/hc/article_attachments/16594894345879) Na **aba "Geral",** verifique o campo **"Parc.Administradora"**:

- Configuração esperada: informar o Parceiro Administradora do cartão;

![Imagem 6: Acesse a Tela "Empresa" (Caminho de acesso: Comercial » Preferências ), aba "EFD - Escrituração Fiscal Digital" :](https://ajuda.sankhya.com.br/hc/article_attachments/16594936682903) Acesse a Tela **"Empresa"** **(Caminho de acesso: Comercial » Preferências),** aba **"EFD - Escrituração Fiscal Digital"** :

- Blocos e Registros:  Bloco 1 cadastrado / Gerar Registro: sim
- Registros: Registro 1600 / Gerar Bloco: sim

![Imagem 7: Registros: Registro 1600 / Gerar Bloco: sim](https://ajuda.sankhya.com.br/hc/article_attachments/15185613579287)

![Imagem 8: Na tela de Livros Fiscais » Conexão » EFD - Escrituração Fiscal Digital - ICMS/IPI, fique atento à marcação "Gerar…](https://ajuda.sankhya.com.br/hc/article_attachments/16594936685079) Na tela de Livros Fiscais » Conexão » EFD - Escrituração Fiscal Digital - ICMS/IPI, fique atento à marcação **"Gerar registro 1600 pelo Resumo de Operações com Cartão?"**, pois quando ela estiver acionada o sistema utilizará os dados inseridos na tela **"Resumo de Operações com Cartão"** para tratar de forma manual as informações referentes ao Registro 1600 ao gerar o arquivo. Por outro lado,  desabilitada a marcação e gerando o arquivo, o sistema não utilizará os dados da tela Resumo de Operações com Cartão.

**![Imagem 9: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/16594894353431) OBSERVAÇÕES:**

**(1)** É necessário que seja um financeiro de origem **estoque**.

**(1)** Tem que ser uma **receita** não renegociada ou um Financeiro/Receita renegociado, com nro de renegociação maior que 0, que tenha sido renegociada uma única vez.
