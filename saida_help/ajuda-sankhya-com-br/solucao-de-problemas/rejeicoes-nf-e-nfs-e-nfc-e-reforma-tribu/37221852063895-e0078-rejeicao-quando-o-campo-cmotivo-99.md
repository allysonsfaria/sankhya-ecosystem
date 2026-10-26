---
id: "37221852063895"
titulo: "E0078 Rejeição: Quando o campo cMotivo = 99, o campo xMotivo deve ser informado obrigatoriamente."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37221852063895-E0078-Rejei%C3%A7%C3%A3o-Quando-o-campo-cMotivo-99-o-campo-xMotivo-deve-ser-informado-obrigatoriamente"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-09-21T11:28:14Z"
rotulos: ["Central de Notas", "NF-e", "SEFAZ", "Passos para resolver", "Erro", "Como Resolver", "Reforma Tributária", "campo cMotivo", "cMotivo = 99", "Código de motivo \"99 - Outros\"", "Documentos Eletrônicos"]
---

# E0078 Rejeição: Quando o campo cMotivo = 99, o campo xMotivo deve ser informado obrigatoriamente.

**MENSAGEM**

E0078 Rejeição: Quando o campo cMotivo = 99, o campo xMotivo deve ser informado obrigatoriamente.

**SITUAÇÃO**

Ao emitir um documento fiscal eletrônico (NF-e, NFC-e ou CT-e) que contenha informações relacionadas à **Reforma Tributária**, o usuário selecionou o **código de motivo "99 - Outros"** em algum campo específico do documento, mas **não preencheu o campo de descrição** que justifica esse motivo. Como resultado, a nota foi rejeitada pela Sefaz com a mensagem de erro E0078.

**SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

**(1)** Identifique em qual campo do documento fiscal foi selecionado o **"Código de Motivo"** igual a **"99 - Outros"**. Este campo pode estar localizado em diferentes grupos do documento, dependendo da operação realizada.

**(2)** Acesse o documento fiscal rejeitado através da tela **"Central de Notas"** (Comercial » Vendas » Central de Notas) ou **"Central de Compras"** (Comercial » Compras » Central de Compras), conforme o tipo de operação.

**(3)** Localize o campo onde foi informado o **"Código de Motivo"** igual a **"99"**. Este campo geralmente está relacionado a:

- Informações de tributação do IBS e CBS;
- Motivos de desoneração ou benefícios fiscais;
- Situações específicas previstas na Reforma Tributária.

**(4)** No campo **"Descrição do Motivo"** ou **"xMotivo"**, que deve estar logo abaixo ou ao lado do campo **"Código de Motivo"**, **preencha obrigatoriamente a justificativa** detalhada do motivo pelo qual foi selecionada a opção "99 - Outros".

**(5)** Certifique-se de que a descrição informada seja **clara, objetiva e esteja de acordo com a legislação fiscal vigente**, explicando adequadamente a situação que justifica o uso do código "99".

**(6)** Salve as alterações realizadas no documento fiscal.

**(7)** Gere um novo lote do documento fiscal e reenvie-o à Sefaz para validação.

**CAUSA**

A rejeição E0078 ocorre quando, ao emitir um documento fiscal eletrônico, o usuário seleciona o **"Código de Motivo" (cMotivo) igual a "99 - Outros"** em algum campo relacionado à tributação ou situações específicas previstas na **Reforma Tributária**, mas **não preenche o campo "Descrição do Motivo" (xMotivo)**. De acordo com as regras de validação da Sefaz, sempre que o código "99" for utilizado, é **obrigatório informar uma descrição textual** que justifique e explique o motivo dessa seleção, garantindo a transparência e conformidade fiscal da operação.
