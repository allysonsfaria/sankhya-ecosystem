---
id: "32451889400343"
titulo: "O preenchimento dos campos Tipo da Guia, UFGuia, Série da Guia e Número da Guia são obrigatórios para essa operação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32451889400343-O-preenchimento-dos-campos-Tipo-da-Guia-UFGuia-S%C3%A9rie-da-Guia-e-N%C3%BAmero-da-Guia-s%C3%A3o-obrigat%C3%B3rios-para-essa-opera%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:31:14Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "TOP", "Passos para resolver", "Razão do erro", "Detalhe do erro", "CORE_E08026", "Série da Guia e Número da Guia são obrigatórios", "para essa operação", "Número de Guia Série de Guia e Tipo de Guia", "O preenchimento dos campos Tipo da Guia", "NT: 2024.003 - v1.01", "Nota Técnica NF-e", "Documentos Eletrônicos"]
---

# O preenchimento dos campos Tipo da Guia, UFGuia, Série da Guia e Número da Guia são obrigatórios para essa operação

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/32451889385367) **MENSAGEM:**

[CORE\_E08026] O preenchimento dos campos Tipo da Guia, UFGuia, Série da Guia e Número da Guia são obrigatórios para essa operação.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/32588740142871) SITUAÇÃO:**

Ao tentar gerar o lote de uma NFe é apresentada a mensagem acima.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/32451889387415)SOLUÇÃO:**

![Imagem 4: Acesse a tela "Empresa" (Comercial » Preferências » Empresa) , em seguida na aba "Documentos Eletrônicos" , sub-aba…](https://ajuda.sankhya.com.br/hc/article_attachments/32588744277015) Acesse a tela **"Empresa"** (Comercial » Preferências » Empresa), em seguida na aba **"Documentos Eletrônicos"**, sub-aba **"NF-e/NFC-e"** e sub-aba **"Nota Técnica NF-e"** e certifique que a **NT: 2024.003 - v1.01, está ativa.**

![Imagem 5: Acesse a tela "Empresa" (Comercial » Preferências » Empresa) , em seguida na aba "Documentos Eletrônicos" , sub-aba…](https://ajuda.sankhya.com.br/hc/article_attachments/32589463415575)

![Imagem 6: Acesse a tela "Configurador de Layout da Nota" (Comercial » Configuração » Configurador de Layout da Nota) e abra o…](https://ajuda.sankhya.com.br/hc/article_attachments/32588740148375) Acesse a tela **"Configurador de Layout da Nota"** (Comercial » Configuração » Configurador de Layout da Nota) e abra o layout referente ao movimento da TOP que está sendo utilizado na emissão da NF-e. Em seguida, adicione no cabeçalho do layout os seguintes campos: **Número de Guia, UF de Emissão, Série de Guia e Tipo de Guia**.

![Imagem 7: Acesse a tela "Configurador de Layout da Nota" (Comercial » Configuração » Configurador de Layout da Nota) e abra o…](https://ajuda.sankhya.com.br/hc/article_attachments/32589509599383)

![Imagem 8: Abra a NF na tela da Central, depois preencha os campos anteriores conforme exemplo abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/32588744280599) Abra a NF na tela da Central, depois preencha os campos anteriores conforme exemplo abaixo:

![Imagem 9: Abra a NF na tela da Central, depois preencha os campos anteriores conforme exemplo abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/32589463418135)

![Imagem 10: Por fim, salve o lançamento da NF-e gere o lote da NF novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/32588744281623) Por fim, salve o lançamento da NF-e gere o lote da NF novamente.

**![Imagem 11: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/32451913749655)CAUSA:**

Conforme definição da [NT 2024.003,](https://www.bing.com/ck/a?!&&p=eeb54c72a95dbdd328bd6d40a64b39f22867f50a37e18f5f3c375e9214f35af4JmltdHM9MTczOTQwNDgwMA&ptn=3&ver=2&hsh=4&fclid=1d04a6cb-f11f-6e81-2bb8-b3e1f0336f71&psq=NT+2024.003&u=a1aHR0cHM6Ly93d3cubmZlLmZhemVuZGEuZ292LmJyL3BvcnRhbC9leGliaXJBcnF1aXZvLmFzcHg_Y29udGV1ZG89ZE1pTVpRaWwlMjBCOD0&ntb=1) essa rejeição ocorre quando há item informado como Animal Vivo, porém não há informação de Guia de Trânsito. Essa informação é validada conforme NCM do produto informado.

Vale destacar que essa regra de validação é opcional e pode ser implementada a critério de cada UF. E ela está em vigor em produção desde de 01/04/2025, conforme estabelecido na NT 2024.003.
