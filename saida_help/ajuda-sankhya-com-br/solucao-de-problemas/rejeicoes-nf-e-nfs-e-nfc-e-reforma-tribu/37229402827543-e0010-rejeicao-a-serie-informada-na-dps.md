---
id: "37229402827543"
titulo: "E0010 Rejeição: A série informada na DPS não pertence à faixa definida para o tipo de emissor utilizado para a sua emissão."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37229402827543-E0010-Rejei%C3%A7%C3%A3o-A-s%C3%A9rie-informada-na-DPS-n%C3%A3o-pertence-%C3%A0-faixa-definida-para-o-tipo-de-emissor-utilizado-para-a-sua-emiss%C3%A3o"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:02Z"
rotulos: ["Configuração", "Prefeituras", "NFS-e", "Erro", "série informada na DPS", "NFS-e Padrão Nacional", "Prefixo Série NFS-e Padrão Nacional", "série da NFS-e", "Documentos Eletrônicos"]
---

# E0010 Rejeição: A série informada na DPS não pertence à faixa definida para o tipo de emissor utilizado para a sua emissão.

**MENSAGEM**

E0010 Rejeição: A série informada na DPS não pertence à faixa definida para o tipo de emissor utilizado para a sua emissão.

**SITUAÇÃO**

Ao tentar emitir uma **NFS-e Padrão Nacional**, o sistema retorna a rejeição informando que a série utilizada na DPS (Declaração de Prestação de Serviços) **não está dentro da faixa permitida** para o tipo de emissor configurado.

**SOLUÇÃO**

Para resolver esta rejeição, ajuste a **série da NFS-e** conforme a faixa permitida para o tipo de emissor:

**(1)** Acesse a tela [**"Empresa"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608254-Empresa) (Comercial » Preferências » Empresa).

**(2)** Na aba **"Documentos Fiscais Eletrônicos"**, sub-aba **''NFS-e''**, sub-aba **''Geral''**.

**(3)** Localize o campo **"Prefixo Série NFS-e Padrão Nacional"** e coloque o prefixo de **número 10,** que corresponde a faixa 00001 a 49999**.**

**Observação:** as faixas estão diretamente relacionadas à versão do prefixo:

- A **faixa 00001 a 49999** corresponde à V2 (prefixo 10), que é a versão mais atual. Essa versão contempla rejeições mais claras e correções adicionais que não foram abrangidas na V1.
- Já **faixa 80000 a 99999** corresponde à V1 (prefixo 80), que é a primeira versão disponibilizada para emissão via Padrão Nacional, e esta possui rejeições menos assertivas, como, por exemplo: “Erro ao inserir valores” e “Erro ao inserir dados da pessoa”.

**CAUSA**

A rejeição ocorre quando a **série informada na DPS** (Declaração de Prestação de Serviços) **não corresponde à faixa definida** pela prefeitura para o tipo de emissor utilizado.
