---
id: "37222609656215"
titulo: "E0202 Rejeição: Na emissão da NFS-e não é permitido que o prestador do serviço seja igual ao tomador do serviço."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222609656215-E0202-Rejei%C3%A7%C3%A3o-Na-emiss%C3%A3o-da-NFS-e-n%C3%A3o-%C3%A9-permitido-que-o-prestador-do-servi%C3%A7o-seja-igual-ao-tomador-do-servi%C3%A7o"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:37Z"
rotulos: ["Configuração", "Parceiro", "Prefeituras", "NFS-e", "Passos para resolver", "Erro", "Como Resolver", "CNPJ ou CPF", "Tomador do serviço", "CNPJ/CPF do tomador", "Prestador do serviço"]
---

# E0202 Rejeição: Na emissão da NFS-e não é permitido que o prestador do serviço seja igual ao tomador do serviço.

**MENSAGEM**

E0202 Rejeição: Na emissão da NFS-e não é permitido que o prestador do serviço seja igual ao tomador do serviço.

**SITUAÇÃO**

Ao tentar emitir uma **Nota Fiscal de Serviço Eletrônica (NFS-e)**, o sistema retorna a rejeição acima, indicando que **o prestador e o tomador do serviço são a mesma empresa**.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas) e localize a nota fiscal que apresentou a rejeição.

**(2)** Na grade **''Cabeçalho''**, verifique o campo **''Parceiro''** informado como tomador se serviço na nota.

**(3)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e consulte o cadastro do parceiro informado como tomador.

**(4)** Na aba ''**Identificação''**, verifique se o campo ''**CNPJ / CPF''** do tomador está diferente do **CNPJ/CPF da empresa prestadora**.

- Corrija o cadastro do parceiro, informando o **CNPJ/CPF correto do tomador**;
- Ou selecione o **parceiro correto** na nota fiscal, caso tenha informado o parceiro errado.

**(5)** Após realizar a correção, cancele a nota rejeitada, caso já tenha sido transmitida, ou exclua o lote, se ainda não tiver ocorrido a transmissão.

**(6)** Gere novamente a NFS-e com as informações corretas do tomador do serviço.

**CAUSA**

A rejeição E0202 ocorre porque **a legislação tributária municipal não permite que uma empresa emita nota fiscal de serviço para si mesma**. O sistema identifica que o **CNPJ/CPF do prestador** (empresa emissora) é **igual ao CNPJ/CPF do tomador** (cliente), caracterizando uma operação inválida. Esta validação é realizada pela **prefeitura no momento da transmissão da NFS-e**, impedindo a emissão de notas fiscais onde prestador e tomador sejam a mesma pessoa jurídica ou física.
