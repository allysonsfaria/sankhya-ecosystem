---
id: "1500002850141"
titulo: "Divergência na parte patronal sobre a comercialização da produção no E-social"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500002850141-Diverg%C3%AAncia-na-parte-patronal-sobre-a-comercializa%C3%A7%C3%A3o-da-produ%C3%A7%C3%A3o-no-E-social"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:31:13Z"
rotulos: ["Configuração", "Fiscal", "Impostos", "não apagar", "#publicadoHyago", "eSocial", "Erro no Recolhimento", "Correção na Marcação", "Retificação no eSocial", "Produtor Rural"]
---

# Divergência na parte patronal sobre a comercialização da produção no E-social

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16304815992471) MENSAGEM:**

Quando a empresa recolhe a parte patronal sobre a comercialização da produção e o valor apurado no portal do eSocial não está correto.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16304799555735) SOLUÇÃO:**

Acesse: Arquivos » Cadastros » Empresas (dados Básicos)', na Aba **"Informações Fiscais"** o cadastro da marcação **"Tributação da Contribuição Previdenciária (Produtor Rural)"**.

![Divergência](https://ajuda.sankhya.com.br/hc/article_attachments/15185539487639)

Acesse a tela: Arquivos » Parceiros » Aba Fiscal » Tributação da Contribuição Previdenciária (Produtor Rural e preencha \*\*Sobre a Comercialização da produção\*\* .

![Divergência](https://ajuda.sankhya.com.br/hc/article_attachments/15185493197975)

Se a informação incorreta já estiver no portal do eSsocial  é necessário retificar o evento S-1000 com os dados corretos. No qual deve constar no cadastro da empresa a informação do **indOpcCP** com valor 1.

**indOpcCP:** nos termos do art. 25, §13, da Lei 8.212/91 e do art. 25, §7°, da Lei 8.870/94 o não preenchimento deste campo por parte do produtor rural implica opção pela comercialização da sua produção:

![Imagem 5: Se a informação incorreta já estiver no portal do eSsocial é necessário retificar o evento S-1000 com os dados…](https://ajuda.sankhya.com.br/hc/article_attachments/16304799558167) Sobre a comercialização da sua produção;

![Imagem 6: Sobre a folha de pagamento. Validação: Não preencha se ({classTrib} <> (07, 08, 21)). Valores Válidos: 1, 2.'](https://ajuda.sankhya.com.br/hc/article_attachments/16304815998103) Sobre a folha de pagamento. Validação: Não preencha se ({classTrib} <> [07, 08, 21]). Valores Válidos: 1, 2.'

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16304816000151) CAUSA:**

O campo indOpcCP  (Indicativo da opção pelo produtor rural pela forma de tributação da contribuição previdenciária) está divergente entre eSocial e MGE.
