---
id: "360055402693"
titulo: "Apropriação de crédito de ICMS, em notas lançadas com CST 90"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360055402693-Apropria%C3%A7%C3%A3o-de-cr%C3%A9dito-de-ICMS-em-notas-lan%C3%A7adas-com-CST-90"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:28:31Z"
rotulos: ["Configuração", "NF-e", "Crédito", "ICMS", "Impostos", "TOP", "#revisadoFer", "#validadoThiagoArantes", "Preferências da empresa", "Apropriar crédito ICMS", "Configuração ICMS CST 90"]
---

# Apropriação de crédito de ICMS, em notas lançadas com CST 90

![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18796718429975) **SOLUÇÃO:**

Para notas com redução de base de cálculo: Estando os itens com CST 90, e redução na base de cálculo de ICMS, e que se faz necessário apropriar o crédito de ICMS nos livros fiscais.

Para que uma nota nessa situação, aproprie crédito, se faz necessário a seguinte configuração:

![Imagem 2: Acesse as Preferências da empresa (Comercial » Preferências » Empresa)](https://ajuda.sankhya.com.br/hc/article_attachments/18796686028311) Acesse as **Preferências da empresa** (Comercial » Preferências » Empresa)

- Aba 'Geração ICMS/IPI' devemos marcar o campo "Usar Tratamento de Código Tributação Definido no Cadastro de Empresas?"

- Aba 'Livro de entrada Cód tributação'
- Campo 90 - Outras Com Crédito/Débito (Valor Contábil vai p/) = **Outros**

![Imagem 3: Campo 90 - Outras Com Crédito/Débito (Valor Contábil vai p/) = Outros](https://ajuda.sankhya.com.br/hc/article_attachments/18796686035479)

![Imagem 4: Acesse a Tela Tipos de Operação - TOP (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)](https://ajuda.sankhya.com.br/hc/article_attachments/18796686039191) Acesse a Tela **Tipos de Operação - TOP** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)

- Aba livros fiscais
- Campo Tipo de ICMS = Com crédito/débito do imposto

**Considerações:**

- Ao gerar os livros, o sistema vai pegar a base de cálculo reduzida, alíquota e valor e lançar em seus devidos campos, e a diferença entre a base cheia e a reduzida, será levada para a coluna 'Outras ICMS'.
- Para notas em que os itens estão com cst 90 e sem redução de base de cálculo, a única diferença é que não terá o campo Outras/Isentas populado, pois não há redução.
- Essa configuração não faz com que o sistema deixe de apresentar a diferença entre a base cheia e a base reduzida, notas lançadas com CST 20 - Com redução de base de  cálculo, nesses casos, o sistema vai buscar nas preferências da empresa, aba Livro de Entrada Cod Tributação, qual campo deve alocar o valor da redução.
