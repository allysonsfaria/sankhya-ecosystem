---
id: "37226335452439"
titulo: "E0541 Rejeição: Não existe o código de identificação do benefício municipal informado na DPS para o município de incidência do ISSQN."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226335452439-E0541-Rejei%C3%A7%C3%A3o-N%C3%A3o-existe-o-c%C3%B3digo-de-identifica%C3%A7%C3%A3o-do-benef%C3%ADcio-municipal-informado-na-DPS-para-o-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-09-28T20:13:49Z"
rotulos: ["Configuração", "Impostos", "Prefeituras", "NFS-e", "ISSQN", "Artigo atualizado KCS", "Declaração de Prestação de Serviços (DPS)", "NFS-e (Nota Fiscal de Serviços Eletrônica)", "Código de identificação do benefício municipal", "Não existe o código de identificação do benefício municipal", "Benefício municipal informado na DPS para o município de incidência do ISSQN", "Prefeitura do município onde o ISSQN está sendo recolhido", "Docs Eletrônicos - KCS"]
---

# E0541 Rejeição: Não existe o código de identificação do benefício municipal informado na DPS para o município de incidência do ISSQN.

**MENSAGEM**

[E0541] Não existe o código de identificação do benefício municipal informado na DPS para o município de incidência do ISSQN.

**SITUAÇÃO**

O erro ocorre na emissão de NFS-e pelo Padrão Nacional quando a DPS leva um número de benefício municipal que o município de incidência do ISSQN não reconhece.

Isso pode acontecer mesmo quando o número parece correto, por exemplo quando ele foi copiado de uma nota fiscal emitida pelo sistema antigo da prefeitura. No Padrão Nacional, o benefício precisa estar cadastrado pelo município no Sistema Nacional NFS-e, e o identificador válido é o gerado nesse cadastro.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Identifique de onde o sistema está buscando o benefício:

- na aba **"Alíquotas de ISS"** no cadastro do Serviço, veja a alíquota vinculada ao serviço da nota;
- se o serviço não tiver alíquota de ISS vinculada e a nota for gerada a partir de um contrato, veja a tela **"Contratos"**.

**(2)** Nesse cadastro, confira o campo **"Número de identificação do Benefício Municipal"**.

**(3)** Confirme com a prefeitura, ou na consulta de parâmetros municipais do portal da NFS-e Nacional, qual é o identificador oficial do benefício para o serviço prestado. Depois:

- **Se o número estiver diferente:** corrija o campo com o identificador oficial.
- **Se o município não tiver o benefício cadastrado no Sistema Nacional:** Necessário procurar a prefeitura para regularizar o cadastro. Enquanto isso, a nota só pode ser emitida sem o benefício.
- **Se a operação não tiver direito ao benefício:** deixe o campo vazio.

**(4)** Confira se o **município de incidência do ISSQN** da nota é o mesmo que concedeu o benefício. Se o ISS for devido a outro município (por exemplo, no local da prestação do serviço), aquele benefício não vale para essa nota.

**(5)** Emita a NFS-e novamente.

**CAUSA**

- **Identificador inválido:** o número informado não corresponde a nenhum benefício cadastrado pelo município no Sistema Nacional NFS-e. Por exemplo, foi usado o código do sistema municipal antigo ou o número da lei que concede o benefício.
- **Benefício não parametrizado:** o município ainda não cadastrou o benefício no Sistema Nacional.
- **Município de incidência diferente:** o benefício existe, mas foi cadastrado por um município diferente daquele a que o ISSQN da nota é devido.
