---
id: "37222898020503"
titulo: "E0234 Rejeição: O endereço do tomador é obrigatório para o indicador de operação informado ou quando a incidência do ISSQN definida para o serviço prestado ocorrer no local do estabelecimento/domicílio do tomador."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222898020503-E0234-Rejei%C3%A7%C3%A3o-O-endere%C3%A7o-do-tomador-%C3%A9-obrigat%C3%B3rio-para-o-indicador-de-opera%C3%A7%C3%A3o-informado-ou-quando-a-incid%C3%AAncia-do-ISSQN-definida-para-o-servi%C3%A7o-prestado-ocorrer-no-local-do-estabelecimento-domic%C3%ADlio-do-tomador"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-08-21T20:20:50Z"
rotulos: ["Configuração", "Parceiro", "TOP", "NFS-e", "ISSQN", "Passos para resolver", "Erro", "Como Resolver", "Incidência do ISSQN", "Endereço do tomador é obrigatório", "Eendereço do tomador não está devidamente cadastrado", "Indicador de presença"]
---

# E0234 Rejeição: O endereço do tomador é obrigatório para o indicador de operação informado ou quando a incidência do ISSQN definida para o serviço prestado ocorrer no local do estabelecimento/domicílio do tomador.

**MENSAGEM**

E0234 Rejeição: O endereço do tomador é obrigatório para o indicador de operação informado ou quando a incidência do ISSQN definida para o serviço prestado ocorrer no local do estabelecimento/domicílio do tomador.

**SITUAÇÃO**

Ao tentar gerar o lote de uma **NFS-e**, o sistema apresenta a mensagem de rejeição informando que **o endereço do tomador é obrigatório** para o tipo de operação configurado ou quando a prestação do serviço ocorre no estabelecimento do tomador.

**SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o cadastro do **tomador do serviço**.

**(2)** Na aba **"Endereço"**, verifique se os dados de endereço estão **devidamente preenchidos**, incluindo:

- **Logradouro**
- **Número**
- **Bairro**
- **Cidade**
- **UF**
- **CEP**

**(3)** Caso o endereço não esteja cadastrado ou esteja incompleto, **preencha todos os campos obrigatórios** do endereço do tomador.

**(4)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

**(5)** Na aba **"NFS-e"**, verifique a configuração do campo **"Local de Tributação"**:

- Se a prestação do serviço ocorre no **estabelecimento do tomador**, selecione a opção **"Cidade do Tomador"**
- Se a prestação ocorre em **local específico**, selecione **"Cidade de Prestação"** e certifique-se de preencher o campo **"Cidade"** no rodapé da nota fiscal

**(6)** Verifique se o parâmetro **"Cidade do ISS conforme CNAE empresa? - CIDISSCNAEEMP"** está **habilitado** para que as configurações de local de tributação sejam aplicadas corretamente.

**(7)** Após realizar os ajustes necessários, **gere o lote da NFS-e novamente**.

**CAUSA**

A rejeição ocorre quando o **endereço do tomador não está devidamente cadastrado** no sistema e a configuração da operação exige essa informação. Isso acontece principalmente em situações onde:

- O **indicador de presença** configurado na TOP exige a identificação do endereço do destinatário (como em operações de entrega em domicílio)
- A **incidência do ISSQN** está configurada para ocorrer no **local do estabelecimento ou domicílio do tomador**, conforme determina o Art. 3º da Lei Complementar nº 116/2003
- O cadastro do parceiro está **incompleto ou utiliza dados genéricos**, sem o preenchimento adequado dos campos de endereço
