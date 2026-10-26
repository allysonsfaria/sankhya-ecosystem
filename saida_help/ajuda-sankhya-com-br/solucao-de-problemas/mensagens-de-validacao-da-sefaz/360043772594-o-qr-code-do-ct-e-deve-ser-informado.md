---
id: "360043772594"
titulo: "O QR Code do CT-e deve ser informado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043772594-O-QR-Code-do-CT-e-deve-ser-informado"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T15:59:08Z"
rotulos: ["ERROCTE", "#PUBLIFER", "#revisadohugo", "CT-e", "Configuração", "XML", "SEFAZ", "850", "QR Code do CT-e Não Informado", "Documentos Eletrônicos"]
---

# O QR Code do CT-e deve ser informado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16414449392279) MENSAGEM:**

[850 - Rejeição]: O QR Code do CT-e deve ser informado.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16414464318359) SOLUÇÃO:**

Para geração das tags QR Code, siga as orientações abaixo:

![Imagem 3: Sistema atualizado para versões abaixo ou superiores:](https://ajuda.sankhya.com.br/hc/article_attachments/16414449394455) Sistema atualizado para versões abaixo ou superiores:

- Sankhya W 3.32b126
- Sankhya W 3.31b286
- Sankhya W 3.30b433

Disponíveis em: [downloads.sankhya.com.br](https://ajuda.sankhya.com.br/hc/pt-br/articles/downloads.sankhya.com.br).

![Imagem 4: Na tela "Preferências" (Caminho de acesso: Configurações » Avançado) o parâmetro DATINICTEQRCOD deverá ser ajustado…](https://ajuda.sankhya.com.br/hc/article_attachments/16414464320919) Na tela **"Preferências"** (Caminho de acesso: Configurações » Avançado) o parâmetro DATINICTEQRCOD deverá ser ajustado conforme abaixo [AN:26/08/2019]:

![Imagem 5: Na tela "Preferências" (Caminho de acesso: Configurações » Avançado) o parâmetro DATINICTEQRCOD deverá ser ajustado…](https://ajuda.sankhya.com.br/hc/article_attachments/13317244209431)

![Imagem 6: Nas preferências da empresa (Caminho de acesso: Comercial » Preferências » Empresa) , aba 'CT-e', valide se o campo…](https://ajuda.sankhya.com.br/hc/article_attachments/16414449397655) Nas preferências da empresa (Caminho de acesso: Comercial » Preferências » Empresa), aba 'CT-e', valide se o campo **"Versão NT CTE"** está configurado com a **Última (Nota Técnica 3.00a)**.

![Imagem 7: Para que seja apresentado o novo modelo de impressão o mesmo já está disponível para ser baixado na tela Comercial »…](https://ajuda.sankhya.com.br/hc/article_attachments/16414464329239) Para que seja apresentado o novo modelo de impressão o mesmo já está disponível para ser baixado na tela Comercial » Arquivo » Cadastros » Modelo de Impressão (Nota/Pedido). Dessa forma, recomenda-se o download [tanto para o MDF-e e CT-e] dos arquivos de impressão atualizados que se adequem a necessidade da empresa.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16414464330391) CAUSA:**

Mensagem apresentada ao realizar a emissão de CT-e no sistema utilizando as parametrizações desatualizadas da última Nota Técnica 300, validando a não geração do QR Code.
