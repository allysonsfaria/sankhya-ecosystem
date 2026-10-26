---
id: "37226686033431"
titulo: "E0673 Rejeição: Não pode haver retenção do ISSQN se o intermediário for o emitente da DPS e estiver estabelecido em município diferente do município de incidência do ISSQN."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226686033431-E0673-Rejei%C3%A7%C3%A3o-N%C3%A3o-pode-haver-reten%C3%A7%C3%A3o-do-ISSQN-se-o-intermedi%C3%A1rio-for-o-emitente-da-DPS-e-estiver-estabelecido-em-munic%C3%ADpio-diferente-do-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:44Z"
rotulos: ["Configuração", "Parceiro", "Impostos", "Prefeituras", "NFS-e", "ISSQN", "Cód. Natureza Oper. ISS (NFS-e)", "Legislação tributária municipal", "Não pode haver retenção do ISSQN", "Intermediário da prestação de serviço"]
---

# E0673 Rejeição: Não pode haver retenção do ISSQN se o intermediário for o emitente da DPS e estiver estabelecido em município diferente do município de incidência do ISSQN.

**MENSAGEM**

E0673 Rejeição: Não pode haver retenção do ISSQN se o intermediário for o emitente da DPS e estiver estabelecido em município diferente do município de incidência do ISSQN.

**SITUAÇÃO**

Ao tentar emitir uma NFS-e (Nota Fiscal de Serviços Eletrônica) atuando como **intermediário da prestação de serviço**, o sistema apresenta a mensagem de rejeição E0673. Isso ocorre quando a empresa emitente está estabelecida em um município diferente do município onde ocorre a incidência do ISSQN e, mesmo assim, foi configurada a retenção do imposto.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Verifique se a empresa emitente está cadastrada como **intermediária** na prestação de serviço e se o município de estabelecimento é diferente do município de incidência do ISSQN. Acesse a tela **"Empresa"** (Comercial » Preferências » Empresa) e confira o município cadastrado.

**(2)** Acesse a tela **''Parceiros''** (Configurações » Cadastros » Parceiros), na aba **''Fiscal''**, verifique a configuração do campo **''Retém ISS''**.

**(3)** Caso necessário, **desabilite o campo**. Pois quando a empresa intermediária está estabelecida em município diferente do município de incidência, não é permitida a retenção do imposto.

**(4)** Verifique na tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP), na aba **"NFS-e"**, se o campo **"Cód. Natureza Oper. ISS (NFS-e)"** está configurado corretamente para operações sem retenção.

**(5)** Confirme se o campo **"Cidade"** no rodapé da nota fiscal está preenchido corretamente com o município onde ocorreu a prestação do serviço.

**(6)** Após realizar os ajustes, gere novamente o lote da NFS-e e verifique se a rejeição foi solucionada.

**(7)** Caso necessário, exporte o arquivo XML no Portal de Vendas (NFS-e » Gerar XML do RPS para NFS-e) e verifique se a tag **"ISSRetido"** está preenchida com **"1"** (sem retenção).

**CAUSA**

A rejeição ocorre porque a **legislação tributária municipal não permite** que empresas intermediárias estabelecidas em município diferente do município de incidência do ISSQN efetuem a retenção do imposto. A retenção do ISSQN só pode ser realizada por empresas inscritas no município onde ocorre a incidência tributária. Quando o sistema identifica que há configuração de retenção em uma situação não permitida, a Prefeitura rejeita a NFS-e com a mensagem E0673.
