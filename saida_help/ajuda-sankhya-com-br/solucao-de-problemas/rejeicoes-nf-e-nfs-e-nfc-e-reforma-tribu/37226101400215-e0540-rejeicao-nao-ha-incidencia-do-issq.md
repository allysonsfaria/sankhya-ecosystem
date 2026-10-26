---
id: "37226101400215"
titulo: "E0540 Rejeição: Não há incidência do ISSQN (tribISSQN = 4) pois a parametrização do município de incidência do ISSQN indica que o código de serviço prestado, informado na DPS, não é incidente neste município."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226101400215-E0540-Rejei%C3%A7%C3%A3o-N%C3%A3o-h%C3%A1-incid%C3%AAncia-do-ISSQN-tribISSQN-4-pois-a-parametriza%C3%A7%C3%A3o-do-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN-indica-que-o-c%C3%B3digo-de-servi%C3%A7o-prestado-informado-na-DPS-n%C3%A3o-%C3%A9-incidente-neste-munic%C3%ADpio"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-24T13:29:19Z"
rotulos: ["Configuração", "Cidades", "Impostos", "Alíquotas de ISS", "Prefeituras", "NFS-e", "Código de tributação", "ISSQN", "Não há incidência do ISSQN (tribISSQN = 4)", "Código de tributação do ISS", "Cidade de prestação do serviço", "Código configurado não permite a incidência do ISSQN"]
---

# E0540 Rejeição: Não há incidência do ISSQN (tribISSQN = 4) pois a parametrização do município de incidência do ISSQN indica que o código de serviço prestado, informado na DPS, não é incidente neste município.

**MENSAGEM**

E0540 Rejeição: Não há incidência do ISSQN (tribISSQN = 4) pois a parametrização do município de incidência do ISSQN indica que o código de serviço prestado, informado na DPS, não é incidente neste município.

**SITUAÇÃO**

Ao emitir uma NFS-e, a nota é rejeitada com a mensagem E0540, indicando que o **código de tributação configurado não permite a incidência do ISSQN** no município informado como local de incidência do imposto.

**SOLUÇÃO**

**(1)** Acesse a tela **"Serviço"** (Configurações » Cadastros » Produtos » Serviço).

**(2)** Localize o serviço utilizado na nota fiscal rejeitada.

**(3)** Na aba **"Alíquotas de ISS"**, verifique se o município de incidência do ISSQN está cadastrado corretamente.

**(4)** Certifique-se de que o campo **"Cód. Trib. Município"** está preenchido com o código correto do município onde o serviço será prestado.

**(5)** Verifique se o **“Código de Tributação ISS”** está configurado corretamente para o município informado, observando as regras abaixo:

- Para **serviços com incidência de ISS no município**, utilize códigos que indiquem tributação, como **“T – Tributável”**, **“1 – Tributável”** ou outro código aceito pela prefeitura.
- Para **serviços cuja incidência ocorre fora do município**, confirme se está sendo utilizado um código compatível, como **“7 – Não Incidência no Município”**.

**(6)** Acesse a tela [**“Cidades”**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) (Configurações » Cadastros » Endereços » Cidades) e confirme se o campo **“Mun. Domicílio Fiscal”** está preenchido corretamente com o **código IBGE** do município.

**(7)** Acesse a tela [**“Central de Vendas”**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) (Comercial » Rotinas » Central de Vendas) e verifique se o campo **“Cidade”** está preenchido com o **município correto de incidência do serviço**.

**(8)** Caso o serviço seja prestado em município diferente do domicílio fiscal, certifique-se de que o campo **“Cidade de Prestação do Serviço”** esteja corretamente preenchido na Central de Vendas.

**(9)** Após realizar os ajustes necessários, **redigite os itens da nota fiscal**, salve as alterações e **gere novamente o lote da NFS-e**.

**(10)** Se o erro persistir, consulte o **manual da prefeitura do município** para confirmar se o **código de serviço informado é permitido** e se há **incidência de ISSQN** para aquele município.

**(11)** Se o erro persistir, consulte o **manual da prefeitura do município** para validar se o código de serviço informado é permitido e se há incidência do ISSQN naquele município específico.

**CAUSA**

A rejeição ocorre quando o **código de tributação do ISS** configurado no cadastro de serviços indica que **não há incidência do ISSQN no município** informado como local de prestação do serviço. Isso pode acontecer quando:

- O campo **"Cód. Trib. Município"** não está preenchido ou está incorreto na aba **"Alíquotas de ISS"** do cadastro de serviços.
- O **"Código de Tributação ISS"** utilizado não permite a incidência do imposto no município informado (por exemplo, código **"7 - Não Incidência no Município"**).
- O município de incidência informado na nota fiscal está divergente do município configurado no cadastro de serviços.
- A **cidade de prestação do serviço** não foi informada corretamente na Central de Vendas.
