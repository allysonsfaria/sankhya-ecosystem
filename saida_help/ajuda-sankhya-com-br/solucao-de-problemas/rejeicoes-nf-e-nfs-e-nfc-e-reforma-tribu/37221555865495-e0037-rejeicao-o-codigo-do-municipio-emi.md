---
id: "37221555865495"
titulo: "E0037 Rejeição: O código do município emissor informado na DPS é inexistente no cadastro de convênio municipal do sistema nacional."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37221555865495-E0037-Rejei%C3%A7%C3%A3o-O-c%C3%B3digo-do-munic%C3%ADpio-emissor-informado-na-DPS-%C3%A9-inexistente-no-cadastro-de-conv%C3%AAnio-municipal-do-sistema-nacional"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-09-28T17:49:27Z"
rotulos: ["Configuração", "Cidades", "Prefeituras", "NFS-e", "Erro", "Artigo atualizado KCS", "NFS-e (Nota Fiscal de Serviços Eletrônica)", "Código do município emissor não possui convênio ativo", "Código do município emissor", "Código do município emissor não está cadastrado", "Sistema Nacional de Notas Fiscais de Serviços Eletrônicas", "Docs Eletrônicos - KCS"]
---

# E0037 Rejeição: O código do município emissor informado na DPS é inexistente no cadastro de convênio municipal do sistema nacional.

**SITUAÇÃO**

Esta rejeição ocorre ao tentar **"Emitir NFS-e"** (Nota Fiscal de Serviços Eletrônica) quando o **"Código do município emissor"** informado no documento não está cadastrado ou não possui convênio ativo no Sistema Nacional de Notas Fiscais de Serviços Eletrônicas. Este artigo também orienta sobre as configurações necessárias no sistema Sankhya para emissão de NFS-e quando o município utiliza emissor próprio.

**SOLUÇÃO**

**(1)** Acesse a tela **"Empresas"** (Configurações >> Cadastros >> Empresas) e localize a **"Empresa emissora"** da NFS-e.

**(2)** Na aba **"Endereço"**, no campo **"Cód. Cidade"**, verifique o código cadastrado para a empresa e confirme se o código do município está correto.

**(3)** Acesse a tela **"Cidades"** (Configurações >> Cadastros >> Endereços >> Cidades) e localize o município da empresa emissora.

**(4)** Na aba **"Geral"**, verifique se o campo **"Mun. domicílio fiscal"** está preenchido com o código correto do município conforme a Tabela do IBGE.

- Para consultar o código correto, acesse o site do **"IBGE"**.
- Digite o nome da cidade na pesquisa e localize a informação **"Código do Município"**.

**(5)** Caso o código esteja incorreto, retorne aos passos 3 e 4 e corrija o campo **"Mun. domicílio fiscal"** com a informação obtida no IBGE.

**(6)** Verifique se o **"Município possui convênio ativo"** com o Sistema Nacional de NFS-e.

- Caso o município não esteja conveniado, a emissão deverá ser realizada pelo sistema próprio da prefeitura.

**(7)** Após realizar as correções necessárias, retorne à **"NFS-e rejeitada"** e tente realizar a **"Transmissão novamente"**.

**(8)** Se a rejeição persistir, refaça o lançamento com os dados corretos.

**INFORMAÇÕES ADICIONAIS**

Muitas vezes o erro ocorre porque o Padrão Nacional está habilitado, mas a prefeitura ainda utiliza o sistema próprio. Acesse a tela **"Empresa"** (Comercial >> Preferências >> Empresa), na aba **"Documentos Fiscais Eletrônicos"**, sub-aba **"NFS-e"**, sub-aba **"Geral"**. Caso a sua cidade ainda não migrou, desabilite a opção **"Emitir NFS-e Padrão Nacional"** e remova o campo **"Prefixo Série NFS-e Padrão Nacional"**.

**CAUSA**

Esta rejeição ocorre quando o **"Código do município emissor"** informado na DPS (Declaração de Prestação de Serviços) está incorreto, desatualizado ou não consta no cadastro de convênios municipais do Sistema Nacional. Isso pode acontecer quando:

- O código do município cadastrado na empresa ou na cidade está divergente do código oficial do IBGE.
- O município não possui convênio ativo com o Sistema Nacional de NFS-e.
- Houve erro de digitação no cadastro do código do município.
- O cadastro da cidade está desatualizado no sistema.
- Ocorreu o erro **"E0039"** por manter habilitada a opção **"Emitir NFS-e Padrão Nacional"** em municípios que operam com emissor próprio.
