---
id: "37229390768919"
titulo: "E0044 Rejeição: NFS-e não existe na base de dados do autorizador de NFS-e nacional. Informe uma chave de NFS-e existente."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37229390768919-E0044-Rejei%C3%A7%C3%A3o-NFS-e-n%C3%A3o-existe-na-base-de-dados-do-autorizador-de-NFS-e-nacional-Informe-uma-chave-de-NFS-e-existente"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:01Z"
rotulos: ["Portal de Vendas", "Prefeituras", "NFS-e", "Erro", "NFS-e nacional", "chave da NFS-e não foi localizada", "Status NFS-e\"", "chave de NFS-e que não existe", "NFS-e não existe na base de dados", "Chave de NFS-e existente", "substituição ou cancelamento", "transmissão da NFS-e", "Documentos Eletrônicos"]
---

# E0044 Rejeição: NFS-e não existe na base de dados do autorizador de NFS-e nacional. Informe uma chave de NFS-e existente.

**MENSAGEM:**

E0044 Rejeição: NFS-e não existe na base de dados do autorizador de NFS-e nacional. Informe uma chave de NFS-e existente.

**SITUAÇÃO:**

Ao tentar realizar uma operação de **substituição ou cancelamento** de uma NFS-e emitida no padrão nacional, o sistema apresenta a mensagem de rejeição informando que a **chave da NFS-e não foi localizada** na base de dados do autorizador nacional.

**SOLUÇÃO:**

**(1)** Acesse a tela [**''Portal de Vendas''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) (Comercial » Consulta » Portal de Vendas).

**(2)** Localize a nota fiscal que deseja substituir ou cancelar.

**(3)** Verifique o campo **"Status NFS-e"** da nota para garantir que ela está com status de **"Aprovada"** ou **"Autorizada"**.

**(4)** Caso a nota não esteja autorizada, realize novamente a **transmissão da NFS-e** para o portal nacional antes de tentar executar a operação de substituição ou cancelamento.

**(5)** Se a nota estiver autorizada, mas a rejeição persistir, aguarde alguns minutos e tente novamente, pois pode haver um **delay na sincronização** entre o sistema e a base de dados do autorizador nacional.

**(6)** Consulte diretamente no **portal da prefeitura** se a NFS-e consta como autorizada e se a chave está correta.

**(7)** Compare a chave exibida no portal com a chave registrada no sistema Sankhya.

**(8)** Após confirmar que a chave está correta e a nota está autorizada, realize novamente a operação de substituição ou cancelamento no sistema.

**CAUSA**

A rejeição ocorre quando o sistema tenta realizar uma operação (substituição ou cancelamento) utilizando uma **chave de NFS-e que não existe** ou **não está registrada** na base de dados do autorizador nacional. Isso pode acontecer por:

- A NFS-e não ter sido **efetivamente autorizada** pela prefeitura no portal nacional;
- A **chave informada estar incorreta** ou incompleta;
- Haver um **delay na sincronização** entre o sistema e a base de dados do autorizador;
- A nota ter sido **rejeitada anteriormente** e não constar como autorizada no portal nacional.
