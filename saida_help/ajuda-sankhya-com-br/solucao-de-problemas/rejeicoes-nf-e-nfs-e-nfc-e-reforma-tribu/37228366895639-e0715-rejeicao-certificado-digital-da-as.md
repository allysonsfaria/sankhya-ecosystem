---
id: "37228366895639"
titulo: "E0715 Rejeição: Certificado Digital da assinatura inválido."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37228366895639-E0715-Rejei%C3%A7%C3%A3o-Certificado-Digital-da-assinatura-inv%C3%A1lido"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-29T14:10:53Z"
rotulos: ["Configuração", "Segurança", "eSocial", "Certificado Digital", "Erro", "Transmitir um evento do eSocial", "Não atende aos requisitos da plataforma", "Certificado Digital da assinatura inválido", "Certificado digital utilizado para assinar o evento"]
---

# E0715 Rejeição: Certificado Digital da assinatura inválido.

**MENSAGEM**

E0715 Rejeição: Certificado Digital da assinatura inválido.

**SITUAÇÃO**

A mensagem de rejeição é apresentada ao tentar **transmitir um evento do eSocial** quando o **certificado digital utilizado para assinar** o evento está inválido, não atende aos requisitos da plataforma ou apresenta problemas em sua estrutura de validação.

**SOLUÇÃO**

**(1)** **Verifique a validade do certificado digital**

- Acesse as propriedades do certificado digital instalado e confirme se ele **não está vencido**.
- Caso o certificado esteja vencido, **providencie a renovação** junto à Autoridade Certificadora antes de realizar nova tentativa de transmissão.

**(2)** **Confirme se o certificado está corretamente instalado**

- Verifique se o **certificado digital está instalado** no repositório correto do sistema operacional.
- Certifique-se de que o certificado é do **tipo A1 ou A3** e está em conformidade com o **padrão ICP-Brasil**.

(3)** Verifique as cadeias de certificação**

- Confirme se todas as **cadeias de certificação intermediárias e raiz** estão corretamente instaladas no computador.
- Caso necessário, realize a **atualização ou reinstalação das cadeias** de certificação conforme orientações da Autoridade Certificadora.

**(4)** **Valide a senha do certificado digital**

- Certifique-se de que a **senha informada** para acesso ao certificado digital está correta.
- Em caso de certificado A3 (token ou cartão), verifique se o **dispositivo está conectado** corretamente ao computador.

**(5)** **Reconfigure o certificado no sistema**

- Acesse a tela **''Certificado Digital''** (Configurações » Cadastros » Certificado Digital).
- Remova o certificado atual e **realize novo cadastro**, informando corretamente o arquivo do certificado e sua senha.

**(6)** **Verifique a integridade do arquivo do certificado**

- Confirme se o **arquivo do certificado digital** (formato .pfx ou .p12) não está corrompido.
- Caso necessário, solicite uma **nova cópia do certificado** junto à Autoridade Certificadora.

**(7)**  **Aguarde e tente novamente**

- Em alguns casos, a rejeição pode ser causada por **instabilidade temporária** nos servidores do eSocial.
- Aguarde alguns minutos e **realize nova tentativa** de transmissão do evento.

**CAUSA**

A rejeição ocorre quando o **certificado digital utilizado para assinar o evento** do eSocial apresenta alguma das seguintes situações: está **vencido**, não está em conformidade com o **padrão ICP-Brasil**, possui **cadeias de certificação ausentes ou incorretas**, o arquivo está **corrompido**, a **senha está incorreta** ou o certificado não está **corretamente instalado** no sistema. Essas condições impedem que a plataforma do eSocial valide a autenticidade e integridade da assinatura digital do evento transmitido.
