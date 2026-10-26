---
id: "37226260094231"
titulo: "E0535 Rejeição: Não é permitido informar benefício municipal quando o prestador de serviço tiver um regime especial de tributação, ou seja, o campo que indica o regime especial de tributação é diferente de 0, (regEspTrib = 1, 2, 3, 4, 5 ou 6)."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226260094231-E0535-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-informar-benef%C3%ADcio-municipal-quando-o-prestador-de-servi%C3%A7o-tiver-um-regime-especial-de-tributa%C3%A7%C3%A3o-ou-seja-o-campo-que-indica-o-regime-especial-de-tributa%C3%A7%C3%A3o-%C3%A9-diferente-de-0-regEspTrib-1-2-3-4-5-ou-6"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:11Z"
rotulos: ["ISS", "Configuração", "SEFAZ", "Impostos", "NFS-e", "Benefício fiscal municipal", "Regime especial de tributação do ISS", "Não é possível informar benefício municipal", "Legislação tributária municipal não permite", "Documentos Eletrônicos"]
---

# E0535 Rejeição: Não é permitido informar benefício municipal quando o prestador de serviço tiver um regime especial de tributação, ou seja, o campo que indica o regime especial de tributação é diferente de 0, (regEspTrib = 1, 2, 3, 4, 5 ou 6).

**MENSAGEM**

E0535 Rejeição: Não é permitido informar benefício municipal quando o prestador de serviço tiver um regime especial de tributação, ou seja, o campo que indica o regime especial de tributação é diferente de 0, (regEspTrib = 1, 2, 3, 4, 5 ou 6).

**SITUAÇÃO**

Ao emitir uma NFS-e (Nota Fiscal de Serviços Eletrônica), o usuário configurou simultaneamente um **regime especial de tributação do ISS** (com código 1, 2, 3, 4, 5 ou 6) e informou um **benefício fiscal municipal**. A Sefaz não permite essa combinação, pois quando a empresa possui regime especial de tributação, **não é possível informar benefício municipal** no documento fiscal.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela [**"Empresa"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608254-Empresa) (Comercial » Preferências » Empresa)

**(2)** Na aba **"Documentos Fiscais Eletrônicos"**, sub-aba **"NFS-e"**, sub-aba **"Geral"**.

**(2)** Verifique o campo **"Regime esp. tributação ISS (NFS-e)"** e identifique se está preenchido com algum dos seguintes códigos:

- **''Microempresa municipal''**
- **''Estimativa''**
- **''Sociedade de profissionais''**
- **''Cooperativa''**
- **''Microempresário Individual (MEI)''**
- **''Microempresário e Empresa de Pequeno Porte (ME EPP)''**

**(3)** Ajuste as informações de regime especial e benefício fiscal

Realize uma das seguintes ações, conforme o caso da empresa:

- **Opção 1:** Se a empresa **possui regime especial de tributação**, remova o **benefício fiscal municipal** informado na NFS-e.
- **Opção 2:** Se a empresa **não possui regime especial de tributação**, altere o campo **“Regime esp. tributação ISS (NFS-e)”** para **0 (zero)** ou deixe-o em branco, conforme permitido pelo município.

**(4)** Consulte o contador responsável para verificar a **situação tributária correta da empresa** e confirmar qual configuração deve ser mantida no sistema.

**(5)** Após realizar todos os ajustes, emita novamente a NFS-e para validar se a rejeição foi solucionada.

**CAUSA**

A rejeição ocorre porque a **legislação tributária municipal não permite** que uma empresa que já possui regime especial de tributação do ISS (como MEI, Microempresa Municipal, Estimativa, entre outros) informe simultaneamente um benefício fiscal municipal na NFS-e. Essa é uma **regra de validação da Sefaz** que impede a duplicidade de tratamentos tributários especiais no mesmo documento fiscal. Quando o campo **"Regime esp. tributação ISS (NFS-e)"** está preenchido com valores de 1 a 6, o sistema não deve enviar informações de benefício municipal, pois isso caracteriza uma **inconsistência fiscal**.
