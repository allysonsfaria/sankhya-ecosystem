---
id: "37226156955159"
titulo: "E0585 Rejeição: Somente é permitido informar suspensão de exigibilidade quando a opção da tributação do ISSQN for uma operação tributável (tribISSQN = 1)."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226156955159-E0585-Rejei%C3%A7%C3%A3o-Somente-%C3%A9-permitido-informar-suspens%C3%A3o-de-exigibilidade-quando-a-op%C3%A7%C3%A3o-da-tributa%C3%A7%C3%A3o-do-ISSQN-for-uma-opera%C3%A7%C3%A3o-tribut%C3%A1vel-tribISSQN-1"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:14Z"
rotulos: ["Configuração", "Alíquota de ISS", "SEFAZ", "Impostos", "NFS-e", "Cód. Natureza Oper. ISS (NFS-e)", "Tributação do ISSQN for uma operação tributável", "Cód. Tributação ISS", "Suspensão de exigibilidade do ISS", "Natureza de operação com suspensão de exigibilidade"]
---

# E0585 Rejeição: Somente é permitido informar suspensão de exigibilidade quando a opção da tributação do ISSQN for uma operação tributável (tribISSQN = 1).

**MENSAGEM**

E0585 Rejeição: Somente é permitido informar suspensão de exigibilidade quando a opção da tributação do ISSQN for uma operação tributável (tribISSQN = 1).

**SITUAÇÃO**

Ao emitir uma NFS-e, o documento foi rejeitado pela SEFAZ com a mensagem relacionada à suspensão de exigibilidade do ISS.

**SOLUÇÃO**

**(1)** Acesse a tela **"Tipos de Operação - TOP"** (Configurações » Cadastros » Tipos de Operação) e localize o TOP utilizado na emissão da NFS-e.

**(2)** Acesse a aba **"NFS-e"** e verifique o campo **"Cód. Natureza Oper. ISS (NFS-e)"**.

**(3)** Certifique-se de que o **"Cód. Tributação ISS"** na grade de itens da nota esteja configurado como **"00 - Tributado"** ou **"01 - Tributado com ISS Retido"**, conforme a operação.

**(4)** Caso o **"Cód. Natureza Oper. ISS (NFS-e)"** esteja configurado com uma opção de **suspensão de exigibilidade** (como códigos 4, 5, 6 ou 7, dependendo do município), confirme que o **"Cód. Tributação ISS"** seja uma **operação tributável**.

**(5)** Se a operação **não for tributável** (como "06 - Isento" ou "07 - Não Tributado"), altere o **"Cód. Natureza Oper. ISS (NFS-e)"** para uma opção compatível, como **"Isenção"**, **"Imune"** ou **"Não incidência"**, conforme as opções permitidas pelo município.

**(6)** Reemita a NFS-e com as configurações corrigidas.

**CAUSA**

A rejeição ocorre porque foi informada uma **natureza de operação com suspensão de exigibilidade** no campo **"Cód. Natureza Oper. ISS (NFS-e)"**, mas o **"Cód. Tributação ISS"** não está configurado como **operação tributável**. A Sefaz exige que a suspensão de exigibilidade seja aplicada **somente em operações tributáveis**, ou seja, quando o **"Cód. Tributação ISS"** for **"00 - Tributado"** ou **"01 - Tributado com ISS Retido"**. Operações isentas, imunes ou não tributadas **não podem ter suspensão de exigibilidade**, pois não há tributo a ser suspenso.
