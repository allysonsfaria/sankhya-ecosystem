---
id: "360044617293"
titulo: "O campo NIRE é obrigatório quando a escrituração possui registro na Junta Comercial. Caso contrário, o campo não deve ser preenchido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617293-O-campo-NIRE-%C3%A9-obrigat%C3%B3rio-quando-a-escritura%C3%A7%C3%A3o-possui-registro-na-Junta-Comercial-Caso-contr%C3%A1rio-o-campo-n%C3%A3o-deve-ser-preenchido"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:53:10Z"
rotulos: ["#criadoRoger", "Configuração", "ECD", "Fiscal", "Campo NIRE obrigatório se registrado na Junta Comercial.", "Configure \"Indicador de existência NIRE\" e gere o arquivo ECD.", "Preencha campos \"Reg. Junta Comercial (NIRE)\" e \"Data Registro\".", "Junta Comercial", "NIRE"]
---

# O campo NIRE é obrigatório quando a escrituração possui registro na Junta Comercial. Caso contrário, o campo não deve ser preenchido

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16981615645975) MENSAGEM:**

O campo NIRE é obrigatório quando a escrituração possui registro na Junta Comercial. Caso contrário, o campo não deve ser preenchido.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16981615644183) SITUAÇÃO:**

Ao tentar transmitir o arquivo ECD, o seguinte erro é apresentado do validador

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16981607462551) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse: Configurações » Cadastros » Empresas](https://ajuda.sankhya.com.br/hc/article_attachments/16981615648535) Acesse: Configurações » Cadastros » Empresas

- Aba: **"Naturezas"**
- Preencha os campos abaixo:
  - **"Reg. Junta Comercial (NIRE)"**
  - "**Data Registro na Junta (NIRE)"**

![Imagem 5: Acesse: Contabilidade » Preferências » Empresa](https://ajuda.sankhya.com.br/hc/article_attachments/16981607464983) Acesse: Contabilidade » Preferências » Empresa

- Aba: **"ECD-Escrituração Contábil Digital"**
- Bloco: **"I"**
  Registro "**I030":** marcado para gerar

![Imagem 6: Acesse: Contabilidade » Conexão » ECD » Geração de Arquivo - ECD](https://ajuda.sankhya.com.br/hc/article_attachments/16981607466007) Acesse: Contabilidade » Conexão » ECD » Geração de Arquivo - ECD

- Aba: **"Parâmetros"**
- Opção **"Indicador de existência NIRE":** 1-Empresa possui NIRE

![Imagem 7: Gere o arquivo da ECD novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16981615656087) Gere o arquivo da ECD novamente.

**![Imagem 8: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16981615659927) OBSERVAÇÃO:**

O Registro I030, além do NIRE, gera outras informações que indicam o Termo de Abertura do Livro.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16981607472279) CAUSA:**

Ocorre quando os dados do NIRE, o registro e a opção na geração, não estão devidamente configurados conforme indicado acima.
