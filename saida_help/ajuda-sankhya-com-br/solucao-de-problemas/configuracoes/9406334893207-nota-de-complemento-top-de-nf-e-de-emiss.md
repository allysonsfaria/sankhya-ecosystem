---
id: "9406334893207"
titulo: "Nota de Complemento - TOP de NF-e de Emissão Própria deve ter o \"Cálculo de ICMS, IPI e ISS\" do tipo \"Não calcula e digita"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9406334893207-Nota-de-Complemento-TOP-de-NF-e-de-Emiss%C3%A3o-Pr%C3%B3pria-deve-ter-o-C%C3%A1lculo-de-ICMS-IPI-e-ISS-do-tipo-N%C3%A3o-calcula-e-digita"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-09-15T13:03:53Z"
rotulos: ["Configuração", "NF-e", "XML", "Impostos", "TOP", "CORE_E02556", "Configuração de TOP para NF-e de Emissão Própria"]
---

# Nota de Complemento - TOP de NF-e de Emissão Própria deve ter o "Cálculo de ICMS, IPI e ISS" do tipo "Não calcula e digita

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16968296016023) MENSAGEM:**

[CORE\_E02556]: TOP de NF-e de Emissão Própria deve ter o "Cálculo de ICMS, IPI e ISS" do tipo "Não calcula e digita.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16968312270615) CAUSA:**

Ao tentar emitir nota de Completo emissão própria, mas a TOP não está configurada corretamente.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16968312266647) SOLUÇÃO:**

![Imagem 4: Verifique a configuração no Tipos de Operação - TOP (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de…](https://ajuda.sankhya.com.br/hc/article_attachments/16968312267415) Verifique a configuração no **Tipos de Operação - TOP** (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP), na aba **"Impostos"**, campo **"Cálculo de ICMS, IPI e ISS"** ajuste para **"Não calcula e digita"**.

![Imagem 5: Verifique a configuração no Tipos de Operação - TOP (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de…](https://ajuda.sankhya.com.br/hc/article_attachments/9405966894103)

![Imagem 6: Verifique a configuração no Tipos de Operação - TOP (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de…](https://ajuda.sankhya.com.br/hc/article_attachments/9406041580567)

**![Imagem 7: Não calcula e digita: o sistema não calculará os impostos e será possível digitá-los na nota. Além disso, quando esta…](https://ajuda.sankhya.com.br/hc/article_attachments/16968312268183) Não calcula e digita:** o sistema não calculará os impostos e será possível digitá-los na nota. Além disso, quando esta opção estiver selecionada, os impostos provenientes do XML serão considerados. E para que a importação dos valores constantes no XML do IPI sejam realizadas, fará necessário que os seguintes campos estejam marcados:

1. Campo **"Tem IPI na compra:",** na tela **"Cadastro de Produtos"**, aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abaimpostos);
2. **"Tem IPI",** na tela **"Cadastro de Parceiros"**, aba [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal);
3. E o campo **"Tem IPI"** desta tela, aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos).
