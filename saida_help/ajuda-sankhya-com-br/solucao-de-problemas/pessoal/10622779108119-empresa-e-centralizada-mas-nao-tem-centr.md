---
id: "10622779108119"
titulo: "Empresa é centralizada, mas não tem centralizador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10622779108119-Empresa-%C3%A9-centralizada-mas-n%C3%A3o-tem-centralizador"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:16:24Z"
rotulos: ["Configuração", "Importação", "SEFAZ", "Folha", "#folha", "Altere empresas centralizadoras para \"Não Centraliza\"", "Verifique e modifique na aba Informações Gerais", "Garanta que o arquivo seja gerado corretamente após as mudanças", "Erro"]
---

# Empresa é centralizada, mas não tem centralizador

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19029652949271) MENSAGEM:**

Empresa é centralizada, mas não tem centralizador.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19029667810455) SITUAÇÃO:**

Ao importar arquivo gerado da sefip 650 a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19029667813783) CAUSA:**

Ocorre quando as empresas filiais estão como centralizadoras.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19029652969239) SOLUÇÃO:**

Só serão utilizadas as opções de centralizadora e centralizadas quando as empresas filiais forem centralizadas na Matriz e a Matriz centralizadora. Ou seja, todo recolhimento de INSS e FGTS na SEFIP será pelo CNPJ da matriz, mas quando as filiais têm CNPJ próprio e funcionários vinculados a eles, o recolhimento de INSS e FGTS é realizado no respectivo CNPJ e não na matriz.

Nesse caso, acesse o cadastro das **Empresas** (Caminho de acesso à tela: Configurações » Cadastros » Pessoal » Empresas), vá até a aba Informações Gerais e no campo 'Centralizadora', nas empresas que estiverem como centralizadora, altere para 'Não Centraliza'.

![Imagem 5: Só serão utilizadas as opções de centralizadora e centralizadas quando as empresas filiais forem centralizadas na…](https://ajuda.sankhya.com.br/hc/article_attachments/19029652974103)

No MGE Pessoal, essa configuração estará em Arquivos > Empresas, aba informações gerais:

![Imagem 6: Após isto, o arquivo será gerado e importado na SEFIP conforme esperado. Importante: Ressaltamos que só utiliza a…](https://ajuda.sankhya.com.br/hc/article_attachments/19029667831319)

Após isto, o arquivo será gerado e importado na SEFIP conforme esperado.

**Importante:** Ressaltamos que só utiliza a configuração de Centralizadora e Centralizadas se o recolhimento for todo pelo CNPJ da matriz. Mas se tiver certificado digital de CNPJ das empresas filiais no CNS, o recolhimento segue esses CNPJ's, dispensando assim a configuração de centralizadas e centralizadora.
