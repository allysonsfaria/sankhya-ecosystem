---
id: "16702513806871"
titulo: "Lote rejeitado: L060 – ISSRetido diferente de 1 - Prefeitura BRASILIA"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/16702513806871-Lote-rejeitado-L060-ISSRetido-diferente-de-1-Prefeitura-BRASILIA"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:54:32Z"
rotulos: ["Configuração", "Alíquota de ISS", "Impostos", "Prefeituras", "NFS-e", "Rejeição L060: ISS Retido Incorreto"]
---

# Lote rejeitado: L060 – ISSRetido diferente de 1 - Prefeitura BRASILIA

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16702513781271)  MENSAGEM:**

L060 – ISSRetido diferente de 1. Possível solução: Informe ISSRedito = 1 para substituto tributário.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16702488178327) CAUSA:**

Quando o serviço esta com dedução de ISS, a nota é gerada sem as informações de ISS e o XML apresenta com a tag ISSRetido = 2, mas a prefeitura exige que seja ISSRetido = 1

![Imagem 3: Quando o serviço esta com dedução de ISS, a nota é gerada sem as informações de ISS e o XML apresenta com a tag…](https://ajuda.sankhya.com.br/hc/article_attachments/16702109259159)

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16702504613015) SOLUÇÃO:**

Por meio do parâmetro **"Permite ISS retido zero em NFS-e - NFSEISSRETZERO"** defina se será permitido enviar RPS à prefeitura com ISS retido zerado.

Na situação da rejeição, o parâmetro citado deve estar ligado.

![Imagem 5: Na situação da rejeição, o parâmetro citado deve estar ligado.](https://ajuda.sankhya.com.br/hc/article_attachments/16702525889559)

Feito o ajuste, basta gerar o lote novamente.
