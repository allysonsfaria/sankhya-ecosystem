---
id: "360044573314"
titulo: "Existem certificados que estão próximos de expirar ou já expiraram, isto pode comprometer as rotinas de geração de Notas Fiscais Eletrônicas (NF-e e NFS-e)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044573314-Existem-certificados-que-est%C3%A3o-pr%C3%B3ximos-de-expirar-ou-j%C3%A1-expiraram-isto-pode-comprometer-as-rotinas-de-gera%C3%A7%C3%A3o-de-Notas-Fiscais-Eletr%C3%B4nicas-NF-e-e-NFS-e"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:51:37Z"
rotulos: ["#Revisadoclaudio", "Configuração", "NF-e", "SEFAZ", "NFS-e", "Sankhya W ou MGE Mitra para troca de certificado", "Certificados digitais próximos ou expirados", "Parâmetro AVISAVCTDIGITAL configura aviso de vencimento", "Certificado Digital", "Erro"]
---

# Existem certificados que estão próximos de expirar ou já expiraram, isto pode comprometer as rotinas de geração de Notas Fiscais Eletrônicas (NF-e e NFS-e)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18611729796503) MENSAGEM:**

Existem certificados que estão próximos de expirar ou já expiraram, isto pode comprometer as rotinas de geração de Notas Fiscais Eletrônicas (NF-e e NFS-e).

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18611729797655) SITUAÇÃO:**

Ao acessar o sistema, é apresentado o aviso, conforme mensagem abaixo:

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18611729801495) SOLUÇÃO:**

Para correção deste erro, seguir os passos abaixo:

- Para clientes que utilizam o **Sankhya W**: [Como realizar troca de certificado digital no Sankhya W ?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043023933)

- Para clientes que utilizam o **MGE Mitra**: [Como realizar a troca de certificado digital - MGE Mitra.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043863794)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18611684503319) CAUSA:**

Quando o certificado digital para emissão de NF-e/NFS-e, está vencido ou próximo ao vencimento, e o parâmetro **"Avisar vencimento do certificado digital - AVISAVCTDIGITAL"** está configurado com valor superior a 0(zero), apresentará o aviso ao acessar o sistema.

**Parâmetro:**

**"Avisar vencimento do certificado digital - AVISAVCTDIGITAL"** (Em Dias)

Se deixar o parâmetro vazio ou 0(zero), não existirá aviso de certificado próximo a expirar ao acessar a Aplicação.
