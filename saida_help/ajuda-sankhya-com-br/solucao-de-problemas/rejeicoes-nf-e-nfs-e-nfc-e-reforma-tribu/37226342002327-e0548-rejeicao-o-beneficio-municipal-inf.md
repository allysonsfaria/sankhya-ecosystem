---
id: "37226342002327"
titulo: "E0548 Rejeição: O Benefício Municipal informado na DPS não permite benefício para prestadores de serviço que não estejam estabelecidos no município de incidência do ISSQN."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226342002327-E0548-Rejei%C3%A7%C3%A3o-O-Benef%C3%ADcio-Municipal-informado-na-DPS-n%C3%A3o-permite-benef%C3%ADcio-para-prestadores-de-servi%C3%A7o-que-n%C3%A3o-estejam-estabelecidos-no-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:05Z"
rotulos: ["Configuração", "Impostos", "Prefeituras", "NFS-e", "ISSQN", "Benefício fiscal municipal", "Município de incidência do ISSQN", "NFS-e (Nota Fiscal de Serviços Eletrônica)", "Benefício fiscal municipal informado na DPS"]
---

# E0548 Rejeição: O Benefício Municipal informado na DPS não permite benefício para prestadores de serviço que não estejam estabelecidos no município de incidência do ISSQN.

**MENSAGEM**

E0548 Rejeição: O Benefício Municipal informado na DPS não permite benefício para prestadores de serviço que não estejam estabelecidos no município de incidência do ISSQN.

**SITUAÇÃO**

Ao tentar emitir uma NFS-e (Nota Fiscal de Serviços Eletrônica) para prestação de serviço fora do município onde a empresa está estabelecida, informando um **benefício fiscal municipal** na DPS (Declaração de Prestação de Serviços), a mensagem de rejeição é apresentada.

**SOLUÇÃO**

Para resolver esta rejeição, siga o passo a passo abaixo:

**(1)** Confirme se a **empresa prestadora do serviço está estabelecida no município de incidência do ISSQN**. Caso não esteja, **o benefício fiscal municipal não poderá ser aplicado**.

**(2)** Acesse a tela **''Serviço''** (Configurações » Cadastros » Produtos » Serviço).

**(3)** Localize o serviço que está sendo prestado.

**(4)** **Revise as configurações de tributação do ISS**, verifique especialmente:

- O **Regime Especial de Tributação do ISS** configurado no cadastro da empresa.
- A **Cidade de Prestação do Serviço** informada na **Central de Vendas**.
- O **benefício fiscal municipal** aplicado na nota.

**(5)** Caso a empresa **não esteja estabelecida no município de incidência**, **remova o benefício fiscal municipal da NFS-e** ou ajuste a configuração para que **não seja aplicado benefício** indevidamente.

**(6)** Acesse a tela [**''Tipos de Operação - TOP''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

**(7)** Na aba **''NFS-e''**, verifique o campo **''Cód. Natureza Oper. ISS (NFS-e)''**, garantindo que esteja configurado corretamente conforme a operação.

**(8)** Acesse a tela [**''Cidades''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades), e verifique nos campos **''Mun. domicílio fiscal''** e **''Cód. município SIAFI''**, se o Município de incidência está corretamente informado.

**(9)** Consulte o **manual da Prefeitura do município** para confirmar se o **benefício fiscal informado é permitido** para **prestadores de serviço não estabelecidos** no município.

**(10)** Após realizar os ajustes necessários, **emita novamente a NFS-e** e verifique se a rejeição foi solucionada.

**CAUSA**

A rejeição ocorre porque o **benefício fiscal municipal informado na DPS** é restrito a prestadores de serviço que estejam **estabelecidos no município de incidência do ISSQN**. Quando a empresa prestadora não possui estabelecimento no município onde o imposto incide, a legislação municipal não permite a aplicação do benefício, resultando na rejeição da nota fiscal pela prefeitura.
