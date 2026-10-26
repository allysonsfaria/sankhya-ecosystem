---
id: "37221845843863"
titulo: "E0074 Rejeição: Não é permitido realizar a substituição para NFS-e que possua Evento de Tributos Recolhidos vinculado, conforme parametrização do município de incidência do ISSQN. Para mais informações, consultar a Administração Tributária Municipal do mu"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37221845843863-E0074-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-realizar-a-substitui%C3%A7%C3%A3o-para-NFS-e-que-possua-Evento-de-Tributos-Recolhidos-vinculado-conforme-parametriza%C3%A7%C3%A3o-do-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN-Para-mais-informa%C3%A7%C3%B5es-consultar-a-Administra%C3%A7%C3%A3o-Tribut%C3%A1ria-Municipal-do-mu"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:18:20Z"
rotulos: ["Configuração", "Impostos", "Prefeituras", "NFS-e", "ISSQN", "Erro", "Município de incidência do ISSQN", "Substituição de uma NFS-e via webservice", "Evento de Tributos Recolhidos vinculado", "Regra de validação específica da prefeitura", "webservice"]
---

# E0074 Rejeição: Não é permitido realizar a substituição para NFS-e que possua Evento de Tributos Recolhidos vinculado, conforme parametrização do município de incidência do ISSQN. Para mais informações, consultar a Administração Tributária Municipal do mu

**MENSAGEM**

E0074 Rejeição: Não é permitido realizar a substituição para NFS-e que possua Evento de Tributos Recolhidos vinculado, conforme parametrização do município de incidência do ISSQN. Para mais informações, consultar a Administração Tributária Municipal do município emissor da NFS-e.

**SITUAÇÃO**

Ao tentar realizar a **substituição de uma NFS-e via webservice**, o sistema **retorna a rejeição E0074**, impedindo a conclusão do processo de substituição da nota fiscal de serviço.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Verifique se a **NFS-e que será substituída** possui **Evento de Tributos Recolhidos** vinculado. Para isso, consulte o **histórico de eventos da nota fiscal** no sistema ou diretamente no **portal da prefeitura do município emissor**.

**(2)** Caso a nota possua esse evento vinculado, **a substituição via webservice não será permitida**, conforme as regras do município. Nessa situação, avalie as seguintes alternativas:

- Realize o **cancelamento da NFS-e original**, utilizando um dos **motivos autorizados pela prefeitura** (por exemplo: erro na emissão, serviço não prestado ou duplicidade);
- Após o cancelamento, **emita uma nova NFS-e** com as informações corretas;
- Entre em contato com a **Administração Tributária Municipal** e verifique se existe **procedimento específico** aplicável a casos com **Evento de Tributos Recolhidos** vinculado.

**(3)** Se a nota **não possuir Evento de Tributos Recolhidos** e, ainda assim, a rejeição persistir:

- Acesse a tela **“Cidades”** (Configurações » Cadastros » Endereços » Cidades), na aba **“NFS-e”**.
- Verifique se a **opção de substituição via webservice** está corretamente habilitada para o município.

**OBSERVAÇÃO**: A rejeição **E0074** está relacionada às **regras específicas de cada município** quanto à **substituição de NFS-e**. De acordo com a documentação disponível, diversos municípios permitem a substituição de NFS-e via **webservice**. No entanto, essa funcionalidade pode sofrer **restrições**, especialmente quando existem **eventos tributários vinculados** à nota fiscal. Os **códigos de cancelamento** mais comumente aceitos pelos municípios são:

- **1 – Erro na emissão**
- **2 – Serviço não prestado**
- **4 – Duplicidade na nota**

Por fim, é **essencial consultar a Administração Tributária Municipal** do município emissor para confirmar as **regras aplicáveis**, bem como eventuais **limitações e procedimentos alternativos** para a regularização do documento fiscal.

**CAUSA**

A rejeição E0074 ocorre porque o **município de incidência do ISSQN não permite a substituição de NFS-e** quando existe um **Evento de Tributos Recolhidos vinculado** à nota fiscal. Esta é uma **regra de validação específica da prefeitura**, que visa garantir a integridade das informações tributárias já registradas e recolhidas. Quando os tributos já foram recolhidos e registrados através de um evento específico, a substituição da nota poderia gerar inconsistências fiscais, por isso a operação é bloqueada pela Administração Tributária Municipal.
