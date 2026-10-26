---
id: "37228370194967"
titulo: "E0716 Rejeição: Certificado Digital fora do padrão estabelecido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37228370194967-E0716-Rejei%C3%A7%C3%A3o-Certificado-Digital-fora-do-padr%C3%A3o-estabelecido"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:06Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "EMPPADCERTDIG", "Certificado Digital", "Erro", "E0716 Rejeição", "validade do certificado digital", "EMPPADCERTDIG - Empresa padrão para utilização do certificado digital", "Rejeição E0716", "Certificado Digital fora do padrão estabelecido", "ICP-Brasil do certificado", "cadeias de certificação"]
---

# E0716 Rejeição: Certificado Digital fora do padrão estabelecido

**MENSAGEM**

E0716 Rejeição: Certificado Digital fora do padrão estabelecido.

**SITUAÇÃO**

A mensagem de rejeição é apresentada ao tentar **transmitir uma nota fiscal eletrônica** quando o **certificado digital utilizado não está em conformidade** com o padrão ICP-Brasil exigido pela SEFAZ ou quando há problemas na cadeia de certificação.

**SOLUÇÃO**

**(1)**  **Verifique a validade do certificado digital**

- Confirme se o certificado digital não está vencido. Caso esteja, providencie a **renovação junto à Autoridade Certificadora** antes de tentar nova transmissão.

**(2)**  **Verifique o padrão ICP-Brasil do certificado**

- Certifique-se de que o certificado digital utilizado está **em conformidade com o padrão ICP-Brasil**.
- Para emissão de NF-e e NFS-e, utilize certificado digital **e-CNPJ** ou **eNF-e** (A1 ou A3).
- O certificado digital é **válido para toda a empresa**, podendo ser utilizado por todos os estabelecimentos (matriz e filiais).

**(3)**  **Instale as cadeias de certificação**

- Verifique se todas as **cadeias de certificação estão corretamente instaladas** no computador.
- Caso necessário, realize a correção da cadeia de certificado seguindo as orientações disponíveis no site da SEFAZ.

**(4)**  **Configure o certificado digital no sistema**

- Acesse a tela [**"Preferências"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) (Configurações » Avançado » Preferências).
- Busque pelo parâmetro **"EMPPADCERTDIG - Empresa padrão para utilização do certificado digital"**.
- No campo **"Inteiro"**, insira o código da empresa padrão para utilização do certificado digital.
- Realize o **upload do arquivo do certificado digital** (.pfx ou .p12) e insira a **senha de proteção** correspondente.

**(5)**  **Aguarde em caso de instabilidade**

- Se a rejeição persistir, aguarde alguns minutos e tente reenviar o documento, pois pode ser causada por **instabilidade temporária nos servidores da SEFAZ**.

**(6)**  **Valide os dados da nota fiscal**

- Confira se os dados da nota fiscal, como **"CNPJ"** e **"Destinatário"**, estão corretos e completos.
- Valide o arquivo XML para garantir que ele segue o **esquema exigido** não possui erros de formatação ou estrutura.

**CAUSA**

A rejeição ocorre quando o **certificado digital utilizado** não está em conformidade com o **padrão ICP-Brasil**, quando as **cadeias de certificação não estão instaladas** corretamente, quando o **certificado está vencido**, ou quando há **problemas na configuração do certificado** no sistema. Também pode ser causada por **instabilidade temporária nos servidores da SEFAZ** ou por **dados inválidos no arquivo XML** da nota fiscal.
