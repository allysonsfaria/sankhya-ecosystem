---
id: "37229532377879"
titulo: "E0284 Rejeição: O intermediário de serviço, quando emitente da DPS, somente pode ser identificado pelo CNPJ ou CPF."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37229532377879-E0284-Rejei%C3%A7%C3%A3o-O-intermedi%C3%A1rio-de-servi%C3%A7o-quando-emitente-da-DPS-somente-pode-ser-identificado-pelo-CNPJ-ou-CPF"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:13:57Z"
rotulos: ["Configuração", "Parceiro", "SEFAZ", "NFS-e", "Erro", "Intermediário de serviço", "DPS (Documento de Prestação de Serviços)", "CNPJ ou CPF válido", "Intermediador", "Identificação do intermediário", "DPS é emitida por um intermediário de serviço"]
---

# E0284 Rejeição: O intermediário de serviço, quando emitente da DPS, somente pode ser identificado pelo CNPJ ou CPF.

**MENSAGEM**

E0284 Rejeição: O intermediário de serviço, quando emitente da DPS, somente pode ser identificado pelo CNPJ ou CPF.

**SITUAÇÃO**

Ao emitir uma **DPS (Documento de Prestação de Serviços)** em que a empresa atua como **intermediário de serviço**, o sistema rejeitará o documento caso a **identificação do intermediário** não esteja preenchida com **CNPJ ou CPF válido**.

**SOLUÇÃO**

Para resolver a rejeição **E0284**, siga os passos abaixo:

**(1)** Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas) e localize o documento que apresentou a rejeição.

**(2)** Na grade **''Cabeçalho''**, verifique se o campo **"Intermediador da Transação"** está preenchido corretamente:

- Certifique-se de que o **CNPJ** ou **CPF** do intermediário está informado;
- Confirme que o **CNPJ ou CPF** está válido e ativo;
- Não utilize outros tipos de identificação além de CNPJ ou CPF.

**(3)** Caso o **intermediário** não esteja cadastrado, acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e realize o cadastro completo do intermediário, incluindo:

- **CNPJ ou CPF** válido;
- Dados cadastrais completos e atualizados.

**(4)** Retorne à tela de emissão da **DPS** e atualize as informações do **intermediário** com o **CNPJ ou CPF** correto.

**(5)** Salve as alterações realizadas no documento.

**(6)** Tente emitir novamente a **DPS** e verifique se a rejeição foi solucionada. 

**CAUSA**

A rejeição **E0284** ocorre quando a **DPS é emitida por um intermediário de serviço** e a **identificação do intermediário** não está preenchida com **CNPJ ou CPF válido**. Conforme as regras de validação da Sefaz estabelecidas pela **Lei Complementar nº 214/2025**, no contexto da **Reforma Tributária**, quando o intermediário atua como emitente da DPS, é **obrigatório** que ele seja identificado exclusivamente por **CNPJ ou CPF**, não sendo permitidos outros tipos de identificação. A ausência ou incorreção dessa informação impede a autorização do documento fiscal.
