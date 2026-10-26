---
id: "360043103573"
titulo: "Versão informada no QR-Code (“100”) não é mais válida para a data de emissão(NT2016/002)."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043103573-Vers%C3%A3o-informada-no-QR-Code-100-n%C3%A3o-%C3%A9-mais-v%C3%A1lida-para-a-data-de-emiss%C3%A3o-NT2016-002"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:08:14Z"
rotulos: ["ERRONF", "Configuração", "SEFAZ", "903", "Versão QR-Code Inválida para Data de Emissão", "Erro", "Documentos Eletrônicos", "NT2016/002"]
---

# Versão informada no QR-Code (“100”) não é mais válida para a data de emissão(NT2016/002).

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16447727559319) MENSAGEM:**

[903-Rejeição]: Versão informada no QR-Code (“100”) não é mais válida para a data de emissão.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16447734711831) SOLUÇÃO:**

Para correção desta mensagem, seguir os passos abaixo.

#### SANKHYAW

![Imagem 3: Acessar " Empresa " (Caminho de acesso: Comercial » Preferências » Empresa ) Aba: " NF-e/NFC-e" "Usar QR Code versão…](https://ajuda.sankhya.com.br/hc/article_attachments/16447734716439) Acessar "**[Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)"** (Caminho de acesso: Comercial » Preferências » Empresa)
Aba: "**NF-e/NFC-e"**
**"Usar QR Code versão 2.0"** [marcado]

![Imagem 4: Acessar " Empresa " (Caminho de acesso: Comercial » Preferências » Empresa ) Aba: " NF-e/NFC-e" "Usar QR Code versão…](https://ajuda.sankhya.com.br/hc/article_attachments/14387383119767)

**MGE/MITRA**

![Imagem 5: Acessar " Empresa " (Caminho de acesso: MGE/Mitra » Menu » Avançado » Preferencias » Empresa ) Aba: " NFC-e", "Usar QR…](https://ajuda.sankhya.com.br/hc/article_attachments/16447734716439)Acessar "**Empresa**" (Caminho de acesso: MGE/Mitra » Menu » Avançado » Preferencias » Empresa)
Aba: "**NFC-e", "Usar QR Code versao 2.0?"** [marcado]

![Imagem 6: Acessar : " Preferências " (Caminho de acesso: Configurações » Avançado » Preferências )](https://ajuda.sankhya.com.br/hc/article_attachments/16447727572119) Acessar : "**[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)"** (Caminho de acesso: Configurações » Avançado » Preferências)

- **"GERARQRCODEXML"** = Ligado

![Imagem 7: "GERARQRCODEXML" = Ligado](https://ajuda.sankhya.com.br/hc/article_attachments/14387418643863)

![Imagem 8: Após ajustes, gerar novamente a NFC-e.](https://ajuda.sankhya.com.br/hc/article_attachments/16447734728855) Após ajustes, gerar novamente a NFC-e.

Exemplo QRCode versão 2.0 [ Usar QR Code versão 2.0 [x] marcado no Cadastro de Empresa.

**<qrCode>**<![CDATA[http://www4.fazenda.rj.gov.br/consultaNFCe/QRCode?p=33180918299882000101650500000003581582857673|**2**|2|1|A297AB7D38C07CA7C5E880B29FCFCBE054EBCD50]]>**</qrCode>**

Exemplo QRCode versão 1.0 [ Usar QR Code versão 2.0  [  ] desmarcado no Cadastro de Empresa.

**<qrCode>**<![CDATA[http://www4.fazenda.rj.gov.br/consultaNFCe/QRCode?chNFe=33180918299882000101650500000003591704203300&n**Versao=100**&tpAmb=2&cDest=07516882666&dhEmi=323031382d30392d31395431343a30383a32312d30333a3030&vNF=78.00&vICMS=12.64&digVal=433934734877395241744d457972777a30333152644b485735574d3d&cIdToken=000001&cHashQRCode=1fb5873a70fe4d7d4f4007f0f796ff302da6e13b]]>**</qrCode>**

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16447734739735) CAUSA:**

Quando for emitida uma NFC-e (modelo 65) com data de emissão posterior a "30/09/2018" e o parâmetro "Versão" informado no**QR-Code** for **"100"**, haverá a rejeição.

**![Imagem 10: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/16447734744087) OBSERVAÇÕES:**

**(1)** ([NT2016/002](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Y6Lj7G0uHwc=)) - Nota Técnica.

**(1)** Importante estar nas versões mais recentes do SANNFE e SankhyaOM/JivaEvo, de acordo com as versões que estão atualmente disponíveis e em manutenção no site [downloads.sankhya.com.br](http://downloads.sankhya.com.br/) e [downloads.jiva.com.br](https://ajuda.sankhya.com.br/hc/pt-br/articles/downloads.jiva.com.br)

**(1)** A versão do MGE/MITRA ou JIVAG1 que suporta esta configuração é a partir da 4.24.
