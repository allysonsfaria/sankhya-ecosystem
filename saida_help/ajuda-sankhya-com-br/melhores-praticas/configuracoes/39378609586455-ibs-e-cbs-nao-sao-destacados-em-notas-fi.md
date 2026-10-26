---
id: "39378609586455"
titulo: "IBS e CBS não são destacados em Notas Fiscais Complementares"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39378609586455-IBS-e-CBS-n%C3%A3o-s%C3%A3o-destacados-em-Notas-Fiscais-Complementares"
trilha: "Melhores Práticas > Configurações"
atualizado_em: "2026-08-11T20:57:32Z"
rotulos: ["Configuração", "NF-e", "Impostos", "IBS", "CBS", "Artigo criado KCS", "Docs Eletrônicos - KCS", "Nota Fiscal Complementar"]
---

# IBS e CBS não são destacados em Notas Fiscais Complementares

**SITUAÇÃO**

Os tributos **IBS** e **CBS** não estão sendo calculados e/ou destacados nas **Notas Fiscais Complementares** emitidas pelo sistema.

**SOLUÇÃO**

Para que os tributos **IBS** e **CBS** sejam destacados na nota fiscal complementar, realize as seguintes verificações e ajustes:

**(1)**  Acesse as **"Preferências da Empresa"** **(** Comercial » Preferências » Empresa ) e verifique **Nota Técnica da Reforma Tributária** está habilitada.
**(2)**  Como a TOP utilizada na nota complementar de emissão própria, possui a configuração "**Cálculo de ICMS, IPI, ISS, IBS, CBS e IS**" como "**Não calcula e Digita**", devemos inserir os valores de **"IBS"** e **"CBS"** diretamente na Central.

**(3)** Na **Central de Vendas**, com a nota complementar aberta, acesse **Outras Opções > Consultar/Alterar Dados do Imposto do Item**.

**(4)**  Inclua os impostos **IBS UF**, **IBS Município** e **CBS**, informando a **base de cálculo**, **alíquota** e **valor** de cada imposto. Salve as alterações.

**(5)**  Gere o **XML de conferência** pelo botão **NF-e** na opção "Gerar XML da NF-e em arquivo para conferência"  e valide se os tributos foram destacados corretamente. Estando as informações corretas, confirme a nota para emissão.

![Imagem 1: (5) Gere o XML de conferência pelo botão NF-e na opção "Gerar XML da NF-e em arquivo para conferência" e valide se os…](https://ajuda.sankhya.com.br/hc/article_attachments/41944185737495)

**CAUSA**

Nas Notas Fiscais Complementares emitidas com uma TOP cuja configuração **"Cálculo de ICMS, IPI e ISS"** está definida como **"Não calcula e Digita"**, o sistema não realiza o cálculo automático dos tributos **IBS** e **CBS**. Nessa situação, os impostos devem ser informados manualmente nos dados do imposto do item para que sejam destacados no XML e no documento fiscal.
