---
id: "37225576584599"
titulo: "E0455 Rejeição: Informe uma chave de NFS-e válida."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225576584599-E0455-Rejei%C3%A7%C3%A3o-Informe-uma-chave-de-NFS-e-v%C3%A1lida"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:52Z"
rotulos: ["Configuração", "XML", "Prefeituras", "NFS-e", "Erro", "Chave de NFS-e", "Chave de acesso da NFS-e", "Chave de NFS-e válida", "Informe uma chave NFS-e", "Download de XML", "Documentos Eletrônicos"]
---

# E0455 Rejeição: Informe uma chave de NFS-e válida.

**MENSAGEM**

E0455 Rejeição: Informe uma chave de NFS-e válida.

**SITUAÇÃO**

Ao tentar realizar operações com NFS-e, como **consulta, cancelamento, substituição ou download de XML**, o sistema apresenta a mensagem de rejeição informando que a **chave da NFS-e informada não é válida**.

**SOLUÇÃO**

Para solucionar esta rejeição, siga os passos abaixo:

**(1)** Verifique se a **chave de acesso da NFS-e** foi informada corretamente. A chave deve conter **todos os dígitos necessários** conforme o padrão estabelecido pela prefeitura emissora.

**(2)** Acesse a tela **"Download de Arquivos XML"** (Comercial » Rotinas » Download de Arquivos XML) e no campo **"Tipo Arquivo"** selecione a opção **"NFS-e"**.

**(3)** Localize a nota fiscal de serviço desejada e **copie a chave de acesso completa** diretamente do sistema ou do arquivo XML da nota.

**(4)** Caso esteja tentando **referenciar uma NFS-e** em outra operação, certifique-se de que:

- A nota fiscal de serviço foi **efetivamente autorizada** pela prefeitura;
- A chave informada corresponde a uma **NFS-e válida e não cancelada**;
- O **formato da chave** está de acordo com o padrão do município emissor.

**(5)** Se a NFS-e foi emitida pelo **Padrão Nacional**, verifique na tela **"Empresa"** (Comercial » Preferências » Empresa), na aba **"Documentos Fiscais Eletrônicos"**, sub-aba **"NFS-e"**, sub-aba **''Geral''** se a opção **"Emitir NFS-e Padrão Nacional"** está habilitada corretamente.

**(6)** Valide se o **município da empresa** está configurado corretamente na tela **"Cidades"** (Configurações » Cadastros » Cidades), verificando os campos **"Mun. domicílio fiscal"** e **"Cód. município SIAFI"**.

**(7)** Caso a chave tenha sido **digitada manualmente**, revise caractere por caractere para garantir que não há **erros de digitação, espaços em branco ou caracteres especiais indevidos**.

**(8)** Se o problema persistir, consulte o **portal da prefeitura** do município emissor para verificar se a nota fiscal de serviço está **devidamente registrada e autorizada** no sistema da administração tributária municipal.

**CAUSA**

A rejeição ocorre quando a **chave de acesso da NFS-e informada** não atende aos critérios de validação estabelecidos pela prefeitura. As principais causas incluem:

- **Chave de acesso digitada incorretamente**, com erros de digitação ou caracteres faltantes;
- **Chave incompleta**, sem todos os dígitos necessários;
- **Chave de uma NFS-e que foi cancelada** ou substituída;
- **Chave inexistente** na base de dados da prefeitura;
- **Formato da chave incompatível** com o padrão do município emissor;
- **Tentativa de referenciar uma nota** que ainda não foi processada ou autorizada pela administração tributária municipal.
