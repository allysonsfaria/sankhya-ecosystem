---
id: "37225288165271"
titulo: "E0438 Rejeição: Não é permitido o preenchimento dos campos do grupo de informações relativas à Dedução/Redução do ISSQN, quando o prestador de serviço tiver algum regime especial de tributação."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225288165271-E0438-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-o-preenchimento-dos-campos-do-grupo-de-informa%C3%A7%C3%B5es-relativas-%C3%A0-Dedu%C3%A7%C3%A3o-Redu%C3%A7%C3%A3o-do-ISSQN-quando-o-prestador-de-servi%C3%A7o-tiver-algum-regime-especial-de-tributa%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:04Z"
rotulos: ["Configuração", "SEFAZ", "Impostos", "Prefeituras", "NFS-e", "ISSQN", "Regime especial de tributação do ISS", "Dedução/Redução do ISSQN", "Legislação tributária municipal", "Cálculo do imposto", "Regime esp. trib. ISS (NFS-e)", "Nota Fiscal de Serviços Eletrônica (NFS-e)"]
---

# E0438 Rejeição: Não é permitido o preenchimento dos campos do grupo de informações relativas à Dedução/Redução do ISSQN, quando o prestador de serviço tiver algum regime especial de tributação.

**MENSAGEM**

E0438 Rejeição: Não é permitido o preenchimento dos campos do grupo de informações relativas à Dedução/Redução do ISSQN, quando o prestador de serviço tiver algum regime especial de tributação.

**SITUAÇÃO**

Ao emitir uma Nota Fiscal de Serviços Eletrônica (NFS-e), o sistema rejeitou o documento e retornou a mensagem de erro E0438, impedindo a autorização da nota fiscal.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela [**"Empresa"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608254-Empresa) (Comercial » Preferências » Empresa).

**(2)** Na aba **''Documentos Fiscais Eletrônicos''**, sub-aba **"NFS-e"**, sub-aba **''Geral''**.

**(3)** Verifique o campo **"Regime esp. trib. ISS (NFS-e)"** e identifique se há algum **regime especial de tributação** configurado, como:

- Microempresa municipal
- Estimativa
- Sociedade de profissionais
- Cooperativa
- Exigibilidade Suspensa por Decisão Judicial
- Exigibilidade Suspensa por Procedimento Administrativo
- MEI (Simples Nacional)
- Outros regimes especiais específicos do município

**(4)** Caso a empresa possua regime especial de tributação, **não preencha os campos relacionados à dedução ou redução do ISSQN** na emissão da NFS-e.

**(5)** Se a empresa **não deveria estar configurada com regime especial**, altere o campo **"Regime esp. trib. ISS (NFS-e)"** para a opção adequada, como **"Tributável"** ou outra opção que não caracterize regime especial.

**(6)** Acesse a tela **"Ajustes de Apuração do ISSQN"** (Livros Fiscais » Avançado » Super Sintegra » Ajustes de Apuração do ISSQN) e verifique se há **lançamentos de deduções** registrados indevidamente.

**(7)** Caso existam lançamentos de dedução e a empresa possua regime especial, **remova ou ajuste esses lançamentos** para que não sejam enviados na NFS-e.

**(8)** Após realizar os ajustes necessários, **emita novamente a NFS-e** sem informar deduções ou reduções do ISSQN.

**CAUSA**

A rejeição ocorre porque a **legislação tributária municipal não permite** que empresas com **regime especial de tributação do ISS** utilizem deduções ou reduções na base de cálculo do ISSQN. Quando a empresa está enquadrada em regimes como Microempresa Municipal, Estimativa, Sociedade de Profissionais, Cooperativa ou possui Exigibilidade Suspensa, o **cálculo do imposto segue regras específicas** que não admitem o preenchimento dos campos do grupo de dedução/redução. O sistema da Sefaz valida essa incompatibilidade e rejeita a nota quando identifica que ambas as informações foram enviadas simultaneamente.
