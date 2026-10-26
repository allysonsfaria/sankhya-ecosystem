---
id: "35812407767319"
titulo: "Aproveitamento de crédito de ICMS em campos próprios — combustíveis"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35812407767319-Aproveitamento-de-cr%C3%A9dito-de-ICMS-em-campos-pr%C3%B3prios-combust%C3%ADveis"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:24:40Z"
rotulos: ["Configuração", "Fiscal", "Crédito", "ICMS", "Impostos", "campos próprios", "combustíveis", "EFD ICMS IPI", "Aproveitamento de crédito", "Geração ICMS IPI", "CST 060"]
---

# Aproveitamento de crédito de ICMS em campos próprios — combustíveis

Este artigo visa orientar a configuração do aproveitamento parcial (1,12%) do crédito de ICMS em campos próprios para operações de compra de combustíveis (CST 060), nos casos em que a legislação estadual autorizar esse crédito.

**SITUAÇÃO:**

Empresas que adquirem, distribuem ou consomem combustíveis precisam registrar no sistema o aproveitamento do crédito de ICMS em campos próprios quando a legislação estadual permitir. Por padrão, operações com ICMS-ST não alimentam créditos em campos próprios; para combustíveis, existe exceção parcial (1,12%) que exige configuração específica.

**SOLUÇÃO:**

**(1)** Acesse a tela **"Empresa''** (Comercial» Preferências), na aba **"Geração ICMS IPI":**

![Imagem 1: (1) Acesse a tela "Empresa'' (Comercial» Preferências), na aba "Geração ICMS IPI":](https://ajuda.sankhya.com.br/hc/article_attachments/35812407763223)

**(2)** Localize o campo **"Creditar ICMS e ICMS/ST de NFe Compra Combustível (CST 060)"** e informe os códigos das TOPs que permitirão o aproveitamento do crédito em campos próprios (incluir todas as TOPs aplicáveis às operações de compra de combustível):

![Imagem 2: (2) Localize o campo "Creditar ICMS e ICMS/ST de NFe Compra Combustível (CST 060)" e informe os códigos das TOPs que…](https://ajuda.sankhya.com.br/hc/article_attachments/36021158930583)

**(3)** Salve a configuração e regenere a nota no livro fiscal:

- Se a nota ainda não estiver no livro, gere a nota normalmente;
- Se a nota já estiver gerada no livro, exclua a geração atual do livro e gere novamente para que os campos de ICMS próprio sejam populados.

**(3)** Confirme que os campos de ICMS próprio foram preenchidos no livro; essa informação será exportada para o **EFD ICMS IPI** durante a geração do arquivo fiscal.

**Importante:** Após alterar a configuração, exclua e regenere a nota no livro fiscal sempre que ela já tiver sido previamente gerada, garantindo o correto preenchimento dos campos de ICMS próprio.
