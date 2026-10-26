---
id: "37225524007703"
titulo: "E0449 Rejeição: Código de serviço informado na DPS não permite dedução/redução na base de cálculo do ISSQN por documento informado."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225524007703-E0449-Rejei%C3%A7%C3%A3o-C%C3%B3digo-de-servi%C3%A7o-informado-na-DPS-n%C3%A3o-permite-dedu%C3%A7%C3%A3o-redu%C3%A7%C3%A3o-na-base-de-c%C3%A1lculo-do-ISSQN-por-documento-informado"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:53Z"
rotulos: ["Configuração", "Impostos", "Prefeituras", "NFS-e", "ISSQN", "manual da Prefeitura do Município", "Código de serviço", "Dedução ou redução na base de cálculo do ISSQN", "Legislação municipal", "Tipo de dedução de base do ISS", "Não permite dedução ou redução na base de cálculo do ISSQN"]
---

# E0449 Rejeição: Código de serviço informado na DPS não permite dedução/redução na base de cálculo do ISSQN por documento informado.

**MENSAGEM**

E0449 Rejeição: Código de serviço informado na DPS não permite dedução/redução na base de cálculo do ISSQN por documento informado.

**SITUAÇÃO**

Ao emitir uma **NFS-e**, o sistema apresenta a mensagem de rejeição informando que o código de serviço utilizado **não permite dedução ou redução na base de cálculo do ISSQN**, mesmo que tenha sido configurado algum percentual de dedução ou redução no documento fiscal.

**SOLUÇÃO**

**(1)** Acesse a tela **"Serviço"** (Configurações » Cadastros » Produtos » Serviço).

**(2)** Localize o serviço utilizado no documento fiscal rejeitado.

**(3)** Verifique o campo **"Cód. Tributação ISS"** e identifique qual código está configurado:

- **''07 - Não Tributado''**
- **''06 - Isento''**
- **''00 - Tributado''**
- **''01 - Tributado com ISS Retido''**

**(4)** Verifique se o campo **"Perc. de dedução na base do ISS"** está preenchido com algum percentual de dedução ou redução.

**(5)** Consulte o **manual da Prefeitura do município** onde o serviço está sendo prestado para verificar se o código de serviço utilizado permite dedução ou redução na base de cálculo do ISSQN.

**(6)** Caso o código de serviço **não permita dedução/redução**, realize **um dos seguintes ajustes**:

- Remova o percentual informado no campo **"Perc. de dedução na base do ISS"**, deixando-o zerado
- Altere o campo **"Tipo de dedução de base do ISS"** para uma opção compatível com a legislação municipal
- Utilize um código de serviço diferente que permita a dedução/redução, conforme orientação do seu contador

**(7)** Acesse a tela [**"Tipo de Operação - TOP"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

**(8)** Na aba **"NFS-e"**, verifique o campo **"Desconto Condicionado para NFS-e"**, garantindo que esteja configurado adequadamente.

**(9)** Salve as alterações realizadas e emita novamente a **NFS-e**.

**CAUSA**

A rejeição ocorre porque o **código de serviço** informado no documento fiscal possui configurações de **dedução ou redução na base de cálculo do ISSQN**, porém a **legislação municipal** não permite esse tipo de dedução/redução para o serviço específico. Cada município possui regras próprias sobre quais serviços permitem deduções, e o sistema valida essas informações no momento da emissão da NFS-e, rejeitando documentos que não estejam em conformidade com as regras da Prefeitura.
