---
id: "27441093067799"
titulo: "Configurações do Livro de Entrada Cód. Tributação para notas do tipo A - Complemento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27441093067799-Configura%C3%A7%C3%B5es-do-Livro-de-Entrada-C%C3%B3d-Tributa%C3%A7%C3%A3o-para-notas-do-tipo-A-Complemento"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Cadastros e Configurações Fiscais"
atualizado_em: "2026-09-15T14:12:40Z"
rotulos: ["Configuração", "NF-e", "ICMS", "Impostos", "TOP", "CFOP", "Nota complementar", "Complemento de Imposto", "CST 020", "CST 051"]
---

# Configurações do Livro de Entrada Cód. Tributação para notas do tipo A - Complemento

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312535976855) Versão disponível: A partir da 4.32
```

---

O artigo apresenta o processo de lançamento de notas de Complemento de Imposto, detalhando as etapas para validação do registro no livro fiscal de notas complementares. São descritas três formas distintas para garantir uma geração correta:

**![Imagem 2: Por meio da CFOP :](https://ajuda.sankhya.com.br/hc/article_attachments/27441076737687) Por meio da [CFOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600714-CFOP):**

Ao configurar o [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#top), aba [NF-e/NFC-e/CF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce/cfe), com os campos **"NF-e"** e **"Tipo de Emissão"** definidos com a opção **"Complementar"**, observe a configuração do campo **"ICMS p/ o Livro Fiscal"** (aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600714-CFOP#abageral), da tela CFOP); se for selecionada uma opção diferente de **"Usar da TOP/Empresa"** o sistema usará a configuração escolhida nesse campo para a geração do livro por meio da tela [Geração ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953-Gera%C3%A7%C3%A3o-ICMS-IPI):

- Quando a opção selecionada for **"Sem créd./déb. - Isentas"**, os valores serão registrados no campo **"Isentas de ICMS"** na aba [ICMS/IPI/ST](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607874-Cadastro-Livro-ICMS-IPI#abaicmsipi) no [Cadastro Livro ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607874-Cadastro-Livro-ICMS-IPI);
- Se a opção for **"Sem créd./déb. - Outras"**, os valores serão registrados no campo **"Outras ICMS"** da mesma aba e tela;

**![Imagem 3: Por meio do Tipo de Operação -TOP :](https://ajuda.sankhya.com.br/hc/article_attachments/27441076740503) Por meio do [Tipo de Operação -TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#top):**

Assim como a primeira opção, defina os campos Tipo de Emissão e NF-e como Complementar.

No campo **"Tipo de ICMS"** da TOP, aba [Livro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal), escolha entre as opções:

- **Sem créd./déb. - Isentas:** caso essa opção seja selecionada, os valores serão registrados no campo Isentas de ICMS na aba ICMS/IPI/ST no Cadastro Livro ICMS/IPI;
- **Sem créd./déb. - Outras:** caso essa opção seja selecionada os valores irão para o campo Outras ICMS da mesma aba e tela;
- **Com créd./déb. de Imposto:** caso essa opção seja selecionada, o sistema definirá automaticamente onde o valor do ICMS será registrado;
- **Com créd./déb. - Isentas:** caso essa opção seja selecionada, os valores serão registrados no campo Isentas de ICMS da mesma aba e tela;
- **Com créd./déb. - Outras:** caso essa opção seja selecionada, os valores irão para o campo Outras ICMS da mesma aba e tela.

**Observação:** para que o sistema sempre se baseie na configuração da TOP para o registro do ICMS, defina o campo ICMS p/ o Livro Fiscal na aba Geral da tela CFOP como **"Usar da TOP/Empresa"**.

Essa configuração permite que o sistema registre corretamente os valores de ICMS com base nas definições estabelecidas para cada operação na TOP ou na configuração de ICMS para o Livro Fiscal, garantindo uma alocação precisa no livro ICMS/IPI.

**![Imagem 4: Por meio das Preferências da Empresa :](https://ajuda.sankhya.com.br/hc/article_attachments/27441093051159) Por meio das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa):**

Seguindo o padrão, defina os campos Tipo de Emissão e NF-e como Complementar.

Então ajuste o campo **Tipo de ICMS** da TOP, aba Livro Fiscal, para as opções:

- Com créd./déb. de imposto;
- Com créd./déb. - outras;
- Com créd./déb. - isentas.

Assim, ao lançar uma nota no livro fiscal, o sistema seguirá a configuração definida na aba Livro de Entrada Cód. Tributação, correspondente a CST utilizada no lançamento da nota. Quando a opção selecionada for:

- **Isentas**: com essa opção selecionada, os valores serão registrados em Isentas de ICMS na aba ICMS/IPI/ST no Cadastro Livro ICMS/IPI;
- **Outras**: caso essa opção seja selecionada, os valores irão para o campo Outras ICMS da mesma aba e tela.

**Observação:** essa funcionalidade somente será aplicada para as notas complementares lançadas com as CST 020 e 051.
