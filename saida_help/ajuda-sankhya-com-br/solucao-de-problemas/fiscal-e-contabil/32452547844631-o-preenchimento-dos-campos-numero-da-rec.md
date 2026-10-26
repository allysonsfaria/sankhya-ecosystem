---
id: "32452547844631"
titulo: "O preenchimento dos campos \"Número da Receita ou Receituário do Agrotóxico / Defensivo Agrícola\" e \"CPF do Responsável Técnico, emitente da receita\" são obrigatórios para essa operação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32452547844631-O-preenchimento-dos-campos-N%C3%BAmero-da-Receita-ou-Receitu%C3%A1rio-do-Agrot%C3%B3xico-Defensivo-Agr%C3%ADcola-e-CPF-do-Respons%C3%A1vel-T%C3%A9cnico-emitente-da-receita-s%C3%A3o-obrigat%C3%B3rios-para-essa-opera%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:31:13Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "TOP", "Passos para resolver", "Razão do erro", "Detalhe do erro", "CPF do Responsável Técnico", "são obrigatórios para essa operação", "CORE_E08025", "Número da Receita", "Receituário do Agrotóxico / Defensivo Agrícola", "emitente da receita", "Documentos Eletrônicos"]
---

# O preenchimento dos campos "Número da Receita ou Receituário do Agrotóxico / Defensivo Agrícola" e "CPF do Responsável Técnico, emitente da receita" são obrigatórios para essa operação

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/32452547831319) **MENSAGEM:**

[CORE\_E08025] "Número da Receita ou Receituário do Agrotóxico / Defensivo Agrícola" e "CPF do Responsável Técnico, emitente da receita" são obrigatórios para essa operação.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/32605415038743) SITUAÇÃO:**

**Ao tentar gerar o lote de uma NFe é apresentada a mensagem acima.**

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/32452516183063)SOLUÇÃO:**

![Imagem 4: Acesse a tela "Empresa" (Comercial » Preferências » Empresa) , em seguida, a aba "Documentos Eletrônicos" , sub-aba…](https://ajuda.sankhya.com.br/hc/article_attachments/32605438928407) Acesse a tela **"Empresa"** (Comercial » Preferências » Empresa), em seguida, a aba **"Documentos Eletrônicos"**, sub-aba **"NF-e/NFC-e"** e sub-aba **"Nota Técnica NF-e"** e certifique-se de que a **NT: 2024.003 - v1.01, está ativa.**

![Imagem 5: Acesse a tela "Empresa" (Comercial » Preferências » Empresa) , em seguida, a aba "Documentos Eletrônicos" , sub-aba…](https://ajuda.sankhya.com.br/hc/article_attachments/32605632539415)

![Imagem 6: Acesse a tela "Configurador de Layout da Nota" ( Comercial » Configuração » Configurador de Layout da Nota ) , abra o…](https://ajuda.sankhya.com.br/hc/article_attachments/32605438929815) Acesse a tela **"Configurador de Layout da Nota"** (Comercial » Configuração » Configurador de Layout da Nota), abra o layout referente ao movimento da TOP que está sendo utilizado na emissão da NF-e. Em seguida, adicione no cabeçalho do layout os seguintes campos: **Número da Receita ou Receituário do Agrotóxico / Defensivo Agrícola** e **CPF do Responsável Técnico, emitente do receituário.**

![Imagem 7: Acesse a tela "Configurador de Layout da Nota" ( Comercial » Configuração » Configurador de Layout da Nota ) , abra o…](https://ajuda.sankhya.com.br/hc/article_attachments/32605632542487)

![Imagem 8: Depois, abra a NF na tela da Central e preencha os campos anteriores conforme exemplo abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/32605438930839) Depois, abra a NF na tela da Central e preencha os campos anteriores conforme exemplo abaixo:

![Imagem 9: Depois, abra a NF na tela da Central e preencha os campos anteriores conforme exemplo abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/32605632544279)

![Imagem 10: Por fim, salve o lançamento da NF e gere o lote da NF novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/32605438932375) Por fim, salve o lançamento da NF e gere o lote da NF novamente. 

**![Imagem 11: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/32452516186263)CAUSA:**

Conforme definição da [**NT** 2024.003,](https://www.bing.com/ck/a?!&&p=eeb54c72a95dbdd328bd6d40a64b39f22867f50a37e18f5f3c375e9214f35af4JmltdHM9MTczOTQwNDgwMA&ptn=3&ver=2&hsh=4&fclid=1d04a6cb-f11f-6e81-2bb8-b3e1f0336f71&psq=NT+2024.003&u=a1aHR0cHM6Ly93d3cubmZlLmZhemVuZGEuZ292LmJyL3BvcnRhbC9leGliaXJBcnF1aXZvLmFzcHg_Y29udGV1ZG89ZE1pTVpRaWwlMjBCOD0&ntb=1) essa informação é validada conforme NCM do produto informado.

Vale destacar que, essa regra de validação é opcional e pode ser implementada a critério de cada UF. E ela está em vigor em produção desde de 01/04/2025, conforme estabelecido na NT 2024.003.
