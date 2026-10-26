---
id: "37226586816407"
titulo: "E0650 Rejeição: Em caso de importação de serviço pelo tomador, o ISSQN deve ser retido pelo tomador."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226586816407-E0650-Rejei%C3%A7%C3%A3o-Em-caso-de-importa%C3%A7%C3%A3o-de-servi%C3%A7o-pelo-tomador-o-ISSQN-deve-ser-retido-pelo-tomador"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:50Z"
rotulos: ["Configuração", "Importação", "TOP", "Prefeituras", "NFS-e", "ISSQN", "ISSQN não foi configurado para retenção", "Cidade do ISS conforme CNAE empresa", "Operação de importação de serviço", "NFS-e de importação de serviço"]
---

# E0650 Rejeição: Em caso de importação de serviço pelo tomador, o ISSQN deve ser retido pelo tomador.

**MENSAGEM**

E0650 Rejeição: Em caso de importação de serviço pelo tomador, o ISSQN deve ser retido pelo tomador.

**SITUAÇÃO**

Ao tentar emitir uma **NFS-e de importação de serviço**, o sistema apresenta a rejeição acima, indicando que o **ISSQN não foi configurado para retenção pelo tomador** do serviço.

**SOLUÇÃO**

**(1)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e localize a **TOP utilizada na emissão da NFS-e**.

**(2)**  Acesse a aba **"NFS-e"** e verifique o campo **"Local de Tributação"**:

- Para **importação de serviço**, selecione a opção **"Exterior"**;
- Esta configuração fará com que a tag <Tributacao> no XML seja preenchida com o valor **"E"**, indicando tributação no exterior.

**(3)** Ainda na aba **"NFS-e"**, localize o campo **"ISSQN Retido"** e configure-o para **"1 - Com retenção de ISSQN"**, garantindo que o **tomador do serviço retenha o imposto**.

**(4)** Verifique se o parâmetro **"Cidade do ISS conforme CNAE empresa? - CIDISSCNAEEMP"** está **ativado** no sistema, pois ele é necessário para que as opções de **local de tributação** sejam utilizadas corretamente.

**(5)** Caso a empresa prestadora esteja no **exterior**, certifique-se de que o **cadastro do parceiro** (Configurações > Cadastros > Parceiros) possua o **CNPJ do exterior** devidamente informado.

**(6)** Salve as alterações e **reemita a NFS-e** com as configurações corretas de **retenção de ISSQN pelo tomador**. 

**CAUSA**

A rejeição E0650 ocorre quando a empresa está realizando uma **operação de importação de serviço** e o sistema identifica que o **ISSQN não está configurado para retenção pelo tomador**. Conforme a legislação tributária, **em operações de importação de serviço, o tomador é responsável pela retenção e recolhimento do ISSQN**. Se o campo **"ISSQN Retido"** não estiver marcado como **"1 - Com retenção"** ou se o **"Local de Tributação"** não estiver configurado como **"Exterior"**, a prefeitura rejeitará a NFS-e com esta mensagem, exigindo a **adequação da configuração fiscal** antes da emissão do documento.
